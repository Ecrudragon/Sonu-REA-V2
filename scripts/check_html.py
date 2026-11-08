#!/usr/bin/env python3
"""Lightweight standard-library checks for the static landing page."""
from html.parser import HTMLParser
from pathlib import Path
import sys


class SiteParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.duplicates = []
        self.tags = []
        self.title_depth = 0
        self.title_text = []

    def handle_starttag(self, tag, attrs):
        self.tags.append(tag)
        attrs = dict(attrs)
        element_id = attrs.get("id")
        if element_id:
            if element_id in self.ids:
                self.duplicates.append(element_id)
            self.ids.add(element_id)
        if tag == "title":
            self.title_depth += 1

    def handle_endtag(self, tag):
        if tag == "title" and self.title_depth:
            self.title_depth -= 1

    def handle_data(self, data):
        if self.title_depth:
            self.title_text.append(data)


def main():
    page = Path(__file__).resolve().parents[1] / "index.html"
    if not page.is_file():
        print("ERROR: index.html is missing", file=sys.stderr)
        return 1
    parser = SiteParser()
    try:
        parser.feed(page.read_text(encoding="utf-8"))
        parser.close()
    except (OSError, UnicodeError, Exception) as error:
        print(f"ERROR: could not parse {page.name}: {error}", file=sys.stderr)
        return 1

    errors = []
    for tag in ("html", "head", "title", "body", "main"):
        if tag not in parser.tags:
            errors.append(f"missing <{tag}> element")
    if not "".join(parser.title_text).strip():
        errors.append("<title> must not be empty")
    if parser.duplicates:
        errors.append("duplicate id attributes: " + ", ".join(sorted(set(parser.duplicates))))
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("HTML structure checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
