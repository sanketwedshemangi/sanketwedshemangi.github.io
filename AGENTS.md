# Project agent memory

This file is the project's committed home for project-intrinsic agent knowledge: build, test, release, architecture, and sharp-edge notes that should travel with the code.

- Edit `src/site.template.html` (an HTML fragment), then run `python3 src/build.py` to regenerate `index.html`; commit both. GitHub Pages serves `index.html` from `main`.
- `build.py` strips the template's test hooks (`window.__open`, `window.__curtain`); screenshot from an unstripped build of the template, not from `index.html`.
- Headless Chrome ignores small window widths: test phone sizes (360x640 to 430x932) inside fixed-size iframes in a wrapper page kept outside the repo.
- Design rules and the captain's standing decisions (Buddhist only, lavender frosted look, script only for names, no RSVP/gallery) are in `docs/design-research.md` and the template's top comment.

## Maintaining this file

Keep this file for knowledge useful to almost every future agent session in this project.
Do not repeat what the codebase already shows; point to the authoritative file or command instead.
Prefer rewriting or pruning existing entries over appending new ones.
When updating this file, preserve this bar for all agents and keep entries concise.
