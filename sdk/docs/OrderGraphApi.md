# lusid.OrderGraphApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_order_graph_blocks**](OrderGraphApi.md#list_order_graph_blocks) | **GET** /api/ordergraph/blocks | [EARLY ACCESS] ListOrderGraphBlocks: Lists blocks that pass the filter provided, and builds a summary picture of the state of their associated order entities.
[**list_order_graph_placement_children**](OrderGraphApi.md#list_order_graph_placement_children) | **GET** /api/ordergraph/placementchildren/{scope}/{code} | [EARLY ACCESS] ListOrderGraphPlacementChildren: Lists all placements for the parent placement specified by the scope and code, and builds a summary picture of the state of their associated order entities.
[**list_order_graph_placements**](OrderGraphApi.md#list_order_graph_placements) | **GET** /api/ordergraph/placements | [EARLY ACCESS] ListOrderGraphPlacements: Lists placements that pass the filter provided, and builds a summary picture of the state of their associated order entities.


# **list_order_graph_blocks**
> PagedResourceListOfOrderGraphBlock list_order_graph_blocks(as_at=as_at, pagination_token=pagination_token, sort_by=sort_by, limit=limit, filter=filter, property_keys=property_keys, use_compliance_v2=use_compliance_v2)

[EARLY ACCESS] ListOrderGraphBlocks: Lists blocks that pass the filter provided, and builds a summary picture of the state of their associated order entities.

Lists all blocks of orders, subject to the filter, along with the IDs of orders, placements, allocations and  executions in the block, the total quantities of each, and a simple text field describing the overall state.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    OrderGraphApi
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
        api_instance = api_client_factory.build(OrderGraphApi)
        as_at = '2013-10-20T19:20:30+01:00' # datetime | See https://support.lusid.com/knowledgebase/article/KA-01832/ (optional)
        pagination_token = 'pagination_token_example' # str | See https://support.lusid.com/knowledgebase/article/KA-01915/ (optional)
        sort_by = ['sort_by_example'] # List[str] | A list of field names or properties to sort by, each suffixed by \" ASC\" or \" DESC\". (optional)
        limit = 56 # int | See https://support.lusid.com/knowledgebase/article/KA-01915/ (optional)
        filter = '' # str | See https://support.lusid.com/knowledgebase/article/KA-01914/ (optional) (default to '')
        property_keys = ['property_keys_example'] # List[str] | Must be block-level properties. See https://support.lusid.com/knowledgebase/article/KA-01855/ (optional)
        use_compliance_v2 = False # bool | Whether to use the V2 compliance engine when deriving compliance statuses for orders. (default: false) (optional) (default to False)

        try:
            # [EARLY ACCESS] ListOrderGraphBlocks: Lists blocks that pass the filter provided, and builds a summary picture of the state of their associated order entities.
            api_response = await api_instance.list_order_graph_blocks(as_at=as_at, pagination_token=pagination_token, sort_by=sort_by, limit=limit, filter=filter, property_keys=property_keys, use_compliance_v2=use_compliance_v2)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling OrderGraphApi->list_order_graph_blocks: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| See https://support.lusid.com/knowledgebase/article/KA-01832/ | [optional] 
 **pagination_token** | **str**| See https://support.lusid.com/knowledgebase/article/KA-01915/ | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 
 **limit** | **int**| See https://support.lusid.com/knowledgebase/article/KA-01915/ | [optional] 
 **filter** | **str**| See https://support.lusid.com/knowledgebase/article/KA-01914/ | [optional] [default to &#39;&#39;]
 **property_keys** | [**List[str]**](str.md)| Must be block-level properties. See https://support.lusid.com/knowledgebase/article/KA-01855/ | [optional] 
 **use_compliance_v2** | **bool**| Whether to use the V2 compliance engine when deriving compliance statuses for orders. (default: false) | [optional] [default to False]

### Return type

[**PagedResourceListOfOrderGraphBlock**](PagedResourceListOfOrderGraphBlock.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Blocks in scope. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_order_graph_placement_children**
> PagedResourceListOfOrderGraphPlacement list_order_graph_placement_children(scope, code, as_at=as_at, pagination_token=pagination_token, sort_by=sort_by, limit=limit, property_keys=property_keys)

[EARLY ACCESS] ListOrderGraphPlacementChildren: Lists all placements for the parent placement specified by the scope and code, and builds a summary picture of the state of their associated order entities.

Lists all child order placements, for the specified parent placement, along with the IDs of the block and order that the  placement is for, each placement's quantity, the IDs of all allocations and executions in the placement  and the total quantities of those, and a simple text field describing the overall state of the placement.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    OrderGraphApi
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
        api_instance = api_client_factory.build(OrderGraphApi)
        scope = 'scope_example' # str | The parent placement's scope
        code = 'code_example' # str | The parent placement's code
        as_at = '2013-10-20T19:20:30+01:00' # datetime | See https://support.lusid.com/knowledgebase/article/KA-01832/ (optional)
        pagination_token = 'pagination_token_example' # str | See https://support.lusid.com/knowledgebase/article/KA-01915/ (optional)
        sort_by = ['sort_by_example'] # List[str] | Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName. (optional)
        limit = 56 # int | See https://support.lusid.com/knowledgebase/article/KA-01915/ (optional)
        property_keys = ['property_keys_example'] # List[str] | Must be placement properties. See https://support.lusid.com/knowledgebase/article/KA-01855/ (optional)

        try:
            # [EARLY ACCESS] ListOrderGraphPlacementChildren: Lists all placements for the parent placement specified by the scope and code, and builds a summary picture of the state of their associated order entities.
            api_response = await api_instance.list_order_graph_placement_children(scope, code, as_at=as_at, pagination_token=pagination_token, sort_by=sort_by, limit=limit, property_keys=property_keys)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling OrderGraphApi->list_order_graph_placement_children: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The parent placement&#39;s scope | 
 **code** | **str**| The parent placement&#39;s code | 
 **as_at** | **datetime**| See https://support.lusid.com/knowledgebase/article/KA-01832/ | [optional] 
 **pagination_token** | **str**| See https://support.lusid.com/knowledgebase/article/KA-01915/ | [optional] 
 **sort_by** | [**List[str]**](str.md)| Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName. | [optional] 
 **limit** | **int**| See https://support.lusid.com/knowledgebase/article/KA-01915/ | [optional] 
 **property_keys** | [**List[str]**](str.md)| Must be placement properties. See https://support.lusid.com/knowledgebase/article/KA-01855/ | [optional] 

### Return type

[**PagedResourceListOfOrderGraphPlacement**](PagedResourceListOfOrderGraphPlacement.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List all child Placements for the specified Placement. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_order_graph_placements**
> PagedResourceListOfOrderGraphPlacement list_order_graph_placements(as_at=as_at, pagination_token=pagination_token, sort_by=sort_by, limit=limit, filter=filter, property_keys=property_keys)

[EARLY ACCESS] ListOrderGraphPlacements: Lists placements that pass the filter provided, and builds a summary picture of the state of their associated order entities.

Lists all order placements, subject to the filter, along with the IDs of the block and order that the  placement is for, each placement's quantity, the IDs of all allocations and executions in the placement  and the total quantities of those, and a simple text field describing the overall state of the placement.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    OrderGraphApi
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
        api_instance = api_client_factory.build(OrderGraphApi)
        as_at = '2013-10-20T19:20:30+01:00' # datetime | See https://support.lusid.com/knowledgebase/article/KA-01832/ (optional)
        pagination_token = 'pagination_token_example' # str | See https://support.lusid.com/knowledgebase/article/KA-01915/ (optional)
        sort_by = ['sort_by_example'] # List[str] | A list of field names or properties to sort by, each suffixed by \" ASC\" or \" DESC\". (optional)
        limit = 56 # int | See https://support.lusid.com/knowledgebase/article/KA-01915/ (optional)
        filter = '' # str | See https://support.lusid.com/knowledgebase/article/KA-01914/ (optional) (default to '')
        property_keys = ['property_keys_example'] # List[str] | Must be placement properties. See https://support.lusid.com/knowledgebase/article/KA-01855/ (optional)

        try:
            # [EARLY ACCESS] ListOrderGraphPlacements: Lists placements that pass the filter provided, and builds a summary picture of the state of their associated order entities.
            api_response = await api_instance.list_order_graph_placements(as_at=as_at, pagination_token=pagination_token, sort_by=sort_by, limit=limit, filter=filter, property_keys=property_keys)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling OrderGraphApi->list_order_graph_placements: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| See https://support.lusid.com/knowledgebase/article/KA-01832/ | [optional] 
 **pagination_token** | **str**| See https://support.lusid.com/knowledgebase/article/KA-01915/ | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 
 **limit** | **int**| See https://support.lusid.com/knowledgebase/article/KA-01915/ | [optional] 
 **filter** | **str**| See https://support.lusid.com/knowledgebase/article/KA-01914/ | [optional] [default to &#39;&#39;]
 **property_keys** | [**List[str]**](str.md)| Must be placement properties. See https://support.lusid.com/knowledgebase/article/KA-01855/ | [optional] 

### Return type

[**PagedResourceListOfOrderGraphPlacement**](PagedResourceListOfOrderGraphPlacement.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Placements in scope. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

