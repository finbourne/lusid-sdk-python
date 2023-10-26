# lusid.SystemConfigurationApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_configuration_transaction_type**](SystemConfigurationApi.md#create_configuration_transaction_type) | **POST** /api/systemconfiguration/transactions/type | [EARLY ACCESS] CreateConfigurationTransactionType: Create transaction type
[**create_side_definition**](SystemConfigurationApi.md#create_side_definition) | **POST** /api/systemconfiguration/transactions/side | [EXPERIMENTAL] CreateSideDefinition: Create side definition
[**delete_transaction_configuration_source**](SystemConfigurationApi.md#delete_transaction_configuration_source) | **DELETE** /api/systemconfiguration/transactions/type/{source} | [EXPERIMENTAL] DeleteTransactionConfigurationSource: Delete all transaction configurations for a source
[**get_transaction_configuration_source**](SystemConfigurationApi.md#get_transaction_configuration_source) | **GET** /api/systemconfiguration/transactions/type/{source} | [EXPERIMENTAL] GetTransactionConfigurationSource: Get all transaction configurations for a source
[**list_configuration_transaction_types**](SystemConfigurationApi.md#list_configuration_transaction_types) | **GET** /api/systemconfiguration/transactions | [EARLY ACCESS] ListConfigurationTransactionTypes: List transaction types
[**set_configuration_transaction_types**](SystemConfigurationApi.md#set_configuration_transaction_types) | **PUT** /api/systemconfiguration/transactions | [EXPERIMENTAL] SetConfigurationTransactionTypes: Set transaction types
[**set_transaction_configuration_source**](SystemConfigurationApi.md#set_transaction_configuration_source) | **PUT** /api/systemconfiguration/transactions/type/{source} | [EXPERIMENTAL] SetTransactionConfigurationSource: Set transaction types for a source


# **create_configuration_transaction_type**
> TransactionSetConfigurationData create_configuration_transaction_type(transaction_configuration_data_request=transaction_configuration_data_request)

[EARLY ACCESS] CreateConfigurationTransactionType: Create transaction type

Create a new transaction type by specifying a definition and mappings to movements.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from lusid.models.transaction_configuration_data_request import TransactionConfigurationDataRequest
from lusid.models.transaction_set_configuration_data import TransactionSetConfigurationData
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
    api_instance = api_client_factory.build(lusid.SystemConfigurationApi)
    transaction_configuration_data_request = {"aliases":[{"type":"Another-Sell","description":"Sale","transactionClass":"MyDefault","transactionGroup":"mysource","source":"mysource","transactionRoles":"LongShorter","isDefault":false}],"movements":[{"movementTypes":"StockMovement","side":"Side1","direction":-1,"properties":{},"mappings":[],"movementOptions":[]},{"movementTypes":"CashCommitment","side":"Side2","direction":1,"properties":{},"mappings":[],"movementOptions":[]}],"properties":{}} # TransactionConfigurationDataRequest | A transaction type definition. (optional)

    try:
        # [EARLY ACCESS] CreateConfigurationTransactionType: Create transaction type
        api_response = await api_instance.create_configuration_transaction_type(transaction_configuration_data_request=transaction_configuration_data_request)
        print("The response of SystemConfigurationApi->create_configuration_transaction_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemConfigurationApi->create_configuration_transaction_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_configuration_data_request** | [**TransactionConfigurationDataRequest**](TransactionConfigurationDataRequest.md)| A transaction type definition. | [optional] 

### Return type

[**TransactionSetConfigurationData**](TransactionSetConfigurationData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_side_definition**
> TransactionSetConfigurationData create_side_definition(side_configuration_data_request=side_configuration_data_request)

[EXPERIMENTAL] CreateSideDefinition: Create side definition

Create a new side definition for use in a transaction type. For more information, see https://support.lusid.com/knowledgebase/article/KA-01875.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from lusid.models.side_configuration_data_request import SideConfigurationDataRequest
from lusid.models.transaction_set_configuration_data import TransactionSetConfigurationData
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
    api_instance = api_client_factory.build(lusid.SystemConfigurationApi)
    side_configuration_data_request = {"side":"Side_Test","security":"security","currency":"currency","rate":"0.7","units":"300","amount":"2000"} # SideConfigurationDataRequest | The definition of the side. (optional)

    try:
        # [EXPERIMENTAL] CreateSideDefinition: Create side definition
        api_response = await api_instance.create_side_definition(side_configuration_data_request=side_configuration_data_request)
        print("The response of SystemConfigurationApi->create_side_definition:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemConfigurationApi->create_side_definition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **side_configuration_data_request** | [**SideConfigurationDataRequest**](SideConfigurationDataRequest.md)| The definition of the side. | [optional] 

### Return type

[**TransactionSetConfigurationData**](TransactionSetConfigurationData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_transaction_configuration_source**
> DeletedEntityResponse delete_transaction_configuration_source(source)

[EXPERIMENTAL] DeleteTransactionConfigurationSource: Delete all transaction configurations for a source

/// WARNING! Changing existing transaction types has a material impact on how data, new and old,  is processed and aggregated by LUSID, and will affect your whole organisation. Only call this API if you are fully aware of the implications of the change.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from lusid.models.deleted_entity_response import DeletedEntityResponse
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
    api_instance = api_client_factory.build(lusid.SystemConfigurationApi)
    source = 'source_example' # str | The source to delete transaction configurations for

    try:
        # [EXPERIMENTAL] DeleteTransactionConfigurationSource: Delete all transaction configurations for a source
        api_response = await api_instance.delete_transaction_configuration_source(source)
        print("The response of SystemConfigurationApi->delete_transaction_configuration_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemConfigurationApi->delete_transaction_configuration_source: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**| The source to delete transaction configurations for | 

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

# **get_transaction_configuration_source**
> TransactionSetConfigurationData get_transaction_configuration_source(source, as_at=as_at)

[EXPERIMENTAL] GetTransactionConfigurationSource: Get all transaction configurations for a source

Returns failure if requested source is not found

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from lusid.models.transaction_set_configuration_data import TransactionSetConfigurationData
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
    api_instance = api_client_factory.build(lusid.SystemConfigurationApi)
    source = 'source_example' # str | The source for which to retrieve transaction configurations
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the transaction configurations.              Defaults to returning the latest version of the transaction configurations if not specified. (optional)

    try:
        # [EXPERIMENTAL] GetTransactionConfigurationSource: Get all transaction configurations for a source
        api_response = await api_instance.get_transaction_configuration_source(source, as_at=as_at)
        print("The response of SystemConfigurationApi->get_transaction_configuration_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemConfigurationApi->get_transaction_configuration_source: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**| The source for which to retrieve transaction configurations | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the transaction configurations.              Defaults to returning the latest version of the transaction configurations if not specified. | [optional] 

### Return type

[**TransactionSetConfigurationData**](TransactionSetConfigurationData.md)

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

# **list_configuration_transaction_types**
> TransactionSetConfigurationData list_configuration_transaction_types(as_at=as_at)

[EARLY ACCESS] ListConfigurationTransactionTypes: List transaction types

Get the list of current transaction types. For information on the default transaction types provided with  LUSID, see https://support.lusid.com/knowledgebase/article/KA-01873/.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from lusid.models.transaction_set_configuration_data import TransactionSetConfigurationData
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
    api_instance = api_client_factory.build(lusid.SystemConfigurationApi)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the transaction types. Defaults              to returning the latest versions if not specified. (optional)

    try:
        # [EARLY ACCESS] ListConfigurationTransactionTypes: List transaction types
        api_response = await api_instance.list_configuration_transaction_types(as_at=as_at)
        print("The response of SystemConfigurationApi->list_configuration_transaction_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemConfigurationApi->list_configuration_transaction_types: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to retrieve the transaction types. Defaults              to returning the latest versions if not specified. | [optional] 

### Return type

[**TransactionSetConfigurationData**](TransactionSetConfigurationData.md)

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

# **set_configuration_transaction_types**
> TransactionSetConfigurationData set_configuration_transaction_types(transaction_set_configuration_data_request=transaction_set_configuration_data_request)

[EXPERIMENTAL] SetConfigurationTransactionTypes: Set transaction types

Configure all existing transaction types. Note it is not possible to configure a single existing transaction type on its own.                WARNING! Changing existing transaction types has a material impact on how data, new and old, is processed and aggregated by LUSID, and will affect your whole organisation. Only call this API if you are fully aware of the implications of the change.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from lusid.models.transaction_set_configuration_data import TransactionSetConfigurationData
from lusid.models.transaction_set_configuration_data_request import TransactionSetConfigurationDataRequest
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
    api_instance = api_client_factory.build(lusid.SystemConfigurationApi)
    transaction_set_configuration_data_request = {"transactionConfigRequests":[{"aliases":[{"type":"Simple-Sell","description":"Sale","transactionClass":"MyDefault","transactionGroup":"mysource","source":"mysource","transactionRoles":"LongShorter","isDefault":false}],"movements":[{"movementTypes":"StockMovement","side":"Side1","direction":-1,"properties":{},"mappings":[],"movementOptions":[]},{"movementTypes":"CashCommitment","side":"Side2","direction":1,"properties":{},"mappings":[],"movementOptions":[]}],"properties":{}},{"aliases":[{"type":"Sell-FIFO","description":"Sale using FIFO logic","transactionClass":"FIFO","transactionGroup":"mysource","source":"mysource","transactionRoles":"LongShorter","isDefault":false}],"movements":[{"movementTypes":"StockMovement","side":"Side1","direction":-1,"properties":{"TransactionConfiguration/default/TaxLotSelectionMethod":{"key":"TransactionConfiguration/default/TaxLotSelectionMethod","value":{"labelValue":"FirstInFirstOut"}}},"mappings":[],"movementOptions":[]},{"movementTypes":"CashCommitment","side":"Side2","direction":1,"properties":{},"mappings":[],"movementOptions":[]}],"properties":{"TransactionConfiguration/default/Example":{"key":"TransactionConfiguration/default/Example","value":{"labelValue":"Value"}}}}],"sideConfigRequests":[{"side":"Side1","security":"security","currency":"currency","rate":"0.5","units":"500","amount":"1000"},{"side":"Side2","security":"security","currency":"currency","rate":"0.75","units":"250","amount":"2000"}]} # TransactionSetConfigurationDataRequest | The complete set of transaction type definitions. (optional)

    try:
        # [EXPERIMENTAL] SetConfigurationTransactionTypes: Set transaction types
        api_response = await api_instance.set_configuration_transaction_types(transaction_set_configuration_data_request=transaction_set_configuration_data_request)
        print("The response of SystemConfigurationApi->set_configuration_transaction_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemConfigurationApi->set_configuration_transaction_types: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_set_configuration_data_request** | [**TransactionSetConfigurationDataRequest**](TransactionSetConfigurationDataRequest.md)| The complete set of transaction type definitions. | [optional] 

### Return type

[**TransactionSetConfigurationData**](TransactionSetConfigurationData.md)

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

# **set_transaction_configuration_source**
> TransactionSetConfigurationData set_transaction_configuration_source(source, set_transaction_configuration_source_request)

[EXPERIMENTAL] SetTransactionConfigurationSource: Set transaction types for a source

This will replace all the existing transaction configurations for the given source                WARNING! Changing existing transaction types has a material impact on how data, new and old, is processed and aggregated by LUSID, and will affect your whole organisation. Only call this API if you are fully aware of the implications of the change.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from lusid.models.set_transaction_configuration_source_request import SetTransactionConfigurationSourceRequest
from lusid.models.transaction_set_configuration_data import TransactionSetConfigurationData
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
    api_instance = api_client_factory.build(lusid.SystemConfigurationApi)
    source = 'source_example' # str | The source to set the transaction configurations for
    set_transaction_configuration_source_request = [{"aliases":[{"type":"Simple-Sell","description":"Sale","transactionClass":"MyDefault","transactionRole":"LongShorter","isDefault":false}],"movements":[{"movementTypes":"StockMovement","side":"Side1","direction":-1,"properties":{},"mappings":[],"movementOptions":[]},{"movementTypes":"CashCommitment","side":"Side2","direction":1,"properties":{},"mappings":[],"movementOptions":[]}],"properties":{"TransactionConfiguration/default/Example":{"key":"TransactionConfiguration/default/Example","value":{"labelValue":"Value"}}}}] # List[SetTransactionConfigurationSourceRequest] | The set of transaction configurations

    try:
        # [EXPERIMENTAL] SetTransactionConfigurationSource: Set transaction types for a source
        api_response = await api_instance.set_transaction_configuration_source(source, set_transaction_configuration_source_request)
        print("The response of SystemConfigurationApi->set_transaction_configuration_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemConfigurationApi->set_transaction_configuration_source: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**| The source to set the transaction configurations for | 
 **set_transaction_configuration_source_request** | [**List[SetTransactionConfigurationSourceRequest]**](SetTransactionConfigurationSourceRequest.md)| The set of transaction configurations | 

### Return type

[**TransactionSetConfigurationData**](TransactionSetConfigurationData.md)

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

