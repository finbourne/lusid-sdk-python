import unittest
import pytz
import json
import logging

from datetime import datetime

import lusid
import lusid.models as models

from lusidfeature import lusid_feature
from utilities import TestDataUtilities
from utilities import InstrumentLoader


class ReferencePortfolio(unittest.TestCase):
    @classmethod
    def setUpClass(cls):

        # Log any exceptions
        cls.logger = logging.getLogger()
        cls.logger.setLevel(logging.INFO)

        # Create API client
        api_client = TestDataUtilities.api_client()

        # Instantiate APIs we will use
        cls.reference_portfolio_api = lusid.ReferencePortfolioApi(api_client)
        cls.portfolios_api = lusid.PortfoliosApi(api_client)
        cls.instruments_api = lusid.InstrumentsApi(api_client)

        # Load instruments
        cls.instrument_loader = InstrumentLoader(cls.instruments_api)
        cls.instrument_ids = cls.instrument_loader.load_instruments()

    @lusid_feature("F6-1")
    def test_create_reference_portfolio(self):

        f39_reference_portfolio_code = "F39p_ReferencePortfolioCode"
        f39_reference_portfolio_name = "F39p_Reference Portfolio Name"

        # Details of the new reference portfolio to be created
        request = models.CreateReferencePortfolioRequest(
            display_name=f39_reference_portfolio_name,
            code=f39_reference_portfolio_code,
        )

        # Create the reference portfolio in LUSID in the tutorials scope
        result = self.reference_portfolio_api.create_reference_portfolio(
            scope=TestDataUtilities.tutorials_scope,
            create_reference_portfolio_request=request,
        )

        self.assertEqual(result.id.code, request.code)

        # Delete portfolio once the test is complete
        self.portfolios_api.delete_portfolio(
            scope=TestDataUtilities.tutorials_scope, code=f39_reference_portfolio_code
        )

    @lusid_feature("F6-2")
    def test_upsert_reference_portfolio_constituents(self):

        constituent_weights = [10, 20, 30, 15, 25]
        effective_date = datetime(year=2021, month=3, day=29, tzinfo=pytz.UTC)

        f40_reference_portfolio_code = "F40p_ReferencePortfolioCode"
        f40_reference_portfolio_name = "F40p_Reference Portfolio Name"


        # Create a new reference portfolio
        request = models.CreateReferencePortfolioRequest(
            display_name=f40_reference_portfolio_name,
            code=f40_reference_portfolio_code,
            created=effective_date,
        )

        self.reference_portfolio_api.create_reference_portfolio(
            scope=TestDataUtilities.tutorials_scope,
            create_reference_portfolio_request=request,
        )

        # Check that all instruments were created successfully
        self.assertEqual(len(constituent_weights), len(self.instrument_ids))

        # Create the constituent requests
        individual_constituent_requests = [
            models.ReferencePortfolioConstituentRequest(
                instrument_identifiers={
                    TestDataUtilities.lusid_luid_identifier: instrument_id
                },
                weight=constituent_weight,
                currency="GBP",
            )
            for instrument_id, constituent_weight in zip(
                self.instrument_ids, constituent_weights
            )
        ]

        # Create a bulk constituent upsert request
        bulk_constituent_request = models.UpsertReferencePortfolioConstituentsRequest(
            effective_from=effective_date,
            weight_type="Static",
            constituents=individual_constituent_requests,
        )

        # Make the upsert request via the reference portfolio API
        self.reference_portfolio_api.upsert_reference_portfolio_constituents(
            scope=TestDataUtilities.tutorials_scope,
            code=f40_reference_portfolio_code,
            upsert_reference_portfolio_constituents_request=bulk_constituent_request,
        )

        # Get reference portfolio holdings
        constituent_holdings = (
            self.reference_portfolio_api.get_reference_portfolio_constituents(
                scope=TestDataUtilities.tutorials_scope,
                code=f40_reference_portfolio_code,
            )
        )

        # Validate count of holdings
        self.assertEqual(len(constituent_holdings.constituents), 5)

        # Validate instruments on holdings
        for constituent, upserted_instrument in zip(
            constituent_holdings.constituents, self.instrument_ids
        ):
            self.assertEqual(constituent.instrument_uid, upserted_instrument)

        # Validate holding weights
        for constituent, weight in zip(
            constituent_holdings.constituents, constituent_weights
        ):
            self.assertEqual(constituent.weight, weight)

        # Delete portfolio once the test is complete
        self.portfolios_api.delete_portfolio(
            scope=TestDataUtilities.tutorials_scope, code=f40_reference_portfolio_code
        )
