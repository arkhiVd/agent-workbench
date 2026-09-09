# Visual validation

Visual validation checks the rendered product after a frontend change. A passing build is necessary, but it does not prove that a person can read, navigate, or operate the page.

## Set the evidence plan first

Name the user path, states, viewport widths, and interaction modes before changing code. For a responsive form, that usually includes a wide viewport, a narrow viewport, keyboard navigation, an invalid submission, and a successful submission. Use the actual acceptance criteria to choose the checks.

## Render the real path

Run the production-equivalent build when the repository provides one. Start the application using the documented command. Exercise the user path through the browser or platform UI rather than setting internal state through developer tools.

Capture evidence that shows both the action and its result. A final screenshot alone may conceal a broken control, focus order, or error state.

## Check each changed surface

| Area | What to inspect |
|---|---|
| Layout | Content does not overlap, clip, or require unintended horizontal scrolling at the named widths. |
| Content | Labels, errors, empty states, and loading states are understandable and visible. |
| Keyboard | Focus is visible, order is sensible, controls operate without a pointer, and dialogs return focus correctly. |
| Semantics | Controls use appropriate native elements or accessible names, and headings follow the page structure. |
| Contrast and motion | The change respects the project's contrast and reduced-motion requirements. |
| Errors | Validation and recovery states explain what happened and how to continue. |

Use automated accessibility checks when the project provides them. Treat a clean automated scan as a useful signal, not proof that the interaction is accessible.

## Evidence and privacy

Store evidence only where the repository says to store it. Use fictional content, test accounts, and redacted fixtures. Do not capture browser profiles, personal data, internal URLs, local file paths, service dashboards, or private messages.

If a real screenshot is deliberately approved for publication, record why it is safe and do not infer or add operational facts around it. Do not add screenshots merely because a task needs visual evidence. A local review artifact may be enough.

## Report the result

A frontend handoff states:

```text
Rendered paths: <paths and states>
Viewports: <named widths or device classes>
Keyboard and accessibility checks: <commands and observations>
Evidence location: <approved repository path or local review artifact>
Skipped checks: <reason>
Known limits: <remaining risk>
```

A reviewer repeats the highest-risk path on the current commit. See [frontend design work](design-work.md) and [Herdr coordination](../coordination/herdr-coordination.md).
