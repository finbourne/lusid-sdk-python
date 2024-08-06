# lusid.ExecutionsApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_execution**](ExecutionsApi.md#delete_execution) | **DELETE** /api/executions/{scope}/{code} | [EARLY ACCESS] DeleteExecution: Delete execution
[**get_execution**](ExecutionsApi.md#get_execution) | **GET** /api/executions/{scope}/{code} | [EARLY ACCESS] GetExecution: Get Execution
[**list_executions**](ExecutionsApi.md#list_executions) | **GET** /api/executions | ListExecutions: List Executions
[**upsert_executions**](ExecutionsApi.md#upsert_executions) | **POST** /api/executions | UpsertExecutions: Upsert Execution


# **delete_execution**
> DeletedEntityResponse delete_execution(scope, code)

[EARLY ACCESS] DeleteExecution: Delete execution

Delete an execution. Deletion will be valid from the execution's creation datetime.  This means that the execution will no longer exist at any effective datetime from the asAt datetime of deletion.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    ExecutionsApi
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
        api_instance = api_client_factory.build(ExecutionsApi)
        scope = 'scope_example' # str | The execution scope.
        code = 'code_example' # str | The execution's code. This, together with the scope uniquely identifies the execution to delete.

        try:
            # [EARLY ACCESS] DeleteExecution: Delete execution
            api_response = await api_instance.delete_execution(scope, code)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling ExecutionsApi->delete_execution: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The execution scope. | 
 **code** | **str**| The execution&#39;s code. This, together with the scope uniquely identifies the execution to delete. | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response from deleting an execution. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_execution**
> Execution get_execution(scope, code, as_at=as_at, property_keys=property_keys)

[EARLY ACCESS] GetExecution: Get Execution

Fetch a Execution that matches the specified identifier

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    ExecutionsApi
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
        api_instance = api_client_factory.build(ExecutionsApi)
        scope = 'scope_example' # str | The scope to which the execution belongs.
        code = 'code_example' # str | The execution's unique identifier.
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the execution. Defaults to return the latest version of the execution if not specified. (optional)
        property_keys = ['property_keys_example'] # List[str] | A list of property keys from the \"Execution\" domain to decorate onto the execution.              These take the format {domain}/{scope}/{code} e.g. \"Execution/system/Name\". (optional)

        try:
            # [EARLY ACCESS] GetExecution: Get Execution
            api_response = await api_instance.get_execution(scope, code, as_at=as_at, property_keys=property_keys)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling ExecutionsApi->get_execution: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope to which the execution belongs. | 
 **code** | **str**| The execution&#39;s unique identifier. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the execution. Defaults to return the latest version of the execution if not specified. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the \&quot;Execution\&quot; domain to decorate onto the execution.              These take the format {domain}/{scope}/{code} e.g. \&quot;Execution/system/Name\&quot;. | [optional] 

### Return type

[**Execution**](Execution.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The execution matching the given identifier. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_executions**
> PagedResourceListOfExecution list_executions(as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter, property_keys=property_keys)

ListExecutions: List Executions

Fetch the last pre-AsAt date version of each execution in scope (does not fetch the entire history).

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    ExecutionsApi
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
        api_instance = api_client_factory.build(ExecutionsApi)
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the execution. Defaults to return the latest version of the execution if not specified. (optional)
        page = 'page_example' # str | The pagination token to use to continue listing execution from a previous call to list executions.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields              must not have changed since the original request. (optional)
        sort_by = ['sort_by_example'] # List[str] | A list of field names or properties to sort by, each suffixed by \" ASC\" or \" DESC\". (optional)
        limit = 56 # int | When paginating, limit the number of returned results to this many. (optional)
        filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid. (optional)
        property_keys = ['property_keys_example'] # List[str] | A list of property keys from the \"Execution\" domain to decorate onto each execution.                  These take the format {domain}/{scope}/{code} e.g. \"Execution/system/Name\". (optional)

        try:
            # ListExecutions: List Executions
            api_response = await api_instance.list_executions(as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter, property_keys=property_keys)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling ExecutionsApi->list_executions: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to retrieve the execution. Defaults to return the latest version of the execution if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing execution from a previous call to list executions.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields              must not have changed since the original request. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the \&quot;Execution\&quot; domain to decorate onto each execution.                  These take the format {domain}/{scope}/{code} e.g. \&quot;Execution/system/Name\&quot;. | [optional] 

### Return type

[**PagedResourceListOfExecution**](PagedResourceListOfExecution.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Executions in scope. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **upsert_executions**
> ResourceListOfExecution upsert_executions(execution_set_request=execution_set_request)

UpsertExecutions: Upsert Execution

Upsert; update existing executions with given ids, or create new executions otherwise.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    ExecutionsApi
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
        api_instance = api_client_factory.build(ExecutionsApi)

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # execution_set_request = ExecutionSetRequest()
        # execution_set_request = ExecutionSetRequest.from_json("")
        execution_set_request = ExecutionSetRequest.from_dict({"requests":[{"id":{"scope":"MyScope","code":"EXEC00000123"},"placementId":{"scope":"MyScope","code":"PLAC00000123"},"properties":{"Execution/MyScope/SomeExecutionProperty":{"key":"Execution/MyScope/SomeExecutionProperty","value":{"labelValue":"XYZ000034567"}}},"instrumentIdentifiers":{"Instrument/default/Currency":"GBP"},"quantity":100,"state":"New","side":"Buy","type":"Limit","createdDate":"2006-04-11T00:00:00.0000000+00:00","settlementDate":"2006-04-13T00:00:00.0000000+00:00","price":{"amount":12413.33,"currency":"USD"},"settlementCurrency":"GBP","settlementCurrencyFxRate":0.67,"counterparty":"SomeCounterparty","averagePrice":12419.2}]}) # ExecutionSetRequest | The collection of execution requests. (optional)

        try:
            # UpsertExecutions: Upsert Execution
            api_response = await api_instance.upsert_executions(execution_set_request=execution_set_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling ExecutionsApi->upsert_executions: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execution_set_request** | [**ExecutionSetRequest**](ExecutionSetRequest.md)| The collection of execution requests. | [optional] 

### Return type

[**ResourceListOfExecution**](ResourceListOfExecution.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A collection of executions. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

