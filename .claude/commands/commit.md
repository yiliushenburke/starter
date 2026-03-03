Group and commit uncommitted changes individually using Conventional Commits.

**Procedure:**
1. **Analyze Changes:**
   - Run `git status` and `git diff` to identify all modified and untracked files.
   - Group files that are related to a single logical change (feature, tests, docs, etc.).
2. **Proposal:**
   - Present the proposed commit groups and their commit messages.
   - Use Conventional Commits format: `<type>(<scope>): <subject>`.
   - Ask for confirmation before proceeding.
3. **Execution:**
   - After confirmation, for each group: stage the files and commit with the proposed message.
   - Report the successful commits.

If there are no changes to commit, say so.
