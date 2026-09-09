# Specify

**Input:** settled decisions and repository evidence.

**Do:** write the problem, users, required behavior, architecture, security, pinned versions, cost limits, non-goals, acceptance criteria, and unresolved questions in `SPEC.md` or the approved project contract.

Acceptance criteria must be observable and name their proof. The spec records decisions already made; it is not a fresh interview.

**Output:** a reviewable contract that a fresh session can use without reconstructing the conversation.

**Gate:** human approval is required before risky implementation. Do not invent requirements to fill gaps.

**Evidence:** the committed spec and linked tests, commands, or manual checks.

Inspired by [AI Hero's `/to-spec` workflow](https://www.aihero.dev/skills-to-spec), with repository-local contracts instead of a required tracker.
