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

from msrest.serialization import Model


class VersionedResourceListOfOutputTransaction(Model):
    """VersionedResourceListOfOutputTransaction.

    :param version:
    :type version: ~lusid.models.Version
    :param values:
    :type values: list[~lusid.models.OutputTransaction]
    :param href: The Uri that returns the same result as the original request,
     but may include resolved as at time(s).
    :type href: str
    :param count: The total number of records returned in the set
    :type count: int
    :param links:
    :type links: list[~lusid.models.Link]
    """

    _attribute_map = {
        'version': {'key': 'version', 'type': 'Version'},
        'values': {'key': 'values', 'type': '[OutputTransaction]'},
        'href': {'key': 'href', 'type': 'str'},
        'count': {'key': 'count', 'type': 'int'},
        'links': {'key': 'links', 'type': '[Link]'},
    }

    def __init__(self, version=None, values=None, href=None, count=None, links=None):
        super(VersionedResourceListOfOutputTransaction, self).__init__()
        self.version = version
        self.values = values
        self.href = href
        self.count = count
        self.links = links
