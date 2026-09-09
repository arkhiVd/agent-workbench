# Model routing by complexity

Choose a model for the work's risk and reasoning load, not by habit or brand. This guide uses the role names Luna, Sol, and Terra as portable labels. They describe a routing policy, not a claim about a provider, a subscription, or a model's permanent capability.

## Routing policy

| Tier | Best fit | Typical work | Required evidence |
|---|---|---|---|
| Luna | Fast, bounded, low-risk work | file inventory, link checks, formatting fixes, narrow research, mechanical edits | command output or cited paths |
| Sol | Standard implementation and analysis | a scoped feature, focused bug fix, contract update, test review | focused checks and complete diff review |
| Terra | High-judgment or high-risk work | architecture decisions, security boundaries, complex review, incident analysis, conflicting evidence | design rationale, independent review, and the full relevant gate |

A tier is a starting point. Promote the task when the first investigation finds hidden coupling, an external boundary, irreversible effects, or a failed verification attempt. Do not demote a risky task because its diff is short.

## Route by task, not by person

A worker can use Luna to enumerate files and Sol to implement a bounded change. The same worker may ask Terra to review a security-sensitive design. The labels do not rank people or make one model responsible for a whole project.

Use a different model family for an independent review when practical. Fresh context matters more than a second opinion produced from the same prompt and assumptions.

## Cost controls

- Run the cheapest check that can answer the current question.
- Stop parallel exploration once the decision has enough evidence.
- Use one strong reviewer for a meaningful diff instead of several shallow reviews.
- Keep raw tool output out of coordination messages. Preserve the command, result, and relevant excerpt.
- Escalate to a human when the question is about intent, risk acceptance, or authorization rather than analysis.

## Examples

| Task | Initial tier | Escalate when |
|---|---|---|
| Check Markdown links in one directory | Luna | the checker finds a broken reference with unclear ownership |
| Add a documented repository command | Sol | the command affects deployment or credentials |
| Choose an authentication boundary | Terra | always, because the trust model needs deliberate review |
| Compare two layout options | Sol | Terra if the decision changes the design system or accessibility model |

Routing changes the amount of scrutiny. It never removes the rules in [agent briefs](agent-briefs.md), [ownership and worktrees](ownership-and-worktrees.md), or the repository's human approval gates.
