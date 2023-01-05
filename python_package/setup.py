#!/usr/bin/env python

import os

here = os.path.dirname(os.path.abspath(__file__))

from setuptools import setup, Extension

from glob import glob

setup(
    ext_modules=[
        Extension(
            name="PyQt5.sip",
            sources=list(glob("PyQt5/siplib/*.c")),
            include_dirs=["PyQt5/siplib/"],
        )
    ]
)
