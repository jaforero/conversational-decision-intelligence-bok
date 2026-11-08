"""Export the editorial graph from the built canonical pages and their registries."""

from __future__ import annotations

import json
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit

import yaml
from mkdocs.plugins import event_priority


class ArticleLinks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_content = False
        self.links: set[str] = set()

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag == "article" and "md-content__inner" in attributes.get("class", "").split():
            self.in_content = True
        if self.in_content and tag == "a" and attributes.get("href"):
            self.links.add(attributes["href"])

    def handle_endtag(self, tag):
        if tag == "article":
            self.in_content = False


def read_yaml(path: Path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def route_for(path: str) -> str:
    stem = Path(path).relative_to("docs").with_suffix("").as_posix()
    route = f"/{stem}/"
    return route.removesuffix("index/") if route.endswith("/index/") else route


@event_priority(-100)
def on_post_build(config, **kwargs) -> None:
    i18n = config.plugins.get("i18n")
    if i18n is not None and getattr(i18n, "building", False):
        return

    root = Path(config.config_file_path).resolve().parent
    site = Path(config.site_dir)
    governance = root / "governance"
    inventory = read_yaml(governance / "content-map.yml")["public_portal"]["navigation"]
    registries = governance / "registries"
    claims = {row["claim_id"]: row for row in read_yaml(registries / "claims.yml")["claims"]}
    sources = {row["source_id"]: row for row in read_yaml(registries / "sources.yml")["records"]}
    page_ids = {route_for(row["path"]): row["id"] for row in inventory}
    origin = urlsplit(config.site_url).netloc
    nodes = {}
    edges = set()
    inbound_pages = set()

    for row in inventory:
        path = row["path"]
        page_id = row["id"]
        route = route_for(path)
        metadata = yaml.safe_load((root / path).read_text(encoding="utf-8").split("---", 2)[1])
        nodes[page_id] = {
            "id": page_id,
            "kind": "page",
            "title": metadata["title"],
            "status": metadata["status"],
            "version": metadata["version"],
            "domains": metadata["domains"],
            "path": path,
            "url": route,
        }
        parser = ArticleLinks()
        parser.feed((site / route.lstrip("/") / "index.html").read_text(encoding="utf-8"))
        for href in parser.links:
            target = urlsplit(urljoin(config.site_url.rstrip("/") + route, href))
            target_route = unquote(target.path).removesuffix("/index.html").rstrip("/") + "/"
            if target.netloc == origin and target_route in page_ids and target_route != route:
                target_id = page_ids[target_route]
                edges.add((page_id, "page_links_to_page", target_id))
                inbound_pages.add(target_id)
        for source_id in metadata.get("source_ids", []):
            edges.add((page_id, "page_lists_source", source_id))
        for claim_id in metadata.get("claim_ids", []):
            edges.add((page_id, "page_lists_claim", claim_id))

    for claim_id in sorted({target for _, relation, target in edges if relation == "page_lists_claim"}):
        claim = claims[claim_id]
        nodes[claim_id] = {
            "id": claim_id,
            "kind": "claim",
            "claim_class": claim["claim_class"],
            "evidence_status": claim["evidence_status"],
        }
        for source_id in claim.get("source_ids", []):
            edges.add((claim_id, "claim_lists_source", source_id))

    for source_id in sorted({target for _, relation, target in edges if relation.endswith("_lists_source")}):
        source = sources[source_id]
        nodes[source_id] = {
            "id": source_id,
            "kind": "source",
            "title": source["title"],
            "authority_level": source["authority_level"],
            "status": source["status"],
            "url": source.get("url"),
        }

    payload = {
        "schema_version": "1.0.0",
        "canonical_language": "es",
        "nodes": [nodes[node_id] for node_id in sorted(nodes)],
        "edges": [{"from": start, "relation": kind, "to": end} for start, kind, end in sorted(edges)],
        "pages_without_inbound_content_links": sorted(set(page_ids.values()) - inbound_pages - {page_ids["/"]}),
    }
    output = site / "assets/data/cdi-knowledge-graph.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
