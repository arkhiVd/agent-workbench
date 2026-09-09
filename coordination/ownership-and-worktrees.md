# Ownership and worktrees

Parallel agents are safe only when their write targets do not overlap. A request such as "do not edit the same file" is useful, but it is not concurrency control. Give each writer an exclusive branch or worktree and explicit paths.

## Ownership record

Record each unit before work starts:

```yaml
id: docs-visual-validation
owner: worker-frontend
branch: docs/visual-validation
worktree: <worktree>/frontend-docs
may_write:
  - frontend/design-work.md
  - frontend/visual-validation.md
must_not_write:
  - coordination/
verification:
  - python scripts/check_links.py
reviewer: reviewer-docs
```

This is a fictional example. It names neither a real user nor a real machine.

## Rules

- One writer owns a file at a time.
- One branch or worktree belongs to one active writer.
- A worker changes only paths named in its brief.
- Shared indexes, roadmaps, and integration files have a designated editor.
- A worker publishes a commit before another worker depends on it.
- A verifier checks the commit being proposed, not an earlier snapshot.
- The coordinator resolves ownership conflicts by rescoping work, not by asking two agents to take turns in one file.

## Worktree procedure

```bash
# from the repository root
mkdir -p ../worktrees
git worktree add -b <branch> ../worktrees/<task> HEAD
cd ../worktrees/<task>
```

Use a path outside the primary checkout so each worker has its own index and working tree. Replace placeholders with local values. Do not publish local directory names in examples or reports.

Before removing a worktree, confirm that the branch has been reviewed or that the owner has explicitly abandoned it. Cleanup is a separate, human-approved operation when it could discard work.

## Dependencies and integration

A dependency needs more than an ordering note. The downstream brief must point to the upstream commit, interface, or decision it relies on. Do not make a worker reconstruct sibling work from a chat summary.

The coordinator or a designated integration owner handles conflicts. A clean merge is evidence only that Git found no textual conflict. Run the relevant validation after integration.

See [Herdr coordination](herdr-coordination.md) and [agent briefs](agent-briefs.md).
