# Repository instructions

## Purpose

<One sentence naming what this repository builds and who uses it.>

## Source of truth

- `SPEC.md`: approved behavior and boundaries
- `ROADMAP.md`: phase order and exit criteria
- `TASKS.md`: current phase and validation state
- `<path>`: runtime or deployed-state evidence

## Commands

```bash
<setup command>
<focused check>
<full validation command>
<production build or plan command>
```

## Boundaries

- Work only on the current approved phase.
- Preserve unrelated working-tree changes.
- Assign one writer to each file or worktree.
- Never commit credentials, private notes, machine inventory, or live connection details.
- Do not merge, publish, deploy, or run destructive commands.
- Ask a human before cost-bearing, security-sensitive, or irreversible work.

## Evidence

Report exact commands and results. For visible changes, attach a rendered view and accessibility results. For infrastructure, inspect the plan and state creates, updates, replacements, and deletes. An agent's summary is not validation evidence.
