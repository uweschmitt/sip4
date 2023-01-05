#!/usr/bin/env python

from setuptools import setup

try:

    from wheel.bdist_wheel import bdist_wheel as _bdist_wheel

    # enforce platform tag:
    # https://stackoverflow.com/questions/45150304/

    class bdist_wheel(_bdist_wheel):
        def finalize_options(self):
            _bdist_wheel.finalize_options(self)
            self.root_is_pure = False

except ImportError:
    bdist_wheel = None

setup(
    cmdclass={"bdist_wheel": bdist_wheel},
)
