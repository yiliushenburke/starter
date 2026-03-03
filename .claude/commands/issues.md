Manage project issues using GitHub CLI: list, create, update, or plan work.

$ARGUMENTS

Depending on the intent or arguments, perform one of the following:

### Action: Summary (Default)
If no arguments or 'summary' is provided, produce a strategic report of open issues.
1. Use `gh issue list --json number,title,labels,updatedAt,body` to fetch open issues.
2. Provide a brief summary of each issue.
3. Evaluate each issue by **Feasibility** vs. **Impact**.
4. Suggest which issues to tackle next with rationale.
5. Ask if the user wants to work on a specific issue or create a new one.

### Action: Create or Update
If a description is provided or 'create'/'update' is requested:
1. If an issue number or title is provided, check if it exists with `gh issue list -S "<title or number>"`.
2. **For New Issues:** Generate a standard description with:
   - **Executive Summary:** One-sentence goal.
   - **Rationale:** Why is this important?
   - **Implementation Ideas:** Technical details, file paths, architecture changes.
   - **Reproduction Steps (for Bugfixes):** If it's a bug, try to reproduce it first.
3. **For Updating:** Fetch the existing body with `gh issue view <number> --json body` and propose changes.
4. Present the generated/updated description and get confirmation before running `gh issue create` or `gh issue edit`.

### Action: Work
If asked to 'work on' a specific issue (e.g., `/project:issues work 42`):
1. Fetch full issue details using `gh issue view <number> --json title,body,labels`.
2. Research the relevant files and logic in the codebase.
3. Provide a comprehensive step-by-step implementation plan with testing details.
4. Present the plan and wait for approval before starting execution.

Default to **Summary** if no specific action is inferred. Ask for clarification if intent is unclear.
