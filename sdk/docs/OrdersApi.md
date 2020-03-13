# lusid.OrdersApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_order**](OrdersApi.md#get_order) | **GET** /api/orders/{scope}/{code} | [EXPERIMENTAL] Fetch a given order.
[**list_orders**](OrdersApi.md#list_orders) | **GET** /api/orders/{scope} | [EXPERIMENTAL] Fetch the last pre-AsAt date version of each order in scope (does not fetch the entire history).
[**upsert_order_properties**](OrdersApi.md#upsert_order_properties) | **POST** /api/orders/{scope}/properties | [EXPERIMENTAL] Upsert; update properties on existing Orders with given ids.
[**upsert_orders**](OrdersApi.md#upsert_orders) | **POST** /api/orders/{scope} | [EXPERIMENTAL] Upsert; update existing orders with given ids, or create new orders otherwise.


# **get_order**
> Order get_order(scope, code, as_at=as_at, property_keys=property_keys)

[EXPERIMENTAL] Fetch a given order.

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

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.OrdersApi(api_client)
    scope = 'scope_example' # str | The scope to which the order belongs.
code = 'code_example' # str | The order's unique identifier.
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the order. Defaults to return the latest version of the order if not specified. (optional)
property_keys = ['property_keys_example'] # list[str] | A list of property keys from the \"Orders\" domain to decorate onto the order.              These take the format {domain}/{scope}/{code} e.g. \"Orders/system/Name\". (optional)

    try:
        # [EXPERIMENTAL] Fetch a given order.
        api_response = api_instance.get_order(scope, code, as_at=as_at, property_keys=property_keys)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrdersApi->get_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope to which the order belongs. | 
 **code** | **str**| The order&#39;s unique identifier. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the order. Defaults to return the latest version of the order if not specified. | [optional] 
 **property_keys** | [**list[str]**](str.md)| A list of property keys from the \&quot;Orders\&quot; domain to decorate onto the order.              These take the format {domain}/{scope}/{code} e.g. \&quot;Orders/system/Name\&quot;. | [optional] 

### Return type

[**Order**](Order.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The order matching the given identifier. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_orders**
> PagedResourceListOfOrder list_orders(scope, as_at=as_at, page=page, sort_by=sort_by, start=start, limit=limit, filter=filter, property_keys=property_keys)

[EXPERIMENTAL] Fetch the last pre-AsAt date version of each order in scope (does not fetch the entire history).

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

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.OrdersApi(api_client)
    scope = 'scope_example' # str | The scope to which the orders belong.
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the order. Defaults to return the latest version of the order if not specified. (optional)
page = 'page_example' # str | The pagination token to use to continue listing orders from a previous call to list orders.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields              must not have changed since the original request. Also, if set, a start value cannot be provided. (optional)
sort_by = ['sort_by_example'] # list[str] | Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName. (optional)
start = 56 # int | When paginating, skip this number of results. (optional)
limit = 56 # int | When paginating, limit the number of returned results to this many. (optional)
filter = 'Quantity gt 0' # str | Expression to filter the result set.  Currently Orders can be filtered by Code (e.g.              \"Code eq 'ORD001'), Quantity (e.g. \"Quantity lt 100\"), Portfolio (e.g. \"Portfolio eq 'TestScope/UKEquities'\"),              LUSID Instrument Id (e.g. \"LusidInstrumentId eq 'LUID_12345678'\") or by Property (Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid). (optional) (default to 'Quantity gt 0')
property_keys = ['property_keys_example'] # list[str] | A list of property keys from the \"Orders\" domain to decorate onto each order.                  These take the format {domain}/{scope}/{code} e.g. \"Orders/system/Name\". (optional)

    try:
        # [EXPERIMENTAL] Fetch the last pre-AsAt date version of each order in scope (does not fetch the entire history).
        api_response = api_instance.list_orders(scope, as_at=as_at, page=page, sort_by=sort_by, start=start, limit=limit, filter=filter, property_keys=property_keys)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrdersApi->list_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope to which the orders belong. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the order. Defaults to return the latest version of the order if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing orders from a previous call to list orders.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields              must not have changed since the original request. Also, if set, a start value cannot be provided. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName. | [optional] 
 **start** | **int**| When paginating, skip this number of results. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Expression to filter the result set.  Currently Orders can be filtered by Code (e.g.              \&quot;Code eq &#39;ORD001&#39;), Quantity (e.g. \&quot;Quantity lt 100\&quot;), Portfolio (e.g. \&quot;Portfolio eq &#39;TestScope/UKEquities&#39;\&quot;),              LUSID Instrument Id (e.g. \&quot;LusidInstrumentId eq &#39;LUID_12345678&#39;\&quot;) or by Property (Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid). | [optional] [default to &#39;Quantity gt 0&#39;]
 **property_keys** | [**list[str]**](str.md)| A list of property keys from the \&quot;Orders\&quot; domain to decorate onto each order.                  These take the format {domain}/{scope}/{code} e.g. \&quot;Orders/system/Name\&quot;. | [optional] 

### Return type

[**PagedResourceListOfOrder**](PagedResourceListOfOrder.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Orders in scope. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_order_properties**
> UpsertOrderPropertiesResponse upsert_order_properties(scope, request=request)

[EXPERIMENTAL] Upsert; update properties on existing Orders with given ids.

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

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.OrdersApi(api_client)
    scope = 'scope_example' # str | The scope to which the orders belong.
request = [lusid.UpsertOrderPropertiesRequest()] # list[UpsertOrderPropertiesRequest] | A collection of order property upsert requests. (optional)

    try:
        # [EXPERIMENTAL] Upsert; update properties on existing Orders with given ids.
        api_response = api_instance.upsert_order_properties(scope, request=request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrdersApi->upsert_order_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope to which the orders belong. | 
 **request** | [**list[UpsertOrderPropertiesRequest]**](UpsertOrderPropertiesRequest.md)| A collection of order property upsert requests. | [optional] 

### Return type

[**UpsertOrderPropertiesResponse**](UpsertOrderPropertiesResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | An upsert order properties response. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_orders**
> ResourceListOfOrder upsert_orders(scope, request=request)

[EXPERIMENTAL] Upsert; update existing orders with given ids, or create new orders otherwise.

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

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.OrdersApi(api_client)
    scope = 'scope_example' # str | The scope to which the orders belong.
request = lusid.OrderSetRequest() # OrderSetRequest | The collection of order requests. (optional)

    try:
        # [EXPERIMENTAL] Upsert; update existing orders with given ids, or create new orders otherwise.
        api_response = api_instance.upsert_orders(scope, request=request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrdersApi->upsert_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope to which the orders belong. | 
 **request** | [**OrderSetRequest**](OrderSetRequest.md)| The collection of order requests. | [optional] 

### Return type

[**ResourceListOfOrder**](ResourceListOfOrder.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A collection of orders. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

