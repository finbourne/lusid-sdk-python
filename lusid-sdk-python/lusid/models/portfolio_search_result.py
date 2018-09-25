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

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id:
    :vartype id: ~lusid.models.ResourceId
    :ivar type: Possible values include: 'Transaction', 'Reference',
     'DerivedTransaction'
    :vartype type: str or ~lusid.models.enum
    :ivar href:
    :vartype href: str
    :ivar description:
    :vartype description: str
    :ivar display_name:
    :vartype display_name: str
    :ivar is_derived:
    :vartype is_derived: bool
    :ivar created:
    :vartype created: datetime
    :ivar parent_portfolio_id:
    :vartype parent_portfolio_id: ~lusid.models.ResourceId
    :ivar properties:
    :vartype properties: list[~lusid.models.PropertyDto]
    :param links:
    :type links: list[~lusid.models.Link]
    """

    _validation = {
        'id': {'readonly': True},
        'type': {'readonly': True},
        'href': {'readonly': True},
        'description': {'readonly': True},
        'display_name': {'readonly': True},
        'is_derived': {'readonly': True},
        'created': {'readonly': True},
        'parent_portfolio_id': {'readonly': True},
        'properties': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'ResourceId'},
        'type': {'key': 'type', 'type': 'str'},
        'href': {'key': 'href', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'is_derived': {'key': 'isDerived', 'type': 'bool'},
        'created': {'key': 'created', 'type': 'iso-8601'},
        'parent_portfolio_id': {'key': 'parentPortfolioId', 'type': 'ResourceId'},
        'properties': {'key': 'properties', 'type': '[PropertyDto]'},
        'links': {'key': 'links', 'type': '[Link]'},
    }

    def __init__(self, links=None):
        super(PortfolioSearchResult, self).__init__()
        self.id = None
        self.type = None
        self.href = None
        self.description = None
        self.display_name = None
        self.is_derived = None
        self.created = None
        self.parent_portfolio_id = None
        self.properties = None
        self.links = links
