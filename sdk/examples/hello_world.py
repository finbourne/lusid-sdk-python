# tag::lusid-imports[]
# LUSID imports
import lusid
import lusid.models as models
from lusid.utilities import ApiConfigurationLoader

# Other imports
import uuid
import datetime
import pytz
# end::lusid-imports[]

# tag::create-client-factory[]
secrets_file_path = "/path/to/secrets.json"
config = ApiConfigurationLoader.load(secrets_file_path)
api_factory = lusid.utilities.ApiClientFactory(
    token=lusid.utilities.RefreshingToken(config),
    api_secrets_filename=secrets_file_path
)
# end::create-client-factory[]

# Create portfolio
# tag::create-tx-portfolios-api[]
tx_portfolios_api = api_factory.build(lusid.api.TransactionPortfoliosApi)
# end::create-tx-portfolios-api[]

# tag::create-portfolio[]
scope = "GettingStartedScope"
guid = uuid.uuid4()

portfolio_request = models.CreateTransactionPortfolioRequest(
    display_name=f"Portfolio-{guid}",
    code=f"Id-{guid}",
    base_currency="GBP",
    created=datetime.datetime(2021, 3, 20, tzinfo=pytz.utc)
)

portfolio = tx_portfolios_api.create_portfolio(scope, create_transaction_portfolio_request=portfolio_request)
portfolio_code = portfolio.id.code
print("Porfolio Code:", portfolio_code)
# end::create-portfolio[]

# tag::upsert-instruments[]
instruments_api = api_factory.build(lusid.api.InstrumentsApi)

# FIGI is from https://www.openfigi.com/id/BBG000C6K6G9
figis_to_create = {
    "BBG000C6K6G9": models.InstrumentDefinition(name="VODAFONE GROUP PLC",
        identifiers={"Figi": models.InstrumentIdValue(value="BBG000C6K6G9")}
    )
}

instruments_api.upsert_instruments(request_body=figis_to_create)
# end::upsert-instruments[]

# tag::get-instruments[]
instruments_response = instruments_api.get_instruments(
    identifier_type="Figi", request_body=list(figis_to_create.keys()))
name_to_luid = {
    value.name: value.lusid_instrument_id
    for _, value in instruments_response.values.items()
}
luid_to_name = {v: k for k, v in name_to_luid.items()}
# end::get-instruments[]

# tag::upsert-transactions[]
tx_portfolios_api = api_factory.build(lusid.api.TransactionPortfoliosApi)

tx1 = models.TransactionRequest(
    transaction_id=f"Transaction-{uuid.uuid4()}",
    type="StockIn",
    instrument_identifiers={"Instrument/default/LusidInstrumentId": name_to_luid["VODAFONE GROUP PLC"]},
    transaction_date=datetime.datetime(2021, 3, 27, tzinfo=pytz.utc),
    settlement_date=datetime.datetime(2021, 3, 28, tzinfo=pytz.utc),
    units=100,
    transaction_price=models.TransactionPrice(price=103),
    total_consideration=models.CurrencyAndAmount(amount=103 * 100, currency="GBP"),
    source="Broker"
)

tx_portfolios_api.upsert_transactions(scope=scope, code=portfolio_code, transaction_request=[tx1])
# end::upsert-transactions[]

# tag::get-holdings[]
tx_portfolios_api = api_factory.build(lusid.api.TransactionPortfoliosApi)

holdings_response = tx_portfolios_api.get_holdings(
    scope=scope, code=portfolio_code, property_keys=["Instrument/default/Name"]).values

print("Holdings:")
for holding in holdings_response:
    print(luid_to_name[holding.instrument_uid], holding.units, holding.cost.amount)