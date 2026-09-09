# Project lifecycle

## Initialize

Inspect the repository, its build system, current state, and deployed boundaries if authorized. Create or repair the repository contract without guessing unknowns.

## Plan

Classify the change. Define outcome, scope, dependencies, risks, exit criteria, validation, and rollback or safe-stop behavior. Obtain approval before implementation.

## Execute

Work one phase or vertical slice on a branch or isolated worktree. Keep changes narrow. Do not merge, deploy, apply, destroy, or publish without explicit human authority.

## Verify

Run focused checks during implementation and the complete local gate before reporting completion. For infrastructure, read the plan line by line and account for creates, changes, replacements, destroys, and cost impact.

## Review

Use fresh context for independent review on non-trivial work. Check standards and intended behavior separately. Fix findings or explain intentional deviations.

## Close

Update task and phase status only after validation passes. Put durable decisions and lessons in Obsidian. Keep the repository contract aligned with what was built. A handoff should reference these sources, not become a competing copy.

See the stage procedures in [`workflows/`](../workflows/understand.md).
