# lusid.QuotesApi

All URIs are relative to *http://localhost:60161*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_quotes**](QuotesApi.md#list_quotes) | **GET** /api/quotes/{scope}/$deprecated | [DEPRECATED] List quotes


# **list_quotes**
> ResourceListOfQuote list_quotes(scope, as_at=as_at, page=page, start=start, limit=limit, filter=filter)

[DEPRECATED] List quotes

List all the quotes from a single scope at the specified date/time  Please use M:Finbourne.WebApi.Controllers.QuotesController.ListQuotesForScope(System.String,System.Nullable{System.DateTimeOffset},System.String,System.Nullable{System.Int32},System.Nullable{System.Int32},System.String) - the signature and behaviour of this endpoint will be changing to omit scope

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

# Defining host is optional and default to http://localhost:60161
configuration.host = "http://localhost:60161"
# Create an instance of the API class
api_instance = lusid.QuotesApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the quotes to list.
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the quotes. Defaults to latest if not specified. (optional)
page = 'page_example' # str | The pagination token to use to continue listing quotes from a previous call to list quotes.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields              must not have changed since the original request. Also, if set, a start value cannot be provided. (optional)
start = 56 # int | When paginating, skip this number of results. (optional)
limit = 56 # int | When paginating, limit the number of returned results to this many. (optional)
filter = 'filter_example' # str | Expression to filter the result set.              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)

try:
    # [DEPRECATED] List quotes
    api_response = api_instance.list_quotes(scope, as_at=as_at, page=page, start=start, limit=limit, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotesApi->list_quotes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the quotes to list. | 
 **as_at** | **datetime**| The asAt datetime at which to list the quotes. Defaults to latest if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing quotes from a previous call to list quotes.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields              must not have changed since the original request. Also, if set, a start value cannot be provided. | [optional] 
 **start** | **int**| When paginating, skip this number of results. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Expression to filter the result set.              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 

### Return type

[**ResourceListOfQuote**](ResourceListOfQuote.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested quotes |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

