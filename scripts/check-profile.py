#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []

MARKDOWN_LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
HTML_SOURCE = re.compile(r'(?:src|srcset)="([^" ]+)')
ANIMATION = re.compile(r"<\s*(?:animate|animateTransform|animateMotion|set)\b", re.I)
SECRET_PATTERNS = {
    "GitHub token": re.compile(r"\bgh[oprsu]_[A-Za-z0-9_]{30,}\b"),
    "Private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
}


def error(message: str) -> None:
    ERRORS.append(message)


def check_markdown() -> None:
    for path in ROOT.rglob("*.md"):
        text = path.read_text(encoding="utf-8")

        for raw_link in MARKDOWN_LINK.findall(text):
            link = raw_link.strip().split("#", 1)[0]
            if not link or link.startswith(("http://", "https://", "mailto:")):
                continue
            target = (path.parent / link).resolve()
            if not target.exists():
                error(f"Broken relative link: {path.relative_to(ROOT)} -> {raw_link}")

        for raw_source in HTML_SOURCE.findall(text):
            if raw_source.startswith(("http://", "https://")):
                continue
            target = (path.parent / raw_source).resolve()
            if not target.exists():
                error(f"Missing referenced asset: {path.relative_to(ROOT)} -> {raw_source}")


def check_svg() -> None:
    for path in ROOT.rglob("*.svg"):
        try:
            ET.parse(path)
        except ET.ParseError as exc:
            error(f"Invalid SVG XML: {path.relative_to(ROOT)} ({exc})")
            continue

        text = path.read_text(encoding="utf-8")
        if ANIMATION.search(text):
            error(f"Animated SVG is not allowed: {path.relative_to(ROOT)}")

        if path.is_relative_to(ROOT / "assets" / "hero"):
            for requirement in ('role="img"', "<title", "<desc"):
                if requirement not in text:
                    error(
                        f"Hero SVG missing accessibility metadata ({requirement}): "
                        f"{path.relative_to(ROOT)}"
                    )


def check_static_only() -> None:
    for path in ROOT.rglob("*"):
        if path.is_file() and path.suffix.lower() == ".gif":
            error(f"GIF is not allowed by the visual system: {path.relative_to(ROOT)}")


def check_secrets() -> None:
    scan_suffixes = {".md", ".yml", ".yaml", ".py", ".svg", ".txt"}
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in scan_suffixes:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for label, pattern in SECRET_PATTERNS.items():
            if pattern.search(text):
                error(f"Possible {label} found in {path.relative_to(ROOT)}")


def main() -> int:
    check_markdown()
    check_svg()
    check_static_only()
    check_secrets()

    markdown_count = len(list(ROOT.rglob("*.md")))
    svg_count = len(list(ROOT.rglob("*.svg")))

    print(f"Markdown files checked: {markdown_count}")
    print(f"SVG files checked: {svg_count}")

    if ERRORS:
        print(f"Profile quality check failed with {len(ERRORS)} error(s):")
        for item in ERRORS:
            print(f"- {item}")
        return 1

    print("Profile quality check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
