# Obsidian as a private knowledge hub

Obsidian is useful here as a private, synchronized knowledge hub across machines. It stores durable reasoning that should survive a repository checkout, tool change, or session reset: decisions, project notes, lessons, research, and links to authoritative repository artifacts.

It is not the repository's runtime contract. A fresh contributor should be able to understand the repository from Git alone.

## Recommended split

- Keep project status, acceptance criteria, commands, and current tasks in Git.
- Keep why a decision was made, reusable technical knowledge, and private context in Obsidian.
- Link from the knowledge note to the repository or issue rather than copying the whole contract.
- Add a concise dated project note after a meaningful phase completes.

## Synchronized writing risks

A synchronized vault is not a transactional database. Two devices or agents can edit the same note before synchronization converges. Treat conflict files as a stop signal. Prefer one writer per note, append small changes, and reconcile deliberately when a conflict is reported. Do not use synchronization to coordinate simultaneous edits to shared task state.

Keep secrets, credentials, private infrastructure details, and raw session transcripts out of any note that may be exported or shared. Before publishing a repository, audit links, attachments, frontmatter, and examples for private references.

## Source of truth

When Obsidian and Git disagree about a command, contract, or acceptance criterion, the repository's current contract governs the repository task. Record the discrepancy in the knowledge hub for later cleanup; do not silently widen the repository's scope.
