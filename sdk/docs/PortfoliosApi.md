# lusid.PortfoliosApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_portfolio**](PortfoliosApi.md#delete_portfolio) | **DELETE** /api/portfolios/{scope}/{code} | [EARLY ACCESS] Delete portfolio
[**delete_portfolio_properties**](PortfoliosApi.md#delete_portfolio_properties) | **DELETE** /api/portfolios/{scope}/{code}/properties | [EARLY ACCESS] Delete portfolio properties
[**get_portfolio**](PortfoliosApi.md#get_portfolio) | **GET** /api/portfolios/{scope}/{code} | [EARLY ACCESS] Get portfolio
[**get_portfolio_commands**](PortfoliosApi.md#get_portfolio_commands) | **GET** /api/portfolios/{scope}/{code}/commands | [EARLY ACCESS] Get portfolio commands
[**get_portfolio_properties**](PortfoliosApi.md#get_portfolio_properties) | **GET** /api/portfolios/{scope}/{code}/properties | [EARLY ACCESS] Get portfolio properties
[**list_portfolios**](PortfoliosApi.md#list_portfolios) | **GET** /api/portfolios | [EARLY ACCESS] List portfolios
[**list_portfolios_for_scope**](PortfoliosApi.md#list_portfolios_for_scope) | **GET** /api/portfolios/{scope} | [EARLY ACCESS] List portfolios for scope
[**update_portfolio**](PortfoliosApi.md#update_portfolio) | **PUT** /api/portfolios/{scope}/{code} | [EARLY ACCESS] Update portfolio
[**upsert_portfolio_properties**](PortfoliosApi.md#upsert_portfolio_properties) | **POST** /api/portfolios/{scope}/{code}/properties | [EARLY ACCESS] Upsert portfolio properties


# **delete_portfolio**
> DeletedEntityResponse delete_portfolio(scope, code)

[EARLY ACCESS] Delete portfolio

Delete a single portfolio. The deletion of the portfolio will be valid from the portfolio's creation datetime. This means that the portfolio will no longer exist at any effective datetime from the asAt datetime of deletion.

### Example

```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lusid.PortfoliosApi()
scope = 'scope_example' # str | The scope of the portfolio.
code = 'code_example' # str | The code of the portfolio.

try:
    # [EARLY ACCESS] Delete portfolio
    api_response = api_instance.delete_portfolio(scope, code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfoliosApi->delete_portfolio: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio. | 
 **code** | **str**| The code of the portfolio. | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_portfolio_properties**
> DeletedEntityResponse delete_portfolio_properties(scope, code, portfolio_property_keys, effective_at=effective_at)

[EARLY ACCESS] Delete portfolio properties

Delete one or more properties from a single portfolio.

### Example

```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lusid.PortfoliosApi()
scope = 'scope_example' # str | The scope of the portfolio to delete properties from.
code = 'code_example' # str | The code of the portfolio to delete properties from. Together with the scope this uniquely              identifies the portfolio.
portfolio_property_keys = ['portfolio_property_keys_example'] # list[str] | The property keys of the properties to delete. These take the format              {domain}/{scope}/{code} e.g. \"Portfolio/Manager/Id\". Each property must be from the \"Portfolio\" domain.
effective_at = 'effective_at_example' # str | The effective datetime at which to delete the properties. Defaults to the current LUSID system datetime if not specified. (optional)

try:
    # [EARLY ACCESS] Delete portfolio properties
    api_response = api_instance.delete_portfolio_properties(scope, code, portfolio_property_keys, effective_at=effective_at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfoliosApi->delete_portfolio_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio to delete properties from. | 
 **code** | **str**| The code of the portfolio to delete properties from. Together with the scope this uniquely              identifies the portfolio. | 
 **portfolio_property_keys** | [**list[str]**](str.md)| The property keys of the properties to delete. These take the format              {domain}/{scope}/{code} e.g. \&quot;Portfolio/Manager/Id\&quot;. Each property must be from the \&quot;Portfolio\&quot; domain. | 
 **effective_at** | **str**| The effective datetime at which to delete the properties. Defaults to the current LUSID system datetime if not specified. | [optional] 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_portfolio**
> Portfolio get_portfolio(scope, code, effective_at=effective_at, as_at=as_at)

[EARLY ACCESS] Get portfolio

Retrieve the definition of a single portfolio.

### Example

```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lusid.PortfoliosApi()
scope = 'scope_example' # str | The scope of the portfolio to retrieve the definition for.
code = 'code_example' # str | The code of the portfolio to retrieve the definition for. Together with the scope this              uniquely identifies the portfolio.
effective_at = 'effective_at_example' # str | The effective datetime at which to retrieve the portfolio definition. Defaults to the current LUSID system datetime if not specified. (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the portfolio definition. Defaults to return the latest version of the portfolio definition if not specified. (optional)

try:
    # [EARLY ACCESS] Get portfolio
    api_response = api_instance.get_portfolio(scope, code, effective_at=effective_at, as_at=as_at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfoliosApi->get_portfolio: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio to retrieve the definition for. | 
 **code** | **str**| The code of the portfolio to retrieve the definition for. Together with the scope this              uniquely identifies the portfolio. | 
 **effective_at** | **str**| The effective datetime at which to retrieve the portfolio definition. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the portfolio definition. Defaults to return the latest version of the portfolio definition if not specified. | [optional] 

### Return type

[**Portfolio**](Portfolio.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_portfolio_commands**
> ResourceListOfProcessedCommand get_portfolio_commands(scope, code, from_as_at=from_as_at, to_as_at=to_as_at, filter=filter)

[EARLY ACCESS] Get portfolio commands

Gets all the commands that modified a single portfolio, including any input transactions.

### Example

```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lusid.PortfoliosApi()
scope = 'scope_example' # str | The scope of the portfolio to retrieve the commands for.
code = 'code_example' # str | The code of the portfolio to retrieve the commands for. Together with the scope this uniquely identifies              the portfolio.
from_as_at = '2013-10-20T19:20:30+01:00' # datetime | The lower bound asAt datetime (inclusive) from which to retrieve commands. There is no lower bound if this is not specified. (optional)
to_as_at = '2013-10-20T19:20:30+01:00' # datetime | The upper bound asAt datetime (inclusive) from which to retrieve commands. There is no upper bound if this is not specified. (optional)
filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)

try:
    # [EARLY ACCESS] Get portfolio commands
    api_response = api_instance.get_portfolio_commands(scope, code, from_as_at=from_as_at, to_as_at=to_as_at, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfoliosApi->get_portfolio_commands: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio to retrieve the commands for. | 
 **code** | **str**| The code of the portfolio to retrieve the commands for. Together with the scope this uniquely identifies              the portfolio. | 
 **from_as_at** | **datetime**| The lower bound asAt datetime (inclusive) from which to retrieve commands. There is no lower bound if this is not specified. | [optional] 
 **to_as_at** | **datetime**| The upper bound asAt datetime (inclusive) from which to retrieve commands. There is no upper bound if this is not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 

### Return type

[**ResourceListOfProcessedCommand**](ResourceListOfProcessedCommand.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_portfolio_properties**
> PortfolioProperties get_portfolio_properties(scope, code, effective_at=effective_at, as_at=as_at)

[EARLY ACCESS] Get portfolio properties

List all the properties of a single portfolio.

### Example

```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lusid.PortfoliosApi()
scope = 'scope_example' # str | The scope of the portfolio to list the properties for.
code = 'code_example' # str | The code of the portfolio to list the properties for. Together with the scope this uniquely              identifies the portfolio.
effective_at = 'effective_at_example' # str | The effective datetime at which to list the portfolio's properties. Defaults to the current LUSID system datetime if not specified. (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the portfolio's properties. Defaults to return the latest version of each property if not specified. (optional)

try:
    # [EARLY ACCESS] Get portfolio properties
    api_response = api_instance.get_portfolio_properties(scope, code, effective_at=effective_at, as_at=as_at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfoliosApi->get_portfolio_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio to list the properties for. | 
 **code** | **str**| The code of the portfolio to list the properties for. Together with the scope this uniquely              identifies the portfolio. | 
 **effective_at** | **str**| The effective datetime at which to list the portfolio&#39;s properties. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the portfolio&#39;s properties. Defaults to return the latest version of each property if not specified. | [optional] 

### Return type

[**PortfolioProperties**](PortfolioProperties.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_portfolios**
> ResourceListOfPortfolio list_portfolios(effective_at=effective_at, as_at=as_at, page=page, start=start, limit=limit, filter=filter, query=query, portfolio_property_keys=portfolio_property_keys)

[EARLY ACCESS] List portfolios

List all the portfolios matching the specified criteria.

### Example

```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lusid.PortfoliosApi()
effective_at = 'effective_at_example' # str | The effective datetime at which to list the portfolios. Defaults to the current LUSID              system datetime if not specified. (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the portfolios. Defaults to return the latest version              of each portfolio if not specified. (optional)
page = 'page_example' # str | The pagination token to use to continue listing portfolios from a previous call to list portfolios. This  value is returned from the previous call. If a pagination token is provided the filter, effectiveAt  and asAt fields must not have changed since the original request. Also, if set, a start value cannot be provided. (optional)
start = 56 # int | When paginating, skip this number of results. (optional)
limit = 56 # int | When paginating, limit the number of returned results to this many. Defaults to 65,535 if not specified. (optional)
filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)
query = 'query_example' # str | Expression specifying the criteria that the returned portfolios must meet e.g. to see which              portfolios have holdings in the instruments with a Lusid Instrument Id (LUID) of 'LUID_PPA8HI6M' or a Figi of 'BBG000BLNNH6'              you would specify \"instrument.identifiers in (('LusidInstrumentId', 'LUID_PPA8HI6M'), ('Figi', 'BBG000BLNNH6'))\". (optional)
portfolio_property_keys = ['portfolio_property_keys_example'] # list[str] | A list of property keys from the \"Portfolio\" domain to decorate onto each portfolio.              These take the format {domain}/{scope}/{code} e.g. \"Portfolio/Manager/Id\". (optional)

try:
    # [EARLY ACCESS] List portfolios
    api_response = api_instance.list_portfolios(effective_at=effective_at, as_at=as_at, page=page, start=start, limit=limit, filter=filter, query=query, portfolio_property_keys=portfolio_property_keys)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfoliosApi->list_portfolios: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **effective_at** | **str**| The effective datetime at which to list the portfolios. Defaults to the current LUSID              system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the portfolios. Defaults to return the latest version              of each portfolio if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing portfolios from a previous call to list portfolios. This  value is returned from the previous call. If a pagination token is provided the filter, effectiveAt  and asAt fields must not have changed since the original request. Also, if set, a start value cannot be provided. | [optional] 
 **start** | **int**| When paginating, skip this number of results. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 65,535 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **query** | **str**| Expression specifying the criteria that the returned portfolios must meet e.g. to see which              portfolios have holdings in the instruments with a Lusid Instrument Id (LUID) of &#39;LUID_PPA8HI6M&#39; or a Figi of &#39;BBG000BLNNH6&#39;              you would specify \&quot;instrument.identifiers in ((&#39;LusidInstrumentId&#39;, &#39;LUID_PPA8HI6M&#39;), (&#39;Figi&#39;, &#39;BBG000BLNNH6&#39;))\&quot;. | [optional] 
 **portfolio_property_keys** | [**list[str]**](str.md)| A list of property keys from the \&quot;Portfolio\&quot; domain to decorate onto each portfolio.              These take the format {domain}/{scope}/{code} e.g. \&quot;Portfolio/Manager/Id\&quot;. | [optional] 

### Return type

[**ResourceListOfPortfolio**](ResourceListOfPortfolio.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_portfolios_for_scope**
> ResourceListOfPortfolio list_portfolios_for_scope(scope, effective_at=effective_at, as_at=as_at, filter=filter, portfolio_property_keys=portfolio_property_keys)

[EARLY ACCESS] List portfolios for scope

List all the portfolios in a single scope.

### Example

```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lusid.PortfoliosApi()
scope = 'scope_example' # str | The scope of the portfolios.
effective_at = 'effective_at_example' # str | The effective datetime at which to list the portfolios. Defaults to the current LUSID              system datetime if not specified. (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the portfolios. Defaults to return the latest version              of each portfolio if not specified. (optional)
filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)
portfolio_property_keys = ['portfolio_property_keys_example'] # list[str] | A list of property keys from the \"Portfolio\" domain to decorate onto each portfolio.              These take the format {domain}/{scope}/{code} e.g. \"Portfolio/Manager/Id\". (optional)

try:
    # [EARLY ACCESS] List portfolios for scope
    api_response = api_instance.list_portfolios_for_scope(scope, effective_at=effective_at, as_at=as_at, filter=filter, portfolio_property_keys=portfolio_property_keys)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfoliosApi->list_portfolios_for_scope: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolios. | 
 **effective_at** | **str**| The effective datetime at which to list the portfolios. Defaults to the current LUSID              system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the portfolios. Defaults to return the latest version              of each portfolio if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **portfolio_property_keys** | [**list[str]**](str.md)| A list of property keys from the \&quot;Portfolio\&quot; domain to decorate onto each portfolio.              These take the format {domain}/{scope}/{code} e.g. \&quot;Portfolio/Manager/Id\&quot;. | [optional] 

### Return type

[**ResourceListOfPortfolio**](ResourceListOfPortfolio.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_portfolio**
> Portfolio update_portfolio(scope, code, effective_at=effective_at, request=request)

[EARLY ACCESS] Update portfolio

Update the definition of a single portfolio. Not all elements within a portfolio definition are  modifiable due to the potential implications for data already stored against the portfolio.

### Example

```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lusid.PortfoliosApi()
scope = 'scope_example' # str | The scope of the portfolio to update the definition for.
code = 'code_example' # str | The code of the portfolio to update the definition for. Together with the scope this uniquely              identifies the portfolio.
effective_at = 'effective_at_example' # str | The effective datetime at which to update the definition. Defaults to the current              LUSID system datetime if not specified. (optional)
request = lusid.UpdatePortfolioRequest() # UpdatePortfolioRequest | The updated portfolio definition. (optional)

try:
    # [EARLY ACCESS] Update portfolio
    api_response = api_instance.update_portfolio(scope, code, effective_at=effective_at, request=request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfoliosApi->update_portfolio: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio to update the definition for. | 
 **code** | **str**| The code of the portfolio to update the definition for. Together with the scope this uniquely              identifies the portfolio. | 
 **effective_at** | **str**| The effective datetime at which to update the definition. Defaults to the current              LUSID system datetime if not specified. | [optional] 
 **request** | [**UpdatePortfolioRequest**](UpdatePortfolioRequest.md)| The updated portfolio definition. | [optional] 

### Return type

[**Portfolio**](Portfolio.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_portfolio_properties**
> PortfolioProperties upsert_portfolio_properties(scope, code, portfolio_properties=portfolio_properties)

[EARLY ACCESS] Upsert portfolio properties

Update or insert one or more properties onto a single portfolio. A property will be updated if it  already exists and inserted if it does not. All properties must be of the domain 'Portfolio'.

### Example

```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lusid.PortfoliosApi()
scope = 'scope_example' # str | The scope of the portfolio to update or insert the properties onto.
code = 'code_example' # str | The code of the portfolio to update or insert the properties onto. Together with the scope              this uniquely identifies the portfolio.
portfolio_properties = {'key': lusid.ModelProperty()} # dict(str, ModelProperty) | The properties to be updated or inserted onto the portfolio. Each property in              the request must be keyed by its unique property key. This has the format {domain}/{scope}/{code} e.g. \"Portfolio/Manager/Id\". (optional)

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
 **scope** | **str**| The scope of the portfolio to update or insert the properties onto. | 
 **code** | **str**| The code of the portfolio to update or insert the properties onto. Together with the scope              this uniquely identifies the portfolio. | 
 **portfolio_properties** | [**dict(str, ModelProperty)**](ModelProperty.md)| The properties to be updated or inserted onto the portfolio. Each property in              the request must be keyed by its unique property key. This has the format {domain}/{scope}/{code} e.g. \&quot;Portfolio/Manager/Id\&quot;. | [optional] 

### Return type

[**PortfolioProperties**](PortfolioProperties.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

