# lusid.TransactionConfigurationApi

All URIs are relative to *https://fbn-prd.lusid.com/api*

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

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransactionConfigurationApi
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
    api_instance = api_client_factory.build(TransactionConfigurationApi)
    side = 'side_example' # str | The label to uniquely identify the side.
    scope = 'default' # str | The scope in which the side exists. When not supplied the scope is 'default'. (optional) (default to 'default')

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_side_definition(side, scope=scope, opts=opts)

        # DeleteSideDefinition: Delete the given side definition
        api_response = api_instance.delete_side_definition(side, scope=scope)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransactionConfigurationApi->delete_side_definition: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **side** | **str**| The label to uniquely identify the side. | 
 **scope** | **str**| The scope in which the side exists. When not supplied the scope is &#39;default&#39;. | [optional] [default to &#39;default&#39;]

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_transaction_type**
> DeletedEntityResponse delete_transaction_type(source, type, scope=scope)

DeleteTransactionType: Delete a transaction type

/// WARNING! Changing existing transaction types has a material impact on how data, new and old, is processed and aggregated by LUSID, and will affect your whole organisation. Only call this API if you are fully aware of the implications of the change.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransactionConfigurationApi
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
    api_instance = api_client_factory.build(TransactionConfigurationApi)
    source = 'source_example' # str | The source that the type is in
    type = 'type_example' # str | One of the type's aliases
    scope = 'default' # str | The scope in which the transaction types exists. When not supplied the scope is 'default'. (optional) (default to 'default')

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_transaction_type(source, type, scope=scope, opts=opts)

        # DeleteTransactionType: Delete a transaction type
        api_response = api_instance.delete_transaction_type(source, type, scope=scope)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransactionConfigurationApi->delete_transaction_type: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**| The source that the type is in | 
 **type** | **str**| One of the type&#39;s aliases | 
 **scope** | **str**| The scope in which the transaction types exists. When not supplied the scope is &#39;default&#39;. | [optional] [default to &#39;default&#39;]

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_transaction_type_source**
> DeletedEntityResponse delete_transaction_type_source(source, scope=scope)

DeleteTransactionTypeSource: Delete all transaction types for the given source and scope

Delete all the types for the given source and scope.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransactionConfigurationApi
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
    api_instance = api_client_factory.build(TransactionConfigurationApi)
    source = 'source_example' # str | The source to set the transaction types for.
    scope = 'default' # str | The scope in which the transaction types exists. When not supplied the scope is 'default'. (optional) (default to 'default')

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_transaction_type_source(source, scope=scope, opts=opts)

        # DeleteTransactionTypeSource: Delete all transaction types for the given source and scope
        api_response = api_instance.delete_transaction_type_source(source, scope=scope)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransactionConfigurationApi->delete_transaction_type_source: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**| The source to set the transaction types for. | 
 **scope** | **str**| The scope in which the transaction types exists. When not supplied the scope is &#39;default&#39;. | [optional] [default to &#39;default&#39;]

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_side_definition**
> SideDefinition get_side_definition(side, scope=scope, as_at=as_at)

GetSideDefinition: Get the side definition for a given side name( or label)

