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
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://www.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://www.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://www.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.AddressKeyDefinitionApi(api_client)
    create_address_key_definition_request = {"addressKey":"Instrument/default/LusidInstrumentId","type":"Text"} # CreateAddressKeyDefinitionRequest | The request used to create the address key definition.

    try:
        # [EARLY ACCESS] CreateAddressKeyDefinition: Create an AddressKeyDefinition.
        api_response = api_instance.create_address_key_definition(create_address_key_definition_request)
        pprint(api_response)
    except ApiException as e:
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
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://www.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://www.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://www.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.AddressKeyDefinitionApi(api_client)
    key = 'key_example' # str | The address key of the address key definition.
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the address key definition. Defaults to return the latest version of the address key definition if not specified. (optional)

    try:
        # [EARLY ACCESS] GetAddressKeyDefinition: Get an AddressKeyDefinition.
        api_response = api_instance.get_address_key_definition(key, as_at=as_at)
        pprint(api_response)
    except ApiException as e:
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
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://www.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://www.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://www.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.AddressKeyDefinitionApi(api_client)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the address key definition.              Defaults to return the latest version of the address key definition if not specified. (optional)
page = 'page_example' # str | The pagination token to use to continue listing address key definitions from a previous call to list address key definitions.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields              must not have changed since the original request. (optional)
limit = 56 # int | When paginating, limit the number of returned results to this many. (optional)
filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid. (optional)

    try:
        # [EARLY ACCESS] ListAddressKeyDefinitions: List AddressKeyDefinitions.
        api_response = api_instance.list_address_key_definitions(as_at=as_at, page=page, limit=limit, filter=filter)
        pprint(api_response)
    except ApiException as e:
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

