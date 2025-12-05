# MedNote: Personal Medical Notes and Automation

MedNote is a minimal Python project scaffold tailored for a solo clinician developer. It focuses on keeping personal medical notes organized while leaving room for small automations and experiments.

## Quick start

1. **Create a virtual environment** (recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

2. **Install the project in editable mode**:
   ```bash
   pip install -e .
   ```

3. **Run the CLI help**:
   ```bash
   mednote --help
   ```

## Project layout

- `src/` – Python source code (CLI lives here).
- `data/` – Place to store personal notes and automation artifacts. A `sample/` folder is included as a safe staging area.
- `docs/` – Use for reference material, workflows, or how-tos.
- `tests/` – Smoke tests and future automation checks.

## Usage ideas

- Keep daily notes in `data/` and commit them to your private repository.
- Add small scripts under `src/` for recurring tasks (e.g., templating visit notes).
- Expand `tests/` to cover any automation to avoid surprises.

## Contributing

This project is intentionally simple. Feel free to adjust structure and conventions to suit your workflow.
