# Writing for agents

An agent-facing document is an executable interface. Write for predictable behavior, not for completeness of explanation.

## Keep the loaded layer small

`AGENTS.md` should contain only rules an agent needs on every task: scope, commands, boundaries, source-of-truth files, and stop conditions. Link to deeper documentation instead of embedding it.

Every line should do at least one of four jobs:

- change behavior;
- identify a source of truth;
- define evidence;
- prevent a known failure.

Delete background that does none of these jobs.

## Name the decision points

Say when a skill is invoked, when it must not be invoked, who approves the next step, and what proves completion. Separate questions from execution. A planning skill may expose choices; an implementation skill should not silently redesign a settled plan.

## Make done observable

Weak: “Improve reliability.”

Strong: “The retry test proves three attempts, the fourth call is suppressed, and `pytest -q` passes.”

Include failure, empty, rollback, and manual-check behavior when they matter.

## Use progressive disclosure

Put the short pointer in always-loaded instructions. Put procedures in workflows. Put rationale and reusable knowledge in the knowledge base. Avoid duplicate copies of the same rule.

These principles are adapted from [AI Hero's writing-for-agents reference](https://www.aihero.dev/skills-writing-for-agents), with original wording and this repository's knowledge-boundary model.
