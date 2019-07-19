# lusid.PortfoliosApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_portfolio**](PortfoliosApi.md#delete_portfolio) | **DELETE** /api/portfolios/{scope}/{code} | [EARLY ACCESS] Delete portfolio
[**delete_portfolio_properties**](PortfoliosApi.md#delete_portfolio_properties) | **DELETE** /api/portfolios/{scope}/{code}/properties | [EARLY ACCESS] Delete portfolio properties
[**get_portfolio**](PortfoliosApi.md#get_portfolio) | **GET** /api/portfolios/{scope}/{code} | [EARLY ACCESS] Get portfolio definition
[**get_portfolio_commands**](PortfoliosApi.md#get_portfolio_commands) | **GET** /api/portfolios/{scope}/{code}/commands | [EARLY ACCESS] Get commands
[**get_portfolio_properties**](PortfoliosApi.md#get_portfolio_properties) | **GET** /api/portfolios/{scope}/{code}/properties | [EARLY ACCESS] Get portfolio properties
[**list_portfolios**](PortfoliosApi.md#list_portfolios) | **GET** /api/portfolios | [EARLY ACCESS] List portfolios
[**list_portfolios_for_scope**](PortfoliosApi.md#list_portfolios_for_scope) | **GET** /api/portfolios/{scope} | [EARLY ACCESS] List portfolios for scope
[**update_portfolio**](PortfoliosApi.md#update_portfolio) | **PUT** /api/portfolios/{scope}/{code} | [EARLY ACCESS] Update portfolio definition
[**upsert_portfolio_properties**](PortfoliosApi.md#upsert_portfolio_properties) | **POST** /api/portfolios/{scope}/{code}/properties | [EARLY ACCESS] Upsert portfolio properties


# **delete_portfolio**
> DeletedEntityResponse delete_portfolio(scope, code, effective_at=effective_at)

[EARLY ACCESS] Delete portfolio

Delete a portfolio at the specified effectiveAt

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
api_instance = lusid.PortfoliosApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the portfolio
code = 'code_example' # str | The code of the portfolio
effective_at = 'effective_at_example' # str | Optional. The effective date of the deletion (optional)

try:
    # [EARLY ACCESS] Delete portfolio
    api_response = api_instance.delete_portfolio(scope, code, effective_at=effective_at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfoliosApi->delete_portfolio: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio | 
 **code** | **str**| The code of the portfolio | 
 **effective_at** | **str**| Optional. The effective date of the deletion | [optional] 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_portfolio_properties**
> DeletedEntityResponse delete_portfolio_properties(scope, code, effective_at=effective_at, portfolio_property_keys=portfolio_property_keys)

[EARLY ACCESS] Delete portfolio properties

Delete one, many or all property values from a portfolio for the specified effectiveAt                Specifying no effectiveAt will delete all properties

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
api_instance = lusid.PortfoliosApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the portfolio
code = 'code_example' # str | Code for the portfolio
effective_at = 'effective_at_example' # str | Optional. The effective date of the deletion (optional)
portfolio_property_keys = ['portfolio_property_keys_example'] # list[str] | Optional. The keys of the properties to be deleted. None specified indicates the intention to delete all properties from the portfolio (optional)

try:
    # [EARLY ACCESS] Delete portfolio properties
    api_response = api_instance.delete_portfolio_properties(scope, code, effective_at=effective_at, portfolio_property_keys=portfolio_property_keys)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfoliosApi->delete_portfolio_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio | 
 **code** | **str**| Code for the portfolio | 
 **effective_at** | **str**| Optional. The effective date of the deletion | [optional] 
 **portfolio_property_keys** | [**list[str]**](str.md)| Optional. The keys of the properties to be deleted. None specified indicates the intention to delete all properties from the portfolio | [optional] 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_portfolio**
> Portfolio get_portfolio(scope, code, effective_at=effective_at, as_at=as_at)

[EARLY ACCESS] Get portfolio definition

Retrieves the basic set of information about a portfolio using the specified scope and code.

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
api_instance = lusid.PortfoliosApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the portfolio
code = 'code_example' # str | The code of the portfolio
effective_at = 'effective_at_example' # str | Optional. The effective date of the data (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The AsAt date of the data (optional)

try:
    # [EARLY ACCESS] Get portfolio definition
    api_response = api_instance.get_portfolio(scope, code, effective_at=effective_at, as_at=as_at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfoliosApi->get_portfolio: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio | 
 **code** | **str**| The code of the portfolio | 
 **effective_at** | **str**| Optional. The effective date of the data | [optional] 
 **as_at** | **datetime**| Optional. The AsAt date of the data | [optional] 

### Return type

[**Portfolio**](Portfolio.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_portfolio_commands**
> ResourceListOfProcessedCommand get_portfolio_commands(scope, code, from_as_at=from_as_at, to_as_at=to_as_at, sort_by=sort_by, start=start, limit=limit, filter=filter)

[EARLY ACCESS] Get commands

Gets all commands that modified a specific portfolio, including any input transactions.

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
api_instance = lusid.PortfoliosApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the portfolio
code = 'code_example' # str | The code of the portfolio
from_as_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. Filters commands by those that were processed at or after this date and time (optional)
to_as_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. Filters commands by those that were processed at or before this date and time (optional)
sort_by = ['sort_by_example'] # list[str] | Optional. Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName (optional)
start = 56 # int | Optional. When paginating, skip this number of results (optional)
limit = 56 # int | Optional. When paginating, limit the number of returned results to this many. (optional)
filter = 'filter_example' # str | Optional. Expression to filter the result set (optional)

try:
    # [EARLY ACCESS] Get commands
    api_response = api_instance.get_portfolio_commands(scope, code, from_as_at=from_as_at, to_as_at=to_as_at, sort_by=sort_by, start=start, limit=limit, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfoliosApi->get_portfolio_commands: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio | 
 **code** | **str**| The code of the portfolio | 
 **from_as_at** | **datetime**| Optional. Filters commands by those that were processed at or after this date and time | [optional] 
 **to_as_at** | **datetime**| Optional. Filters commands by those that were processed at or before this date and time | [optional] 
 **sort_by** | [**list[str]**](str.md)| Optional. Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName | [optional] 
 **start** | **int**| Optional. When paginating, skip this number of results | [optional] 
 **limit** | **int**| Optional. When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Optional. Expression to filter the result set | [optional] 

### Return type

[**ResourceListOfProcessedCommand**](ResourceListOfProcessedCommand.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_portfolio_properties**
> PortfolioProperties get_portfolio_properties(scope, code, effective_at=effective_at, as_at=as_at, sort_by=sort_by, start=start, limit=limit)

[EARLY ACCESS] Get portfolio properties

Get the properties of a portfolio

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
api_instance = lusid.PortfoliosApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the portfolio
code = 'code_example' # str | The code of the portfolio
effective_at = 'effective_at_example' # str | Optional. The effective date of the data (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The AsAt date of the data (optional)
sort_by = ['sort_by_example'] # list[str] | Optional. Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName (optional)
start = 56 # int | Optional. When paginating, skip this number of results (optional)
limit = 56 # int | Optional. When paginating, limit the number of returned results to this many. (optional)

try:
    # [EARLY ACCESS] Get portfolio properties
    api_response = api_instance.get_portfolio_properties(scope, code, effective_at=effective_at, as_at=as_at, sort_by=sort_by, start=start, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfoliosApi->get_portfolio_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio | 
 **code** | **str**| The code of the portfolio | 
 **effective_at** | **str**| Optional. The effective date of the data | [optional] 
 **as_at** | **datetime**| Optional. The AsAt date of the data | [optional] 
 **sort_by** | [**list[str]**](str.md)| Optional. Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName | [optional] 
 **start** | **int**| Optional. When paginating, skip this number of results | [optional] 
 **limit** | **int**| Optional. When paginating, limit the number of returned results to this many. | [optional] 

### Return type

[**PortfolioProperties**](PortfolioProperties.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_portfolios**
> ResourceListOfPortfolio list_portfolios(effective_at=effective_at, as_at=as_at, page=page, sort_by=sort_by, start=start, limit=limit, filter=filter, query=query, portfolio_property_keys=portfolio_property_keys)

[EARLY ACCESS] List portfolios

List all portfolios matching the specified criteria.                Example query syntax for the query parameter:                - To see which portfolios have holdings in the specified instruments:                    instrument.identifiers in (('LusidInstrumentId', 'LUID_PPA8HI6M'), ('Figi', 'BBG000BLNNH6'))                * Note that copy/pasting above examples results in incorrect single quote character

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
api_instance = lusid.PortfoliosApi(lusid.ApiClient(configuration))
effective_at = 'effective_at_example' # str | Optional. The effective date of the data (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The AsAt date of the data (optional)
page = 'page_example' # str | Optional. The pagination token to continue listing portfolios. This value is returned from a previous call to ListPortfolios.  If this is set, then the sortBy, filter, query, effectiveAt, and asAt fields must not have changed. Also, if set, a start  value cannot be set. (optional)
sort_by = ['sort_by_example'] # list[str] | Optional. Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName (optional)
start = 56 # int | Optional. When paginating, skip this number of results (optional)
limit = 56 # int | Optional. When paginating, limit the number of returned results to this many. (optional)
filter = 'filter_example' # str | Optional. Expression to filter the result set (optional)
query = 'query_example' # str | Optional. Expression specifying the criteria that the returned portfolios must meet (optional)
portfolio_property_keys = ['portfolio_property_keys_example'] # list[str] | Optional. Keys of the properties to be decorated on to the portfolio (optional)

try:
    # [EARLY ACCESS] List portfolios
    api_response = api_instance.list_portfolios(effective_at=effective_at, as_at=as_at, page=page, sort_by=sort_by, start=start, limit=limit, filter=filter, query=query, portfolio_property_keys=portfolio_property_keys)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfoliosApi->list_portfolios: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **effective_at** | **str**| Optional. The effective date of the data | [optional] 
 **as_at** | **datetime**| Optional. The AsAt date of the data | [optional] 
 **page** | **str**| Optional. The pagination token to continue listing portfolios. This value is returned from a previous call to ListPortfolios.  If this is set, then the sortBy, filter, query, effectiveAt, and asAt fields must not have changed. Also, if set, a start  value cannot be set. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Optional. Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName | [optional] 
 **start** | **int**| Optional. When paginating, skip this number of results | [optional] 
 **limit** | **int**| Optional. When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Optional. Expression to filter the result set | [optional] 
 **query** | **str**| Optional. Expression specifying the criteria that the returned portfolios must meet | [optional] 
 **portfolio_property_keys** | [**list[str]**](str.md)| Optional. Keys of the properties to be decorated on to the portfolio | [optional] 

### Return type

[**ResourceListOfPortfolio**](ResourceListOfPortfolio.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_portfolios_for_scope**
> ResourceListOfPortfolio list_portfolios_for_scope(scope, effective_at=effective_at, as_at=as_at, sort_by=sort_by, start=start, limit=limit, filter=filter, portfolio_property_keys=portfolio_property_keys)

[EARLY ACCESS] List portfolios for scope

List all the portfolios in the specified scope

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
api_instance = lusid.PortfoliosApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope
effective_at = 'effective_at_example' # str | Optional. The effective date of the data (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The AsAt date of the data (optional)
sort_by = ['sort_by_example'] # list[str] | Optional. Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName (optional)
start = 56 # int | Optional. When paginating, skip this number of results (optional)
limit = 56 # int | Optional. When paginating, limit the number of returned results to this many. (optional)
filter = 'filter_example' # str | Optional. Expression to filter the result set (optional)
portfolio_property_keys = ['portfolio_property_keys_example'] # list[str] | Optional. Keys of the properties to be decorated on to the portfolio (optional)

try:
    # [EARLY ACCESS] List portfolios for scope
    api_response = api_instance.list_portfolios_for_scope(scope, effective_at=effective_at, as_at=as_at, sort_by=sort_by, start=start, limit=limit, filter=filter, portfolio_property_keys=portfolio_property_keys)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfoliosApi->list_portfolios_for_scope: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope | 
 **effective_at** | **str**| Optional. The effective date of the data | [optional] 
 **as_at** | **datetime**| Optional. The AsAt date of the data | [optional] 
 **sort_by** | [**list[str]**](str.md)| Optional. Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName | [optional] 
 **start** | **int**| Optional. When paginating, skip this number of results | [optional] 
 **limit** | **int**| Optional. When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Optional. Expression to filter the result set | [optional] 
 **portfolio_property_keys** | [**list[str]**](str.md)| Optional. Keys of the properties to be decorated on to the portfolio | [optional] 

### Return type

[**ResourceListOfPortfolio**](ResourceListOfPortfolio.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_portfolio**
> Portfolio update_portfolio(scope, code, effective_at=effective_at, request=request)

[EARLY ACCESS] Update portfolio definition

Update the definition of a specific portfolio. Note, some parts of a portfolio definition are not available for modification after the initial creation.

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
api_instance = lusid.PortfoliosApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the portfolio
code = 'code_example' # str | The code of the portfolio
effective_at = 'effective_at_example' # str | Optional. The effective date for the change (optional)
request = lusid.UpdatePortfolioRequest() # UpdatePortfolioRequest | The updated portfolio definition (optional)

try:
    # [EARLY ACCESS] Update portfolio definition
    api_response = api_instance.update_portfolio(scope, code, effective_at=effective_at, request=request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfoliosApi->update_portfolio: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio | 
 **code** | **str**| The code of the portfolio | 
 **effective_at** | **str**| Optional. The effective date for the change | [optional] 
 **request** | [**UpdatePortfolioRequest**](UpdatePortfolioRequest.md)| The updated portfolio definition | [optional] 

### Return type

[**Portfolio**](Portfolio.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_portfolio_properties**
> PortfolioProperties upsert_portfolio_properties(scope, code, portfolio_properties=portfolio_properties)

[EARLY ACCESS] Upsert portfolio properties

Upsert one or more property values to a portfolio. All properties must be of the domain Portfolio.

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
api_instance = lusid.PortfoliosApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the portfolio
code = 'code_example' # str | The code of the portfolio
portfolio_properties = {'key': lusid.ModelProperty()} # dict(str, ModelProperty) | The property values to be upserted to the portfolio. Time variant properties must have an EffectiveFrom date. (optional)

try:
    # [EARLY ACCESS] Upsert portfolio properties
    api_response = api_instance.upsert_portfolio_properties(scope, code, portfolio_properties=portfolio_properties)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfoliosApi->upsert_portfolio_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio | 
 **code** | **str**| The code of the portfolio | 
 **portfolio_properties** | [**dict(str, ModelProperty)**](ModelProperty.md)| The property values to be upserted to the portfolio. Time variant properties must have an EffectiveFrom date. | [optional] 

### Return type

[**PortfolioProperties**](PortfolioProperties.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

