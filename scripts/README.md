# Documentation checks

Both checks use the Python standard library and scan from the repository root.

```bash
python scripts/check_public_safety.py
python scripts/check_links.py
```

`check_public_safety.py` flags common credential forms, concrete network and account identifiers, machine-specific paths, and unexpected binary files. `assets/herdr-workflow.png` is the only approved binary exception. Pattern matching cannot prove that prose is safe; inspect the complete diff before publication.

`check_links.py` checks local destinations and Markdown heading fragments. It does not make network requests or report whether external sites are available.

A failure prints the source path and line when available. Replace sensitive example data with fictional names or angle-bracket placeholders; do not weaken a rule merely to make a check green.
