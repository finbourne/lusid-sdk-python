# lusid.AddressKeyDefinitionApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_address_key_definition**](AddressKeyDefinitionApi.md#create_address_key_definition) | **POST** /api/addresskeydefinitions | [EARLY ACCESS] CreateAddressKeyDefinition: Create an AddressKeyDefinition.
[**get_address_key_definition**](AddressKeyDefinitionApi.md#get_address_key_definition) | **GET** /api/addresskeydefinitions/{key} | [EARLY ACCESS] GetAddressKeyDefinition: Get an AddressKeyDefinition.
[**list_address_key_definitions**](AddressKeyDefinitionApi.md#list_address_key_definitions) | **GET** /api/addresskeydefinitions | [EARLY ACCESS] ListAddressKeyDefinitions: List AddressKeyDefinitions.


# **create_address_key_definition**
> AddressKeyDefinition create_address_key_definition(create_address_key_definition_request)

[EARLY ACCESS] CreateAddressKeyDefinition: Create an AddressKeyDefinition.

Create the given address key definition.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from lusid.models.address_key_definition import AddressKeyDefinition
from lusid.models.create_address_key_definition_request import CreateAddressKeyDefinitionRequest
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
    api_instance = api_client_factory.build(lusid.AddressKeyDefinitionApi)
    create_address_key_definition_request = {"addressKey":"Instrument/default/LusidInstrumentId","type":"Text"} # CreateAddressKeyDefinitionRequest | The request used to create the address key definition.

    try:
        # [EARLY ACCESS] CreateAddressKeyDefinition: Create an AddressKeyDefinition.
        api_response = await api_instance.create_address_key_definition(create_address_key_definition_request)
        print("The response of AddressKeyDefinitionApi->create_address_key_definition:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddressKeyDefinitionApi->create_address_key_definition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_address_key_definition_request** | [**CreateAddressKeyDefinitionRequest**](CreateAddressKeyDefinitionRequest.md)| The request used to create the address key definition. | 

### Return type

[**AddressKeyDefinition**](AddressKeyDefinition.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created address key definition. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_address_key_definition**
> AddressKeyDefinition get_address_key_definition(key, as_at=as_at)

[EARLY ACCESS] GetAddressKeyDefinition: Get an AddressKeyDefinition.

Get the address key definition with the given address key at the specific asAt time.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from lusid.models.address_key_definition import AddressKeyDefinition
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
    api_instance = api_client_factory.build(lusid.AddressKeyDefinitionApi)
    key = 'key_example' # str | The address key of the address key definition.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the address key definition. Defaults to return the latest version of the address key definition if not specified. (optional)

    try:
        # [EARLY ACCESS] GetAddressKeyDefinition: Get an AddressKeyDefinition.
        api_response = await api_instance.get_address_key_definition(key, as_at=as_at)
        print("The response of AddressKeyDefinitionApi->get_address_key_definition:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddressKeyDefinitionApi->get_address_key_definition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The address key of the address key definition. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the address key definition. Defaults to return the latest version of the address key definition if not specified. | [optional] 

### Return type

[**AddressKeyDefinition**](AddressKeyDefinition.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The address key definition with the given address key. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_address_key_definitions**
> PagedResourceListOfAddressKeyDefinition list_address_key_definitions(as_at=as_at, page=page, limit=limit, filter=filter)

[EARLY ACCESS] ListAddressKeyDefinitions: List AddressKeyDefinitions.

Fetch the last pre-AsAt date version of each address key definition.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from lusid.models.paged_resource_list_of_address_key_definition import PagedResourceListOfAddressKeyDefinition
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
    api_instance = api_client_factory.build(lusid.AddressKeyDefinitionApi)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the address key definition.              Defaults to return the latest version of the address key definition if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing address key definitions from a previous call to list address key definitions.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields              must not have changed since the original request. (optional)
    limit = 56 # int | When paginating, limit the number of returned results to this many. (optional)
    filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid. (optional)

    try:
        # [EARLY ACCESS] ListAddressKeyDefinitions: List AddressKeyDefinitions.
        api_response = await api_instance.list_address_key_definitions(as_at=as_at, page=page, limit=limit, filter=filter)
        print("The response of AddressKeyDefinitionApi->list_address_key_definitions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddressKeyDefinitionApi->list_address_key_definitions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to retrieve the address key definition.              Defaults to return the latest version of the address key definition if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing address key definitions from a previous call to list address key definitions.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields              must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid. | [optional] 

### Return type

[**PagedResourceListOfAddressKeyDefinition**](PagedResourceListOfAddressKeyDefinition.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of address key definitions. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

