from datetime import datetime

import pytz
import uuid
import lusid
import lusid.models as models


class TestDataUtilities:

    tutorials_scope = "Testdemo"

    lusid_cash_identifier = "Instrument/default/Currency"
    lusid_luid_identifier = "Instrument/default/LusidInstrumentId"

    def __init__(self, transaction_portfolio_api: lusid.TransactionPortfoliosApi):
        self.transaction_portfolio_api = transaction_portfolio_api

    def create_transaction_portfolio(self, scope):
        guid = str(uuid.uuid4())

        # Effective date of the portfolio, this is the date the portfolio was created and became live.
        # All dates/times must be supplied in UTC
        effective_date = datetime(2018, 1, 1, tzinfo=pytz.utc)

        # Details of the new portfolio to be created, created here with the minimum set of mandatory fields
        request = models.CreateTransactionPortfolioRequest(display_name="Portfolio-{}".format(guid),
                                                           code="Id-{}".format(guid),
                                                           base_currency="GBP",
                                                           created=effective_date)

        # Create the portfolio in LUSID
        portfolio = self.transaction_portfolio_api.create_portfolio(scope, create_request=request)

        assert(portfolio.id.code == request.code)

        return portfolio.id.code

    def build_transaction_request(self, instrument_id, units, price, currency, trade_date, transaction_type):
        return models.TransactionRequest(transaction_id=str(uuid.uuid4()),
                                         type=transaction_type,
                                         instrument_identifiers={self.lusid_luid_identifier: instrument_id},
                                         transaction_date=trade_date,
                                         settlement_date=trade_date,
                                         units=units,
                                         transaction_price=models.TransactionPrice(price=price),
                                         total_consideration=models.CurrencyAndAmount(amount=price*units, currency=currency),
                                         source="Broker")

    def build_cash_fundsin_transaction_request(self, units, currency, trade_date):
        return models.TransactionRequest(transaction_id=str(uuid.uuid4()),
                                         type="FundsIn",
                                         instrument_identifiers={self.lusid_cash_identifier: currency},
                                         transaction_date=trade_date,
                                         settlement_date=trade_date,
                                         units=units,
                                         total_consideration=models.CurrencyAndAmount(currency=currency),
                                         transaction_price=models.TransactionPrice(price=0.0),
                                         source="Client")

