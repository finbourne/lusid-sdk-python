# coding=utf-8
# --------------------------------------------------------------------------
# Copyright © 2018 FINBOURNE TECHNOLOGY LTD
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# --------------------------------------------------------------------------


from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "urllib3 >= 1.15",
    "six >= 1.10",
    "certifi >= 14.05.14",
    "python-dateutil >= 2.5.3",
    "urllib3 >= 1.15.1",
    "requests >= 2.21.0"
]

version = {}
with open("./lusid/__version__.py") as fp:
    exec(fp.read(), version)

setup(

    name='lusid-sdk',
    version=version['__version__'],
    description='Python SDK for LUSID API',
    url='https://github.com/finbourne/lusid-sdk-python',
    author='FINBOURNE Technology',
    author_email='engineering@finbourne.com',
    license='MIT',
    keywords=["OpenAPI", "FINBOURNE", "LUSID", "LUSID API"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=['tests*', 'examples*']),
    include_package_data=True
)
