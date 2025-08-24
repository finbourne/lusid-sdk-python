# lusid.AddressKeyDefinitionApi

All URIs are relative to *https://fbn-prd.lusid.com/api*

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

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    AddressKeyDefinitionApi
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
    api_instance = api_client_factory.build(AddressKeyDefinitionApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # create_address_key_definition_request = CreateAddressKeyDefinitionRequest.from_json("")
    # create_address_key_definition_request = CreateAddressKeyDefinitionRequest.from_dict({})
    create_address_key_definition_request = CreateAddressKeyDefinitionRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.create_address_key_definition(create_address_key_definition_request, opts=opts)

        # [EARLY ACCESS] CreateAddressKeyDefinition: Create an AddressKeyDefinition.
        api_response = api_instance.create_address_key_definition(create_address_key_definition_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling AddressKeyDefinitionApi->create_address_key_definition: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_address_key_definition_request** | [**CreateAddressKeyDefinitionRequest**](CreateAddressKeyDefinitionRequest.md)| The request used to create the address key definition. | 

### Return type

[**AddressKeyDefinition**](AddressKeyDefinition.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created address key definition. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_address_key_definition**
> AddressKeyDefinition get_address_key_definition(key, as_at=as_at)

[EARLY ACCESS] GetAddressKeyDefinition: Get an AddressKeyDefinition.

Get the address key definition with the given address key at the specific asAt time.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    AddressKeyDefinitionApi
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
    api_instance = api_client_factory.build(AddressKeyDefinitionApi)
    key = 'key_example' # str | The address key of the address key definition.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the address key definition. Defaults to return the latest version of the address key definition if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_address_key_definition(key, as_at=as_at, opts=opts)

        # [EARLY ACCESS] GetAddressKeyDefinition: Get an AddressKeyDefinition.
        api_response = api_instance.get_address_key_definition(key, as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling AddressKeyDefinitionApi->get_address_key_definition: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The address key of the address key definition. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the address key definition. Defaults to return the latest version of the address key definition if not specified. | [optional] 

### Return type

[**AddressKeyDefinition**](AddressKeyDefinition.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The address key definition with the given address key. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_address_key_definitions**
> PagedResourceListOfAddressKeyDefinition list_address_key_definitions(as_at=as_at, page=page, limit=limit, filter=filter)

[EARLY ACCESS] ListAddressKeyDefinitions: List AddressKeyDefinitions.

Fetch the last pre-AsAt date version of each address key definition.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    AddressKeyDefinitionApi
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
    api_instance = api_client_factory.build(AddressKeyDefinitionApi)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the address key definition.              Defaults to return the latest version of the address key definition if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing address key definitions from a previous call to list address key definitions.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields              must not have changed since the original request. (optional)
    limit = 56 # int | When paginating, limit the number of returned results to this many. (optional)
    filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_address_key_definitions(as_at=as_at, page=page, limit=limit, filter=filter, opts=opts)

        # [EARLY ACCESS] ListAddressKeyDefinitions: List AddressKeyDefinitions.
        api_response = api_instance.list_address_key_definitions(as_at=as_at, page=page, limit=limit, filter=filter)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling AddressKeyDefinitionApi->list_address_key_definitions: %s\n" % e)

main()
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

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of address key definitions. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

