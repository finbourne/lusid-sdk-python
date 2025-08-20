# lusid.OrdersApi

All URIs are relative to *https://fbn-prd.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_order**](OrdersApi.md#delete_order) | **DELETE** /api/orders/{scope}/{code} | [EARLY ACCESS] DeleteOrder: Delete order
[**get_order**](OrdersApi.md#get_order) | **GET** /api/orders/{scope}/{code} | [EARLY ACCESS] GetOrder: Get Order
[**list_orders**](OrdersApi.md#list_orders) | **GET** /api/orders | ListOrders: List Orders
[**upsert_orders**](OrdersApi.md#upsert_orders) | **POST** /api/orders | UpsertOrders: Upsert Order


# **delete_order**
> DeletedEntityResponse delete_order(scope, code)

[EARLY ACCESS] DeleteOrder: Delete order

Delete an order. Deletion will be valid from the order's creation datetime. This means that the order will no longer exist at any effective datetime from the asAt datetime of deletion.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    OrdersApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "lusidUrl":"https://<your-domain>.lusid.com/api",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the lusid SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(OrdersApi)
    scope = 'scope_example' # str | The order scope.
    code = 'code_example' # str | The order's code. This, together with the scope uniquely identifies the order to delete.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_order(scope, code, opts=opts)

        # [EARLY ACCESS] DeleteOrder: Delete order
        api_response = api_instance.delete_order(scope, code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling OrdersApi->delete_order: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The order scope. | 
 **code** | **str**| The order&#39;s code. This, together with the scope uniquely identifies the order to delete. | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response from deleting an order. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_order**
> Order get_order(scope, code, as_at=as_at, property_keys=property_keys)

[EARLY ACCESS] GetOrder: Get Order

Fetch an Order that matches the specified identifier.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    OrdersApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "lusidUrl":"https://<your-domain>.lusid.com/api",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the lusid SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(OrdersApi)
    scope = 'scope_example' # str | The scope to which the order belongs.
    code = 'code_example' # str | The order's unique identifier.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the order. Defaults to return the latest version of the order if not specified. (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the \"Orders\" domain to decorate onto the order.             These take the format {domain}/{scope}/{code} e.g. \"Orders/system/Name\". (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_order(scope, code, as_at=as_at, property_keys=property_keys, opts=opts)

        # [EARLY ACCESS] GetOrder: Get Order
        api_response = api_instance.get_order(scope, code, as_at=as_at, property_keys=property_keys)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling OrdersApi->get_order: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope to which the order belongs. | 
 **code** | **str**| The order&#39;s unique identifier. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the order. Defaults to return the latest version of the order if not specified. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the \&quot;Orders\&quot; domain to decorate onto the order.             These take the format {domain}/{scope}/{code} e.g. \&quot;Orders/system/Name\&quot;. | [optional] 

### Return type

[**Order**](Order.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The order matching the given identifier. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_orders**
> PagedResourceListOfOrder list_orders(as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter, property_keys=property_keys, data_model_scope=data_model_scope, data_model_code=data_model_code, membership_type=membership_type)

ListOrders: List Orders

Fetch the last pre-AsAt date version of each order with optional filtering (does not fetch the entire history).

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    OrdersApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "lusidUrl":"https://<your-domain>.lusid.com/api",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the lusid SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(OrdersApi)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the order. Defaults to return the latest version of the order if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing orders from a previous call to list orders.             This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields             must not have changed since the original request. (optional)
    sort_by = ['sort_by_example'] # List[str] | A list of field names or properties to sort by, each suffixed by \" ASC\" or \" DESC\". (optional)
    limit = 56 # int | When paginating, limit the number of returned results to this many. (optional)
    filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here:             https://support.lusid.com/filtering-results-from-lusid. (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the \"Orders\" domain to decorate onto each order.                 These take the format {domain}/{scope}/{code} e.g. \"Orders/system/Name\".                 All properties, except derived properties, are returned by default, without specifying here. (optional)
    data_model_scope = 'data_model_scope_example' # str | The optional scope of a Custom Data Model to use (optional)
    data_model_code = 'data_model_code_example' # str | The optional code of a Custom Data Model to use (optional)
    membership_type = 'membership_type_example' # str | The membership types of the specified Custom Data Model to return. Allowable values are Member, Candidate and All. Defaults to Member. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_orders(as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter, property_keys=property_keys, data_model_scope=data_model_scope, data_model_code=data_model_code, membership_type=membership_type, opts=opts)

        # ListOrders: List Orders
        api_response = api_instance.list_orders(as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter, property_keys=property_keys, data_model_scope=data_model_scope, data_model_code=data_model_code, membership_type=membership_type)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling OrdersApi->list_orders: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to retrieve the order. Defaults to return the latest version of the order if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing orders from a previous call to list orders.             This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields             must not have changed since the original request. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here:             https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the \&quot;Orders\&quot; domain to decorate onto each order.                 These take the format {domain}/{scope}/{code} e.g. \&quot;Orders/system/Name\&quot;.                 All properties, except derived properties, are returned by default, without specifying here. | [optional] 
 **data_model_scope** | **str**| The optional scope of a Custom Data Model to use | [optional] 
 **data_model_code** | **str**| The optional code of a Custom Data Model to use | [optional] 
 **membership_type** | **str**| The membership types of the specified Custom Data Model to return. Allowable values are Member, Candidate and All. Defaults to Member. | [optional] 

### Return type

[**PagedResourceListOfOrder**](PagedResourceListOfOrder.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Orders. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **upsert_orders**
> ResourceListOfOrder upsert_orders(order_set_request, data_model_scope=data_model_scope, data_model_code=data_model_code)

UpsertOrders: Upsert Order

Upsert; update existing orders with given ids, or create new orders otherwise.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    OrdersApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "lusidUrl":"https://<your-domain>.lusid.com/api",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the lusid SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(OrdersApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # order_set_request = OrderSetRequest.from_json("")
    # order_set_request = OrderSetRequest.from_dict({})
    order_set_request = OrderSetRequest()
    data_model_scope = 'data_model_scope_example' # str | The optional scope of a Custom Data Model to use (optional)
    data_model_code = 'data_model_code_example' # str | The optional code of a Custom Data Model to use (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.upsert_orders(order_set_request, data_model_scope=data_model_scope, data_model_code=data_model_code, opts=opts)

        # UpsertOrders: Upsert Order
        api_response = api_instance.upsert_orders(order_set_request, data_model_scope=data_model_scope, data_model_code=data_model_code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling OrdersApi->upsert_orders: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_set_request** | [**OrderSetRequest**](OrderSetRequest.md)| The collection of order requests. | 
 **data_model_scope** | **str**| The optional scope of a Custom Data Model to use | [optional] 
 **data_model_code** | **str**| The optional code of a Custom Data Model to use | [optional] 

### Return type

[**ResourceListOfOrder**](ResourceListOfOrder.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A collection of orders. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

