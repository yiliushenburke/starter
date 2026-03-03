Automate the release process including testing, versioning, changelog, and tagging.

Follow these steps precisely:

1. **Check Workspace:** Ensure the worktree is clean. Fail if there are uncommitted changes and instruct to run `/project:commit` first.
2. **Verify Integrity:** Run `make` to ensure all tests and checks pass.
3. **Determine Version Bump:**
   - Identify the latest git tag (e.g., `v1.2.3`).
   - Analyze changes between the latest tag and `HEAD` to propose a version (**major**, **minor**, or **patch**).
4. **Propose Version:**
   - Propose a new version number with rationale.
   - Ask for confirmation.
   - Update the version in `package.json`, `pyproject.toml`, or other config files if they exist.
   - Update version references in source files and documentation.
5. **Update CHANGELOG.md and README.md:**
   - Immediately after the version is decided, update `CHANGELOG.md`.
   - Create a new entry summarizing all changes since the last release.
   - Follow the established format in `CHANGELOG.md`.
   - Update `README.md` if it contains version badges or references.
6. **Finalize Release:**
   - Ask for final confirmation.
   - If confirmed:
     - Create a release commit: `git add CHANGELOG.md README.md && git commit -m "chore(release): version <new_version>"`
     - Create a git tag: `git tag -a "v<new_version>" -m "Release v<new_version>"`
     - Push the tag to the remote if it exists.
     - Use `gh release create` with the changelog entry as release notes.

Report the successful completion and new version.
