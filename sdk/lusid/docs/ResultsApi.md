# lusid.ResultsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_results**](ResultsApi.md#get_results) | **GET** /api/results/{scope}/{key}/{date} | Get results
[**upsert_results**](ResultsApi.md#upsert_results) | **POST** /api/results/{scope}/{key}/{date} | Upsert results


# **get_results**
> Results get_results(scope, key, date, as_at=as_at, sort_by=sort_by, start=start, limit=limit)

Get results

Retrieve some previously stored results

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
api_instance = lusid.ResultsApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the data
key = 'key_example' # str | The key that identifies the data
date = '2013-10-20T19:20:30+01:00' # datetime | The date for which the data was loaded
as_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The AsAt date of the data (optional)
sort_by = ['sort_by_example'] # list[str] | Optional. Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName (optional)
start = 56 # int | Optional. When paginating, skip this number of results (optional)
limit = 56 # int | Optional. When paginating, limit the number of returned results to this many. (optional)

try:
    # Get results
    api_response = api_instance.get_results(scope, key, date, as_at=as_at, sort_by=sort_by, start=start, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResultsApi->get_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the data | 
 **key** | **str**| The key that identifies the data | 
 **date** | **datetime**| The date for which the data was loaded | 
 **as_at** | **datetime**| Optional. The AsAt date of the data | [optional] 
 **sort_by** | [**list[str]**](str.md)| Optional. Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName | [optional] 
 **start** | **int**| Optional. When paginating, skip this number of results | [optional] 
 **limit** | **int**| Optional. When paginating, limit the number of returned results to this many. | [optional] 

### Return type

[**Results**](Results.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_results**
> Results upsert_results(scope, key, date, create_results=create_results)

Upsert results

Upsert pre-calculated results against a specified scope/key/date combination

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
api_instance = lusid.ResultsApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the data
key = 'key_example' # str | The key that identifies the data
date = '2013-10-20T19:20:30+01:00' # datetime | The date for which the data is relevant
create_results = lusid.CreateResults() # CreateResults | The results to upload (optional)

try:
    # Upsert results
    api_response = api_instance.upsert_results(scope, key, date, create_results=create_results)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResultsApi->upsert_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the data | 
 **key** | **str**| The key that identifies the data | 
 **date** | **datetime**| The date for which the data is relevant | 
 **create_results** | [**CreateResults**](CreateResults.md)| The results to upload | [optional] 

### Return type

[**Results**](Results.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

