Analyze and propose refactoring plans to improve code readability and maintainability.

$ARGUMENTS

**Phase 1: Deep Analysis & Planning**
Run a deep analysis focusing on performance, security, readability, and maintainability.
**Do NOT propose changes that alter existing functionality or fix bugs.** This is strictly maintenance, clean-up, and refactoring.

Priorities:
1. **DRY:** Identify and extract duplicated or near-duplicated code.
2. **Documentation:** Add comprehensive docstrings following project conventions.
3. **Test Coverage:** Identify missing coverage and propose tests for corner and edge cases.
4. **Simplification:** Split long, complex, or deeply nested logic into smaller, focused, testable methods.

List all intended changes file by file, explaining the rationale and expected benefit.

**Phase 2: User Agreement**
Stop and present the complete plan. Wait for explicit agreement before making any modifications.

**Phase 3: Step-by-Step Implementation**
After agreement, implement iteratively. Ensure after each logical change:
- Code is properly formatted.
- Linters pass.
- All tests pass.
