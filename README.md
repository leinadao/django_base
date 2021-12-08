[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

# Python Django Base
A base python Djano setup

## Set up in another repo
```
  git remote add python-django-base git@github.com:leinadao/python-django-base.git
  git fetch python-django-base
  git rebase python-django-base/main # Resolve any conflicts.
  git push # possibly need --force
```
Update latest base changes in a repo:
```
  git fetch python-django-base
  git rebase python-django-base/main # Resolve any conflicts.
  git push # possibly need --force
```

=======

## Setup
### Install Poetry (if not already on your system)
It can be installed system-wide using:
```
brew install poetry
```

### Configure Poetry
Poetry creates a virtual environment for the project. Storing the virtual environment in the source directory
e.g. allows VSCode to find and activate it, which means that e.g. flake8 plugins are found and run.

At the moment poetry venv location can't be set in `pyproject.toml`, only in `poetry.toml`.
`poetry.toml` may contain config that should not be source-controlled so this should be considered if updating it.

A manual system-wide config change can also be made if needed:
```
poetry config virtualenvs.in-project true
```

### Create virtual environment
Any existing venvs can be removed:
```
poetry env list
poetry env remove ...
```
Then install a new one into `.venv`:
```
poetry install
```

### Set git to use pre-commit hooks
```
poetry run pre-commit install
```

## Updating
### Poetry
Update Poetry version:
```
poetry self update
```

### Python packages
Poetry will only update minor or patch versions by default (e.g. for versions pinned with ^) using:
```
poetry update
```

For major versions you can see which packages are outdated:
```
poetry show --latest
```
And then manually update them using `poetry add ...@latest` or by editing `pyproject.toml` and using `poetry install`.
TODO: Look into plugin [`poetry up`](https://github.com/MousaZeidBaker/poetry-plugin-up).

### Pre-commit packages
```
poetry run pre-commit autoupdate
```

TODO: Use pre-commit to ensure latest base repo has been rebased in?
