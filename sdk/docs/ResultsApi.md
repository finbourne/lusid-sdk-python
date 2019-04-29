# lusid.ResultsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_results**](ResultsApi.md#get_results) | **GET** /api/results/{entityScope}/{entityCode}/{calculationScope}/{calculationCode}/{effectiveAt} | Retrieve a page of results all keyed by the provided parameters. The result store is not bi-temporal; a single date  addressed the market effectiveAt.
[**upsert_results**](ResultsApi.md#upsert_results) | **POST** /api/results | Upsert results


# **get_results**
> Results get_results(entity_scope, entity_code, calculation_scope, calculation_code, effective_at)

Retrieve a page of results all keyed by the provided parameters. The result store is not bi-temporal; a single date  addressed the market effectiveAt.

Retrieve pre-calculated results that have been stored in LUSID.

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
api_instance = lusid.ResultsApi(lusid.ApiClient(configuration))
entity_scope = 'entity_scope_example' # str | The scope of the data or entity being stored
entity_code = 'entity_code_example' # str | The identifier for the data or results entity being stored
calculation_scope = 'calculation_scope_example' # str | The identifying scope for the calculation that produced the result
calculation_code = 'calculation_code_example' # str | The identifying calculation name for the results
effective_at = '2013-10-20T19:20:30+01:00' # datetime | The market date for which the data is stored

try:
    # Retrieve a page of results all keyed by the provided parameters. The result store is not bi-temporal; a single date  addressed the market effectiveAt.
    api_response = api_instance.get_results(entity_scope, entity_code, calculation_scope, calculation_code, effective_at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResultsApi->get_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_scope** | **str**| The scope of the data or entity being stored | 
 **entity_code** | **str**| The identifier for the data or results entity being stored | 
 **calculation_scope** | **str**| The identifying scope for the calculation that produced the result | 
 **calculation_code** | **str**| The identifying calculation name for the results | 
 **effective_at** | **datetime**| The market date for which the data is stored | 

### Return type

[**Results**](Results.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_results**
> Results upsert_results(request=request)

Upsert results

Upsert pre-calculated results against a specified combination of key parameters defined in the CreateResults request.

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
api_instance = lusid.ResultsApi(lusid.ApiClient(configuration))
request = lusid.CreateResults() # CreateResults | The details of what to upsert (optional)

try:
    # Upsert results
    api_response = api_instance.upsert_results(request=request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResultsApi->upsert_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CreateResults**](CreateResults.md)| The details of what to upsert | [optional] 

### Return type

[**Results**](Results.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

