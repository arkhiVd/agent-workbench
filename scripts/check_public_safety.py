#!/usr/bin/env python3
"""Reject common private or secret material before publication.

This conservative stdlib check complements, but does not replace, a human diff
review. It scans repository text and permits only the approved screenshot as a
binary file.
"""

from __future__ import annotations

import hashlib
import ipaddress
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {".git", "__pycache__", ".pytest_cache", ".venv", "node_modules"}
APPROVED_BINARY = {
    Path("assets/herdr-workflow.png"): "a3b9e536b2198daf2683680d35d754c01b4fe5ed0d6ce035542072b270b1a1d4"
}
TEXT_SUFFIXES = {
    ".cfg",
    ".conf",
    ".css",
    ".csv",
    ".html",
    ".ini",
    ".js",
    ".json",
    ".jsx",
    ".md",
    ".py",
    ".sh",
    ".toml",
    ".ts",
    ".tsx",
    ".txt",
    ".xml",
    ".yaml",
    ".yml",
}
TEXT_FILENAMES = {"LICENSE", "Makefile", ".gitignore", ".gitattributes", ".editorconfig"}
MAX_TEXT_BYTES = 2_000_000

Rule = tuple[str, re.Pattern[str]]
RULES: list[Rule] = [
    (
        "private key material",
        re.compile(r"-{4,}BEGIN [A-Z0-9 ]*" + "PRIV" + r"ATE KEY-{4,}"),
    ),
    (
        "cloud access key",
        re.compile(r"\b(?:" + "AK" + r"IA|ASIA)[A-Z0-9]{16}\b"),
    ),
    ("GitHub token", re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{20,}\b")),
    ("OpenAI token", re.compile(r"\b" + "sk" + r"-(?!ant-)[A-Za-z0-9_-]{20,}\b")),
    ("Anthropic token", re.compile(r"\b" + "sk" + r"-ant-[A-Za-z0-9_-]{20,}\b")),
    ("Google API key", re.compile(r"\b" + "AI" + r"za[A-Za-z0-9_-]{30,}\b")),
    ("Slack token", re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{12,}\b")),
    (
        "JSON web token",
        re.compile(r"\beyJ[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\b"),
    ),
    (
        "credential assignment",
        re.compile(
            r"(?i)\b(?:api[_-]?key|access[_-]?token|auth[_-]?token|password|passwd|secret)"
            r"\s*[:=]\s*[\"']?(?!<|\$\{|your-|example-|placeholder)"
            r"[A-Za-z0-9_./+=-]{8,}"
        ),
    ),
    ("cloud account identifier", re.compile(r"(?<!\d)\d{12}(?!\d)")),
    (
        "cloud resource identifier",
        re.compile(r"\b" + "a" + r"rn:[a-z0-9-]+:[^\s`]+", re.IGNORECASE),
    ),
    (
        "machine-specific home path",
        re.compile(r"(?:/home/[A-Za-z0-9._-]+|/Users/[A-Za-z0-9._-]+|[A-Za-z]:\\Users\\[^\\\s]+)"),
    ),
    (
        "private vault path",
        re.compile(r"(?:Documents/" + "my" + r"vault|\.ob" + r"sidian/)", re.IGNORECASE),
    ),
    (
        "concrete SSH destination",
        re.compile(r"\bssh(?:\s+-[A-Za-z]+(?:\s+\S+)?)?\s+[A-Za-z0-9._-]+@[A-Za-z0-9._-]+"),
    ),
]

IPV4_CANDIDATE = re.compile(r"(?<![\w.])(?:\d{1,3}\.){3}\d{1,3}(?![\w.])")
IPV6_CANDIDATE = re.compile(
    r"(?<![0-9A-Fa-f:])(?:[0-9A-Fa-f]{0,4}:){2,7}[0-9A-Fa-f]{0,4}(?![0-9A-Fa-f:])"
)


def repository_files() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*")
        if path.is_file() and not any(part in SKIP_DIRS for part in path.relative_to(ROOT).parts)
    )


def read_text(path: Path) -> tuple[str | None, str | None]:
    relative = path.relative_to(ROOT)
    data = path.read_bytes()
    if relative in APPROVED_BINARY:
        if not data.startswith(b"\x89PNG\r\n\x1a\n"):
            return None, "approved binary path has an unexpected file signature"
        if hashlib.sha256(data).hexdigest() != APPROVED_BINARY[relative]:
            return None, "approved binary differs from the human-reviewed file"
        return None, None
    if path.suffix.lower() not in TEXT_SUFFIXES and path.name not in TEXT_FILENAMES:
        return None, "unapproved file type"
    if b"\0" in data:
        return None, "unapproved binary file"
    if len(data) > MAX_TEXT_BYTES:
        return None, f"text file exceeds {MAX_TEXT_BYTES} bytes"
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError:
        return None, "non-UTF-8 or binary file"
    if any(ord(char) < 32 and char not in "\t\n\r\f" for char in text):
        return None, "text file contains binary control characters"
    return text, None


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def scan_text(relative: Path, text: str) -> list[str]:
    findings: list[str] = []
    for label, pattern in RULES:
        for match in pattern.finditer(text):
            findings.append(f"{relative}:{line_number(text, match.start())}: {label}")

    for pattern in (IPV4_CANDIDATE, IPV6_CANDIDATE):
        for match in pattern.finditer(text):
            candidate = match.group(0)
            try:
                address = ipaddress.ip_address(candidate)
            except ValueError:
                continue
            findings.append(
                f"{relative}:{line_number(text, match.start())}: network address ({address.version=})"
            )
    return findings


def main() -> int:
    findings: list[str] = []
    for path in repository_files():
        text, error = read_text(path)
        relative = path.relative_to(ROOT)
        if error:
            findings.append(f"{relative}: {error}")
        elif text is not None:
            findings.extend(scan_text(relative, text))

    if findings:
        print("Public-safety check failed:")
        for finding in findings:
            print(f"  - {finding}")
        print("Review each finding; use fictional data or portable angle-bracket placeholders.")
        return 1

    print(f"Public-safety check passed ({len(repository_files())} files scanned).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
