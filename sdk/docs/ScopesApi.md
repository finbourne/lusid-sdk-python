# lusid.ScopesApi

All URIs are relative to *http://local-unit-test-server.lusid.com:31406*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_scopes**](ScopesApi.md#list_scopes) | **GET** /api/scopes | [EARLY ACCESS] List Scopes


# **list_scopes**
> ResourceListOfScopeDefinition list_scopes(filter=filter)

[EARLY ACCESS] List Scopes

List all the scopes that contain data.

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

# Defining host is optional and default to http://local-unit-test-server.lusid.com:31406
configuration.host = "http://local-unit-test-server.lusid.com:31406"
# Create an instance of the API class
api_instance = lusid.ScopesApi(lusid.ApiClient(configuration))
filter = 'filter_example' # str | Expression to filter the result set.              For example, to filter on the Scope, use \"scope eq 'string'\"              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)

try:
    # [EARLY ACCESS] List Scopes
    api_response = api_instance.list_scopes(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScopesApi->list_scopes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Expression to filter the result set.              For example, to filter on the Scope, use \&quot;scope eq &#39;string&#39;\&quot;              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 

### Return type

[**ResourceListOfScopeDefinition**](ResourceListOfScopeDefinition.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of scopes |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

