# Repository instructions

## Purpose

This repository publishes a practical, tool-aware workflow for agent-assisted software development. It covers project contracts, skills, Pi, Herdr, Obsidian, cross-machine work, validation, and review.

## Working rules

- Read `SPEC.md`, `ROADMAP.md`, and `TASKS.md` before substantial changes.
- Work only on the current phase and keep changes reviewable.
- Write public-safe examples. Do not add private notes, secrets, credentials, IP addresses, account IDs, session logs, or live infrastructure inventory.
- The approved screenshot in `assets/herdr-workflow.png` is an intentional exception. Do not add further private screenshots or infer operational details from it.
- Write original prose. Link and credit inspirations in `ATTRIBUTION.md`; do not copy third-party skills or documentation unless their license is reviewed and preserved.
- Keep `AGENTS.md` operational. Put explanations in `kb/`, procedures in `workflows/`, coordination guidance in `coordination/`, and reusable examples in `templates/` or `examples/`.
- Prefer relative links and portable placeholders such as `<repo>`, `<remote-host>`, and `<worktree>`.
- One writer owns a file at a time. Parallel agents must receive non-overlapping paths.
- Agents may not merge, publish, deploy, or perform destructive actions.

## Writing style

Use short headings, plain language, concrete examples, and commands that readers can run. Avoid promotional claims and generic AI advice. Every operational claim should name its evidence or source of truth.

## Validation

Run before handoff:

```bash
git diff --check
python scripts/check_public_safety.py
python scripts/check_links.py
```

Also inspect the complete diff and verify that Markdown links resolve. If a check is unavailable, record that fact in `TASKS.md` rather than claiming it passed.
