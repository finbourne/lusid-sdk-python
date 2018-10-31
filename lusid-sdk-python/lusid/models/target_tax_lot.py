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


class TargetTaxLot(Model):
    """Used to specify holdings target amounts at the tax-lot level.

    :param units: Quantity of holding
    :type units: float
    :param cost: Book cost of holding in transaction currency
    :type cost: ~lusid.models.CurrencyAndAmount
    :param portfolio_cost: Book cost of holding in portfolio currency
    :type portfolio_cost: float
    :param price: Purchase price. Part of the unique key required for multiple
     taxlots
    :type price: float
    :param purchase_date: Purchase Date. Part of the unique key required for
     multiple taxlots
    :type purchase_date: datetime
    :param settlement_date: Original settlement date of the tax-lot's opening
     transaction.
    :type settlement_date: datetime
    """

    _validation = {
        'units': {'required': True},
    }

    _attribute_map = {
        'units': {'key': 'units', 'type': 'float'},
        'cost': {'key': 'cost', 'type': 'CurrencyAndAmount'},
        'portfolio_cost': {'key': 'portfolioCost', 'type': 'float'},
        'price': {'key': 'price', 'type': 'float'},
        'purchase_date': {'key': 'purchaseDate', 'type': 'iso-8601'},
        'settlement_date': {'key': 'settlementDate', 'type': 'iso-8601'},
    }

    def __init__(self, units, cost=None, portfolio_cost=None, price=None, purchase_date=None, settlement_date=None):
        super(TargetTaxLot, self).__init__()
        self.units = units
        self.cost = cost
        self.portfolio_cost = portfolio_cost
        self.price = price
        self.purchase_date = purchase_date
        self.settlement_date = settlement_date
