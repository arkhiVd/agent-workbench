# AI-assisted development workflow

This repository documents a controlled way to use coding agents without treating chat as the project record.

The core loop is:

```text
Understand → Decide → Specify → Slice → Implement → Validate → Review → Record
```

Each arrow is a handoff between a human decision, a repository artifact, or evidence from a tool. The agent can accelerate the work, but it does not replace ownership of requirements, risk, review, merge, or deployment.

## Three kinds of state

- **Knowledge hub:** private, durable notes and decisions kept in Obsidian.
- **Repository:** public or private operational contracts such as `AGENTS.md`, `SPEC.md`, `ROADMAP.md`, and `TASKS.md`.
- **Session:** disposable working context. A handoff may summarize it, but should point to durable sources rather than copy them.

Use the smallest workflow that fits the change. A typo does not need a project spec. A change to permissions, data, infrastructure, or CI credentials does.

## Where to start

- New to the method: [Getting started](getting-started.md)
- Choosing the next action: [Main flow](main-flow.md)
- Designing a new idea: [Concept development](concept-development.md)
- Working on a repository: [Project lifecycle](project-lifecycle.md)
- Writing instructions agents can follow: [Writing for agents](writing-for-agents.md)
- Moving between machines or harnesses: [Cross-machine work](cross-machine-work.md)
- Publishing examples safely: [Public safety](public-safety.md)

The detailed stage procedures live in [workflows/](../workflows/understand.md).

## Influences

The staged flow and skill-oriented information architecture were influenced by [AI Hero's skills collection](https://www.aihero.dev/skills), especially its pages on [specification](https://www.aihero.dev/skills-to-spec), [ticket slicing](https://www.aihero.dev/skills-to-tickets), [implementation](https://www.aihero.dev/skills-implement), [review](https://www.aihero.dev/skills-code-review), [handoffs](https://www.aihero.dev/skills-handoff), and [writing for agents](https://www.aihero.dev/skills-writing-for-agents). This repository uses original prose and adapts the ideas for an Obsidian knowledge hub and repository-local contracts.
