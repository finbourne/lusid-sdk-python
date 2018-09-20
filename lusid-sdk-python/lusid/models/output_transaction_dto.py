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


class OutputTransactionDto(Model):
    """OutputTransactionDto.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar trade_id: Unique trade identifier
    :vartype trade_id: str
    :ivar type: LUSID transaction type code - Buy, Sell, StockIn, StockOut,
     etc
    :vartype type: str
    :ivar description: LUSID transaction description
    :vartype description: str
    :ivar security_uid: Unique security identifier
    :vartype security_uid: str
    :ivar trade_date: Trade date
    :vartype trade_date: datetime
    :ivar settlement_date: Settlement date
    :vartype settlement_date: datetime
    :ivar units: Quantity of trade in units of the security
    :vartype units: float
    :ivar trade_price: Execution price for the trade
    :vartype trade_price: ~lusid.models.TradePrice
    :ivar total_consideration: Total value of the trade
    :vartype total_consideration: ~lusid.models.CurrencyAndAmount
    :ivar exchange_rate: Rate between trade and settlement currency
    :vartype exchange_rate: float
    :ivar trade_to_portfolio_rate: Rate between trade and portfolio currency
    :vartype trade_to_portfolio_rate: float
    :ivar trade_currency: Trade currency
    :vartype trade_currency: str
    :ivar properties:
    :vartype properties: list[~lusid.models.PerpetualPropertyDto]
    :ivar counterparty_id: Counterparty identifier
    :vartype counterparty_id: str
    :ivar source: Where this trade came from, either Client or System.
     Possible values include: 'System', 'Client'
    :vartype source: str or ~lusid.models.enum
    :ivar netting_set:
    :vartype netting_set: str
    :ivar transaction_status: Transaction status (active, amended or
     cancelled). Possible values include: 'Active', 'Amended', 'Cancelled'
    :vartype transaction_status: str or ~lusid.models.enum
    :ivar entry_date_time: Date/Time the transaction was booked into LUSID
    :vartype entry_date_time: datetime
    :ivar cancel_date_time: Date/Time the cancellation was booked into LUSID
    :vartype cancel_date_time: datetime
    :ivar realised_gain_loss: Collection of gains or losses
    :vartype realised_gain_loss: list[~lusid.models.RealisedGainLossDto]
    """

    _validation = {
        'trade_id': {'required': True, 'readonly': True},
        'type': {'required': True, 'readonly': True},
        'description': {'required': True, 'readonly': True},
        'security_uid': {'readonly': True},
        'trade_date': {'readonly': True},
        'settlement_date': {'readonly': True},
        'units': {'readonly': True},
        'trade_price': {'readonly': True},
        'total_consideration': {'readonly': True},
        'exchange_rate': {'readonly': True},
        'trade_to_portfolio_rate': {'readonly': True},
        'trade_currency': {'readonly': True},
        'properties': {'readonly': True},
        'counterparty_id': {'readonly': True},
        'source': {'readonly': True},
        'netting_set': {'readonly': True},
        'transaction_status': {'readonly': True},
        'entry_date_time': {'readonly': True},
        'cancel_date_time': {'readonly': True},
        'realised_gain_loss': {'readonly': True},
    }

    _attribute_map = {
        'trade_id': {'key': 'tradeId', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'security_uid': {'key': 'securityUid', 'type': 'str'},
        'trade_date': {'key': 'tradeDate', 'type': 'iso-8601'},
        'settlement_date': {'key': 'settlementDate', 'type': 'iso-8601'},
        'units': {'key': 'units', 'type': 'float'},
        'trade_price': {'key': 'tradePrice', 'type': 'TradePrice'},
        'total_consideration': {'key': 'totalConsideration', 'type': 'CurrencyAndAmount'},
        'exchange_rate': {'key': 'exchangeRate', 'type': 'float'},
        'trade_to_portfolio_rate': {'key': 'tradeToPortfolioRate', 'type': 'float'},
        'trade_currency': {'key': 'tradeCurrency', 'type': 'str'},
        'properties': {'key': 'properties', 'type': '[PerpetualPropertyDto]'},
        'counterparty_id': {'key': 'counterpartyId', 'type': 'str'},
        'source': {'key': 'source', 'type': 'str'},
        'netting_set': {'key': 'nettingSet', 'type': 'str'},
        'transaction_status': {'key': 'transactionStatus', 'type': 'str'},
        'entry_date_time': {'key': 'entryDateTime', 'type': 'iso-8601'},
        'cancel_date_time': {'key': 'cancelDateTime', 'type': 'iso-8601'},
        'realised_gain_loss': {'key': 'realisedGainLoss', 'type': '[RealisedGainLossDto]'},
    }

    def __init__(self):
        super(OutputTransactionDto, self).__init__()
        self.trade_id = None
        self.type = None
        self.description = None
        self.security_uid = None
        self.trade_date = None
        self.settlement_date = None
        self.units = None
        self.trade_price = None
        self.total_consideration = None
        self.exchange_rate = None
        self.trade_to_portfolio_rate = None
        self.trade_currency = None
        self.properties = None
        self.counterparty_id = None
        self.source = None
        self.netting_set = None
        self.transaction_status = None
        self.entry_date_time = None
        self.cancel_date_time = None
        self.realised_gain_loss = None
