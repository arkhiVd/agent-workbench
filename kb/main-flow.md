# Main flow

The workflow is a sequence of gates, not a prompt that asks an agent to do everything at once.

| Stage | Main input | Output | Owner of the gate |
|---|---|---|---|
| Understand | code, request, constraints | shared problem model | human and agent |
| Decide | alternatives and risks | settled direction | human |
| Specify | settled decisions | durable contract | human approves; agent drafts |
| Slice | contract and dependencies | reviewable tasks | human approves; agent proposes |
| Implement | one task | branch and change | agent works; human owns authority |
| Validate | changed behavior | command or manual evidence | agent gathers; human judges |
| Review | diff and evidence | findings or approval recommendation | independent reviewer |
| Record | decisions and results | updated project and knowledge records | agent drafts; human confirms |

A small change may combine stages. A multi-session or risky change should make them explicit. Do not skip a gate merely because a model can produce code quickly.

AI Hero uses a similar separation between deciding, specifying, slicing, implementing, and reviewing. Its useful lesson is that implementation should execute an agreed shape rather than reopen design by accident. See [AI Hero's main skills flow](https://www.aihero.dev/skills).

## Safe-stop conditions

Stop before editing when requirements conflict, the target is unclear, the required evidence is unavailable, a destructive action is proposed, or a public/private boundary is uncertain.

## Evidence rule

Every completion claim should point to a diff, command output, test, plan, rendered result, screenshot, or documented manual check. Reasoning alone is not evidence.
