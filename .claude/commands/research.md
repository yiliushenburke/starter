Conduct extensible, structured research with iterative report updates and executive-level synthesis.

Follow this 4-phase workflow on the topic: $ARGUMENTS

### Phase 1: Planning & Approval
1. **Analyze Topic:** Identify the core research goal and break it down into high-level research questions.
2. **Sub-Questions:** For each question, identify 3-5 specific sub-questions that must be addressed.
3. **Approval:** Present the research questions and sub-questions for approval or modification.

### Phase 2: Report Initialization
1. **Initialize Directory:** Create a `research/<topic>/` sub-directory for detailed research assets.
2. **Create Skeleton:** Create `research/<report-title>.md` with:
   - **Executive Summary:** (Placeholder: "To be completed after research.")
   - **Research Questions:** (A section for each approved question with sub-points.)
   - **Conclusions:** (Placeholder.)
   - **Recommendations:** (Placeholder.)

### Phase 3: Iterative Research & Report Update
For each approved research question:
1. **Invoke Researcher:** Use the Agent tool to spawn a `researcher` agent for the specific question, asking it to investigate all sub-points.
2. **Asset Creation:** The researcher will produce detailed summaries in `research/<topic>/`.
3. **Update Main Report:** After each researcher run, update the corresponding section in the main report with:
   - A high-level overview of findings.
   - Links to the detailed research assets.
   - Subsections for specific findings.

### Phase 4: Synthesis & Finalization
Once all questions have been investigated:
1. **Conclusions:** Synthesize overall findings into a "Conclusions" section.
2. **Executive Summary:** Write a comprehensive summary at the beginning highlighting critical insights.
3. **Recommendations:** Provide actionable recommendations including next steps and follow-up research lines.
4. **Final Suggestion:** Advise that the research is complete and `/project:draft` can turn the report into a full article.

Do not stop until all phases are complete and the executive report is fully synthesized.
