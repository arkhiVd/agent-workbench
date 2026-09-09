# Getting started

## 1. Define the boundary

Decide whether the work is a note, a repository change, or a risky operational action. State what the agent may inspect, edit, run, and publish. If the boundary is unclear, stop and ask.

## 2. Establish the repository contract

For a substantial repository, create or inspect:

- `AGENTS.md`: local rules, commands, architecture, and safety boundaries.
- `SPEC.md`: problem, users, behavior, versions, non-goals, and acceptance criteria.
- `ROADMAP.md`: ordered phases and exit criteria.
- `TASKS.md`: current executable work and validation status.

The contract belongs with the code so a fresh agent can use it. The reasoning behind decisions belongs in the private knowledge hub.

## 3. Choose a change class

- **Trivial:** documentation or harmless presentation changes.
- **Standard:** features, refactors, and ordinary bug fixes.
- **Risky:** permissions, secrets, networking, data stores, deployment, deletion, or cost-bearing resources.

When uncertain, use the higher class.

## 4. Work one bounded slice

Read only the evidence needed for the next decision. Plan before editing. Use a branch or isolated worktree. Keep one writer per file and preserve unrelated changes.

## 5. Prove the result

Run the repository's documented checks. Report exact commands, results, skipped checks, and residual risk. A confident agent summary is not validation evidence.

## 6. Review and record

Review the diff against both the repository standards and the intended behavior. Record durable decisions in Obsidian and update repository task state only when the stated validation passed.

## Further reading

- [Main flow](main-flow.md)
- [Project lifecycle](project-lifecycle.md)
- [Public safety](public-safety.md)
