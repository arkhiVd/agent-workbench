# Concept development

Do not start with implementation when the problem is still changing. Start by making the decision visible.

## Explore

Write the problem, affected users, constraints, evidence, and non-goals. Search existing notes and repository material before inventing a new concept. Record uncertainty separately from decisions.

## Shape

Compare a small number of viable approaches. Identify seams where behavior can be tested, data or permission boundaries, operational cost, and failure recovery. Prefer an existing boundary over introducing a new abstraction.

## Decide

A human chooses the direction. Record the choice, rejected alternatives, assumptions, and what would invalidate it. The durable rationale belongs in the knowledge hub; the selected behavior belongs in the project spec.

## Prove direction cheaply

Choose the smallest prototype, spike, example, or test that can disprove the risky assumption. A prototype is evidence for a decision, not permission to quietly become production code.

## Move to a project

Create a repository spec when the work spans sessions, contributors, or meaningful risk. Split it into narrow vertical slices only after the behavior and seams are agreed. AI Hero's [spec](https://www.aihero.dev/skills-to-spec) and [ticket](https://www.aihero.dev/skills-to-tickets) concepts are useful here; this project keeps the final contract in Git rather than requiring one tracker.
