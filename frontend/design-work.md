# Frontend design work

A frontend task begins with the user experience and the rendered result. A component that compiles can still hide content, fail at a narrow width, or be unusable from a keyboard.

## Write a visual contract

Before implementation, record the visible behavior that the change must preserve or introduce:

- target users and the action they need to complete;
- page states such as loading, empty, error, and success;
- layout rules at wide and narrow viewports;
- typography, spacing, color, focus, and motion constraints that matter to the task;
- semantic structure and keyboard behavior;
- content that must remain visible, readable, and reachable.

Keep the contract proportional to the change. A button-label correction may need one sentence. A new flow needs states, breakpoints, and acceptance checks.

## Build against the contract

Inspect the existing design system, routes, components, and accessible names before adding new patterns. Reuse a suitable existing component when it meets the contract. If it does not, explain the new pattern and add the smallest reusable unit that solves the real problem.

Do not replace a specific design decision with generic "modern" styling. Do not treat a screenshot as the only source of truth when the product has semantic and interaction requirements.

## Use third-party guidance honestly

Anthropic publishes a Claude Code-compatible `frontend-design` skill at <https://github.com/anthropics/skills/tree/main/skills/frontend-design>. It may be useful as a design-work reference.

This repository does not own, bundle, modify, or redistribute that skill. It does not claim Anthropic endorses this workflow. Read the upstream instructions and license before using or copying any material. This repository's visual contract and validation rules remain the project contract.

## Definition of done

A frontend change is ready for review when it has:

1. a written visual contract or a clear link to the applicable design decision;
2. rendered evidence for the affected states and viewports;
3. keyboard and semantic checks for changed controls;
4. the relevant automated checks and a complete diff review;
5. documented limitations when a state or platform cannot be tested.

See [visual validation](visual-validation.md) for the evidence procedure and [agent briefs](../coordination/agent-briefs.md) for how to delegate a frontend task.
