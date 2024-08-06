# lusid.OrdersApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_order**](OrdersApi.md#delete_order) | **DELETE** /api/orders/{scope}/{code} | [EARLY ACCESS] DeleteOrder: Delete order
[**get_order**](OrdersApi.md#get_order) | **GET** /api/orders/{scope}/{code} | [EARLY ACCESS] GetOrder: Get Order
[**list_orders**](OrdersApi.md#list_orders) | **GET** /api/orders | ListOrders: List Orders
[**upsert_orders**](OrdersApi.md#upsert_orders) | **POST** /api/orders | UpsertOrders: Upsert Order


# **delete_order**
> DeletedEntityResponse delete_order(scope, code)

[EARLY ACCESS] DeleteOrder: Delete order

Delete an order. Deletion will be valid from the order's creation datetime.  This means that the order will no longer exist at any effective datetime from the asAt datetime of deletion.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    OrdersApi
)

async def main():

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

    # Use the lusid ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(OrdersApi)
        scope = 'scope_example' # str | The order scope.
        code = 'code_example' # str | The order's code. This, together with the scope uniquely identifies the order to delete.

        try:
            # [EARLY ACCESS] DeleteOrder: Delete order
            api_response = await api_instance.delete_order(scope, code)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling OrdersApi->delete_order: %s\n" % e)

asyncio.run(main())
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
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    OrdersApi
)

async def main():

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

    # Use the lusid ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(OrdersApi)
        scope = 'scope_example' # str | The scope to which the order belongs.
        code = 'code_example' # str | The order's unique identifier.
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the order. Defaults to return the latest version of the order if not specified. (optional)
        property_keys = ['property_keys_example'] # List[str] | A list of property keys from the \"Orders\" domain to decorate onto the order.              These take the format {domain}/{scope}/{code} e.g. \"Orders/system/Name\". (optional)

        try:
            # [EARLY ACCESS] GetOrder: Get Order
            api_response = await api_instance.get_order(scope, code, as_at=as_at, property_keys=property_keys)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling OrdersApi->get_order: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope to which the order belongs. | 
 **code** | **str**| The order&#39;s unique identifier. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the order. Defaults to return the latest version of the order if not specified. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the \&quot;Orders\&quot; domain to decorate onto the order.              These take the format {domain}/{scope}/{code} e.g. \&quot;Orders/system/Name\&quot;. | [optional] 

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
> PagedResourceListOfOrder list_orders(as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter, property_keys=property_keys)

ListOrders: List Orders

Fetch the last pre-AsAt date version of each order with optional filtering (does not fetch the entire history).

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    OrdersApi
)

async def main():

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

    # Use the lusid ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(OrdersApi)
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the order. Defaults to return the latest version of the order if not specified. (optional)
        page = 'page_example' # str | The pagination token to use to continue listing orders from a previous call to list orders.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields              must not have changed since the original request. (optional)
        sort_by = ['sort_by_example'] # List[str] | A list of field names or properties to sort by, each suffixed by \" ASC\" or \" DESC\". (optional)
        limit = 56 # int | When paginating, limit the number of returned results to this many. (optional)
        filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid. (optional)
        property_keys = ['property_keys_example'] # List[str] | A list of property keys from the \"Orders\" domain to decorate onto each order.                  These take the format {domain}/{scope}/{code} e.g. \"Orders/system/Name\". (optional)

        try:
            # ListOrders: List Orders
            api_response = await api_instance.list_orders(as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter, property_keys=property_keys)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling OrdersApi->list_orders: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to retrieve the order. Defaults to return the latest version of the order if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing orders from a previous call to list orders.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields              must not have changed since the original request. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the \&quot;Orders\&quot; domain to decorate onto each order.                  These take the format {domain}/{scope}/{code} e.g. \&quot;Orders/system/Name\&quot;. | [optional] 

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
> ResourceListOfOrder upsert_orders(order_set_request=order_set_request)

UpsertOrders: Upsert Order

Upsert; update existing orders with given ids, or create new orders otherwise.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    OrdersApi
)

async def main():

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

    # Use the lusid ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(OrdersApi)

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # order_set_request = OrderSetRequest()
        # order_set_request = OrderSetRequest.from_json("")
        order_set_request = OrderSetRequest.from_dict({"orderRequests":[{"properties":{"Order/MyScope/SomeOrderProperty":{"key":"Order/MyScope/SomeOrderProperty","value":{"labelValue":"XYZ000034567"}}},"instrumentIdentifiers":{"Instrument/default/Currency":"GBP"},"quantity":100,"side":"Buy","orderBookId":{"scope":"MyScope","code":"UKEQ-Orders"},"portfolioId":{"scope":"MyScope","code":"UK-Equity"},"id":{"scope":"MyScope","code":"ORD00000123"},"state":"New","type":"Limit","timeInForce":"GoodTilCancel","date":"2023-05-02T00:00:00.0000000+00:00","price":{"amount":534,"currency":"USD"},"orderInstruction":{"scope":"MyScope","code":"Instruction-06"},"package":{"scope":"MyScope","code":"UKEQ-Package"}}]}) # OrderSetRequest | The collection of order requests. (optional)

        try:
            # UpsertOrders: Upsert Order
            api_response = await api_instance.upsert_orders(order_set_request=order_set_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling OrdersApi->upsert_orders: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_set_request** | [**OrderSetRequest**](OrderSetRequest.md)| The collection of order requests. | [optional] 

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

