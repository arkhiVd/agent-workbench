# Harbor Lantern

Harbor Lantern is a fictional static status page for a community ferry. The task is to add a service-alert banner without turning a small content change into a site rewrite.

## 1. Specify

**Required behavior:** When an active alert exists, show its severity, message, and last-updated time above the timetable. With no alert, render no empty container.

**Non-goals:** live vessel tracking, user accounts, push notifications, and changes to timetable data.

**Acceptance evidence:**

- fixture tests prove active and empty states;
- the production build succeeds;
- wide and narrow screenshots show the banner;
- keyboard order, zoom, and contrast are checked in the rendered page.

## 2. Slice and own

| Owner | Paths | Output |
|---|---|---|
| Implementer | `src/alert.*`, `tests/alert.*` | Data shape, rendering, and focused tests |
| Visual reviewer | no writes | Rendered-state findings against the visual contract |
| Coordinator | project task record | Combined evidence and unresolved risks |

The visual reviewer starts after the implementer publishes a reviewable revision. This avoids two writers changing the same component.

## 3. Validate

A fictional evidence record might read:

```text
python -m unittest tests.test_alert  -> 4 tests passed
python -m build_site                 -> completed
manual: default, empty, and long-message states rendered at both agreed widths
manual: keyboard order, visible focus, 200% zoom, and contrast checked
```

These lines are illustrative. In a real repository, preserve the command output or CI link instead of copying this result.

## 4. Review and record

The coordinator compares the diff and rendered evidence with the acceptance criteria. A human decides whether to merge. The [handoff](handoff.md) points to repository state and says what remains; it does not recreate chat history.
