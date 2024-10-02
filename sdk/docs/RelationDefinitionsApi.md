# lusid.RelationDefinitionsApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_relation_definition**](RelationDefinitionsApi.md#create_relation_definition) | **POST** /api/relationdefinitions | [EXPERIMENTAL] CreateRelationDefinition: Create a relation definition
[**delete_relation_definition**](RelationDefinitionsApi.md#delete_relation_definition) | **DELETE** /api/relationdefinitions/{scope}/{code} | [EXPERIMENTAL] DeleteRelationDefinition: Delete relation definition
[**get_relation_definition**](RelationDefinitionsApi.md#get_relation_definition) | **GET** /api/relationdefinitions/{scope}/{code} | [EXPERIMENTAL] GetRelationDefinition: Get relation definition


# **create_relation_definition**
> RelationDefinition create_relation_definition(create_relation_definition_request)

[EXPERIMENTAL] CreateRelationDefinition: Create a relation definition

Define a new relation.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    RelationDefinitionsApi
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
        api_instance = api_client_factory.build(RelationDefinitionsApi)

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # create_relation_definition_request = CreateRelationDefinitionRequest.from_json("")
        # create_relation_definition_request = CreateRelationDefinitionRequest.from_dict({})
        create_relation_definition_request = CreateRelationDefinitionRequest()

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.create_relation_definition(create_relation_definition_request, opts=opts)

            # [EXPERIMENTAL] CreateRelationDefinition: Create a relation definition
            api_response = await api_instance.create_relation_definition(create_relation_definition_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling RelationDefinitionsApi->create_relation_definition: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_relation_definition_request** | [**CreateRelationDefinitionRequest**](CreateRelationDefinitionRequest.md)| The definition of the new relation. | 

### Return type

[**RelationDefinition**](RelationDefinition.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created relation definition |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_relation_definition**
> DeletedEntityResponse delete_relation_definition(scope, code)

[EXPERIMENTAL] DeleteRelationDefinition: Delete relation definition

Delete the definition of the specified relation.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    RelationDefinitionsApi
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
        api_instance = api_client_factory.build(RelationDefinitionsApi)
        scope = 'scope_example' # str | The scope of the relation to be deleted.
        code = 'code_example' # str | The code of the relation to be deleted. Together with the domain and scope this uniquely              identifies the relation.

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.delete_relation_definition(scope, code, opts=opts)

            # [EXPERIMENTAL] DeleteRelationDefinition: Delete relation definition
            api_response = await api_instance.delete_relation_definition(scope, code)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling RelationDefinitionsApi->delete_relation_definition: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the relation to be deleted. | 
 **code** | **str**| The code of the relation to be deleted. Together with the domain and scope this uniquely              identifies the relation. | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The time that the relation definition was deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_relation_definition**
> RelationDefinition get_relation_definition(scope, code, as_at=as_at)

[EXPERIMENTAL] GetRelationDefinition: Get relation definition

Retrieve the definition of a specified relation.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    RelationDefinitionsApi
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
        api_instance = api_client_factory.build(RelationDefinitionsApi)
        scope = 'scope_example' # str | The scope of the specified relation.
        code = 'code_example' # str | The code of the specified relation. Together with the domain and scope this uniquely              identifies the relation.
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the relation definition. Defaults to return              the latest version of the definition if not specified. (optional)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.get_relation_definition(scope, code, as_at=as_at, opts=opts)

            # [EXPERIMENTAL] GetRelationDefinition: Get relation definition
            api_response = await api_instance.get_relation_definition(scope, code, as_at=as_at)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling RelationDefinitionsApi->get_relation_definition: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the specified relation. | 
 **code** | **str**| The code of the specified relation. Together with the domain and scope this uniquely              identifies the relation. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the relation definition. Defaults to return              the latest version of the definition if not specified. | [optional] 

### Return type

[**RelationDefinition**](RelationDefinition.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested relation definition |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

