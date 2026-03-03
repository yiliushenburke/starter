Scaffold a new project using modern standard practices and tooling.

$ARGUMENTS

### Phase 1: Requirement Gathering
Ask structured questions to determine preferences:
- Primary programming language and framework (e.g., Python/FastAPI, TypeScript/React, Rust/Axum).
- Tooling preferences (e.g., `uv` vs `poetry` for Python, `pnpm` vs `npm` for JS).
- Repository architecture (single app, monorepo).
- Linting, formatting, or testing frameworks to enforce.

### Phase 2: Planning
1. Create a detailed step-by-step scaffolding plan in `plans/scaffold.md`.
2. Prioritize native scaffolding tools (`uv init`, `npm create`, `cargo new`, `go mod init`) over manual file creation.
3. Include installation of necessary dependencies (`pytest`, `ruff`, `eslint`, etc.).
4. Include creating or updating a `makefile` with `test`, `lint`, and `build` targets. The default `make` target MUST run `lint` + `test`.
5. Present the plan for review and await approval.

### Phase 3: Execution
1. Execute the plan step-by-step.
2. Use non-interactive flags for all scaffolding tools (`-y`, `--yes`, `--force`) to prevent hanging.
3. Write or append to the `makefile`.
4. Run `make` to verify the default target passes.
5. Provide a final summary of the scaffolded project.
