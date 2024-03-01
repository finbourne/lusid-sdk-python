# lusid.TransactionConfigurationApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_side_definition**](TransactionConfigurationApi.md#delete_side_definition) | **DELETE** /api/transactionconfiguration/sides/{side}/$delete | DeleteSideDefinition: Delete the given side definition
[**delete_transaction_type**](TransactionConfigurationApi.md#delete_transaction_type) | **DELETE** /api/transactionconfiguration/types/{source}/{type} | DeleteTransactionType: Delete a transaction type
[**delete_transaction_type_source**](TransactionConfigurationApi.md#delete_transaction_type_source) | **DELETE** /api/transactionconfiguration/types/{source}/$delete | DeleteTransactionTypeSource: Delete all transaction types for the given source and scope
[**get_side_definition**](TransactionConfigurationApi.md#get_side_definition) | **GET** /api/transactionconfiguration/sides/{side} | GetSideDefinition: Get the side definition for a given side name( or label)
[**get_transaction_type**](TransactionConfigurationApi.md#get_transaction_type) | **GET** /api/transactionconfiguration/types/{source}/{type} | GetTransactionType: Get a single transaction configuration type
[**list_side_definitions**](TransactionConfigurationApi.md#list_side_definitions) | **GET** /api/transactionconfiguration/sides | ListSideDefinitions: List the side definitions
[**list_transaction_types**](TransactionConfigurationApi.md#list_transaction_types) | **GET** /api/transactionconfiguration/types | ListTransactionTypes: List transaction types
[**set_side_definition**](TransactionConfigurationApi.md#set_side_definition) | **PUT** /api/transactionconfiguration/sides/{side} | SetSideDefinition: Set a side definition
[**set_side_definitions**](TransactionConfigurationApi.md#set_side_definitions) | **PUT** /api/transactionconfiguration/sides | SetSideDefinitions: Set the given side definitions
[**set_transaction_type**](TransactionConfigurationApi.md#set_transaction_type) | **PUT** /api/transactionconfiguration/types/{source}/{type} | SetTransactionType: Set a specific transaction type
[**set_transaction_type_source**](TransactionConfigurationApi.md#set_transaction_type_source) | **PUT** /api/transactionconfiguration/types/{source} | SetTransactionTypeSource: Set the transaction types for the given source and scope


# **delete_side_definition**
> DeletedEntityResponse delete_side_definition(side, scope=scope)

DeleteSideDefinition: Delete the given side definition

Delete the side which user specify in the request.

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
    TransactionConfigurationApi,
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
    api_instance = api_client_factory.build(lusid.TransactionConfigurationApi)
    side = 'side_example' # str | The label to uniquely identify the side.
    scope = 'default' # str | The scope in which the side exists. When not supplied the scope is 'default'. (optional) (default to 'default')

    try:
        # DeleteSideDefinition: Delete the given side definition
        api_response = await api_instance.delete_side_definition(side, scope=scope)
        print("The response of TransactionConfigurationApi->delete_side_definition:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionConfigurationApi->delete_side_definition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **side** | **str**| The label to uniquely identify the side. | 
 **scope** | **str**| The scope in which the side exists. When not supplied the scope is &#39;default&#39;. | [optional] [default to &#39;default&#39;]

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
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_transaction_type**
> DeletedEntityResponse delete_transaction_type(source, type, scope=scope)

DeleteTransactionType: Delete a transaction type

/// WARNING! Changing existing transaction types has a material impact on how data, new and old,  is processed and aggregated by LUSID, and will affect your whole organisation. Only call this API if you are fully aware of the implications of the change.

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
    TransactionConfigurationApi,
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
    api_instance = api_client_factory.build(lusid.TransactionConfigurationApi)
    source = 'source_example' # str | The source that the type is in
    type = 'type_example' # str | One of the type's aliases
    scope = 'default' # str | The scope in which the transaction types exists. When not supplied the scope is 'default'. (optional) (default to 'default')

    try:
        # DeleteTransactionType: Delete a transaction type
        api_response = await api_instance.delete_transaction_type(source, type, scope=scope)
        print("The response of TransactionConfigurationApi->delete_transaction_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionConfigurationApi->delete_transaction_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**| The source that the type is in | 
 **type** | **str**| One of the type&#39;s aliases | 
 **scope** | **str**| The scope in which the transaction types exists. When not supplied the scope is &#39;default&#39;. | [optional] [default to &#39;default&#39;]

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
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_transaction_type_source**
> DeletedEntityResponse delete_transaction_type_source(source, scope=scope)

DeleteTransactionTypeSource: Delete all transaction types for the given source and scope

Delete all the types for the given source and scope.

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
    TransactionConfigurationApi,
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
    api_instance = api_client_factory.build(lusid.TransactionConfigurationApi)
    source = 'source_example' # str | The source to set the transaction types for.
    scope = 'default' # str | The scope in which the transaction types exists. When not supplied the scope is 'default'. (optional) (default to 'default')

    try:
        # DeleteTransactionTypeSource: Delete all transaction types for the given source and scope
        api_response = await api_instance.delete_transaction_type_source(source, scope=scope)
        print("The response of TransactionConfigurationApi->delete_transaction_type_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionConfigurationApi->delete_transaction_type_source: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**| The source to set the transaction types for. | 
 **scope** | **str**| The scope in which the transaction types exists. When not supplied the scope is &#39;default&#39;. | [optional] [default to &#39;default&#39;]

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
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_side_definition**
> SideDefinition get_side_definition(side, scope=scope, as_at=as_at)

GetSideDefinition: Get the side definition for a given side name( or label)

Get the side definition user requested.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.side_definition import SideDefinition
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    TransactionConfigurationApi,
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
    api_instance = api_client_factory.build(lusid.TransactionConfigurationApi)
    side = 'side_example' # str | The label to uniquely identify the side.
    scope = 'default' # str | The scope in which the side exists. When not supplied the scope is 'default'. (optional) (default to 'default')
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the transaction types. Defaults to returning the latest versions if not specified. (optional)

    try:
        # GetSideDefinition: Get the side definition for a given side name( or label)
        api_response = await api_instance.get_side_definition(side, scope=scope, as_at=as_at)
        print("The response of TransactionConfigurationApi->get_side_definition:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionConfigurationApi->get_side_definition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **side** | **str**| The label to uniquely identify the side. | 
 **scope** | **str**| The scope in which the side exists. When not supplied the scope is &#39;default&#39;. | [optional] [default to &#39;default&#39;]
 **as_at** | **datetime**| The asAt datetime at which to retrieve the transaction types. Defaults to returning the latest versions if not specified. | [optional] 

### Return type

[**SideDefinition**](SideDefinition.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction_type**
> TransactionType get_transaction_type(source, type, as_at=as_at, scope=scope)

GetTransactionType: Get a single transaction configuration type

Get a single transaction type. Returns failure if not found

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.transaction_type import TransactionType
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    TransactionConfigurationApi,
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
    api_instance = api_client_factory.build(lusid.TransactionConfigurationApi)
    source = 'source_example' # str | The source that the type is in
    type = 'type_example' # str | One of the type's aliases
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the transaction configuration.              Defaults to returning the latest version of the transaction configuration type if not specified (optional)
    scope = 'default' # str | The scope in which the transaction types exists. When not supplied the scope is 'default'. (optional) (default to 'default')

    try:
        # GetTransactionType: Get a single transaction configuration type
        api_response = await api_instance.get_transaction_type(source, type, as_at=as_at, scope=scope)
        print("The response of TransactionConfigurationApi->get_transaction_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionConfigurationApi->get_transaction_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**| The source that the type is in | 
 **type** | **str**| One of the type&#39;s aliases | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the transaction configuration.              Defaults to returning the latest version of the transaction configuration type if not specified | [optional] 
 **scope** | **str**| The scope in which the transaction types exists. When not supplied the scope is &#39;default&#39;. | [optional] [default to &#39;default&#39;]

### Return type

[**TransactionType**](TransactionType.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_side_definitions**
> ResourceListOfSideDefinition list_side_definitions(as_at=as_at, scope=scope)

ListSideDefinitions: List the side definitions

List all the side definitions in the given scope

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.resource_list_of_side_definition import ResourceListOfSideDefinition
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    TransactionConfigurationApi,
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
    api_instance = api_client_factory.build(lusid.TransactionConfigurationApi)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the transaction types. Defaults to returning the latest versions if not specified. (optional)
    scope = 'default' # str | The scope in which the side exists. When not supplied the scope is 'default'. (optional) (default to 'default')

    try:
        # ListSideDefinitions: List the side definitions
        api_response = await api_instance.list_side_definitions(as_at=as_at, scope=scope)
        print("The response of TransactionConfigurationApi->list_side_definitions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionConfigurationApi->list_side_definitions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to retrieve the transaction types. Defaults to returning the latest versions if not specified. | [optional] 
 **scope** | **str**| The scope in which the side exists. When not supplied the scope is &#39;default&#39;. | [optional] [default to &#39;default&#39;]

### Return type

[**ResourceListOfSideDefinition**](ResourceListOfSideDefinition.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_transaction_types**
> Dict[str, List[TransactionType]] list_transaction_types(as_at=as_at, scope=scope)

ListTransactionTypes: List transaction types

Get the list of current transaction types. For information on the default transaction types provided with  LUSID, see https://support.lusid.com/knowledgebase/article/KA-01873/.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.transaction_type import TransactionType
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    TransactionConfigurationApi,
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
    api_instance = api_client_factory.build(lusid.TransactionConfigurationApi)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the transaction types. Defaults              to returning the latest versions if not specified. (optional)
    scope = 'default' # str | The scope in which the side exists. When not supplied the scope is 'default'. (optional) (default to 'default')

    try:
        # ListTransactionTypes: List transaction types
        api_response = await api_instance.list_transaction_types(as_at=as_at, scope=scope)
        print("The response of TransactionConfigurationApi->list_transaction_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionConfigurationApi->list_transaction_types: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to retrieve the transaction types. Defaults              to returning the latest versions if not specified. | [optional] 
 **scope** | **str**| The scope in which the side exists. When not supplied the scope is &#39;default&#39;. | [optional] [default to &#39;default&#39;]

### Return type

**Dict[str, List[TransactionType]]**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_side_definition**
> SideDefinition set_side_definition(side, side_definition_request, scope=scope)

SetSideDefinition: Set a side definition

Set a new side definition for use in a transaction type. For more information, see https://support.lusid.com/knowledgebase/article/KA-01875.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.side_definition import SideDefinition
from lusid.models.side_definition_request import SideDefinitionRequest
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    TransactionConfigurationApi,
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
    api_instance = api_client_factory.build(lusid.TransactionConfigurationApi)
    side = 'side_example' # str | The label to uniquely identify the side.
    side_definition_request = {"security":"Txn:LusidInstrumentId","currency":"Txn:TradeCurrency","rate":"Txn:Units","units":"1","amount":"Transaction/MyScope/TradeAmount","notionalAmount":"Transaction/default/NotionalAmount"} # SideDefinitionRequest | The side definition to create or replace.
    scope = 'default' # str | The scope in which the side exists. When not supplied the scope is 'default'. (optional) (default to 'default')

    try:
        # SetSideDefinition: Set a side definition
        api_response = await api_instance.set_side_definition(side, side_definition_request, scope=scope)
        print("The response of TransactionConfigurationApi->set_side_definition:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionConfigurationApi->set_side_definition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **side** | **str**| The label to uniquely identify the side. | 
 **side_definition_request** | [**SideDefinitionRequest**](SideDefinitionRequest.md)| The side definition to create or replace. | 
 **scope** | **str**| The scope in which the side exists. When not supplied the scope is &#39;default&#39;. | [optional] [default to &#39;default&#39;]

### Return type

[**SideDefinition**](SideDefinition.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_side_definitions**
> ResourceListOfSideDefinition set_side_definitions(sides_definition_request, scope=scope)

SetSideDefinitions: Set the given side definitions

Set a new side definition for use in a transaction type. For more information, see https://support.lusid.com/knowledgebase/article/KA-01875.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.resource_list_of_side_definition import ResourceListOfSideDefinition
from lusid.models.sides_definition_request import SidesDefinitionRequest
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    TransactionConfigurationApi,
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
    api_instance = api_client_factory.build(lusid.TransactionConfigurationApi)
    sides_definition_request = [{"side":"Side1","sideRequest":{"security":"Txn:LusidInstrumentId","currency":"Txn:TradeCurrency","rate":"Txn:Units","units":"1","amount":"Transaction/MyScope/TradeAmount","notionalAmount":"Transaction/default/NotionalAmount"}}] # List[SidesDefinitionRequest] | The list of side definitions to create, or replace.
    scope = 'default' # str | The scope in which the side exists. When not supplied the scope is 'default'. (optional) (default to 'default')

    try:
        # SetSideDefinitions: Set the given side definitions
        api_response = await api_instance.set_side_definitions(sides_definition_request, scope=scope)
        print("The response of TransactionConfigurationApi->set_side_definitions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionConfigurationApi->set_side_definitions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sides_definition_request** | [**List[SidesDefinitionRequest]**](SidesDefinitionRequest.md)| The list of side definitions to create, or replace. | 
 **scope** | **str**| The scope in which the side exists. When not supplied the scope is &#39;default&#39;. | [optional] [default to &#39;default&#39;]

### Return type

[**ResourceListOfSideDefinition**](ResourceListOfSideDefinition.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_transaction_type**
> TransactionType set_transaction_type(source, type, transaction_type_request, scope=scope)

SetTransactionType: Set a specific transaction type

Set a transaction type for the given source and type. If the requested transaction type does not exist, it will be created    WARNING! Changing existing transaction types has a material impact on how data, new and old, is processed and aggregated by LUSID, and will affect your whole organisation. Only call this API if you are fully aware of the implications of the change.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.transaction_type import TransactionType
from lusid.models.transaction_type_request import TransactionTypeRequest
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    TransactionConfigurationApi,
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
    api_instance = api_client_factory.build(lusid.TransactionConfigurationApi)
    source = 'source_example' # str | The source to set the transaction configuration for
    type = 'type_example' # str | One of the transaction configuration alias types to uniquely identify the configuration. If this type does not exist, then a new transaction type is created using the body of the request in the given source, without including this type
    transaction_type_request = {"aliases":[{"type":"CustomBuy","description":"A custom buy type","transactionClass":"Buy","transactionRoles":"Longer","isDefault":false},{"type":"BuyAlias","description":"A similar buy type","transactionClass":"Buy","transactionRoles":"Longer","isDefault":false}],"movements":[{"movementTypes":"StockMovement","side":"Side1","direction":-1,"properties":{"TransactionConfiguration/default/TaxLotSelectionMethod":{"key":"TransactionConfiguration/default/TaxLotSelectionMethod","value":{"labelValue":"FirstInFirstOut"}}},"mappings":[],"movementOptions":[]},{"movementTypes":"CashCommitment","side":"Side1","direction":1,"properties":{},"mappings":[{"propertyKey":"Transaction/scopeA/Strategy","setTo":"Cash"}],"movementOptions":[],"settlementDateOverride":"Transaction/MyScope/SettlementDateOverride"}],"properties":{"TransactionConfiguration/default/TotalConsiderationPolicy":{"key":"TransactionConfiguration/default/TotalConsiderationPolicy","value":{"labelValue":"Add"}}},"calculations":[{"type":"TaxAmounts","side":"Side1"}]} # TransactionTypeRequest | The transaction configuration to set
    scope = 'default' # str | The scope in which the transaction types exists. When not supplied the scope is 'default'. (optional) (default to 'default')

    try:
        # SetTransactionType: Set a specific transaction type
        api_response = await api_instance.set_transaction_type(source, type, transaction_type_request, scope=scope)
        print("The response of TransactionConfigurationApi->set_transaction_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionConfigurationApi->set_transaction_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**| The source to set the transaction configuration for | 
 **type** | **str**| One of the transaction configuration alias types to uniquely identify the configuration. If this type does not exist, then a new transaction type is created using the body of the request in the given source, without including this type | 
 **transaction_type_request** | [**TransactionTypeRequest**](TransactionTypeRequest.md)| The transaction configuration to set | 
 **scope** | **str**| The scope in which the transaction types exists. When not supplied the scope is &#39;default&#39;. | [optional] [default to &#39;default&#39;]

### Return type

[**TransactionType**](TransactionType.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_transaction_type_source**
> ResourceListOfTransactionType set_transaction_type_source(source, transaction_type_request, scope=scope)

SetTransactionTypeSource: Set the transaction types for the given source and scope

The complete set of transaction types for the source.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.resource_list_of_transaction_type import ResourceListOfTransactionType
from lusid.models.transaction_type_request import TransactionTypeRequest
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    TransactionConfigurationApi,
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
    api_instance = api_client_factory.build(lusid.TransactionConfigurationApi)
    source = 'source_example' # str | The source to set the transaction types for.
    transaction_type_request = [{"aliases":[{"type":"Simple-Sell","description":"Sale","transactionClass":"MyDefault","transactionRoles":"LongShorter","isDefault":false}],"movements":[{"movementTypes":"Traded","side":"Side1","direction":-1,"properties":{},"mappings":[],"movementOptions":[]},{"movementTypes":"CashSettlement","side":"Side2","direction":1,"properties":{},"mappings":[],"movementOptions":[],"settlementDateOverride":"Transaction/MyScope/SettlementDateOverride"}],"properties":{"TransactionConfiguration/default/Example":{"key":"TransactionConfiguration/default/Example","value":{"labelValue":"Value"}}},"calculations":[{"type":"TaxAmounts","side":"Side1"}]}] # List[TransactionTypeRequest] | The set of transaction types.
    scope = 'default' # str | The scope in which the transaction types exists. When not supplied the scope is 'default'. (optional) (default to 'default')

    try:
        # SetTransactionTypeSource: Set the transaction types for the given source and scope
        api_response = await api_instance.set_transaction_type_source(source, transaction_type_request, scope=scope)
        print("The response of TransactionConfigurationApi->set_transaction_type_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionConfigurationApi->set_transaction_type_source: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**| The source to set the transaction types for. | 
 **transaction_type_request** | [**List[TransactionTypeRequest]**](TransactionTypeRequest.md)| The set of transaction types. | 
 **scope** | **str**| The scope in which the transaction types exists. When not supplied the scope is &#39;default&#39;. | [optional] [default to &#39;default&#39;]

### Return type

[**ResourceListOfTransactionType**](ResourceListOfTransactionType.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

