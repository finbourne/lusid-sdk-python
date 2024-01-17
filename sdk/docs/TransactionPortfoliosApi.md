# lusid.TransactionPortfoliosApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adjust_holdings**](TransactionPortfoliosApi.md#adjust_holdings) | **POST** /api/transactionportfolios/{scope}/{code}/holdings | AdjustHoldings: Adjust holdings
[**batch_adjust_holdings**](TransactionPortfoliosApi.md#batch_adjust_holdings) | **POST** /api/transactionportfolios/{scope}/{code}/holdings/$batchAdjust | [EARLY ACCESS] BatchAdjustHoldings: Batch adjust holdings
[**batch_upsert_transactions**](TransactionPortfoliosApi.md#batch_upsert_transactions) | **POST** /api/transactionportfolios/{scope}/{code}/transactions/$batchUpsert | [EARLY ACCESS] BatchUpsertTransactions: Batch upsert transactions
[**build_transactions**](TransactionPortfoliosApi.md#build_transactions) | **POST** /api/transactionportfolios/{scope}/{code}/transactions/$build | BuildTransactions: Build transactions
[**cancel_adjust_holdings**](TransactionPortfoliosApi.md#cancel_adjust_holdings) | **DELETE** /api/transactionportfolios/{scope}/{code}/holdings | CancelAdjustHoldings: Cancel adjust holdings
[**cancel_transactions**](TransactionPortfoliosApi.md#cancel_transactions) | **DELETE** /api/transactionportfolios/{scope}/{code}/transactions | CancelTransactions: Cancel transactions
[**create_portfolio**](TransactionPortfoliosApi.md#create_portfolio) | **POST** /api/transactionportfolios/{scope} | CreatePortfolio: Create portfolio
[**create_trade_ticket**](TransactionPortfoliosApi.md#create_trade_ticket) | **POST** /api/transactionportfolios/{scope}/{code}/$tradeticket | [EXPERIMENTAL] CreateTradeTicket: Create Trade Ticket
[**delete_custodian_accounts**](TransactionPortfoliosApi.md#delete_custodian_accounts) | **POST** /api/transactionportfolios/{scope}/{code}/custodianaccounts/$delete | [EXPERIMENTAL] DeleteCustodianAccounts: Soft or hard delete multiple custodian accounts
[**delete_properties_from_transaction**](TransactionPortfoliosApi.md#delete_properties_from_transaction) | **DELETE** /api/transactionportfolios/{scope}/{code}/transactions/{transactionId}/properties | DeletePropertiesFromTransaction: Delete properties from transaction
[**get_a2_b_data**](TransactionPortfoliosApi.md#get_a2_b_data) | **GET** /api/transactionportfolios/{scope}/{code}/a2b | GetA2BData: Get A2B data
[**get_a2_b_movements**](TransactionPortfoliosApi.md#get_a2_b_movements) | **GET** /api/transactionportfolios/{scope}/{code}/a2bmovements | GetA2BMovements: Get an A2B report at the movement level for the given portfolio.
[**get_bucketed_cash_flows**](TransactionPortfoliosApi.md#get_bucketed_cash_flows) | **POST** /api/transactionportfolios/{scope}/{code}/bucketedCashFlows | [EXPERIMENTAL] GetBucketedCashFlows: Get bucketed cash flows from a list of portfolios
[**get_custodian_account**](TransactionPortfoliosApi.md#get_custodian_account) | **GET** /api/transactionportfolios/{scope}/{code}/custodianaccounts/{custodianAccountScope}/{custodianAccountCode} | [EXPERIMENTAL] GetCustodianAccount: Get Custodian Account
[**get_details**](TransactionPortfoliosApi.md#get_details) | **GET** /api/transactionportfolios/{scope}/{code}/details | GetDetails: Get details
[**get_holding_contributors**](TransactionPortfoliosApi.md#get_holding_contributors) | **GET** /api/transactionportfolios/{scope}/{code}/holdings/{holdingId}/contributors | [EXPERIMENTAL] GetHoldingContributors: Get Holdings Contributors
[**get_holdings**](TransactionPortfoliosApi.md#get_holdings) | **GET** /api/transactionportfolios/{scope}/{code}/holdings | GetHoldings: Get holdings
[**get_holdings_adjustment**](TransactionPortfoliosApi.md#get_holdings_adjustment) | **GET** /api/transactionportfolios/{scope}/{code}/holdingsadjustments/{effectiveAt} | GetHoldingsAdjustment: Get holdings adjustment
[**get_holdings_with_orders**](TransactionPortfoliosApi.md#get_holdings_with_orders) | **GET** /api/transactionportfolios/{scope}/{code}/holdingsWithOrders | [EXPERIMENTAL] GetHoldingsWithOrders: Get holdings with orders
[**get_portfolio_cash_flows**](TransactionPortfoliosApi.md#get_portfolio_cash_flows) | **GET** /api/transactionportfolios/{scope}/{code}/cashflows | [BETA] GetPortfolioCashFlows: Get portfolio cash flows
[**get_portfolio_cash_ladder**](TransactionPortfoliosApi.md#get_portfolio_cash_ladder) | **GET** /api/transactionportfolios/{scope}/{code}/cashladder | GetPortfolioCashLadder: Get portfolio cash ladder
[**get_portfolio_cash_statement**](TransactionPortfoliosApi.md#get_portfolio_cash_statement) | **GET** /api/transactionportfolios/{scope}/{code}/cashstatement | GetPortfolioCashStatement: Get portfolio cash statement
[**get_transaction_history**](TransactionPortfoliosApi.md#get_transaction_history) | **GET** /api/transactionportfolios/{scope}/{code}/transactions/{transactionId}/history | [EARLY ACCESS] GetTransactionHistory: Get the history of a transaction
[**get_transactions**](TransactionPortfoliosApi.md#get_transactions) | **GET** /api/transactionportfolios/{scope}/{code}/transactions | GetTransactions: Get transactions
[**get_upsertable_portfolio_cash_flows**](TransactionPortfoliosApi.md#get_upsertable_portfolio_cash_flows) | **GET** /api/transactionportfolios/{scope}/{code}/upsertablecashflows | [BETA] GetUpsertablePortfolioCashFlows: Get upsertable portfolio cash flows.
[**list_custodian_accounts**](TransactionPortfoliosApi.md#list_custodian_accounts) | **GET** /api/transactionportfolios/{scope}/{code}/custodianaccounts | [EXPERIMENTAL] ListCustodianAccounts: List Custodian Accounts
[**list_holdings_adjustments**](TransactionPortfoliosApi.md#list_holdings_adjustments) | **GET** /api/transactionportfolios/{scope}/{code}/holdingsadjustments | ListHoldingsAdjustments: List holdings adjustments
[**look_through_holdings**](TransactionPortfoliosApi.md#look_through_holdings) | **GET** /api/transactionportfolios/{scope}/{code}/holdings/$lookthrough | [EXPERIMENTAL] LookThroughHoldings: Get LookThrough Holdings
[**look_through_transactions**](TransactionPortfoliosApi.md#look_through_transactions) | **GET** /api/transactionportfolios/{scope}/{code}/transactions/$lookthrough | [EXPERIMENTAL] LookThroughTransactions: Look through transactions
[**patch_portfolio_details**](TransactionPortfoliosApi.md#patch_portfolio_details) | **PATCH** /api/transactionportfolios/{scope}/{code}/details | [EARLY ACCESS] PatchPortfolioDetails: Patch portfolio details
[**resolve_instrument**](TransactionPortfoliosApi.md#resolve_instrument) | **POST** /api/transactionportfolios/{scope}/{code}/$resolve | [EARLY ACCESS] ResolveInstrument: Resolve instrument
[**set_holdings**](TransactionPortfoliosApi.md#set_holdings) | **PUT** /api/transactionportfolios/{scope}/{code}/holdings | SetHoldings: Set holdings
[**upsert_custodian_accounts**](TransactionPortfoliosApi.md#upsert_custodian_accounts) | **POST** /api/transactionportfolios/{scope}/{code}/custodianaccounts | [EXPERIMENTAL] UpsertCustodianAccounts: Upsert Custodian Accounts
[**upsert_custodian_accounts_properties**](TransactionPortfoliosApi.md#upsert_custodian_accounts_properties) | **POST** /api/transactionportfolios/{scope}/{code}/custodianaccounts/{custodianAccountScope}/{custodianAccountCode}/properties/$upsert | [EXPERIMENTAL] UpsertCustodianAccountsProperties: Upsert custodian accounts properties
[**upsert_portfolio_details**](TransactionPortfoliosApi.md#upsert_portfolio_details) | **POST** /api/transactionportfolios/{scope}/{code}/details | UpsertPortfolioDetails: Upsert portfolio details
[**upsert_transaction_properties**](TransactionPortfoliosApi.md#upsert_transaction_properties) | **POST** /api/transactionportfolios/{scope}/{code}/transactions/{transactionId}/properties | UpsertTransactionProperties: Upsert transaction properties
[**upsert_transactions**](TransactionPortfoliosApi.md#upsert_transactions) | **POST** /api/transactionportfolios/{scope}/{code}/transactions | UpsertTransactions: Upsert transactions


# **adjust_holdings**
> AdjustHolding adjust_holdings(scope, code, effective_at, adjust_holding_request, reconciliation_methods=reconciliation_methods)

AdjustHoldings: Adjust holdings

Adjust one or more holdings of the specified transaction portfolio to the provided targets. LUSID will  automatically construct adjustment transactions to ensure that the holdings which have been adjusted are  always set to the provided targets for the specified effective datetime. Read more about the difference between  adjusting and setting holdings here https://support.lusid.com/how-do-i-adjust-my-holdings.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from lusid.models.adjust_holding import AdjustHolding
from lusid.models.adjust_holding_request import AdjustHoldingRequest
from pprint import pprint

from lusid import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
	  EnvironmentVariablesConfigurationLoader,
	  SecretsFileConfigurationLoader,
	  ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
    code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which the holdings should be set to the provided targets.
    adjust_holding_request = [{"instrumentIdentifiers":{"Instrument/default/Figi":"BBG000C6K6G9","Instrument/default/Isin":"GB00BH4HKS39"},"subHoldingKeys":{"Transaction/Algo/Name":{"key":"Transaction/Algo/Name","value":{"labelValue":"Algo1"}}},"properties":{"Holding/ibor/CurrentMarketValue":{"key":"Holding/ibor/CurrentMarketValue","value":{"metricValue":{"value":1000}}}},"taxLots":[{"units":100,"cost":{"amount":10000,"currency":"GBP"},"portfolioCost":10000,"price":100,"purchaseDate":"2018-03-05T00:00:00.0000000+00:00","settlementDate":"2018-03-08T00:00:00.0000000+00:00"}],"currency":"GBP"}] # List[AdjustHoldingRequest] | The selected set of holdings to adjust to the provided targets for the              transaction portfolio.
    reconciliation_methods = ['reconciliation_methods_example'] # List[str] | Optional parameter for specifying a reconciliation method: e.g. FxForward. (optional)

    try:
        # AdjustHoldings: Adjust holdings
        api_response = await api_instance.adjust_holdings(scope, code, effective_at, adjust_holding_request, reconciliation_methods=reconciliation_methods)
        print("The response of TransactionPortfoliosApi->adjust_holdings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionPortfoliosApi->adjust_holdings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. | 
 **effective_at** | **str**| The effective datetime or cut label at which the holdings should be set to the provided targets. | 
 **adjust_holding_request** | [**List[AdjustHoldingRequest]**](AdjustHoldingRequest.md)| The selected set of holdings to adjust to the provided targets for the              transaction portfolio. | 
 **reconciliation_methods** | [**List[str]**](str.md)| Optional parameter for specifying a reconciliation method: e.g. FxForward. | [optional] 

### Return type

[**AdjustHolding**](AdjustHolding.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The version of the transaction portfolio that contains the newly adjusted holdings |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_adjust_holdings**
> BatchAdjustHoldingsResponse batch_adjust_holdings(scope, code, success_mode, request_body, reconciliation_methods=reconciliation_methods)

[EARLY ACCESS] BatchAdjustHoldings: Batch adjust holdings

Adjust one or more holdings of the specified transaction portfolio to the provided targets. LUSID will  automatically construct adjustment transactions to ensure that the holdings which have been adjusted are  always set to the provided targets for the specified effective datetime in each request.                Each request must be keyed by a unique correlation id. This id is ephemeral and is not stored by LUSID.  It serves only as a way to easily identify each adjustment in the response.    Note: If using partial failure modes, then it is important to check the response body for failures as any failures will still return a 200 status code

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from lusid.models.adjust_holding_for_date_request import AdjustHoldingForDateRequest
from lusid.models.batch_adjust_holdings_response import BatchAdjustHoldingsResponse
from pprint import pprint

from lusid import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
	  EnvironmentVariablesConfigurationLoader,
	  SecretsFileConfigurationLoader,
	  ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
    code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies               the transaction portfolio.
    success_mode = 'Partial' # str | Whether the batch request should fail Atomically or in a Partial fashion - Allowed Values: Atomic, Partial (default to 'Partial')
    request_body = {"AdjustHoldingRequest1":{"effectiveAt":"2018-03-05T00:00:00.0000000+00:00","instrumentIdentifiers":{"Instrument/default/Figi":"BBG000C6K6G9","Instrument/default/Isin":"GB00BH4HKS39"},"subHoldingKeys":{"Transaction/Algo/Name":{"key":"Transaction/Algo/Name","value":{"labelValue":"Algo1"}}},"properties":{"Holding/Entity/Name":{"key":"Holding/Entity/Name","value":{"labelValue":"Financial Entity"}}},"taxLots":[{"units":100,"cost":{"amount":10000,"currency":"GBP"},"portfolioCost":10000,"price":100,"purchaseDate":"2018-03-05T00:00:00.0000000+00:00","settlementDate":"2018-03-08T00:00:00.0000000+00:00"}],"currency":"GBP"},"AdjustHoldingRequest2":{"effectiveAt":"2019-10-02T00:00:00.0000000+00:00","instrumentIdentifiers":{"Instrument/default/Figi":"CCG000C6K6G9","Instrument/default/Isin":"US00BH4HKS39"},"subHoldingKeys":{"Transaction/Algo/Name":{"key":"Transaction/Algo/Name","value":{"labelValue":"Algo1"}}},"properties":{"Holding/Entity/Name":{"key":"Holding/Entity/Name","value":{"labelValue":"Financial Entity"}}},"taxLots":[{"units":50,"cost":{"amount":500,"currency":"USD"},"portfolioCost":500,"price":50,"purchaseDate":"2019-03-05T00:00:00.0000000+00:00","settlementDate":"2019-03-08T00:00:00.0000000+00:00"}],"currency":"GBP"}} # Dict[str, AdjustHoldingForDateRequest] | The selected set of holdings to adjust to the provided targets for the               transaction portfolio.
    reconciliation_methods = ['reconciliation_methods_example'] # List[str] | Optional parameter for specifying a reconciliation method: e.g. FxForward. (optional)

    try:
        # [EARLY ACCESS] BatchAdjustHoldings: Batch adjust holdings
        api_response = await api_instance.batch_adjust_holdings(scope, code, success_mode, request_body, reconciliation_methods=reconciliation_methods)
        print("The response of TransactionPortfoliosApi->batch_adjust_holdings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionPortfoliosApi->batch_adjust_holdings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this uniquely identifies               the transaction portfolio. | 
 **success_mode** | **str**| Whether the batch request should fail Atomically or in a Partial fashion - Allowed Values: Atomic, Partial | [default to &#39;Partial&#39;]
 **request_body** | [**Dict[str, AdjustHoldingForDateRequest]**](AdjustHoldingForDateRequest.md)| The selected set of holdings to adjust to the provided targets for the               transaction portfolio. | 
 **reconciliation_methods** | [**List[str]**](str.md)| Optional parameter for specifying a reconciliation method: e.g. FxForward. | [optional] 

### Return type

[**BatchAdjustHoldingsResponse**](BatchAdjustHoldingsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successful AdjustHolding requests along with any failures |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_upsert_transactions**
> BatchUpsertPortfolioTransactionsResponse batch_upsert_transactions(scope, code, success_mode, request_body, preserve_properties=preserve_properties)

[EARLY ACCESS] BatchUpsertTransactions: Batch upsert transactions

Create or update transactions in the transaction portfolio. A transaction will be updated  if it already exists and created if it does not.    Each request must be keyed by a unique correlation id. This id is ephemeral and is not stored by LUSID.  It serves only as a way to easily identify each transaction in the response.    Note: If using partial failure modes, then it is important to check the response body for failures as any failures will still return a 200 status code

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from lusid.models.batch_upsert_portfolio_transactions_response import BatchUpsertPortfolioTransactionsResponse
from lusid.models.transaction_request import TransactionRequest
from pprint import pprint

from lusid import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
	  EnvironmentVariablesConfigurationLoader,
	  SecretsFileConfigurationLoader,
	  ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
    code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
    success_mode = 'Partial' # str | Whether the batch request should fail Atomically or in a Partial fashion - Allowed Values: Atomic, Partial. (default to 'Partial')
    request_body = {"transactionRequest-1":{"transactionId":"TransactionId-111111","type":"StockIn","instrumentIdentifiers":{"Instrument/default/Figi":"BBG000C6K6G9","Instrument/default/Isin":"GB00BH4HKS39"},"transactionDate":"2018-03-05T00:00:00.0000000+00:00","settlementDate":"2018-03-08T00:00:00.0000000+00:00","units":1000,"transactionPrice":{"price":123,"type":"Price"},"totalConsideration":{"amount":123000,"currency":"GBP"},"transactionCurrency":"GBP","properties":{"Transaction/Algo/Name":{"key":"Transaction/Algo/Name","value":{"labelValue":"Algo1"}}},"counterpartyId":"CounterpartyId-118263","source":"","otcConfirmation":{"counterpartyAgreementId":{"scope":"someScope","code":"someCode"}},"orderId":{"scope":"someScope","code":"ORD001"},"allocationId":{"scope":"someScope","code":"ALLOC001"}},"transactionRequest-2":{"transactionId":"TransactionId-222222","type":"StockIn","instrumentIdentifiers":{"Instrument/default/Figi":"BBG000GJ45S5","Instrument/default/Isin":"GB00BFRLS45S"},"transactionDate":"2019-03-05T00:00:00.0000000+00:00","settlementDate":"2019-03-08T00:00:00.0000000+00:00","units":1000,"transactionPrice":{"price":123,"type":"Price"},"totalConsideration":{"amount":123000,"currency":"GBP"},"transactionCurrency":"GBP","properties":{"Transaction/Algo/Name":{"key":"Transaction/Algo/Name","value":{"labelValue":"Algo1"}}},"counterpartyId":"CounterpartyId-141556","source":"","otcConfirmation":{"counterpartyAgreementId":{"scope":"someScope","code":"someCode"}},"orderId":{"scope":"someScope","code":"ORD001"},"allocationId":{"scope":"someScope","code":"ALLOC001"}}} # Dict[str, TransactionRequest] | The payload describing the transactions to be created or updated.
    preserve_properties = True # bool | If set to false, the entire property set will be overwritten by the provided properties. If not specified or set to true, only the properties provided will be updated. (optional) (default to True)

    try:
        # [EARLY ACCESS] BatchUpsertTransactions: Batch upsert transactions
        api_response = await api_instance.batch_upsert_transactions(scope, code, success_mode, request_body, preserve_properties=preserve_properties)
        print("The response of TransactionPortfoliosApi->batch_upsert_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionPortfoliosApi->batch_upsert_transactions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. | 
 **success_mode** | **str**| Whether the batch request should fail Atomically or in a Partial fashion - Allowed Values: Atomic, Partial. | [default to &#39;Partial&#39;]
 **request_body** | [**Dict[str, TransactionRequest]**](TransactionRequest.md)| The payload describing the transactions to be created or updated. | 
 **preserve_properties** | **bool**| If set to false, the entire property set will be overwritten by the provided properties. If not specified or set to true, only the properties provided will be updated. | [optional] [default to True]

### Return type

[**BatchUpsertPortfolioTransactionsResponse**](BatchUpsertPortfolioTransactionsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully upserted transaction requests along with any failures |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **build_transactions**
> VersionedResourceListOfOutputTransaction build_transactions(scope, code, transaction_query_parameters, as_at=as_at, filter=filter, property_keys=property_keys, limit=limit, page=page)

BuildTransactions: Build transactions

Builds and returns all transactions that affect the holdings of a portfolio over a given interval of  effective time into a set of output transactions. This includes transactions automatically generated by  LUSID such as holding adjustments.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from lusid.models.transaction_query_parameters import TransactionQueryParameters
from lusid.models.versioned_resource_list_of_output_transaction import VersionedResourceListOfOutputTransaction
from pprint import pprint

from lusid import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
	  EnvironmentVariablesConfigurationLoader,
	  SecretsFileConfigurationLoader,
	  ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
    code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
    transaction_query_parameters = {"startDate":"2018-03-05T00:00:00.0000000+00:00","endDate":"2018-03-19T00:00:00.0000000+00:00","queryMode":"TradeDate","showCancelledTransactions":false} # TransactionQueryParameters | The query queryParameters which control how the output transactions are built.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to build the transactions. Defaults to return the latest              version of each transaction if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the result set.              For example, to return only transactions with a transaction type of 'Buy', specify \"type eq 'Buy'\".              For more information about filtering LUSID results, see https://support.lusid.com/knowledgebase/article/KA-01914. (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the \"Instrument\" or \"Transaction\" domain to decorate onto              the transactions. These take the format {domain}/{scope}/{code} e.g. \"Instrument/system/Name\" or              \"Transaction/strategy/quantsignal\". (optional)
    limit = 56 # int | When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing transactions from a previous call to BuildTransactions. (optional)

    try:
        # BuildTransactions: Build transactions
        api_response = await api_instance.build_transactions(scope, code, transaction_query_parameters, as_at=as_at, filter=filter, property_keys=property_keys, limit=limit, page=page)
        print("The response of TransactionPortfoliosApi->build_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionPortfoliosApi->build_transactions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. | 
 **transaction_query_parameters** | [**TransactionQueryParameters**](TransactionQueryParameters.md)| The query queryParameters which control how the output transactions are built. | 
 **as_at** | **datetime**| The asAt datetime at which to build the transactions. Defaults to return the latest              version of each transaction if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set.              For example, to return only transactions with a transaction type of &#39;Buy&#39;, specify \&quot;type eq &#39;Buy&#39;\&quot;.              For more information about filtering LUSID results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the \&quot;Instrument\&quot; or \&quot;Transaction\&quot; domain to decorate onto              the transactions. These take the format {domain}/{scope}/{code} e.g. \&quot;Instrument/system/Name\&quot; or              \&quot;Transaction/strategy/quantsignal\&quot;. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing transactions from a previous call to BuildTransactions. | [optional] 

### Return type

[**VersionedResourceListOfOutputTransaction**](VersionedResourceListOfOutputTransaction.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested transactions from the specified transaction portfolio |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_adjust_holdings**
> DeletedEntityResponse cancel_adjust_holdings(scope, code, effective_at)

CancelAdjustHoldings: Cancel adjust holdings

Cancel all previous holding adjustments made on the specified transaction portfolio for a specified effective  datetime. This should be used to undo holding adjustments made via set holdings or adjust holdings.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from lusid.models.deleted_entity_response import DeletedEntityResponse
from pprint import pprint

from lusid import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
	  EnvironmentVariablesConfigurationLoader,
	  SecretsFileConfigurationLoader,
	  ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
    code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which the holding adjustments should be undone.

    try:
        # CancelAdjustHoldings: Cancel adjust holdings
        api_response = await api_instance.cancel_adjust_holdings(scope, code, effective_at)
        print("The response of TransactionPortfoliosApi->cancel_adjust_holdings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionPortfoliosApi->cancel_adjust_holdings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. | 
 **effective_at** | **str**| The effective datetime or cut label at which the holding adjustments should be undone. | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the holding adjustments were cancelled |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_transactions**
> DeletedEntityResponse cancel_transactions(scope, code, transaction_ids)

CancelTransactions: Cancel transactions

Cancel one or more transactions from the transaction portfolio.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from lusid.models.deleted_entity_response import DeletedEntityResponse
from pprint import pprint

from lusid import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
	  EnvironmentVariablesConfigurationLoader,
	  SecretsFileConfigurationLoader,
	  ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
    code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
    transaction_ids = ['transaction_ids_example'] # List[str] | The IDs of the transactions to cancel.

    try:
        # CancelTransactions: Cancel transactions
        api_response = await api_instance.cancel_transactions(scope, code, transaction_ids)
        print("The response of TransactionPortfoliosApi->cancel_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionPortfoliosApi->cancel_transactions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. | 
 **transaction_ids** | [**List[str]**](str.md)| The IDs of the transactions to cancel. | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the transactions were cancelled |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_portfolio**
> Portfolio create_portfolio(scope, create_transaction_portfolio_request)

CreatePortfolio: Create portfolio

Create a transaction portfolio in a particular scope.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from lusid.models.create_transaction_portfolio_request import CreateTransactionPortfolioRequest
from lusid.models.portfolio import Portfolio
from pprint import pprint

from lusid import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
	  EnvironmentVariablesConfigurationLoader,
	  SecretsFileConfigurationLoader,
	  ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope in which to create the transaction portfolio.
    create_transaction_portfolio_request = {"displayName":"Portfolio UK","description":"Portfolio for UK market","code":"PortfolioUk","created":"2018-03-05T12:00:00.0000000+00:00","baseCurrency":"GBP","corporateActionSourceId":{"scope":"Sources","code":"Vendor1"},"accountingMethod":"Default","subHoldingKeys":[],"properties":{"Portfolio/Manager/Name":{"key":"Portfolio/Manager/Name","value":{"labelValue":"Matt Smith"},"effectiveFrom":"2018-03-05T12:00:00.0000000+00:00"},"Portfolio/Manager/Id":{"key":"Portfolio/Manager/Id","value":{"metricValue":{"value":1628483,"unit":"NoUnits"}},"effectiveFrom":"2018-03-05T12:00:00.0000000+00:00"}},"instrumentScopes":[],"amortisationMethod":"NoAmortisation","transactionTypeScope":"SomeScope","instrumentEventConfiguration":{"transactionTemplateScopes":["default"]}} # CreateTransactionPortfolioRequest | The definition of the transaction portfolio.

    try:
        # CreatePortfolio: Create portfolio
        api_response = await api_instance.create_portfolio(scope, create_transaction_portfolio_request)
        print("The response of TransactionPortfoliosApi->create_portfolio:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionPortfoliosApi->create_portfolio: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope in which to create the transaction portfolio. | 
 **create_transaction_portfolio_request** | [**CreateTransactionPortfolioRequest**](CreateTransactionPortfolioRequest.md)| The definition of the transaction portfolio. | 

### Return type

[**Portfolio**](Portfolio.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly-created transaction portfolio |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_trade_ticket**
> LusidTradeTicket create_trade_ticket(scope, code, lusid_trade_ticket=lusid_trade_ticket)

[EXPERIMENTAL] CreateTradeTicket: Create Trade Ticket

Upsert a trade ticket. This is broadly equivalent to a singular call to upsert an instrument, then a counterparty and finally  a transaction that makes use of the two. It can be viewed as a utility function or part of a workflow more familiar to users  with OTC systems than flow and equity trading ones.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from lusid.models.lusid_trade_ticket import LusidTradeTicket
from pprint import pprint

from lusid import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
	  EnvironmentVariablesConfigurationLoader,
	  SecretsFileConfigurationLoader,
	  ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
    code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
    lusid_trade_ticket = {"transactionId":"TradeTicket-1111111","transactionType":"OpenTradeTicket","source":"default","transactionDate":"2020-01-01T09:00:00.00Z","settlementDate":"2020-01-01T09:00:00.00Z","totalConsideration":{"amount":1020000,"currency":"GBP"},"units":1000000,"instrumentIdentifiers":{"Instrument/default/ClientInternal":"my-bond"},"instrumentScope":"myScope","instrumentName":"my_bond","instrumentDefinition":{"startDate":"2018-01-01T00:00:00.0000000+00:00","maturityDate":"2019-01-01T00:00:00.0000000+00:00","domAmount":1,"domCcy":"GBP","fgnAmount":-1.5,"fgnCcy":"USD","refSpotRate":1.5,"isNdf":false,"fixingDate":"0001-01-01T00:00:00.0000000+00:00","instrumentType":"FxForward"},"counterpartyAgreementId":{"scope":"demoScope","code":"myCounterparty"},"tradeTicketType":"LusidTradeTicket"} # LusidTradeTicket | the trade ticket to upsert (optional)

    try:
        # [EXPERIMENTAL] CreateTradeTicket: Create Trade Ticket
        api_response = await api_instance.create_trade_ticket(scope, code, lusid_trade_ticket=lusid_trade_ticket)
        print("The response of TransactionPortfoliosApi->create_trade_ticket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionPortfoliosApi->create_trade_ticket: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. | 
 **lusid_trade_ticket** | [**LusidTradeTicket**](LusidTradeTicket.md)| the trade ticket to upsert | [optional] 

### Return type

[**LusidTradeTicket**](LusidTradeTicket.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The created trade ticket, possibly populated with created LUID and identifiers if missing on the request. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_custodian_accounts**
> DeleteCustodianAccountsResponse delete_custodian_accounts(scope, code, resource_id, delete_mode=delete_mode)

[EXPERIMENTAL] DeleteCustodianAccounts: Soft or hard delete multiple custodian accounts

Delete one or more custodian accounts from the Transaction Portfolios. Soft deletion marks the custodian account as inactive  While the Hard deletion is deleting the custodian account.  The batch limit per request is 2,000.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from lusid.models.delete_custodian_accounts_response import DeleteCustodianAccountsResponse
from lusid.models.resource_id import ResourceId
from pprint import pprint

from lusid import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
	  EnvironmentVariablesConfigurationLoader,
	  SecretsFileConfigurationLoader,
	  ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the Transaction Portfolios.
    code = 'code_example' # str | The code of the Transaction Portfolios. Together with the scope this uniquely identifies              the Transaction Portfolios.
    resource_id = [{"scope":"ScopeA","code":"AccountCode1"},{"scope":"ScopeB","code":"AccountCode2"}] # List[ResourceId] | The scope and codes of the custodian accounts to delete.
    delete_mode = 'delete_mode_example' # str | The delete mode to use (defaults to 'Soft'). (optional)

    try:
        # [EXPERIMENTAL] DeleteCustodianAccounts: Soft or hard delete multiple custodian accounts
        api_response = await api_instance.delete_custodian_accounts(scope, code, resource_id, delete_mode=delete_mode)
        print("The response of TransactionPortfoliosApi->delete_custodian_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionPortfoliosApi->delete_custodian_accounts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Transaction Portfolios. | 
 **code** | **str**| The code of the Transaction Portfolios. Together with the scope this uniquely identifies              the Transaction Portfolios. | 
 **resource_id** | [**List[ResourceId]**](ResourceId.md)| The scope and codes of the custodian accounts to delete. | 
 **delete_mode** | **str**| The delete mode to use (defaults to &#39;Soft&#39;). | [optional] 

### Return type

[**DeleteCustodianAccountsResponse**](DeleteCustodianAccountsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the custodian accounts were deleted. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_properties_from_transaction**
> DeletedEntityResponse delete_properties_from_transaction(scope, code, transaction_id, property_keys)

DeletePropertiesFromTransaction: Delete properties from transaction

Delete one or more properties from a single transaction in a transaction portfolio.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from lusid.models.deleted_entity_response import DeletedEntityResponse
from pprint import pprint

from lusid import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
	  EnvironmentVariablesConfigurationLoader,
	  SecretsFileConfigurationLoader,
	  ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
    code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
    transaction_id = 'transaction_id_example' # str | The unique ID of the transaction from which to delete properties.
    property_keys = ['property_keys_example'] # List[str] | The property keys of the properties to delete.              These must be from the \"Transaction\" domain and have the format {domain}/{scope}/{code}, for example              \"Transaction/strategy/quantsignal\".

    try:
        # DeletePropertiesFromTransaction: Delete properties from transaction
        api_response = await api_instance.delete_properties_from_transaction(scope, code, transaction_id, property_keys)
        print("The response of TransactionPortfoliosApi->delete_properties_from_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionPortfoliosApi->delete_properties_from_transaction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. | 
 **transaction_id** | **str**| The unique ID of the transaction from which to delete properties. | 
 **property_keys** | [**List[str]**](str.md)| The property keys of the properties to delete.              These must be from the \&quot;Transaction\&quot; domain and have the format {domain}/{scope}/{code}, for example              \&quot;Transaction/strategy/quantsignal\&quot;. | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the property was deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_a2_b_data**
> VersionedResourceListOfA2BDataRecord get_a2_b_data(scope, code, from_effective_at, to_effective_at, as_at=as_at, recipe_id_scope=recipe_id_scope, recipe_id_code=recipe_id_code, property_keys=property_keys, filter=filter)

GetA2BData: Get A2B data

Get an A2B report for the given portfolio.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from lusid.models.versioned_resource_list_of_a2_b_data_record import VersionedResourceListOfA2BDataRecord
from pprint import pprint

from lusid import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
	  EnvironmentVariablesConfigurationLoader,
	  SecretsFileConfigurationLoader,
	  ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the portfolio to retrieve the A2B report for.
    code = 'code_example' # str | The code of the portfolio to retrieve the A2B report for. Together with the scope this              uniquely identifies the portfolio.
    from_effective_at = 'from_effective_at_example' # str | The lower bound effective datetime or cut label (inclusive) from which to retrieve the data.              There is no lower bound if this is not specified.
    to_effective_at = 'to_effective_at_example' # str | The upper bound effective datetime or cut label (inclusive) from which to retrieve the data.              There is no upper bound if this is not specified.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the portfolio. Defaults to return the latest version              of each transaction if not specified. (optional)
    recipe_id_scope = 'recipe_id_scope_example' # str | The scope of the given recipeId (optional)
    recipe_id_code = 'recipe_id_code_example' # str | The code of the given recipeId (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the \"Instrument\" domain to decorate onto              the results. These take the format {domain}/{scope}/{code} e.g. \"Instrument/system/Name\". (optional)
    filter = 'filter_example' # str | Expression to filter the result set.              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)

    try:
        # GetA2BData: Get A2B data
        api_response = await api_instance.get_a2_b_data(scope, code, from_effective_at, to_effective_at, as_at=as_at, recipe_id_scope=recipe_id_scope, recipe_id_code=recipe_id_code, property_keys=property_keys, filter=filter)
        print("The response of TransactionPortfoliosApi->get_a2_b_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionPortfoliosApi->get_a2_b_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio to retrieve the A2B report for. | 
 **code** | **str**| The code of the portfolio to retrieve the A2B report for. Together with the scope this              uniquely identifies the portfolio. | 
 **from_effective_at** | **str**| The lower bound effective datetime or cut label (inclusive) from which to retrieve the data.              There is no lower bound if this is not specified. | 
 **to_effective_at** | **str**| The upper bound effective datetime or cut label (inclusive) from which to retrieve the data.              There is no upper bound if this is not specified. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the portfolio. Defaults to return the latest version              of each transaction if not specified. | [optional] 
 **recipe_id_scope** | **str**| The scope of the given recipeId | [optional] 
 **recipe_id_code** | **str**| The code of the given recipeId | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the \&quot;Instrument\&quot; domain to decorate onto              the results. These take the format {domain}/{scope}/{code} e.g. \&quot;Instrument/system/Name\&quot;. | [optional] 
 **filter** | **str**| Expression to filter the result set.              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 

### Return type

[**VersionedResourceListOfA2BDataRecord**](VersionedResourceListOfA2BDataRecord.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested portfolio A2B data |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_a2_b_movements**
> VersionedResourceListOfA2BMovementRecord get_a2_b_movements(scope, code, from_effective_at, to_effective_at, as_at=as_at, recipe_id_scope=recipe_id_scope, recipe_id_code=recipe_id_code, property_keys=property_keys, filter=filter)

GetA2BMovements: Get an A2B report at the movement level for the given portfolio.

Get an A2B report at the movement level for the given portfolio.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from lusid.models.versioned_resource_list_of_a2_b_movement_record import VersionedResourceListOfA2BMovementRecord
from pprint import pprint

from lusid import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
	  EnvironmentVariablesConfigurationLoader,
	  SecretsFileConfigurationLoader,
	  ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the portfolio to retrieve the A2B movement report for.
    code = 'code_example' # str | The code of the portfolio to retrieve the A2B movement report for. Together with the scope this              uniquely identifies the portfolio.
    from_effective_at = 'from_effective_at_example' # str | The lower bound effective datetime or cut label (inclusive) from which to retrieve the data.              There is no lower bound if this is not specified.
    to_effective_at = 'to_effective_at_example' # str | The upper bound effective datetime or cut label (inclusive) from which to retrieve the data.              There is no upper bound if this is not specified.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the portfolio. Defaults to return the latest version              of each transaction if not specified. (optional)
    recipe_id_scope = 'recipe_id_scope_example' # str | The scope of the given recipeId (optional)
    recipe_id_code = 'recipe_id_code_example' # str | The code of the given recipeId (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the \"Instrument\" domain to decorate onto              the results. These take the format {domain}/{scope}/{code} e.g. \"Instrument/system/Name\". (optional)
    filter = 'filter_example' # str | Expression to filter the result set.              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)

    try:
        # GetA2BMovements: Get an A2B report at the movement level for the given portfolio.
        api_response = await api_instance.get_a2_b_movements(scope, code, from_effective_at, to_effective_at, as_at=as_at, recipe_id_scope=recipe_id_scope, recipe_id_code=recipe_id_code, property_keys=property_keys, filter=filter)
        print("The response of TransactionPortfoliosApi->get_a2_b_movements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionPortfoliosApi->get_a2_b_movements: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio to retrieve the A2B movement report for. | 
 **code** | **str**| The code of the portfolio to retrieve the A2B movement report for. Together with the scope this              uniquely identifies the portfolio. | 
 **from_effective_at** | **str**| The lower bound effective datetime or cut label (inclusive) from which to retrieve the data.              There is no lower bound if this is not specified. | 
 **to_effective_at** | **str**| The upper bound effective datetime or cut label (inclusive) from which to retrieve the data.              There is no upper bound if this is not specified. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the portfolio. Defaults to return the latest version              of each transaction if not specified. | [optional] 
 **recipe_id_scope** | **str**| The scope of the given recipeId | [optional] 
 **recipe_id_code** | **str**| The code of the given recipeId | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the \&quot;Instrument\&quot; domain to decorate onto              the results. These take the format {domain}/{scope}/{code} e.g. \&quot;Instrument/system/Name\&quot;. | [optional] 
 **filter** | **str**| Expression to filter the result set.              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 

### Return type

[**VersionedResourceListOfA2BMovementRecord**](VersionedResourceListOfA2BMovementRecord.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested portfolio A2B movement data |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bucketed_cash_flows**
> BucketedCashFlowResponse get_bucketed_cash_flows(scope, code, bucketed_cash_flow_request=bucketed_cash_flow_request)

[EXPERIMENTAL] GetBucketedCashFlows: Get bucketed cash flows from a list of portfolios

We bucket/aggregate a transaction portfolio's instruments by date or tenor specified in the request.  The cashflows are grouped by both instrumentId and currency.                If you want transactional level cashflow, please use the 'GetUpsertableCashFlows' endpoint.  If you want instrument cashflow, please use the 'GetPortfolioCashFlows' endpoint.  Note that these endpoints do not apply bucketing.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from lusid.models.bucketed_cash_flow_request import BucketedCashFlowRequest
from lusid.models.bucketed_cash_flow_response import BucketedCashFlowResponse
from pprint import pprint

from lusid import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
	  EnvironmentVariablesConfigurationLoader,
	  SecretsFileConfigurationLoader,
	  ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
    code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies the portfolio.
    bucketed_cash_flow_request = {"roundingMethod":"RoundUp","bucketingDates":["2020-01-01T00:00:00.0000000+00:00","2020-07-01T00:00:00.0000000+00:00","2021-01-01T00:00:00.0000000+00:00","2021-07-01T00:00:00.0000000+00:00"],"equipWithSubtotals":false,"excludeUnsettledTrades":false,"cashFlowType":"InstrumentCashFlow"} # BucketedCashFlowRequest | Request specifying the bucketing of cashflows (optional)

    try:
        # [EXPERIMENTAL] GetBucketedCashFlows: Get bucketed cash flows from a list of portfolios
        api_response = await api_instance.get_bucketed_cash_flows(scope, code, bucketed_cash_flow_request=bucketed_cash_flow_request)
        print("The response of TransactionPortfoliosApi->get_bucketed_cash_flows:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionPortfoliosApi->get_bucketed_cash_flows: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this uniquely identifies the portfolio. | 
 **bucketed_cash_flow_request** | [**BucketedCashFlowRequest**](BucketedCashFlowRequest.md)| Request specifying the bucketing of cashflows | [optional] 

### Return type

[**BucketedCashFlowResponse**](BucketedCashFlowResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested portfolio instruments&#39; bucketed cash flow data |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custodian_account**
> CustodianAccount get_custodian_account(scope, code, custodian_account_scope, custodian_account_code, effective_at=effective_at, as_at=as_at, property_keys=property_keys)

[EXPERIMENTAL] GetCustodianAccount: Get Custodian Account

Retrieve the definition of a particular Custodian Account which is part of a Transaction Portfolios.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from lusid.models.custodian_account import CustodianAccount
from pprint import pprint

from lusid import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
	  EnvironmentVariablesConfigurationLoader,
	  SecretsFileConfigurationLoader,
	  ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the Transaction Portfolio.
    code = 'code_example' # str | The code of the Transaction Portfolio. Together with the scope this uniquely identifies the Transaction Portfolio.
    custodian_account_scope = 'custodian_account_scope_example' # str | The scope of the Custodian Account.
    custodian_account_code = 'custodian_account_code_example' # str | The code of the Custodian Account.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve the Custodian Account properties. Defaults to the current LUSID system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Custodian Account definition. Defaults to returning the latest version of the Custodian Account definition if not specified. (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the 'CustodianAccount' domain to decorate onto the Custodian Account.              These must take the format {domain}/{scope}/{code}, for example 'CustodianAccount/Manager/Id'. If not provided will return all the entitled properties for that Custodian Account. (optional)

    try:
        # [EXPERIMENTAL] GetCustodianAccount: Get Custodian Account
        api_response = await api_instance.get_custodian_account(scope, code, custodian_account_scope, custodian_account_code, effective_at=effective_at, as_at=as_at, property_keys=property_keys)
        print("The response of TransactionPortfoliosApi->get_custodian_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionPortfoliosApi->get_custodian_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Transaction Portfolio. | 
 **code** | **str**| The code of the Transaction Portfolio. Together with the scope this uniquely identifies the Transaction Portfolio. | 
 **custodian_account_scope** | **str**| The scope of the Custodian Account. | 
 **custodian_account_code** | **str**| The code of the Custodian Account. | 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the Custodian Account properties. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Custodian Account definition. Defaults to returning the latest version of the Custodian Account definition if not specified. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;CustodianAccount&#39; domain to decorate onto the Custodian Account.              These must take the format {domain}/{scope}/{code}, for example &#39;CustodianAccount/Manager/Id&#39;. If not provided will return all the entitled properties for that Custodian Account. | [optional] 

### Return type

[**CustodianAccount**](CustodianAccount.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Custodian Account definition |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_details**
> PortfolioDetails get_details(scope, code, effective_at=effective_at, as_at=as_at)

GetDetails: Get details

Get certain details associated with a transaction portfolio.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from lusid.models.portfolio_details import PortfolioDetails
from pprint import pprint

from lusid import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
	  EnvironmentVariablesConfigurationLoader,
	  SecretsFileConfigurationLoader,
	  ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
    code = 'code_example' # str | The code of the transaction portfolio. Together with the              scope this uniquely identifies the transaction portfolio.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve the details of the transaction              portfolio. Defaults to the current LUSID system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the details of the transaction portfolio. Defaults              to returning the latest version of the details if not specified. (optional)

    try:
        # GetDetails: Get details
        api_response = await api_instance.get_details(scope, code, effective_at=effective_at, as_at=as_at)
        print("The response of TransactionPortfoliosApi->get_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionPortfoliosApi->get_details: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the              scope this uniquely identifies the transaction portfolio. | 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the details of the transaction              portfolio. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the details of the transaction portfolio. Defaults              to returning the latest version of the details if not specified. | [optional] 

### Return type

[**PortfolioDetails**](PortfolioDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The details of the specified transaction portfolio |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_holding_contributors**
> VersionedResourceListOfHoldingContributor get_holding_contributors(scope, code, holding_id, effective_date=effective_date, from_trade_date=from_trade_date, to_trade_date=to_trade_date, include_historic=include_historic, tax_lot_id=tax_lot_id, limit=limit, as_at=as_at, page=page)

[EXPERIMENTAL] GetHoldingContributors: Get Holdings Contributors

Lists all transactions that affect the holdings of a portfolio over a given effective interval. This includes  transactions automatically generated by LUSID such as holding adjustments.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from lusid.models.versioned_resource_list_of_holding_contributor import VersionedResourceListOfHoldingContributor
from pprint import pprint

from lusid import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
	  EnvironmentVariablesConfigurationLoader,
	  SecretsFileConfigurationLoader,
	  ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
    code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
    holding_id = 56 # int | The unique holding identifier
    effective_date = '2013-10-20T19:20:30+01:00' # datetime | Effective date (optional)
    from_trade_date = '2013-10-20T19:20:30+01:00' # datetime | The from trade date, defaults to first time this holding is opened, lower bound for transactions (optional)
    to_trade_date = '2013-10-20T19:20:30+01:00' # datetime | The to trade date upper bound date, defaults to effectiveDate. upper bound for transactions (optional)
    include_historic = False # bool | If true, transactions from previously closed holdings are returned.              If false, only transactions from last time position is opened. (optional) (default to False)
    tax_lot_id = 'tax_lot_id_example' # str | Constrains the Holding Contributors to those which contributed to the specified tax lot. (optional)
    limit = 56 # int | When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to build the transactions. Defaults to return the latest              version of each transaction if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing transactions from a previous call to GetHoldingContributors. (optional)

    try:
        # [EXPERIMENTAL] GetHoldingContributors: Get Holdings Contributors
        api_response = await api_instance.get_holding_contributors(scope, code, holding_id, effective_date=effective_date, from_trade_date=from_trade_date, to_trade_date=to_trade_date, include_historic=include_historic, tax_lot_id=tax_lot_id, limit=limit, as_at=as_at, page=page)
        print("The response of TransactionPortfoliosApi->get_holding_contributors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionPortfoliosApi->get_holding_contributors: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. | 
 **holding_id** | **int**| The unique holding identifier | 
 **effective_date** | **datetime**| Effective date | [optional] 
 **from_trade_date** | **datetime**| The from trade date, defaults to first time this holding is opened, lower bound for transactions | [optional] 
 **to_trade_date** | **datetime**| The to trade date upper bound date, defaults to effectiveDate. upper bound for transactions | [optional] 
 **include_historic** | **bool**| If true, transactions from previously closed holdings are returned.              If false, only transactions from last time position is opened. | [optional] [default to False]
 **tax_lot_id** | **str**| Constrains the Holding Contributors to those which contributed to the specified tax lot. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to build the transactions. Defaults to return the latest              version of each transaction if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing transactions from a previous call to GetHoldingContributors. | [optional] 

### Return type

[**VersionedResourceListOfHoldingContributor**](VersionedResourceListOfHoldingContributor.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested holding contributors from the specified transaction portfolio |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_holdings**
> VersionedResourceListOfPortfolioHolding get_holdings(scope, code, effective_at=effective_at, as_at=as_at, filter=filter, property_keys=property_keys, by_taxlots=by_taxlots)

GetHoldings: Get holdings

Calculate holdings for a transaction portfolio.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from lusid.models.versioned_resource_list_of_portfolio_holding import VersionedResourceListOfPortfolioHolding
from pprint import pprint

from lusid import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
	  EnvironmentVariablesConfigurationLoader,
	  SecretsFileConfigurationLoader,
	  ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
    code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve the holdings of the transaction              portfolio. Defaults to the current LUSID system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the holdings of the transaction portfolio. Defaults              to return the latest version if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the result set.              For example, to filter on the Holding Type, use \"holdingType eq 'p'\".              For more information about filtering LUSID results, see https://support.lusid.com/knowledgebase/article/KA-01914. (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the \"Instrument\", \"Holding\", \"Custodian Account\" or \"Portfolio\" domain to decorate onto              holdings. These must have the format {domain}/{scope}/{code}, for example \"Instrument/system/Name\" or \"Holding/system/Cost\". (optional)
    by_taxlots = True # bool | Whether or not to expand the holdings to return the underlying tax-lots. Defaults to              False. (optional)

    try:
        # GetHoldings: Get holdings
        api_response = await api_instance.get_holdings(scope, code, effective_at=effective_at, as_at=as_at, filter=filter, property_keys=property_keys, by_taxlots=by_taxlots)
        print("The response of TransactionPortfoliosApi->get_holdings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionPortfoliosApi->get_holdings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. | 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the holdings of the transaction              portfolio. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the holdings of the transaction portfolio. Defaults              to return the latest version if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set.              For example, to filter on the Holding Type, use \&quot;holdingType eq &#39;p&#39;\&quot;.              For more information about filtering LUSID results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the \&quot;Instrument\&quot;, \&quot;Holding\&quot;, \&quot;Custodian Account\&quot; or \&quot;Portfolio\&quot; domain to decorate onto              holdings. These must have the format {domain}/{scope}/{code}, for example \&quot;Instrument/system/Name\&quot; or \&quot;Holding/system/Cost\&quot;. | [optional] 
 **by_taxlots** | **bool**| Whether or not to expand the holdings to return the underlying tax-lots. Defaults to              False. | [optional] 

### Return type

[**VersionedResourceListOfPortfolioHolding**](VersionedResourceListOfPortfolioHolding.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The holdings and version of the specified transaction portfolio |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_holdings_adjustment**
> HoldingsAdjustment get_holdings_adjustment(scope, code, effective_at, as_at=as_at, property_keys=property_keys)

GetHoldingsAdjustment: Get holdings adjustment

Get a holdings adjustment made to a transaction portfolio at a specific effective datetime. Note that a  holdings adjustment will only be returned if one exists for the specified effective datetime.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from lusid.models.holdings_adjustment import HoldingsAdjustment
from pprint import pprint

from lusid import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
	  EnvironmentVariablesConfigurationLoader,
	  SecretsFileConfigurationLoader,
	  ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
    code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label of the holdings adjustment.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the holdings adjustment. Defaults to the return the latest              version of the holdings adjustment if not specified. (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the ‘Instrument' domain to decorate onto holdings adjustments.              These must have the format {domain}/{scope}/{code}, for example 'Instrument/system/Name'.              Note that properties from the 'Holding’ domain are automatically returned. (optional)

    try:
        # GetHoldingsAdjustment: Get holdings adjustment
        api_response = await api_instance.get_holdings_adjustment(scope, code, effective_at, as_at=as_at, property_keys=property_keys)
        print("The response of TransactionPortfoliosApi->get_holdings_adjustment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionPortfoliosApi->get_holdings_adjustment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. | 
 **effective_at** | **str**| The effective datetime or cut label of the holdings adjustment. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the holdings adjustment. Defaults to the return the latest              version of the holdings adjustment if not specified. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the ‘Instrument&#39; domain to decorate onto holdings adjustments.              These must have the format {domain}/{scope}/{code}, for example &#39;Instrument/system/Name&#39;.              Note that properties from the &#39;Holding’ domain are automatically returned. | [optional] 

### Return type

[**HoldingsAdjustment**](HoldingsAdjustment.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The details of the requested holdings adjustment |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_holdings_with_orders**
> VersionedResourceListWithWarningsOfPortfolioHolding get_holdings_with_orders(scope, code, effective_at=effective_at, as_at=as_at, filter=filter, property_keys=property_keys, by_taxlots=by_taxlots, recipe_id_scope=recipe_id_scope, recipe_id_code=recipe_id_code)

[EXPERIMENTAL] GetHoldingsWithOrders: Get holdings with orders

Get the holdings of a transaction portfolio. Create virtual holdings for any outstanding orders,  and account for order state/fulfillment; that is, treat outstanding orders (and related records) as  if they had been realised at moment of query.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from lusid.models.versioned_resource_list_with_warnings_of_portfolio_holding import VersionedResourceListWithWarningsOfPortfolioHolding
from pprint import pprint

from lusid import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
	  EnvironmentVariablesConfigurationLoader,
	  SecretsFileConfigurationLoader,
	  ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
    code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve the holdings of the transaction              portfolio. Defaults to the current LUSID system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the holdings of the transaction portfolio. Defaults              to return the latest version of the holdings if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the result set.              For example, to filter on the Holding Type, use \"holdingType eq 'p'\"              For more information about filtering LUSID results, see https://support.lusid.com/knowledgebase/article/KA-01914. (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the \"Instrument\", \"Holding\" or \"Portfolio\" domain to decorate onto              the holdings. These take the format {domain}/{scope}/{code} e.g. \"Instrument/system/Name\" or \"Holding/system/Cost\". (optional)
    by_taxlots = True # bool | Whether or not to expand the holdings to return the underlying tax-lots. Defaults to              False. (optional)
    recipe_id_scope = 'recipe_id_scope_example' # str | The scope of the given recipeId (optional)
    recipe_id_code = 'recipe_id_code_example' # str | The code of the given recipeId (optional)

    try:
        # [EXPERIMENTAL] GetHoldingsWithOrders: Get holdings with orders
        api_response = await api_instance.get_holdings_with_orders(scope, code, effective_at=effective_at, as_at=as_at, filter=filter, property_keys=property_keys, by_taxlots=by_taxlots, recipe_id_scope=recipe_id_scope, recipe_id_code=recipe_id_code)
        print("The response of TransactionPortfoliosApi->get_holdings_with_orders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionPortfoliosApi->get_holdings_with_orders: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. | 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the holdings of the transaction              portfolio. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the holdings of the transaction portfolio. Defaults              to return the latest version of the holdings if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set.              For example, to filter on the Holding Type, use \&quot;holdingType eq &#39;p&#39;\&quot;              For more information about filtering LUSID results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the \&quot;Instrument\&quot;, \&quot;Holding\&quot; or \&quot;Portfolio\&quot; domain to decorate onto              the holdings. These take the format {domain}/{scope}/{code} e.g. \&quot;Instrument/system/Name\&quot; or \&quot;Holding/system/Cost\&quot;. | [optional] 
 **by_taxlots** | **bool**| Whether or not to expand the holdings to return the underlying tax-lots. Defaults to              False. | [optional] 
 **recipe_id_scope** | **str**| The scope of the given recipeId | [optional] 
 **recipe_id_code** | **str**| The code of the given recipeId | [optional] 

### Return type

[**VersionedResourceListWithWarningsOfPortfolioHolding**](VersionedResourceListWithWarningsOfPortfolioHolding.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The holdings and version of the specified transaction portfolio |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_portfolio_cash_flows**
> ResourceListOfInstrumentCashFlow get_portfolio_cash_flows(scope, code, effective_at=effective_at, window_start=window_start, window_end=window_end, as_at=as_at, filter=filter, recipe_id_scope=recipe_id_scope, recipe_id_code=recipe_id_code, exclude_unsettled_trades=exclude_unsettled_trades)

[BETA] GetPortfolioCashFlows: Get portfolio cash flows

Get the set of cash flows that occur in a window for the transaction portfolio's instruments.                Note that grouping can affect the quantity of information returned; where a holding is an amalgamation of one or more (e.g. cash) instruments, a unique  transaction identifier will not be available. The same may go for diagnostic information (e.g. multiple sources of an aggregate cash amount on a date that is  not split out. Grouping at the transaction and instrument level is recommended for those seeking to attribute individual flows.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from lusid.models.resource_list_of_instrument_cash_flow import ResourceListOfInstrumentCashFlow
from pprint import pprint

from lusid import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
	  EnvironmentVariablesConfigurationLoader,
	  SecretsFileConfigurationLoader,
	  ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
    code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this               uniquely identifies the portfolio.
    effective_at = 'effective_at_example' # str | The valuation (pricing) effective datetime or cut label (inclusive) at which to evaluate the cashflows.  This determines whether cashflows are evaluated in a historic or forward looking context and will, for certain models, affect where data is looked up.  For example, on a swap if the effectiveAt is in the middle of the window, cashflows before it will be historic and resets assumed to exist where if the effectiveAt  is before the start of the range they are forward looking and will be expectations assuming the model supports that.  There is evidently a presumption here about availability of data and that the effectiveAt is realistically on or before the real-world today. (optional)
    window_start = 'window_start_example' # str | The lower bound effective datetime or cut label (inclusive) from which to retrieve the cashflows.               There is no lower bound if this is not specified. i.e. it is the minimum date. (optional)
    window_end = 'window_end_example' # str | The upper bound effective datetime or cut label (inclusive) from which to retrieve the cashflows.               The upper bound defaults to 'max date' if it is not specified (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the data. Defaults to returning the latest version               of each transaction if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the result set.               For example, to return only transactions with a transaction type of 'Buy', specify \"type eq 'Buy'\".               For more information about filtering LUSID results, see https://support.lusid.com/knowledgebase/article/KA-01914. (optional)
    recipe_id_scope = 'recipe_id_scope_example' # str | The scope of the given recipeId (optional)
    recipe_id_code = 'recipe_id_code_example' # str | The code of the given recipeID (optional)
    exclude_unsettled_trades = False # bool | If absent or set to false, cashflows will returned based on trade date - more specifically, cashflows from any unsettled trades will be included in the results. If set to true, unsettled trades will be excluded from the result set. (optional) (default to False)

    try:
        # [BETA] GetPortfolioCashFlows: Get portfolio cash flows
        api_response = await api_instance.get_portfolio_cash_flows(scope, code, effective_at=effective_at, window_start=window_start, window_end=window_end, as_at=as_at, filter=filter, recipe_id_scope=recipe_id_scope, recipe_id_code=recipe_id_code, exclude_unsettled_trades=exclude_unsettled_trades)
        print("The response of TransactionPortfoliosApi->get_portfolio_cash_flows:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionPortfoliosApi->get_portfolio_cash_flows: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this               uniquely identifies the portfolio. | 
 **effective_at** | **str**| The valuation (pricing) effective datetime or cut label (inclusive) at which to evaluate the cashflows.  This determines whether cashflows are evaluated in a historic or forward looking context and will, for certain models, affect where data is looked up.  For example, on a swap if the effectiveAt is in the middle of the window, cashflows before it will be historic and resets assumed to exist where if the effectiveAt  is before the start of the range they are forward looking and will be expectations assuming the model supports that.  There is evidently a presumption here about availability of data and that the effectiveAt is realistically on or before the real-world today. | [optional] 
 **window_start** | **str**| The lower bound effective datetime or cut label (inclusive) from which to retrieve the cashflows.               There is no lower bound if this is not specified. i.e. it is the minimum date. | [optional] 
 **window_end** | **str**| The upper bound effective datetime or cut label (inclusive) from which to retrieve the cashflows.               The upper bound defaults to &#39;max date&#39; if it is not specified | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the data. Defaults to returning the latest version               of each transaction if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set.               For example, to return only transactions with a transaction type of &#39;Buy&#39;, specify \&quot;type eq &#39;Buy&#39;\&quot;.               For more information about filtering LUSID results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **recipe_id_scope** | **str**| The scope of the given recipeId | [optional] 
 **recipe_id_code** | **str**| The code of the given recipeID | [optional] 
 **exclude_unsettled_trades** | **bool**| If absent or set to false, cashflows will returned based on trade date - more specifically, cashflows from any unsettled trades will be included in the results. If set to true, unsettled trades will be excluded from the result set. | [optional] [default to False]

### Return type

[**ResourceListOfInstrumentCashFlow**](ResourceListOfInstrumentCashFlow.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested portfolio instruments&#39; cash flow data |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_portfolio_cash_ladder**
> ResourceListOfPortfolioCashLadder get_portfolio_cash_ladder(scope, code, from_effective_at, to_effective_at, effective_at, as_at=as_at, filter=filter, recipe_id_scope=recipe_id_scope, recipe_id_code=recipe_id_code, exclude_unsettled_trades=exclude_unsettled_trades)

GetPortfolioCashLadder: Get portfolio cash ladder

Get a cash ladder for a transaction portfolio.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from lusid.models.resource_list_of_portfolio_cash_ladder import ResourceListOfPortfolioCashLadder
from pprint import pprint

from lusid import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
	  EnvironmentVariablesConfigurationLoader,
	  SecretsFileConfigurationLoader,
	  ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
    code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this              uniquely identifies the portfolio.
    from_effective_at = 'from_effective_at_example' # str | The lower bound effective datetime or cut label (inclusive) from which to retrieve the data.              There is no lower bound if this is not specified.
    to_effective_at = 'to_effective_at_example' # str | The upper bound effective datetime or cut label (inclusive) from which to retrieve the data.              There is no upper bound if this is not specified.
    effective_at = 'effective_at_example' # str | The valuation (pricing) effective datetime or cut label (inclusive) at which to evaluate the cashflows.  This determines whether cashflows are evaluated in a historic or forward looking context and will, for certain models, affect where data is looked up.  For example, on a swap if the effectiveAt is in the middle of the window, cashflows before it will be historic and resets assumed to exist where if the effectiveAt  is before the start of the range they are forward looking and will be expectations assuming the model supports that.  There is evidently a presumption here about availability of data and that the effectiveAt is realistically on or before the real-world today.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the portfolio. Defaults to returning the latest version              of each transaction if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the result set.              For example, to return only transactions with a transaction type of 'Buy', specify \"type eq 'Buy'\".              For more information about filtering LUSID results, see https://support.lusid.com/knowledgebase/article/KA-01914. (optional)
    recipe_id_scope = 'recipe_id_scope_example' # str | The scope of the given recipeId (optional)
    recipe_id_code = 'recipe_id_code_example' # str | The code of the given recipeID (optional)
    exclude_unsettled_trades = False # bool | If absent or set to false, cashflows will returned based on trade date - more specifically, cashflows from any unsettled trades will be included in the results. If set to true, unsettled trades will be excluded from the result set. (optional) (default to False)

    try:
        # GetPortfolioCashLadder: Get portfolio cash ladder
        api_response = await api_instance.get_portfolio_cash_ladder(scope, code, from_effective_at, to_effective_at, effective_at, as_at=as_at, filter=filter, recipe_id_scope=recipe_id_scope, recipe_id_code=recipe_id_code, exclude_unsettled_trades=exclude_unsettled_trades)
        print("The response of TransactionPortfoliosApi->get_portfolio_cash_ladder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionPortfoliosApi->get_portfolio_cash_ladder: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this              uniquely identifies the portfolio. | 
 **from_effective_at** | **str**| The lower bound effective datetime or cut label (inclusive) from which to retrieve the data.              There is no lower bound if this is not specified. | 
 **to_effective_at** | **str**| The upper bound effective datetime or cut label (inclusive) from which to retrieve the data.              There is no upper bound if this is not specified. | 
 **effective_at** | **str**| The valuation (pricing) effective datetime or cut label (inclusive) at which to evaluate the cashflows.  This determines whether cashflows are evaluated in a historic or forward looking context and will, for certain models, affect where data is looked up.  For example, on a swap if the effectiveAt is in the middle of the window, cashflows before it will be historic and resets assumed to exist where if the effectiveAt  is before the start of the range they are forward looking and will be expectations assuming the model supports that.  There is evidently a presumption here about availability of data and that the effectiveAt is realistically on or before the real-world today. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the portfolio. Defaults to returning the latest version              of each transaction if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set.              For example, to return only transactions with a transaction type of &#39;Buy&#39;, specify \&quot;type eq &#39;Buy&#39;\&quot;.              For more information about filtering LUSID results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **recipe_id_scope** | **str**| The scope of the given recipeId | [optional] 
 **recipe_id_code** | **str**| The code of the given recipeID | [optional] 
 **exclude_unsettled_trades** | **bool**| If absent or set to false, cashflows will returned based on trade date - more specifically, cashflows from any unsettled trades will be included in the results. If set to true, unsettled trades will be excluded from the result set. | [optional] [default to False]

### Return type

[**ResourceListOfPortfolioCashLadder**](ResourceListOfPortfolioCashLadder.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested portfolio cash-ladder |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_portfolio_cash_statement**
> ResourceListOfPortfolioCashFlow get_portfolio_cash_statement(scope, code, from_effective_at, to_effective_at, as_at=as_at, filter=filter, recipe_id_scope=recipe_id_scope, recipe_id_code=recipe_id_code)

GetPortfolioCashStatement: Get portfolio cash statement

Get a cash statement for a transaction portfolio.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from lusid.models.resource_list_of_portfolio_cash_flow import ResourceListOfPortfolioCashFlow
from pprint import pprint

from lusid import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
	  EnvironmentVariablesConfigurationLoader,
	  SecretsFileConfigurationLoader,
	  ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
    code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this              uniquely identifies the portfolio.
    from_effective_at = 'from_effective_at_example' # str | The lower bound effective datetime or cut label (inclusive) from which to retrieve the data.              There is no lower bound if this is not specified.
    to_effective_at = 'to_effective_at_example' # str | The upper bound effective datetime or cut label (inclusive) from which to retrieve the data.              There is no upper bound if this is not specified.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the portfolio. Defaults to returning the latest version              of each transaction if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the result set.              For example, to return only transactions with a transaction type of 'Buy', specify \"type eq 'Buy'\".              For more information about filtering LUSID results, see https://support.lusid.com/knowledgebase/article/KA-01914. (optional)
    recipe_id_scope = 'recipe_id_scope_example' # str | The scope of the given recipeId (optional)
    recipe_id_code = 'recipe_id_code_example' # str | The code of the given recipeID (optional)

    try:
        # GetPortfolioCashStatement: Get portfolio cash statement
        api_response = await api_instance.get_portfolio_cash_statement(scope, code, from_effective_at, to_effective_at, as_at=as_at, filter=filter, recipe_id_scope=recipe_id_scope, recipe_id_code=recipe_id_code)
        print("The response of TransactionPortfoliosApi->get_portfolio_cash_statement:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionPortfoliosApi->get_portfolio_cash_statement: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this              uniquely identifies the portfolio. | 
 **from_effective_at** | **str**| The lower bound effective datetime or cut label (inclusive) from which to retrieve the data.              There is no lower bound if this is not specified. | 
 **to_effective_at** | **str**| The upper bound effective datetime or cut label (inclusive) from which to retrieve the data.              There is no upper bound if this is not specified. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the portfolio. Defaults to returning the latest version              of each transaction if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set.              For example, to return only transactions with a transaction type of &#39;Buy&#39;, specify \&quot;type eq &#39;Buy&#39;\&quot;.              For more information about filtering LUSID results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **recipe_id_scope** | **str**| The scope of the given recipeId | [optional] 
 **recipe_id_code** | **str**| The code of the given recipeID | [optional] 

### Return type

[**ResourceListOfPortfolioCashFlow**](ResourceListOfPortfolioCashFlow.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested portfolio cash flow data |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction_history**
> ResourceListOfChangeHistory get_transaction_history(scope, code, transaction_id, as_at=as_at)

[EARLY ACCESS] GetTransactionHistory: Get the history of a transaction

Get all of the changes that have happened to a transaction.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from lusid.models.resource_list_of_change_history import ResourceListOfChangeHistory
from pprint import pprint

from lusid import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
	  EnvironmentVariablesConfigurationLoader,
	  SecretsFileConfigurationLoader,
	  ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
    code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
    transaction_id = 'transaction_id_example' # str | The unique ID of the transaction to create or update.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the history of the transaction. Defaults              to return the latest version if not specified. (optional)

    try:
        # [EARLY ACCESS] GetTransactionHistory: Get the history of a transaction
        api_response = await api_instance.get_transaction_history(scope, code, transaction_id, as_at=as_at)
        print("The response of TransactionPortfoliosApi->get_transaction_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionPortfoliosApi->get_transaction_history: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. | 
 **transaction_id** | **str**| The unique ID of the transaction to create or update. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the history of the transaction. Defaults              to return the latest version if not specified. | [optional] 

### Return type

[**ResourceListOfChangeHistory**](ResourceListOfChangeHistory.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The history of the specified transaction (changes that have been made to it). |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transactions**
> VersionedResourceListOfTransaction get_transactions(scope, code, from_transaction_date=from_transaction_date, to_transaction_date=to_transaction_date, as_at=as_at, filter=filter, property_keys=property_keys, page=page, limit=limit, show_cancelled_transactions=show_cancelled_transactions, sort_by=sort_by)

GetTransactions: Get transactions

Retrieve all the transactions that occurred during a particular time interval.                If the portfolio is a derived transaction portfolio, the transactions returned are the  union set of all transactions of the parent (and any grandparents, etc.) as well as  those of the derived transaction portfolio itself.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from lusid.models.versioned_resource_list_of_transaction import VersionedResourceListOfTransaction
from pprint import pprint

from lusid import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
	  EnvironmentVariablesConfigurationLoader,
	  SecretsFileConfigurationLoader,
	  ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
    code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies               the transaction portfolio.
    from_transaction_date = 'from_transaction_date_example' # str | The lower bound effective datetime or cut label (inclusive) from which to retrieve transactions.               There is no lower bound if this is not specified. (optional)
    to_transaction_date = 'to_transaction_date_example' # str | The upper bound effective datetime or cut label (inclusive) from which to retrieve transactions.               There is no upper bound if this is not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve transactions. Defaults to returning the latest version               of each transaction if not specified. (optional)
    filter = 'filter_example' # str | Expression with which to filter the result set.               For example, to return only transactions with a transaction type of 'Buy', specify \"type eq 'Buy'\"               For more information about filtering LUSID results, see https://support.lusid.com/knowledgebase/article/KA-01914. (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the 'Instrument', 'Transaction', \"LegalEntity\" or \"CustodianAccount\" domain to decorate onto               transactions. These must have the format {domain}/{scope}/{code}, for example 'Instrument/system/Name' or               'Transaction/strategy/quantsignal'. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing transactions from a previous call to GetTransactions. (optional)
    limit = 56 # int | When paginating, limit the number of returned results to this many. The current behaviour is               to return all transactions if possible, but this will change to defaulting to 1000 if not specified in the future. It is recommended               to populate this field to enable pagination. (optional)
    show_cancelled_transactions = True # bool | Option to specify whether or not to include cancelled transactions,               including previous versions of transactions which have since been amended.               Defaults to False if not specified. (optional)
    sort_by = ['sort_by_example'] # List[str] | A list of field names or properties to sort by, each suffixed by \" ASC\" or \" DESC\" (optional)

    try:
        # GetTransactions: Get transactions
        api_response = await api_instance.get_transactions(scope, code, from_transaction_date=from_transaction_date, to_transaction_date=to_transaction_date, as_at=as_at, filter=filter, property_keys=property_keys, page=page, limit=limit, show_cancelled_transactions=show_cancelled_transactions, sort_by=sort_by)
        print("The response of TransactionPortfoliosApi->get_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionPortfoliosApi->get_transactions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this uniquely identifies               the transaction portfolio. | 
 **from_transaction_date** | **str**| The lower bound effective datetime or cut label (inclusive) from which to retrieve transactions.               There is no lower bound if this is not specified. | [optional] 
 **to_transaction_date** | **str**| The upper bound effective datetime or cut label (inclusive) from which to retrieve transactions.               There is no upper bound if this is not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve transactions. Defaults to returning the latest version               of each transaction if not specified. | [optional] 
 **filter** | **str**| Expression with which to filter the result set.               For example, to return only transactions with a transaction type of &#39;Buy&#39;, specify \&quot;type eq &#39;Buy&#39;\&quot;               For more information about filtering LUSID results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;Instrument&#39;, &#39;Transaction&#39;, \&quot;LegalEntity\&quot; or \&quot;CustodianAccount\&quot; domain to decorate onto               transactions. These must have the format {domain}/{scope}/{code}, for example &#39;Instrument/system/Name&#39; or               &#39;Transaction/strategy/quantsignal&#39;. | [optional] 
 **page** | **str**| The pagination token to use to continue listing transactions from a previous call to GetTransactions. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. The current behaviour is               to return all transactions if possible, but this will change to defaulting to 1000 if not specified in the future. It is recommended               to populate this field to enable pagination. | [optional] 
 **show_cancelled_transactions** | **bool**| Option to specify whether or not to include cancelled transactions,               including previous versions of transactions which have since been amended.               Defaults to False if not specified. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot; | [optional] 

### Return type

[**VersionedResourceListOfTransaction**](VersionedResourceListOfTransaction.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested transactions from the specified transaction portfolio |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_upsertable_portfolio_cash_flows**
> ResourceListOfTransaction get_upsertable_portfolio_cash_flows(scope, code, effective_at=effective_at, window_start=window_start, window_end=window_end, as_at=as_at, filter=filter, recipe_id_scope=recipe_id_scope, recipe_id_code=recipe_id_code, exclude_unsettled_trades=exclude_unsettled_trades)

[BETA] GetUpsertablePortfolioCashFlows: Get upsertable portfolio cash flows.

Get the set of cash flows that occur in a window for the given portfolio instruments as a set of upsertable transactions (DTOs).                Note that grouping can affect the quantity of information returned; where a holding is an amalgamation of one or more (e.g. cash) instruments, a unique  transaction identifier will not be available. The same may go for diagnostic information (e.g. multiple sources of an aggregate cash amount on a date that is  not split out. Grouping at the transaction and instrument level is recommended for those seeking to attribute individual flows.                In essence this is identical to the 'GetCashFlows' endpoint but returns the cash flows as a set of transactions suitable for directly putting back into LUSID.  There are a couple of important points:  (1) Internally it can not be fully known where the user wishes to insert these transactions, e.g. portfolio and movement type.      These are therefore defaulted to a sensible option; the user will likely need to change these.  (2) Similarly, knowledge of any properties the user might wish to add to a transaction are unknown and consequently left empty.  (3) The transaction id that is added is simply a concatenation of the original transaction id, instrument id and payment date and direction. The user can happily override this.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from lusid.models.resource_list_of_transaction import ResourceListOfTransaction
from pprint import pprint

from lusid import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
	  EnvironmentVariablesConfigurationLoader,
	  SecretsFileConfigurationLoader,
	  ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
    code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this               uniquely identifies the portfolio.
    effective_at = 'effective_at_example' # str | The valuation (pricing) effective datetime or cut label (inclusive) at which to evaluate the cashflows.  This determines whether cashflows are evaluated in a historic or forward looking context and will, for certain models, affect where data is looked up.  For example, on a swap if the effectiveAt is in the middle of the window, cashflows before it will be historic and resets assumed to exist where if the effectiveAt  is before the start of the range they are forward looking and will be expectations assuming the model supports that.  There is evidently a presumption here about availability of data and that the effectiveAt is realistically on or before the real-world today. (optional)
    window_start = 'window_start_example' # str | The lower bound effective datetime or cut label (inclusive) from which to retrieve the cashflows.               There is no lower bound if this is not specified. i.e. uses minimum date-time (optional)
    window_end = 'window_end_example' # str | The upper bound effective datetime or cut label (inclusive) from which to retrieve the cashflows.               The upper bound defaults to 'max date' if it is not specified (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the portfolio. Defaults to return the latest version               of each transaction if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the result set.               For example, to return only transactions with a transaction type of 'Buy', specify \"type eq 'Buy'\".               For more information about filtering LUSID results, see https://support.lusid.com/knowledgebase/article/KA-01914. (optional)
    recipe_id_scope = 'recipe_id_scope_example' # str | The scope of the given recipeId (optional)
    recipe_id_code = 'recipe_id_code_example' # str | The code of the given recipeID (optional)
    exclude_unsettled_trades = True # bool | If absent or set to true, unsettled trades will be excluded from the result set. If set to false, cashflows will returned based on trade date - more specifically, cashflows from any unsettled trades will be included in the results. (optional) (default to True)

    try:
        # [BETA] GetUpsertablePortfolioCashFlows: Get upsertable portfolio cash flows.
        api_response = await api_instance.get_upsertable_portfolio_cash_flows(scope, code, effective_at=effective_at, window_start=window_start, window_end=window_end, as_at=as_at, filter=filter, recipe_id_scope=recipe_id_scope, recipe_id_code=recipe_id_code, exclude_unsettled_trades=exclude_unsettled_trades)
        print("The response of TransactionPortfoliosApi->get_upsertable_portfolio_cash_flows:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionPortfoliosApi->get_upsertable_portfolio_cash_flows: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this               uniquely identifies the portfolio. | 
 **effective_at** | **str**| The valuation (pricing) effective datetime or cut label (inclusive) at which to evaluate the cashflows.  This determines whether cashflows are evaluated in a historic or forward looking context and will, for certain models, affect where data is looked up.  For example, on a swap if the effectiveAt is in the middle of the window, cashflows before it will be historic and resets assumed to exist where if the effectiveAt  is before the start of the range they are forward looking and will be expectations assuming the model supports that.  There is evidently a presumption here about availability of data and that the effectiveAt is realistically on or before the real-world today. | [optional] 
 **window_start** | **str**| The lower bound effective datetime or cut label (inclusive) from which to retrieve the cashflows.               There is no lower bound if this is not specified. i.e. uses minimum date-time | [optional] 
 **window_end** | **str**| The upper bound effective datetime or cut label (inclusive) from which to retrieve the cashflows.               The upper bound defaults to &#39;max date&#39; if it is not specified | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the portfolio. Defaults to return the latest version               of each transaction if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set.               For example, to return only transactions with a transaction type of &#39;Buy&#39;, specify \&quot;type eq &#39;Buy&#39;\&quot;.               For more information about filtering LUSID results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **recipe_id_scope** | **str**| The scope of the given recipeId | [optional] 
 **recipe_id_code** | **str**| The code of the given recipeID | [optional] 
 **exclude_unsettled_trades** | **bool**| If absent or set to true, unsettled trades will be excluded from the result set. If set to false, cashflows will returned based on trade date - more specifically, cashflows from any unsettled trades will be included in the results. | [optional] [default to True]

### Return type

[**ResourceListOfTransaction**](ResourceListOfTransaction.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested portfolio instruments&#39; cash flow data as a set of upsertable transactions |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_custodian_accounts**
> PagedResourceListOfCustodianAccount list_custodian_accounts(scope, code, effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, property_keys=property_keys)

[EXPERIMENTAL] ListCustodianAccounts: List Custodian Accounts

List the custodian accounts in a Transaction Portfolios

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from lusid.models.paged_resource_list_of_custodian_account import PagedResourceListOfCustodianAccount
from pprint import pprint

from lusid import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
	  EnvironmentVariablesConfigurationLoader,
	  SecretsFileConfigurationLoader,
	  ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the Transaction Portfolio.
    code = 'code_example' # str | The code of the Transaction Portfolio. Together with the scope this uniquely identifies              the Transaction Portfolios.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to list the TimeVariant properties decorated on Custodian Accounts. Defaults to the current LUSID              system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the instrument. Defaults to              returning the latest version if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing custodian accounts; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. (optional)
    limit = 56 # int | When paginating, limit the results to this number. Defaults to 100 if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the results.              For example, to filter on the Custodian Account type, specify \"code eq '001'\". For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the 'CustodianAccount' domain to decorate onto the Custodian Account.              These must have the format {domain}/{scope}/{code}, for example 'CustodianAccount/system/Name'. (optional)

    try:
        # [EXPERIMENTAL] ListCustodianAccounts: List Custodian Accounts
        api_response = await api_instance.list_custodian_accounts(scope, code, effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, property_keys=property_keys)
        print("The response of TransactionPortfoliosApi->list_custodian_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionPortfoliosApi->list_custodian_accounts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Transaction Portfolio. | 
 **code** | **str**| The code of the Transaction Portfolio. Together with the scope this uniquely identifies              the Transaction Portfolios. | 
 **effective_at** | **str**| The effective datetime or cut label at which to list the TimeVariant properties decorated on Custodian Accounts. Defaults to the current LUSID              system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the instrument. Defaults to              returning the latest version if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing custodian accounts; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results.              For example, to filter on the Custodian Account type, specify \&quot;code eq &#39;001&#39;\&quot;. For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;CustodianAccount&#39; domain to decorate onto the Custodian Account.              These must have the format {domain}/{scope}/{code}, for example &#39;CustodianAccount/system/Name&#39;. | [optional] 

### Return type

[**PagedResourceListOfCustodianAccount**](PagedResourceListOfCustodianAccount.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The custodian accounts in the given Transaction Portfolios. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_holdings_adjustments**
> ResourceListOfHoldingsAdjustmentHeader list_holdings_adjustments(scope, code, from_effective_at=from_effective_at, to_effective_at=to_effective_at, as_at=as_at)

ListHoldingsAdjustments: List holdings adjustments

List the holdings adjustments made to the specified transaction portfolio over a specified interval of effective time.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from lusid.models.resource_list_of_holdings_adjustment_header import ResourceListOfHoldingsAdjustmentHeader
from pprint import pprint

from lusid import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
	  EnvironmentVariablesConfigurationLoader,
	  SecretsFileConfigurationLoader,
	  ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
    code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
    from_effective_at = 'from_effective_at_example' # str | The lower bound effective datetime or cut label (inclusive) from which to retrieve the holdings              adjustments. There is no lower bound if this is not specified. (optional)
    to_effective_at = 'to_effective_at_example' # str | The upper bound effective datetime or cut label (inclusive) from which to retrieve the holdings              adjustments. There is no upper bound if this is not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the holdings adjustments. Defaults to return the              latest version of each holding adjustment if not specified. (optional)

    try:
        # ListHoldingsAdjustments: List holdings adjustments
        api_response = await api_instance.list_holdings_adjustments(scope, code, from_effective_at=from_effective_at, to_effective_at=to_effective_at, as_at=as_at)
        print("The response of TransactionPortfoliosApi->list_holdings_adjustments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionPortfoliosApi->list_holdings_adjustments: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. | 
 **from_effective_at** | **str**| The lower bound effective datetime or cut label (inclusive) from which to retrieve the holdings              adjustments. There is no lower bound if this is not specified. | [optional] 
 **to_effective_at** | **str**| The upper bound effective datetime or cut label (inclusive) from which to retrieve the holdings              adjustments. There is no upper bound if this is not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the holdings adjustments. Defaults to return the              latest version of each holding adjustment if not specified. | [optional] 

### Return type

[**ResourceListOfHoldingsAdjustmentHeader**](ResourceListOfHoldingsAdjustmentHeader.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The record of holdings adjustments made to the specified transaction portfolio |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **look_through_holdings**
> VersionedResourceListOfPortfolioHolding look_through_holdings(scope, code, effective_at=effective_at, as_at=as_at, filter=filter, property_keys=property_keys, quotes_scope=quotes_scope, slice=slice, share_class=share_class)

[EXPERIMENTAL] LookThroughHoldings: Get LookThrough Holdings

Calculate holdings for a transaction portfolio with lookthrough

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from lusid.models.versioned_resource_list_of_portfolio_holding import VersionedResourceListOfPortfolioHolding
from pprint import pprint

from lusid import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
	  EnvironmentVariablesConfigurationLoader,
	  SecretsFileConfigurationLoader,
	  ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
    code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve the holdings of the transaction              portfolio. Defaults to the current LUSID system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the holdings of the transaction portfolio. Defaults              to return the latest version if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the result set.              For example, to filter on the Holding Type, use \"holdingType eq 'p'\".              For more information about filtering LUSID results, see https://support.lusid.com/knowledgebase/article/KA-01914. (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the \"Instrument\", \"Holding\" or \"Portfolio\" domain to decorate onto              holdings. These must have the format {domain}/{scope}/{code}, for example \"Instrument/system/Name\" or \"Holding/system/Cost\". (optional)
    quotes_scope = 'quotes_scope_example' # str | The scope containing the quotes with the FX rates used for currency conversion. (optional)
    slice = 'slice_example' # str | When running LookThrough, define this slice as the root slice in the portfolio to look through from. (optional)
    share_class = 'share_class_example' # str | When running LookThrough, use this along with the slice parameter to specify              the root share class in the slice in the portfolio to look through from. The slice parameter is a prerequisite              for this parameter to be valid. (optional)

    try:
        # [EXPERIMENTAL] LookThroughHoldings: Get LookThrough Holdings
        api_response = await api_instance.look_through_holdings(scope, code, effective_at=effective_at, as_at=as_at, filter=filter, property_keys=property_keys, quotes_scope=quotes_scope, slice=slice, share_class=share_class)
        print("The response of TransactionPortfoliosApi->look_through_holdings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionPortfoliosApi->look_through_holdings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. | 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the holdings of the transaction              portfolio. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the holdings of the transaction portfolio. Defaults              to return the latest version if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set.              For example, to filter on the Holding Type, use \&quot;holdingType eq &#39;p&#39;\&quot;.              For more information about filtering LUSID results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the \&quot;Instrument\&quot;, \&quot;Holding\&quot; or \&quot;Portfolio\&quot; domain to decorate onto              holdings. These must have the format {domain}/{scope}/{code}, for example \&quot;Instrument/system/Name\&quot; or \&quot;Holding/system/Cost\&quot;. | [optional] 
 **quotes_scope** | **str**| The scope containing the quotes with the FX rates used for currency conversion. | [optional] 
 **slice** | **str**| When running LookThrough, define this slice as the root slice in the portfolio to look through from. | [optional] 
 **share_class** | **str**| When running LookThrough, use this along with the slice parameter to specify              the root share class in the slice in the portfolio to look through from. The slice parameter is a prerequisite              for this parameter to be valid. | [optional] 

### Return type

[**VersionedResourceListOfPortfolioHolding**](VersionedResourceListOfPortfolioHolding.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The holdings and version of the specified transaction portfolio with lookthrough |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **look_through_transactions**
> VersionedResourceListOfTransaction look_through_transactions(scope, code, from_transaction_date=from_transaction_date, to_transaction_date=to_transaction_date, as_at=as_at, filter=filter, property_keys=property_keys, page=page, limit=limit, quotes_scope=quotes_scope, slice=slice, share_class=share_class, use_alternate_scaling_logic=use_alternate_scaling_logic, alternate_effective_at=alternate_effective_at)

[EXPERIMENTAL] LookThroughTransactions: Look through transactions

Retrieve all the transactions that occurred during a particular time interval.    If the portfolio is part of a fund as defined in Fund Accounting documents, the transactions returned are the  union set of all transactions in portfolios of the same type, in any funds invested in by the portfolio's fund  (and any funds invested in from that fund, etc.).  The transactions will be scaled according to the ratio of the value of the investment in the fund to the NAV of the fund itself.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from lusid.models.versioned_resource_list_of_transaction import VersionedResourceListOfTransaction
from pprint import pprint

from lusid import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
	  EnvironmentVariablesConfigurationLoader,
	  SecretsFileConfigurationLoader,
	  ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
    code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
    from_transaction_date = 'from_transaction_date_example' # str | The lower bound effective datetime or cut label (inclusive) from which to retrieve transactions.              There is no lower bound if this is not specified. (optional)
    to_transaction_date = 'to_transaction_date_example' # str | The upper bound effective datetime or cut label (inclusive) from which to retrieve transactions.              There is no upper bound if this is not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve transactions. Defaults to returning the latest version              of each transaction if not specified. (optional)
    filter = 'filter_example' # str | Expression with which to filter the result set.              For example, to return only transactions with a transaction type of 'Buy', specify \"type eq 'Buy'\"              For more information about filtering LUSID results, see https://support.lusid.com/knowledgebase/article/KA-01914. (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the 'Instrument', 'Transaction', \"LegalEntity\" or \"CustodianAccount\" domain to decorate onto              transactions. These must have the format {domain}/{scope}/{code}, for example 'Instrument/system/Name' or              'Transaction/strategy/quantsignal'. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing transactions from a previous call to LookThroughTransactions. (optional)
    limit = 56 # int | When paginating, limit the number of returned results to this many. This will default to 1000 if not specified. (optional)
    quotes_scope = 'quotes_scope_example' # str | The scope containing the quotes with the FX rates used for currency conversion. (optional)
    slice = 'slice_example' # str | When running LookThrough, define this slice as the root slice in the portfolio to look through from. (optional)
    share_class = 'share_class_example' # str | When running LookThrough, use this along with the slice parameter to specify              the root share class in the slice in the portfolio to look through from. The slice parameter is a prerequisite              for this parameter to be valid. (optional)
    use_alternate_scaling_logic = False # bool | When running LookThrough, set this flag to use the same scaling logic as for LT Holdings (optional) (default to False)
    alternate_effective_at = 'alternate_effective_at_example' # str | This effectiveAt field is required when using alternate scaling logic to determine which fund and currency data is used for scaling (optional)

    try:
        # [EXPERIMENTAL] LookThroughTransactions: Look through transactions
        api_response = await api_instance.look_through_transactions(scope, code, from_transaction_date=from_transaction_date, to_transaction_date=to_transaction_date, as_at=as_at, filter=filter, property_keys=property_keys, page=page, limit=limit, quotes_scope=quotes_scope, slice=slice, share_class=share_class, use_alternate_scaling_logic=use_alternate_scaling_logic, alternate_effective_at=alternate_effective_at)
        print("The response of TransactionPortfoliosApi->look_through_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionPortfoliosApi->look_through_transactions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. | 
 **from_transaction_date** | **str**| The lower bound effective datetime or cut label (inclusive) from which to retrieve transactions.              There is no lower bound if this is not specified. | [optional] 
 **to_transaction_date** | **str**| The upper bound effective datetime or cut label (inclusive) from which to retrieve transactions.              There is no upper bound if this is not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve transactions. Defaults to returning the latest version              of each transaction if not specified. | [optional] 
 **filter** | **str**| Expression with which to filter the result set.              For example, to return only transactions with a transaction type of &#39;Buy&#39;, specify \&quot;type eq &#39;Buy&#39;\&quot;              For more information about filtering LUSID results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;Instrument&#39;, &#39;Transaction&#39;, \&quot;LegalEntity\&quot; or \&quot;CustodianAccount\&quot; domain to decorate onto              transactions. These must have the format {domain}/{scope}/{code}, for example &#39;Instrument/system/Name&#39; or              &#39;Transaction/strategy/quantsignal&#39;. | [optional] 
 **page** | **str**| The pagination token to use to continue listing transactions from a previous call to LookThroughTransactions. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. This will default to 1000 if not specified. | [optional] 
 **quotes_scope** | **str**| The scope containing the quotes with the FX rates used for currency conversion. | [optional] 
 **slice** | **str**| When running LookThrough, define this slice as the root slice in the portfolio to look through from. | [optional] 
 **share_class** | **str**| When running LookThrough, use this along with the slice parameter to specify              the root share class in the slice in the portfolio to look through from. The slice parameter is a prerequisite              for this parameter to be valid. | [optional] 
 **use_alternate_scaling_logic** | **bool**| When running LookThrough, set this flag to use the same scaling logic as for LT Holdings | [optional] [default to False]
 **alternate_effective_at** | **str**| This effectiveAt field is required when using alternate scaling logic to determine which fund and currency data is used for scaling | [optional] 

### Return type

[**VersionedResourceListOfTransaction**](VersionedResourceListOfTransaction.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested transactions from the specified transaction portfolio |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_portfolio_details**
> PortfolioDetails patch_portfolio_details(scope, code, operation, effective_at=effective_at)

[EARLY ACCESS] PatchPortfolioDetails: Patch portfolio details

Create or update certain details for a particular transaction portfolio.  The behaviour is defined by the JSON Patch specification.                Note that not all elements of a transaction portfolio definition are  modifiable once it has been created due to the potential implications for data already stored.  Currently supported properties are: SubHoldingKeys, BaseCurrency, AmortisationMethod

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from lusid.models.operation import Operation
from lusid.models.portfolio_details import PortfolioDetails
from pprint import pprint

from lusid import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
	  EnvironmentVariablesConfigurationLoader,
	  SecretsFileConfigurationLoader,
	  ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
    code = 'code_example' # str | The code of the transaction portfolio. Together with the               scope this uniquely identifies the transaction portfolio.
    operation = [{"value":["Transaction/Client/AccountType"],"path":"/subHoldingKeys","op":"add"},{"value":"GBP","path":"/baseCurrency","op":"add"},{"value":"newscope","path":"/transactiontypescope","op":"add"},{"value":"TransactionDate","path":"/cashGainLossCalculationDate","op":"add"}] # List[Operation] | The patch document.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which the updated or inserted details should become valid.               Defaults to the current LUSID system datetime if not specified.               Note that this will affect all bitemporal entities in the request, but will not be used for any perpetual entities. (optional)

    try:
        # [EARLY ACCESS] PatchPortfolioDetails: Patch portfolio details
        api_response = await api_instance.patch_portfolio_details(scope, code, operation, effective_at=effective_at)
        print("The response of TransactionPortfoliosApi->patch_portfolio_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionPortfoliosApi->patch_portfolio_details: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the               scope this uniquely identifies the transaction portfolio. | 
 **operation** | [**List[Operation]**](Operation.md)| The patch document. | 
 **effective_at** | **str**| The effective datetime or cut label at which the updated or inserted details should become valid.               Defaults to the current LUSID system datetime if not specified.               Note that this will affect all bitemporal entities in the request, but will not be used for any perpetual entities. | [optional] 

### Return type

[**PortfolioDetails**](PortfolioDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The newly patched details |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resolve_instrument**
> UpsertPortfolioTransactionsResponse resolve_instrument(scope, code, instrument_identifier_type, instrument_identifier_value, from_effective_at=from_effective_at, re_resolve=re_resolve, request_body=request_body)

[EARLY ACCESS] ResolveInstrument: Resolve instrument

Try to resolve the instrument for transaction and holdings for a given instrument identifier and a specified  period of time. Also update the instrument identifiers with the given instrument identifiers collection.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from lusid.models.upsert_portfolio_transactions_response import UpsertPortfolioTransactionsResponse
from pprint import pprint

from lusid import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
	  EnvironmentVariablesConfigurationLoader,
	  SecretsFileConfigurationLoader,
	  ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
    code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
    instrument_identifier_type = 'instrument_identifier_type_example' # str | The instrument identifier type.
    instrument_identifier_value = 'instrument_identifier_value_example' # str | The value for the given instrument identifier.
    from_effective_at = 'from_effective_at_example' # str | The lower bound effective datetime or cut label (inclusive) from which to retrieve the data.              There is no lower bound if this is not specified. (optional)
    re_resolve = False # bool | When set to true, instrument resolution will be attempted for all transactions and holdings for the given identifier and date range.              When set to false (default behaviour), instrument resolution will only be attempted for those transactions and holdings that were previously unresolved. (optional) (default to False)
    request_body = {"Instrument/default/Figi":"BBG000C6K6G9","Instrument/default/Isin":"GB00BH4HKS39"} # Dict[str, str] | The dictionary with the instrument identifiers to be updated on the             transaction and holdings. (optional)

    try:
        # [EARLY ACCESS] ResolveInstrument: Resolve instrument
        api_response = await api_instance.resolve_instrument(scope, code, instrument_identifier_type, instrument_identifier_value, from_effective_at=from_effective_at, re_resolve=re_resolve, request_body=request_body)
        print("The response of TransactionPortfoliosApi->resolve_instrument:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionPortfoliosApi->resolve_instrument: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. | 
 **instrument_identifier_type** | **str**| The instrument identifier type. | 
 **instrument_identifier_value** | **str**| The value for the given instrument identifier. | 
 **from_effective_at** | **str**| The lower bound effective datetime or cut label (inclusive) from which to retrieve the data.              There is no lower bound if this is not specified. | [optional] 
 **re_resolve** | **bool**| When set to true, instrument resolution will be attempted for all transactions and holdings for the given identifier and date range.              When set to false (default behaviour), instrument resolution will only be attempted for those transactions and holdings that were previously unresolved. | [optional] [default to False]
 **request_body** | [**Dict[str, str]**](str.md)| The dictionary with the instrument identifiers to be updated on the             transaction and holdings. | [optional] 

### Return type

[**UpsertPortfolioTransactionsResponse**](UpsertPortfolioTransactionsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The version of the transaction portfolio that contains the newly updated or inserted transactions |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_holdings**
> AdjustHolding set_holdings(scope, code, effective_at, adjust_holding_request, reconciliation_methods=reconciliation_methods)

SetHoldings: Set holdings

Set the holdings of the specified transaction portfolio to the provided targets. LUSID will automatically  construct adjustment transactions to ensure that the entire set of holdings for the transaction portfolio  are always set to the provided targets for the specified effective datetime. Read more about the difference between  adjusting and setting holdings here https://support.lusid.com/how-do-i-adjust-my-holdings.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from lusid.models.adjust_holding import AdjustHolding
from lusid.models.adjust_holding_request import AdjustHoldingRequest
from pprint import pprint

from lusid import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
	  EnvironmentVariablesConfigurationLoader,
	  SecretsFileConfigurationLoader,
	  ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
    code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which the holdings should be set to the provided targets.
    adjust_holding_request = [{"instrumentIdentifiers":{"Instrument/default/Figi":"BBG000C6K6G9","Instrument/default/Isin":"GB00BH4HKS39"},"subHoldingKeys":{"Transaction/Algo/Name":{"key":"Transaction/Algo/Name","value":{"labelValue":"Algo1"}}},"properties":{"Holding/ibor/CurrentMarketValue":{"key":"Holding/ibor/CurrentMarketValue","value":{"metricValue":{"value":1000}}}},"taxLots":[{"units":100,"cost":{"amount":10000,"currency":"GBP"},"portfolioCost":10000,"price":100,"purchaseDate":"2018-03-05T00:00:00.0000000+00:00","settlementDate":"2018-03-08T00:00:00.0000000+00:00"}],"currency":"GBP"}] # List[AdjustHoldingRequest] | The complete set of target holdings for the transaction portfolio.
    reconciliation_methods = ['reconciliation_methods_example'] # List[str] | Optional parameter for specifying a reconciliation method: e.g. FxForward. (optional)

    try:
        # SetHoldings: Set holdings
        api_response = await api_instance.set_holdings(scope, code, effective_at, adjust_holding_request, reconciliation_methods=reconciliation_methods)
        print("The response of TransactionPortfoliosApi->set_holdings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionPortfoliosApi->set_holdings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. | 
 **effective_at** | **str**| The effective datetime or cut label at which the holdings should be set to the provided targets. | 
 **adjust_holding_request** | [**List[AdjustHoldingRequest]**](AdjustHoldingRequest.md)| The complete set of target holdings for the transaction portfolio. | 
 **reconciliation_methods** | [**List[str]**](str.md)| Optional parameter for specifying a reconciliation method: e.g. FxForward. | [optional] 

### Return type

[**AdjustHolding**](AdjustHolding.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The version of the transaction portfolio that contains the newly set holdings |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_custodian_accounts**
> CustodianAccountsUpsertResponse upsert_custodian_accounts(scope, code, custodian_account_request)

[EXPERIMENTAL] UpsertCustodianAccounts: Upsert Custodian Accounts

Create or update Custodian Accounts in the Transaction Portfolios. A Custodian Account will be updated  if it already exists and created if it does not.  The batch limit per request is 2,000.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from lusid.models.custodian_account_request import CustodianAccountRequest
from lusid.models.custodian_accounts_upsert_response import CustodianAccountsUpsertResponse
from pprint import pprint

from lusid import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
	  EnvironmentVariablesConfigurationLoader,
	  SecretsFileConfigurationLoader,
	  ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the Transaction Portfolio.
    code = 'code_example' # str | The code of the Transaction Portfolio. Together with the scope this uniquely identifies              the Transaction Portfolios.
    custodian_account_request = [{"scope":"ScopeA","code":"Account1","status":"Active","accountNumber":"10003786BGBP","accountName":"Account1 Sterling","accountingMethod":"FirstInFirstOut","currency":"GBP","properties":{},"custodianIdentifier":{"idTypeScope":"ScopeA","idTypeCode":"LegalEntityCode1","code":"LegalEntityValue1"},"accountType":"Cash"},{"scope":"ScopeB","code":"Account2","status":"Active","accountNumber":"10003786BEUR","accountName":"Account2 Euro","accountingMethod":"FirstInFirstOut","currency":"EUR","properties":{},"custodianIdentifier":{"idTypeScope":"ScopeA","idTypeCode":"LegalEntityCode2","code":"LegalEntityValue2"},"accountType":"Swap"}] # List[CustodianAccountRequest] | A list of Custodian Accounts to be created or updated.

    try:
        # [EXPERIMENTAL] UpsertCustodianAccounts: Upsert Custodian Accounts
        api_response = await api_instance.upsert_custodian_accounts(scope, code, custodian_account_request)
        print("The response of TransactionPortfoliosApi->upsert_custodian_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionPortfoliosApi->upsert_custodian_accounts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Transaction Portfolio. | 
 **code** | **str**| The code of the Transaction Portfolio. Together with the scope this uniquely identifies              the Transaction Portfolios. | 
 **custodian_account_request** | [**List[CustodianAccountRequest]**](CustodianAccountRequest.md)| A list of Custodian Accounts to be created or updated. | 

### Return type

[**CustodianAccountsUpsertResponse**](CustodianAccountsUpsertResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The newly upserted custodian accounts. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_custodian_accounts_properties**
> CustodianAccountProperties upsert_custodian_accounts_properties(scope, code, custodian_account_scope, custodian_account_code, request_body=request_body)

[EXPERIMENTAL] UpsertCustodianAccountsProperties: Upsert custodian accounts properties

Update or insert one or more properties onto a single custodian account. A property will be updated if it  already exists and inserted if it does not. All properties must be of the domain 'CustodianAccount'.                Upserting a property that exists for a Transaction Portfolios, with a null value, will delete the instance of the property for that group.                Properties have an <i>effectiveFrom</i> datetime for which the property is valid, and an <i>effectiveUntil</i>  datetime until which the property is valid. Not supplying an <i>effectiveUntil</i> datetime results in the property being  valid indefinitely, or until the next <i>effectiveFrom</i> datetime of the property.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from lusid.models.custodian_account_properties import CustodianAccountProperties
from lusid.models.model_property import ModelProperty
from pprint import pprint

from lusid import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
	  EnvironmentVariablesConfigurationLoader,
	  SecretsFileConfigurationLoader,
	  ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the Transaction Portfolios to update or insert the properties onto.
    code = 'code_example' # str | The code of the Transaction Portfolios to update or insert the properties onto. Together with the scope this uniquely identifies the Transaction Portfolios.
    custodian_account_scope = 'custodian_account_scope_example' # str | The scope of the Custodian Account to update or insert the properties onto.
    custodian_account_code = 'custodian_account_code_example' # str | The unique ID of the custodian account to create or update properties for.
    request_body = {"CustodianAccount/MyScope/FundManagerName":{"key":"CustodianAccount/MyScope/FundManagerName","value":{"labelValue":"Smith"},"effectiveFrom":"2018-03-05T00:00:00.0000000+00:00"},"CustodianAccount/MyScope/SomeProperty":{"key":"CustodianAccount/MyScope/SomeProperty","value":{"labelValue":"SomeValue"},"effectiveFrom":"2016-01-01T00:00:00.0000000+00:00"},"CustodianAccount/MyScope/AnotherProperty":{"key":"CustodianAccount/MyScope/AnotherProperty","value":{"labelValue":"AnotherValue"},"effectiveFrom":"2018-03-05T00:00:00.0000000+00:00","effectiveUntil":"2020-01-01T00:00:00.0000000+00:00"},"CustodianAccount/MyScope/ReBalanceInterval":{"key":"CustodianAccount/MyScope/ReBalanceInterval","value":{"metricValue":{"value":30,"unit":"Days"}}}} # Dict[str, ModelProperty] | The properties to be updated or inserted onto the Transaction Portfolio. Each property in               the request must be keyed by its unique property key. This has the format {domain}/{scope}/{code} e.g. \"CustodianAccount/Manager/Id\". (optional)

    try:
        # [EXPERIMENTAL] UpsertCustodianAccountsProperties: Upsert custodian accounts properties
        api_response = await api_instance.upsert_custodian_accounts_properties(scope, code, custodian_account_scope, custodian_account_code, request_body=request_body)
        print("The response of TransactionPortfoliosApi->upsert_custodian_accounts_properties:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionPortfoliosApi->upsert_custodian_accounts_properties: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Transaction Portfolios to update or insert the properties onto. | 
 **code** | **str**| The code of the Transaction Portfolios to update or insert the properties onto. Together with the scope this uniquely identifies the Transaction Portfolios. | 
 **custodian_account_scope** | **str**| The scope of the Custodian Account to update or insert the properties onto. | 
 **custodian_account_code** | **str**| The unique ID of the custodian account to create or update properties for. | 
 **request_body** | [**Dict[str, ModelProperty]**](ModelProperty.md)| The properties to be updated or inserted onto the Transaction Portfolio. Each property in               the request must be keyed by its unique property key. This has the format {domain}/{scope}/{code} e.g. \&quot;CustodianAccount/Manager/Id\&quot;. | [optional] 

### Return type

[**CustodianAccountProperties**](CustodianAccountProperties.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated or inserted properties |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_portfolio_details**
> PortfolioDetails upsert_portfolio_details(scope, code, create_portfolio_details, effective_at=effective_at)

UpsertPortfolioDetails: Upsert portfolio details

Create or update certain details for a particular transaction portfolio. The details are updated if they already exist, and inserted if they do not.                Note that not all elements of a transaction portfolio definition are  modifiable once it has been created due to the potential implications for data already stored.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from lusid.models.create_portfolio_details import CreatePortfolioDetails
from lusid.models.portfolio_details import PortfolioDetails
from pprint import pprint

from lusid import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
	  EnvironmentVariablesConfigurationLoader,
	  SecretsFileConfigurationLoader,
	  ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
    code = 'code_example' # str | The code of the transaction portfolio. Together with the               scope this uniquely identifies the transaction portfolio.
    create_portfolio_details = {"corporateActionSourceId":{"scope":"Sources","code":"Vendor1"}} # CreatePortfolioDetails | The details to create or update for the specified transaction portfolio.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which the updated or inserted details should become valid.               Defaults to the current LUSID system datetime if not specified. (optional)

    try:
        # UpsertPortfolioDetails: Upsert portfolio details
        api_response = await api_instance.upsert_portfolio_details(scope, code, create_portfolio_details, effective_at=effective_at)
        print("The response of TransactionPortfoliosApi->upsert_portfolio_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionPortfoliosApi->upsert_portfolio_details: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the               scope this uniquely identifies the transaction portfolio. | 
 **create_portfolio_details** | [**CreatePortfolioDetails**](CreatePortfolioDetails.md)| The details to create or update for the specified transaction portfolio. | 
 **effective_at** | **str**| The effective datetime or cut label at which the updated or inserted details should become valid.               Defaults to the current LUSID system datetime if not specified. | [optional] 

### Return type

[**PortfolioDetails**](PortfolioDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The newly updated or inserted details |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_transaction_properties**
> UpsertTransactionPropertiesResponse upsert_transaction_properties(scope, code, transaction_id, request_body)

UpsertTransactionProperties: Upsert transaction properties

Create or update one or more transaction properties for a single transaction in the transaction portfolio.  Each property will be updated if it already exists and created if it does not.  Both transaction and portfolio must exist at the time when properties are created or updated.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from lusid.models.perpetual_property import PerpetualProperty
from lusid.models.upsert_transaction_properties_response import UpsertTransactionPropertiesResponse
from pprint import pprint

from lusid import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
	  EnvironmentVariablesConfigurationLoader,
	  SecretsFileConfigurationLoader,
	  ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
    code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
    transaction_id = 'transaction_id_example' # str | The unique ID of the transaction to create or update properties for.
    request_body = {"Transaction/MyScope/MyPropertyName":{"key":"Transaction/MyScope/MyPropertyName","value":{"metricValue":{"value":12345.5672,"unit":"Unit"}}},"Transaction/MyScope/MyPropertyName2":{"key":"Transaction/MyScope/MyPropertyName2","value":{"metricValue":{"value":925.3,"unit":"Unit"}}}} # Dict[str, PerpetualProperty] | The properties and their associated values to create or update.

    try:
        # UpsertTransactionProperties: Upsert transaction properties
        api_response = await api_instance.upsert_transaction_properties(scope, code, transaction_id, request_body)
        print("The response of TransactionPortfoliosApi->upsert_transaction_properties:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionPortfoliosApi->upsert_transaction_properties: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. | 
 **transaction_id** | **str**| The unique ID of the transaction to create or update properties for. | 
 **request_body** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md)| The properties and their associated values to create or update. | 

### Return type

[**UpsertTransactionPropertiesResponse**](UpsertTransactionPropertiesResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The version of the transaction portfolio that contains the newly updated or inserted transaction property |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_transactions**
> UpsertPortfolioTransactionsResponse upsert_transactions(scope, code, transaction_request, preserve_properties=preserve_properties)

UpsertTransactions: Upsert transactions

Create or update transactions in the transaction portfolio. A transaction will be updated  if it already exists and created if it does not.  The maximum number of transactions that this method can upsert per request is 10,000.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from lusid.models.transaction_request import TransactionRequest
from lusid.models.upsert_portfolio_transactions_response import UpsertPortfolioTransactionsResponse
from pprint import pprint

from lusid import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
	  EnvironmentVariablesConfigurationLoader,
	  SecretsFileConfigurationLoader,
	  ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.TransactionPortfoliosApi)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
    code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
    transaction_request = [{"transactionId":"TransactionId-111111","type":"StockIn","instrumentIdentifiers":{"Instrument/default/Figi":"BBG000C6K6G9","Instrument/default/Isin":"GB00BH4HKS39"},"transactionDate":"2018-03-05T00:00:00.0000000+00:00","settlementDate":"2018-03-08T00:00:00.0000000+00:00","units":1000,"transactionPrice":{"price":123,"type":"Price"},"totalConsideration":{"amount":123000,"currency":"GBP"},"transactionCurrency":"GBP","properties":{"Transaction/Algo/Name":{"key":"Transaction/Algo/Name","value":{"labelValue":"Algo1"}}},"counterpartyId":"CounterpartyId-118263","source":"","otcConfirmation":{"counterpartyAgreementId":{"scope":"someScope","code":"someCode"}},"orderId":{"scope":"someScope","code":"ORD001"},"allocationId":{"scope":"someScope","code":"ALLOC001"}}] # List[TransactionRequest] | A list of transactions to be created or updated.
    preserve_properties = True # bool | If set to false, the entire property set will be overwritten by the provided properties. If not specified or set to true, only the properties provided will be updated. (optional) (default to True)

    try:
        # UpsertTransactions: Upsert transactions
        api_response = await api_instance.upsert_transactions(scope, code, transaction_request, preserve_properties=preserve_properties)
        print("The response of TransactionPortfoliosApi->upsert_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionPortfoliosApi->upsert_transactions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. | 
 **transaction_request** | [**List[TransactionRequest]**](TransactionRequest.md)| A list of transactions to be created or updated. | 
 **preserve_properties** | **bool**| If set to false, the entire property set will be overwritten by the provided properties. If not specified or set to true, only the properties provided will be updated. | [optional] [default to True]

### Return type

[**UpsertPortfolioTransactionsResponse**](UpsertPortfolioTransactionsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The version of the transaction portfolio that contains the newly updated or inserted transactions |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

