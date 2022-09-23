# lusid.TransactionPortfoliosApi

All URIs are relative to *https://fbn-prd.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adjust_holdings**](TransactionPortfoliosApi.md#adjust_holdings) | **POST** /api/transactionportfolios/{scope}/{code}/holdings | AdjustHoldings: Adjust holdings
[**build_transactions**](TransactionPortfoliosApi.md#build_transactions) | **POST** /api/transactionportfolios/{scope}/{code}/transactions/$build | BuildTransactions: Build transactions
[**cancel_adjust_holdings**](TransactionPortfoliosApi.md#cancel_adjust_holdings) | **DELETE** /api/transactionportfolios/{scope}/{code}/holdings | CancelAdjustHoldings: Cancel adjust holdings
[**cancel_transactions**](TransactionPortfoliosApi.md#cancel_transactions) | **DELETE** /api/transactionportfolios/{scope}/{code}/transactions | CancelTransactions: Cancel transactions
[**create_portfolio**](TransactionPortfoliosApi.md#create_portfolio) | **POST** /api/transactionportfolios/{scope} | CreatePortfolio: Create portfolio
[**delete_properties_from_transaction**](TransactionPortfoliosApi.md#delete_properties_from_transaction) | **DELETE** /api/transactionportfolios/{scope}/{code}/transactions/{transactionId}/properties | DeletePropertiesFromTransaction: Delete properties from transaction
[**get_a2_b_data**](TransactionPortfoliosApi.md#get_a2_b_data) | **GET** /api/transactionportfolios/{scope}/{code}/a2b | GetA2BData: Get A2B data
[**get_a2_b_movements**](TransactionPortfoliosApi.md#get_a2_b_movements) | **GET** /api/transactionportfolios/{scope}/{code}/a2bmovements | GetA2BMovements: Get an A2B report at the movement level for the given portfolio.
[**get_details**](TransactionPortfoliosApi.md#get_details) | **GET** /api/transactionportfolios/{scope}/{code}/details | GetDetails: Get details
[**get_holdings**](TransactionPortfoliosApi.md#get_holdings) | **GET** /api/transactionportfolios/{scope}/{code}/holdings | GetHoldings: Get holdings
[**get_holdings_adjustment**](TransactionPortfoliosApi.md#get_holdings_adjustment) | **GET** /api/transactionportfolios/{scope}/{code}/holdingsadjustments/{effectiveAt} | GetHoldingsAdjustment: Get holdings adjustment
[**get_portfolio_cash_ladder**](TransactionPortfoliosApi.md#get_portfolio_cash_ladder) | **GET** /api/transactionportfolios/{scope}/{code}/cashladder | GetPortfolioCashLadder: Get portfolio cash ladder
[**get_portfolio_cash_statement**](TransactionPortfoliosApi.md#get_portfolio_cash_statement) | **GET** /api/transactionportfolios/{scope}/{code}/cashstatement | GetPortfolioCashStatement: Get portfolio cash statement
[**get_transaction_history**](TransactionPortfoliosApi.md#get_transaction_history) | **GET** /api/transactionportfolios/{scope}/{code}/transactions/{transactionId}/history | [EARLY ACCESS] GetTransactionHistory: Get the history of a transaction
[**get_transactions**](TransactionPortfoliosApi.md#get_transactions) | **GET** /api/transactionportfolios/{scope}/{code}/transactions | GetTransactions: Get transactions
[**list_holdings_adjustments**](TransactionPortfoliosApi.md#list_holdings_adjustments) | **GET** /api/transactionportfolios/{scope}/{code}/holdingsadjustments | ListHoldingsAdjustments: List holdings adjustments
[**resolve_instrument**](TransactionPortfoliosApi.md#resolve_instrument) | **POST** /api/transactionportfolios/{scope}/{code}/$resolve | [EARLY ACCESS] ResolveInstrument: Resolve instrument
[**set_holdings**](TransactionPortfoliosApi.md#set_holdings) | **PUT** /api/transactionportfolios/{scope}/{code}/holdings | SetHoldings: Set holdings
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
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-prd.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.TransactionPortfoliosApi(api_client)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
effective_at = 'effective_at_example' # str | The effective datetime or cut label at which the holdings should be set to the provided targets.
adjust_holding_request = [{"instrumentIdentifiers":{"instrument/default/Figi":"BBG000C6K6G9","instrument/default/Isin":"GB00BH4HKS39"},"subHoldingKeys":{"transaction/Algo/Name":{"key":"Transaction/Algo/Name","value":{"labelValue":"Algo1"}}},"properties":{"holding/Entity/Name":{"key":"Holding/Entity/Name","value":{"labelValue":"Financial Entity"}}},"taxLots":[{"units":100,"cost":{"amount":10000,"currency":"GBP"},"portfolioCost":10000,"price":100,"purchaseDate":"2018-03-05T00:00:00.0000000+00:00","settlementDate":"2018-03-08T00:00:00.0000000+00:00"}],"currency":"GBP"}] # list[AdjustHoldingRequest] | The selected set of holdings to adjust to the provided targets for the              transaction portfolio.
reconciliation_methods = ['reconciliation_methods_example'] # list[str] | Optional parameter for specifying a reconciliation method: e.g. FxForward. (optional)

    try:
        # AdjustHoldings: Adjust holdings
        api_response = api_instance.adjust_holdings(scope, code, effective_at, adjust_holding_request, reconciliation_methods=reconciliation_methods)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TransactionPortfoliosApi->adjust_holdings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. | 
 **effective_at** | **str**| The effective datetime or cut label at which the holdings should be set to the provided targets. | 
 **adjust_holding_request** | [**list[AdjustHoldingRequest]**](AdjustHoldingRequest.md)| The selected set of holdings to adjust to the provided targets for the              transaction portfolio. | 
 **reconciliation_methods** | [**list[str]**](str.md)| Optional parameter for specifying a reconciliation method: e.g. FxForward. | [optional] 

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

# **build_transactions**
> VersionedResourceListOfOutputTransaction build_transactions(scope, code, transaction_query_parameters, as_at=as_at, filter=filter, property_keys=property_keys, limit=limit, page=page)

BuildTransactions: Build transactions

Builds and returns all transactions that affect the holdings of a portfolio over a given interval of  effective time into a set of output transactions. This includes transactions automatically generated by  LUSID such as holding adjustments.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-prd.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.TransactionPortfoliosApi(api_client)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
transaction_query_parameters = {"startDate":"2018-03-05T00:00:00.0000000+00:00","endDate":"2018-03-19T00:00:00.0000000+00:00","queryMode":"TradeDate","showCancelledTransactions":false} # TransactionQueryParameters | The query queryParameters which control how the output transactions are built.
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to build the transactions. Defaults to return the latest              version of each transaction if not specified. (optional)
filter = 'filter_example' # str | Expression to filter the result set.              For example, to return only transactions with a transaction type of 'Buy', specify \"type eq 'Buy'\".              For more information about filtering LUSID results, see https://support.lusid.com/knowledgebase/article/KA-01914. (optional)
property_keys = ['property_keys_example'] # list[str] | A list of property keys from the \"Instrument\" or \"Transaction\" domain to decorate onto              the transactions. These take the format {domain}/{scope}/{code} e.g. \"Instrument/system/Name\" or              \"Transaction/strategy/quantsignal\". (optional)
limit = 56 # int | When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. (optional)
page = 'page_example' # str | The pagination token to use to continue listing transactions from a previous call to BuildTransactions. (optional)

    try:
        # BuildTransactions: Build transactions
        api_response = api_instance.build_transactions(scope, code, transaction_query_parameters, as_at=as_at, filter=filter, property_keys=property_keys, limit=limit, page=page)
        pprint(api_response)
    except ApiException as e:
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
 **property_keys** | [**list[str]**](str.md)| A list of property keys from the \&quot;Instrument\&quot; or \&quot;Transaction\&quot; domain to decorate onto              the transactions. These take the format {domain}/{scope}/{code} e.g. \&quot;Instrument/system/Name\&quot; or              \&quot;Transaction/strategy/quantsignal\&quot;. | [optional] 
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
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-prd.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.TransactionPortfoliosApi(api_client)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
effective_at = 'effective_at_example' # str | The effective datetime or cut label at which the holding adjustments should be undone.

    try:
        # CancelAdjustHoldings: Cancel adjust holdings
        api_response = api_instance.cancel_adjust_holdings(scope, code, effective_at)
        pprint(api_response)
    except ApiException as e:
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
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-prd.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.TransactionPortfoliosApi(api_client)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
transaction_ids = ['transaction_ids_example'] # list[str] | The IDs of the transactions to cancel.

    try:
        # CancelTransactions: Cancel transactions
        api_response = api_instance.cancel_transactions(scope, code, transaction_ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TransactionPortfoliosApi->cancel_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. | 
 **transaction_ids** | [**list[str]**](str.md)| The IDs of the transactions to cancel. | 

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
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-prd.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.TransactionPortfoliosApi(api_client)
    scope = 'scope_example' # str | The scope in which to create the transaction portfolio.
create_transaction_portfolio_request = {"displayName":"Portfolio UK","description":"Portfolio for UK market","code":"PortfolioUk","created":"2018-03-05T12:00:00.0000000+00:00","baseCurrency":"GBP","corporateActionSourceId":{"scope":"Sources","code":"Vendor1"},"accountingMethod":"Default","subHoldingKeys":[],"properties":{"portfolio/Manager/Name":{"key":"Portfolio/Manager/Name","value":{"labelValue":"Matt Smith"},"effectiveFrom":"2018-03-05T12:00:00.0000000+00:00"},"portfolio/Manager/Id":{"key":"Portfolio/Manager/Id","value":{"metricValue":{"value":1628483,"unit":"NoUnits"}},"effectiveFrom":"2018-03-05T12:00:00.0000000+00:00"}},"instrumentScopes":[],"amortisationMethod":"NoAmortisation"} # CreateTransactionPortfolioRequest | The definition of the transaction portfolio.

    try:
        # CreatePortfolio: Create portfolio
        api_response = api_instance.create_portfolio(scope, create_transaction_portfolio_request)
        pprint(api_response)
    except ApiException as e:
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

# **delete_properties_from_transaction**
> DeletedEntityResponse delete_properties_from_transaction(scope, code, transaction_id, property_keys)

DeletePropertiesFromTransaction: Delete properties from transaction

Delete one or more properties from a single transaction in a transaction portfolio.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-prd.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.TransactionPortfoliosApi(api_client)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
transaction_id = 'transaction_id_example' # str | The unique ID of the transaction from which to delete properties.
property_keys = ['property_keys_example'] # list[str] | The property keys of the properties to delete.              These must be from the \"Transaction\" domain and have the format {domain}/{scope}/{code}, for example              \"Transaction/strategy/quantsignal\".

    try:
        # DeletePropertiesFromTransaction: Delete properties from transaction
        api_response = api_instance.delete_properties_from_transaction(scope, code, transaction_id, property_keys)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TransactionPortfoliosApi->delete_properties_from_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. | 
 **transaction_id** | **str**| The unique ID of the transaction from which to delete properties. | 
 **property_keys** | [**list[str]**](str.md)| The property keys of the properties to delete.              These must be from the \&quot;Transaction\&quot; domain and have the format {domain}/{scope}/{code}, for example              \&quot;Transaction/strategy/quantsignal\&quot;. | 

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
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-prd.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.TransactionPortfoliosApi(api_client)
    scope = 'scope_example' # str | The scope of the portfolio to retrieve the A2B report for.
code = 'code_example' # str | The code of the portfolio to retrieve the A2B report for. Together with the scope this              uniquely identifies the portfolio.
from_effective_at = 'from_effective_at_example' # str | The lower bound effective datetime or cut label (inclusive) from which to retrieve the data.              There is no lower bound if this is not specified.
to_effective_at = 'to_effective_at_example' # str | The upper bound effective datetime or cut label (inclusive) from which to retrieve the data.              There is no upper bound if this is not specified.
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the portfolio. Defaults to return the latest version              of each transaction if not specified. (optional)
recipe_id_scope = 'recipe_id_scope_example' # str | The scope of the given recipeId (optional)
recipe_id_code = 'recipe_id_code_example' # str | The code of the given recipeId (optional)
property_keys = ['property_keys_example'] # list[str] | A list of property keys from the \"Instrument\" domain to decorate onto              the results. These take the format {domain}/{scope}/{code} e.g. \"Instrument/system/Name\". (optional)
filter = 'filter_example' # str | Expression to filter the result set.              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)

    try:
        # GetA2BData: Get A2B data
        api_response = api_instance.get_a2_b_data(scope, code, from_effective_at, to_effective_at, as_at=as_at, recipe_id_scope=recipe_id_scope, recipe_id_code=recipe_id_code, property_keys=property_keys, filter=filter)
        pprint(api_response)
    except ApiException as e:
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
 **property_keys** | [**list[str]**](str.md)| A list of property keys from the \&quot;Instrument\&quot; domain to decorate onto              the results. These take the format {domain}/{scope}/{code} e.g. \&quot;Instrument/system/Name\&quot;. | [optional] 
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
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-prd.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.TransactionPortfoliosApi(api_client)
    scope = 'scope_example' # str | The scope of the portfolio to retrieve the A2B movement report for.
code = 'code_example' # str | The code of the portfolio to retrieve the A2B movement report for. Together with the scope this              uniquely identifies the portfolio.
from_effective_at = 'from_effective_at_example' # str | The lower bound effective datetime or cut label (inclusive) from which to retrieve the data.              There is no lower bound if this is not specified.
to_effective_at = 'to_effective_at_example' # str | The upper bound effective datetime or cut label (inclusive) from which to retrieve the data.              There is no upper bound if this is not specified.
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the portfolio. Defaults to return the latest version              of each transaction if not specified. (optional)
recipe_id_scope = 'recipe_id_scope_example' # str | The scope of the given recipeId (optional)
recipe_id_code = 'recipe_id_code_example' # str | The code of the given recipeId (optional)
property_keys = ['property_keys_example'] # list[str] | A list of property keys from the \"Instrument\" domain to decorate onto              the results. These take the format {domain}/{scope}/{code} e.g. \"Instrument/system/Name\". (optional)
filter = 'filter_example' # str | Expression to filter the result set.              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)

    try:
        # GetA2BMovements: Get an A2B report at the movement level for the given portfolio.
        api_response = api_instance.get_a2_b_movements(scope, code, from_effective_at, to_effective_at, as_at=as_at, recipe_id_scope=recipe_id_scope, recipe_id_code=recipe_id_code, property_keys=property_keys, filter=filter)
        pprint(api_response)
    except ApiException as e:
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
 **property_keys** | [**list[str]**](str.md)| A list of property keys from the \&quot;Instrument\&quot; domain to decorate onto              the results. These take the format {domain}/{scope}/{code} e.g. \&quot;Instrument/system/Name\&quot;. | [optional] 
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

# **get_details**
> PortfolioDetails get_details(scope, code, effective_at=effective_at, as_at=as_at)

GetDetails: Get details

Get certain details associated with a transaction portfolio.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-prd.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.TransactionPortfoliosApi(api_client)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
code = 'code_example' # str | The code of the transaction portfolio. Together with the              scope this uniquely identifies the transaction portfolio.
effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve the details of the transaction              portfolio. Defaults to the current LUSID system datetime if not specified. (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the details of the transaction portfolio. Defaults              to returning the latest version of the details if not specified. (optional)

    try:
        # GetDetails: Get details
        api_response = api_instance.get_details(scope, code, effective_at=effective_at, as_at=as_at)
        pprint(api_response)
    except ApiException as e:
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

# **get_holdings**
> VersionedResourceListOfPortfolioHolding get_holdings(scope, code, effective_at=effective_at, as_at=as_at, filter=filter, property_keys=property_keys, by_taxlots=by_taxlots)

GetHoldings: Get holdings

Calculate holdings for a transaction portfolio.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-prd.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.TransactionPortfoliosApi(api_client)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve the holdings of the transaction              portfolio. Defaults to the current LUSID system datetime if not specified. (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the holdings of the transaction portfolio. Defaults              to return the latest version if not specified. (optional)
filter = 'filter_example' # str | Expression to filter the result set.              For example, to filter on the Holding Type, use \"holdingType eq 'p'\".              For more information about filtering LUSID results, see https://support.lusid.com/knowledgebase/article/KA-01914. (optional)
property_keys = ['property_keys_example'] # list[str] | A list of property keys from the \"Instrument\" or \"Holding\" domain to decorate onto              holdings. These must have the format {domain}/{scope}/{code}, for example \"Instrument/system/Name\" or \"Holding/system/Cost\". (optional)
by_taxlots = True # bool | Whether or not to expand the holdings to return the underlying tax-lots. Defaults to              False. (optional)

    try:
        # GetHoldings: Get holdings
        api_response = api_instance.get_holdings(scope, code, effective_at=effective_at, as_at=as_at, filter=filter, property_keys=property_keys, by_taxlots=by_taxlots)
        pprint(api_response)
    except ApiException as e:
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
 **property_keys** | [**list[str]**](str.md)| A list of property keys from the \&quot;Instrument\&quot; or \&quot;Holding\&quot; domain to decorate onto              holdings. These must have the format {domain}/{scope}/{code}, for example \&quot;Instrument/system/Name\&quot; or \&quot;Holding/system/Cost\&quot;. | [optional] 
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
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-prd.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.TransactionPortfoliosApi(api_client)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
effective_at = 'effective_at_example' # str | The effective datetime or cut label of the holdings adjustment.
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the holdings adjustment. Defaults to the return the latest              version of the holdings adjustment if not specified. (optional)
property_keys = ['property_keys_example'] # list[str] | A list of property keys from the ‘Instrument' domain to decorate onto holdings adjustments.              These must have the format {domain}/{scope}/{code}, for example 'Instrument/system/Name'.              Note that properties from the 'Holding’ domain are automatically returned. (optional)

    try:
        # GetHoldingsAdjustment: Get holdings adjustment
        api_response = api_instance.get_holdings_adjustment(scope, code, effective_at, as_at=as_at, property_keys=property_keys)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TransactionPortfoliosApi->get_holdings_adjustment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. | 
 **effective_at** | **str**| The effective datetime or cut label of the holdings adjustment. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the holdings adjustment. Defaults to the return the latest              version of the holdings adjustment if not specified. | [optional] 
 **property_keys** | [**list[str]**](str.md)| A list of property keys from the ‘Instrument&#39; domain to decorate onto holdings adjustments.              These must have the format {domain}/{scope}/{code}, for example &#39;Instrument/system/Name&#39;.              Note that properties from the &#39;Holding’ domain are automatically returned. | [optional] 

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

# **get_portfolio_cash_ladder**
> ResourceListOfPortfolioCashLadder get_portfolio_cash_ladder(scope, code, from_effective_at, to_effective_at, effective_at, as_at=as_at, filter=filter, recipe_id_scope=recipe_id_scope, recipe_id_code=recipe_id_code)

GetPortfolioCashLadder: Get portfolio cash ladder

Get a cash ladder for a transaction portfolio.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-prd.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.TransactionPortfoliosApi(api_client)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this              uniquely identifies the portfolio.
from_effective_at = 'from_effective_at_example' # str | The lower bound effective datetime or cut label (inclusive) from which to retrieve the data.              There is no lower bound if this is not specified.
to_effective_at = 'to_effective_at_example' # str | The upper bound effective datetime or cut label (inclusive) from which to retrieve the data.              There is no upper bound if this is not specified.
effective_at = 'effective_at_example' # str | The valuation (pricing) effective datetime or cut label (inclusive) at which to evaluate the cashflows.  This determines whether cashflows are evaluated in a historic or forward looking context and will, for certain models, affect where data is looked up.  For example, on a swap if the effectiveAt is in the middle of the window, cashflows before it will be historic and resets assumed to exist where if the effectiveAt  is before the start of the range they are forward looking and will be expectations assuming the model supports that.  There is evidently a presumption here about availability of data and that the effectiveAt is realistically on or before the real-world today.
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the portfolio. Defaults to returning the latest version              of each transaction if not specified. (optional)
filter = 'filter_example' # str | Expression to filter the result set.              For example, to return only transactions with a transaction type of 'Buy', specify \"type eq 'Buy'\".              For more information about filtering LUSID results, see https://support.lusid.com/knowledgebase/article/KA-01914. (optional)
recipe_id_scope = 'recipe_id_scope_example' # str | The scope of the given recipeId (optional)
recipe_id_code = 'recipe_id_code_example' # str | The code of the given recipeID (optional)

    try:
        # GetPortfolioCashLadder: Get portfolio cash ladder
        api_response = api_instance.get_portfolio_cash_ladder(scope, code, from_effective_at, to_effective_at, effective_at, as_at=as_at, filter=filter, recipe_id_scope=recipe_id_scope, recipe_id_code=recipe_id_code)
        pprint(api_response)
    except ApiException as e:
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
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-prd.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.TransactionPortfoliosApi(api_client)
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
        api_response = api_instance.get_portfolio_cash_statement(scope, code, from_effective_at, to_effective_at, as_at=as_at, filter=filter, recipe_id_scope=recipe_id_scope, recipe_id_code=recipe_id_code)
        pprint(api_response)
    except ApiException as e:
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
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-prd.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.TransactionPortfoliosApi(api_client)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
transaction_id = 'transaction_id_example' # str | The unique ID of the transaction to create or update.
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the history of the transaction. Defaults              to return the latest version if not specified. (optional)

    try:
        # [EARLY ACCESS] GetTransactionHistory: Get the history of a transaction
        api_response = api_instance.get_transaction_history(scope, code, transaction_id, as_at=as_at)
        pprint(api_response)
    except ApiException as e:
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
> VersionedResourceListOfTransaction get_transactions(scope, code, from_transaction_date=from_transaction_date, to_transaction_date=to_transaction_date, as_at=as_at, filter=filter, property_keys=property_keys, page=page, limit=limit, show_cancelled_transactions=show_cancelled_transactions)

GetTransactions: Get transactions

Retrieve all the transactions that occurred during a particular time interval.                If the portfolio is a derived transaction portfolio, the transactions returned are the  union set of all transactions of the parent (and any grandparents, etc.) as well as  those of the derived transaction portfolio itself.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-prd.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.TransactionPortfoliosApi(api_client)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies               the transaction portfolio.
from_transaction_date = 'from_transaction_date_example' # str | The lower bound effective datetime or cut label (inclusive) from which to retrieve transactions.               There is no lower bound if this is not specified. (optional)
to_transaction_date = 'to_transaction_date_example' # str | The upper bound effective datetime or cut label (inclusive) from which to retrieve transactions.               There is no upper bound if this is not specified. (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve transactions. Defaults to returning the latest version               of each transaction if not specified. (optional)
filter = 'filter_example' # str | Expression with which to filter the result set.               For example, to return only transactions with a transaction type of 'Buy', specify \"type eq 'Buy'\"               For more information about filtering LUSID results, see https://support.lusid.com/knowledgebase/article/KA-01914. (optional)
property_keys = ['property_keys_example'] # list[str] | A list of property keys from the 'Instrument' or 'Transaction' domain to decorate onto               transactions. These must have the format {domain}/{scope}/{code}, for example 'Instrument/system/Name' or               'Transaction/strategy/quantsignal'. (optional)
page = 'page_example' # str | The pagination token to use to continue listing transactions from a previous call to GetTransactions. (optional)
limit = 56 # int | When paginating, limit the number of returned results to this many. The current behaviour is               to return all transactions if possible, but this will change to defaulting to 1000 if not specified in the future. It is recommended               to populate this field to enable pagination. (optional)
show_cancelled_transactions = True # bool | Option to specify whether or not to include cancelled transactions,               including previous versions of transactions which have since been amended.               Defaults to False if not specified. (optional)

    try:
        # GetTransactions: Get transactions
        api_response = api_instance.get_transactions(scope, code, from_transaction_date=from_transaction_date, to_transaction_date=to_transaction_date, as_at=as_at, filter=filter, property_keys=property_keys, page=page, limit=limit, show_cancelled_transactions=show_cancelled_transactions)
        pprint(api_response)
    except ApiException as e:
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
 **property_keys** | [**list[str]**](str.md)| A list of property keys from the &#39;Instrument&#39; or &#39;Transaction&#39; domain to decorate onto               transactions. These must have the format {domain}/{scope}/{code}, for example &#39;Instrument/system/Name&#39; or               &#39;Transaction/strategy/quantsignal&#39;. | [optional] 
 **page** | **str**| The pagination token to use to continue listing transactions from a previous call to GetTransactions. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. The current behaviour is               to return all transactions if possible, but this will change to defaulting to 1000 if not specified in the future. It is recommended               to populate this field to enable pagination. | [optional] 
 **show_cancelled_transactions** | **bool**| Option to specify whether or not to include cancelled transactions,               including previous versions of transactions which have since been amended.               Defaults to False if not specified. | [optional] 

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

# **list_holdings_adjustments**
> ResourceListOfHoldingsAdjustmentHeader list_holdings_adjustments(scope, code, from_effective_at=from_effective_at, to_effective_at=to_effective_at, as_at=as_at)

ListHoldingsAdjustments: List holdings adjustments

List the holdings adjustments made to the specified transaction portfolio over a specified interval of effective time.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-prd.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.TransactionPortfoliosApi(api_client)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
from_effective_at = 'from_effective_at_example' # str | The lower bound effective datetime or cut label (inclusive) from which to retrieve the holdings              adjustments. There is no lower bound if this is not specified. (optional)
to_effective_at = 'to_effective_at_example' # str | The upper bound effective datetime or cut label (inclusive) from which to retrieve the holdings              adjustments. There is no upper bound if this is not specified. (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the holdings adjustments. Defaults to return the              latest version of each holding adjustment if not specified. (optional)

    try:
        # ListHoldingsAdjustments: List holdings adjustments
        api_response = api_instance.list_holdings_adjustments(scope, code, from_effective_at=from_effective_at, to_effective_at=to_effective_at, as_at=as_at)
        pprint(api_response)
    except ApiException as e:
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

# **resolve_instrument**
> UpsertPortfolioTransactionsResponse resolve_instrument(scope, code, instrument_identifier_type, instrument_identifier_value, from_effective_at=from_effective_at, re_resolve=re_resolve, request_body=request_body)

[EARLY ACCESS] ResolveInstrument: Resolve instrument

Try to resolve the instrument for transaction and holdings for a given instrument identifier and a specified  period of time. Also update the instrument identifiers with the given instrument identifiers collection.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-prd.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.TransactionPortfoliosApi(api_client)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
instrument_identifier_type = 'instrument_identifier_type_example' # str | The instrument identifier type.
instrument_identifier_value = 'instrument_identifier_value_example' # str | The value for the given instrument identifier.
from_effective_at = 'from_effective_at_example' # str | The lower bound effective datetime or cut label (inclusive) from which to retrieve the data.              There is no lower bound if this is not specified. (optional)
re_resolve = False # bool | When set to true, instrument resolution will be attempted for all transactions and holdings for the given identifier and date range.              When set to false (default behaviour), instrument resolution will only be attempted for those transactions and holdings that were previously unresolved. (optional) (default to False)
request_body = {"instrument/default/Figi":"BBG000C6K6G9","instrument/default/Isin":"GB00BH4HKS39"} # dict(str, str) | The dictionary with the instrument identifiers to be updated on the             transaction and holdings. (optional)

    try:
        # [EARLY ACCESS] ResolveInstrument: Resolve instrument
        api_response = api_instance.resolve_instrument(scope, code, instrument_identifier_type, instrument_identifier_value, from_effective_at=from_effective_at, re_resolve=re_resolve, request_body=request_body)
        pprint(api_response)
    except ApiException as e:
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
 **request_body** | [**dict(str, str)**](str.md)| The dictionary with the instrument identifiers to be updated on the             transaction and holdings. | [optional] 

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
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-prd.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.TransactionPortfoliosApi(api_client)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
effective_at = 'effective_at_example' # str | The effective datetime or cut label at which the holdings should be set to the provided targets.
adjust_holding_request = [{"instrumentIdentifiers":{"instrument/default/Figi":"BBG000C6K6G9","instrument/default/Isin":"GB00BH4HKS39"},"subHoldingKeys":{"transaction/Algo/Name":{"key":"Transaction/Algo/Name","value":{"labelValue":"Algo1"}}},"properties":{"holding/Entity/Name":{"key":"Holding/Entity/Name","value":{"labelValue":"Financial Entity"}}},"taxLots":[{"units":100,"cost":{"amount":10000,"currency":"GBP"},"portfolioCost":10000,"price":100,"purchaseDate":"2018-03-05T00:00:00.0000000+00:00","settlementDate":"2018-03-08T00:00:00.0000000+00:00"}],"currency":"GBP"}] # list[AdjustHoldingRequest] | The complete set of target holdings for the transaction portfolio.
reconciliation_methods = ['reconciliation_methods_example'] # list[str] | Optional parameter for specifying a reconciliation method: e.g. FxForward. (optional)

    try:
        # SetHoldings: Set holdings
        api_response = api_instance.set_holdings(scope, code, effective_at, adjust_holding_request, reconciliation_methods=reconciliation_methods)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TransactionPortfoliosApi->set_holdings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. | 
 **effective_at** | **str**| The effective datetime or cut label at which the holdings should be set to the provided targets. | 
 **adjust_holding_request** | [**list[AdjustHoldingRequest]**](AdjustHoldingRequest.md)| The complete set of target holdings for the transaction portfolio. | 
 **reconciliation_methods** | [**list[str]**](str.md)| Optional parameter for specifying a reconciliation method: e.g. FxForward. | [optional] 

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

# **upsert_portfolio_details**
> PortfolioDetails upsert_portfolio_details(scope, code, create_portfolio_details, effective_at=effective_at)

UpsertPortfolioDetails: Upsert portfolio details

Create or update certain details for a particular transaction portfolio. The details are updated if they already exist, and inserted if they do not.                Note that not all elements of a transaction portfolio definition are  modifiable once it has been created due to the potential implications for data already stored.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-prd.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.TransactionPortfoliosApi(api_client)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
code = 'code_example' # str | The code of the transaction portfolio. Together with the               scope this uniquely identifies the transaction portfolio.
create_portfolio_details = {"corporateActionSourceId":{"scope":"Sources","code":"Vendor1"}} # CreatePortfolioDetails | The details to create or update for the specified transaction portfolio.
effective_at = 'effective_at_example' # str | The effective datetime or cut label at which the updated or inserted details should become valid.               Defaults to the current LUSID system datetime if not specified. (optional)

    try:
        # UpsertPortfolioDetails: Upsert portfolio details
        api_response = api_instance.upsert_portfolio_details(scope, code, create_portfolio_details, effective_at=effective_at)
        pprint(api_response)
    except ApiException as e:
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
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-prd.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.TransactionPortfoliosApi(api_client)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
transaction_id = 'transaction_id_example' # str | The unique ID of the transaction to create or update properties for.
request_body = {"transaction/MyScope/MyPropertyName":{"key":"Transaction/MyScope/MyPropertyName","value":{"metricValue":{"value":12345.5672,"unit":"Unit"}}},"transaction/MyScope/MyPropertyName2":{"key":"Transaction/MyScope/MyPropertyName2","value":{"metricValue":{"value":925.3,"unit":"Unit"}}}} # dict(str, PerpetualProperty) | The properties and their associated values to create or update.

    try:
        # UpsertTransactionProperties: Upsert transaction properties
        api_response = api_instance.upsert_transaction_properties(scope, code, transaction_id, request_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TransactionPortfoliosApi->upsert_transaction_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. | 
 **transaction_id** | **str**| The unique ID of the transaction to create or update properties for. | 
 **request_body** | [**dict(str, PerpetualProperty)**](PerpetualProperty.md)| The properties and their associated values to create or update. | 

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
> UpsertPortfolioTransactionsResponse upsert_transactions(scope, code, transaction_request)

UpsertTransactions: Upsert transactions

Create or update transactions in the transaction portfolio. A transaction will be updated  if it already exists and created if it does not.  The maximum number of transactions that this method can upsert per request is 10,000.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-prd.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.TransactionPortfoliosApi(api_client)
    scope = 'scope_example' # str | The scope of the transaction portfolio.
code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
transaction_request = [{"transactionId":"TransactionId-111111","type":"StockIn","instrumentIdentifiers":{"instrument/default/Figi":"BBG000C6K6G9","instrument/default/Isin":"GB00BH4HKS39"},"transactionDate":"2018-03-05T00:00:00.0000000+00:00","settlementDate":"2018-03-08T00:00:00.0000000+00:00","units":1000,"transactionPrice":{"price":123,"type":"Price"},"totalConsideration":{"amount":123000,"currency":"GBP"},"transactionCurrency":"GBP","properties":{"transaction/Algo/Name":{"key":"Transaction/Algo/Name","value":{"labelValue":"Algo1"}}},"counterpartyId":"CounterpartyId-118263","source":"","otcConfirmation":{"counterpartyAgreementId":{"scope":"someScope","code":"someCode"}}}] # list[TransactionRequest] | A list of transactions to be created or updated.

    try:
        # UpsertTransactions: Upsert transactions
        api_response = api_instance.upsert_transactions(scope, code, transaction_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TransactionPortfoliosApi->upsert_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. | 
 **transaction_request** | [**list[TransactionRequest]**](TransactionRequest.md)| A list of transactions to be created or updated. | 

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

