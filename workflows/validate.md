# Validate

**Input:** changed files and acceptance criteria.

**Do:** run focused checks first, then the repository's full local gate. Include formatting, linting, tests, builds, plans, security scans, and rendered or device checks where applicable. For infrastructure, read the plan line by line and count creates, changes, replacements, and destroys.

**Output:** exact commands, results, skipped checks, residual risk, and manual evidence.

**Gate:** an implementation report is not evidence. Stop on unexpected destructive or cost-bearing output.

**Evidence:** command output, test artifacts, screenshots, rendered checks, or authorized environment observations.
