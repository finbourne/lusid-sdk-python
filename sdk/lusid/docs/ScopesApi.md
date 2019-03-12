# lusid.ScopesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_scopes**](ScopesApi.md#list_scopes) | **GET** /api/scopes | List scopes


# **list_scopes**
> ResourceListOfScopeDefinition list_scopes(sort_by=sort_by, start=start, limit=limit, filter=filter, query=query)

List scopes

List all the scopes

### Example

* OAuth Authentication (oauth2): 
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = lusid.ScopesApi(lusid.ApiClient(configuration))
sort_by = ['sort_by_example'] # list[str] | Optional. Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName (optional)
start = 56 # int | Optional. When paginating, skip this number of results (optional)
limit = 56 # int | Optional. When paginating, limit the number of returned results to this many. (optional)
filter = 'filter_example' # str | Optional. Expression to filter the result set (optional)
query = 'query_example' # str | Optional. Expression specifying the criteria that the returned portfolios must meet (optional)

try:
    # List scopes
    api_response = api_instance.list_scopes(sort_by=sort_by, start=start, limit=limit, filter=filter, query=query)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScopesApi->list_scopes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort_by** | [**list[str]**](str.md)| Optional. Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName | [optional] 
 **start** | **int**| Optional. When paginating, skip this number of results | [optional] 
 **limit** | **int**| Optional. When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Optional. Expression to filter the result set | [optional] 
 **query** | **str**| Optional. Expression specifying the criteria that the returned portfolios must meet | [optional] 

### Return type

[**ResourceListOfScopeDefinition**](ResourceListOfScopeDefinition.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

