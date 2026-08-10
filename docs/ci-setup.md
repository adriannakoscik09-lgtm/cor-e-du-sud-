# CI Configuration

This directory contains GitHub Actions workflow files for continuous integration.

## Workflow

The CI pipeline runs on every push and pull request to `main`:

1. **Checkout** the repository
2. **Set up Python 3.11**
3. **Install dependencies** from `requirements.txt` plus `pytest`
4. **Run tests** with `python -m pytest tests/ -v`

## Adding the workflow file

Due to OAuth token scope limitations, the `.github/workflows/ci.yml` file needs to be added manually or via a token with the `workflow` scope. See the file content below:

```yaml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
          pip install pytest

      - name: Run tests
        run: python -m pytest tests/ -v
```