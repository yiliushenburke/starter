Manage project tasks: create, work on, report, or update the roadmap in TASKS.md.

$ARGUMENTS

Depending on the intent or arguments, perform one of the following:

### Action: Create
Add a new task to `TASKS.md`.
1. Read `TASKS.md` to understand the current structure.
2. Use the provided task description or infer from conversation context.
3. Identify the appropriate section or create a new one.
4. Add the task with status `[ ]` (Todo).
5. Follow existing formatting conventions.

### Action: Work
Mark a task as 'In Progress' and start working on it.
1. Identify the target task from the arguments or context.
2. Read `TASKS.md` and locate the entry.
3. Update its status to `[/]` (In Progress).
4. If there is a plan for the task, ask to confirm next steps and begin.
5. Otherwise, suggest running `/project:plan` first.

### Action: Report
Produce a strategic report of current tasks.
1. Analyze `TASKS.md` and list all `[ ]` Todo or `[/]` In Progress tasks.
2. For each, assess **Feasibility** and **Strategic Value**.
3. Sort by high value and feasibility, suggesting 2-3 top priorities.

### Action: Update
Synchronize `TASKS.md` with project progress.
1. Read `TASKS.md`, `CHANGELOG.md`, and recent `journal/` entries.
2. Analyze uncommitted changes and conversation context.
3. Update statuses: mark completed as `[x]`, move current work to `[/]`, add new features if missing.
4. If a task was implemented differently, update its description.

Default to **Report** if no clear intent is provided. Ask for clarification if unclear.
