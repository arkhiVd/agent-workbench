#!/usr/bin/env python3
"""Check local Markdown file destinations and heading anchors using stdlib only."""

from __future__ import annotations

import html
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {".git", "__pycache__", ".pytest_cache", ".venv", "node_modules"}
LINK_OPEN = re.compile(r"\]\(\s*")
REFERENCE_DESTINATION = re.compile(r"^\s*\[[^\]]+\]:\s*(?:<([^>]+)>|(\S+))", re.MULTILINE)
HTML_DESTINATION = re.compile(r"\b(?:href|src)=[\"']([^\"']+)[\"']", re.IGNORECASE)
HEADING = re.compile(r"^\s{0,3}#{1,6}\s+(.+?)\s*#*\s*$", re.MULTILINE)


def markdown_files() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*.md")
        if not any(part in SKIP_DIRS for part in path.relative_to(ROOT).parts)
    )


def without_fenced_code(text: str) -> str:
    lines: list[str] = []
    fence: str | None = None
    for line in text.splitlines(keepends=True):
        marker = re.match(r"^\s*(`{3,}|~{3,})", line)
        if marker:
            token = marker.group(1)[0]
            if fence is None:
                fence = token
            elif fence == token:
                fence = None
            lines.append("\n" if line.endswith("\n") else "")
        elif fence is None:
            lines.append(line)
        else:
            lines.append("\n" if line.endswith("\n") else "")
    return "".join(lines)


def github_slug(heading: str) -> str:
    heading = re.sub(r"<[^>]+>", "", html.unescape(heading)).strip().lower()
    kept = "".join(
        char
        for char in heading
        if char in " -_" or not unicodedata.category(char).startswith(("P", "C"))
    )
    return re.sub(r"\s+", "-", kept)


def anchors(path: Path) -> set[str]:
    text = path.read_text(encoding="utf-8")
    counts: Counter[str] = Counter()
    result: set[str] = set()
    for match in HEADING.finditer(without_fenced_code(text)):
        base = github_slug(match.group(1))
        suffix = counts[base]
        result.add(base if suffix == 0 else f"{base}-{suffix}")
        counts[base] += 1
    return result


def inline_destinations(text: str) -> list[tuple[int, str]]:
    """Parse inline destinations, including angle brackets and balanced parentheses."""
    found: list[tuple[int, str]] = []
    for opener in LINK_OPEN.finditer(text):
        start = opener.end()
        if start >= len(text):
            continue
        if text[start] == "<":
            end = text.find(">", start + 1)
            if end != -1:
                found.append((text.count("\n", 0, opener.start()) + 1, text[start + 1 : end]))
            continue

        cursor = start
        depth = 0
        while cursor < len(text):
            char = text[cursor]
            if char == "\\":
                cursor += 2
                continue
            if char == "(":
                depth += 1
            elif char == ")":
                if depth == 0:
                    break
                depth -= 1
            elif char.isspace() and depth == 0:
                break
            cursor += 1
        if cursor > start:
            found.append((text.count("\n", 0, opener.start()) + 1, text[start:cursor]))
    return found


def destinations(text: str) -> list[tuple[int, str]]:
    cleaned = without_fenced_code(text)
    found = inline_destinations(cleaned)
    for pattern in (REFERENCE_DESTINATION, HTML_DESTINATION):
        for match in pattern.finditer(cleaned):
            destination = next(group for group in match.groups() if group is not None)
            found.append((cleaned.count("\n", 0, match.start()) + 1, destination))
    return found


def resolve(source: Path, destination: str) -> tuple[Path, str]:
    split = urlsplit(html.unescape(destination))
    raw_path = unquote(split.path)
    if raw_path.startswith("/"):
        target = ROOT / raw_path.lstrip("/")
    elif raw_path:
        target = source.parent / raw_path
    else:
        target = source
    return target.resolve(), unquote(split.fragment)


def main() -> int:
    failures: list[str] = []
    anchor_cache: dict[Path, set[str]] = {}
    checked = 0

    for source in markdown_files():
        text = source.read_text(encoding="utf-8")
        for line, destination in destinations(text):
            split = urlsplit(html.unescape(destination))
            if split.scheme or split.netloc or destination.startswith(("mailto:", "tel:")):
                continue
            checked += 1
            target, fragment = resolve(source, destination)
            try:
                target.relative_to(ROOT)
            except ValueError:
                failures.append(f"{source.relative_to(ROOT)}:{line}: link escapes repository: {destination}")
                continue
            if not target.exists():
                failures.append(f"{source.relative_to(ROOT)}:{line}: missing target: {destination}")
                continue
            if fragment:
                if target.is_dir():
                    target = target / "README.md"
                if target.suffix.lower() != ".md" or not target.exists():
                    failures.append(f"{source.relative_to(ROOT)}:{line}: anchor target is not Markdown: {destination}")
                    continue
                available = anchor_cache.setdefault(target, anchors(target))
                if github_slug(fragment) not in available:
                    failures.append(f"{source.relative_to(ROOT)}:{line}: missing anchor: {destination}")

    if failures:
        print("Internal-link check failed:")
        for failure in failures:
            print(f"  - {failure}")
        return 1

    print(f"Internal-link check passed ({len(markdown_files())} Markdown files, {checked} local links).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
