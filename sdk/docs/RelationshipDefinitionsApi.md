# lusid.RelationshipDefinitionsApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_relationship_definition**](RelationshipDefinitionsApi.md#create_relationship_definition) | **POST** /api/relationshipdefinitions | [EARLY ACCESS] CreateRelationshipDefinition: Create Relationship Definition
[**delete_relationship_definition**](RelationshipDefinitionsApi.md#delete_relationship_definition) | **DELETE** /api/relationshipdefinitions/{scope}/{code} | [EARLY ACCESS] DeleteRelationshipDefinition: Delete Relationship Definition
[**get_relationship_definition**](RelationshipDefinitionsApi.md#get_relationship_definition) | **GET** /api/relationshipdefinitions/{scope}/{code} | [EARLY ACCESS] GetRelationshipDefinition: Get relationship definition
[**list_relationship_definitions**](RelationshipDefinitionsApi.md#list_relationship_definitions) | **GET** /api/relationshipdefinitions | [EARLY ACCESS] ListRelationshipDefinitions: List relationship definitions
[**update_relationship_definition**](RelationshipDefinitionsApi.md#update_relationship_definition) | **PUT** /api/relationshipdefinitions/{scope}/{code} | [EARLY ACCESS] UpdateRelationshipDefinition: Update Relationship Definition


# **create_relationship_definition**
> RelationshipDefinition create_relationship_definition(create_relationship_definition_request)

[EARLY ACCESS] CreateRelationshipDefinition: Create Relationship Definition

Create a new relationship definition to be used for creating relationships between entities.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    RelationshipDefinitionsApi
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
        api_instance = api_client_factory.build(RelationshipDefinitionsApi)

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # create_relationship_definition_request = CreateRelationshipDefinitionRequest()
        # create_relationship_definition_request = CreateRelationshipDefinitionRequest.from_json("")
        create_relationship_definition_request = CreateRelationshipDefinitionRequest.from_dict({"scope":"PortfolioManagementTeam","code":"Traders","sourceEntityType":"Portfolio","targetEntityType":"Person","displayName":"Authorised traders to trade for specific portfolio ","outwardDescription":"can be traded by","inwardDescription":"can trade with portfolio","lifeTime":"TimeVariant","relationshipCardinality":"ManyToMany"}) # CreateRelationshipDefinitionRequest | The definition of the new relationship.

        try:
            # [EARLY ACCESS] CreateRelationshipDefinition: Create Relationship Definition
            api_response = await api_instance.create_relationship_definition(create_relationship_definition_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling RelationshipDefinitionsApi->create_relationship_definition: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_relationship_definition_request** | [**CreateRelationshipDefinitionRequest**](CreateRelationshipDefinitionRequest.md)| The definition of the new relationship. | 

### Return type

[**RelationshipDefinition**](RelationshipDefinition.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created relationship definition |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_relationship_definition**
> DeletedEntityResponse delete_relationship_definition(scope, code)

[EARLY ACCESS] DeleteRelationshipDefinition: Delete Relationship Definition

Delete the definition of the specified relationship.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    RelationshipDefinitionsApi
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
        api_instance = api_client_factory.build(RelationshipDefinitionsApi)
        scope = 'scope_example' # str | The scope of the relationship definition to be deleted.
        code = 'code_example' # str | The code of the relationship definition to be deleted. Together with the domain and scope this uniquely              identifies the relationship.

        try:
            # [EARLY ACCESS] DeleteRelationshipDefinition: Delete Relationship Definition
            api_response = await api_instance.delete_relationship_definition(scope, code)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling RelationshipDefinitionsApi->delete_relationship_definition: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the relationship definition to be deleted. | 
 **code** | **str**| The code of the relationship definition to be deleted. Together with the domain and scope this uniquely              identifies the relationship. | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The time that the relationship definition was deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_relationship_definition**
> RelationshipDefinition get_relationship_definition(scope, code, as_at=as_at)

[EARLY ACCESS] GetRelationshipDefinition: Get relationship definition

Retrieve the specified relationship definition

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    RelationshipDefinitionsApi
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
        api_instance = api_client_factory.build(RelationshipDefinitionsApi)
        scope = 'scope_example' # str | The scope of the specified relationship definition.
        code = 'code_example' # str | The code of the specified relationship definition. Together with the domain and scope this uniquely              identifies the relationship definition.
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the relationship definition. Defaults to return              the latest version of the definition if not specified. (optional)

        try:
            # [EARLY ACCESS] GetRelationshipDefinition: Get relationship definition
            api_response = await api_instance.get_relationship_definition(scope, code, as_at=as_at)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling RelationshipDefinitionsApi->get_relationship_definition: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the specified relationship definition. | 
 **code** | **str**| The code of the specified relationship definition. Together with the domain and scope this uniquely              identifies the relationship definition. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the relationship definition. Defaults to return              the latest version of the definition if not specified. | [optional] 

### Return type

[**RelationshipDefinition**](RelationshipDefinition.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested relationship definition |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_relationship_definitions**
> PagedResourceListOfRelationshipDefinition list_relationship_definitions(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)

[EARLY ACCESS] ListRelationshipDefinitions: List relationship definitions

Retrieve one or more specified relationship definitions.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    RelationshipDefinitionsApi
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
        api_instance = api_client_factory.build(RelationshipDefinitionsApi)
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the relationship definitions. Defaults to return              the latest version of each definition if not specified. (optional)
        page = 'page_example' # str | The pagination token to use to continue listing relationship definitions from a previous call to list relationship definitions. This  value is returned from the previous call. If a pagination token is provided the filter, sortBy and asAt field  must not have changed since the original request. (optional)
        limit = 56 # int | When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. (optional)
        filter = 'filter_example' # str | Expression to filter the result set.              For example, to filter on the Scope, use \"scope eq 'ExampleScope'\"              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)
        sort_by = ['sort_by_example'] # List[str] | A list of field names to sort by, each suffixed by \" ASC\" or \" DESC\" (optional)

        try:
            # [EARLY ACCESS] ListRelationshipDefinitions: List relationship definitions
            api_response = await api_instance.list_relationship_definitions(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling RelationshipDefinitionsApi->list_relationship_definitions: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to retrieve the relationship definitions. Defaults to return              the latest version of each definition if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing relationship definitions from a previous call to list relationship definitions. This  value is returned from the previous call. If a pagination token is provided the filter, sortBy and asAt field  must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set.              For example, to filter on the Scope, use \&quot;scope eq &#39;ExampleScope&#39;\&quot;              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot; | [optional] 

### Return type

[**PagedResourceListOfRelationshipDefinition**](PagedResourceListOfRelationshipDefinition.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested relationship definitions |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **update_relationship_definition**
> RelationshipDefinition update_relationship_definition(scope, code, update_relationship_definition_request)

[EARLY ACCESS] UpdateRelationshipDefinition: Update Relationship Definition

Update the definition of a specified existing relationship. Not all elements within a relationship definition  are modifiable due to the potential implications for values already stored against the relationship.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    RelationshipDefinitionsApi
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
        api_instance = api_client_factory.build(RelationshipDefinitionsApi)
        scope = 'scope_example' # str | The scope of the relationship definition being updated.
        code = 'code_example' # str | The code of the relationship definition being updated. Together with the scope this uniquely              identifies the relationship definition.

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # update_relationship_definition_request = UpdateRelationshipDefinitionRequest()
        # update_relationship_definition_request = UpdateRelationshipDefinitionRequest.from_json("")
        update_relationship_definition_request = UpdateRelationshipDefinitionRequest.from_dict({"displayName":"Authorised traders to trade for specific portfolio ","outwardDescription":"can be traded by","inwardDescription":"can trade with portfolio"}) # UpdateRelationshipDefinitionRequest | The details of relationship definition to update.

        try:
            # [EARLY ACCESS] UpdateRelationshipDefinition: Update Relationship Definition
            api_response = await api_instance.update_relationship_definition(scope, code, update_relationship_definition_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling RelationshipDefinitionsApi->update_relationship_definition: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the relationship definition being updated. | 
 **code** | **str**| The code of the relationship definition being updated. Together with the scope this uniquely              identifies the relationship definition. | 
 **update_relationship_definition_request** | [**UpdateRelationshipDefinitionRequest**](UpdateRelationshipDefinitionRequest.md)| The details of relationship definition to update. | 

### Return type

[**RelationshipDefinition**](RelationshipDefinition.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated relationship definition |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

