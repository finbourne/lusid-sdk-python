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


class MarketContextSuppliers(Model):
    """It is possible to control which supplier is used for a given asset class.

    :param commodity: Possible values include: 'DataScope', 'Lusid'
    :type commodity: str or ~lusid.models.enum
    :param credit: Possible values include: 'DataScope', 'Lusid'
    :type credit: str or ~lusid.models.enum
    :param equity: Possible values include: 'DataScope', 'Lusid'
    :type equity: str or ~lusid.models.enum
    :param fx: Possible values include: 'DataScope', 'Lusid'
    :type fx: str or ~lusid.models.enum
    :param rates: Possible values include: 'DataScope', 'Lusid'
    :type rates: str or ~lusid.models.enum
    """

    _attribute_map = {
        'commodity': {'key': 'Commodity', 'type': 'str'},
        'credit': {'key': 'Credit', 'type': 'str'},
        'equity': {'key': 'Equity', 'type': 'str'},
        'fx': {'key': 'Fx', 'type': 'str'},
        'rates': {'key': 'Rates', 'type': 'str'},
    }

    def __init__(self, commodity=None, credit=None, equity=None, fx=None, rates=None):
        super(MarketContextSuppliers, self).__init__()
        self.commodity = commodity
        self.credit = credit
        self.equity = equity
        self.fx = fx
        self.rates = rates
