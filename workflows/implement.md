# Implement

**Input:** one approved task, its contract, and the correct branch or worktree.

**Do:** read the relevant callers and tests, make the smallest change, and preserve unrelated work. Use test-first development at agreed behavioral seams where tests represent the contract. Keep the implementation within the task's scope.

**Output:** a diff on a branch or isolated worktree, with focused checks run.

**Gate:** the agent must not merge, deploy, apply, destroy, publish, or reopen settled design without explicit authority.

**Evidence:** diff, focused test output, and a record of skipped checks or residual risk.

See [AI Hero's implementation workflow](https://www.aihero.dev/skills-implement) for the useful separation between decided work and implementation.
