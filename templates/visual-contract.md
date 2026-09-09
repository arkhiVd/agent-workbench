# Visual contract: <view or flow>

## User and job

<Who is using this view, and what must they complete?>

## Required states

- Default: <content and primary action>
- Loading: <feedback and preserved context>
- Empty: <explanation and recovery action>
- Error: <message, retry, and support path>
- Narrow viewport: <priority and reflow>

## Design constraints

- Information hierarchy: <ordered elements>
- Existing system primitives: <tokens and components>
- Interaction and motion: <keyboard, pointer, focus, reduced motion>
- Content constraints: <realistic longest and shortest values>

## Evidence

- [ ] Rendered at `<wide viewport>` and `<narrow viewport>`
- [ ] Keyboard path and visible focus checked
- [ ] Automated accessibility check run with `<command>`
- [ ] Contrast, zoom, error state, and reduced motion checked manually
- [ ] Before-and-after images or recording attached to the review

A source diff cannot prove a visual result. Review the rendered interface.
