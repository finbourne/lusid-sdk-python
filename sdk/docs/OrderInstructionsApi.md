# lusid.OrderInstructionsApi

All URIs are relative to *https://fbn-ci.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_order_instruction**](OrderInstructionsApi.md#delete_order_instruction) | **DELETE** /api/orderinstructions/{scope}/{code} | [EXPERIMENTAL] DeleteOrderInstruction: Delete orderInstruction
[**get_order_instruction**](OrderInstructionsApi.md#get_order_instruction) | **GET** /api/orderinstructions/{scope}/{code} | [EXPERIMENTAL] GetOrderInstruction: Get OrderInstruction
[**list_order_instructions**](OrderInstructionsApi.md#list_order_instructions) | **GET** /api/orderinstructions | [EXPERIMENTAL] ListOrderInstructions: List OrderInstructions
[**upsert_order_instructions**](OrderInstructionsApi.md#upsert_order_instructions) | **POST** /api/orderinstructions | [EXPERIMENTAL] UpsertOrderInstructions: Upsert OrderInstruction


# **delete_order_instruction**
> DeletedEntityResponse delete_order_instruction(scope, code)

[EXPERIMENTAL] DeleteOrderInstruction: Delete orderInstruction

Delete an orderInstruction. Deletion will be valid from the orderInstruction's creation datetime.  This means that the orderInstruction will no longer exist at any effective datetime from the asAt datetime of deletion.

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
    api_instance = lusid.OrderInstructionsApi(api_client)
    scope = 'scope_example' # str | The orderInstruction scope.
    code = 'code_example' # str | The orderInstruction's code. This, together with the scope uniquely identifies the orderInstruction to delete.

    try:
        # [EXPERIMENTAL] DeleteOrderInstruction: Delete orderInstruction
        api_response = await api_instance.delete_order_instruction(scope, code)
        print("The response of OrderInstructionsApi->delete_order_instruction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderInstructionsApi->delete_order_instruction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The orderInstruction scope. | 
 **code** | **str**| The orderInstruction&#39;s code. This, together with the scope uniquely identifies the orderInstruction to delete. | 

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
**200** | The response from deleting an orderInstruction. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_instruction**
> OrderInstruction get_order_instruction(scope, code, as_at=as_at, property_keys=property_keys)

[EXPERIMENTAL] GetOrderInstruction: Get OrderInstruction

Fetch a OrderInstruction that matches the specified identifier

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
    api_instance = lusid.OrderInstructionsApi(api_client)
    scope = 'scope_example' # str | The scope to which the orderInstruction belongs.
    code = 'code_example' # str | The orderInstruction's unique identifier.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the orderInstruction. Defaults to return the latest version of the orderInstruction if not specified. (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the \"OrderInstruction\" domain to decorate onto the orderInstruction.              These take the format {domain}/{scope}/{code} e.g. \"OrderInstruction/system/Name\". (optional)

    try:
        # [EXPERIMENTAL] GetOrderInstruction: Get OrderInstruction
        api_response = await api_instance.get_order_instruction(scope, code, as_at=as_at, property_keys=property_keys)
        print("The response of OrderInstructionsApi->get_order_instruction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderInstructionsApi->get_order_instruction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope to which the orderInstruction belongs. | 
 **code** | **str**| The orderInstruction&#39;s unique identifier. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the orderInstruction. Defaults to return the latest version of the orderInstruction if not specified. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the \&quot;OrderInstruction\&quot; domain to decorate onto the orderInstruction.              These take the format {domain}/{scope}/{code} e.g. \&quot;OrderInstruction/system/Name\&quot;. | [optional] 

### Return type

[**OrderInstruction**](OrderInstruction.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The orderInstruction matching the given identifier. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_order_instructions**
> PagedResourceListOfOrderInstruction list_order_instructions(as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter, property_keys=property_keys)

[EXPERIMENTAL] ListOrderInstructions: List OrderInstructions

Fetch the last pre-AsAt date version of each orderInstruction in scope (does not fetch the entire history).

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
    api_instance = lusid.OrderInstructionsApi(api_client)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the orderInstruction. Defaults to return the latest version of the orderInstruction if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing orderInstructions from a previous call to list orderInstructions.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields              must not have changed since the original request. (optional)
    sort_by = ['sort_by_example'] # List[str] | Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName. (optional)
    limit = 56 # int | When paginating, limit the number of returned results to this many. (optional)
    filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid. (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the \"OrderInstruction\" domain to decorate onto each orderInstruction.                  These take the format {domain}/{scope}/{code} e.g. \"OrderInstruction/system/Name\". (optional)

    try:
        # [EXPERIMENTAL] ListOrderInstructions: List OrderInstructions
        api_response = await api_instance.list_order_instructions(as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter, property_keys=property_keys)
        print("The response of OrderInstructionsApi->list_order_instructions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderInstructionsApi->list_order_instructions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to retrieve the orderInstruction. Defaults to return the latest version of the orderInstruction if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing orderInstructions from a previous call to list orderInstructions.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields              must not have changed since the original request. | [optional] 
 **sort_by** | [**List[str]**](str.md)| Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the \&quot;OrderInstruction\&quot; domain to decorate onto each orderInstruction.                  These take the format {domain}/{scope}/{code} e.g. \&quot;OrderInstruction/system/Name\&quot;. | [optional] 

### Return type

[**PagedResourceListOfOrderInstruction**](PagedResourceListOfOrderInstruction.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OrderInstructions in scope. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_order_instructions**
> ResourceListOfOrderInstruction upsert_order_instructions(order_instruction_set_request=order_instruction_set_request)

[EXPERIMENTAL] UpsertOrderInstructions: Upsert OrderInstruction

Upsert; update existing orderInstructions with given ids, or create new orderInstructions otherwise.

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
    api_instance = lusid.OrderInstructionsApi(api_client)
    order_instruction_set_request = {"requests":[{"id":{"scope":"MyScope","code":"PACK00000123"},"createdDate":"2020-01-01T00:00:00.0000000+00:00","portfolioId":{"scope":"MyScope","code":"testPortfolio"},"instrumentIdentifiers":{"Instrument/default/Currency":"GBP"},"quantity":10,"properties":{"OrderInstruction/MyScope/SomeOrderInstructionProperty":{"key":"OrderInstruction/MyScope/SomeOrderInstructionProperty","value":{"labelValue":"XYZ000034567"}}}}]} # OrderInstructionSetRequest | The collection of orderInstruction requests. (optional)

    try:
        # [EXPERIMENTAL] UpsertOrderInstructions: Upsert OrderInstruction
        api_response = await api_instance.upsert_order_instructions(order_instruction_set_request=order_instruction_set_request)
        print("The response of OrderInstructionsApi->upsert_order_instructions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderInstructionsApi->upsert_order_instructions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_instruction_set_request** | [**OrderInstructionSetRequest**](OrderInstructionSetRequest.md)| The collection of orderInstruction requests. | [optional] 

### Return type

[**ResourceListOfOrderInstruction**](ResourceListOfOrderInstruction.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A collection of orderInstructions. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

