# rrdtool-bindings

Python bindings from [RRDtool](https://oss.oetiker.ch/rrdtool),
packaged to work with modern Python packaging tools.

Spiritual successor to [python-rrdtool](https://pypi.org/project/rrdtool/),
which has not been updated since 2022 and the GitHub project was archived in 2023.
It failed to install/compile via `uv` or `pdm` on recent Fedora releases,
so this project was born.

Supported Python versions: 3.9+

## Installation

This package compiles the bindings, so it requires the following dependencies:

* Debian/Ubuntu: `apt-get install -y gcc librrd-dev python3-dev`
* Fedora/Red Hat: `dnf install -y gcc rrdtool-devel python3-devel`

Then run:

    pip install rrdtool-bindings

## Usage

Example from the RRDtool documentation.

```python
import rrdtool

# Create Round Robin Database
rrdtool.create('test.rrd', '--start', 'now', '--step', '300', 'RRA:AVERAGE:0.5:1:1200', 'DS:temp:GAUGE:600:-273:5000')

# Feed updates to the RRD
rrdtool.update('test.rrd', 'N:32')
```

See [rrdpython](https://oss.oetiker.ch/rrdtool/prog/rrdpython.en.html) and `tests/test_bindings.py` for more examples.

## History

### v0.4.0 - 2025-09-15

Fix for Debian 13 (Trixie).

### v0.3.1 - 2025-04-07

Update change history in README.

### v0.3.0 - 2025-04-07

Update supported Python versions.

### v0.2.0 - 2024-05-31

Initial release.

Uses the C code from [5JAN24](https://github.com/oetiker/rrdtool-1.x/blob/b39df920f0ff31a49460d9872006a2579ee4c7ed/bindings/python/rrdtoolmodule.c).


## Contributing

Changes to the C code should be submitted [upstream](https://github.com/oetiker/rrdtool-1.x),
then copied to this repository.

This project uses [uv](https://docs.astral.sh/uv/),
so you will need that installed first.
Then fork/clone the repository and run `uv sync`.
Wheels can be compiled locally via `uv build`.

[`just`](https://github.com/casey/just) is used as a task runner for convenience,
but it is optional,
any of the commands in `Justfile` can be ran by hand.
