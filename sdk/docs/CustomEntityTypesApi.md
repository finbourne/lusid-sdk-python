# lusid.CustomEntityTypesApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_custom_entity_type**](CustomEntityTypesApi.md#create_custom_entity_type) | **POST** /api/customentitytypes | [EARLY ACCESS] CreateCustomEntityType: Define a new Custom Entity Type.
[**get_custom_entity_type**](CustomEntityTypesApi.md#get_custom_entity_type) | **GET** /api/customentitytypes/{entityType} | [EARLY ACCESS] GetCustomEntityType: Get a Custom Entity Type.
[**list_custom_entity_types**](CustomEntityTypesApi.md#list_custom_entity_types) | **GET** /api/customentitytypes | [EARLY ACCESS] ListCustomEntityTypes: List Custom Entity Types.
[**update_custom_entity_type**](CustomEntityTypesApi.md#update_custom_entity_type) | **PUT** /api/customentitytypes/{entityType} | [EARLY ACCESS] UpdateCustomEntityType: Modify an existing Custom Entity Type.


# **create_custom_entity_type**
> CustomEntityType create_custom_entity_type(create_custom_entity_type_request)

[EARLY ACCESS] CreateCustomEntityType: Define a new Custom Entity Type.

The API will return a Bad Request if the Custom Entity Type already exists.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from lusid.models.create_custom_entity_type_request import CreateCustomEntityTypeRequest
from lusid.models.custom_entity_type import CustomEntityType
from pprint import pprint

from lusid import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
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
    api_instance = api_client_factory.build(lusid.CustomEntityTypesApi)
    create_custom_entity_type_request = {"entityTypeName":"Support Ticket","displayName":"Support Ticket","description":"SupportTicket","fieldSchema":[{"name":"clientId","lifetime":"Perpetual","type":"String","required":true},{"name":"issueDescription","lifetime":"TimeVariant","type":"String","required":true},{"name":"internalNotes","lifetime":"TimeVariant","type":"String","required":false},{"name":"isResolved","lifetime":"TimeVariant","type":"Boolean","required":false}]} # CreateCustomEntityTypeRequest | The payload containing the description of the Custom Entity Type.

    try:
        # [EARLY ACCESS] CreateCustomEntityType: Define a new Custom Entity Type.
        api_response = await api_instance.create_custom_entity_type(create_custom_entity_type_request)
        print("The response of CustomEntityTypesApi->create_custom_entity_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomEntityTypesApi->create_custom_entity_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_custom_entity_type_request** | [**CreateCustomEntityTypeRequest**](CreateCustomEntityTypeRequest.md)| The payload containing the description of the Custom Entity Type. | 

### Return type

[**CustomEntityType**](CustomEntityType.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The created Custom Entity Type. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_entity_type**
> CustomEntityType get_custom_entity_type(entity_type, as_at=as_at)

[EARLY ACCESS] GetCustomEntityType: Get a Custom Entity Type.

Retrieve a specific Custom Entity Type at a point in AsAt time.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from lusid.models.custom_entity_type import CustomEntityType
from pprint import pprint

from lusid import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
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
    api_instance = api_client_factory.build(lusid.CustomEntityTypesApi)
    entity_type = 'entity_type_example' # str | The identifier for the Custom Entity Type, derived from the \"entityTypeName\" provided on creation.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The AsAt datetime at which to retrieve the definition. (optional)

    try:
        # [EARLY ACCESS] GetCustomEntityType: Get a Custom Entity Type.
        api_response = await api_instance.get_custom_entity_type(entity_type, as_at=as_at)
        print("The response of CustomEntityTypesApi->get_custom_entity_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomEntityTypesApi->get_custom_entity_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| The identifier for the Custom Entity Type, derived from the \&quot;entityTypeName\&quot; provided on creation. | 
 **as_at** | **datetime**| The AsAt datetime at which to retrieve the definition. | [optional] 

### Return type

[**CustomEntityType**](CustomEntityType.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Custom Entity Type. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_custom_entity_types**
> PagedResourceListOfCustomEntityType list_custom_entity_types(as_at=as_at, limit=limit, filter=filter, sort_by=sort_by, page=page)

[EARLY ACCESS] ListCustomEntityTypes: List Custom Entity Types.

List all Custom Entity Types matching particular criteria.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from lusid.models.paged_resource_list_of_custom_entity_type import PagedResourceListOfCustomEntityType
from pprint import pprint

from lusid import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
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
    api_instance = api_client_factory.build(lusid.CustomEntityTypesApi)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the entities. Defaults to returning the latest version              of each Custom Entity Type if not specified. (optional)
    limit = 56 # int | When paginating, limit the results to this number. Defaults to 100 if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the results. For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. (optional)
    sort_by = ['sort_by_example'] # List[str] | A list of field names to sort by, each suffixed by \" ASC\" or \" DESC\" (optional)
    page = 'page_example' # str | The pagination token to use to continue listing entities; this              value is returned from the previous call. If a pagination token is provided, the filter, limit, sortBy,              and asAt fields must not have changed since the original request. (optional)

    try:
        # [EARLY ACCESS] ListCustomEntityTypes: List Custom Entity Types.
        api_response = await api_instance.list_custom_entity_types(as_at=as_at, limit=limit, filter=filter, sort_by=sort_by, page=page)
        print("The response of CustomEntityTypesApi->list_custom_entity_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomEntityTypesApi->list_custom_entity_types: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list the entities. Defaults to returning the latest version              of each Custom Entity Type if not specified. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results. For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot; | [optional] 
 **page** | **str**| The pagination token to use to continue listing entities; this              value is returned from the previous call. If a pagination token is provided, the filter, limit, sortBy,              and asAt fields must not have changed since the original request. | [optional] 

### Return type

[**PagedResourceListOfCustomEntityType**](PagedResourceListOfCustomEntityType.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List Custom Entity Types. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_custom_entity_type**
> CustomEntityType update_custom_entity_type(entity_type, update_custom_entity_type_request)

[EARLY ACCESS] UpdateCustomEntityType: Modify an existing Custom Entity Type.

The API will return a Bad Request if the Custom Entity Type does not exist.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from lusid.models.custom_entity_type import CustomEntityType
from lusid.models.update_custom_entity_type_request import UpdateCustomEntityTypeRequest
from pprint import pprint

from lusid import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
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
    api_instance = api_client_factory.build(lusid.CustomEntityTypesApi)
    entity_type = 'entity_type_example' # str | The identifier for the Custom Entity Type, derived from the \"entityTypeName\" provided on creation.
    update_custom_entity_type_request = {"displayName":"Support Ticket","description":"Support Ticket","fieldSchema":[{"name":"clientId","lifetime":"Perpetual","type":"String","required":true},{"name":"issueDescription","lifetime":"TimeVariant","type":"String","required":true},{"name":"internalNotes","lifetime":"TimeVariant","type":"String","required":false},{"name":"isResolved","lifetime":"TimeVariant","type":"Boolean","required":false}]} # UpdateCustomEntityTypeRequest | The payload containing the description of the Custom Entity Type.

    try:
        # [EARLY ACCESS] UpdateCustomEntityType: Modify an existing Custom Entity Type.
        api_response = await api_instance.update_custom_entity_type(entity_type, update_custom_entity_type_request)
        print("The response of CustomEntityTypesApi->update_custom_entity_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomEntityTypesApi->update_custom_entity_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| The identifier for the Custom Entity Type, derived from the \&quot;entityTypeName\&quot; provided on creation. | 
 **update_custom_entity_type_request** | [**UpdateCustomEntityTypeRequest**](UpdateCustomEntityTypeRequest.md)| The payload containing the description of the Custom Entity Type. | 

### Return type

[**CustomEntityType**](CustomEntityType.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated Custom Entity Type. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

