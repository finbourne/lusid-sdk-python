# lusid.TransactionPortfoliosApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_transaction_property**](TransactionPortfoliosApi.md#add_transaction_property) | **POST** /api/transactionportfolios/{scope}/{code}/transactions/{transactionId}/properties | [EARLY ACCESS] Add transaction property
[**adjust_holdings**](TransactionPortfoliosApi.md#adjust_holdings) | **POST** /api/transactionportfolios/{scope}/{code}/holdings/{effectiveAt} | [EARLY ACCESS] Adjust holdings
[**build_transactions**](TransactionPortfoliosApi.md#build_transactions) | **POST** /api/transactionportfolios/{scope}/{code}/transactions/$build | [EARLY ACCESS] Build transactions
[**cancel_adjust_holdings**](TransactionPortfoliosApi.md#cancel_adjust_holdings) | **DELETE** /api/transactionportfolios/{scope}/{code}/holdings/{effectiveAt} | [EARLY ACCESS] Cancel adjust holdings
[**cancel_executions**](TransactionPortfoliosApi.md#cancel_executions) | **DELETE** /api/transactionportfolios/{scope}/{code}/executions | [EARLY ACCESS] Cancel executions
[**cancel_transactions**](TransactionPortfoliosApi.md#cancel_transactions) | **DELETE** /api/transactionportfolios/{scope}/{code}/transactions | [EARLY ACCESS] Cancel transactions
[**create_portfolio**](TransactionPortfoliosApi.md#create_portfolio) | **POST** /api/transactionportfolios/{scope} | [EARLY ACCESS] Create portfolio
[**delete_property_from_transaction**](TransactionPortfoliosApi.md#delete_property_from_transaction) | **DELETE** /api/transactionportfolios/{scope}/{code}/transactions/{transactionId}/properties | [EARLY ACCESS] Delete property from transaction
[**get_details**](TransactionPortfoliosApi.md#get_details) | **GET** /api/transactionportfolios/{scope}/{code}/details | [EARLY ACCESS] Get details
[**get_holdings**](TransactionPortfoliosApi.md#get_holdings) | **GET** /api/transactionportfolios/{scope}/{code}/holdings | [EARLY ACCESS] Get holdings
[**get_holdings_adjustment**](TransactionPortfoliosApi.md#get_holdings_adjustment) | **GET** /api/transactionportfolios/{scope}/{code}/holdingsadjustments/{effectiveAt} | [EARLY ACCESS] Get holdings adjustment
[**get_transactions**](TransactionPortfoliosApi.md#get_transactions) | **GET** /api/transactionportfolios/{scope}/{code}/transactions | [EARLY ACCESS] Get transactions
[**list_holdings_adjustments**](TransactionPortfoliosApi.md#list_holdings_adjustments) | **GET** /api/transactionportfolios/{scope}/{code}/holdingsadjustments | [EARLY ACCESS] List holdings adjustments
[**set_holdings**](TransactionPortfoliosApi.md#set_holdings) | **PUT** /api/transactionportfolios/{scope}/{code}/holdings/{effectiveAt} | [EARLY ACCESS] Set holdings
[**upsert_executions**](TransactionPortfoliosApi.md#upsert_executions) | **POST** /api/transactionportfolios/{scope}/{code}/executions | [EARLY ACCESS] Upsert executions
[**upsert_portfolio_details**](TransactionPortfoliosApi.md#upsert_portfolio_details) | **POST** /api/transactionportfolios/{scope}/{code}/details | [EARLY ACCESS] Upsert portfolio details
[**upsert_transactions**](TransactionPortfoliosApi.md#upsert_transactions) | **POST** /api/transactionportfolios/{scope}/{code}/transactions | [EARLY ACCESS] Upsert transactions


# **add_transaction_property**
> AddTransactionPropertyResponse add_transaction_property(scope, code, transaction_id, transaction_properties)

[EARLY ACCESS] Add transaction property

Update or insert one or more transaction properties to a single transaction in a transaction portfolio.  Each property will be updated if it already exists and inserted if it does not.

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
scope = 'scope_example' # str | The scope of the transaction portfolio.
code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
transaction_id = 'transaction_id_example' # str | The unique id of the transaction to update or insert properties against.
transaction_properties = {'key': lusid.PerpetualPropertyValue()} # dict(str, PerpetualPropertyValue) | The properties with their associated values to update or insert onto the              transaction.

try:
    # [EARLY ACCESS] Add transaction property
    api_response = api_instance.add_transaction_property(scope, code, transaction_id, transaction_properties)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionPortfoliosApi->add_transaction_property: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. | 
 **transaction_id** | **str**| The unique id of the transaction to update or insert properties against. | 
 **transaction_properties** | [**dict(str, PerpetualPropertyValue)**](PerpetualPropertyValue.md)| The properties with their associated values to update or insert onto the              transaction. | 

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

[EARLY ACCESS] Adjust holdings

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

# create an instance of the API class
api_instance = lusid.TransactionPortfoliosApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the transaction portfolio.
code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
effective_at = 'effective_at_example' # str | The effective datetime at which the holdings should be set to the provided targets.
holding_adjustments = None # list[AdjustHoldingRequest] | The selected set of holdings to adjust to the provided targets for the              transaction portfolio. (optional)

try:
    # [EARLY ACCESS] Adjust holdings
    api_response = api_instance.adjust_holdings(scope, code, effective_at, holding_adjustments=holding_adjustments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionPortfoliosApi->adjust_holdings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. | 
 **effective_at** | **str**| The effective datetime at which the holdings should be set to the provided targets. | 
 **holding_adjustments** | [**list[AdjustHoldingRequest]**](list.md)| The selected set of holdings to adjust to the provided targets for the              transaction portfolio. | [optional] 

### Return type

[**AdjustHolding**](AdjustHolding.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **build_transactions**
> VersionedResourceListOfOutputTransaction build_transactions(scope, code, parameters, as_at=as_at, property_keys=property_keys, filter=filter)

[EARLY ACCESS] Build transactions

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

# create an instance of the API class
api_instance = lusid.TransactionPortfoliosApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the transaction portfolio.
code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
parameters = lusid.TransactionQueryParameters() # TransactionQueryParameters | The query parameters which control how the output transactions are built.
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to build the transactions. Defaults to return the latest              version of each transaction if not specified. (optional)
property_keys = ['property_keys_example'] # list[str] | A list of property keys from the \"Instrument\" or \"Trade\" domain to decorate onto              the transactions. These take the format {domain}/{scope}/{code} e.g. \"Instrument/system/Name\" or              \"Trade/strategy/quantsignal\". (optional)
filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)

try:
    # [EARLY ACCESS] Build transactions
    api_response = api_instance.build_transactions(scope, code, parameters, as_at=as_at, property_keys=property_keys, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionPortfoliosApi->build_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. | 
 **parameters** | [**TransactionQueryParameters**](TransactionQueryParameters.md)| The query parameters which control how the output transactions are built. | 
 **as_at** | **datetime**| The asAt datetime at which to build the transactions. Defaults to return the latest              version of each transaction if not specified. | [optional] 
 **property_keys** | [**list[str]**](str.md)| A list of property keys from the \&quot;Instrument\&quot; or \&quot;Trade\&quot; domain to decorate onto              the transactions. These take the format {domain}/{scope}/{code} e.g. \&quot;Instrument/system/Name\&quot; or              \&quot;Trade/strategy/quantsignal\&quot;. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 

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

[EARLY ACCESS] Cancel adjust holdings

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

# create an instance of the API class
api_instance = lusid.TransactionPortfoliosApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the transaction portfolio.
code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
effective_at = 'effective_at_example' # str | The effective datetime at which the holding adjustments should be undone.

try:
    # [EARLY ACCESS] Cancel adjust holdings
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
 **effective_at** | **str**| The effective datetime at which the holding adjustments should be undone. | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

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

# create an instance of the API class
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_transactions**
> DeletedEntityResponse cancel_transactions(scope, code, transaction_ids)

[EARLY ACCESS] Cancel transactions

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

# create an instance of the API class
api_instance = lusid.TransactionPortfoliosApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the transaction portfolio.
code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
transaction_ids = ['transaction_ids_example'] # list[str] | The ids of the transactions to cancel.

try:
    # [EARLY ACCESS] Cancel transactions
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_portfolio**
> Portfolio create_portfolio(scope, create_request=create_request)

[EARLY ACCESS] Create portfolio

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

# create an instance of the API class
api_instance = lusid.TransactionPortfoliosApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope that the transaction portfolio will be created in.
create_request = lusid.CreateTransactionPortfolioRequest() # CreateTransactionPortfolioRequest | The definition and details of the transaction portfolio. (optional)

try:
    # [EARLY ACCESS] Create portfolio
    api_response = api_instance.create_portfolio(scope, create_request=create_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionPortfoliosApi->create_portfolio: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that the transaction portfolio will be created in. | 
 **create_request** | [**CreateTransactionPortfolioRequest**](CreateTransactionPortfolioRequest.md)| The definition and details of the transaction portfolio. | [optional] 

### Return type

[**Portfolio**](Portfolio.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_property_from_transaction**
> DeletedEntityResponse delete_property_from_transaction(scope, code, transaction_id, transaction_property_key)

[EARLY ACCESS] Delete property from transaction

Delete a single property value from a single transaction in a transaction portfolio.

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
scope = 'scope_example' # str | The scope of the transaction portfolio.
code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
transaction_id = 'transaction_id_example' # str | The unique id of the transaction to delete the property value from.
transaction_property_key = 'transaction_property_key_example' # str | The property key of the property value to delete from the transaction.              This must be from the \"Trade\" domain and will have the format {domain}/{scope}/{code} e.g.              \"Trade/strategy/quantsignal\".

try:
    # [EARLY ACCESS] Delete property from transaction
    api_response = api_instance.delete_property_from_transaction(scope, code, transaction_id, transaction_property_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionPortfoliosApi->delete_property_from_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. | 
 **transaction_id** | **str**| The unique id of the transaction to delete the property value from. | 
 **transaction_property_key** | **str**| The property key of the property value to delete from the transaction.              This must be from the \&quot;Trade\&quot; domain and will have the format {domain}/{scope}/{code} e.g.              \&quot;Trade/strategy/quantsignal\&quot;. | 

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

[EARLY ACCESS] Get details

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

# create an instance of the API class
api_instance = lusid.TransactionPortfoliosApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the transaction portfolio to retrieve the details for.
code = 'code_example' # str | The code of the transaction portfolio to retrieve the details for. Together with the              scope this uniquely identifies the transaction portfolio.
effective_at = 'effective_at_example' # str | The effective datetime at which to retrieve the details of the transaction              portfolio. Defaults to the current LUSID system datetime if not specified. (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the details of the transaction portfolio. Defaults              to return the latest version of the details if not specified. (optional)

try:
    # [EARLY ACCESS] Get details
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
 **effective_at** | **str**| The effective datetime at which to retrieve the details of the transaction              portfolio. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the details of the transaction portfolio. Defaults              to return the latest version of the details if not specified. | [optional] 

### Return type

[**PortfolioDetails**](PortfolioDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_holdings**
> VersionedResourceListOfPortfolioHolding get_holdings(scope, code, by_taxlots=by_taxlots, effective_at=effective_at, as_at=as_at, filter=filter, property_keys=property_keys)

[EARLY ACCESS] Get holdings

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

# create an instance of the API class
api_instance = lusid.TransactionPortfoliosApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the transaction portfolio.
code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
by_taxlots = True # bool | Whether or not to expand the holdings to return the underlying tax-lots. Defaults to              False. (optional)
effective_at = 'effective_at_example' # str | The effective datetime at which to retrieve the holdings of the transaction              portfolio. Defaults to the current LUSID system datetime if not specified. (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the holdings of the transaction portfolio. Defaults              to return the latest version of the holdings if not specified. (optional)
filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)
property_keys = ['property_keys_example'] # list[str] | A list of property keys from the \"Instrument\" or \"Holding\" domain to decorate onto              the holdings. These take the format {domain}/{scope}/{code} e.g. \"Instrument/system/Name\" or \"Holding/system/Cost\". (optional)

try:
    # [EARLY ACCESS] Get holdings
    api_response = api_instance.get_holdings(scope, code, by_taxlots=by_taxlots, effective_at=effective_at, as_at=as_at, filter=filter, property_keys=property_keys)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionPortfoliosApi->get_holdings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. | 
 **by_taxlots** | **bool**| Whether or not to expand the holdings to return the underlying tax-lots. Defaults to              False. | [optional] 
 **effective_at** | **str**| The effective datetime at which to retrieve the holdings of the transaction              portfolio. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the holdings of the transaction portfolio. Defaults              to return the latest version of the holdings if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **property_keys** | [**list[str]**](str.md)| A list of property keys from the \&quot;Instrument\&quot; or \&quot;Holding\&quot; domain to decorate onto              the holdings. These take the format {domain}/{scope}/{code} e.g. \&quot;Instrument/system/Name\&quot; or \&quot;Holding/system/Cost\&quot;. | [optional] 

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

[EARLY ACCESS] Get holdings adjustment

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

# create an instance of the API class
api_instance = lusid.TransactionPortfoliosApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the transaction portfolio.
code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
effective_at = 'effective_at_example' # str | The effective datetime of the holdings adjustment.
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the holdings adjustment. Defaults to the return the latest              version of the holdings adjustment if not specified. (optional)

try:
    # [EARLY ACCESS] Get holdings adjustment
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
 **effective_at** | **str**| The effective datetime of the holdings adjustment. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the holdings adjustment. Defaults to the return the latest              version of the holdings adjustment if not specified. | [optional] 

### Return type

[**HoldingsAdjustment**](HoldingsAdjustment.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transactions**
> VersionedResourceListOfTransaction get_transactions(scope, code, from_transaction_date=from_transaction_date, to_transaction_date=to_transaction_date, as_at=as_at, property_keys=property_keys, filter=filter)

[EARLY ACCESS] Get transactions

Get transactions from the specified transaction portfolio over a given interval of effective time.     When the specified portfolio is a derived transaction portfolio, the returned set of transactions is the  union set of all transactions of the parent (and any grandparents etc.) and the specified derived transaction portfolio itself.

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
scope = 'scope_example' # str | The scope of the transaction portfolio.
code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
from_transaction_date = 'from_transaction_date_example' # str | The lower bound effective datetime (inclusive) from which to retrieve the transactions.              There is no lower bound if this is not specified. (optional)
to_transaction_date = 'to_transaction_date_example' # str | The upper bound effective datetime (inclusive) from which to retrieve transactions.              There is no upper bound if this is not specified. (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the transactions. Defaults to return the latest version              of each transaction if not specified. (optional)
property_keys = ['property_keys_example'] # list[str] | A list of property keys from the \"Instrument\" or \"Trade\" domain to decorate onto              the transactions. These take the format {domain}/{scope}/{code} e.g. \"Instrument/system/Name\" or              \"Trade/strategy/quantsignal\". (optional)
filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)

try:
    # [EARLY ACCESS] Get transactions
    api_response = api_instance.get_transactions(scope, code, from_transaction_date=from_transaction_date, to_transaction_date=to_transaction_date, as_at=as_at, property_keys=property_keys, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionPortfoliosApi->get_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. | 
 **from_transaction_date** | **str**| The lower bound effective datetime (inclusive) from which to retrieve the transactions.              There is no lower bound if this is not specified. | [optional] 
 **to_transaction_date** | **str**| The upper bound effective datetime (inclusive) from which to retrieve transactions.              There is no upper bound if this is not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the transactions. Defaults to return the latest version              of each transaction if not specified. | [optional] 
 **property_keys** | [**list[str]**](str.md)| A list of property keys from the \&quot;Instrument\&quot; or \&quot;Trade\&quot; domain to decorate onto              the transactions. These take the format {domain}/{scope}/{code} e.g. \&quot;Instrument/system/Name\&quot; or              \&quot;Trade/strategy/quantsignal\&quot;. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 

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

[EARLY ACCESS] List holdings adjustments

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

# create an instance of the API class
api_instance = lusid.TransactionPortfoliosApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the transaction portfolio.
code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
from_effective_at = 'from_effective_at_example' # str | The lower bound effective datetime (inclusive) from which to retrieve the holdings              adjustments. There is no lower bound if this is not specified. (optional)
to_effective_at = 'to_effective_at_example' # str | The upper bound effective datetime (inclusive) from which to retrieve the holdings              adjustments. There is no upper bound if this is not specified. (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the holdings adjustments. Defaults to return the              latest version of each holding adjustment if not specified. (optional)

try:
    # [EARLY ACCESS] List holdings adjustments
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
 **from_effective_at** | **str**| The lower bound effective datetime (inclusive) from which to retrieve the holdings              adjustments. There is no lower bound if this is not specified. | [optional] 
 **to_effective_at** | **str**| The upper bound effective datetime (inclusive) from which to retrieve the holdings              adjustments. There is no upper bound if this is not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the holdings adjustments. Defaults to return the              latest version of each holding adjustment if not specified. | [optional] 

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

[EARLY ACCESS] Set holdings

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

# create an instance of the API class
api_instance = lusid.TransactionPortfoliosApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the transaction portfolio.
code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
effective_at = 'effective_at_example' # str | The effective datetime at which the holdings should be set to the provided targets.
holding_adjustments = None # list[AdjustHoldingRequest] | The complete set of target holdings for the transaction portfolio. (optional)

try:
    # [EARLY ACCESS] Set holdings
    api_response = api_instance.set_holdings(scope, code, effective_at, holding_adjustments=holding_adjustments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionPortfoliosApi->set_holdings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. | 
 **effective_at** | **str**| The effective datetime at which the holdings should be set to the provided targets. | 
 **holding_adjustments** | [**list[AdjustHoldingRequest]**](list.md)| The complete set of target holdings for the transaction portfolio. | [optional] 

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

# create an instance of the API class
api_instance = lusid.TransactionPortfoliosApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the transaction portfolio.
code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
executions = None # list[ExecutionRequest] | The executions to update or insert. (optional)

try:
    # [EARLY ACCESS] Upsert executions
    api_response = api_instance.upsert_executions(scope, code, executions=executions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionPortfoliosApi->upsert_executions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. | 
 **executions** | [**list[ExecutionRequest]**](list.md)| The executions to update or insert. | [optional] 

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

[EARLY ACCESS] Upsert portfolio details

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

# create an instance of the API class
api_instance = lusid.TransactionPortfoliosApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the transaction portfolio to update or insert details for.
code = 'code_example' # str | The code of the transaction portfolio to update or insert details for. Together with the              scope this uniquely identifies the transaction portfolio.
effective_at = 'effective_at_example' # str | The effective datetime at which the updated or inserted details should become valid.              Defaults to the current LUSID system datetime if not specified. (optional)
details = lusid.CreatePortfolioDetails() # CreatePortfolioDetails | The details to update or insert for the specified transaction portfolio. (optional)

try:
    # [EARLY ACCESS] Upsert portfolio details
    api_response = api_instance.upsert_portfolio_details(scope, code, effective_at=effective_at, details=details)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionPortfoliosApi->upsert_portfolio_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio to update or insert details for. | 
 **code** | **str**| The code of the transaction portfolio to update or insert details for. Together with the              scope this uniquely identifies the transaction portfolio. | 
 **effective_at** | **str**| The effective datetime at which the updated or inserted details should become valid.              Defaults to the current LUSID system datetime if not specified. | [optional] 
 **details** | [**CreatePortfolioDetails**](CreatePortfolioDetails.md)| The details to update or insert for the specified transaction portfolio. | [optional] 

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

[EARLY ACCESS] Upsert transactions

Update or insert transactions into the specified transaction portfolio. A transaction will be updated  if it already exists and inserted if it does not.

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
scope = 'scope_example' # str | The scope of the transaction portfolio.
code = 'code_example' # str | The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio.
transactions = None # list[TransactionRequest] | The transactions to be updated or inserted. (optional)

try:
    # [EARLY ACCESS] Upsert transactions
    api_response = api_instance.upsert_transactions(scope, code, transactions=transactions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionPortfoliosApi->upsert_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the transaction portfolio. | 
 **code** | **str**| The code of the transaction portfolio. Together with the scope this uniquely identifies              the transaction portfolio. | 
 **transactions** | [**list[TransactionRequest]**](list.md)| The transactions to be updated or inserted. | [optional] 

### Return type

[**UpsertPortfolioTransactionsResponse**](UpsertPortfolioTransactionsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

