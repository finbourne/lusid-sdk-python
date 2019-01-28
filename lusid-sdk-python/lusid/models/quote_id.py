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


class QuoteId(Model):
    """QuoteId.

    :param instrument_id:
    :type instrument_id: str
    :param instrument_id_type: Possible values include: 'LusidInstrumentId',
     'Figi', 'RIC', 'QuotePermId', 'Isin', 'CurrencyPair'
    :type instrument_id_type: str or ~lusid.models.enum
    :param quote_type: Possible values include: 'Price', 'Spread', 'Rate'
    :type quote_type: str or ~lusid.models.enum
    :param price_side: Possible values include: 'Bid', 'Mid', 'Ask'
    :type price_side: str or ~lusid.models.enum
    """

    _validation = {
        'instrument_id': {'required': True},
        'instrument_id_type': {'required': True},
        'quote_type': {'required': True},
        'price_side': {'required': True},
    }

    _attribute_map = {
        'instrument_id': {'key': 'instrumentId', 'type': 'str'},
        'instrument_id_type': {'key': 'instrumentIdType', 'type': 'str'},
        'quote_type': {'key': 'quoteType', 'type': 'str'},
        'price_side': {'key': 'priceSide', 'type': 'str'},
    }

    def __init__(self, instrument_id, instrument_id_type, quote_type, price_side):
        super(QuoteId, self).__init__()
        self.instrument_id = instrument_id
        self.instrument_id_type = instrument_id_type
        self.quote_type = quote_type
        self.price_side = price_side
