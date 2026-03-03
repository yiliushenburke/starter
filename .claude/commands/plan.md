Interactive planning workflow: gather context, analyze codebase, and generate a detailed plan.

$ARGUMENTS

### Phase 1: Context Gathering (Clarification)
1. Do not start planning immediately. Analyze the initial request.
2. If the request is vague or lacks technical details, ask 1-3 targeted follow-up questions (e.g., "Are we targeting a specific UI component?", "Should this include database migrations?").

### Phase 2: Agentic Analysis
1. Use the Agent tool to spawn a `planner` agent with the clarified objective.
2. The planner will scan the repository and return a detailed Markdown plan.
3. Review the plan and apply corrections based on feedback.
4. Ensure the final plan is comprehensive, actionable, and aligned with the goal.

### Phase 3: Saving the Plan
1. Ensure the `plans/` directory exists.
2. Save the Markdown plan to `plans/` with a descriptive kebab-case filename (e.g., `plans/implement-auth.md`).
3. Notify that the plan has been saved.

### Phase 4: Task Synchronization (TASKS.md)
1. Read `TASKS.md` to understand the project roadmap.
2. Ask whether to link this plan to `TASKS.md`:
   - "Add as a new task"
   - "Update an existing task"
   - "Skip"
3. If linking, update `TASKS.md` so the relevant task points to the plan file (e.g., `(See plan: plans/implement-auth.md)`).

### Phase 5: Issues Synchronization
1. Advise that `/project:issues` can synchronize this plan with the issue tracker.

Do not skip any phases. Start with Phase 1.
