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


class MarketOptions(Model):
    """The set of options that control miscellaneous and default market resolution
    behaviour.
    These are aimed at a 'crude' level of control for those who do not wish to
    fine tune the way that data is resolved.
    For clients who wish to simply match instruments to prices this is quite
    possibly sufficient. For those wishing to control market data sources
    according to requirements based on accuracy or timeliness it is not. In
    more advanced cases the options should largely be ignored and rules
    specified
    per source. Be aware that where no specified rule matches the final
    fallback is on to the logic implied here.

    :param default_supplier: The default supplier of data. This controls which
     'dialect' is used to find particular market data. e.g. one supplier might
     address data by RIC, another by PermId. Possible values include:
     'DataScope', 'Lusid'
    :type default_supplier: str or ~lusid.models.enum
    :param default_instrument_code_type: when instrument quotes are searched
     for, what identifier should be used by default. Possible values include:
     'LusidInstrumentId', 'Figi', 'RIC', 'QuotePermId', 'Isin', 'CurrencyPair'
    :type default_instrument_code_type: str or ~lusid.models.enum
    :param default_scope: for default rules, which scope should data be
     searched for in
    :type default_scope: str
    """

    _attribute_map = {
        'default_supplier': {'key': 'defaultSupplier', 'type': 'str'},
        'default_instrument_code_type': {'key': 'defaultInstrumentCodeType', 'type': 'str'},
        'default_scope': {'key': 'defaultScope', 'type': 'str'},
    }

    def __init__(self, default_supplier=None, default_instrument_code_type=None, default_scope=None):
        super(MarketOptions, self).__init__()
        self.default_supplier = default_supplier
        self.default_instrument_code_type = default_instrument_code_type
        self.default_scope = default_scope
