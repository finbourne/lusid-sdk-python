# lusid.EntityResolversApi

All URIs are relative to *https://fbn-prd.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_entity_resolver**](EntityResolversApi.md#create_entity_resolver) | **POST** /api/entityresolvers | [EXPERIMENTAL] CreateEntityResolver: Create an Entity Resolver
[**delete_entity_resolver**](EntityResolversApi.md#delete_entity_resolver) | **DELETE** /api/entityresolvers/{scope}/{code} | [EXPERIMENTAL] DeleteEntityResolver: Delete an Entity Resolver
[**get_entity_resolver**](EntityResolversApi.md#get_entity_resolver) | **GET** /api/entityresolvers/{scope}/{code} | [EXPERIMENTAL] GetEntityResolver: Get a single Entity Resolver
[**update_entity_resolver**](EntityResolversApi.md#update_entity_resolver) | **PUT** /api/entityresolvers/{scope}/{code} | [EXPERIMENTAL] UpdateEntityResolver: Update an Entity Resolver


# **create_entity_resolver**
> EntityResolver create_entity_resolver(create_entity_resolver_request=create_entity_resolver_request)

[EXPERIMENTAL] CreateEntityResolver: Create an Entity Resolver

Define a new Entity Resolver. The resolver's identifier matching order is the sequence of identifier  property keys that will be tried, in turn, when resolving an entity of the given type in the resolver's scope.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    EntityResolversApi
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
    api_instance = api_client_factory.build(EntityResolversApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # create_entity_resolver_request = CreateEntityResolverRequest.from_json("")
    # create_entity_resolver_request = CreateEntityResolverRequest.from_dict({})
    create_entity_resolver_request = CreateEntityResolverRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.create_entity_resolver(create_entity_resolver_request=create_entity_resolver_request, opts=opts)

        # [EXPERIMENTAL] CreateEntityResolver: Create an Entity Resolver
        api_response = api_instance.create_entity_resolver(create_entity_resolver_request=create_entity_resolver_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling EntityResolversApi->create_entity_resolver: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_entity_resolver_request** | [**CreateEntityResolverRequest**](CreateEntityResolverRequest.md)| The request defining the new Entity Resolver | [optional] 

### Return type

[**EntityResolver**](EntityResolver.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created Entity Resolver |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_entity_resolver**
> DeletedEntityResponse delete_entity_resolver(scope, code)

[EXPERIMENTAL] DeleteEntityResolver: Delete an Entity Resolver

The deletion will take effect from the deletion datetime, i.e. the Entity Resolver will no longer exist  at any asAt datetime after the asAt datetime of deletion. Resolution in the affected scope reverts to  the default matching order.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    EntityResolversApi
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
    api_instance = api_client_factory.build(EntityResolversApi)
    scope = 'scope_example' # str | The scope of the Entity Resolver
    code = 'code_example' # str | The code of the Entity Resolver. Together with the scope this uniquely identifies the Entity Resolver

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_entity_resolver(scope, code, opts=opts)

        # [EXPERIMENTAL] DeleteEntityResolver: Delete an Entity Resolver
        api_response = api_instance.delete_entity_resolver(scope, code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling EntityResolversApi->delete_entity_resolver: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Entity Resolver | 
 **code** | **str**| The code of the Entity Resolver. Together with the scope this uniquely identifies the Entity Resolver | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The deleted entity metadata |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_entity_resolver**
> EntityResolver get_entity_resolver(scope, code, as_at=as_at)

[EXPERIMENTAL] GetEntityResolver: Get a single Entity Resolver

Get a single Entity Resolver by scope and code at an optional asAt, defaulting to latest if not specified.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    EntityResolversApi
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
    api_instance = api_client_factory.build(EntityResolversApi)
    scope = 'scope_example' # str | The scope of the Entity Resolver
    code = 'code_example' # str | The code of the Entity Resolver. Together with the scope this uniquely identifies the Entity Resolver
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Entity Resolver. Defaults to return              the latest version if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_entity_resolver(scope, code, as_at=as_at, opts=opts)

        # [EXPERIMENTAL] GetEntityResolver: Get a single Entity Resolver
        api_response = api_instance.get_entity_resolver(scope, code, as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling EntityResolversApi->get_entity_resolver: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Entity Resolver | 
 **code** | **str**| The code of the Entity Resolver. Together with the scope this uniquely identifies the Entity Resolver | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Entity Resolver. Defaults to return              the latest version if not specified. | [optional] 

### Return type

[**EntityResolver**](EntityResolver.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Entity Resolver |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **update_entity_resolver**
> EntityResolver update_entity_resolver(scope, code, upsert_entity_resolver_request=upsert_entity_resolver_request)

[EXPERIMENTAL] UpdateEntityResolver: Update an Entity Resolver

Overwrites the description and identifier matching order of an existing Entity Resolver.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    EntityResolversApi
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
    api_instance = api_client_factory.build(EntityResolversApi)
    scope = 'scope_example' # str | The scope of the Entity Resolver
    code = 'code_example' # str | The code of the Entity Resolver. Together with the scope this uniquely identifies the Entity Resolver

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # upsert_entity_resolver_request = UpsertEntityResolverRequest.from_json("")
    # upsert_entity_resolver_request = UpsertEntityResolverRequest.from_dict({})
    upsert_entity_resolver_request = UpsertEntityResolverRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.update_entity_resolver(scope, code, upsert_entity_resolver_request=upsert_entity_resolver_request, opts=opts)

        # [EXPERIMENTAL] UpdateEntityResolver: Update an Entity Resolver
        api_response = api_instance.update_entity_resolver(scope, code, upsert_entity_resolver_request=upsert_entity_resolver_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling EntityResolversApi->update_entity_resolver: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Entity Resolver | 
 **code** | **str**| The code of the Entity Resolver. Together with the scope this uniquely identifies the Entity Resolver | 
 **upsert_entity_resolver_request** | [**UpsertEntityResolverRequest**](UpsertEntityResolverRequest.md)| The request containing the updated details of the Entity Resolver | [optional] 

### Return type

[**EntityResolver**](EntityResolver.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated Entity Resolver |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

