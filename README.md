# LUSID<sup>®</sup> Python SDK
This is the Python SDK for [LUSID by FINBOURNE](https://www.finbourne.com/lusid-technology), a bi-temporal investment management data platform with portfolio accounting capabilities. To use it you'll need a LUSID account. [Sign up for free at lusid.com](https://www.lusid.com/app/signup)

<a href="https://www.lusid.com/app/signup"><img src="https://content.finbourne.com/LUSID_repo.png" alt="LUSID_by_Finbourne"></a>

## Installation

The PyPi package for the LUSID SDK can installed using the following:

```
pip install lusid-sdk
```

We publish two versions of the Python SDK:

* **lusid-sdk-python (this one) - supports `Production` and `Early Access` API endpoints**
* [lusid-sdk-python-preview](https://github.com/finbourne/lusid-sdk-python-preview) - supports `Production`, `Early Access`, `Beta` and `Experimental` API endpoints.

For more details on API endpoint categories, see [What is the LUSID feature release lifecycle?](https://support.lusid.com/knowledgebase/article/KA-01786/en-us).
To find out which category an API endpoint falls into, see [LUSID API Documentation](https://www.lusid.com/api/swagger/index.html).

> If you install both `lusid-sdk-python` and `lusid-sdk-python-preview`, `import lusid` will refer to `lusid-sdk-python`. 

## Usage

### Create API Client

First, import the following LUSID modules:


```python
import lusid
import lusid.models as models
from lusid.utilities import ApiConfigurationLoader
```

And construct the API factory:

```python
secrets_file_path = "/path/to/secrets.json"
config = ApiConfigurationLoader.load(secrets_file_path)
api_factory = lusid.utilities.ApiClientFactory(
    token=lusid.utilities.RefreshingToken(config),
    api_secrets_filename=secrets_file_path
)
```

> You will need to create a secrets file containing your LUSID credentials. For instructions on how to construct this file, see [Getting started with the LUSID API and SDKs](https://support.lusid.com/knowledgebase/article/KA-01916/)

Now that the API client is ready, you are ready to use the various API endpoints.
You can list all the API endpoints by running the following: 

```python
[api for api in dir(lusid.api) if "API" in api]
```

An API endpoint can be constructed by calling `api_factory.build(lusid.api.<className>)` for any of the returned classes.

### Code Samples

Before running the examples, import the following modules:

```python
import uuid
import datetime
import pytz
```

The examples below should be run in order, as they assume that the preceding code has been executed.

> Sets of working examples for using this SDK are available in the [Python examples repo](https://github.com/finbourne/lusid-sdk-examples-python).

#### Create portfolio

```python
tx_portfolios_api = api_factory.build(lusid.api.TransactionPortfoliosApi)

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
```

#### Upsert instruments

```python
instruments_api = api_factory.build(lusid.api.InstrumentsApi)

# FIGI is from https://www.openfigi.com/id/BBG000C6K6G9
figis_to_create = {
    "BBG000C6K6G9": models.InstrumentDefinition(name="VODAFONE GROUP PLC",
        identifiers={"Figi": models.InstrumentIdValue(value="BBG000C6K6G9")}
    )
}

instruments_api.upsert_instruments(request_body=figis_to_create)
```

#### Get instruments

```python
instruments_response = instruments_api.get_instruments(
    identifier_type="Figi", request_body=list(figis_to_create.keys()))
name_to_luid = {
    value.name: value.lusid_instrument_id
    for _, value in instruments_response.values.items()
}
luid_to_name = {v: k for k, v in name_to_luid.items()}
```

#### Upsert transactions

```python
tx_portfolios_api = api_factory.build(lusid.api.TransactionPortfoliosApi)

tx1 = models.TransactionRequest(
    transaction_id=f"Transaction-{uuid.uuid4()}",
    type="StockIn",
    instrument_identifiers={"Instrument/default/LusidInstrumentId": name_to_luid["VODAFONE GROUP PLC"]},
    transaction_date=datetime.datetime(2021, 3, 27, tzinfo=pytz.utc).isoformat(),
    settlement_date=datetime.datetime(2021, 3, 28, tzinfo=pytz.utc).isoformat(),
    units=100,
    transaction_price=models.TransactionPrice(price=103),
    total_consideration=models.CurrencyAndAmount(amount=103 * 100, currency="GBP"),
    source="Broker"
)

tx_portfolios_api.upsert_transactions(scope=scope, code=portfolio_code, transaction_request=[tx1])
```

#### Get holdings

```python
tx_portfolios_api = api_factory.build(lusid.api.TransactionPortfoliosApi)

holdings_response = tx_portfolios_api.get_holdings(
    scope=scope, code=portfolio_code, property_keys=["Instrument/default/Name"]).values

print("Holdings:")
for holding in holdings_response:
    print(luid_to_name[holding.instrument_uid], holding.units, holding.cost.amount)
```

For more fully fledged examples showing how to use the SDK, see [sdk/tests/tutorials](sdk/tests/tutorials)

## Manually building the SDK

A pre-generated version of the latest SDK is included in the `sdk` folder. 
This is based on the [OpenAPI specification](https://github.com/OAI/OpenAPI-Specification) specification named `lusid.json` in the root folder. The most up to date version of the OpenAPI specification can be downloaded from [api.lusid.com/swagger/v0/swagger.json](https://api.lusid.com/swagger/v0/swagger.json).

If you want to generate the Python SDK locally from the FINBOURNE OpenAPI specification, see [github.com/finbourne/lusid-sdk-generators](https://github.com/finbourne/lusid-sdk-generators).

## Build status 

| branch | status |
| --- | --- |
| `master` | ![PyPI](https://img.shields.io/pypi/v/lusid-sdk?color=blue) ![run-sdk-tests](https://github.com/finbourne/lusid-sdk-python/workflows/run-sdk-tests/badge.svg?branch=master) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=finbourne_lusid-sdk-python&metric=alert_status)](https://sonarcloud.io/dashboard?id=finbourne_lusid-sdk-python) |
| `develop` | ![run-sdk-tests](https://github.com/finbourne/lusid-sdk-python/workflows/run-sdk-tests/badge.svg?branch=develop) |
