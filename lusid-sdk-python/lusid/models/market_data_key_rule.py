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


class MarketDataKeyRule(Model):
    """A market data key rule describes a mapping for satisfying a particular
    market dependency. The supplier, scope, quote type and price side
    information define the quote in the market and which Vendor for market data
    would be used to perform the lookup.
    The market data key defines what dependency this satisfies. The key is a
    rule that describes the asset class, its identifier and any other
    specifics required to uniquely describe a specific economic entity (e.g. an
    Fx currency pair, equity name or credit curve).

    :param key: The market data key pattern which this is a rule for. A dot
     separated string (A.B.C.D.*)
    :type key: str
    :param supplier: The market data supplier (where the data comes from).
     Possible values include: 'DataScope', 'Lusid'
    :type supplier: str or ~lusid.models.enum
    :param data_scope: The scope in which the data should be found when using
     this rule.
    :type data_scope: str
    :param quote_type: Is the quote to be looked for a price, yield etc.
     Possible values include: 'Price', 'Spread', 'Rate'
    :type quote_type: str or ~lusid.models.enum
    :param price_side: The conceptual qualification for the field. Something
     like Bid, Ask or Mid. Possible values include: 'Bid', 'Mid', 'Ask'
    :type price_side: str or ~lusid.models.enum
    """

    _validation = {
        'key': {'required': True},
        'supplier': {'required': True},
        'data_scope': {'required': True},
    }

    _attribute_map = {
        'key': {'key': 'key', 'type': 'str'},
        'supplier': {'key': 'supplier', 'type': 'str'},
        'data_scope': {'key': 'dataScope', 'type': 'str'},
        'quote_type': {'key': 'quoteType', 'type': 'str'},
        'price_side': {'key': 'priceSide', 'type': 'str'},
    }

    def __init__(self, key, supplier, data_scope, quote_type=None, price_side=None):
        super(MarketDataKeyRule, self).__init__()
        self.key = key
        self.supplier = supplier
        self.data_scope = data_scope
        self.quote_type = quote_type
        self.price_side = price_side
