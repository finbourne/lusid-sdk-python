# lusid.AnalyticsStoresApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_analytic_store**](AnalyticsStoresApi.md#create_analytic_store) | **POST** /api/analytics | [EXPERIMENTAL] Create analytic store
[**delete_analytic_store**](AnalyticsStoresApi.md#delete_analytic_store) | **DELETE** /api/analytics/{scope}/{year}/{month}/{day} | [EXPERIMENTAL] Delete analytic store
[**get_analytic_store**](AnalyticsStoresApi.md#get_analytic_store) | **GET** /api/analytics/{scope}/{year}/{month}/{day} | [EXPERIMENTAL] Get analytic store
[**list_analytic_stores**](AnalyticsStoresApi.md#list_analytic_stores) | **GET** /api/analytics | [EXPERIMENTAL] List analytic stores
[**set_analytics**](AnalyticsStoresApi.md#set_analytics) | **PUT** /api/analytics/{scope}/{year}/{month}/{day}/prices | [EXPERIMENTAL] Set analytic data


# **create_analytic_store**
> AnalyticStore create_analytic_store(request=request)

[EXPERIMENTAL] Create analytic store

Create a new analytic store for the specified scope and date

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

# Defining host is optional and default to http://localhost/api
configuration.host = "http://localhost/api"
# Create an instance of the API class
api_instance = lusid.AnalyticsStoresApi(lusid.ApiClient(configuration))
request = lusid.CreateAnalyticStoreRequest() # CreateAnalyticStoreRequest | A populated analytic store definition (optional)

try:
    # [EXPERIMENTAL] Create analytic store
    api_response = api_instance.create_analytic_store(request=request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsStoresApi->create_analytic_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CreateAnalyticStoreRequest**](CreateAnalyticStoreRequest.md)| A populated analytic store definition | [optional] 

### Return type

[**AnalyticStore**](AnalyticStore.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The meta data of the created analytic store |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_analytic_store**
> DeletedEntityResponse delete_analytic_store(scope, year, month, day)

[EXPERIMENTAL] Delete analytic store

Delete stored analytic data in the specified scope for the specified date

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

# Defining host is optional and default to http://localhost/api
configuration.host = "http://localhost/api"
# Create an instance of the API class
api_instance = lusid.AnalyticsStoresApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The analytics data scope
year = 56 # int | The year component of the date
month = 56 # int | The month component of the date
day = 56 # int | The day component of the date

try:
    # [EXPERIMENTAL] Delete analytic store
    api_response = api_instance.delete_analytic_store(scope, year, month, day)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsStoresApi->delete_analytic_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The analytics data scope | 
 **year** | **int**| The year component of the date | 
 **month** | **int**| The month component of the date | 
 **day** | **int**| The day component of the date | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A confirmation of the deleted store |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_analytic_store**
> AnalyticStore get_analytic_store(scope, year, month, day, as_at=as_at)

[EXPERIMENTAL] Get analytic store

Get the meta data associated with a specified scope and date combination (analytic store)

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

# Defining host is optional and default to http://localhost/api
configuration.host = "http://localhost/api"
# Create an instance of the API class
api_instance = lusid.AnalyticsStoresApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The analytics data scope
year = 56 # int | The year component of the date for the data in the scope
month = 56 # int | The month component of the date for the data in the scope
day = 56 # int | The day component of the date for the data in the scope
as_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The AsAt date of the data (optional)

try:
    # [EXPERIMENTAL] Get analytic store
    api_response = api_instance.get_analytic_store(scope, year, month, day, as_at=as_at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsStoresApi->get_analytic_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The analytics data scope | 
 **year** | **int**| The year component of the date for the data in the scope | 
 **month** | **int**| The month component of the date for the data in the scope | 
 **day** | **int**| The day component of the date for the data in the scope | 
 **as_at** | **datetime**| Optional. The AsAt date of the data | [optional] 

### Return type

[**AnalyticStore**](AnalyticStore.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The analytic store&#39;s meta data |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_analytic_stores**
> ResourceListOfAnalyticStoreKey list_analytic_stores(as_at=as_at, sort_by=sort_by, start=start, limit=limit, filter=filter)

[EXPERIMENTAL] List analytic stores

List all defined analytic stores

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

# Defining host is optional and default to http://localhost/api
configuration.host = "http://localhost/api"
# Create an instance of the API class
api_instance = lusid.AnalyticsStoresApi(lusid.ApiClient(configuration))
as_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The AsAt date of the data (optional)
sort_by = ['sort_by_example'] # list[str] | Optional. Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName (optional)
start = 56 # int | Optional. When paginating, skip this number of results (optional)
limit = 56 # int | Optional. When paginating, limit the number of returned results to this many. (optional)
filter = 'filter_example' # str | Optional. Expression to filter the result set (optional)

try:
    # [EXPERIMENTAL] List analytic stores
    api_response = api_instance.list_analytic_stores(as_at=as_at, sort_by=sort_by, start=start, limit=limit, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsStoresApi->list_analytic_stores: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| Optional. The AsAt date of the data | [optional] 
 **sort_by** | [**list[str]**](str.md)| Optional. Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName | [optional] 
 **start** | **int**| Optional. When paginating, skip this number of results | [optional] 
 **limit** | **int**| Optional. When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Optional. Expression to filter the result set | [optional] 

### Return type

[**ResourceListOfAnalyticStoreKey**](ResourceListOfAnalyticStoreKey.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of analytic store keys |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_analytics**
> AnalyticStore set_analytics(scope, year, month, day, data=data)

[EXPERIMENTAL] Set analytic data

Store the complete set of analytics for an existing analytic store for the specified scope and date

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

# Defining host is optional and default to http://localhost/api
configuration.host = "http://localhost/api"
# Create an instance of the API class
api_instance = lusid.AnalyticsStoresApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the data being stored
year = 56 # int | The year component of the date for the data
month = 56 # int | The month component of the date for the data
day = 56 # int | The day component of the date for the data
data = [lusid.InstrumentAnalytic()] # list[InstrumentAnalytic] | The analytic data being inserted (optional)

try:
    # [EXPERIMENTAL] Set analytic data
    api_response = api_instance.set_analytics(scope, year, month, day, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsStoresApi->set_analytics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the data being stored | 
 **year** | **int**| The year component of the date for the data | 
 **month** | **int**| The month component of the date for the data | 
 **day** | **int**| The day component of the date for the data | 
 **data** | [**list[InstrumentAnalytic]**](InstrumentAnalytic.md)| The analytic data being inserted | [optional] 

### Return type

[**AnalyticStore**](AnalyticStore.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The meta data of the analytic store |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

