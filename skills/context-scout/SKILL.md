---
name: context-scout
description: Build a concise repository context brief before a bounded implementation, review, or investigation. Use when the task depends on project contracts, current state, ownership, or validation commands.
---

# Context scout

Establish what is true before proposing changes.

1. Read the nearest repository instructions and the task's named contract files.
2. Inspect version-control status. Preserve unrelated changes and identify the current branch or worktree.
3. Find the requested behavior, its callers, tests, and documented validation commands. Prefer direct files and command output over chat summaries.
4. Separate observed facts from decisions and unknowns. Do not search private knowledge stores unless the user authorizes that source for this task.
5. Stop if scope, writable paths, or destructive effects require a human decision.

Return only:

- goal and explicit non-goals;
- source-of-truth files or live evidence;
- owned paths and conflicts;
- commands that can prove completion;
- open decisions or blockers.

Do not edit files during this skill.
