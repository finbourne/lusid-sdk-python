#!/bin/bash -e

if [[ (${#1} -eq 0) ]] ; then
    echo
    echo "[ERROR] missing API key"
    echo
    exit 1
fi

if [[ (${#2} -eq 0) ]] ; then
    echo 
    echo "[ERROR] missing PyPi repo"
    echo
    exit 1
fi

pypi_password=$1
pypi_repo=$2

cd sdk

api_version=$(cat lusid/__init__.py | grep __version__ |  awk '{split($0, a, "="); print a[2]}' | tr -d ' "')

# package
pip install twine wheel pyOpenSSL
python setup.py sdist
python setup.py bdist_wheel

# upload
twine upload --repository-url $pypi_repo -u pypi -p $pypi_password dist/*

cd ..
