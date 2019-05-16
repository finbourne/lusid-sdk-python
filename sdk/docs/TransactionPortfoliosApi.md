# lusid.TransactionPortfoliosApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_transaction_property**](TransactionPortfoliosApi.md#add_transaction_property) | **POST** /api/transactionportfolios/{scope}/{code}/transactions/{transactionId}/properties | Add transaction properties
[**adjust_holdings**](TransactionPortfoliosApi.md#adjust_holdings) | **POST** /api/transactionportfolios/{scope}/{code}/holdings/{effectiveAt} | Adjust holdings
[**build_transactions**](TransactionPortfoliosApi.md#build_transactions) | **POST** /api/transactionportfolios/{scope}/{code}/transactions/$build | Build output transactions
[**cancel_adjust_holdings**](TransactionPortfoliosApi.md#cancel_adjust_holdings) | **DELETE** /api/transactionportfolios/{scope}/{code}/holdings/{effectiveAt} | Cancel holdings adjustments
[**create_portfolio**](TransactionPortfoliosApi.md#create_portfolio) | **POST** /api/transactionportfolios/{scope} | Create transaction portfolio
[**delete_executions**](TransactionPortfoliosApi.md#delete_executions) | **DELETE** /api/transactionportfolios/{scope}/{code}/executions | Delete executions
[**delete_property_from_transaction**](TransactionPortfoliosApi.md#delete_property_from_transaction) | **DELETE** /api/transactionportfolios/{scope}/{code}/transactions/{transactionId}/properties | Delete transaction property
[**delete_transactions**](TransactionPortfoliosApi.md#delete_transactions) | **DELETE** /api/transactionportfolios/{scope}/{code}/transactions | Delete transactions
[**get_details**](TransactionPortfoliosApi.md#get_details) | **GET** /api/transactionportfolios/{scope}/{code}/details | Get portfolio details
[**get_holdings**](TransactionPortfoliosApi.md#get_holdings) | **GET** /api/transactionportfolios/{scope}/{code}/holdings | Get holdings
[**get_holdings_adjustment**](TransactionPortfoliosApi.md#get_holdings_adjustment) | **GET** /api/transactionportfolios/{scope}/{code}/holdingsadjustments/{effectiveAt} | Get holding adjustment
[**get_transactions**](TransactionPortfoliosApi.md#get_transactions) | **GET** /api/transactionportfolios/{scope}/{code}/transactions | Get transactions
[**list_holdings_adjustments**](TransactionPortfoliosApi.md#list_holdings_adjustments) | **GET** /api/transactionportfolios/{scope}/{code}/holdingsadjustments | List holdings adjustments
[**set_holdings**](TransactionPortfoliosApi.md#set_holdings) | **PUT** /api/transactionportfolios/{scope}/{code}/holdings/{effectiveAt} | Set all holdings on a transaction portfolio
[**upsert_executions**](TransactionPortfoliosApi.md#upsert_executions) | **POST** /api/transactionportfolios/{scope}/{code}/executions | Upsert executions
[**upsert_portfolio_details**](TransactionPortfoliosApi.md#upsert_portfolio_details) | **POST** /api/transactionportfolios/{scope}/{code}/details | Upsert details
[**upsert_transactions**](TransactionPortfoliosApi.md#upsert_transactions) | **POST** /api/transactionportfolios/{scope}/{code}/transactions | Upsert transactions into the specified transaction portfolio


# **add_transaction_property**
> AddTransactionPropertyResponse add_transaction_property(scope, code, transaction_id, transaction_properties=transaction_properties)

Add transaction properties

Upsert one or more transaction properties to a single transaction in a portfolio

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

# create an instance of the API class
api_instance = lusid.TransactionPortfoliosApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the portfolio
code = 'code_example' # str | The code of the portfolio
transaction_id = 'transaction_id_example' # str | Id of transaction
transaction_properties = {'key': lusid.PerpetualPropertyValue()} # dict(str, PerpetualPropertyValue) | Transaction properties values (optional)

try:
    # Add transaction properties
    api_response = api_instance.add_transaction_property(scope, code, transaction_id, transaction_properties=transaction_properties)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionPortfoliosApi->add_transaction_property: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio | 
 **code** | **str**| The code of the portfolio | 
 **transaction_id** | **str**| Id of transaction | 
 **transaction_properties** | [**dict(str, PerpetualPropertyValue)**](PerpetualPropertyValue.md)| Transaction properties values | [optional] 

### Return type

[**AddTransactionPropertyResponse**](AddTransactionPropertyResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **adjust_holdings**
> AdjustHolding adjust_holdings(scope, code, effective_at, holding_adjustments=holding_adjustments)

Adjust holdings

Adjust one or more holdings in a transaction portfolio    Prompt the creation of transactions in a specific transaction portfolio to bring selected holdings to the specified targets

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

# create an instance of the API class
api_instance = lusid.TransactionPortfoliosApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the portfolio
code = 'code_example' # str | The code of the portfolio
effective_at = '2013-10-20T19:20:30+01:00' # datetime | The effective date of the change
holding_adjustments = NULL # list[AdjustHoldingRequest] | The selected set of holdings adjustments (optional)

try:
    # Adjust holdings
    api_response = api_instance.adjust_holdings(scope, code, effective_at, holding_adjustments=holding_adjustments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionPortfoliosApi->adjust_holdings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio | 
 **code** | **str**| The code of the portfolio | 
 **effective_at** | **datetime**| The effective date of the change | 
 **holding_adjustments** | [**list[AdjustHoldingRequest]**](list.md)| The selected set of holdings adjustments | [optional] 

### Return type

[**AdjustHolding**](AdjustHolding.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **build_transactions**
> VersionedResourceListOfOutputTransaction build_transactions(scope, code, as_at=as_at, sort_by=sort_by, start=start, limit=limit, property_keys=property_keys, filter=filter, parameters=parameters)

Build output transactions

Builds and returns the collection of all types of transactions that affect the holdings of a portfolio in to a set of output transactions

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

# create an instance of the API class
api_instance = lusid.TransactionPortfoliosApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the portfolio
code = 'code_example' # str | The code of the portfolio
as_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The AsAt date of the data (optional)
sort_by = ['sort_by_example'] # list[str] | Optional. Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName (optional)
start = 56 # int | Optional. When paginating, skip this number of results (optional)
limit = 56 # int | Optional. When paginating, limit the number of returned results to this many. (optional)
property_keys = ['property_keys_example'] # list[str] | Optional. Keys for the transaction or instrument property values that will be decorated onto the transactions. No properties will be decorated if none are specified. (optional)
filter = 'filter_example' # str | Optional. Expression to filter the result set (optional)
parameters = lusid.TransactionQueryParameters() # TransactionQueryParameters | Optional. Transaction query parameters (optional)

try:
    # Build output transactions
    api_response = api_instance.build_transactions(scope, code, as_at=as_at, sort_by=sort_by, start=start, limit=limit, property_keys=property_keys, filter=filter, parameters=parameters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionPortfoliosApi->build_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio | 
 **code** | **str**| The code of the portfolio | 
 **as_at** | **datetime**| Optional. The AsAt date of the data | [optional] 
 **sort_by** | [**list[str]**](str.md)| Optional. Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName | [optional] 
 **start** | **int**| Optional. When paginating, skip this number of results | [optional] 
 **limit** | **int**| Optional. When paginating, limit the number of returned results to this many. | [optional] 
 **property_keys** | [**list[str]**](str.md)| Optional. Keys for the transaction or instrument property values that will be decorated onto the transactions. No properties will be decorated if none are specified. | [optional] 
 **filter** | **str**| Optional. Expression to filter the result set | [optional] 
 **parameters** | [**TransactionQueryParameters**](TransactionQueryParameters.md)| Optional. Transaction query parameters | [optional] 

### Return type

[**VersionedResourceListOfOutputTransaction**](VersionedResourceListOfOutputTransaction.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_adjust_holdings**
> DeletedEntityResponse cancel_adjust_holdings(scope, code, effective_at)

Cancel holdings adjustments

Cancel previous adjust-holdings for the portfolio for a specific date

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

# create an instance of the API class
api_instance = lusid.TransactionPortfoliosApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the portfolio
code = 'code_example' # str | The code of the portfolio
effective_at = '2013-10-20T19:20:30+01:00' # datetime | The effective date of the change

try:
    # Cancel holdings adjustments
    api_response = api_instance.cancel_adjust_holdings(scope, code, effective_at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionPortfoliosApi->cancel_adjust_holdings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio | 
 **code** | **str**| The code of the portfolio | 
 **effective_at** | **datetime**| The effective date of the change | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_portfolio**
> Portfolio create_portfolio(scope, create_request=create_request)

Create transaction portfolio

Create a transaction portfolio in a specific scope

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

# create an instance of the API class
api_instance = lusid.TransactionPortfoliosApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope into which the transaction portfolio will be created
create_request = lusid.CreateTransactionPortfolioRequest() # CreateTransactionPortfolioRequest | The transaction portfolio definition (optional)

try:
    # Create transaction portfolio
    api_response = api_instance.create_portfolio(scope, create_request=create_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionPortfoliosApi->create_portfolio: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope into which the transaction portfolio will be created | 
 **create_request** | [**CreateTransactionPortfolioRequest**](CreateTransactionPortfolioRequest.md)| The transaction portfolio definition | [optional] 

### Return type

[**Portfolio**](Portfolio.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_executions**
> DeletedEntityResponse delete_executions(scope, code, execution_ids=execution_ids)

Delete executions

Delete one or more executions from a transaction portfolio

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

# create an instance of the API class
api_instance = lusid.TransactionPortfoliosApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the portfolio
code = 'code_example' # str | The code of the portfolio
execution_ids = ['execution_ids_example'] # list[str] | Ids of executions to delete (optional)

try:
    # Delete executions
    api_response = api_instance.delete_executions(scope, code, execution_ids=execution_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionPortfoliosApi->delete_executions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio | 
 **code** | **str**| The code of the portfolio | 
 **execution_ids** | [**list[str]**](str.md)| Ids of executions to delete | [optional] 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_property_from_transaction**
> DeletedEntityResponse delete_property_from_transaction(scope, code, transaction_id, transaction_property_key=transaction_property_key)

Delete transaction property

Delete a property value from a single transaction in a portfolio

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

# create an instance of the API class
api_instance = lusid.TransactionPortfoliosApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the portfolio
code = 'code_example' # str | Code for the portfolio
transaction_id = 'transaction_id_example' # str | Id of the transaction to delete the property from
transaction_property_key = 'transaction_property_key_example' # str | The key of the property to be deleted (optional)

try:
    # Delete transaction property
    api_response = api_instance.delete_property_from_transaction(scope, code, transaction_id, transaction_property_key=transaction_property_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionPortfoliosApi->delete_property_from_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio | 
 **code** | **str**| Code for the portfolio | 
 **transaction_id** | **str**| Id of the transaction to delete the property from | 
 **transaction_property_key** | **str**| The key of the property to be deleted | [optional] 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_transactions**
> DeletedEntityResponse delete_transactions(scope, code, transaction_ids=transaction_ids)

Delete transactions

Delete one or more transactions from a transaction portfolio

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

# create an instance of the API class
api_instance = lusid.TransactionPortfoliosApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the portfolio
code = 'code_example' # str | The code of the portfolio
transaction_ids = ['transaction_ids_example'] # list[str] | Ids of transactions to delete (optional)

try:
    # Delete transactions
    api_response = api_instance.delete_transactions(scope, code, transaction_ids=transaction_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionPortfoliosApi->delete_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio | 
 **code** | **str**| The code of the portfolio | 
 **transaction_ids** | [**list[str]**](str.md)| Ids of transactions to delete | [optional] 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_details**
> PortfolioDetails get_details(scope, code, effective_at=effective_at, as_at=as_at)

Get portfolio details

Get the details document associated with a transaction portfolio                When requesting details from a derived transaction portfolio, the returned set of details could come from a different transaction portfolio

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

# create an instance of the API class
api_instance = lusid.TransactionPortfoliosApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the portfolio
code = 'code_example' # str | The code of the portfolio
effective_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The effective date of the data (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The AsAt date of the data (optional)

try:
    # Get portfolio details
    api_response = api_instance.get_details(scope, code, effective_at=effective_at, as_at=as_at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionPortfoliosApi->get_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio | 
 **code** | **str**| The code of the portfolio | 
 **effective_at** | **datetime**| Optional. The effective date of the data | [optional] 
 **as_at** | **datetime**| Optional. The AsAt date of the data | [optional] 

### Return type

[**PortfolioDetails**](PortfolioDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_holdings**
> VersionedResourceListOfPortfolioHolding get_holdings(scope, code, by_taxlots=by_taxlots, effective_at=effective_at, as_at=as_at, sort_by=sort_by, start=start, limit=limit, filter=filter, property_keys=property_keys)

Get holdings

Get the aggregate holdings of a transaction portfolio.  If no effectiveAt or asAt  are supplied then values will be defaulted to the latest system time.

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

# create an instance of the API class
api_instance = lusid.TransactionPortfoliosApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the portfolio
code = 'code_example' # str | The code of the portfolio
by_taxlots = True # bool | Option to expand holdings to return the underlying tax-lots (optional)
effective_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The effective date of the portfolio (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The AsAt date of the data (optional)
sort_by = ['sort_by_example'] # list[str] | Optional. Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName (optional)
start = 56 # int | Optional. When paginating, skip this number of results (optional)
limit = 56 # int | Optional. When paginating, limit the number of returned results to this many. (optional)
filter = 'filter_example' # str | Optional. Expression to filter the result set (optional)
property_keys = ['property_keys_example'] # list[str] | Optional. Keys for the Holding or instrument property values that will be decorated onto the transactions. No properties will be decorated if none are specified. (optional)

try:
    # Get holdings
    api_response = api_instance.get_holdings(scope, code, by_taxlots=by_taxlots, effective_at=effective_at, as_at=as_at, sort_by=sort_by, start=start, limit=limit, filter=filter, property_keys=property_keys)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionPortfoliosApi->get_holdings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio | 
 **code** | **str**| The code of the portfolio | 
 **by_taxlots** | **bool**| Option to expand holdings to return the underlying tax-lots | [optional] 
 **effective_at** | **datetime**| Optional. The effective date of the portfolio | [optional] 
 **as_at** | **datetime**| Optional. The AsAt date of the data | [optional] 
 **sort_by** | [**list[str]**](str.md)| Optional. Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName | [optional] 
 **start** | **int**| Optional. When paginating, skip this number of results | [optional] 
 **limit** | **int**| Optional. When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Optional. Expression to filter the result set | [optional] 
 **property_keys** | [**list[str]**](str.md)| Optional. Keys for the Holding or instrument property values that will be decorated onto the transactions. No properties will be decorated if none are specified. | [optional] 

### Return type

[**VersionedResourceListOfPortfolioHolding**](VersionedResourceListOfPortfolioHolding.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_holdings_adjustment**
> HoldingsAdjustment get_holdings_adjustment(scope, code, effective_at, as_at=as_at)

Get holding adjustment

Get a holdings adjustment for a transaction portfolio at a specific effective time.    A holdings adjustment definition will only be returned if one exists for the specified effective time

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

# create an instance of the API class
api_instance = lusid.TransactionPortfoliosApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the portfolio
code = 'code_example' # str | The code of the portfolio
effective_at = '2013-10-20T19:20:30+01:00' # datetime | The effective time of the holdings adjustment
as_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The AsAt date of the data (optional)

try:
    # Get holding adjustment
    api_response = api_instance.get_holdings_adjustment(scope, code, effective_at, as_at=as_at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionPortfoliosApi->get_holdings_adjustment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio | 
 **code** | **str**| The code of the portfolio | 
 **effective_at** | **datetime**| The effective time of the holdings adjustment | 
 **as_at** | **datetime**| Optional. The AsAt date of the data | [optional] 

### Return type

[**HoldingsAdjustment**](HoldingsAdjustment.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transactions**
> VersionedResourceListOfTransaction get_transactions(scope, code, from_transaction_date=from_transaction_date, to_transaction_date=to_transaction_date, as_at=as_at, sort_by=sort_by, start=start, limit=limit, property_keys=property_keys, filter=filter)

Get transactions

Get the transactions from a transaction portfolio    When the requested portfolio is a derived transaction portfolio, the returned set of transactions is the union set of all transactions of the parent (and ancestors) and the specified portfolio.

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

# create an instance of the API class
api_instance = lusid.TransactionPortfoliosApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the portfolio
code = 'code_example' # str | The code of the portfolio
from_transaction_date = '2013-10-20T19:20:30+01:00' # datetime | Optional. Limit the returned transactions to those with a transaction date equal or later than this date (optional)
to_transaction_date = '2013-10-20T19:20:30+01:00' # datetime | Optional. Limit the returned transactions to those with a transaction date equal or before this date (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The AsAt date of the data (optional)
sort_by = ['sort_by_example'] # list[str] | Optional. Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName (optional)
start = 56 # int | Optional. When paginating, skip this number of results (optional)
limit = 56 # int | Optional. When paginating, limit the number of returned results to this many. (optional)
property_keys = ['property_keys_example'] # list[str] | Optional. Keys for the transaction or instrument property values that will be decorated onto the transactions. No properties will be decorated if none are specified. (optional)
filter = 'filter_example' # str | Optional. Expression to filter the result set (optional)

try:
    # Get transactions
    api_response = api_instance.get_transactions(scope, code, from_transaction_date=from_transaction_date, to_transaction_date=to_transaction_date, as_at=as_at, sort_by=sort_by, start=start, limit=limit, property_keys=property_keys, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionPortfoliosApi->get_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio | 
 **code** | **str**| The code of the portfolio | 
 **from_transaction_date** | **datetime**| Optional. Limit the returned transactions to those with a transaction date equal or later than this date | [optional] 
 **to_transaction_date** | **datetime**| Optional. Limit the returned transactions to those with a transaction date equal or before this date | [optional] 
 **as_at** | **datetime**| Optional. The AsAt date of the data | [optional] 
 **sort_by** | [**list[str]**](str.md)| Optional. Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName | [optional] 
 **start** | **int**| Optional. When paginating, skip this number of results | [optional] 
 **limit** | **int**| Optional. When paginating, limit the number of returned results to this many. | [optional] 
 **property_keys** | [**list[str]**](str.md)| Optional. Keys for the transaction or instrument property values that will be decorated onto the transactions. No properties will be decorated if none are specified. | [optional] 
 **filter** | **str**| Optional. Expression to filter the result set | [optional] 

### Return type

[**VersionedResourceListOfTransaction**](VersionedResourceListOfTransaction.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_holdings_adjustments**
> ResourceListOfHoldingsAdjustmentHeader list_holdings_adjustments(scope, code, from_effective_at=from_effective_at, to_effective_at=to_effective_at, as_at=as_at)

List holdings adjustments

Get holdings adjustments from a transaction portfolio in an interval of effective time.

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

# create an instance of the API class
api_instance = lusid.TransactionPortfoliosApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the portfolio
code = 'code_example' # str | Code for the portfolio
from_effective_at = '2013-10-20T19:20:30+01:00' # datetime | Holdings adjustments between this time (inclusive) and the toEffectiveAt are returned. (optional)
to_effective_at = '2013-10-20T19:20:30+01:00' # datetime | Holdings adjustments between this time (inclusive) and the fromEffectiveAt are returned. (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The AsAt date of the data (optional)

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
 **scope** | **str**| The scope of the portfolio | 
 **code** | **str**| Code for the portfolio | 
 **from_effective_at** | **datetime**| Holdings adjustments between this time (inclusive) and the toEffectiveAt are returned. | [optional] 
 **to_effective_at** | **datetime**| Holdings adjustments between this time (inclusive) and the fromEffectiveAt are returned. | [optional] 
 **as_at** | **datetime**| Optional. The AsAt date of the data | [optional] 

### Return type

[**ResourceListOfHoldingsAdjustmentHeader**](ResourceListOfHoldingsAdjustmentHeader.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_holdings**
> AdjustHolding set_holdings(scope, code, effective_at, holding_adjustments=holding_adjustments)

Set all holdings on a transaction portfolio

Prompt the creation of transactions in a specific transaction portfolio to bring all holdings to the specified targets

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

# create an instance of the API class
api_instance = lusid.TransactionPortfoliosApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the transaction portfolio
code = 'code_example' # str | The code of the transaction portfolio
effective_at = '2013-10-20T19:20:30+01:00' # datetime | The effective date of the change
holding_adjustments = NULL # list[AdjustHoldingRequest] | The complete set of holdings adjustments for the portfolio (optional)

try:
    # Set all holdings on a transaction portfolio
    api_response = api_instance.set_holdings(scope, code, effective_at, holding_adjustments=holding_adjustments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionPortfoliosApi->set_holdings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio | 
 **code** | **str**| The code of the transaction portfolio | 
 **effective_at** | **datetime**| The effective date of the change | 
 **holding_adjustments** | [**list[AdjustHoldingRequest]**](list.md)| The complete set of holdings adjustments for the portfolio | [optional] 

### Return type

[**AdjustHolding**](AdjustHolding.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_executions**
> UpsertPortfolioExecutionsResponse upsert_executions(scope, code, executions=executions)

Upsert executions

Inserts new executions, or updates those already present

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

# create an instance of the API class
api_instance = lusid.TransactionPortfoliosApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the portfolio
code = 'code_example' # str | The code of the portfolio
executions = NULL # list[ExecutionRequest] | The executions to be updated (optional)

try:
    # Upsert executions
    api_response = api_instance.upsert_executions(scope, code, executions=executions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionPortfoliosApi->upsert_executions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio | 
 **code** | **str**| The code of the portfolio | 
 **executions** | [**list[ExecutionRequest]**](list.md)| The executions to be updated | [optional] 

### Return type

[**UpsertPortfolioExecutionsResponse**](UpsertPortfolioExecutionsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_portfolio_details**
> PortfolioDetails upsert_portfolio_details(scope, code, effective_at=effective_at, details=details)

Upsert details

Update the portfolio details for the specified transaction portfolios or add if it doesn't already exist (in the case of a derived transaction portfolio).

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

# create an instance of the API class
api_instance = lusid.TransactionPortfoliosApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the portfolio
code = 'code_example' # str | The code of the portfolio
effective_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The effective date of the change (optional)
details = lusid.CreatePortfolioDetails() # CreatePortfolioDetails | The set of details for the portfolio (optional)

try:
    # Upsert details
    api_response = api_instance.upsert_portfolio_details(scope, code, effective_at=effective_at, details=details)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionPortfoliosApi->upsert_portfolio_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio | 
 **code** | **str**| The code of the portfolio | 
 **effective_at** | **datetime**| Optional. The effective date of the change | [optional] 
 **details** | [**CreatePortfolioDetails**](CreatePortfolioDetails.md)| The set of details for the portfolio | [optional] 

### Return type

[**PortfolioDetails**](PortfolioDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_transactions**
> UpsertPortfolioTransactionsResponse upsert_transactions(scope, code, transactions=transactions)

Upsert transactions into the specified transaction portfolio

Upsert transactions

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

# create an instance of the API class
api_instance = lusid.TransactionPortfoliosApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the portfolio
code = 'code_example' # str | The code for the portfolio
transactions = NULL # list[TransactionRequest] | The transactions to be upserted (optional)

try:
    # Upsert transactions into the specified transaction portfolio
    api_response = api_instance.upsert_transactions(scope, code, transactions=transactions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionPortfoliosApi->upsert_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio | 
 **code** | **str**| The code for the portfolio | 
 **transactions** | [**list[TransactionRequest]**](list.md)| The transactions to be upserted | [optional] 

### Return type

[**UpsertPortfolioTransactionsResponse**](UpsertPortfolioTransactionsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

