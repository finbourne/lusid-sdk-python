# lusid.ScopesApi

All URIs are relative to *https://fbn-ci.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_scopes**](ScopesApi.md#list_scopes) | **GET** /api/scopes | ListScopes: List Scopes


# **list_scopes**
> ResourceListOfScopeDefinition list_scopes(filter=filter)

ListScopes: List Scopes

List all the scopes that contain data.

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
    api_instance = lusid.ScopesApi(api_client)
    filter = 'filter_example' # str | Expression to filter the result set.              For example, to filter on the Scope, use \"scope eq 'string'\"              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)

    try:
        # ListScopes: List Scopes
        api_response = await api_instance.list_scopes(filter=filter)
        print("The response of ScopesApi->list_scopes:\n")
        pprint(api_response)
    except Exception as e:
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

