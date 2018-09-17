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


class UpsertPortfolioTradeRequest(Model):
    """UpsertPortfolioTradeRequest.

    :param trade_id: Unique trade identifier
    :type trade_id: str
    :param type: LUSID transaction type code - Buy, Sell, StockIn, StockOut,
     etc
    :type type: str
    :param security_uid: Unique security identifier
    :type security_uid: str
    :param trade_date: Trade date
    :type trade_date: datetime
    :param settlement_date: Settlement date
    :type settlement_date: datetime
    :param units: Quantity of trade in units of the security
    :type units: float
    :param trade_price: Execution price for the trade
    :type trade_price: float
    :param total_consideration: Total value of the trade
    :type total_consideration: float
    :param exchange_rate: Rate between trade and settle currency
    :type exchange_rate: float
    :param settlement_currency: Settlement currency
    :type settlement_currency: str
    :param trade_currency: Trade currency
    :type trade_currency: str
    :param properties:
    :type properties: list[~lusid.models.CreatePerpetualPropertyRequest]
    :param counterparty_id: Counterparty identifier
    :type counterparty_id: str
    :param source: Where this trade came from, either Client or System.
     Possible values include: 'System', 'Client'
    :type source: str or ~lusid.models.enum
    :param dividend_state: Possible values include: 'Default', 'ExDividend',
     'CumDividend'
    :type dividend_state: str or ~lusid.models.enum
    :param trade_price_type: Possible values include: 'Price', 'Yield',
     'Spread'
    :type trade_price_type: str or ~lusid.models.enum
    :param unit_type: Possible values include: 'Nominal', 'Shares',
     'FaceValue', 'Contracts'
    :type unit_type: str or ~lusid.models.enum
    :param netting_set:
    :type netting_set: str
    """

    _validation = {
        'trade_id': {'required': True},
        'type': {'required': True},
        'settlement_currency': {'required': True},
    }

    _attribute_map = {
        'trade_id': {'key': 'tradeId', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'security_uid': {'key': 'securityUid', 'type': 'str'},
        'trade_date': {'key': 'tradeDate', 'type': 'iso-8601'},
        'settlement_date': {'key': 'settlementDate', 'type': 'iso-8601'},
        'units': {'key': 'units', 'type': 'float'},
        'trade_price': {'key': 'tradePrice', 'type': 'float'},
        'total_consideration': {'key': 'totalConsideration', 'type': 'float'},
        'exchange_rate': {'key': 'exchangeRate', 'type': 'float'},
        'settlement_currency': {'key': 'settlementCurrency', 'type': 'str'},
        'trade_currency': {'key': 'tradeCurrency', 'type': 'str'},
        'properties': {'key': 'properties', 'type': '[CreatePerpetualPropertyRequest]'},
        'counterparty_id': {'key': 'counterpartyId', 'type': 'str'},
        'source': {'key': 'source', 'type': 'str'},
        'dividend_state': {'key': 'dividendState', 'type': 'str'},
        'trade_price_type': {'key': 'tradePriceType', 'type': 'str'},
        'unit_type': {'key': 'unitType', 'type': 'str'},
        'netting_set': {'key': 'nettingSet', 'type': 'str'},
    }

    def __init__(self, trade_id, type, settlement_currency, security_uid=None, trade_date=None, settlement_date=None, units=None, trade_price=None, total_consideration=None, exchange_rate=None, trade_currency=None, properties=None, counterparty_id=None, source=None, dividend_state=None, trade_price_type=None, unit_type=None, netting_set=None):
        super(UpsertPortfolioTradeRequest, self).__init__()
        self.trade_id = trade_id
        self.type = type
        self.security_uid = security_uid
        self.trade_date = trade_date
        self.settlement_date = settlement_date
        self.units = units
        self.trade_price = trade_price
        self.total_consideration = total_consideration
        self.exchange_rate = exchange_rate
        self.settlement_currency = settlement_currency
        self.trade_currency = trade_currency
        self.properties = properties
        self.counterparty_id = counterparty_id
        self.source = source
        self.dividend_state = dividend_state
        self.trade_price_type = trade_price_type
        self.unit_type = unit_type
        self.netting_set = netting_set
