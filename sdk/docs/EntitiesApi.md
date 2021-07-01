# lusid.EntitiesApi

All URIs are relative to *http://local-unit-test-server.lusid.com:33044*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_portfolio_changes**](EntitiesApi.md#get_portfolio_changes) | **GET** /api/entities/changes/portfolios | [EARLY ACCESS] Get the next change to each portfolio in a scope.


# **get_portfolio_changes**
> ResourceListOfChange get_portfolio_changes(scope, effective_at, as_at=as_at)

[EARLY ACCESS] Get the next change to each portfolio in a scope.

Gets the time of the next (earliest effective at) modification (correction and/or amendment) to each portfolio in a scope relative to a point in bitemporal time.  Includes changes from parent portfolios in different scopes.  Excludes changes from subcriptions (e.g corporate actions).

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

# Defining host is optional and default to http://local-unit-test-server.lusid.com:33044
configuration.host = "http://local-unit-test-server.lusid.com:33044"
# Create an instance of the API class
api_instance = lusid.EntitiesApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope
effective_at = 'effective_at_example' # str | The effective date of the origin.
as_at = '2013-10-20T19:20:30+01:00' # datetime | The as-at date of the origin. (optional)

try:
    # [EARLY ACCESS] Get the next change to each portfolio in a scope.
    api_response = api_instance.get_portfolio_changes(scope, effective_at, as_at=as_at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntitiesApi->get_portfolio_changes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope | 
 **effective_at** | **str**| The effective date of the origin. | 
 **as_at** | **datetime**| The as-at date of the origin. | [optional] 

### Return type

[**ResourceListOfChange**](ResourceListOfChange.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | The details of the input related failure |  -  |
**200** | A list of portfolio changes in the requested scope relative to the specified time. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

