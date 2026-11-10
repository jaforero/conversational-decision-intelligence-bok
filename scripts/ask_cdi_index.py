"""Build and validate the bilingual local evidence index from rendered CDI-BoK pages."""

from __future__ import annotations

import json
import subprocess
from functools import cache
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote

import yaml
from mkdocs.exceptions import PluginError
from mkdocs.plugins import event_priority


class PassageText(HTMLParser):
    def __init__(self, html: str):
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self.skipped = False
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        if tag in {"script", "style", "pre"}:
            self.skipped = True
        if tag in {"p", "li", "blockquote", "br", "tr"}:
            self.parts.append("\n")

    def handle_endtag(self, tag):
        if tag in {"script", "style", "pre"}:
            self.skipped = False
        if tag in {"p", "li", "blockquote", "br", "tr"}:
            self.parts.append("\n")

    def handle_data(self, data):
        if not self.skipped:
            self.parts.append(data)

    @property
    def passages(self) -> list[str]:
        return [text for line in "".join(self.parts).splitlines() if (text := " ".join(line.split()))]


class Anchors(HTMLParser):
    def __init__(self, html: str):
        super().__init__()
        self.ids: set[str] = set()
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        if identifier := dict(attrs).get("id"):
            self.ids.add(identifier)


@event_priority(-110)
def on_post_build(config, **kwargs) -> None:
    i18n = config.plugins.get("i18n")
    if i18n is not None and getattr(i18n, "building", False):
        return

    root = Path(config.config_file_path).resolve().parent
    site = Path(config.site_dir)
    assets = site / "assets/data"
    source_sha = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()
    catalog = yaml.safe_load((root / "governance/ask-cdi.yml").read_text(encoding="utf-8"))
    graph = json.loads((assets / "cdi-knowledge-graph.json").read_text(encoding="utf-8"))
    pages = {node["url"]: node for node in graph["nodes"] if node["kind"] == "page"}

    @cache
    def page_anchors(route: str) -> set[str]:
        return Anchors((site / route.lstrip("/") / "index.html").read_text(encoding="utf-8")).ids

    for lang, prefix in (("es", ""), ("en", "en/")):
        index = json.loads((site / prefix / "search/search_index.json").read_text(encoding="utf-8"))
        titles = {doc["location"]: doc["title"] for doc in index["docs"] if "#" not in doc["location"]}
        sections = {}
        for doc in index["docs"]:
            location = doc["location"]
            relative, separator, fragment = location.partition("#")
            if not separator:
                continue
            route = "/" + relative
            canonical = "/" + relative.removeprefix(prefix)
            page = pages.get(canonical)
            passages = PassageText(doc["text"]).passages
            if not page or page["status"] not in {"approved", "candidate"} or not passages:
                continue
            if unquote(fragment) not in page_anchors(route):
                raise PluginError(f"Ask CDI: missing rendered anchor /{location}")
            sections["/" + location] = {
                "source": "/" + location,
                "title": doc["title"],
                "page": titles[relative],
                "status": page["status"],
                "passages": passages,
                "retrievable": page["path"] not in {"docs/index.md", "docs/ask-cdi.md"}
                and not canonical.startswith(("/versions/", "/about/", "/start-here/")),
                "simulated": canonical.startswith(("/practice-lab/sla-decision-brief/", "/practice-lab/b2b-proposal/")),
            }

        editorial = []
        for item in catalog[lang]:
            section = sections.get(item["source"])
            if not section or item["excerpt"] not in " ".join(section["passages"]):
                raise PluginError(f"Ask CDI: excerpt absent from published source {item['source']}")
            section_route = item["source"].split("#", 1)[0]
            canonical_route = "/" + section_route.lstrip("/").removeprefix(prefix)
            source_node = pages.get(canonical_route)
            if not source_node:
                raise PluginError(f"Ask CDI: cannot locate editorial file {section_route}")
            source_path = source_node["path"]
            if lang == "en":
                source_path = source_path.removesuffix(".md") + ".en.md"
            # Prefer a line-anchored, commit-pinned original when the verified
            # excerpt occurs verbatim within a Markdown source line.
            source_lines = (root / source_path).read_text(encoding="utf-8").splitlines()
            line_number = next((i for i, line in enumerate(source_lines, 1)
                                if item["excerpt"] in line), None)
            github_url = f"https://github.com/jaforero/conversational-decision-intelligence-bok/blob/{source_sha}/{source_path}"
            if line_number is not None:
                github_url += f"#L{line_number}-L{line_number}"
            editorial.append({**item, "title": section["title"], "page": section["page"],
                "status": section["status"], "source_sha": source_sha, "source_path": source_path,
                "github_url": github_url})

        payload = {"editorial": editorial, "sections": [section for section in sections.values() if section["retrievable"]]}
        (assets / f"ask-cdi-{lang}.json").write_text(
            json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8"
        )
