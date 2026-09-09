# Slice

**Input:** approved spec and dependencies.

**Do:** split work into narrow vertical slices. Each slice should cross the layers needed to demonstrate one behavior, fit one focused session where possible, declare blockers, and include acceptance and validation criteria.

Prefer tracer bullets over layer-by-layer tickets. Sequence wide mechanical refactors with expand, migrate, and contract steps when a vertical slice cannot stay green.

**Output:** `TASKS.md` entries or tracker tickets with explicit blocking edges.

**Gate:** human confirms granularity and dependencies before implementation.

**Evidence:** a task can be demoed independently and names its proof.

Inspired by [AI Hero's `/to-tickets` workflow](https://www.aihero.dev/skills-to-tickets).
