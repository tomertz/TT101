# Repository Setup Plan

This plan lists the best-practice changes proposed for the [tomertz/TT101](https://github.com/tomertz/TT101) repository. Nothing in this plan has been done yet. Each item needs approval before it's carried out.

## Current state

| File | Status |
|------|--------|
| `converter.py` | The unit converter app. Committed and pushed. |
| `REQUIREMENTS.md` | Requirements for the converter. Committed and pushed. |
| `pound_to_kg.py` | Older pound-to-kilogram script, replaced by `converter.py`. Committed and pushed. |
| `__pycache__/` | Folder Python creates automatically when code runs. Not committed. |

## 1. Add a `.gitignore` file

**Why:** It stops Git from tracking files that are generated automatically or that are specific to one computer. Without it, folders like `__pycache__` keep showing up as changes and can get committed by accident.

**What it will contain:**

```
# Python generated files
__pycache__/
*.py[cod]

# Virtual environments
.venv/
venv/

# Test and coverage output
.pytest_cache/
.coverage
htmlcov/

# Editor and operating system files
.vscode/
.idea/
Thumbs.db
.DS_Store
```

The local `__pycache__` folder will also be deleted. Python recreates it when needed.

## 2. Add a `README.md` file

**Why:** GitHub shows this file on the repository's main page. It tells visitors, and you later on, what the project is and how to use it.

**What it will contain:**

- A one-sentence description of the app.
- The list of supported units and what they convert to.
- How to run it on Windows: `py converter.py`.
- An example session showing an input such as `100 mi` and the output `160.93 km`.
- How to quit: type `q` or press Enter on an empty line.
- How to run the tests (see item 4).
- A link to `REQUIREMENTS.md` for full details.

## 3. Delete `pound_to_kg.py`

**Why:** `converter.py` already converts pounds to kilograms, so the old script is duplicate code that could confuse readers. Git keeps the file's history, so it can be restored at any time if needed.

**What will happen:** The file will be removed from the folder and from the current version of the repository.

## 4. Add automated tests in `test_converter.py`

**Why:** Tests confirm the app still works after each change. Running one command checks every case in seconds, instead of trying inputs by hand.

**What it will cover:**

- Every example in the "Examples" table of `REQUIREMENTS.md`.
- Every unit converting in both directions.
- Uppercase unit codes and extra spaces in the input.
- Zero, including `-0`, which must display as `0.00`.
- Every invalid-input rule: negative numbers, a missing unit, unknown units, text instead of a number, too many parts, and values such as `nan` and `inf`.

**How it will work:** The tests will use Python's built-in `unittest` module, so nothing needs to be installed. To run them:

```powershell
py -m unittest
```

The "Press any key to continue..." behavior can't be tested automatically, because it reads directly from the keyboard. It will still need a quick manual check.

## How the changes will be committed

Each item will be its own commit, so each change can be reviewed or undone separately:

1. `Add .gitignore for Python project`
2. `Add README with usage instructions`
3. `Remove pound_to_kg.py, replaced by converter.py`
4. `Add unit tests for converter`

All four commits will be pushed to the `main` branch together once they're done. This plan file (`SETUP_PLAN.md`) is only for review and won't be committed unless you ask.

## Ongoing practices (no setup needed)

These are habits to follow from now on, not changes to make:

- **Commit small, focused changes often**, with a message that says what changed.
- **Use a branch for larger new features** (for example `add-temperature`), and merge it into `main` through a pull request once it works.
- **Never commit passwords, API keys, or personal data.** Anything pushed to GitHub stays in the history.
- **Track bugs and ideas in GitHub Issues**, and close them from commits with messages like `Fixes #3`.
- **Run the tests before every push.**
- **Run `git pull` before starting work** if you use more than one computer.
