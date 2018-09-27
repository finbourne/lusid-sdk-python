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


class RealisedGainLoss(Model):
    """RealisedGainLoss.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar instrument_uid: Unique instrument identifier
    :vartype instrument_uid: str
    :ivar units: Quantity against which gain has been made in units of the
     instrument
    :vartype units: float
    :ivar purchase_trade_date: Date the position was originally purchased
    :vartype purchase_trade_date: datetime
    :ivar purchase_settlement_date: Date the position originally settled
    :vartype purchase_settlement_date: datetime
    :ivar purchase_price: Price the instrument was purchased at
    :vartype purchase_price: float
    :ivar cost_trade_ccy: Purchase cost in the trade currency
    :vartype cost_trade_ccy: ~lusid.models.CurrencyAndAmount
    :ivar cost_portfolio_ccy: Purchase cost in the trade currency
    :vartype cost_portfolio_ccy: ~lusid.models.CurrencyAndAmount
    :ivar realised_trade_ccy: Gains or losses in the trade currency
    :vartype realised_trade_ccy: ~lusid.models.CurrencyAndAmount
    :ivar realised_total: Total gains or losses in the portfolio currency
    :vartype realised_total: ~lusid.models.CurrencyAndAmount
    :ivar realised_market: Market gains or losses in the portfolio currency
    :vartype realised_market: ~lusid.models.CurrencyAndAmount
    :ivar realised_currency: Currency gains or losses in the portfolio
     currency
    :vartype realised_currency: ~lusid.models.CurrencyAndAmount
    """

    _validation = {
        'instrument_uid': {'readonly': True},
        'units': {'readonly': True},
        'purchase_trade_date': {'readonly': True},
        'purchase_settlement_date': {'readonly': True},
        'purchase_price': {'readonly': True},
        'cost_trade_ccy': {'readonly': True},
        'cost_portfolio_ccy': {'readonly': True},
        'realised_trade_ccy': {'readonly': True},
        'realised_total': {'readonly': True},
        'realised_market': {'readonly': True},
        'realised_currency': {'readonly': True},
    }

    _attribute_map = {
        'instrument_uid': {'key': 'instrumentUid', 'type': 'str'},
        'units': {'key': 'units', 'type': 'float'},
        'purchase_trade_date': {'key': 'purchaseTradeDate', 'type': 'iso-8601'},
        'purchase_settlement_date': {'key': 'purchaseSettlementDate', 'type': 'iso-8601'},
        'purchase_price': {'key': 'purchasePrice', 'type': 'float'},
        'cost_trade_ccy': {'key': 'costTradeCcy', 'type': 'CurrencyAndAmount'},
        'cost_portfolio_ccy': {'key': 'costPortfolioCcy', 'type': 'CurrencyAndAmount'},
        'realised_trade_ccy': {'key': 'realisedTradeCcy', 'type': 'CurrencyAndAmount'},
        'realised_total': {'key': 'realisedTotal', 'type': 'CurrencyAndAmount'},
        'realised_market': {'key': 'realisedMarket', 'type': 'CurrencyAndAmount'},
        'realised_currency': {'key': 'realisedCurrency', 'type': 'CurrencyAndAmount'},
    }

    def __init__(self):
        super(RealisedGainLoss, self).__init__()
        self.instrument_uid = None
        self.units = None
        self.purchase_trade_date = None
        self.purchase_settlement_date = None
        self.purchase_price = None
        self.cost_trade_ccy = None
        self.cost_portfolio_ccy = None
        self.realised_trade_ccy = None
        self.realised_total = None
        self.realised_market = None
        self.realised_currency = None
