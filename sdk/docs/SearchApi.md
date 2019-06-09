# lusid.SearchApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**instruments_search**](SearchApi.md#instruments_search) | **POST** /api/search/instruments | Search instruments
[**portfolio_groups_search**](SearchApi.md#portfolio_groups_search) | **POST** /api/search/portfoliogroups | Search portfolio groups
[**portfolios_search**](SearchApi.md#portfolios_search) | **POST** /api/search/portfolios | Search portfolios
[**properties_search**](SearchApi.md#properties_search) | **POST** /api/search/propertydefinitions | Search property definitions


# **instruments_search**
> list[InstrumentMatch] instruments_search(mastered_effective_at=mastered_effective_at, mastered_only=mastered_only, symbols=symbols)

Search instruments

Search through instruments that have been mastered in LUSID, and optionally augment results with instruments from a symbology service

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
api_instance = lusid.SearchApi(lusid.ApiClient(configuration))
mastered_effective_at = 'mastered_effective_at_example' # str | Optional. The effective date for searching mastered instruments. If this is not set, then the current date is taken.  This parameter has no effect on instruments that have not been mastered within LUSID. (optional)
mastered_only = False # bool | Optional. If set to true, only search over instruments that have been mastered within LUSID. Default to false (optional) (default to False)
symbols = None # list[InstrumentSearchProperty] | A collection of instrument symbols to search for (optional)

try:
    # Search instruments
    api_response = api_instance.instruments_search(mastered_effective_at=mastered_effective_at, mastered_only=mastered_only, symbols=symbols)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->instruments_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mastered_effective_at** | **str**| Optional. The effective date for searching mastered instruments. If this is not set, then the current date is taken.  This parameter has no effect on instruments that have not been mastered within LUSID. | [optional] 
 **mastered_only** | **bool**| Optional. If set to true, only search over instruments that have been mastered within LUSID. Default to false | [optional] [default to False]
 **symbols** | [**list[InstrumentSearchProperty]**](list.md)| A collection of instrument symbols to search for | [optional] 

### Return type

[**list[InstrumentMatch]**](InstrumentMatch.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portfolio_groups_search**
> ResourceListOfPortfolioGroup portfolio_groups_search(sort_by=sort_by, start=start, limit=limit, filter=filter, request=request)

Search portfolio groups

Search through all portfolio groups

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
api_instance = lusid.SearchApi(lusid.ApiClient(configuration))
sort_by = ['sort_by_example'] # list[str] | Optional. Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName (optional)
start = 56 # int | Optional. When paginating, skip this number of results (optional)
limit = 56 # int | Optional. When paginating, limit the number of returned results to this many. (optional)
filter = 'filter_example' # str | Optional. Expression to filter the result set (optional)
request = None # object | A valid Elasticsearch 5.x request (optional)

try:
    # Search portfolio groups
    api_response = api_instance.portfolio_groups_search(sort_by=sort_by, start=start, limit=limit, filter=filter, request=request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->portfolio_groups_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort_by** | [**list[str]**](str.md)| Optional. Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName | [optional] 
 **start** | **int**| Optional. When paginating, skip this number of results | [optional] 
 **limit** | **int**| Optional. When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Optional. Expression to filter the result set | [optional] 
 **request** | **object**| A valid Elasticsearch 5.x request | [optional] 

### Return type

[**ResourceListOfPortfolioGroup**](ResourceListOfPortfolioGroup.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portfolios_search**
> ResourceListOfPortfolioSearchResult portfolios_search(sort_by=sort_by, start=start, limit=limit, filter=filter, request=request)

Search portfolios

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

# create an instance of the API class
api_instance = lusid.SearchApi(lusid.ApiClient(configuration))
sort_by = ['sort_by_example'] # list[str] | Optional. Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName (optional)
start = 56 # int | Optional. When paginating, skip this number of results (optional)
limit = 56 # int | Optional. When paginating, limit the number of returned results to this many. (optional)
filter = 'filter_example' # str | Optional. Expression to filter the result set (optional)
request = None # object | A valid Elasticsearch 5.x request (optional)

try:
    # Search portfolios
    api_response = api_instance.portfolios_search(sort_by=sort_by, start=start, limit=limit, filter=filter, request=request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->portfolios_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort_by** | [**list[str]**](str.md)| Optional. Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName | [optional] 
 **start** | **int**| Optional. When paginating, skip this number of results | [optional] 
 **limit** | **int**| Optional. When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Optional. Expression to filter the result set | [optional] 
 **request** | **object**| A valid Elasticsearch 5.x request | [optional] 

### Return type

[**ResourceListOfPortfolioSearchResult**](ResourceListOfPortfolioSearchResult.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **properties_search**
> ResourceListOfPropertyDefinition properties_search(sort_by=sort_by, start=start, limit=limit, filter=filter, request=request)

Search property definitions

Search through all property definitions

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
api_instance = lusid.SearchApi(lusid.ApiClient(configuration))
sort_by = ['sort_by_example'] # list[str] | Optional. Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName (optional)
start = 56 # int | Optional. When paginating, skip this number of results (optional)
limit = 56 # int | Optional. When paginating, limit the number of returned results to this many. (optional)
filter = 'filter_example' # str | Optional. Expression to filter the result set (optional)
request = None # object | A valid Elasticsearch 5.x request (optional)

try:
    # Search property definitions
    api_response = api_instance.properties_search(sort_by=sort_by, start=start, limit=limit, filter=filter, request=request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->properties_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort_by** | [**list[str]**](str.md)| Optional. Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName | [optional] 
 **start** | **int**| Optional. When paginating, skip this number of results | [optional] 
 **limit** | **int**| Optional. When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Optional. Expression to filter the result set | [optional] 
 **request** | **object**| A valid Elasticsearch 5.x request | [optional] 

### Return type

[**ResourceListOfPropertyDefinition**](ResourceListOfPropertyDefinition.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