Get the side definition user requested.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransactionConfigurationApi
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
    api_instance = api_client_factory.build(TransactionConfigurationApi)
    side = 'side_example' # str | The label to uniquely identify the side.
    scope = 'default' # str | The scope in which the side exists. When not supplied the scope is 'default'. (optional) (default to 'default')
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the transaction types. Defaults to returning the latest versions if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_side_definition(side, scope=scope, as_at=as_at, opts=opts)

        # GetSideDefinition: Get the side definition for a given side name( or label)
        api_response = api_instance.get_side_definition(side, scope=scope, as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransactionConfigurationApi->get_side_definition: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **side** | **str**| The label to uniquely identify the side. | 
 **scope** | **str**| The scope in which the side exists. When not supplied the scope is &#39;default&#39;. | [optional] [default to &#39;default&#39;]
 **as_at** | **datetime**| The asAt datetime at which to retrieve the transaction types. Defaults to returning the latest versions if not specified. | [optional] 

### Return type

[**SideDefinition**](SideDefinition.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_transaction_type**
> TransactionType get_transaction_type(source, type, as_at=as_at, scope=scope)

GetTransactionType: Get a single transaction configuration type

Get a single transaction type. Returns failure if not found

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransactionConfigurationApi
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
    api_instance = api_client_factory.build(TransactionConfigurationApi)
    source = 'source_example' # str | The source that the type is in
    type = 'type_example' # str | One of the type's aliases
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the transaction configuration.             Defaults to returning the latest version of the transaction configuration type if not specified (optional)
    scope = 'default' # str | The scope in which the transaction types exists. When not supplied the scope is 'default'. (optional) (default to 'default')

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_transaction_type(source, type, as_at=as_at, scope=scope, opts=opts)

        # GetTransactionType: Get a single transaction configuration type
        api_response = api_instance.get_transaction_type(source, type, as_at=as_at, scope=scope)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransactionConfigurationApi->get_transaction_type: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**| The source that the type is in | 
 **type** | **str**| One of the type&#39;s aliases | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the transaction configuration.             Defaults to returning the latest version of the transaction configuration type if not specified | [optional] 
 **scope** | **str**| The scope in which the transaction types exists. When not supplied the scope is &#39;default&#39;. | [optional] [default to &#39;default&#39;]

### Return type

[**TransactionType**](TransactionType.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_side_definitions**
> ResourceListOfSideDefinition list_side_definitions(as_at=as_at, scope=scope)

ListSideDefinitions: List the side definitions

List all the side definitions in the given scope

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransactionConfigurationApi
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
    api_instance = api_client_factory.build(TransactionConfigurationApi)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the transaction types. Defaults to returning the latest versions if not specified. (optional)
    scope = 'default' # str | The scope in which the side exists. When not supplied the scope is 'default'. (optional) (default to 'default')

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_side_definitions(as_at=as_at, scope=scope, opts=opts)

        # ListSideDefinitions: List the side definitions
        api_response = api_instance.list_side_definitions(as_at=as_at, scope=scope)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransactionConfigurationApi->list_side_definitions: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to retrieve the transaction types. Defaults to returning the latest versions if not specified. | [optional] 
 **scope** | **str**| The scope in which the side exists. When not supplied the scope is &#39;default&#39;. | [optional] [default to &#39;default&#39;]

### Return type

[**ResourceListOfSideDefinition**](ResourceListOfSideDefinition.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_transaction_types**
> Dict[str, List[TransactionType]] list_transaction_types(as_at=as_at, scope=scope)

ListTransactionTypes: List transaction types

Get the list of current transaction types. For information on the default transaction types provided with LUSID, see https://support.lusid.com/knowledgebase/article/KA-01873/.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransactionConfigurationApi
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
    api_instance = api_client_factory.build(TransactionConfigurationApi)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the transaction types. Defaults             to returning the latest versions if not specified. (optional)
    scope = 'default' # str | The scope in which the side exists. When not supplied the scope is 'default'. (optional) (default to 'default')

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_transaction_types(as_at=as_at, scope=scope, opts=opts)

        # ListTransactionTypes: List transaction types
        api_response = api_instance.list_transaction_types(as_at=as_at, scope=scope)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransactionConfigurationApi->list_transaction_types: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to retrieve the transaction types. Defaults             to returning the latest versions if not specified. | [optional] 
 **scope** | **str**| The scope in which the side exists. When not supplied the scope is &#39;default&#39;. | [optional] [default to &#39;default&#39;]

### Return type

**Dict[str, List[TransactionType]]**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **set_side_definition**
> SideDefinition set_side_definition(side, side_definition_request, scope=scope)

SetSideDefinition: Set a side definition

Set a new side definition for use in a transaction type. For more information, see https://support.lusid.com/knowledgebase/article/KA-01875.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransactionConfigurationApi
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
    api_instance = api_client_factory.build(TransactionConfigurationApi)
    side = 'side_example' # str | The label to uniquely identify the side.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # side_definition_request = SideDefinitionRequest.from_json("")
    # side_definition_request = SideDefinitionRequest.from_dict({})
    side_definition_request = SideDefinitionRequest()
    scope = 'default' # str | The scope in which the side exists. When not supplied the scope is 'default'. (optional) (default to 'default')

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.set_side_definition(side, side_definition_request, scope=scope, opts=opts)

        # SetSideDefinition: Set a side definition
        api_response = api_instance.set_side_definition(side, side_definition_request, scope=scope)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransactionConfigurationApi->set_side_definition: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **side** | **str**| The label to uniquely identify the side. | 
 **side_definition_request** | [**SideDefinitionRequest**](SideDefinitionRequest.md)| The side definition to create or replace. | 
 **scope** | **str**| The scope in which the side exists. When not supplied the scope is &#39;default&#39;. | [optional] [default to &#39;default&#39;]

### Return type

[**SideDefinition**](SideDefinition.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **set_side_definitions**
> ResourceListOfSideDefinition set_side_definitions(sides_definition_request, scope=scope)

SetSideDefinitions: Set the given side definitions

Set a new side definition for use in a transaction type. For more information, see https://support.lusid.com/knowledgebase/article/KA-01875.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransactionConfigurationApi
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
    api_instance = api_client_factory.build(TransactionConfigurationApi)
    sides_definition_request = [{"side":"Side1","sideRequest":{"security":"Txn:LusidInstrumentId","currency":"Txn:TradeCurrency","rate":"Txn:Units","units":"1","amount":"Transaction/MyScope/TradeAmount","notionalAmount":"Transaction/default/NotionalAmount","currentFace":"Txn:CurrentFace"}}] # List[SidesDefinitionRequest] | The list of side definitions to create, or replace.
    scope = 'default' # str | The scope in which the side exists. When not supplied the scope is 'default'. (optional) (default to 'default')

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.set_side_definitions(sides_definition_request, scope=scope, opts=opts)

        # SetSideDefinitions: Set the given side definitions
        api_response = api_instance.set_side_definitions(sides_definition_request, scope=scope)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransactionConfigurationApi->set_side_definitions: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sides_definition_request** | [**List[SidesDefinitionRequest]**](SidesDefinitionRequest.md)| The list of side definitions to create, or replace. | 
 **scope** | **str**| The scope in which the side exists. When not supplied the scope is &#39;default&#39;. | [optional] [default to &#39;default&#39;]

### Return type

[**ResourceListOfSideDefinition**](ResourceListOfSideDefinition.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **set_transaction_type**
> TransactionType set_transaction_type(source, type, transaction_type_request, scope=scope)

SetTransactionType: Set a specific transaction type

Set a transaction type for the given source and type. If the requested transaction type does not exist, it will be created  WARNING! Changing existing transaction types has a material impact on how data, new and old, is processed and aggregated by LUSID, and will affect your whole organisation. Only call this API if you are fully aware of the implications of the change.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransactionConfigurationApi
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
    api_instance = api_client_factory.build(TransactionConfigurationApi)
    source = 'source_example' # str | The source to set the transaction configuration for
    type = 'type_example' # str | One of the transaction configuration alias types to uniquely identify the configuration. If this type does not exist, then a new transaction type is created using the body of the request in the given source, without including this type

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # transaction_type_request = TransactionTypeRequest.from_json("")
    # transaction_type_request = TransactionTypeRequest.from_dict({})
    transaction_type_request = TransactionTypeRequest()
    scope = 'default' # str | The scope in which the transaction types exists. When not supplied the scope is 'default'. (optional) (default to 'default')

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.set_transaction_type(source, type, transaction_type_request, scope=scope, opts=opts)

        # SetTransactionType: Set a specific transaction type
        api_response = api_instance.set_transaction_type(source, type, transaction_type_request, scope=scope)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransactionConfigurationApi->set_transaction_type: %s\n" % e)

main()
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

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **set_transaction_type_source**
> ResourceListOfTransactionType set_transaction_type_source(source, transaction_type_request, scope=scope)

SetTransactionTypeSource: Set the transaction types for the given source and scope

The complete set of transaction types for the source.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TransactionConfigurationApi
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
    api_instance = api_client_factory.build(TransactionConfigurationApi)
    source = 'source_example' # str | The source to set the transaction types for.
    transaction_type_request = [{"aliases":[{"type":"Simple-Sell","description":"Sale","transactionClass":"MyDefault","transactionRoles":"LongShorter","isDefault":false}],"movements":[{"movementTypes":"Traded","side":"Side1","direction":-1,"properties":{},"mappings":[],"movementOptions":[]},{"movementTypes":"CashSettlement","side":"Side2","direction":1,"properties":{},"mappings":[],"movementOptions":[],"settlementDateOverride":"Transaction/MyScope/SettlementDateOverride"}],"properties":{"TransactionConfiguration/default/Example":{"key":"TransactionConfiguration/default/Example","value":{"labelValue":"Value"}}},"calculations":[{"type":"TaxAmounts","side":"Side1"}]}] # List[TransactionTypeRequest] | The set of transaction types.
    scope = 'default' # str | The scope in which the transaction types exists. When not supplied the scope is 'default'. (optional) (default to 'default')

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.set_transaction_type_source(source, transaction_type_request, scope=scope, opts=opts)

        # SetTransactionTypeSource: Set the transaction types for the given source and scope
        api_response = api_instance.set_transaction_type_source(source, transaction_type_request, scope=scope)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TransactionConfigurationApi->set_transaction_type_source: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**| The source to set the transaction types for. | 
 **transaction_type_request** | [**List[TransactionTypeRequest]**](TransactionTypeRequest.md)| The set of transaction types. | 
 **scope** | **str**| The scope in which the transaction types exists. When not supplied the scope is &#39;default&#39;. | [optional] [default to &#39;default&#39;]

### Return type

[**ResourceListOfTransactionType**](ResourceListOfTransactionType.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

