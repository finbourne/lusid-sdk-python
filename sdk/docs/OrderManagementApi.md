# lusid.OrderManagementApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**book_transactions**](OrderManagementApi.md#book_transactions) | **POST** /api/ordermanagement/booktransactions | [EXPERIMENTAL] BookTransactions: Books transactions using specific allocations as a source.
[**cancel_orders**](OrderManagementApi.md#cancel_orders) | **POST** /api/ordermanagement/cancelorders | [EARLY ACCESS] CancelOrders: Cancel existing orders
[**cancel_orders_and_move_remaining**](OrderManagementApi.md#cancel_orders_and_move_remaining) | **POST** /api/ordermanagement/cancelordersandmoveremaining | [EARLY ACCESS] CancelOrdersAndMoveRemaining: Cancel existing orders and move any unplaced quantities to new orders in new blocks
[**cancel_placements**](OrderManagementApi.md#cancel_placements) | **POST** /api/ordermanagement/$cancelplacements | [EARLY ACCESS] CancelPlacements: Cancel existing placements
[**create_orders**](OrderManagementApi.md#create_orders) | **POST** /api/ordermanagement/createorders | [EARLY ACCESS] CreateOrders: Upsert a Block and associated orders
[**get_order_history**](OrderManagementApi.md#get_order_history) | **GET** /api/ordermanagement/order/{scope}/{code}/$history | [EXPERIMENTAL] GetOrderHistory: Get the history of an order and related entity changes
[**move_orders**](OrderManagementApi.md#move_orders) | **POST** /api/ordermanagement/moveorders | [EARLY ACCESS] MoveOrders: Move orders to new or existing block
[**place_blocks**](OrderManagementApi.md#place_blocks) | **POST** /api/ordermanagement/placeblocks | [EARLY ACCESS] PlaceBlocks: Places blocks for a given list of placement requests.
[**run_allocation_service**](OrderManagementApi.md#run_allocation_service) | **POST** /api/ordermanagement/allocate | [EXPERIMENTAL] RunAllocationService: Runs the Allocation Service
[**update_orders**](OrderManagementApi.md#update_orders) | **POST** /api/ordermanagement/updateorders | [EARLY ACCESS] UpdateOrders: Update existing orders
[**update_placements**](OrderManagementApi.md#update_placements) | **POST** /api/ordermanagement/$updateplacements | [EARLY ACCESS] UpdatePlacements: Update existing placements


# **book_transactions**
> BookTransactionsResponse book_transactions(book_transactions_request, apply_fees_and_commission=apply_fees_and_commission)

[EXPERIMENTAL] BookTransactions: Books transactions using specific allocations as a source.

Takes a collection of allocation IDs, and maps fields from those allocations and related orders onto new transactions.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    OrderManagementApi
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

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(OrderManagementApi)

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # book_transactions_request = BookTransactionsRequest.from_json("")
        # book_transactions_request = BookTransactionsRequest.from_dict({})
        book_transactions_request = BookTransactionsRequest()
        apply_fees_and_commission = True # bool | Whether to apply fees and commissions to transactions (default: true) (optional) (default to True)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.book_transactions(book_transactions_request, apply_fees_and_commission=apply_fees_and_commission, opts=opts)

            # [EXPERIMENTAL] BookTransactions: Books transactions using specific allocations as a source.
            api_response = await api_instance.book_transactions(book_transactions_request, apply_fees_and_commission=apply_fees_and_commission)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling OrderManagementApi->book_transactions: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **book_transactions_request** | [**BookTransactionsRequest**](BookTransactionsRequest.md)| The allocations to create transactions for | 
 **apply_fees_and_commission** | **bool**| Whether to apply fees and commissions to transactions (default: true) | [optional] [default to True]

### Return type

[**BookTransactionsResponse**](BookTransactionsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The results from booking transactions from allocations |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **cancel_orders**
> CancelOrdersResponse cancel_orders(request_body)

[EARLY ACCESS] CancelOrders: Cancel existing orders

The response returns both the collection of successfully canceled orders, as well as those  that failed. For each failure, a reason is provided. It is important to check the failed set for  unsuccessful results.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    OrderManagementApi
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

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(OrderManagementApi)
        request_body = {"request1":{"scope":"MyScope","code":"Order00000123"},"request2":{"scope":"MyScope","code":"Order00000124"}} # Dict[str, ResourceId] | The request containing the ids of the orders to be cancelled.

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.cancel_orders(request_body, opts=opts)

            # [EARLY ACCESS] CancelOrders: Cancel existing orders
            api_response = await api_instance.cancel_orders(request_body)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling OrderManagementApi->cancel_orders: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, ResourceId]**](ResourceId.md)| The request containing the ids of the orders to be cancelled. | 

### Return type

[**CancelOrdersResponse**](CancelOrdersResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully cancelled orders along with any failures |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **cancel_orders_and_move_remaining**
> CancelOrdersAndMoveRemainingResponse cancel_orders_and_move_remaining(request_body)

[EARLY ACCESS] CancelOrdersAndMoveRemaining: Cancel existing orders and move any unplaced quantities to new orders in new blocks

Cancels existing orders, reducing their quantities to those aleady placed. Any remaining quantities are moved  to new orders in new blocks. The placed quantities are distributed to the cancelled orders on a pro-rata basis.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    OrderManagementApi
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

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(OrderManagementApi)
        request_body = {"request1":{"cancelOrderId":{"scope":"MyScope","code":"Order1"},"moveRemainingToOrderId":{"scope":"MyScope","code":"Order1_Rollover"},"moveRemainingToBlockId":{"scope":"MyScope","code":"Block_Rollover"}},"request2":{"cancelOrderId":{"scope":"MyScope","code":"Order2"},"moveRemainingToOrderId":{"scope":"MyScope","code":"Order2_Rollover"},"moveRemainingToBlockId":{"scope":"MyScope","code":"Block_Rollover"}}} # Dict[str, CancelOrdersAndMoveRemainingRequest] | The request containing the orders to be cancelled, and the destinations of remaining quantities.

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.cancel_orders_and_move_remaining(request_body, opts=opts)

            # [EARLY ACCESS] CancelOrdersAndMoveRemaining: Cancel existing orders and move any unplaced quantities to new orders in new blocks
            api_response = await api_instance.cancel_orders_and_move_remaining(request_body)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling OrderManagementApi->cancel_orders_and_move_remaining: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, CancelOrdersAndMoveRemainingRequest]**](CancelOrdersAndMoveRemainingRequest.md)| The request containing the orders to be cancelled, and the destinations of remaining quantities. | 

### Return type

[**CancelOrdersAndMoveRemainingResponse**](CancelOrdersAndMoveRemainingResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully cancelled and moved orders, along with any failures |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **cancel_placements**
> CancelPlacementsResponse cancel_placements(request_body)

[EARLY ACCESS] CancelPlacements: Cancel existing placements

The response returns both the collection of successfully canceled placements, as well as those  that failed. For each failure, a reason is provided. It is important to check the failed set for  unsuccessful results.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    OrderManagementApi
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

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(OrderManagementApi)
        request_body = {"request1":{"scope":"MyScope","code":"PLAC00000123"},"request2":{"scope":"MyScope","code":"PLAC00000124"}} # Dict[str, ResourceId] | The request containing the ids of the placements to be cancelled.

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.cancel_placements(request_body, opts=opts)

            # [EARLY ACCESS] CancelPlacements: Cancel existing placements
            api_response = await api_instance.cancel_placements(request_body)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling OrderManagementApi->cancel_placements: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, ResourceId]**](ResourceId.md)| The request containing the ids of the placements to be cancelled. | 

### Return type

[**CancelPlacementsResponse**](CancelPlacementsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully cancelled placements along with any failures |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **create_orders**
> ResourceListOfBlockAndOrders create_orders(block_and_orders_create_request)

[EARLY ACCESS] CreateOrders: Upsert a Block and associated orders

Upsert a Block and create associated orders.  This will fail if the block exists and already references orders with differing fields to the upsert request.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    OrderManagementApi
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

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(OrderManagementApi)

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # block_and_orders_create_request = BlockAndOrdersCreateRequest.from_json("")
        # block_and_orders_create_request = BlockAndOrdersCreateRequest.from_dict({})
        block_and_orders_create_request = BlockAndOrdersCreateRequest()

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.create_orders(block_and_orders_create_request, opts=opts)

            # [EARLY ACCESS] CreateOrders: Upsert a Block and associated orders
            api_response = await api_instance.create_orders(block_and_orders_create_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling OrderManagementApi->create_orders: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_and_orders_create_request** | [**BlockAndOrdersCreateRequest**](BlockAndOrdersCreateRequest.md)| The collection of block and orders requests. | 

### Return type

[**ResourceListOfBlockAndOrders**](ResourceListOfBlockAndOrders.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A collection of block and associated orders. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_order_history**
> ResourceListOfChangeIntervalWithOrderManagementDetail get_order_history(scope, code, as_at=as_at)

[EXPERIMENTAL] GetOrderHistory: Get the history of an order and related entity changes

Get the changes that have happened to an order and related entities.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    OrderManagementApi
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

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(OrderManagementApi)
        scope = 'scope_example' # str | The scope of the order.
        code = 'code_example' # str | The code of the order.
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the history of the order and related entities. Defaults              to return the latest version if not specified. (optional)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.get_order_history(scope, code, as_at=as_at, opts=opts)

            # [EXPERIMENTAL] GetOrderHistory: Get the history of an order and related entity changes
            api_response = await api_instance.get_order_history(scope, code, as_at=as_at)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling OrderManagementApi->get_order_history: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the order. | 
 **code** | **str**| The code of the order. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the history of the order and related entities. Defaults              to return the latest version if not specified. | [optional] 

### Return type

[**ResourceListOfChangeIntervalWithOrderManagementDetail**](ResourceListOfChangeIntervalWithOrderManagementDetail.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The history of the specified order and related entities (changes that have been made to it). |  -  |
**400** | The details of the input related failure |  -  |
**404** | Order not found. |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **move_orders**
> ResourceListOfMovedOrderToDifferentBlockResponse move_orders(move_orders_to_different_blocks_request)

[EARLY ACCESS] MoveOrders: Move orders to new or existing block

Move an order to a block, creating the block if it does not already exist.   This will fail if the block exists and already references orders with differing fields to the upsert request.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    OrderManagementApi
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

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(OrderManagementApi)

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # move_orders_to_different_blocks_request = MoveOrdersToDifferentBlocksRequest.from_json("")
        # move_orders_to_different_blocks_request = MoveOrdersToDifferentBlocksRequest.from_dict({})
        move_orders_to_different_blocks_request = MoveOrdersToDifferentBlocksRequest()

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.move_orders(move_orders_to_different_blocks_request, opts=opts)

            # [EARLY ACCESS] MoveOrders: Move orders to new or existing block
            api_response = await api_instance.move_orders(move_orders_to_different_blocks_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling OrderManagementApi->move_orders: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **move_orders_to_different_blocks_request** | [**MoveOrdersToDifferentBlocksRequest**](MoveOrdersToDifferentBlocksRequest.md)| The collection of order and destination block ids. | 

### Return type

[**ResourceListOfMovedOrderToDifferentBlockResponse**](ResourceListOfMovedOrderToDifferentBlockResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of block and order pairs for each order moved into a block, and the Id of the order&#39;s previous block (if any). |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **place_blocks**
> ResourceListOfPlacement place_blocks(place_blocks_request=place_blocks_request)

[EARLY ACCESS] PlaceBlocks: Places blocks for a given list of placement requests.

The referenced block's existence will be verified.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    OrderManagementApi
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

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(OrderManagementApi)

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # place_blocks_request = PlaceBlocksRequest.from_json("")
        # place_blocks_request = PlaceBlocksRequest.from_dict({})
        place_blocks_request = PlaceBlocksRequest()

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.place_blocks(place_blocks_request=place_blocks_request, opts=opts)

            # [EARLY ACCESS] PlaceBlocks: Places blocks for a given list of placement requests.
            api_response = await api_instance.place_blocks(place_blocks_request=place_blocks_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling OrderManagementApi->place_blocks: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **place_blocks_request** | [**PlaceBlocksRequest**](PlaceBlocksRequest.md)| The request containing the blocks to the placed. | [optional] 

### Return type

[**ResourceListOfPlacement**](ResourceListOfPlacement.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The block placements. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **run_allocation_service**
> AllocationServiceRunResponse run_allocation_service(resource_id, allocation_algorithm=allocation_algorithm)

[EXPERIMENTAL] RunAllocationService: Runs the Allocation Service

This will allocate executions for a given list of placements back to their originating orders.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    OrderManagementApi
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

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(OrderManagementApi)
        resource_id = [{"scope":"MyScope","code":"PLAC00000123"},{"scope":"MyScope","code":"PLAC00000456"}] # List[ResourceId] | The List of Placement IDs for which you wish to allocate executions.
        allocation_algorithm = 'allocation_algorithm_example' # str | A string representation of the allocation algorithm you would like to use to allocate shares from executions e.g. \"PR-FIFO\".  This defaults to \"PR-FIFO\". (optional)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.run_allocation_service(resource_id, allocation_algorithm=allocation_algorithm, opts=opts)

            # [EXPERIMENTAL] RunAllocationService: Runs the Allocation Service
            api_response = await api_instance.run_allocation_service(resource_id, allocation_algorithm=allocation_algorithm)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling OrderManagementApi->run_allocation_service: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | [**List[ResourceId]**](ResourceId.md)| The List of Placement IDs for which you wish to allocate executions. | 
 **allocation_algorithm** | **str**| A string representation of the allocation algorithm you would like to use to allocate shares from executions e.g. \&quot;PR-FIFO\&quot;.  This defaults to \&quot;PR-FIFO\&quot;. | [optional] 

### Return type

[**AllocationServiceRunResponse**](AllocationServiceRunResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The results from a run of the Allocation Service |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **update_orders**
> UpdateOrdersResponse update_orders(request_body)

[EARLY ACCESS] UpdateOrders: Update existing orders

The response returns both the collection of successfully updated orders, as well as those  that failed. For each failure, a reason is provided. It is important to check the failed set for  unsuccessful results.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    OrderManagementApi
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

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(OrderManagementApi)
        request_body = {"update1":{"id":{"scope":"MyScope","code":"Code1"},"quantity":101},"update2":{"id":{"scope":"MyScope","code":"Code2"},"quantity":100,"portfolioId":{"scope":"MyScope","code":"NewPortfolio"},"properties":{"Order/MyScope/OrderProperty":{"key":"Order/MyScope/OrderProperty","value":{"labelValue":"NewValue"}}}}} # Dict[str, OrderUpdateRequest] | The request containing the orders to be updated.

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.update_orders(request_body, opts=opts)

            # [EARLY ACCESS] UpdateOrders: Update existing orders
            api_response = await api_instance.update_orders(request_body)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling OrderManagementApi->update_orders: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, OrderUpdateRequest]**](OrderUpdateRequest.md)| The request containing the orders to be updated. | 

### Return type

[**UpdateOrdersResponse**](UpdateOrdersResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully updated orders along with any failures |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **update_placements**
> UpdatePlacementsResponse update_placements(request_body)

[EARLY ACCESS] UpdatePlacements: Update existing placements

The response returns both the collection of successfully updated placements, as well as those  that failed. For each failure, a reason is provided. It is important to check the failed set for  unsuccessful results.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    OrderManagementApi
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

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(OrderManagementApi)
        request_body = {"request1":{"id":{"scope":"MyScope","code":"PLAC00000123"},"quantity":100,"properties":{"Placement/MyScope/SomePlacementProperty":{"key":"Placement/MyScope/SomePlacementProperty","value":{"labelValue":"XYZ000034567"}}},"counterparty":"SomeCounterparty","entryType":"Manual"}} # Dict[str, PlacementUpdateRequest] | The request containing the placements to be updated.

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.update_placements(request_body, opts=opts)

            # [EARLY ACCESS] UpdatePlacements: Update existing placements
            api_response = await api_instance.update_placements(request_body)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling OrderManagementApi->update_placements: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, PlacementUpdateRequest]**](PlacementUpdateRequest.md)| The request containing the placements to be updated. | 

### Return type

[**UpdatePlacementsResponse**](UpdatePlacementsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully updated placements along with any failures |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

