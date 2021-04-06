# lusid.TransactionPortfoliosApi

All URIs are relative to *http://local-unit-test-server.lusid.com:62600*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adjust_holdings**](TransactionPortfoliosApi.md#adjust_holdings) | **POST** /api/transactionportfolios/{scope}/{code}/holdings | Adjust holdings
[**build_transactions**](TransactionPortfoliosApi.md#build_transactions) | **POST** /api/transactionportfolios/{scope}/{code}/transactions/$build | Build transactions
[**cancel_adjust_holdings**](TransactionPortfoliosApi.md#cancel_adjust_holdings) | **DELETE** /api/transactionportfolios/{scope}/{code}/holdings | Cancel adjust holdings
[**cancel_executions**](TransactionPortfoliosApi.md#cancel_executions) | **DELETE** /api/transactionportfolios/{scope}/{code}/executions | [EARLY ACCESS] Cancel executions
[**cancel_transactions**](TransactionPortfoliosApi.md#cancel_transactions) | **DELETE** /api/transactionportfolios/{scope}/{code}/transactions | Cancel transactions
[**create_portfolio**](TransactionPortfoliosApi.md#create_portfolio) | **POST** /api/transactionportfolios/{scope} | Create portfolio
[**delete_properties_from_transaction**](TransactionPortfoliosApi.md#delete_properties_from_transaction) | **DELETE** /api/transactionportfolios/{scope}/{code}/transactions/{transactionId}/properties | Delete properties from transaction
[**get_details**](TransactionPortfoliosApi.md#get_details) | **GET** /api/transactionportfolios/{scope}/{code}/details | Get details
[**get_holdings**](TransactionPortfoliosApi.md#get_holdings) | **GET** /api/transactionportfolios/{scope}/{code}/holdings | Get holdings
[**get_holdings_adjustment**](TransactionPortfoliosApi.md#get_holdings_adjustment) | **GET** /api/transactionportfolios/{scope}/{code}/holdingsadjustments/{effectiveAt} | Get holdings adjustment
[**get_portfolio_cash_statement**](TransactionPortfoliosApi.md#get_portfolio_cash_statement) | **GET** /api/transactionportfolios/{scope}/{code}/cashstatement | [EARLY ACCESS] Get CashStatement for the given portfolio.
[**get_transactions**](TransactionPortfoliosApi.md#get_transactions) | **GET** /api/transactionportfolios/{scope}/{code}/transactions | Get transactions
[**list_holdings_adjustments**](TransactionPortfoliosApi.md#list_holdings_adjustments) | **GET** /api/transactionportfolios/{scope}/{code}/holdingsadjustments | List holdings adjustments
[**resolve_instrument**](TransactionPortfoliosApi.md#resolve_instrument) | **POST** /api/transactionportfolios/{scope}/{code}/$resolve | [EARLY ACCESS] Resolve Instrument
[**set_holdings**](TransactionPortfoliosApi.md#set_holdings) | **PUT** /api/transactionportfolios/{scope}/{code}/holdings | Set holdings
[**upsert_executions**](TransactionPortfoliosApi.md#upsert_executions) | **POST** /api/transactionportfolios/{scope}/{code}/executions | [EARLY ACCESS] Upsert executions
[**upsert_portfolio_details**](TransactionPortfoliosApi.md#upsert_portfolio_details) | **POST** /api/transactionportfolios/{scope}/{code}/details | Upsert portfolio details
[**upsert_transaction_properties**](TransactionPortfoliosApi.md#upsert_transaction_properties) | **POST** /api/transactionportfolios/{scope}/{code}/transactions/{transactionId}/properties | Upsert transaction properties
[**upsert_transactions**](TransactionPortfoliosApi.md#upsert_transactions) | **POST** /api/transactionportfolios/{scope}/{code}/transactions | Upsert transactions


# **adjust_holdings**
> AdjustHolding adjust_holdings(scope, code, effective_at, adjust_holding_request, reconciliation_methods=reconciliation_methods)

Adjust holdings

Adjust one or more holdings of the specified transaction portfolio to the provided targets. LUSID will  automatically construct adjustment transactions to ensure that the holdings which have been adjusted are  always set to the provided targets for the specified effective datetime. Read more about the difference between  adjusting and setting holdings here https://support.lusid.com/how-do-i-adjust-my-holdings.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://local-unit-test-server.lusid.com:62600
configuration.host = "http://local-unit-test-server.lusid.com:62600"
# Create an instance of the API class
api_instance = lusid.TransactionPortfoliosApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the transaction portfolio.
code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
effective_at = 'effective_at_example' # str | The effective datetime or cut label at which the holdings should be set to the provided targets.
adjust_holding_request = [{"instrumentIdentifiers":{"instrument/default/Figi":"BBG000C6K6G9","instrument/default/Isin":"GB00BH4HKS39"},"subHoldingKeys":{"transaction/Algo/Name":{"key":"Transaction/Algo/Name","value":{"labelValue":"Algo1"}}},"properties":{"holding/Entity/Name":{"key":"Holding/Entity/Name","value":{"labelValue":"Financial Entity"}}},"taxLots":[{"units":100,"cost":{"amount":10000,"currency":"GBP"},"portfolioCost":10000,"price":100,"purchaseDate":"2018-03-05T00:00:00.0000000+00:00","settlementDate":"2018-03-08T00:00:00.0000000+00:00"}],"currency":"GBP"}] # list[AdjustHoldingRequest] | The selected set of holdings to adjust to the provided targets for the              transaction portfolio.
reconciliation_methods = ['reconciliation_methods_example'] # list[str] | Optional parameter for specifying a reconciliation method: e.g. FxForward. (optional)

try:
    # Adjust holdings
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
> VersionedResourceListOfOutputTransaction build_transactions(scope, code, transaction_query_parameters, as_at=as_at, filter=filter, property_keys=property_keys)

Build transactions

Builds and returns all transactions that affect the holdings of a portfolio over a given interval of  effective time into a set of output transactions. This includes transactions automatically generated by  LUSID such as holding adjustments.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://local-unit-test-server.lusid.com:62600
configuration.host = "http://local-unit-test-server.lusid.com:62600"
# Create an instance of the API class
api_instance = lusid.TransactionPortfoliosApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the transaction portfolio.
code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
transaction_query_parameters = {"startDate":"2018-03-05T00:00:00.0000000+00:00","endDate":"2018-03-19T00:00:00.0000000+00:00","queryMode":"TradeDate","showCancelledTransactions":false} # TransactionQueryParameters | The query queryParameters which control how the output transactions are built.
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to build the transactions. Defaults to return the latest              version of each transaction if not specified. (optional)
filter = 'filter_example' # str | Expression to filter the result set.              For example, to filter on the Transaction Type, use \"type eq 'Buy'\"              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)
property_keys = ['property_keys_example'] # list[str] | A list of property keys from the \"Instrument\" or \"Transaction\" domain to decorate onto              the transactions. These take the format {domain}/{scope}/{code} e.g. \"Instrument/system/Name\" or              \"Transaction/strategy/quantsignal\". (optional)

try:
    # Build transactions
    api_response = api_instance.build_transactions(scope, code, transaction_query_parameters, as_at=as_at, filter=filter, property_keys=property_keys)
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
 **filter** | **str**| Expression to filter the result set.              For example, to filter on the Transaction Type, use \&quot;type eq &#39;Buy&#39;\&quot;              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **property_keys** | [**list[str]**](str.md)| A list of property keys from the \&quot;Instrument\&quot; or \&quot;Transaction\&quot; domain to decorate onto              the transactions. These take the format {domain}/{scope}/{code} e.g. \&quot;Instrument/system/Name\&quot; or              \&quot;Transaction/strategy/quantsignal\&quot;. | [optional] 

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

Cancel adjust holdings

Cancel all previous holding adjustments made on the specified transaction portfolio for a specified effective  datetime. This should be used to undo holding adjustments made via set holdings or adjust holdings.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://local-unit-test-server.lusid.com:62600
configuration.host = "http://local-unit-test-server.lusid.com:62600"
# Create an instance of the API class
api_instance = lusid.TransactionPortfoliosApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the transaction portfolio.
code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
effective_at = 'effective_at_example' # str | The effective datetime or cut label at which the holding adjustments should be undone.

try:
    # Cancel adjust holdings
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

# **cancel_executions**
> DeletedEntityResponse cancel_executions(scope, code, execution_ids)

[EARLY ACCESS] Cancel executions

Cancel one or more executions which exist in a specified transaction portfolio.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://local-unit-test-server.lusid.com:62600
configuration.host = "http://local-unit-test-server.lusid.com:62600"
# Create an instance of the API class
api_instance = lusid.TransactionPortfoliosApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the transaction portfolio.
code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
execution_ids = ['execution_ids_example'] # list[str] | The ids of the executions to cancel.

try:
    # [EARLY ACCESS] Cancel executions
    api_response = api_instance.cancel_executions(scope, code, execution_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionPortfoliosApi->cancel_executions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. | 
 **execution_ids** | [**list[str]**](str.md)| The ids of the executions to cancel. | 

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
**200** | The datetime that the executions were cancelled |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_transactions**
> DeletedEntityResponse cancel_transactions(scope, code, transaction_ids)

Cancel transactions

Cancel one or more transactions from the specified transaction portfolio.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://local-unit-test-server.lusid.com:62600
configuration.host = "http://local-unit-test-server.lusid.com:62600"
# Create an instance of the API class
api_instance = lusid.TransactionPortfoliosApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the transaction portfolio.
code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
transaction_ids = ['transaction_ids_example'] # list[str] | The ids of the transactions to cancel.

try:
    # Cancel transactions
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
 **transaction_ids** | [**list[str]**](str.md)| The ids of the transactions to cancel. | 

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

Create portfolio

Create a transaction portfolio in a specific scope.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://local-unit-test-server.lusid.com:62600
configuration.host = "http://local-unit-test-server.lusid.com:62600"
# Create an instance of the API class
api_instance = lusid.TransactionPortfoliosApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope that the transaction portfolio will be created in.
create_transaction_portfolio_request = {"displayName":"Portfolio UK","description":"Portfolio for UK market","code":"PortfolioUk","created":"2018-03-05T12:00:00.0000000+00:00","baseCurrency":"GBP","corporateActionSourceId":{"scope":"Sources","code":"Vendor1"},"accountingMethod":"Default","subHoldingKeys":[],"properties":{"portfolio/Manager/Name":{"key":"Portfolio/Manager/Name","value":{"labelValue":"Matt Smith"},"effectiveFrom":"2018-03-05T12:00:00.0000000+00:00"},"portfolio/Manager/Id":{"key":"Portfolio/Manager/Id","value":{"metricValue":{"value":1628483,"unit":"NoUnits"}},"effectiveFrom":"2018-03-05T12:00:00.0000000+00:00"}}} # CreateTransactionPortfolioRequest | The definition and details of the transaction portfolio.

try:
    # Create portfolio
    api_response = api_instance.create_portfolio(scope, create_transaction_portfolio_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionPortfoliosApi->create_portfolio: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that the transaction portfolio will be created in. | 
 **create_transaction_portfolio_request** | [**CreateTransactionPortfolioRequest**](CreateTransactionPortfolioRequest.md)| The definition and details of the transaction portfolio. | 

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
**201** | The newly created transaction portfolio |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_properties_from_transaction**
> DeletedEntityResponse delete_properties_from_transaction(scope, code, transaction_id, property_keys)

Delete properties from transaction

Delete one or more property values from a single transaction in a transaction portfolio.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://local-unit-test-server.lusid.com:62600
configuration.host = "http://local-unit-test-server.lusid.com:62600"
# Create an instance of the API class
api_instance = lusid.TransactionPortfoliosApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the transaction portfolio.
code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
transaction_id = 'transaction_id_example' # str | The unique id of the transaction to delete the property value from.
property_keys = ['property_keys_example'] # list[str] | The property keys of the properties to delete from the transaction.              This must be from the \"Transaction\" domain and will have the format {domain}/{scope}/{code} e.g.              \"Transaction/strategy/quantsignal\".

try:
    # Delete properties from transaction
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
 **transaction_id** | **str**| The unique id of the transaction to delete the property value from. | 
 **property_keys** | [**list[str]**](str.md)| The property keys of the properties to delete from the transaction.              This must be from the \&quot;Transaction\&quot; domain and will have the format {domain}/{scope}/{code} e.g.              \&quot;Transaction/strategy/quantsignal\&quot;. | 

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

# **get_details**
> PortfolioDetails get_details(scope, code, effective_at=effective_at, as_at=as_at)

Get details

Get the details associated with a transaction portfolio.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://local-unit-test-server.lusid.com:62600
configuration.host = "http://local-unit-test-server.lusid.com:62600"
# Create an instance of the API class
api_instance = lusid.TransactionPortfoliosApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the transaction portfolio to retrieve the details for.
code = 'code_example' # str | The code of the transaction portfolio to retrieve the details for. Together with the              scope this uniquely identifies the transaction portfolio.
effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve the details of the transaction              portfolio. Defaults to the current LUSID system datetime if not specified. (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the details of the transaction portfolio. Defaults              to return the latest version of the details if not specified. (optional)

try:
    # Get details
    api_response = api_instance.get_details(scope, code, effective_at=effective_at, as_at=as_at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionPortfoliosApi->get_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio to retrieve the details for. | 
 **code** | **str**| The code of the transaction portfolio to retrieve the details for. Together with the              scope this uniquely identifies the transaction portfolio. | 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the details of the transaction              portfolio. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the details of the transaction portfolio. Defaults              to return the latest version of the details if not specified. | [optional] 

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

Get holdings

Get the holdings of the specified transaction portfolio.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://local-unit-test-server.lusid.com:62600
configuration.host = "http://local-unit-test-server.lusid.com:62600"
# Create an instance of the API class
api_instance = lusid.TransactionPortfoliosApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the transaction portfolio.
code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve the holdings of the transaction              portfolio. Defaults to the current LUSID system datetime if not specified. (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the holdings of the transaction portfolio. Defaults              to return the latest version of the holdings if not specified. (optional)
filter = 'filter_example' # str | Expression to filter the result set.               For example, to filter on the Holding Type, use \"holdingType eq 'p'\"              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)
property_keys = ['property_keys_example'] # list[str] | A list of property keys from the \"Instrument\" or \"Holding\" domain to decorate onto              the holdings. These take the format {domain}/{scope}/{code} e.g. \"Instrument/system/Name\" or \"Holding/system/Cost\". (optional)
by_taxlots = True # bool | Whether or not to expand the holdings to return the underlying tax-lots. Defaults to              False. (optional)

try:
    # Get holdings
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
 **as_at** | **datetime**| The asAt datetime at which to retrieve the holdings of the transaction portfolio. Defaults              to return the latest version of the holdings if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set.               For example, to filter on the Holding Type, use \&quot;holdingType eq &#39;p&#39;\&quot;              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **property_keys** | [**list[str]**](str.md)| A list of property keys from the \&quot;Instrument\&quot; or \&quot;Holding\&quot; domain to decorate onto              the holdings. These take the format {domain}/{scope}/{code} e.g. \&quot;Instrument/system/Name\&quot; or \&quot;Holding/system/Cost\&quot;. | [optional] 
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
> HoldingsAdjustment get_holdings_adjustment(scope, code, effective_at, as_at=as_at)

Get holdings adjustment

Get a holdings adjustment made to a transaction portfolio at a specific effective datetime. Note that a  holdings adjustment will only be returned if one exists for the specified effective datetime.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://local-unit-test-server.lusid.com:62600
configuration.host = "http://local-unit-test-server.lusid.com:62600"
# Create an instance of the API class
api_instance = lusid.TransactionPortfoliosApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the transaction portfolio.
code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
effective_at = 'effective_at_example' # str | The effective datetime or cut label of the holdings adjustment.
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the holdings adjustment. Defaults to the return the latest              version of the holdings adjustment if not specified. (optional)

try:
    # Get holdings adjustment
    api_response = api_instance.get_holdings_adjustment(scope, code, effective_at, as_at=as_at)
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

# **get_portfolio_cash_statement**
> ResourceListOfPortfolioCashFlow get_portfolio_cash_statement(scope, code, from_effective_at, to_effective_at, as_at=as_at, filter=filter, recipe_id_scope=recipe_id_scope, recipe_id_code=recipe_id_code)

[EARLY ACCESS] Get CashStatement for the given portfolio.

Get CashStatement for the given portfolio.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://local-unit-test-server.lusid.com:62600
configuration.host = "http://local-unit-test-server.lusid.com:62600"
# Create an instance of the API class
api_instance = lusid.TransactionPortfoliosApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the portfolio to retrieve the CashStatement for.
code = 'code_example' # str | The code of the portfolio to retrieve the CashStatement for. Together with the scope this              uniquely identifies the portfolio.
from_effective_at = 'from_effective_at_example' # str | The lower bound effective datetime or cut label (inclusive) from which to retrieve the data.              There is no lower bound if this is not specified.
to_effective_at = 'to_effective_at_example' # str | The upper bound effective datetime or cut label (inclusive) from which to retrieve the data.              There is no upper bound if this is not specified.
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the portfolio. Defaults to return the latest version              of each transaction if not specified. (optional)
filter = 'filter_example' # str | Expression to filter the result set.               For example, to filter on the Transaction Type, use \"type eq 'Buy'\"              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)
recipe_id_scope = 'recipe_id_scope_example' # str | The scope of the given recipeId (optional)
recipe_id_code = 'recipe_id_code_example' # str | The code of the given recipeID (optional)

try:
    # [EARLY ACCESS] Get CashStatement for the given portfolio.
    api_response = api_instance.get_portfolio_cash_statement(scope, code, from_effective_at, to_effective_at, as_at=as_at, filter=filter, recipe_id_scope=recipe_id_scope, recipe_id_code=recipe_id_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionPortfoliosApi->get_portfolio_cash_statement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio to retrieve the CashStatement for. | 
 **code** | **str**| The code of the portfolio to retrieve the CashStatement for. Together with the scope this              uniquely identifies the portfolio. | 
 **from_effective_at** | **str**| The lower bound effective datetime or cut label (inclusive) from which to retrieve the data.              There is no lower bound if this is not specified. | 
 **to_effective_at** | **str**| The upper bound effective datetime or cut label (inclusive) from which to retrieve the data.              There is no upper bound if this is not specified. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the portfolio. Defaults to return the latest version              of each transaction if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set.               For example, to filter on the Transaction Type, use \&quot;type eq &#39;Buy&#39;\&quot;              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
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

# **get_transactions**
> VersionedResourceListOfTransaction get_transactions(scope, code, from_transaction_date=from_transaction_date, to_transaction_date=to_transaction_date, as_at=as_at, filter=filter, property_keys=property_keys)

Get transactions

Get transactions from the specified transaction portfolio over a given interval of effective time.     When the specified portfolio is a derived transaction portfolio, the returned set of transactions is the  union set of all transactions of the parent (and any grandparents etc.) and the specified derived transaction portfolio itself.  The maximum number of transactions that this method can get per request is 2,000.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://local-unit-test-server.lusid.com:62600
configuration.host = "http://local-unit-test-server.lusid.com:62600"
# Create an instance of the API class
api_instance = lusid.TransactionPortfoliosApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the transaction portfolio.
code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
from_transaction_date = 'from_transaction_date_example' # str | The lower bound effective datetime or cut label (inclusive) from which to retrieve the transactions.              There is no lower bound if this is not specified. (optional)
to_transaction_date = 'to_transaction_date_example' # str | The upper bound effective datetime or cut label (inclusive) from which to retrieve transactions.              There is no upper bound if this is not specified. (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the transactions. Defaults to return the latest version              of each transaction if not specified. (optional)
filter = 'filter_example' # str | Expression to filter the result set.               For example, to filter on the Transaction Type, use \"type eq 'Buy'\"              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)
property_keys = ['property_keys_example'] # list[str] | A list of property keys from the \"Instrument\" or \"Transaction\" domain to decorate onto              the transactions. These take the format {domain}/{scope}/{code} e.g. \"Instrument/system/Name\" or              \"Transaction/strategy/quantsignal\". (optional)

try:
    # Get transactions
    api_response = api_instance.get_transactions(scope, code, from_transaction_date=from_transaction_date, to_transaction_date=to_transaction_date, as_at=as_at, filter=filter, property_keys=property_keys)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionPortfoliosApi->get_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. | 
 **from_transaction_date** | **str**| The lower bound effective datetime or cut label (inclusive) from which to retrieve the transactions.              There is no lower bound if this is not specified. | [optional] 
 **to_transaction_date** | **str**| The upper bound effective datetime or cut label (inclusive) from which to retrieve transactions.              There is no upper bound if this is not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the transactions. Defaults to return the latest version              of each transaction if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set.               For example, to filter on the Transaction Type, use \&quot;type eq &#39;Buy&#39;\&quot;              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **property_keys** | [**list[str]**](str.md)| A list of property keys from the \&quot;Instrument\&quot; or \&quot;Transaction\&quot; domain to decorate onto              the transactions. These take the format {domain}/{scope}/{code} e.g. \&quot;Instrument/system/Name\&quot; or              \&quot;Transaction/strategy/quantsignal\&quot;. | [optional] 

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

List holdings adjustments

List the holdings adjustments made to the specified transaction portfolio over a specified interval of effective time.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://local-unit-test-server.lusid.com:62600
configuration.host = "http://local-unit-test-server.lusid.com:62600"
# Create an instance of the API class
api_instance = lusid.TransactionPortfoliosApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the transaction portfolio.
code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
from_effective_at = 'from_effective_at_example' # str | The lower bound effective datetime or cut label (inclusive) from which to retrieve the holdings              adjustments. There is no lower bound if this is not specified. (optional)
to_effective_at = 'to_effective_at_example' # str | The upper bound effective datetime or cut label (inclusive) from which to retrieve the holdings              adjustments. There is no upper bound if this is not specified. (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the holdings adjustments. Defaults to return the              latest version of each holding adjustment if not specified. (optional)

try:
    # List holdings adjustments
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
> UpsertPortfolioTransactionsResponse resolve_instrument(scope, code, instrument_identifier_type, instrument_identifier_value, from_effective_at=from_effective_at, request_body=request_body)

[EARLY ACCESS] Resolve Instrument

Try to resolve the instrument for transaction and holdings for a given instrument identifier and a specified    period of time. Also update the instrument identifiers with the given instrument identifiers collection.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://local-unit-test-server.lusid.com:62600
configuration.host = "http://local-unit-test-server.lusid.com:62600"
# Create an instance of the API class
api_instance = lusid.TransactionPortfoliosApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the transaction portfolio.
code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
instrument_identifier_type = 'instrument_identifier_type_example' # str | The instrument identifier type.
instrument_identifier_value = 'instrument_identifier_value_example' # str | The value for the given instrument identifier.
from_effective_at = 'from_effective_at_example' # str | The lower bound effective datetime or cut label (inclusive) from which to retrieve the data.              There is no lower bound if this is not specified. (optional)
request_body = {"instrument/default/Figi":"BBG000C6K6G9","instrument/default/Isin":"GB00BH4HKS39"} # dict(str, str) | The dictionary with the instrument identifiers to be updated on the              transaction and holdings. (optional)

try:
    # [EARLY ACCESS] Resolve Instrument
    api_response = api_instance.resolve_instrument(scope, code, instrument_identifier_type, instrument_identifier_value, from_effective_at=from_effective_at, request_body=request_body)
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
 **request_body** | [**dict(str, str)**](str.md)| The dictionary with the instrument identifiers to be updated on the              transaction and holdings. | [optional] 

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

Set holdings

Set the holdings of the specified transaction portfolio to the provided targets. LUSID will automatically  construct adjustment transactions to ensure that the entire set of holdings for the transaction portfolio  are always set to the provided targets for the specified effective datetime. Read more about the difference between  adjusting and setting holdings here https://support.lusid.com/how-do-i-adjust-my-holdings.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://local-unit-test-server.lusid.com:62600
configuration.host = "http://local-unit-test-server.lusid.com:62600"
# Create an instance of the API class
api_instance = lusid.TransactionPortfoliosApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the transaction portfolio.
code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
effective_at = 'effective_at_example' # str | The effective datetime or cut label at which the holdings should be set to the provided targets.
adjust_holding_request = [{"instrumentIdentifiers":{"instrument/default/Figi":"BBG000C6K6G9","instrument/default/Isin":"GB00BH4HKS39"},"subHoldingKeys":{"transaction/Algo/Name":{"key":"Transaction/Algo/Name","value":{"labelValue":"Algo1"}}},"properties":{"holding/Entity/Name":{"key":"Holding/Entity/Name","value":{"labelValue":"Financial Entity"}}},"taxLots":[{"units":100,"cost":{"amount":10000,"currency":"GBP"},"portfolioCost":10000,"price":100,"purchaseDate":"2018-03-05T00:00:00.0000000+00:00","settlementDate":"2018-03-08T00:00:00.0000000+00:00"}],"currency":"GBP"}] # list[AdjustHoldingRequest] | The complete set of target holdings for the transaction portfolio.
reconciliation_methods = ['reconciliation_methods_example'] # list[str] | Optional parameter for specifying a reconciliation method: e.g. FxForward. (optional)

try:
    # Set holdings
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

# **upsert_executions**
> UpsertPortfolioExecutionsResponse upsert_executions(scope, code, execution_request=execution_request)

[EARLY ACCESS] Upsert executions

Update or insert executions into the specified transaction portfolio. An execution will be updated  if it already exists and inserted if it does not.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://local-unit-test-server.lusid.com:62600
configuration.host = "http://local-unit-test-server.lusid.com:62600"
# Create an instance of the API class
api_instance = lusid.TransactionPortfoliosApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the transaction portfolio.
code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
execution_request = [{"executionId":"ExecutionId-11111","side":"SellShort","instrumentIdentifiers":{"clientInternal":"CLI-183461"},"transactionTime":"2018-03-05T12:00:00.0000000+00:00","lastShares":1000,"lastPx":1.23,"currency":"USD"}] # list[ExecutionRequest] | The executions to update or insert. (optional)

try:
    # [EARLY ACCESS] Upsert executions
    api_response = api_instance.upsert_executions(scope, code, execution_request=execution_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionPortfoliosApi->upsert_executions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. | 
 **execution_request** | [**list[ExecutionRequest]**](ExecutionRequest.md)| The executions to update or insert. | [optional] 

### Return type

[**UpsertPortfolioExecutionsResponse**](UpsertPortfolioExecutionsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The version of the transaction portfolio that contains the newly updated or inserted executions |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_portfolio_details**
> PortfolioDetails upsert_portfolio_details(scope, code, create_portfolio_details, effective_at=effective_at)

Upsert portfolio details

Update or insert details for the specified transaction portfolio. The details will be updated  if they already exist and inserted if they do not.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://local-unit-test-server.lusid.com:62600
configuration.host = "http://local-unit-test-server.lusid.com:62600"
# Create an instance of the API class
api_instance = lusid.TransactionPortfoliosApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the transaction portfolio to update or insert details for.
code = 'code_example' # str | The code of the transaction portfolio to update or insert details for. Together with the              scope this uniquely identifies the transaction portfolio.
create_portfolio_details = {"corporateActionSourceId":{"scope":"Sources","code":"Vendor1"}} # CreatePortfolioDetails | The details to update or insert for the specified transaction portfolio.
effective_at = 'effective_at_example' # str | The effective datetime or cut label at which the updated or inserted details should become valid.              Defaults to the current LUSID system datetime if not specified. (optional)

try:
    # Upsert portfolio details
    api_response = api_instance.upsert_portfolio_details(scope, code, create_portfolio_details, effective_at=effective_at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionPortfoliosApi->upsert_portfolio_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio to update or insert details for. | 
 **code** | **str**| The code of the transaction portfolio to update or insert details for. Together with the              scope this uniquely identifies the transaction portfolio. | 
 **create_portfolio_details** | [**CreatePortfolioDetails**](CreatePortfolioDetails.md)| The details to update or insert for the specified transaction portfolio. | 
 **effective_at** | **str**| The effective datetime or cut label at which the updated or inserted details should become valid.              Defaults to the current LUSID system datetime if not specified. | [optional] 

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

Upsert transaction properties

Update or insert one or more transaction properties to a single transaction in a transaction portfolio.  Each property will be updated if it already exists and inserted if it does not.  Both transaction and portfolio must exist at the time when properties are updated or inserted.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://local-unit-test-server.lusid.com:62600
configuration.host = "http://local-unit-test-server.lusid.com:62600"
# Create an instance of the API class
api_instance = lusid.TransactionPortfoliosApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the transaction portfolio.
code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
transaction_id = 'transaction_id_example' # str | The unique id of the transaction to update or insert properties against.
request_body = {"transaction/MyScope/MyPropertyName":{"key":"Transaction/MyScope/MyPropertyName","value":{"metricValue":{"value":12345.5672,"unit":"Unit"}}},"transaction/MyScope/MyPropertyName2":{"key":"Transaction/MyScope/MyPropertyName2","value":{"metricValue":{"value":925.3,"unit":"Unit"}}}} # dict(str, PerpetualProperty) | The properties with their associated values to update or insert onto the              transaction.

try:
    # Upsert transaction properties
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
 **transaction_id** | **str**| The unique id of the transaction to update or insert properties against. | 
 **request_body** | [**dict(str, PerpetualProperty)**](PerpetualProperty.md)| The properties with their associated values to update or insert onto the              transaction. | 

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

Upsert transactions

Update or insert transactions into the specified transaction portfolio. A transaction will be updated  if it already exists and inserted if it does not.  The maximum number of transactions that this method can upsert per request is 10,000.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://local-unit-test-server.lusid.com:62600
configuration.host = "http://local-unit-test-server.lusid.com:62600"
# Create an instance of the API class
api_instance = lusid.TransactionPortfoliosApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the transaction portfolio.
code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
transaction_request = [{"transactionId":"TransactionId-111111","type":"StockIn","instrumentIdentifiers":{"instrument/default/Figi":"BBG000C6K6G9","instrument/default/Isin":"GB00BH4HKS39"},"transactionDate":"2018-03-05T00:00:00.0000000+00:00","settlementDate":"2018-03-08T00:00:00.0000000+00:00","units":1000,"transactionPrice":{"price":123,"type":"Price"},"totalConsideration":{"amount":123000,"currency":"GBP"},"transactionCurrency":"GBP","properties":{"transaction/Algo/Name":{"key":"Transaction/Algo/Name","value":{"labelValue":"Algo1"}}},"counterpartyId":"CounterpartyId-118263","source":""}] # list[TransactionRequest] | The transactions to be updated or inserted.

try:
    # Upsert transactions
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
 **transaction_request** | [**list[TransactionRequest]**](TransactionRequest.md)| The transactions to be updated or inserted. | 

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

