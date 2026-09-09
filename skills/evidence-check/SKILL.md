---
name: evidence-check
description: Check whether a change's acceptance criteria are supported by current command, diff, plan, or rendered evidence. Use before handoff or review, especially when an agent has claimed completion.
---

# Evidence check

Verify the reviewed revision rather than trusting its author.

1. Read the approved acceptance criteria and repository validation instructions.
2. Identify the exact revision or working diff under review.
3. Map each criterion to a suitable artifact: test output, build output, plan, runtime observation, or rendered view.
4. Run safe local checks when authorized. Never substitute expected output for output that actually ran.
5. Inspect the complete diff for scope drift, credentials, generated junk, and missing failure-state coverage.
6. Mark evidence stale if it predates the reviewed revision.

Return a table with `criterion`, `evidence`, `revision`, and `status`. Use `pass`, `fail`, `missing`, or `stale`. Then list residual risks and checks not run.

Do not merge, deploy, approve destructive work, or describe an unrun check as passing.
