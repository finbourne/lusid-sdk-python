# lusid.CustomEntitiesApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_custom_entity**](CustomEntitiesApi.md#delete_custom_entity) | **DELETE** /api/customentities/{entityType}/{identifierType}/{identifierValue} | [EARLY ACCESS] DeleteCustomEntity: Delete a Custom Entity instance.
[**delete_custom_entity_access_metadata**](CustomEntitiesApi.md#delete_custom_entity_access_metadata) | **DELETE** /api/customentities/{entityType}/{identifierType}/{identifierValue}/metadata/{metadataKey} | [EARLY ACCESS] DeleteCustomEntityAccessMetadata: Delete a Custom Entity Access Metadata entry
[**get_all_custom_entity_access_metadata**](CustomEntitiesApi.md#get_all_custom_entity_access_metadata) | **GET** /api/customentities/{entityType}/{identifierType}/{identifierValue}/metadata | [EARLY ACCESS] GetAllCustomEntityAccessMetadata: Get all the Access Metadata rules for a Custom Entity
[**get_custom_entity**](CustomEntitiesApi.md#get_custom_entity) | **GET** /api/customentities/{entityType}/{identifierType}/{identifierValue} | [EARLY ACCESS] GetCustomEntity: Get a Custom Entity instance.
[**get_custom_entity_access_metadata_by_key**](CustomEntitiesApi.md#get_custom_entity_access_metadata_by_key) | **GET** /api/customentities/{entityType}/{identifierType}/{identifierValue}/metadata/{metadataKey} | [EARLY ACCESS] GetCustomEntityAccessMetadataByKey: Get an entry identified by a metadataKey in the Access Metadata of a Custom Entity
[**get_custom_entity_relationships**](CustomEntitiesApi.md#get_custom_entity_relationships) | **GET** /api/customentities/{entityType}/{identifierType}/{identifierValue}/relationships | [EARLY ACCESS] GetCustomEntityRelationships: Get Relationships for Custom Entity
[**list_custom_entities**](CustomEntitiesApi.md#list_custom_entities) | **GET** /api/customentities/{entityType} | [EARLY ACCESS] ListCustomEntities: List Custom Entities of the specified entityType.
[**patch_custom_entity_access_metadata**](CustomEntitiesApi.md#patch_custom_entity_access_metadata) | **PATCH** /api/customentities/{entityType}/{identifierType}/{identifierValue}/metadata | [EARLY ACCESS] PatchCustomEntityAccessMetadata: Patch Access Metadata rules for a Custom Entity.
[**upsert_custom_entities**](CustomEntitiesApi.md#upsert_custom_entities) | **POST** /api/customentities/{entityType}/$batchUpsert | [EARLY ACCESS] UpsertCustomEntities: Batch upsert instances of Custom Entities
[**upsert_custom_entity**](CustomEntitiesApi.md#upsert_custom_entity) | **POST** /api/customentities/{entityType} | [EARLY ACCESS] UpsertCustomEntity: Upsert a Custom Entity instance
[**upsert_custom_entity_access_metadata**](CustomEntitiesApi.md#upsert_custom_entity_access_metadata) | **PUT** /api/customentities/{entityType}/{identifierType}/{identifierValue}/metadata/{metadataKey} | [EARLY ACCESS] UpsertCustomEntityAccessMetadata: Upsert a Custom Entity Access Metadata entry associated with a specific metadataKey. This creates or updates the data in LUSID.


# **delete_custom_entity**
> DeletedEntityResponse delete_custom_entity(entity_type, identifier_type, identifier_value, identifier_scope)

[EARLY ACCESS] DeleteCustomEntity: Delete a Custom Entity instance.

Delete a Custom Entity instance by a specific entity type.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.deleted_entity_response import DeletedEntityResponse
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    CustomEntitiesApi,
    EnvironmentVariablesConfigurationLoader,
    SecretsFileConfigurationLoader,
    ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.CustomEntitiesApi)
    entity_type = 'entity_type_example' # str | The type of Custom Entity to remove.
    identifier_type = 'identifier_type_example' # str | An identifier type attached to the Custom Entity instance.
    identifier_value = 'identifier_value_example' # str | The identifier value.
    identifier_scope = 'identifier_scope_example' # str | The identifier scope.

    try:
        # [EARLY ACCESS] DeleteCustomEntity: Delete a Custom Entity instance.
        api_response = await api_instance.delete_custom_entity(entity_type, identifier_type, identifier_value, identifier_scope)
        print("The response of CustomEntitiesApi->delete_custom_entity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomEntitiesApi->delete_custom_entity: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| The type of Custom Entity to remove. | 
 **identifier_type** | **str**| An identifier type attached to the Custom Entity instance. | 
 **identifier_value** | **str**| The identifier value. | 
 **identifier_scope** | **str**| The identifier scope. | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete a Custom Entity instance. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_custom_entity_access_metadata**
> DeletedEntityResponse delete_custom_entity_access_metadata(entity_type, identifier_type, identifier_value, metadata_key, identifier_scope, effective_at=effective_at, effective_until=effective_until)

[EARLY ACCESS] DeleteCustomEntityAccessMetadata: Delete a Custom Entity Access Metadata entry

Deletes the Custom Entity Access Metadata entry that exactly matches the provided identifier parts.    It is important to always check to verify success (or failure).

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.deleted_entity_response import DeletedEntityResponse
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    CustomEntitiesApi,
    EnvironmentVariablesConfigurationLoader,
    SecretsFileConfigurationLoader,
    ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.CustomEntitiesApi)
    entity_type = 'entity_type_example' # str | The type of the Custom Entity.
    identifier_type = 'identifier_type_example' # str | An identifier type attached to the Custom Entity instance.
    identifier_value = 'identifier_value_example' # str | The identifier value.
    metadata_key = 'metadata_key_example' # str | Key of the metadata entry to delete.
    identifier_scope = 'identifier_scope_example' # str | The identifier scope.
    effective_at = 'effective_at_example' # str | The effectiveAt datetime at which to retrieve the Access Metadata. (optional)
    effective_until = '2013-10-20T19:20:30+01:00' # datetime | The effective datetime until which the Access Metadata is valid. If not supplied this will be valid indefinitely, or until the next 'effectiveAt' datetime of the Access Metadata. (optional)

    try:
        # [EARLY ACCESS] DeleteCustomEntityAccessMetadata: Delete a Custom Entity Access Metadata entry
        api_response = await api_instance.delete_custom_entity_access_metadata(entity_type, identifier_type, identifier_value, metadata_key, identifier_scope, effective_at=effective_at, effective_until=effective_until)
        print("The response of CustomEntitiesApi->delete_custom_entity_access_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomEntitiesApi->delete_custom_entity_access_metadata: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| The type of the Custom Entity. | 
 **identifier_type** | **str**| An identifier type attached to the Custom Entity instance. | 
 **identifier_value** | **str**| The identifier value. | 
 **metadata_key** | **str**| Key of the metadata entry to delete. | 
 **identifier_scope** | **str**| The identifier scope. | 
 **effective_at** | **str**| The effectiveAt datetime at which to retrieve the Access Metadata. | [optional] 
 **effective_until** | **datetime**| The effective datetime until which the Access Metadata is valid. If not supplied this will be valid indefinitely, or until the next &#39;effectiveAt&#39; datetime of the Access Metadata. | [optional] 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The access metadata for the CustomEntity or any failure. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_custom_entity_access_metadata**
> Dict[str, List[AccessMetadataValue]] get_all_custom_entity_access_metadata(entity_type, identifier_type, identifier_value, identifier_scope, effective_at=effective_at, as_at=as_at)

[EARLY ACCESS] GetAllCustomEntityAccessMetadata: Get all the Access Metadata rules for a Custom Entity

Get all the Custom Entity access metadata for the specified identifier scope, code and value

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.access_metadata_value import AccessMetadataValue
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    CustomEntitiesApi,
    EnvironmentVariablesConfigurationLoader,
    SecretsFileConfigurationLoader,
    ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.CustomEntitiesApi)
    entity_type = 'entity_type_example' # str | The type of the Custom Entity.
    identifier_type = 'identifier_type_example' # str | An identifier type attached to the Custom Entity instance.
    identifier_value = 'identifier_value_example' # str | The identifier value.
    identifier_scope = 'identifier_scope_example' # str | The identifier scope.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to get the entities. Defaults to the current LUSID system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Access Metadata. Defaults to returning the latest version of the metadata if not specified. (optional)

    try:
        # [EARLY ACCESS] GetAllCustomEntityAccessMetadata: Get all the Access Metadata rules for a Custom Entity
        api_response = await api_instance.get_all_custom_entity_access_metadata(entity_type, identifier_type, identifier_value, identifier_scope, effective_at=effective_at, as_at=as_at)
        print("The response of CustomEntitiesApi->get_all_custom_entity_access_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomEntitiesApi->get_all_custom_entity_access_metadata: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| The type of the Custom Entity. | 
 **identifier_type** | **str**| An identifier type attached to the Custom Entity instance. | 
 **identifier_value** | **str**| The identifier value. | 
 **identifier_scope** | **str**| The identifier scope. | 
 **effective_at** | **str**| The effective datetime or cut label at which to get the entities. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Access Metadata. Defaults to returning the latest version of the metadata if not specified. | [optional] 

### Return type

**Dict[str, List[AccessMetadataValue]]**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The access metadata for the CustomEntity or any failure. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_entity**
> CustomEntityResponse get_custom_entity(entity_type, identifier_type, identifier_value, identifier_scope, as_at=as_at, effective_at=effective_at, related_entity_property_keys=related_entity_property_keys, relationship_definition_ids=relationship_definition_ids)

[EARLY ACCESS] GetCustomEntity: Get a Custom Entity instance.

Retrieve a Custom Entity instance by a specific entity type at a point in AsAt time.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.custom_entity_response import CustomEntityResponse
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    CustomEntitiesApi,
    EnvironmentVariablesConfigurationLoader,
    SecretsFileConfigurationLoader,
    ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.CustomEntitiesApi)
    entity_type = 'entity_type_example' # str | The type of Custom Entity to retrieve. An entityType can be created using the \"CreateCustomEntityDefinition\" endpoint for CustomEntityDefinitions.
    identifier_type = 'identifier_type_example' # str | An identifier type attached to the Custom Entity instance.
    identifier_value = 'identifier_value_example' # str | The identifier value.
    identifier_scope = 'identifier_scope_example' # str | The identifier scope.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The AsAt datetime at which to retrieve the Custom Entity instance. (optional)
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to get the Custom Entity instance. Defaults to the current LUSID system datetime if not specified. (optional)
    related_entity_property_keys = ['related_entity_property_keys_example'] # List[str] | A list of property keys from any domain that supports relationships              to decorate onto related entities. These must take the format {domain}/{scope}/{code}, for example 'Portfolio/Manager/Id'. (optional)
    relationship_definition_ids = ['relationship_definition_ids_example'] # List[str] | A list of relationship definitions that are used to decorate related entities              onto the entity in the response. These must take the form {relationshipDefinitionScope}/{relationshipDefinitionCode}. (optional)

    try:
        # [EARLY ACCESS] GetCustomEntity: Get a Custom Entity instance.
        api_response = await api_instance.get_custom_entity(entity_type, identifier_type, identifier_value, identifier_scope, as_at=as_at, effective_at=effective_at, related_entity_property_keys=related_entity_property_keys, relationship_definition_ids=relationship_definition_ids)
        print("The response of CustomEntitiesApi->get_custom_entity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomEntitiesApi->get_custom_entity: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| The type of Custom Entity to retrieve. An entityType can be created using the \&quot;CreateCustomEntityDefinition\&quot; endpoint for CustomEntityDefinitions. | 
 **identifier_type** | **str**| An identifier type attached to the Custom Entity instance. | 
 **identifier_value** | **str**| The identifier value. | 
 **identifier_scope** | **str**| The identifier scope. | 
 **as_at** | **datetime**| The AsAt datetime at which to retrieve the Custom Entity instance. | [optional] 
 **effective_at** | **str**| The effective datetime or cut label at which to get the Custom Entity instance. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **related_entity_property_keys** | [**List[str]**](str.md)| A list of property keys from any domain that supports relationships              to decorate onto related entities. These must take the format {domain}/{scope}/{code}, for example &#39;Portfolio/Manager/Id&#39;. | [optional] 
 **relationship_definition_ids** | [**List[str]**](str.md)| A list of relationship definitions that are used to decorate related entities              onto the entity in the response. These must take the form {relationshipDefinitionScope}/{relationshipDefinitionCode}. | [optional] 

### Return type

[**CustomEntityResponse**](CustomEntityResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get a custom entity instance. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_entity_access_metadata_by_key**
> List[AccessMetadataValue] get_custom_entity_access_metadata_by_key(entity_type, identifier_type, identifier_value, metadata_key, identifier_scope, effective_at=effective_at, as_at=as_at)

[EARLY ACCESS] GetCustomEntityAccessMetadataByKey: Get an entry identified by a metadataKey in the Access Metadata of a Custom Entity

Get Custom Entity access metadata for the specified metadata key

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.access_metadata_value import AccessMetadataValue
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    CustomEntitiesApi,
    EnvironmentVariablesConfigurationLoader,
    SecretsFileConfigurationLoader,
    ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.CustomEntitiesApi)
    entity_type = 'entity_type_example' # str | The type of the Custom Entity.
    identifier_type = 'identifier_type_example' # str | An identifier type attached to the Custom Entity instance.
    identifier_value = 'identifier_value_example' # str | The identifier value.
    metadata_key = 'metadata_key_example' # str | Key of the metadata entry to retrieve
    identifier_scope = 'identifier_scope_example' # str | The identifier scope.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to get the entities. Defaults to the current LUSID system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Access Metadata. Defaults to returning the latest version of the metadata if not specified. (optional)

    try:
        # [EARLY ACCESS] GetCustomEntityAccessMetadataByKey: Get an entry identified by a metadataKey in the Access Metadata of a Custom Entity
        api_response = await api_instance.get_custom_entity_access_metadata_by_key(entity_type, identifier_type, identifier_value, metadata_key, identifier_scope, effective_at=effective_at, as_at=as_at)
        print("The response of CustomEntitiesApi->get_custom_entity_access_metadata_by_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomEntitiesApi->get_custom_entity_access_metadata_by_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| The type of the Custom Entity. | 
 **identifier_type** | **str**| An identifier type attached to the Custom Entity instance. | 
 **identifier_value** | **str**| The identifier value. | 
 **metadata_key** | **str**| Key of the metadata entry to retrieve | 
 **identifier_scope** | **str**| The identifier scope. | 
 **effective_at** | **str**| The effective datetime or cut label at which to get the entities. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Access Metadata. Defaults to returning the latest version of the metadata if not specified. | [optional] 

### Return type

[**List[AccessMetadataValue]**](AccessMetadataValue.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The access metadata for the CustomEntity or any failure. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_entity_relationships**
> ResourceListOfRelationship get_custom_entity_relationships(entity_type, identifier_scope, identifier_type, identifier_value, effective_at=effective_at, as_at=as_at, filter=filter, identifier_types=identifier_types)

[EARLY ACCESS] GetCustomEntityRelationships: Get Relationships for Custom Entity

Get relationships for the specified Custom Entity.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.resource_list_of_relationship import ResourceListOfRelationship
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    CustomEntitiesApi,
    EnvironmentVariablesConfigurationLoader,
    SecretsFileConfigurationLoader,
    ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.CustomEntitiesApi)
    entity_type = 'entity_type_example' # str | The type of entity get relationships for.
    identifier_scope = 'identifier_scope_example' # str | The identifier scope.
    identifier_type = 'identifier_type_example' # str | An identifier type attached to the Custom Entity.
    identifier_value = 'identifier_value_example' # str | The identifier value.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to get relationships. Defaults to the current LUSID system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve relationships. Defaults to return the latest LUSID AsAt time if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter relationships. Users should provide null or empty string for this field until further notice. (optional)
    identifier_types = ['identifier_types_example'] # List[str] | Identifiers types (as property keys) used for referencing Persons or Legal Entities. These take the format              {domain}/{scope}/{code} e.g. \"Person/CompanyDetails/Role\". They must be from the \"Person\" or \"LegalEntity\" domain.              Only identifier types stated will be used to look up relevant entities in relationships. If not applicable, provide an empty array. (optional)

    try:
        # [EARLY ACCESS] GetCustomEntityRelationships: Get Relationships for Custom Entity
        api_response = await api_instance.get_custom_entity_relationships(entity_type, identifier_scope, identifier_type, identifier_value, effective_at=effective_at, as_at=as_at, filter=filter, identifier_types=identifier_types)
        print("The response of CustomEntitiesApi->get_custom_entity_relationships:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomEntitiesApi->get_custom_entity_relationships: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| The type of entity get relationships for. | 
 **identifier_scope** | **str**| The identifier scope. | 
 **identifier_type** | **str**| An identifier type attached to the Custom Entity. | 
 **identifier_value** | **str**| The identifier value. | 
 **effective_at** | **str**| The effective datetime or cut label at which to get relationships. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve relationships. Defaults to return the latest LUSID AsAt time if not specified. | [optional] 
 **filter** | **str**| Expression to filter relationships. Users should provide null or empty string for this field until further notice. | [optional] 
 **identifier_types** | [**List[str]**](str.md)| Identifiers types (as property keys) used for referencing Persons or Legal Entities. These take the format              {domain}/{scope}/{code} e.g. \&quot;Person/CompanyDetails/Role\&quot;. They must be from the \&quot;Person\&quot; or \&quot;LegalEntity\&quot; domain.              Only identifier types stated will be used to look up relevant entities in relationships. If not applicable, provide an empty array. | [optional] 

### Return type

[**ResourceListOfRelationship**](ResourceListOfRelationship.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The relationships for the specified custom entity. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_custom_entities**
> PagedResourceListOfCustomEntityResponse list_custom_entities(entity_type, effective_at=effective_at, as_at=as_at, limit=limit, filter=filter, sort_by=sort_by, page=page, related_entity_property_keys=related_entity_property_keys, relationship_definition_ids=relationship_definition_ids)

[EARLY ACCESS] ListCustomEntities: List Custom Entities of the specified entityType.

List all the Custom Entities matching particular criteria.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.paged_resource_list_of_custom_entity_response import PagedResourceListOfCustomEntityResponse
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    CustomEntitiesApi,
    EnvironmentVariablesConfigurationLoader,
    SecretsFileConfigurationLoader,
    ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.CustomEntitiesApi)
    entity_type = 'entity_type_example' # str | The type of Custom Entity to list.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to list the entities. Defaults to the current LUSID              system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the entities. Defaults to returning the latest version              of each portfolio if not specified. (optional)
    limit = 56 # int | When paginating, limit the results to this number. Defaults to 100 if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the results. For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. (optional)
    sort_by = ['sort_by_example'] # List[str] | A list of field names or properties to sort by, each suffixed by \" ASC\" or \" DESC\". (optional)
    page = 'page_example' # str | The pagination token to use to continue listing entities; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. (optional)
    related_entity_property_keys = ['related_entity_property_keys_example'] # List[str] | A list of property keys from any domain that supports relationships              to decorate onto related entities. These must take the format {domain}/{scope}/{code}, for example 'Portfolio/Manager/Id'. (optional)
    relationship_definition_ids = ['relationship_definition_ids_example'] # List[str] | A list of relationship definitions that are used to decorate related entities              onto the entities in the response. These must take the form {relationshipDefinitionScope}/{relationshipDefinitionCode}. (optional)

    try:
        # [EARLY ACCESS] ListCustomEntities: List Custom Entities of the specified entityType.
        api_response = await api_instance.list_custom_entities(entity_type, effective_at=effective_at, as_at=as_at, limit=limit, filter=filter, sort_by=sort_by, page=page, related_entity_property_keys=related_entity_property_keys, relationship_definition_ids=relationship_definition_ids)
        print("The response of CustomEntitiesApi->list_custom_entities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomEntitiesApi->list_custom_entities: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| The type of Custom Entity to list. | 
 **effective_at** | **str**| The effective datetime or cut label at which to list the entities. Defaults to the current LUSID              system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the entities. Defaults to returning the latest version              of each portfolio if not specified. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results. For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 
 **page** | **str**| The pagination token to use to continue listing entities; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. | [optional] 
 **related_entity_property_keys** | [**List[str]**](str.md)| A list of property keys from any domain that supports relationships              to decorate onto related entities. These must take the format {domain}/{scope}/{code}, for example &#39;Portfolio/Manager/Id&#39;. | [optional] 
 **relationship_definition_ids** | [**List[str]**](str.md)| A list of relationship definitions that are used to decorate related entities              onto the entities in the response. These must take the form {relationshipDefinitionScope}/{relationshipDefinitionCode}. | [optional] 

### Return type

[**PagedResourceListOfCustomEntityResponse**](PagedResourceListOfCustomEntityResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List custom entities of the specified entityType. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_custom_entity_access_metadata**
> Dict[str, List[AccessMetadataValue]] patch_custom_entity_access_metadata(entity_type, identifier_type, identifier_value, identifier_scope, access_metadata_operation, effective_at=effective_at, effective_until=effective_until)

[EARLY ACCESS] PatchCustomEntityAccessMetadata: Patch Access Metadata rules for a Custom Entity.

Patch Custom Entity Access Metadata Rules in a single scope.  The behaviour is defined by the JSON Patch specification.                Currently only 'add' is a supported operation on the patch document    Currently only valid metadata keys are supported paths on the patch document                The response will return any affected Custom Entity Access Metadata rules or a failure message if unsuccessful.                It is important to always check to verify success (or failure).                Multiple rules for a metadataKey can exist with different effective at dates, when resources are accessed the rule that is active for the current time will be fetched.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.access_metadata_operation import AccessMetadataOperation
from lusid.models.access_metadata_value import AccessMetadataValue
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    CustomEntitiesApi,
    EnvironmentVariablesConfigurationLoader,
    SecretsFileConfigurationLoader,
    ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.CustomEntitiesApi)
    entity_type = 'entity_type_example' # str | The type of the Custom Entity.
    identifier_type = 'identifier_type_example' # str | An identifier type attached to the Custom Entity instance.
    identifier_value = 'identifier_value_example' # str | The identifier value.
    identifier_scope = 'identifier_scope_example' # str | The identifier scope.
    access_metadata_operation = [lusid.AccessMetadataOperation()] # List[AccessMetadataOperation] | The Json Patch document
    effective_at = 'effective_at_example' # str | The effectiveAt datetime at which the Access Metadata will be effective from (optional)
    effective_until = '2013-10-20T19:20:30+01:00' # datetime | The effective datetime until which the Access Metadata is valid. If not supplied this will be valid indefinitely, or until the next 'effectiveAt' datetime of the Access Metadata (optional)

    try:
        # [EARLY ACCESS] PatchCustomEntityAccessMetadata: Patch Access Metadata rules for a Custom Entity.
        api_response = await api_instance.patch_custom_entity_access_metadata(entity_type, identifier_type, identifier_value, identifier_scope, access_metadata_operation, effective_at=effective_at, effective_until=effective_until)
        print("The response of CustomEntitiesApi->patch_custom_entity_access_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomEntitiesApi->patch_custom_entity_access_metadata: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| The type of the Custom Entity. | 
 **identifier_type** | **str**| An identifier type attached to the Custom Entity instance. | 
 **identifier_value** | **str**| The identifier value. | 
 **identifier_scope** | **str**| The identifier scope. | 
 **access_metadata_operation** | [**List[AccessMetadataOperation]**](AccessMetadataOperation.md)| The Json Patch document | 
 **effective_at** | **str**| The effectiveAt datetime at which the Access Metadata will be effective from | [optional] 
 **effective_until** | **datetime**| The effective datetime until which the Access Metadata is valid. If not supplied this will be valid indefinitely, or until the next &#39;effectiveAt&#39; datetime of the Access Metadata | [optional] 

### Return type

**Dict[str, List[AccessMetadataValue]]**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The access metadata for the CustomEntity or any failure. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_custom_entities**
> UpsertCustomEntitiesResponse upsert_custom_entities(entity_type, success_mode, request_body)

[EARLY ACCESS] UpsertCustomEntities: Batch upsert instances of Custom Entities

Note: If using partial failure modes, then it is important to check the response body for failures as any failures will still return a 200 status code

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.custom_entity_request import CustomEntityRequest
from lusid.models.upsert_custom_entities_response import UpsertCustomEntitiesResponse
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    CustomEntitiesApi,
    EnvironmentVariablesConfigurationLoader,
    SecretsFileConfigurationLoader,
    ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.CustomEntitiesApi)
    entity_type = 'entity_type_example' # str | The type of the Custom Entity to be created. An entityType can be created using the \"CreateCustomEntityDefinition\" endpoint for CustomEntityDefinitions.
    success_mode = 'success_mode_example' # str | Whether the batch request should fail Atomically or in a Partial fashion - Allowed Values: Atomic, Partial
    request_body = {"CustomEntity1":{"displayName":"CustomEntity1","description":"MyFirstCustomEntity","identifiers":[{"identifierScope":"scope1","identifierType":"supportTicketId","identifierValue":"xyz123pqr"}],"fields":[{"name":"clientId","value":"AcmeLtd","effectiveFrom":"0001-01-01T00:00:00.0000000+00:00","effectiveUntil":"9999-12-31T23:59:59.9999999+00:00"},{"name":"issueDescription","value":"I can't access this portfolio","effectiveFrom":"2020-01-01T12:00:00.0000000+00:00","effectiveUntil":"9999-12-31T23:59:59.9999999+00:00"}]},"CustomEntity2":{"displayName":"CustomEntity2","description":"MyFirstCustomEntity","identifiers":[{"identifierScope":"scope1","identifierType":"supportTicketId","identifierValue":"yazr1531"}],"fields":[{"name":"clientId","value":"AcmeLtd","effectiveFrom":"0001-01-01T00:00:00.0000000+00:00","effectiveUntil":"9999-12-31T23:59:59.9999999+00:00"},{"name":"issueDescription","value":"Having trouble adding identifiers","effectiveFrom":"2020-01-01T12:00:00.0000000+00:00","effectiveUntil":"9999-12-31T23:59:59.9999999+00:00"}]}} # Dict[str, CustomEntityRequest] | The payload describing the Custom Entity instances

    try:
        # [EARLY ACCESS] UpsertCustomEntities: Batch upsert instances of Custom Entities
        api_response = await api_instance.upsert_custom_entities(entity_type, success_mode, request_body)
        print("The response of CustomEntitiesApi->upsert_custom_entities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomEntitiesApi->upsert_custom_entities: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| The type of the Custom Entity to be created. An entityType can be created using the \&quot;CreateCustomEntityDefinition\&quot; endpoint for CustomEntityDefinitions. | 
 **success_mode** | **str**| Whether the batch request should fail Atomically or in a Partial fashion - Allowed Values: Atomic, Partial | 
 **request_body** | [**Dict[str, CustomEntityRequest]**](CustomEntityRequest.md)| The payload describing the Custom Entity instances | 

### Return type

[**UpsertCustomEntitiesResponse**](UpsertCustomEntitiesResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The upserted custom entity instance |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_custom_entity**
> CustomEntityResponse upsert_custom_entity(entity_type, custom_entity_request)

[EARLY ACCESS] UpsertCustomEntity: Upsert a Custom Entity instance

Insert the Custom Entity if it does not exist or update the Custom Entity with the supplied state if it does exist.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.custom_entity_request import CustomEntityRequest
from lusid.models.custom_entity_response import CustomEntityResponse
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    CustomEntitiesApi,
    EnvironmentVariablesConfigurationLoader,
    SecretsFileConfigurationLoader,
    ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.CustomEntitiesApi)
    entity_type = 'entity_type_example' # str | The type of the Custom Entity to be created. An entityType can be created using the \"CreateCustomEntityDefinition\" endpoint for CustomEntityDefinitions.
    custom_entity_request = {"displayName":"Portfolio Access Denied","description":"User cannot access the portfolio","identifiers":[{"identifierScope":"someScope","identifierType":"supportTicketId","identifierValue":"xyz123pqr"}],"fields":[{"name":"clientId","value":"AcmeLtd"},{"name":"issueDescription","value":"I can't access this portfolio","effectiveFrom":"2023-03-03T09:00:00.0000000+00:00"}]} # CustomEntityRequest | The payload describing the Custom Entity instance.

    try:
        # [EARLY ACCESS] UpsertCustomEntity: Upsert a Custom Entity instance
        api_response = await api_instance.upsert_custom_entity(entity_type, custom_entity_request)
        print("The response of CustomEntitiesApi->upsert_custom_entity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomEntitiesApi->upsert_custom_entity: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| The type of the Custom Entity to be created. An entityType can be created using the \&quot;CreateCustomEntityDefinition\&quot; endpoint for CustomEntityDefinitions. | 
 **custom_entity_request** | [**CustomEntityRequest**](CustomEntityRequest.md)| The payload describing the Custom Entity instance. | 

### Return type

[**CustomEntityResponse**](CustomEntityResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The upserted custom entity instance |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_custom_entity_access_metadata**
> List[AccessMetadataValue] upsert_custom_entity_access_metadata(entity_type, identifier_type, identifier_value, metadata_key, identifier_scope, upsert_custom_entity_access_metadata_request, effective_at=effective_at, effective_until=effective_until)

[EARLY ACCESS] UpsertCustomEntityAccessMetadata: Upsert a Custom Entity Access Metadata entry associated with a specific metadataKey. This creates or updates the data in LUSID.

Update or insert one Custom Entity Access Metadata entry in a single scope. An item will be updated if it already exists  and inserted if it does not.                The response will return the successfully updated or inserted Custom Entity Access Metadata rule or failure message if unsuccessful.                It is important to always check to verify success (or failure).                Multiple rules for a metadataKey can exist with different effective at dates, when resources are accessed the rule that is active for the current time will be fetched.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.access_metadata_value import AccessMetadataValue
from lusid.models.upsert_custom_entity_access_metadata_request import UpsertCustomEntityAccessMetadataRequest
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    CustomEntitiesApi,
    EnvironmentVariablesConfigurationLoader,
    SecretsFileConfigurationLoader,
    ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.CustomEntitiesApi)
    entity_type = 'entity_type_example' # str | The type of the Custom Entity.
    identifier_type = 'identifier_type_example' # str | An identifier type attached to the Custom Entity instance.
    identifier_value = 'identifier_value_example' # str | The identifier value.
    metadata_key = 'metadata_key_example' # str | Key of the metadata entry to retrieve
    identifier_scope = 'identifier_scope_example' # str | The identifier scope.
    upsert_custom_entity_access_metadata_request = {"metadata":[{"value":"SilverLicence","provider":"TestDataProvider"}]} # UpsertCustomEntityAccessMetadataRequest | The Custom Entity Access Metadata entry to upsert
    effective_at = 'effective_at_example' # str | The effectiveAt datetime at which the Access Metadata will be effective from (optional)
    effective_until = '2013-10-20T19:20:30+01:00' # datetime | The effective datetime until which the Access Metadata is valid. If not supplied this will be valid indefinitely, or until the next 'effectiveAt' datetime of the Access Metadata (optional)

    try:
        # [EARLY ACCESS] UpsertCustomEntityAccessMetadata: Upsert a Custom Entity Access Metadata entry associated with a specific metadataKey. This creates or updates the data in LUSID.
        api_response = await api_instance.upsert_custom_entity_access_metadata(entity_type, identifier_type, identifier_value, metadata_key, identifier_scope, upsert_custom_entity_access_metadata_request, effective_at=effective_at, effective_until=effective_until)
        print("The response of CustomEntitiesApi->upsert_custom_entity_access_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomEntitiesApi->upsert_custom_entity_access_metadata: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| The type of the Custom Entity. | 
 **identifier_type** | **str**| An identifier type attached to the Custom Entity instance. | 
 **identifier_value** | **str**| The identifier value. | 
 **metadata_key** | **str**| Key of the metadata entry to retrieve | 
 **identifier_scope** | **str**| The identifier scope. | 
 **upsert_custom_entity_access_metadata_request** | [**UpsertCustomEntityAccessMetadataRequest**](UpsertCustomEntityAccessMetadataRequest.md)| The Custom Entity Access Metadata entry to upsert | 
 **effective_at** | **str**| The effectiveAt datetime at which the Access Metadata will be effective from | [optional] 
 **effective_until** | **datetime**| The effective datetime until which the Access Metadata is valid. If not supplied this will be valid indefinitely, or until the next &#39;effectiveAt&#39; datetime of the Access Metadata | [optional] 

### Return type

[**List[AccessMetadataValue]**](AccessMetadataValue.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The access metadata for the CustomEntity or any failure. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

