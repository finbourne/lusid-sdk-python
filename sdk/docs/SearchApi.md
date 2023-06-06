# lusid.SearchApi

All URIs are relative to *https://fbn-ci.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**instruments_search**](SearchApi.md#instruments_search) | **POST** /api/search/instruments | [EARLY ACCESS] InstrumentsSearch: Instruments search
[**search_portfolio_groups**](SearchApi.md#search_portfolio_groups) | **GET** /api/search/portfoliogroups | SearchPortfolioGroups: Search Portfolio Groups
[**search_portfolios**](SearchApi.md#search_portfolios) | **GET** /api/search/portfolios | SearchPortfolios: Search Portfolios
[**search_properties**](SearchApi.md#search_properties) | **GET** /api/search/propertydefinitions | SearchProperties: Search Property Definitions


# **instruments_search**
> List[InstrumentMatch] instruments_search(instrument_search_property, mastered_effective_at=mastered_effective_at, mastered_only=mastered_only, scope=scope)

[EARLY ACCESS] InstrumentsSearch: Instruments search

Search across all instruments that have been mastered in LUSID. Optionally augment the results with instruments from an external symbology service,  currently OpenFIGI.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-ci.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.SearchApi(api_client)
    instrument_search_property = [{"key":"Instrument/default/Isin","value":"US0378331005"}] # List[InstrumentSearchProperty] | A collection of instrument properties to search for. LUSID will return instruments for any matched              properties.
    mastered_effective_at = 'mastered_effective_at_example' # str | The effective datetime or cut label to use when searching mastered instruments. This parameter has no effect on instruments that  have not been mastered within LUSID. Defaults to the current LUSID system datetime if not specified. (optional)
    mastered_only = False # bool | If set to true, only search over instruments that have been mastered within LUSID. Defaults to false. (optional) (default to False)
    scope = 'scope_example' # str | The scope in which the instrument lies. (optional)

    try:
        # [EARLY ACCESS] InstrumentsSearch: Instruments search
        api_response = await api_instance.instruments_search(instrument_search_property, mastered_effective_at=mastered_effective_at, mastered_only=mastered_only, scope=scope)
        print("The response of SearchApi->instruments_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->instruments_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instrument_search_property** | [**List[InstrumentSearchProperty]**](InstrumentSearchProperty.md)| A collection of instrument properties to search for. LUSID will return instruments for any matched              properties. | 
 **mastered_effective_at** | **str**| The effective datetime or cut label to use when searching mastered instruments. This parameter has no effect on instruments that  have not been mastered within LUSID. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **mastered_only** | **bool**| If set to true, only search over instruments that have been mastered within LUSID. Defaults to false. | [optional] [default to False]
 **scope** | **str**| The scope in which the instrument lies. | [optional] 

### Return type

[**List[InstrumentMatch]**](InstrumentMatch.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The instruments found by the search |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_portfolio_groups**
> PagedResourceListOfPortfolioGroupSearchResult search_portfolio_groups(search=search, filter=filter, sort_by=sort_by, limit=limit, page=page)

SearchPortfolioGroups: Search Portfolio Groups

Search through all portfolio groups

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-ci.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.SearchApi(api_client)
    search = 'search_example' # str | A parameter used for searching any portfolio group field. Wildcards(*) are supported at the end of words (e.g. 'Port*'). Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)
    filter = 'filter_example' # str | Expression to filter the result set.   For example, to filter on the Scope, use \"id.scope eq 'string'\"  Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)
    sort_by = 'sort_by_example' # str | Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName. Multiple fields can be denoted by a comma e.g. -MyFieldName,AnotherFieldName,-AFurtherFieldName (optional)
    limit = 56 # int | When paginating, only return this number of records (optional)
    page = 'page_example' # str | Encoded page string returned from a previous search result that will retrieve the next page of data. When this field is supplied, filter, sortBy and search fields should not be supplied. (optional)

    try:
        # SearchPortfolioGroups: Search Portfolio Groups
        api_response = await api_instance.search_portfolio_groups(search=search, filter=filter, sort_by=sort_by, limit=limit, page=page)
        print("The response of SearchApi->search_portfolio_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search_portfolio_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| A parameter used for searching any portfolio group field. Wildcards(*) are supported at the end of words (e.g. &#39;Port*&#39;). Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **filter** | **str**| Expression to filter the result set.   For example, to filter on the Scope, use \&quot;id.scope eq &#39;string&#39;\&quot;  Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **sort_by** | **str**| Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName. Multiple fields can be denoted by a comma e.g. -MyFieldName,AnotherFieldName,-AFurtherFieldName | [optional] 
 **limit** | **int**| When paginating, only return this number of records | [optional] 
 **page** | **str**| Encoded page string returned from a previous search result that will retrieve the next page of data. When this field is supplied, filter, sortBy and search fields should not be supplied. | [optional] 

### Return type

[**PagedResourceListOfPortfolioGroupSearchResult**](PagedResourceListOfPortfolioGroupSearchResult.md)

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

# **search_portfolios**
> PagedResourceListOfPortfolioSearchResult search_portfolios(search=search, filter=filter, sort_by=sort_by, limit=limit, page=page)

SearchPortfolios: Search Portfolios

Search through all portfolios

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-ci.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.SearchApi(api_client)
    search = 'search_example' # str | A parameter used for searching any portfolio field. Wildcards(*) are supported at the end of words (e.g. 'Port*'). Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)
    filter = 'filter_example' # str | Expression to filter the result set.   For example, to filter on the portfolio Type, use \"type eq 'Transaction'\"  Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)
    sort_by = 'sort_by_example' # str | Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName. Multiple fields can be denoted by a comma e.g. -MyFieldName,AnotherFieldName,-AFurtherFieldName (optional)
    limit = 56 # int | When paginating, only return this number of records (optional)
    page = 'page_example' # str | Encoded page string returned from a previous search result that will retrieve the next page of data. When this field is supplied, filter, sortBy and search fields should not be supplied. (optional)

    try:
        # SearchPortfolios: Search Portfolios
        api_response = await api_instance.search_portfolios(search=search, filter=filter, sort_by=sort_by, limit=limit, page=page)
        print("The response of SearchApi->search_portfolios:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search_portfolios: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| A parameter used for searching any portfolio field. Wildcards(*) are supported at the end of words (e.g. &#39;Port*&#39;). Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **filter** | **str**| Expression to filter the result set.   For example, to filter on the portfolio Type, use \&quot;type eq &#39;Transaction&#39;\&quot;  Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **sort_by** | **str**| Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName. Multiple fields can be denoted by a comma e.g. -MyFieldName,AnotherFieldName,-AFurtherFieldName | [optional] 
 **limit** | **int**| When paginating, only return this number of records | [optional] 
 **page** | **str**| Encoded page string returned from a previous search result that will retrieve the next page of data. When this field is supplied, filter, sortBy and search fields should not be supplied. | [optional] 

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
> PagedResourceListOfPropertyDefinitionSearchResult search_properties(search=search, filter=filter, sort_by=sort_by, limit=limit, page=page)

SearchProperties: Search Property Definitions

Search through all Property Definitions

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-ci.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.SearchApi(api_client)
    search = 'search_example' # str | A parameter used for searching any field. Wildcards(*) are supported at the end of words (e.g. 'Port*'). Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)
    filter = 'filter_example' # str | Expression to filter the result set.   For example, to filter on the Value Type, use \"valueType eq 'string'\"  Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)
    sort_by = 'sort_by_example' # str | Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName. Multiple fields can be denoted by a comma e.g. -MyFieldName,AnotherFieldName,-AFurtherFieldName (optional)
    limit = 56 # int | When paginating, only return this number of records (optional)
    page = 'page_example' # str | Encoded page string returned from a previous search result that will retrieve the next page of data. When this field is supplied, filter, sortBy and search fields should not be supplied. (optional)

    try:
        # SearchProperties: Search Property Definitions
        api_response = await api_instance.search_properties(search=search, filter=filter, sort_by=sort_by, limit=limit, page=page)
        print("The response of SearchApi->search_properties:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| A parameter used for searching any field. Wildcards(*) are supported at the end of words (e.g. &#39;Port*&#39;). Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **filter** | **str**| Expression to filter the result set.   For example, to filter on the Value Type, use \&quot;valueType eq &#39;string&#39;\&quot;  Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **sort_by** | **str**| Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName. Multiple fields can be denoted by a comma e.g. -MyFieldName,AnotherFieldName,-AFurtherFieldName | [optional] 
 **limit** | **int**| When paginating, only return this number of records | [optional] 
 **page** | **str**| Encoded page string returned from a previous search result that will retrieve the next page of data. When this field is supplied, filter, sortBy and search fields should not be supplied. | [optional] 

### Return type

[**PagedResourceListOfPropertyDefinitionSearchResult**](PagedResourceListOfPropertyDefinitionSearchResult.md)

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

