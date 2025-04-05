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
publish: build
  uv publish
