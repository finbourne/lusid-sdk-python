# lusid.CustomDataModelsApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_custom_data_model**](CustomDataModelsApi.md#create_custom_data_model) | **POST** /api/datamodel/{entityType} | [EXPERIMENTAL] CreateCustomDataModel: Create a Custom Data Model
[**delete_custom_data_model**](CustomDataModelsApi.md#delete_custom_data_model) | **DELETE** /api/datamodel/{entityType}/{scope}/{code} | [EXPERIMENTAL] DeleteCustomDataModel: Delete a Custom Data Model
[**get_custom_data_model**](CustomDataModelsApi.md#get_custom_data_model) | **GET** /api/datamodel/{entityType}/{scope}/{code} | [EXPERIMENTAL] GetCustomDataModel: Get a Custom Data Model
[**list_data_model_hierarchies**](CustomDataModelsApi.md#list_data_model_hierarchies) | **GET** /api/datamodel/hierarchies | [EXPERIMENTAL] ListDataModelHierarchies: List Custom Data Model hierarchies.
[**list_supported_entity_types**](CustomDataModelsApi.md#list_supported_entity_types) | **GET** /api/datamodel/entitytype | [EXPERIMENTAL] ListSupportedEntityTypes: List the currently supported entity types for use in Custom Data Models.
[**update_custom_data_model**](CustomDataModelsApi.md#update_custom_data_model) | **PUT** /api/datamodel/{entityType}/{scope}/{code} | [EXPERIMENTAL] UpdateCustomDataModel: Update a Custom Data Model


# **create_custom_data_model**
> CustomDataModel create_custom_data_model(entity_type, create_custom_data_model_request=create_custom_data_model_request)

[EXPERIMENTAL] CreateCustomDataModel: Create a Custom Data Model

Creates a Custom Data Model.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    CustomDataModelsApi
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
    api_instance = api_client_factory.build(CustomDataModelsApi)
    entity_type = 'entity_type_example' # str | The entity type of the Data Model.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # create_custom_data_model_request = CreateCustomDataModelRequest.from_json("")
    # create_custom_data_model_request = CreateCustomDataModelRequest.from_dict({})
    create_custom_data_model_request = CreateCustomDataModelRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.create_custom_data_model(entity_type, create_custom_data_model_request=create_custom_data_model_request, opts=opts)

        # [EXPERIMENTAL] CreateCustomDataModel: Create a Custom Data Model
        api_response = api_instance.create_custom_data_model(entity_type, create_custom_data_model_request=create_custom_data_model_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling CustomDataModelsApi->create_custom_data_model: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| The entity type of the Data Model. | 
 **create_custom_data_model_request** | [**CreateCustomDataModelRequest**](CreateCustomDataModelRequest.md)| The request containing the details of the Data Model. | [optional] 

### Return type

[**CustomDataModel**](CustomDataModel.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created Data Model |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_custom_data_model**
> DeletedEntityResponse delete_custom_data_model(entity_type, scope, code)

[EXPERIMENTAL] DeleteCustomDataModel: Delete a Custom Data Model

Delete a Custom Data Model. The data model will remain viewable at previous as at times, but will no longer  be part of any hierarchies.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    CustomDataModelsApi
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
    api_instance = api_client_factory.build(CustomDataModelsApi)
    entity_type = 'entity_type_example' # str | The entity type of the Data Model.
    scope = 'scope_example' # str | The scope of the specified Data Model.
    code = 'code_example' # str | The code of the specified Data Model.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_custom_data_model(entity_type, scope, code, opts=opts)

        # [EXPERIMENTAL] DeleteCustomDataModel: Delete a Custom Data Model
        api_response = api_instance.delete_custom_data_model(entity_type, scope, code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling CustomDataModelsApi->delete_custom_data_model: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| The entity type of the Data Model. | 
 **scope** | **str**| The scope of the specified Data Model. | 
 **code** | **str**| The code of the specified Data Model. | 

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

# **get_custom_data_model**
> CustomDataModel get_custom_data_model(entity_type, scope, code, as_at=as_at)

[EXPERIMENTAL] GetCustomDataModel: Get a Custom Data Model

Retrieves a Custom Data Model at a given as at time.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    CustomDataModelsApi
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
    api_instance = api_client_factory.build(CustomDataModelsApi)
    entity_type = 'entity_type_example' # str | The entity type of the Data Model.
    scope = 'scope_example' # str | The scope of the specified Data Model.
    code = 'code_example' # str | The code of the specified Data Model.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Data Model. Defaults to return              the latest version of the Data Model if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_custom_data_model(entity_type, scope, code, as_at=as_at, opts=opts)

        # [EXPERIMENTAL] GetCustomDataModel: Get a Custom Data Model
        api_response = api_instance.get_custom_data_model(entity_type, scope, code, as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling CustomDataModelsApi->get_custom_data_model: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| The entity type of the Data Model. | 
 **scope** | **str**| The scope of the specified Data Model. | 
 **code** | **str**| The code of the specified Data Model. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Data Model. Defaults to return              the latest version of the Data Model if not specified. | [optional] 

### Return type

[**CustomDataModel**](CustomDataModel.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The requested Data Model |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_data_model_hierarchies**
> ResourceListOfDataModelSummary list_data_model_hierarchies(as_at=as_at, filter=filter)

[EXPERIMENTAL] ListDataModelHierarchies: List Custom Data Model hierarchies.

Lists the data model summaries within their hierarchical structure.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    CustomDataModelsApi
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
    api_instance = api_client_factory.build(CustomDataModelsApi)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Data Model. Defaults to return              the latest version of the Data Model if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the results. Only EntityType is supported (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_data_model_hierarchies(as_at=as_at, filter=filter, opts=opts)

        # [EXPERIMENTAL] ListDataModelHierarchies: List Custom Data Model hierarchies.
        api_response = api_instance.list_data_model_hierarchies(as_at=as_at, filter=filter)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling CustomDataModelsApi->list_data_model_hierarchies: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Data Model. Defaults to return              the latest version of the Data Model if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results. Only EntityType is supported | [optional] 

### Return type

[**ResourceListOfDataModelSummary**](ResourceListOfDataModelSummary.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All data model hierarchies. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_supported_entity_types**
> ResourceListOfString list_supported_entity_types()

[EXPERIMENTAL] ListSupportedEntityTypes: List the currently supported entity types for use in Custom Data Models.

Lists the currently supported entity types available to bind with Custom Data Models.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    CustomDataModelsApi
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
    api_instance = api_client_factory.build(CustomDataModelsApi)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_supported_entity_types(opts=opts)

        # [EXPERIMENTAL] ListSupportedEntityTypes: List the currently supported entity types for use in Custom Data Models.
        api_response = api_instance.list_supported_entity_types()
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling CustomDataModelsApi->list_supported_entity_types: %s\n" % e)

main()
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResourceListOfString**](ResourceListOfString.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All supported entity types. |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **update_custom_data_model**
> CustomDataModel update_custom_data_model(entity_type, scope, code, update_custom_data_model_request=update_custom_data_model_request)

[EXPERIMENTAL] UpdateCustomDataModel: Update a Custom Data Model

Updates a Custom Data Model.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    CustomDataModelsApi
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
    api_instance = api_client_factory.build(CustomDataModelsApi)
    entity_type = 'entity_type_example' # str | The entity type of the Data Model.
    scope = 'scope_example' # str | The scope of the specified Data Model.
    code = 'code_example' # str | The code of the specified Data Model.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # update_custom_data_model_request = UpdateCustomDataModelRequest.from_json("")
    # update_custom_data_model_request = UpdateCustomDataModelRequest.from_dict({})
    update_custom_data_model_request = UpdateCustomDataModelRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.update_custom_data_model(entity_type, scope, code, update_custom_data_model_request=update_custom_data_model_request, opts=opts)

        # [EXPERIMENTAL] UpdateCustomDataModel: Update a Custom Data Model
        api_response = api_instance.update_custom_data_model(entity_type, scope, code, update_custom_data_model_request=update_custom_data_model_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling CustomDataModelsApi->update_custom_data_model: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| The entity type of the Data Model. | 
 **scope** | **str**| The scope of the specified Data Model. | 
 **code** | **str**| The code of the specified Data Model. | 
 **update_custom_data_model_request** | [**UpdateCustomDataModelRequest**](UpdateCustomDataModelRequest.md)| The request containing the details of the Data Model. | [optional] 

### Return type

[**CustomDataModel**](CustomDataModel.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated Data Model |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

