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


class CompletePortfolio(Model):
    """CompletePortfolio.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id:
    :vartype id: ~lusid.models.ResourceId
    :ivar href:
    :vartype href: str
    :ivar description:
    :vartype description: str
    :ivar display_name:
    :vartype display_name: str
    :ivar created:
    :vartype created: datetime
    :ivar parent_portfolio_id:
    :vartype parent_portfolio_id: ~lusid.models.ResourceId
    :ivar is_derived:
    :vartype is_derived: bool
    :ivar type: Possible values include: 'Transaction', 'Reference',
     'DerivedTransaction'
    :vartype type: str or ~lusid.models.enum
    :param version:
    :type version: ~lusid.models.Version
    :param properties:
    :type properties: list[~lusid.models.Property]
    :param base_currency:
    :type base_currency: str
    :param links:
    :type links: list[~lusid.models.Link]
    """

    _validation = {
        'id': {'readonly': True},
        'href': {'readonly': True},
        'description': {'readonly': True},
        'display_name': {'readonly': True},
        'created': {'readonly': True},
        'parent_portfolio_id': {'readonly': True},
        'is_derived': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'ResourceId'},
        'href': {'key': 'href', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'created': {'key': 'created', 'type': 'iso-8601'},
        'parent_portfolio_id': {'key': 'parentPortfolioId', 'type': 'ResourceId'},
        'is_derived': {'key': 'isDerived', 'type': 'bool'},
        'type': {'key': 'type', 'type': 'str'},
        'version': {'key': 'version', 'type': 'Version'},
        'properties': {'key': 'properties', 'type': '[Property]'},
        'base_currency': {'key': 'baseCurrency', 'type': 'str'},
        'links': {'key': 'links', 'type': '[Link]'},
    }

    def __init__(self, version=None, properties=None, base_currency=None, links=None):
        super(CompletePortfolio, self).__init__()
        self.id = None
        self.href = None
        self.description = None
        self.display_name = None
        self.created = None
        self.parent_portfolio_id = None
        self.is_derived = None
        self.type = None
        self.version = version
        self.properties = properties
        self.base_currency = base_currency
        self.links = links
