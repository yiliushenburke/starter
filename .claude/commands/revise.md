Interactive revision workflow: select a file, audit its structure and style based on the Style Guide, and iteratively improve it.

$ARGUMENTS

### Phase 1: File Selection
1. **Select File:** Prompt to select a Markdown file for revision (check `drafts/` or project root).
2. **Confirmation:** Confirm the file selection.

### Phase 2: Analysis and Audit (Style Guide Driven)
1. **Read Style Guide:** Read `.gemini/style-guide.md`.
2. **Invoke Editor:** Use the Agent tool to spawn an `editor` agent to analyze the file against the Style Guide.
3. **Step-by-Step Audit:** The editor should work through these phases from the Style Guide:
   - **Phase 1 (Structural):** Narrative arc, headers, hooks, and deep dives.
   - **Phase 2 (Content & Substance):** Abstractions, concrete imagery, and subtext.
   - **Phase 3 (Linguistic):** Removing "AI-isms" — punchline em dashes, predictable triads, unnecessary juxtaposition.
4. **Audit Report:** Present a concise summary of findings for each phase.

### Phase 3: Interactive Revision
1. **Proposed Changes:** For each improvement, propose a specific change.
2. **Review Loop:** Present the proposed change and get approval before applying it.
3. **Apply Change:** Once approved, apply the improvement to the file.
4. **Next Phase:** Move to the next audit phase once the current one is complete.

### Phase 4: Finalization
1. **Summary:** Summarize all changes made during the revision.
2. **Completion:** Confirm the revision is complete.

Do not skip any phases. Start with Phase 1.
