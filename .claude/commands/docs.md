Analyze codebase to update or generate project documentation in the docs folder.

$ARGUMENTS

**Step 1: Preparation**
1. Check if `docs/` exists. If not, create it.
2. Ensure `docs/index.md` exists. If not, create a placeholder.
3. List and read all existing files in `docs/`.

**Step 2: Context Gathering**
1. Read `CHANGELOG.md` and all files in `journal/` for project evolution and current state.
2. Use the Agent tool to spawn an Explore agent for a deep codebase inspection. Focus on:
   - Overall architecture and data flow.
   - Key classes, methods, and their relationships.
   - External dependencies and frameworks.
   - Deployment and execution procedures.
   - Testing strategies and development workflows.

**Step 3: Gap Analysis & Planning**
Compare the codebase context with existing `docs/`. Identify missing or outdated information.
Target at least:
- `docs/index.md`: Project overview, core functionalities, use cases.
- `docs/deploy.md`: How to deploy, run, and execute.
- `docs/design.md`: Architecture, tech stack, design patterns.
- `docs/develop.md`: Development discipline, git workflow, testing, coding standards.
- Additional files for specific components or modules.

**Step 4: Proposal**
Present a detailed plan. For each file (existing or new):
- What needs to be added, removed, or updated.
- Rationale for the changes.
- Specific files, classes, and methods to document.

**Step 5: Information Gathering**
If there are gaps that code inspection can't resolve (deployment details, business rationale), ask for clarification.

**This command is strictly for analysis and planning.** Do NOT modify documentation files until the plan is approved.
