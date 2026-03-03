# Project Instructions

## Style Guide

All technical writing, articles, and documentation must follow the style guide at `.gemini/style-guide.md`. The `/revise` command and the `editor` agent use these rules for structured audits.

## Project Conventions

- **Journal entries**: Every significant change requires a one-line entry in `journal/YYYY-MM-DD.md`.
- **Validation**: Run `make` before considering work complete — it runs lint + tests.
- **Plans**: Store execution plans in `plans/` as kebab-case markdown files.
- **Research**: Store research assets in `research/` with detailed markdown summaries.
- **Tasks**: Track the project roadmap in `TASKS.md`.
- **Changelog**: Keep `CHANGELOG.md` updated for releases.

## Custom Commands

Run `/project:command-name` to invoke project-specific workflows:
- `/project:commit` — group and commit changes using Conventional Commits
- `/project:research` — structured research with executive synthesis
- `/project:draft` — interactive drafting using the style guide
- `/project:revise` — audit and improve a draft against the style guide
- `/project:plan` — generate a detailed execution plan
- `/project:task` — manage the project roadmap
- `/project:issues` — manage GitHub issues
- `/project:release` — automate versioning, changelog, and tagging
- `/project:docs` — generate or update project documentation
- `/project:onboard` — onboard a new developer
- `/project:scaffold` — scaffold a new project
- `/project:maintenance` — analyze and propose refactoring
