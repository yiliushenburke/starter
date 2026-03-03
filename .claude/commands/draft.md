Interactive drafting workflow: gather context, create an outline based on the Style Guide, and generate a technical draft section-by-section.

$ARGUMENTS

### Phase 1: Context Gathering
1. **Analyze Request:** Identify the topic to draft.
2. **Search Context:** Search for existing context in `research/`, `plans/`, `TASKS.md`, and `journal/`.
3. **Read Style Guide:** Read `.gemini/style-guide.md`.
4. **Validate Context:** If no relevant context is found, suggest running `/project:research` or `/project:plan` first, or ask for more details.

### Phase 2: Title and Path
1. **Propose Metadata:** Propose a title and target file path (e.g., `drafts/your-title.md`).
2. **Confirmation:** Get approval for the title and path.

### Phase 3: Outline Creation (Style Guide Driven)
1. **Generate Outline:** Based on the context and `.gemini/style-guide.md` rules (hooks, hierarchical headers, deep dives), generate a detailed Markdown outline.
2. **Review Loop:** Present the outline and refine until approved.

### Phase 4: Initialization
1. **Create Skeleton:** Create the target file with approved title and sections.
2. **Placeholders:** Use `<!-- [Section Name] Placeholder -->` for each section to fill.

### Phase 5: Section-by-Section Drafting
1. **Iterative Drafting:** For each section, use the Agent tool to spawn a `reporter` agent.
2. **Instructions:** Direct the reporter to fill the specific placeholder with detailed prose following the Style Guide tone.
3. **Review Progress:** Update on progress after each section is filled.

### Phase 6: Conclusion
1. **Final Summary:** Notify that the draft is complete.
2. **Next Steps:** Suggest using `/project:revise` to audit the draft against the Style Guide.

Do not skip any phases. Start with Phase 1.
