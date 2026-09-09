# Review

**Input:** final diff, contract, repository standards, and validation evidence.

Review on two separate axes:

- **Standards:** does the change follow repository conventions and safety rules?
- **Spec:** does it implement the intended behavior without scope creep?

Use fresh context for independent review of Standard and Risky work. Order findings by severity, cite the affected path and failure scenario, and propose the smallest useful correction or proof.

**Output:** resolved findings or an explicit explanation of intentional deviations.

**Gate:** every new push invalidates earlier review and evidence. Re-run the relevant checks.

See [AI Hero's two-axis review model](https://www.aihero.dev/skills-code-review), adapted here without requiring its tooling.
