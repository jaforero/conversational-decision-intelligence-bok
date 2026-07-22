"""Localize generated interface details and create language-scoped search indexes."""

from __future__ import annotations

import json
from pathlib import Path

from mkdocs.exceptions import PluginError
from mkdocs.plugins import event_priority


def on_page_content(output: str, page, **kwargs) -> str:
    """Keep deep-link anchors while localizing their accessible tooltip."""

    if not str(page.url).lstrip("/").startswith("en/"):
        output = output.replace('title="Permanent link"', 'title="Enlace permanente"')
    return output


@event_priority(-100)
def on_post_build(config, **kwargs) -> None:
    """Split the combined MkDocs index after every localized build has finished."""

    i18n = config.plugins.get("i18n")
    if i18n is not None and getattr(i18n, "building", False):
        return

    site_dir = Path(config.site_dir)
    combined_path = site_dir / "search" / "search_index.json"
    if not combined_path.exists():
        raise PluginError("The combined search index was not generated")

    combined = json.loads(combined_path.read_text(encoding="utf-8"))
    documents = combined.get("docs")
    if not isinstance(documents, list):
        raise PluginError("The generated search index has no document list")

    spanish = [doc for doc in documents if not str(doc.get("location", "")).startswith("en/")]
    english = [doc for doc in documents if str(doc.get("location", "")).startswith("en/")]
    if not spanish or not english:
        raise PluginError("Both Spanish and English search documents are required")

    spanish_index = {**combined, "docs": spanish}
    english_index = {**combined, "docs": english}

    combined_path.write_text(
        json.dumps(spanish_index, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8",
    )
    english_path = site_dir / "en" / "search" / "search_index.json"
    english_path.parent.mkdir(parents=True, exist_ok=True)
    english_path.write_text(
        json.dumps(english_index, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8",
    )
