# Handoff: Harbor Lantern alert banner

## Goal and boundary

Add the approved service-alert banner. Vessel tracking and timetable changes remain out of scope.

## Current state

- Review branch: `<review-branch>`
- Revision: `<commit-id>`
- Owned paths: `src/alert.*`, `tests/alert.*`
- Contract: [example brief](README.md)

## Decisions

- Omit the banner when no alert exists, so the page has no unexplained gap.
- Keep severity in text as well as color, so meaning does not depend on color perception.

## Evidence

| Check | Result | Location |
|---|---|---|
| Focused fixture tests | pass | `<ci-run>` |
| Production build | pass | `<ci-run>` |
| Wide and narrow rendered states | reviewed | `<review-attachment>` |
| Keyboard, zoom, and contrast | reviewed | `<review-note>` |

## Next safe action

A fresh reviewer should inspect the complete diff and verify that the empty-state fixture leaves no banner container.

## Unknowns

- The longest translated alert has not been tested. Obtain a representative fixture before release if localization is in scope.
