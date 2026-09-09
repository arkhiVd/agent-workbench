# Herdr coordination

Herdr can keep agent workspaces, panes, and status visible. In this workflow it is a coordinator aid. It is not an autonomous manager, a source of requirements, or an authority to merge, deploy, or approve work.

## What the coordinator owns

The coordinator translates an approved phase into bounded units of work. It owns:

- the completion condition for the phase;
- worker briefs and file ownership;
- dependencies and the order in which work becomes ready;
- a concise status view for the human;
- escalation when a decision is irreversible, ambiguous, or outside the approved scope.

The coordinator does not silently rewrite worker code. A fix, conflict resolution, or integration change becomes a new bounded task with a named owner.

## What Herdr contributes

Use Herdr to make the current state visible:

- which workspace or worktree belongs to each task;
- whether an agent is working, blocked, or idle;
- which task needs a human decision;
- where a worker's branch and evidence live.

The source of truth remains Git and repository documents. A pane label or agent-status signal can be stale. Confirm completion from the branch, commit, diff, and validation output.

## A small coordination loop

1. Define the phase outcome and observable exit criteria.
2. Split only independent work. Give each unit exclusive paths and a worktree.
3. Give every worker a complete [brief](agent-briefs.md).
4. Track completions as queue items. Do not interrupt the coordinator to perform a deep review of each message.
5. Verify a worker's current commit. A later commit requires verification again.
6. Record a handoff or blocker in a Git-tracked document. Ask the human only for a real decision or explicit approval.

Avoid a standing swarm for ordinary work. One agent can usually complete a small documentation or code change faster and with less coordination cost.

## Human gates

A human must approve merges, publication, deployment, destructive actions, changes with material cost, and decisions that change product intent. Herdr may show that a task is ready. It cannot make the decision.

## Safe public examples

Examples should use roles such as `coordinator`, `worker-docs`, and `reviewer`, plus placeholders such as `<worktree>` and `<remote-host>`. Do not publish pane logs, session records, connection settings, or screenshots beyond an explicitly approved artifact.

See [ownership and worktrees](ownership-and-worktrees.md) for the concurrency rule and [visual validation](../frontend/visual-validation.md) for evidence required by frontend tasks.
