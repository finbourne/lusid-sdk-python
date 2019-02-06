import uuid
from datetime import datetime
import pytz
import lusid.models as models

try:
    # Python 3.x
    from urllib.request import pathname2url
except ImportError:
    # Python 2.7
    from urllib import pathname2url


class TestDataUtilities(object):

    @classmethod
    def create_transaction_portfolio(cls, client, scope):

        uuid_gen = uuid.uuid4()
        effective_date = datetime(2018, 1, 1, tzinfo=pytz.utc)

        # portfolio request
        original_portfolio_id = "Id-" + str(uuid_gen)
        request = models.CreateTransactionPortfolioRequest("Portfolio-" + str(uuid_gen),
                                                           original_portfolio_id,
                                                           base_currency="GBP",
                                                           created=effective_date)
        # create the portfolio
        portfolio_response = client.create_portfolio(scope, request)

        assert portfolio_response.id.code == request.code

        return portfolio_response.id.code

    @classmethod
    def build_transaction_request(cls, instrument_id, units, price, currency, trade_date, transaction_type):

        tran_request = models.TransactionRequest(
            transaction_id=str(uuid.uuid4()),
            type=transaction_type,
            instrument_uid=instrument_id,
            transaction_date=trade_date,
            settlement_date=trade_date,
            units=units,
            transaction_price=models.TransactionPrice(price),
            total_consideration=models.CurrencyAndAmount(units*price, currency),
            source="Client")

        return tran_request

    @classmethod
    def build_cash_funds_in_transaction_request(cls, units, currency, trade_date):

        tran_request = models.TransactionRequest(
            transaction_id=str(uuid.uuid4()),
            type="FundsIn",
            instrument_uid="CCY_" + currency,
            transaction_date=trade_date,
            settlement_date=trade_date,
            units=units,
            transaction_price=models.TransactionPrice(0),
            total_consideration=models.CurrencyAndAmount(0, currency),
            source="Client")

        return tran_request
