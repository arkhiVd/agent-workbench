# Specification

## Problem

Agent-assisted development often depends on chat history, private machine context, and loosely defined prompts. That makes work difficult to verify, resume, review, or move between tools and machines.

## Audience

Solo developers and small teams who use coding agents while retaining human control over requirements, risk, merge, and deployment decisions.

## Product

A public documentation repository containing:

- a concept-to-project development workflow;
- concise repository instruction patterns;
- an Obsidian-centered knowledge model;
- Pi and Herdr operating guidance;
- bounded multi-agent coordination and model routing;
- cross-machine handoff practices;
- frontend design and visual validation guidance;
- reusable skills, templates, and fictional examples.

## Core model

`Understand → Decide → Specify → Slice → Implement → Validate → Review → Record`

Private durable knowledge belongs in the knowledge hub. Project contracts and current execution state belong in Git. Temporary handoffs point to those sources instead of copying them. Chat sessions are disposable.

## Safety and publication

The repository must not disclose credentials, network addresses, account identifiers, private infrastructure topology, vault notes, or machine inventories. Examples use fictional names and placeholders. The repository includes one user-approved real screenshot as an intentional exception.

Third-party projects are influences, not bundled dependencies. Original prose must link to and credit AI Hero, pstack, Herdr, Pi, Obsidian, and the upstream Claude Code frontend-design skill where relevant.

## Non-goals

- Reproducing a private vault or machine configuration
- Shipping an autonomous merge or deployment system
- Prescribing one model provider, issue tracker, sync tool, or coding client
- Copying third-party skill collections
- Treating agent reports as validation evidence

## Acceptance criteria

- A reader can create a repository contract using the supplied templates.
- The main workflow explains its gates, artifacts, owners, and evidence.
- Obsidian is documented as a private, synchronized knowledge hub with conflict-aware writing rules.
- Pi and Herdr examples show bounded coordination and complexity-based model selection.
- Frontend work includes a visual contract, rendered evidence, accessibility checks, and upstream design-skill reference.
- Cross-machine examples reveal no real connection details or topology.
- Public-safety and internal-link checks pass.
- An independent fresh-context review has no unresolved high-severity findings.
