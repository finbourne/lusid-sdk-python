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

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar href: Link to retrieve the current entity
    :vartype href: str
    :ivar id: Identifier for the portfolio
    :vartype id: ~lusid.models.ResourceId
    :ivar type: The type of portfolio this is (e.g. Transaction Portfolio,
     Reference  Portfolio). Possible values include: 'Transaction',
     'Reference', 'DerivedTransaction'
    :vartype type: str or ~lusid.models.enum
    :ivar display_name: Display name of the portfolio
    :vartype display_name: str
    :ivar description: Description of the portfolio
    :vartype description: str
    :ivar created: Portfolio creation time in UTC
    :vartype created: datetime
    :ivar parent_portfolio_id: If this is a derived portfolio, the identifier
     of the portfolio from which it is derived
    :vartype parent_portfolio_id: ~lusid.models.ResourceId
    :ivar version: The version of the portfolio
    :vartype version: ~lusid.models.Version
    :ivar is_derived:
    :vartype is_derived: bool
    :param links:
    :type links: list[~lusid.models.Link]
    """

    _validation = {
        'href': {'readonly': True},
        'id': {'readonly': True},
        'type': {'readonly': True},
        'display_name': {'readonly': True},
        'description': {'readonly': True},
        'created': {'readonly': True},
        'parent_portfolio_id': {'readonly': True},
        'version': {'readonly': True},
        'is_derived': {'readonly': True},
    }

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

    def __init__(self, links=None):
        super(Portfolio, self).__init__()
        self.href = None
        self.id = None
        self.type = None
        self.display_name = None
        self.description = None
        self.created = None
        self.parent_portfolio_id = None
        self.version = None
        self.is_derived = None
        self.links = links
