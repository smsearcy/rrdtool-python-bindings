# rrdtool-bindings

Python bindings from [RRDtool](https://oss.oetiker.ch/rrdtool),
packaged to work with modern Python packaging tools.

Spiritual successor to [python-rrdtool](https://pypi.org/project/rrdtool/),
which has not been updated since 2022 and the GitHub project was archived in 2023,
so I created this project.

Supported Python versions: 3.8+

## Installation

This compiles the bindings, so it requires the following packages:

* Debian/Ubuntu: `apt-get install -y librrd-dev`
* Fedora/Red Hat: `dnf install -y rrdtool-devel`

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

### v0.2.0 - Unreleased

Initial release.

Uses the C code from [5JAN24](https://github.com/oetiker/rrdtool-1.x/blob/b39df920f0ff31a49460d9872006a2579ee4c7ed/bindings/python/rrdtoolmodule.c).


## Contributing

Changes to the C code should be submitted [upstream](https://github.com/oetiker/rrdtool-1.x),
then copied to this repository.

This project uses [PDM](https://pdm-project.org/latest/),
so you will need that installed first.
Then fork/clone the repository and run `pdm install`.
Wheels can be compiled locally via `pdm build`.

[`just`](https://github.com/casey/just) is used as a task runner for convenience,
but it is optional,
any of the commands in `justfile` can be ran by hand.
