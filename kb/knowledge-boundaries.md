# Knowledge boundaries

Keep information in the place that can govern it.

| Information | Durable home |
|---|---|
| Why a decision was made, lessons, patterns, and private context | Obsidian |
| Repository commands, architecture, constraints, and acceptance criteria | Git |
| Current task status and validation state | `TASKS.md` or the approved tracker |
| Temporary context needed to move work | handoff document |
| Secrets and private operational details | approved secret or internal systems, never this repository |

Do not copy the entire vault into a repository. Do not make the vault the hidden prerequisite for building a public project. A repository should explain its own contract and use placeholders for private dependencies.

The split prevents two failures: repository instructions becoming a personal diary, and durable knowledge disappearing into an unsearchable chat transcript.

## Linking rules

Repository documents may point to public source material and to local repository files. Private notes may link to the repository, but public files must not expose private note paths, titles, screenshots, or excerpts.
