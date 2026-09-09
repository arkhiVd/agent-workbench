# Cross-machine work

Moving work between machines or agent harnesses is a portability problem, not a reason to copy every detail into a chat or note.

## Before moving

1. Commit or otherwise identify the current repository state.
2. Record the branch, worktree, changed paths, checks run, open risks, and exact next action.
3. Confirm the receiving machine can access the repository and the approved knowledge references.
4. Redact secrets and private topology from the handoff.

## What travels

A portable handoff contains the current goal, authority boundary, decisions in flight, evidence, unresolved questions, suggested next skill, and references to specs, tasks, commits, and diffs.

It should not duplicate documents already in Git or Obsidian. AI Hero's [handoff guidance](https://www.aihero.dev/skills-handoff) makes the same distinction: a handoff is valuable when work travels, not as a replacement for ordinary context compaction.

## Synchronization discipline

Do not have two writers edit the same file or shared task record concurrently. Use separate branches or worktrees for independent work, then integrate deliberately. Synchronized knowledge hubs can produce conflicts even when each editor is acting correctly, so inspect sync state before writing and stop on conflict artifacts.

Use portable placeholders such as `<repo>`, `<worktree>`, and `<remote-host>`. Never document real addresses, account identifiers, machine inventories, or authentication paths.
