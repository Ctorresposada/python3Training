# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Environment

- Python 3.13.3 via a local virtual environment in `myenv/`
- Activate: `source myenv/bin/activate`
- Only external dependency: `requests` (for `spaceGETHTTP.py`)

## Running Scripts

```bash
source myenv/bin/activate
python3 <script_name>.py
```

No build step, test suite, or linter is configured.

## Codebase Overview

This is a Python learning/training repository. Each `.py` file is a standalone script covering a specific concept:

| Concept | Files |
|---|---|
| Basics & math | `helloWorld.py`, `tax.py`, `decades.py` |
| Control flow | `tempCheck.py`, `rock_paper_scissorsELSEIFS.py` |
| Functions | `add_function.py`, `greetingsFunc.py` |
| Loops & ranges | `loopRange.py` |
| Lists | `lists.py` |
| Dictionaries | `dictionary.py`, `DictionarieS.py`, `dictionaryANDlist.py` |
| Classes & OOP | `employeeClass.py`, `robotDogClass.py` |
| Inheritance | `robotClass.py` |
| Cross-file imports | `companyClass.py` (imports `employeeClass.py`) |
| HTTP / APIs | `spaceGETHTTP.py` (fetches live astronaut data from a public API) |
| Error handling | `errorHandling.py` (reads `acronimos.txt`) |

Scripts are independent and self-contained unless noted above. There are no shared modules, packages, or `__init__.py` files.


  ## Style Rules
  - Add a comment explaining each function
  - Keep scripts under 500 lines

  ## Git Workflow
  - Always create a feature branch, never commit directly to main
  - Branch naming: feature/, hotfix/, fix/