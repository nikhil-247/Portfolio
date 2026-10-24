from __future__ import annotations

import unittest
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]


class PortfolioParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: set[str] = set()
        self.local_refs: set[str] = set()
        self.external_blank_links: list[dict[str, str]] = []
        self.project_cards = 0
        self.text = ""

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {key: value or "" for key, value in attrs}
        if values.get("id"):
            self.ids.add(values["id"])
        href = values.get("href", "")
        src = values.get("src", "")
        for value in (href, src):
            if value.startswith("#") and len(value) > 1:
                self.local_refs.add(value[1:])
        if values.get("target") == "_blank":
            self.external_blank_links.append(values)
        if tag == "article" and "project-card" in values.get("class", "").split():
            self.project_cards += 1

    def handle_data(self, data: str) -> None:
        self.text += data


class PortfolioTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.html = (ROOT / "index.html").read_text(encoding="utf-8")
        cls.parser = PortfolioParser()
        cls.parser.feed(cls.html)

    def test_local_assets_exist(self) -> None:
        for asset in ("styles.css", "script.js", "favicon.svg"):
            with self.subTest(asset=asset):
                self.assertTrue((ROOT / asset).is_file())

    def test_section_anchors_resolve(self) -> None:
        for ref in self.parser.local_refs:
            with self.subTest(anchor=ref):
                self.assertIn(ref, self.parser.ids)

    def test_featured_projects_have_public_repository_links(self) -> None:
        self.assertEqual(self.parser.project_cards, 9)
        self.assertIn("CertFlow", self.parser.text)
        self.assertIn("Tarang", self.parser.text)
        self.assertIn("SimhaGuard 360", self.parser.text)
        self.assertIn("Email Scheduler", self.parser.text)
        self.assertIn("Build Security", self.parser.text)
        self.assertIn("BLE Device Monitor", self.parser.text)

    def test_external_new_tab_links_use_rel_noreferrer(self) -> None:
        for link in self.parser.external_blank_links:
            with self.subTest(href=link.get("href", "")):
                rel = set(link.get("rel", "").split())
                self.assertIn("noreferrer", rel)

    def test_major_engineering_projects_link_to_public_repositories(self) -> None:
        urls = {link.get("href", "") for link in self.parser.external_blank_links}
        self.assertIn("https://github.com/nikhil-247/Email-Scheduler", urls)
        self.assertIn("https://github.com/nikhil-247/Build-security", urls)
        self.assertIn("https://github.com/nikhil-247/BLE-Based-Device-Communication---Monitoring", urls)


if __name__ == "__main__":
    unittest.main()
