#!/bin/bash
#
# build_mac.sh
# Copyright (C) 2023 Uwe Schmitt <uwe.schmitt@id.ethz.ch>
#
# Distributed under terms of the MIT license.
#

python build.py prepare
python configure.py --arch=x86_64 --sip-module PyQt5.sip --no-tools

make

cp siplib/sip.so python_package/PyQt5

cd python_package
python -m build -w
