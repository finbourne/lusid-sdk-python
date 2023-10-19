# lusid.AborApi

All URIs are relative to *https://fbn-prd.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_je_lines**](AborApi.md#get_je_lines) | **POST** /api/abor/{scope}/{code}/JELines/$query/$deprecated | [DEPRECATED] GetJELines: DEPRECATED: please use GetJournalEntryLines instead. Get the JELines for the given Abor.


# **get_je_lines**
> VersionedResourceListOfJournalEntryLine get_je_lines(scope, code, je_lines_query_parameters, as_at=as_at, limit=limit, page=page)

[DEPRECATED] GetJELines: DEPRECATED: please use GetJournalEntryLines instead. Get the JELines for the given Abor.

DEPRECATED: please use GetJournalEntryLines instead. Gets the JELines for the given Abor                The JE Lines have been generated from transactions and translated via posting rules

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-prd.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.AborApi(api_client)
    scope = 'scope_example' # str | The scope of the Abor.
code = 'code_example' # str | The code of the Abor. Together with the scope is creating the unique identifier for the given Abor.
je_lines_query_parameters = {"startDate":"2018-03-05T00:00:00.0000000+00:00","endDate":"2018-03-19T00:00:00.0000000+00:00","propertyKeys":[]} # JELinesQueryParameters | The query parameters used in running the generation of the JELines.
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve JELines. Defaults to returning the latest version               of each transaction if not specified. (optional)
limit = 56 # int | When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. (optional)
page = 'page_example' # str | The pagination token to use to continue listing JELines from a previous call to GetJELines. (optional)

    try:
        # [DEPRECATED] GetJELines: DEPRECATED: please use GetJournalEntryLines instead. Get the JELines for the given Abor.
        api_response = api_instance.get_je_lines(scope, code, je_lines_query_parameters, as_at=as_at, limit=limit, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AborApi->get_je_lines: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Abor. | 
 **code** | **str**| The code of the Abor. Together with the scope is creating the unique identifier for the given Abor. | 
 **je_lines_query_parameters** | [**JELinesQueryParameters**](JELinesQueryParameters.md)| The query parameters used in running the generation of the JELines. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve JELines. Defaults to returning the latest version               of each transaction if not specified. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing JELines from a previous call to GetJELines. | [optional] 

### Return type

[**VersionedResourceListOfJournalEntryLine**](VersionedResourceListOfJournalEntryLine.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested JELines for the specified Abor. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

