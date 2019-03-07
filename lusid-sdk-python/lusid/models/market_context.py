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


class MarketContext(Model):
    """Market context node. This defines how LUSID processes parts of a request
    that require resolution of market data such as instrument prices or
    Fx rates. It controls where the data is loaded from and which sources take
    precedence.

    :param market_rules: The set of rules that define how to resolve
     particular use cases. These can be relatively general or specific in
     nature.
     Nominally any number are possible and will be processed in order where
     applicable. However, there is evidently a potential
     for increased computational cost where many rules must be applied to
     resolve data. Ensuring that portfolios are structured in
     such a way as to reduce the number of rules required is therefore
     sensible.
    :type market_rules: list[~lusid.models.MarketDataKeyRule]
    :param suppliers: It is possible to control which supplier is used for a
     given asset class.
    :type suppliers: ~lusid.models.MarketContextSuppliers
    :param options: Miscellaneous options around market loading. In the
     simplest usage case, this is just a default supplier and instrument
     resolution code.
    :type options: ~lusid.models.MarketOptions
    """

    _attribute_map = {
        'market_rules': {'key': 'marketRules', 'type': '[MarketDataKeyRule]'},
        'suppliers': {'key': 'suppliers', 'type': 'MarketContextSuppliers'},
        'options': {'key': 'options', 'type': 'MarketOptions'},
    }

    def __init__(self, market_rules=None, suppliers=None, options=None):
        super(MarketContext, self).__init__()
        self.market_rules = market_rules
        self.suppliers = suppliers
        self.options = options
