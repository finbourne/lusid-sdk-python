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


class OutputTransaction(Model):
    """OutputTransaction.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar transaction_id: Unique transaction identifier
    :vartype transaction_id: str
    :ivar type: LUSID transaction type code - Buy, Sell, StockIn, StockOut,
     etc
    :vartype type: str
    :ivar description: LUSID transaction description
    :vartype description: str
    :ivar instrument_uid: Unique instrument identifier
    :vartype instrument_uid: str
    :ivar transaction_date: Transaction date
    :vartype transaction_date: datetime
    :ivar settlement_date: Settlement date
    :vartype settlement_date: datetime
    :ivar units: Quantity of trade in units of the instrument
    :vartype units: float
    :ivar transaction_price: Execution price for the transaction
    :vartype transaction_price: ~lusid.models.TransactionPrice
    :ivar total_consideration: Total value of the transaction in settlement
     currency
    :vartype total_consideration: ~lusid.models.CurrencyAndAmount
    :ivar exchange_rate: Rate between transaction and settlement currency
    :vartype exchange_rate: float
    :ivar transaction_to_portfolio_rate: Rate between transaction and
     portfolio currency
    :vartype transaction_to_portfolio_rate: float
    :ivar transaction_currency: Transaction currency
    :vartype transaction_currency: str
    :ivar properties:
    :vartype properties: list[~lusid.models.PerpetualProperty]
    :ivar counterparty_id: Counterparty identifier
    :vartype counterparty_id: str
    :ivar source: Where this transaction came from, either Client or System.
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
    :vartype realised_gain_loss: list[~lusid.models.RealisedGainLoss]
    """

    _validation = {
        'transaction_id': {'readonly': True},
        'type': {'readonly': True},
        'description': {'readonly': True},
        'instrument_uid': {'readonly': True},
        'transaction_date': {'readonly': True},
        'settlement_date': {'readonly': True},
        'units': {'readonly': True},
        'transaction_price': {'readonly': True},
        'total_consideration': {'readonly': True},
        'exchange_rate': {'readonly': True},
        'transaction_to_portfolio_rate': {'readonly': True},
        'transaction_currency': {'readonly': True},
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
        'transaction_id': {'key': 'transactionId', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'instrument_uid': {'key': 'instrumentUid', 'type': 'str'},
        'transaction_date': {'key': 'transactionDate', 'type': 'iso-8601'},
        'settlement_date': {'key': 'settlementDate', 'type': 'iso-8601'},
        'units': {'key': 'units', 'type': 'float'},
        'transaction_price': {'key': 'transactionPrice', 'type': 'TransactionPrice'},
        'total_consideration': {'key': 'totalConsideration', 'type': 'CurrencyAndAmount'},
        'exchange_rate': {'key': 'exchangeRate', 'type': 'float'},
        'transaction_to_portfolio_rate': {'key': 'transactionToPortfolioRate', 'type': 'float'},
        'transaction_currency': {'key': 'transactionCurrency', 'type': 'str'},
        'properties': {'key': 'properties', 'type': '[PerpetualProperty]'},
        'counterparty_id': {'key': 'counterpartyId', 'type': 'str'},
        'source': {'key': 'source', 'type': 'str'},
        'netting_set': {'key': 'nettingSet', 'type': 'str'},
        'transaction_status': {'key': 'transactionStatus', 'type': 'str'},
        'entry_date_time': {'key': 'entryDateTime', 'type': 'iso-8601'},
        'cancel_date_time': {'key': 'cancelDateTime', 'type': 'iso-8601'},
        'realised_gain_loss': {'key': 'realisedGainLoss', 'type': '[RealisedGainLoss]'},
    }

    def __init__(self):
        super(OutputTransaction, self).__init__()
        self.transaction_id = None
        self.type = None
        self.description = None
        self.instrument_uid = None
        self.transaction_date = None
        self.settlement_date = None
        self.units = None
        self.transaction_price = None
        self.total_consideration = None
        self.exchange_rate = None
        self.transaction_to_portfolio_rate = None
        self.transaction_currency = None
        self.properties = None
        self.counterparty_id = None
        self.source = None
        self.netting_set = None
        self.transaction_status = None
        self.entry_date_time = None
        self.cancel_date_time = None
        self.realised_gain_loss = None
