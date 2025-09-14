"""Instructions for setuptools to build the rrdtool bindings."""

import os
import subprocess

from setuptools import Extension, setup

extra_compile_args = []

# on Fedora it wanted `gcc-11`, which didn't exist
if subprocess.run(["command -v gcc-11"], shell=True, check=False).returncode > 0:
    os.environ["CC"] = "gcc"

# Debian Trixe: disable incompatible-pointer-types compilation errors for now...
if not subprocess.run(["grep 13 /etc/debian_version"], shell=True, check=False).returncode:
    extra_compile_args = ["-Wno-incompatible-pointer-types"]

setup(
    ext_modules=[
        Extension(
            name="rrdtool",
            sources=["src/rrdtool/rrdtoolmodule.c"],
            libraries=["rrd"],
            extra_compile_args=extra_compile_args,
        )
    ]
)
