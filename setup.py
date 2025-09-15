"""Instructions for setuptools to build the rrdtool bindings."""

import os
import platform
import subprocess
import sys

from setuptools import Extension, setup

# on Fedora it wanted `gcc-11`, which didn't exist
if subprocess.run(["command -v gcc-11"], shell=True, check=False).returncode > 0:
    os.environ["CC"] = "gcc"

extra_compile_args = []

# Debian Trixie: disable incompatible-pointer-types
if sys.version_info >= (3, 10):
    distro_info = platform.freedesktop_os_release()
    if distro_info["ID"] == "debian" and distro_info["VERSION_ID"] == "13":
        extra_compile_args.append("-Wno-incompatible-pointer-types")
elif not subprocess.run(
    ["/usr/bin/grep", "13", "/etc/debian_version"], check=False
).returncode:
    extra_compile_args.append("-Wno-incompatible-pointer-types")

print("Extra compile args:", extra_compile_args)

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
