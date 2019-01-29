import unittest
import requests
import json
import uuid
import os
from datetime import datetime
import pytz
import lusid
import lusid.models as models
from unittest import TestCase
from collections import namedtuple
from msrest.authentication import BasicTokenAuthentication
from time import sleep

try:
    # Python 3.x
    from urllib.request import pathname2url
except ImportError:
    # Python 2.7
    from urllib import pathname2url


class TestDataUtilities(object):
    # any class attributes?
    def __init__(self, client):
        self.client = client


    def create_transaction_portfolio(self, scope):

        uuid_gen = uuid.uuid4()
        effective_date = datetime(2018, 1, 1, tzinfo=pytz.utc)

        # portfolio request
        original_portfolio_id = "Id-" + str(uuid_gen)
        request = models.CreateTransactionPortfolioRequest("Portfolio-" + str(uuid_gen),
                                                           original_portfolio_id,
                                                           base_currency="GBP",
                                                           created=effective_date)
        # create the portfolio
        portfolio_response = self.client.create_portfolio(scope, request)

        assert portfolio_response.id.code == request.code

        return portfolio_response.id.code

    def build_transaction_request(self, instrument_id, units, price, currency, trade_date, transaction_type):

        tran_response = models.TransactionRequest(
                                                        transaction_id=str(uuid.uuid4()),
                                                        type=transaction_type,
                                                        instrument_uid=instrument_id,
                                                        transaction_date=trade_date,
                                                        settlement_date=trade_date,
                                                        units=units,
                                                        transaction_price=models.TransactionPrice(price),
                                                        total_consideration=models.CurrencyAndAmount(units*price, currency),
                                                        source="Client")

        return tran_response

    def build_cash_funds_in_transaction_request(self, units, currency, trade_date):

        tran_response = models.TransactionRequest(
                                                        transaction_id=str(uuid.uuid4()),
                                                        type="FundsIn",
                                                        instrument_uid="CCY_" + currency,
                                                        transaction_date=trade_date,
                                                        settlement_date=trade_date,
                                                        units=units,
                                                        transaction_price=models.TransactionPrice(0),
                                                        total_consideration=models.CurrencyAndAmount(0, currency),
                                                        source="Client")

        return tran_response
