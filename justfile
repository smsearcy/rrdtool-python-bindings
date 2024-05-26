# Commands are ran via `pdm run` so that it works without activating the virtualenv

# run common tasks ('fix', 'pre-commit', and 'tests')
default: fix pre-commit tests

# run pre-commit hooks/checks
pre-commit:
  pdm run pre-commit run --all-files

# run ruff to format/lint code
fix:
  pdm run ruff format .
  pdm run ruff check . --fix

# run pytest
tests:
  pdm run pytest tests
