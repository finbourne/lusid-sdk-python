# lusid.RelationalDatasetDefinitionApi

All URIs are relative to *https://fbn-prd.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_relational_dataset_definition**](RelationalDatasetDefinitionApi.md#create_relational_dataset_definition) | **POST** /api/relationaldatasetdefinitions | [EARLY ACCESS] CreateRelationalDatasetDefinition: Create a Relational Dataset Definition
[**delete_relational_dataset_definition**](RelationalDatasetDefinitionApi.md#delete_relational_dataset_definition) | **DELETE** /api/relationaldatasetdefinitions/{scope}/{code} | [EARLY ACCESS] DeleteRelationalDatasetDefinition: Delete a Relational Dataset Definition
[**get_relational_dataset_definition**](RelationalDatasetDefinitionApi.md#get_relational_dataset_definition) | **GET** /api/relationaldatasetdefinitions/{scope}/{code} | [EARLY ACCESS] GetRelationalDatasetDefinition: Get a Relational Dataset Definition
[**list_relational_dataset_definitions**](RelationalDatasetDefinitionApi.md#list_relational_dataset_definitions) | **GET** /api/relationaldatasetdefinitions | [EARLY ACCESS] ListRelationalDatasetDefinitions: List Relational Dataset Definitions
[**update_relational_dataset_definition**](RelationalDatasetDefinitionApi.md#update_relational_dataset_definition) | **PUT** /api/relationaldatasetdefinitions/{scope}/{code} | [EARLY ACCESS] UpdateRelationalDatasetDefinition: Update a Relational Dataset Definition


# **create_relational_dataset_definition**
> RelationalDatasetDefinition create_relational_dataset_definition(create_relational_dataset_definition_request)

[EARLY ACCESS] CreateRelationalDatasetDefinition: Create a Relational Dataset Definition

Create a new relational dataset definition.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    RelationalDatasetDefinitionApi
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
    api_instance = api_client_factory.build(RelationalDatasetDefinitionApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # create_relational_dataset_definition_request = CreateRelationalDatasetDefinitionRequest.from_json("")
    # create_relational_dataset_definition_request = CreateRelationalDatasetDefinitionRequest.from_dict({})
    create_relational_dataset_definition_request = CreateRelationalDatasetDefinitionRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.create_relational_dataset_definition(create_relational_dataset_definition_request, opts=opts)

        # [EARLY ACCESS] CreateRelationalDatasetDefinition: Create a Relational Dataset Definition
        api_response = api_instance.create_relational_dataset_definition(create_relational_dataset_definition_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling RelationalDatasetDefinitionApi->create_relational_dataset_definition: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_relational_dataset_definition_request** | [**CreateRelationalDatasetDefinitionRequest**](CreateRelationalDatasetDefinitionRequest.md)| The relational dataset definition to create. | 

### Return type

[**RelationalDatasetDefinition**](RelationalDatasetDefinition.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created relational dataset definition. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_relational_dataset_definition**
> DeletedEntityResponse delete_relational_dataset_definition(scope, code)

[EARLY ACCESS] DeleteRelationalDatasetDefinition: Delete a Relational Dataset Definition

Delete a relational dataset definition.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    RelationalDatasetDefinitionApi
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
    api_instance = api_client_factory.build(RelationalDatasetDefinitionApi)
    scope = 'scope_example' # str | The scope of the relational dataset definition.
    code = 'code_example' # str | The code of the relational dataset definition.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_relational_dataset_definition(scope, code, opts=opts)

        # [EARLY ACCESS] DeleteRelationalDatasetDefinition: Delete a Relational Dataset Definition
        api_response = api_instance.delete_relational_dataset_definition(scope, code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling RelationalDatasetDefinitionApi->delete_relational_dataset_definition: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the relational dataset definition. | 
 **code** | **str**| The code of the relational dataset definition. | 

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

# **get_relational_dataset_definition**
> RelationalDatasetDefinition get_relational_dataset_definition(scope, code, as_at=as_at)

[EARLY ACCESS] GetRelationalDatasetDefinition: Get a Relational Dataset Definition

Retrieve a relational dataset definition by its identifier.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    RelationalDatasetDefinitionApi
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
    api_instance = api_client_factory.build(RelationalDatasetDefinitionApi)
    scope = 'scope_example' # str | The scope of the relational dataset definition.
    code = 'code_example' # str | The code of the relational dataset definition.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the relational dataset definition. Defaults to return the latest version if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_relational_dataset_definition(scope, code, as_at=as_at, opts=opts)

        # [EARLY ACCESS] GetRelationalDatasetDefinition: Get a Relational Dataset Definition
        api_response = api_instance.get_relational_dataset_definition(scope, code, as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling RelationalDatasetDefinitionApi->get_relational_dataset_definition: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the relational dataset definition. | 
 **code** | **str**| The code of the relational dataset definition. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the relational dataset definition. Defaults to return the latest version if not specified. | [optional] 

### Return type

[**RelationalDatasetDefinition**](RelationalDatasetDefinition.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested relational dataset definition. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_relational_dataset_definitions**
> PagedResourceListOfRelationalDatasetDefinition list_relational_dataset_definitions(as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter)

[EARLY ACCESS] ListRelationalDatasetDefinitions: List Relational Dataset Definitions

List all relational dataset definitions matching particular criteria.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    RelationalDatasetDefinitionApi
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
    api_instance = api_client_factory.build(RelationalDatasetDefinitionApi)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the relational dataset definitions. Defaults to return the latest version if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing relational dataset definitions from a previous call to list relational dataset definitions. (optional)
    sort_by = ['sort_by_example'] # List[str] | A list of field names to sort by, each suffixed by \" ASC\" or \" DESC\" (optional)
    limit = 56 # int | When paginating, limit the number of returned results to this many. (optional)
    filter = 'filter_example' # str | Expression to filter the result set. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_relational_dataset_definitions(as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter, opts=opts)

        # [EARLY ACCESS] ListRelationalDatasetDefinitions: List Relational Dataset Definitions
        api_response = api_instance.list_relational_dataset_definitions(as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling RelationalDatasetDefinitionApi->list_relational_dataset_definitions: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list the relational dataset definitions. Defaults to return the latest version if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing relational dataset definitions from a previous call to list relational dataset definitions. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot; | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Expression to filter the result set. | [optional] 

### Return type

[**PagedResourceListOfRelationalDatasetDefinition**](PagedResourceListOfRelationalDatasetDefinition.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of relational dataset definitions. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **update_relational_dataset_definition**
> RelationalDatasetDefinition update_relational_dataset_definition(scope, code, update_relational_dataset_definition_request=update_relational_dataset_definition_request)

[EARLY ACCESS] UpdateRelationalDatasetDefinition: Update a Relational Dataset Definition

Update an existing relational dataset definition.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    RelationalDatasetDefinitionApi
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
    api_instance = api_client_factory.build(RelationalDatasetDefinitionApi)
    scope = 'scope_example' # str | The scope of the relational dataset definition.
    code = 'code_example' # str | The code of the relational dataset definition.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # update_relational_dataset_definition_request = UpdateRelationalDatasetDefinitionRequest.from_json("")
    # update_relational_dataset_definition_request = UpdateRelationalDatasetDefinitionRequest.from_dict({})
    update_relational_dataset_definition_request = UpdateRelationalDatasetDefinitionRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.update_relational_dataset_definition(scope, code, update_relational_dataset_definition_request=update_relational_dataset_definition_request, opts=opts)

        # [EARLY ACCESS] UpdateRelationalDatasetDefinition: Update a Relational Dataset Definition
        api_response = api_instance.update_relational_dataset_definition(scope, code, update_relational_dataset_definition_request=update_relational_dataset_definition_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling RelationalDatasetDefinitionApi->update_relational_dataset_definition: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the relational dataset definition. | 
 **code** | **str**| The code of the relational dataset definition. | 
 **update_relational_dataset_definition_request** | [**UpdateRelationalDatasetDefinitionRequest**](UpdateRelationalDatasetDefinitionRequest.md)| The updated relational dataset definition. | [optional] 

### Return type

[**RelationalDatasetDefinition**](RelationalDatasetDefinition.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated relational dataset definition. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

