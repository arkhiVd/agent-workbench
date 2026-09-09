# Fictional bounded Herdr run

A coordinator is preparing the Harbor Lantern change. Herdr supplies separate agent sessions, but the repository contract still controls ownership and evidence.

## Assignment

```text
Coordinator goal: prepare the alert-banner change for human review.

Worker A
  Owns: src/alert.*, tests/alert.*
  Deliver: implementation, focused tests, exact command output
  Must not: edit docs, merge, or deploy

Worker B
  Owns: no files (read-only review)
  Starts after: Worker A provides a revision
  Deliver: findings against the visual contract and acceptance criteria

Coordinator
  Owns: task evidence only
  Deliver: checked combined diff, validation summary, unresolved risks
  Must not: report success unless the cited checks ran on the reviewed revision
```

## Why this is bounded

- Each writable path has one owner.
- The reviewer reads a stable revision rather than racing the implementer.
- The coordinator names the evidence required before handoff.
- Merge and release remain human actions.

For independent tasks, a coordinator may run workers in parallel. Shared files, coupled design decisions, and final integration stay sequential unless isolated worktrees make ownership explicit.
