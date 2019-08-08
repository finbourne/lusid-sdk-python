# lusid.ScopesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_scopes**](ScopesApi.md#list_scopes) | **GET** /api/scopes | [EARLY ACCESS] List scopes


# **list_scopes**
> ResourceListOfScopeDefinition list_scopes(filter=filter)

[EARLY ACCESS] List scopes

List all the scopes that contain data.

### Example

```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lusid.ScopesApi()
filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)

try:
    # [EARLY ACCESS] List scopes
    api_response = api_instance.list_scopes(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScopesApi->list_scopes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 

### Return type

[**ResourceListOfScopeDefinition**](ResourceListOfScopeDefinition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

