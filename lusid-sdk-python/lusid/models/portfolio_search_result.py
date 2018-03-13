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


class PortfolioSearchResult(Model):
    """PortfolioSearchResult.

    :param id:
    :type id: ~lusid.models.ResourceId
    :param href:
    :type href: str
    :param description:
    :type description: str
    :param name:
    :type name: str
    :param is_derived:
    :type is_derived: bool
    :param created:
    :type created: datetime
    :param parent_portfolio_id:
    :type parent_portfolio_id: ~lusid.models.ResourceId
    :param properties:
    :type properties: list[~lusid.models.PropertyDto]
    :param _links:
    :type _links: list[~lusid.models.Link]
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'ResourceId'},
        'href': {'key': 'href', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'is_derived': {'key': 'isDerived', 'type': 'bool'},
        'created': {'key': 'created', 'type': 'iso-8601'},
        'parent_portfolio_id': {'key': 'parentPortfolioId', 'type': 'ResourceId'},
        'properties': {'key': 'properties', 'type': '[PropertyDto]'},
        '_links': {'key': '_links', 'type': '[Link]'},
    }

    def __init__(self, id=None, href=None, description=None, name=None, is_derived=None, created=None, parent_portfolio_id=None, properties=None, _links=None):
        super(PortfolioSearchResult, self).__init__()
        self.id = id
        self.href = href
        self.description = description
        self.name = name
        self.is_derived = is_derived
        self.created = created
        self.parent_portfolio_id = parent_portfolio_id
        self.properties = properties
        self._links = _links
