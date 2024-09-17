# lusid.AllocationsApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_allocation**](AllocationsApi.md#delete_allocation) | **DELETE** /api/allocations/{scope}/{code} | [EARLY ACCESS] DeleteAllocation: Delete allocation
[**get_allocation**](AllocationsApi.md#get_allocation) | **GET** /api/allocations/{scope}/{code} | [EARLY ACCESS] GetAllocation: Get Allocation
[**list_allocations**](AllocationsApi.md#list_allocations) | **GET** /api/allocations | ListAllocations: List Allocations
[**upsert_allocations**](AllocationsApi.md#upsert_allocations) | **POST** /api/allocations | UpsertAllocations: Upsert Allocations


# **delete_allocation**
> DeletedEntityResponse delete_allocation(scope, code)

[EARLY ACCESS] DeleteAllocation: Delete allocation

Delete an allocation. Deletion will be valid from the allocation's creation datetime.  This means that the allocation will no longer exist at any effective datetime from the asAt datetime of deletion.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    AllocationsApi
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
        api_instance = api_client_factory.build(AllocationsApi)
        scope = 'scope_example' # str | The allocation scope.
        code = 'code_example' # str | The allocation's code. This, together with the scope uniquely identifies the allocation to delete.

        try:
            # [EARLY ACCESS] DeleteAllocation: Delete allocation
            api_response = await api_instance.delete_allocation(scope, code)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling AllocationsApi->delete_allocation: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The allocation scope. | 
 **code** | **str**| The allocation&#39;s code. This, together with the scope uniquely identifies the allocation to delete. | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response from deleting an allocation. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_allocation**
> Allocation get_allocation(scope, code, as_at=as_at, property_keys=property_keys)

[EARLY ACCESS] GetAllocation: Get Allocation

Fetch an Allocation matching the provided identifier

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    AllocationsApi
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
        api_instance = api_client_factory.build(AllocationsApi)
        scope = 'scope_example' # str | The scope to which the allocation belongs.
        code = 'code_example' # str | The allocation's unique identifier.
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the allocation. Defaults to return the latest version of the allocation if not specified. (optional)
        property_keys = ['property_keys_example'] # List[str] | A list of property keys from the \"Allocations\" domain to decorate onto the allocation.              These take the format {domain}/{scope}/{code} e.g. \"Allocations/system/Name\". (optional)

        try:
            # [EARLY ACCESS] GetAllocation: Get Allocation
            api_response = await api_instance.get_allocation(scope, code, as_at=as_at, property_keys=property_keys)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling AllocationsApi->get_allocation: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope to which the allocation belongs. | 
 **code** | **str**| The allocation&#39;s unique identifier. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the allocation. Defaults to return the latest version of the allocation if not specified. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the \&quot;Allocations\&quot; domain to decorate onto the allocation.              These take the format {domain}/{scope}/{code} e.g. \&quot;Allocations/system/Name\&quot;. | [optional] 

### Return type

[**Allocation**](Allocation.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The allocation matching the given identifier. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_allocations**
> PagedResourceListOfAllocation list_allocations(as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter, property_keys=property_keys)

ListAllocations: List Allocations

Fetch the last pre-AsAt date version of each allocation in scope (does not fetch the entire history).

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    AllocationsApi
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
        api_instance = api_client_factory.build(AllocationsApi)
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the allocation. Defaults to return the latest version of the allocation if not specified. (optional)
        page = 'page_example' # str | The pagination token to use to continue listing allocations from a previous call to list allocations.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields              must not have changed since the original request. (optional)
        sort_by = ['sort_by_example'] # List[str] | A list of field names or properties to sort by, each suffixed by \" ASC\" or \" DESC\". (optional)
        limit = 56 # int | When paginating, limit the number of returned results to this many. (optional)
        filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid. (optional)
        property_keys = ['property_keys_example'] # List[str] | A list of property keys from the \"Allocations\" domain to decorate onto each allocation.                  These take the format {domain}/{scope}/{code} e.g. \"Allocations/system/Name\". (optional)

        try:
            # ListAllocations: List Allocations
            api_response = await api_instance.list_allocations(as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter, property_keys=property_keys)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling AllocationsApi->list_allocations: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to retrieve the allocation. Defaults to return the latest version of the allocation if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing allocations from a previous call to list allocations.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields              must not have changed since the original request. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the \&quot;Allocations\&quot; domain to decorate onto each allocation.                  These take the format {domain}/{scope}/{code} e.g. \&quot;Allocations/system/Name\&quot;. | [optional] 

### Return type

[**PagedResourceListOfAllocation**](PagedResourceListOfAllocation.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Allocations. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **upsert_allocations**
> ResourceListOfAllocation upsert_allocations(allocation_set_request=allocation_set_request)

UpsertAllocations: Upsert Allocations

Upsert; update existing allocations with given ids, or create new allocations otherwise.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    AllocationsApi
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
        api_instance = api_client_factory.build(AllocationsApi)

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # allocation_set_request = AllocationSetRequest()
        # allocation_set_request = AllocationSetRequest.from_json("")
        allocation_set_request = AllocationSetRequest.from_dict({"allocationRequests":[{"properties":{"Allocation/MyScope/SomeAllocationProperty":{"key":"Allocation/MyScope/SomeAllocationProperty","value":{"labelValue":"XYZ000034567"}}},"instrumentIdentifiers":{"Instrument/default/Currency":"GBP"},"quantity":100,"portfolioId":{"scope":"MyScope","code":"UKEquity"},"allocatedOrderId":{"scope":"MyScope","code":"ORD00000123"},"id":{"scope":"MyScope","code":"ALLOC00000123"},"placementIds":[{"scope":"MyScope","code":"SomePlacement"}],"state":"New","side":"Buy","type":"Limit","settlementDate":"2006-04-14T00:00:00.0000000+00:00","date":"2006-04-11T00:00:00.0000000+00:00","price":{"amount":12413.33,"currency":"USD"},"settlementCurrency":"USD","settlementCurrencyFxRate":1,"counterparty":"SomeCounterparty","executionIds":[{"scope":"MyScope","code":"EXEC00000123"}]}]}) # AllocationSetRequest | The collection of allocation requests. (optional)

        try:
            # UpsertAllocations: Upsert Allocations
            api_response = await api_instance.upsert_allocations(allocation_set_request=allocation_set_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling AllocationsApi->upsert_allocations: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **allocation_set_request** | [**AllocationSetRequest**](AllocationSetRequest.md)| The collection of allocation requests. | [optional] 

### Return type

[**ResourceListOfAllocation**](ResourceListOfAllocation.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of allocations. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

