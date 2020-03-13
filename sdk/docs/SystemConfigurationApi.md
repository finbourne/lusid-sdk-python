# lusid.SystemConfigurationApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_configuration_transaction_type**](SystemConfigurationApi.md#create_configuration_transaction_type) | **POST** /api/systemconfiguration/transactions/type | [EARLY ACCESS] Create transaction type
[**create_side_definition**](SystemConfigurationApi.md#create_side_definition) | **POST** /api/systemconfiguration/transactions/side | [EXPERIMENTAL] Create side definition
[**list_configuration_transaction_types**](SystemConfigurationApi.md#list_configuration_transaction_types) | **GET** /api/systemconfiguration/transactions | [EARLY ACCESS] List transaction types
[**set_configuration_transaction_types**](SystemConfigurationApi.md#set_configuration_transaction_types) | **PUT** /api/systemconfiguration/transactions | [EXPERIMENTAL] Set transaction types


# **create_configuration_transaction_type**
> TransactionSetConfigurationData create_configuration_transaction_type(type=type)

[EARLY ACCESS] Create transaction type

Create a new transaction type by specifying a definition and the mappings to movements

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://localhost/api
configuration.host = "http://localhost/api"

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.SystemConfigurationApi(api_client)
    type = lusid.TransactionConfigurationDataRequest() # TransactionConfigurationDataRequest | A transaction type definition (optional)

    try:
        # [EARLY ACCESS] Create transaction type
        api_response = api_instance.create_configuration_transaction_type(type=type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SystemConfigurationApi->create_configuration_transaction_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**TransactionConfigurationDataRequest**](TransactionConfigurationDataRequest.md)| A transaction type definition | [optional] 

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
**201** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_side_definition**
> TransactionSetConfigurationData create_side_definition(side=side)

[EXPERIMENTAL] Create side definition

Create a new side definition for us in transaction type configuration

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://localhost/api
configuration.host = "http://localhost/api"

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.SystemConfigurationApi(api_client)
    side = lusid.SideConfigurationDataRequest() # SideConfigurationDataRequest | The definition of the side to be created. (optional)

    try:
        # [EXPERIMENTAL] Create side definition
        api_response = api_instance.create_side_definition(side=side)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SystemConfigurationApi->create_side_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **side** | [**SideConfigurationDataRequest**](SideConfigurationDataRequest.md)| The definition of the side to be created. | [optional] 

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
**201** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_configuration_transaction_types**
> TransactionSetConfigurationData list_configuration_transaction_types()

[EARLY ACCESS] List transaction types

Get the list of persisted transaction types

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://localhost/api
configuration.host = "http://localhost/api"

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.SystemConfigurationApi(api_client)
    
    try:
        # [EARLY ACCESS] List transaction types
        api_response = api_instance.list_configuration_transaction_types()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SystemConfigurationApi->list_configuration_transaction_types: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_configuration_transaction_types**
> TransactionSetConfigurationData set_configuration_transaction_types(types=types)

[EXPERIMENTAL] Set transaction types

Set all transaction types to be used by the movements engine, for the organisation                WARNING! Changing these mappings will have a material impact on how data, new and old, is processed and aggregated by LUSID. This will affect your whole organisation. Only change if you are fully aware of the implications of the change.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://localhost/api
configuration.host = "http://localhost/api"

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.SystemConfigurationApi(api_client)
    types = lusid.TransactionSetConfigurationDataRequest() # TransactionSetConfigurationDataRequest | The complete set of transaction type definitions (optional)

    try:
        # [EXPERIMENTAL] Set transaction types
        api_response = api_instance.set_configuration_transaction_types(types=types)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SystemConfigurationApi->set_configuration_transaction_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **types** | [**TransactionSetConfigurationDataRequest**](TransactionSetConfigurationDataRequest.md)| The complete set of transaction type definitions | [optional] 

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

