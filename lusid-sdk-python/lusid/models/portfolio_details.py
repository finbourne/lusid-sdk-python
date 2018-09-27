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


class PortfolioDetails(Model):
    """PortfolioDetails.

    :param href:
    :type href: str
    :param origin_portfolio_id:
    :type origin_portfolio_id: ~lusid.models.ResourceId
    :param version: The version of the portfolio
    :type version: ~lusid.models.Version
    :param base_currency:
    :type base_currency: str
    :param links:
    :type links: list[~lusid.models.Link]
    """

    _attribute_map = {
        'href': {'key': 'href', 'type': 'str'},
        'origin_portfolio_id': {'key': 'originPortfolioId', 'type': 'ResourceId'},
        'version': {'key': 'version', 'type': 'Version'},
        'base_currency': {'key': 'baseCurrency', 'type': 'str'},
        'links': {'key': 'links', 'type': '[Link]'},
    }

    def __init__(self, href=None, origin_portfolio_id=None, version=None, base_currency=None, links=None):
        super(PortfolioDetails, self).__init__()
        self.href = href
        self.origin_portfolio_id = origin_portfolio_id
        self.version = version
        self.base_currency = base_currency
        self.links = links
