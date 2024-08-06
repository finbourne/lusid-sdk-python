# lusid.CustomEntityDefinitionsApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_custom_entity_definition**](CustomEntityDefinitionsApi.md#create_custom_entity_definition) | **POST** /api/customentities/entitytypes | [EARLY ACCESS] CreateCustomEntityDefinition: Define a new Custom Entity type.
[**get_definition**](CustomEntityDefinitionsApi.md#get_definition) | **GET** /api/customentities/entitytypes/{entityType} | [EARLY ACCESS] GetDefinition: Get a Custom Entity type definition.
[**list_custom_entity_definitions**](CustomEntityDefinitionsApi.md#list_custom_entity_definitions) | **GET** /api/customentities/entitytypes | [EARLY ACCESS] ListCustomEntityDefinitions: List the Custom Entity type definitions
[**update_custom_entity_definition**](CustomEntityDefinitionsApi.md#update_custom_entity_definition) | **PUT** /api/customentities/entitytypes/{entityType} | [EARLY ACCESS] UpdateCustomEntityDefinition: Modify an existing Custom Entity type.


# **create_custom_entity_definition**
> CustomEntityDefinition create_custom_entity_definition(custom_entity_definition_request)

[EARLY ACCESS] CreateCustomEntityDefinition: Define a new Custom Entity type.

The API will return a Bad Request if the Custom Entity type already exists.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    CustomEntityDefinitionsApi
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
        api_instance = api_client_factory.build(CustomEntityDefinitionsApi)

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # custom_entity_definition_request = CustomEntityDefinitionRequest()
        # custom_entity_definition_request = CustomEntityDefinitionRequest.from_json("")
        custom_entity_definition_request = CustomEntityDefinitionRequest.from_dict({"entityTypeName":"SupportTicket","displayName":"Support Ticket","description":"Support Ticket","fieldSchema":[{"name":"clientId","lifetime":"Perpetual","type":"String","required":true},{"name":"issueDescription","lifetime":"TimeVariant","type":"String","required":true},{"name":"internalNotes","lifetime":"TimeVariant","type":"String","required":false},{"name":"isResolved","lifetime":"TimeVariant","type":"Boolean","required":false}]}) # CustomEntityDefinitionRequest | The payload containing the description of the Custom Entity type.

        try:
            # [EARLY ACCESS] CreateCustomEntityDefinition: Define a new Custom Entity type.
            api_response = await api_instance.create_custom_entity_definition(custom_entity_definition_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CustomEntityDefinitionsApi->create_custom_entity_definition: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_entity_definition_request** | [**CustomEntityDefinitionRequest**](CustomEntityDefinitionRequest.md)| The payload containing the description of the Custom Entity type. | 

### Return type

[**CustomEntityDefinition**](CustomEntityDefinition.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The created Custom Entity type. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_definition**
> CustomEntityDefinition get_definition(entity_type, as_at=as_at)

[EARLY ACCESS] GetDefinition: Get a Custom Entity type definition.

Retrieve a CustomEntityDefinition by a specific entityType at a point in AsAt time

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    CustomEntityDefinitionsApi
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
        api_instance = api_client_factory.build(CustomEntityDefinitionsApi)
        entity_type = 'entity_type_example' # str | The identifier for the Custom Entity type, derived from the \"entityTypeName\" provided on creation.
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The AsAt datetime at which to retrieve the definition. (optional)

        try:
            # [EARLY ACCESS] GetDefinition: Get a Custom Entity type definition.
            api_response = await api_instance.get_definition(entity_type, as_at=as_at)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CustomEntityDefinitionsApi->get_definition: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| The identifier for the Custom Entity type, derived from the \&quot;entityTypeName\&quot; provided on creation. | 
 **as_at** | **datetime**| The AsAt datetime at which to retrieve the definition. | [optional] 

### Return type

[**CustomEntityDefinition**](CustomEntityDefinition.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Custom Entity definition. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_custom_entity_definitions**
> PagedResourceListOfCustomEntityDefinition list_custom_entity_definitions(as_at=as_at, limit=limit, filter=filter, page=page)

[EARLY ACCESS] ListCustomEntityDefinitions: List the Custom Entity type definitions

List all Custom Entity type definitions matching particular criteria.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    CustomEntityDefinitionsApi
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
        api_instance = api_client_factory.build(CustomEntityDefinitionsApi)
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the entities. Defaults to returning the latest version              of each portfolio if not specified. (optional)
        limit = 56 # int | When paginating, limit the results to this number. Defaults to 100 if not specified. (optional)
        filter = 'filter_example' # str | Expression to filter the results. For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. (optional)
        page = 'page_example' # str | The pagination token to use to continue listing entities; this              value is returned from the previous call. If a pagination token is provided, the filter, limit              and asAt fields must not have changed since the original request. (optional)

        try:
            # [EARLY ACCESS] ListCustomEntityDefinitions: List the Custom Entity type definitions
            api_response = await api_instance.list_custom_entity_definitions(as_at=as_at, limit=limit, filter=filter, page=page)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CustomEntityDefinitionsApi->list_custom_entity_definitions: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list the entities. Defaults to returning the latest version              of each portfolio if not specified. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results. For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **page** | **str**| The pagination token to use to continue listing entities; this              value is returned from the previous call. If a pagination token is provided, the filter, limit              and asAt fields must not have changed since the original request. | [optional] 

### Return type

[**PagedResourceListOfCustomEntityDefinition**](PagedResourceListOfCustomEntityDefinition.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List Custom Entity type definitions. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **update_custom_entity_definition**
> CustomEntityDefinition update_custom_entity_definition(entity_type, update_custom_entity_definition_request)

[EARLY ACCESS] UpdateCustomEntityDefinition: Modify an existing Custom Entity type.

The API will return a Bad Request if the Custom Entity type does not exist.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    CustomEntityDefinitionsApi
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
        api_instance = api_client_factory.build(CustomEntityDefinitionsApi)
        entity_type = 'entity_type_example' # str | The identifier for the Custom Entity type, derived from the \"entityTypeName\" provided on creation.

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # update_custom_entity_definition_request = UpdateCustomEntityDefinitionRequest()
        # update_custom_entity_definition_request = UpdateCustomEntityDefinitionRequest.from_json("")
        update_custom_entity_definition_request = UpdateCustomEntityDefinitionRequest.from_dict({"displayName":"Support Ticket","description":"Support Ticket","fieldSchema":[{"name":"clientId","lifetime":"Perpetual","type":"String","required":true},{"name":"issueDescription","lifetime":"TimeVariant","type":"String","required":true},{"name":"internalNotes","lifetime":"TimeVariant","type":"String","required":false},{"name":"isResolved","lifetime":"TimeVariant","type":"Boolean","required":false}]}) # UpdateCustomEntityDefinitionRequest | The payload containing the description of the Custom Entity type.

        try:
            # [EARLY ACCESS] UpdateCustomEntityDefinition: Modify an existing Custom Entity type.
            api_response = await api_instance.update_custom_entity_definition(entity_type, update_custom_entity_definition_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CustomEntityDefinitionsApi->update_custom_entity_definition: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| The identifier for the Custom Entity type, derived from the \&quot;entityTypeName\&quot; provided on creation. | 
 **update_custom_entity_definition_request** | [**UpdateCustomEntityDefinitionRequest**](UpdateCustomEntityDefinitionRequest.md)| The payload containing the description of the Custom Entity type. | 

### Return type

[**CustomEntityDefinition**](CustomEntityDefinition.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated Custom Entity type. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

