# Commands are ran via `uv run` so that it works without activating the virtualenv

default: pre-commit fix build tests

# Format with Ruff
fmt:
  uv run ruff format .

# Lint with Ruff (no fixes)
check:
  uv run ruff check .

# Ruff: format and lint (with fixes)
fix: fmt
  uv run ruff check . --fix

# Run pre-commit hooks/checks
pre-commit:
  uvx pre-commit run --all-files

# Build package (just sdist)
build:
  uv build --sdist

# Run pytest
tests:
  uv run pytest

# Build/Publish package (just sdist)
release tag:
  git rev-parse --abbrev-ref HEAD | awk '$1 != "main" {print "Must be on `main` branch"; exit 1}'
  @echo 'Creating release {{ tag }}'
  rm -f dist/*.tar.gz
  git tag {{ tag }}
  uv build --sdist
  uv publish dist/*.tar.gz
  git push origin {{ tag }}
