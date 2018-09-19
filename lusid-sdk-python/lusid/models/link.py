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


class Link(Model):
    """Link.

    :param relation: Possible values include: 'Root', 'Properties', 'Trades',
     'Details', 'Constituents', 'HoldingsAdjustment', 'Commands'
    :type relation: str or ~lusid.models.enum
    :param href:
    :type href: str
    :param description:
    :type description: str
    :param method: Possible values include: 'POST', 'GET', 'PATCH', 'DELETE'
    :type method: str or ~lusid.models.enum
    """

    _validation = {
        'relation': {'required': True},
        'href': {'required': True},
        'method': {'required': True},
    }

    _attribute_map = {
        'relation': {'key': 'relation', 'type': 'str'},
        'href': {'key': 'href', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'method': {'key': 'method', 'type': 'str'},
    }

    def __init__(self, relation, href, method, description=None):
        super(Link, self).__init__()
        self.relation = relation
        self.href = href
        self.description = description
        self.method = method
