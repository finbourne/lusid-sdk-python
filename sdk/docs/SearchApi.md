# lusid.SearchApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**instruments_search**](SearchApi.md#instruments_search) | **POST** /api/search/instruments | [EXPERIMENTAL] Instruments search
[**portfolio_groups_search**](SearchApi.md#portfolio_groups_search) | **POST** /api/search/portfoliogroups | [EXPERIMENTAL] Portfolio groups search
[**portfolios_search**](SearchApi.md#portfolios_search) | **POST** /api/search/portfolios | [EXPERIMENTAL] [DEPRECATED] Portfolios search
[**properties_search**](SearchApi.md#properties_search) | **POST** /api/search/propertydefinitions | [EXPERIMENTAL] [DEPRECATED] Search property definitions
[**search_portfolios**](SearchApi.md#search_portfolios) | **GET** /api/search/portfolios | [EXPERIMENTAL] Search Portfolios
[**search_properties**](SearchApi.md#search_properties) | **GET** /api/search/propertydefinitions | [EXPERIMENTAL] Search Property Definitions


# **instruments_search**
> list[InstrumentMatch] instruments_search(symbols, mastered_effective_at=mastered_effective_at, mastered_only=mastered_only)

[EXPERIMENTAL] Instruments search

Search across all instruments that have been mastered in LUSID. Optionally augment the results with instruments from an external symbology service,  currently OpenFIGI.

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

# Defining host is optional and default to http://localhost/api
configuration.host = "http://localhost/api"
# Create an instance of the API class
api_instance = lusid.SearchApi(lusid.ApiClient(configuration))
symbols = [lusid.InstrumentSearchProperty()] # list[InstrumentSearchProperty] | A collection of instrument properties to search for. LUSID will return instruments for any matched              properties.
mastered_effective_at = 'mastered_effective_at_example' # str | The effective datetime or cut label to use when searching mastered instruments. This parameter has no effect on instruments that  have not been mastered within LUSID. Defaults to the current LUSID system datetime if not specified. (optional)
mastered_only = False # bool | If set to true, only search over instruments that have been mastered within LUSID. Defaults to false. (optional) (default to False)

try:
    # [EXPERIMENTAL] Instruments search
    api_response = api_instance.instruments_search(symbols, mastered_effective_at=mastered_effective_at, mastered_only=mastered_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->instruments_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbols** | [**list[InstrumentSearchProperty]**](InstrumentSearchProperty.md)| A collection of instrument properties to search for. LUSID will return instruments for any matched              properties. | 
 **mastered_effective_at** | **str**| The effective datetime or cut label to use when searching mastered instruments. This parameter has no effect on instruments that  have not been mastered within LUSID. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **mastered_only** | **bool**| If set to true, only search over instruments that have been mastered within LUSID. Defaults to false. | [optional] [default to False]

### Return type

[**list[InstrumentMatch]**](InstrumentMatch.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The instruments found by the search |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portfolio_groups_search**
> ResourceListOfPortfolioGroup portfolio_groups_search(request, filter=filter)

[EXPERIMENTAL] Portfolio groups search

Search across all portfolio groups across all scopes.

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

# Defining host is optional and default to http://localhost/api
configuration.host = "http://localhost/api"
# Create an instance of the API class
api_instance = lusid.SearchApi(lusid.ApiClient(configuration))
request = None # object | The search query to use. Read more about search queries in LUSID here https://support.lusid.com/constructing-a-search-request.
filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)

try:
    # [EXPERIMENTAL] Portfolio groups search
    api_response = api_instance.portfolio_groups_search(request, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->portfolio_groups_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | **object**| The search query to use. Read more about search queries in LUSID here https://support.lusid.com/constructing-a-search-request. | 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 

### Return type

[**ResourceListOfPortfolioGroup**](ResourceListOfPortfolioGroup.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The portfolio groups found by the search |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portfolios_search**
> ResourceListOfPortfolioSearchResult portfolios_search(request, filter=filter)

[EXPERIMENTAL] [DEPRECATED] Portfolios search

Search across all portfolios across all scopes.

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

# Defining host is optional and default to http://localhost/api
configuration.host = "http://localhost/api"
# Create an instance of the API class
api_instance = lusid.SearchApi(lusid.ApiClient(configuration))
request = None # object | The search query to use. Read more about search queries in LUSID here https://support.lusid.com/constructing-a-search-request.
filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)

try:
    # [EXPERIMENTAL] [DEPRECATED] Portfolios search
    api_response = api_instance.portfolios_search(request, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->portfolios_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | **object**| The search query to use. Read more about search queries in LUSID here https://support.lusid.com/constructing-a-search-request. | 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 

### Return type

[**ResourceListOfPortfolioSearchResult**](ResourceListOfPortfolioSearchResult.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The portfolios found by the search |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **properties_search**
> ResourceListOfPropertyDefinition properties_search(request, filter=filter)

[EXPERIMENTAL] [DEPRECATED] Search property definitions

Search across all user defined property definitions across all scopes.

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

# Defining host is optional and default to http://localhost/api
configuration.host = "http://localhost/api"
# Create an instance of the API class
api_instance = lusid.SearchApi(lusid.ApiClient(configuration))
request = None # object | The search query to use. Read more about search queries in LUSID here https://support.lusid.com/constructing-a-search-request.
filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)

try:
    # [EXPERIMENTAL] [DEPRECATED] Search property definitions
    api_response = api_instance.properties_search(request, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->properties_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | **object**| The search query to use. Read more about search queries in LUSID here https://support.lusid.com/constructing-a-search-request. | 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 

### Return type

[**ResourceListOfPropertyDefinition**](ResourceListOfPropertyDefinition.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The property definitions found by the search |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_portfolios**
> PagedResourceListOfPortfolioSearchResult search_portfolios(search=search, filter=filter, sort_by=sort_by, limit=limit, page=page)

[EXPERIMENTAL] Search Portfolios

Search through all portfolios

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

# Defining host is optional and default to http://localhost/api
configuration.host = "http://localhost/api"
# Create an instance of the API class
api_instance = lusid.SearchApi(lusid.ApiClient(configuration))
search = 'search_example' # str | A parameter used for searching any portfolio field. Wildcards(*) are supported at the end of words (e.g. 'Port*'). See <see href=\"https://support.lusid.com/filtering-results-from-lusid\"> filtering results from LUSID </see> for more details. (optional)
filter = 'filter_example' # str | Expression to filter the result set. Read more about <see href=\"https://support.lusid.com/filtering-results-from-lusid\"> filtering results from LUSID</see>. (optional)
sort_by = 'sort_by_example' # str | Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName. Multiple fields can be denoted by a comma e.g. -MyFieldName,AnotherFieldName,-AFurtherFieldName (optional)
limit = 56 # int | When paginating, only return this number of records (optional)
page = 'page_example' # str | Encoded page string returned from a previous search result that will retrieve the next page of data. When this field is supplied, filter, sortby and search fields should not be supplied. (optional)

try:
    # [EXPERIMENTAL] Search Portfolios
    api_response = api_instance.search_portfolios(search=search, filter=filter, sort_by=sort_by, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_portfolios: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| A parameter used for searching any portfolio field. Wildcards(*) are supported at the end of words (e.g. &#39;Port*&#39;). See &lt;see href&#x3D;\&quot;https://support.lusid.com/filtering-results-from-lusid\&quot;&gt; filtering results from LUSID &lt;/see&gt; for more details. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about &lt;see href&#x3D;\&quot;https://support.lusid.com/filtering-results-from-lusid\&quot;&gt; filtering results from LUSID&lt;/see&gt;. | [optional] 
 **sort_by** | **str**| Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName. Multiple fields can be denoted by a comma e.g. -MyFieldName,AnotherFieldName,-AFurtherFieldName | [optional] 
 **limit** | **int**| When paginating, only return this number of records | [optional] 
 **page** | **str**| Encoded page string returned from a previous search result that will retrieve the next page of data. When this field is supplied, filter, sortby and search fields should not be supplied. | [optional] 

### Return type

[**PagedResourceListOfPortfolioSearchResult**](PagedResourceListOfPortfolioSearchResult.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_properties**
> PagedResourceListOfPropertyDefinition search_properties(search=search, filter=filter, sort_by=sort_by, limit=limit, page=page)

[EXPERIMENTAL] Search Property Definitions

Search through all Property Definitions

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

# Defining host is optional and default to http://localhost/api
configuration.host = "http://localhost/api"
# Create an instance of the API class
api_instance = lusid.SearchApi(lusid.ApiClient(configuration))
search = 'search_example' # str | A parameter used for searching any field. Wildcards(*) are supported at the end of words (e.g. 'Port*'). See <see href=\"https://support.lusid.com/filtering-results-from-lusid\"> filtering results from LUSID </see> for more details. (optional)
filter = 'filter_example' # str | Expression to filter the result set. Read more about <see href=\"https://support.lusid.com/filtering-results-from-lusid\"> filtering results from LUSID</see>. (optional)
sort_by = 'sort_by_example' # str | Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName. Multiple fields can be denoted by a comma e.g. -MyFieldName,AnotherFieldName,-AFurtherFieldName (optional)
limit = 56 # int | When paginating, only return this number of records (optional)
page = 'page_example' # str | Encoded page string returned from a previous search result that will retrieve the next page of data. When this field is supplied, filter, sortby and search fields should not be supplied. (optional)

try:
    # [EXPERIMENTAL] Search Property Definitions
    api_response = api_instance.search_properties(search=search, filter=filter, sort_by=sort_by, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| A parameter used for searching any field. Wildcards(*) are supported at the end of words (e.g. &#39;Port*&#39;). See &lt;see href&#x3D;\&quot;https://support.lusid.com/filtering-results-from-lusid\&quot;&gt; filtering results from LUSID &lt;/see&gt; for more details. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about &lt;see href&#x3D;\&quot;https://support.lusid.com/filtering-results-from-lusid\&quot;&gt; filtering results from LUSID&lt;/see&gt;. | [optional] 
 **sort_by** | **str**| Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName. Multiple fields can be denoted by a comma e.g. -MyFieldName,AnotherFieldName,-AFurtherFieldName | [optional] 
 **limit** | **int**| When paginating, only return this number of records | [optional] 
 **page** | **str**| Encoded page string returned from a previous search result that will retrieve the next page of data. When this field is supplied, filter, sortby and search fields should not be supplied. | [optional] 

### Return type

[**PagedResourceListOfPropertyDefinition**](PagedResourceListOfPropertyDefinition.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

