"""Instructions for setuptools to build the rrdtool bindings."""

import os
import subprocess

from setuptools import Extension, setup

# on Fedora it wanted `gcc-11`, which didn't exist
if subprocess.run(["command -v gcc-11"], shell=True, check=False).returncode > 0:
    os.environ["CC"] = "gcc"

setup(
    ext_modules=[
        Extension(
            name="rrdtool",
            sources=["src/rrdtool/rrdtoolmodule.c"],
            libraries=["rrd"],
        )
    ]
)
