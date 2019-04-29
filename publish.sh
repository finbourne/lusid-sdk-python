#!/bin/bash

set -e

if [[ (${#1} -eq 0) ]] ; then
    echo
    echo "[ERROR] missing API key"
    echo
    exit 1
fi

PYPI_PASSWORD=$1
api_version=$(cat lusid/__init__.py | grep __version__ |  awk '{split($0, a, "="); print a[2]}' | tr -d ' "')

# package
python setup.py sdist
python setup.py bdist_wheel

# upload
twine upload --repository-url https://nexus.finbourne.com/repository/pypi/ -u pypi -p $PYPI_PASSWORD dist/* 
