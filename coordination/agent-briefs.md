# Agent briefs

A brief is the contract for one unit of agent work. It must let a worker act without access to the coordinator's chat history, private notes, or another worker's terminal.

## Required fields

```text
Goal:        One observable outcome.
Scope:       Files the worker may write and files it must not change.
Context:     Repository documents, commits, and facts needed to start.
Acceptance:  Checkable conditions for completion.
Verify:      Exact commands, manual checks, and known limitations.
Constraints: Safety boundaries, time limit, and prohibited actions.
Report:      Commit, changed paths, evidence, skipped checks, deviations, and blockers.
Owner:       Worker, branch or worktree, and reviewer.
```

Write a short brief for a small task. Add detail only when it prevents guessing. A vague brief creates an expensive review problem later.

## Example

```text
Goal: Document the browser evidence required for a responsive component change.
Scope: May write frontend/visual-validation.md only.
Context: Read frontend/design-work.md and the repository AGENTS.md.
Acceptance: The document covers wide and narrow viewports, keyboard checks,
accessibility evidence, and a safe evidence location.
Verify: Run python scripts/check_links.py. Read the changed file and its links.
Constraints: Do not add screenshots or refer to a private environment.
Report: State the commit, commands run, results, skipped checks, and blockers.
Owner: worker-frontend in <worktree>. Reviewer: reviewer-docs.
```

## Brief quality check

Do not start a worker if any of these questions has no answer:

- What does done look like?
- Which files may change?
- Which check supports each completion claim?
- What must the worker avoid?
- Where does the result go?

The coordinator updates the brief when evidence shows it was wrong. It does not ask a worker to infer missing requirements.

## Reporting

A worker report is a handoff, not proof. It should be concise enough to scan:

```text
Status: PASS | BLOCKED | NEEDS-REVIEW
Commit: <commit>
Changed paths: <paths>
Evidence: <commands and results>
Skipped checks: <reason>
Deviation: <none or explanation>
Blocker or next step: <one concrete action>
```

The reviewer inspects the branch, diff, and evidence independently. See [ownership and worktrees](ownership-and-worktrees.md) and [Pi usage](pi-usage.md).
