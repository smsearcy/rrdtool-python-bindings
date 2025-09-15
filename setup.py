"""Instructions for setuptools to build the rrdtool bindings."""

import platform
import sys

from setuptools import Extension, setup

extra_compile_args = []

if sys.platform.startswith("linux"):
    distro_info = platform.freedesktop_os_release()
    if distro_info["ID"] == "debian" and distro_info["VERSION_ID"] == "13":
        # Debian Trixie: disable incompatible-pointer-types
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
