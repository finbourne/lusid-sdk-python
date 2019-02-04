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


class Portfolio(Model):
    """Portfolio.

    :param href: Link to retrieve the current entity
    :type href: str
    :param id: Identifier for the portfolio
    :type id: ~lusid.models.ResourceId
    :param type: The type of portfolio this is (e.g. Transaction Portfolio,
     Reference  Portfolio). Possible values include: 'Transaction',
     'Reference', 'DerivedTransaction'
    :type type: str or ~lusid.models.enum
    :param display_name: Display name of the portfolio
    :type display_name: str
    :param description: Description of the portfolio
    :type description: str
    :param created: Portfolio creation time in UTC
    :type created: datetime
    :param parent_portfolio_id: If this is a derived portfolio, the identifier
     of the portfolio from which it is derived
    :type parent_portfolio_id: ~lusid.models.ResourceId
    :param version: The version of the portfolio
    :type version: ~lusid.models.Version
    :param is_derived:
    :type is_derived: bool
    :param links:
    :type links: list[~lusid.models.Link]
    """

    _attribute_map = {
        'href': {'key': 'href', 'type': 'str'},
        'id': {'key': 'id', 'type': 'ResourceId'},
        'type': {'key': 'type', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'created': {'key': 'created', 'type': 'iso-8601'},
        'parent_portfolio_id': {'key': 'parentPortfolioId', 'type': 'ResourceId'},
        'version': {'key': 'version', 'type': 'Version'},
        'is_derived': {'key': 'isDerived', 'type': 'bool'},
        'links': {'key': 'links', 'type': '[Link]'},
    }

    def __init__(self, href=None, id=None, type=None, display_name=None, description=None, created=None, parent_portfolio_id=None, version=None, is_derived=None, links=None):
        super(Portfolio, self).__init__()
        self.href = href
        self.id = id
        self.type = type
        self.display_name = display_name
        self.description = description
        self.created = created
        self.parent_portfolio_id = parent_portfolio_id
        self.version = version
        self.is_derived = is_derived
        self.links = links
