# lusid.SystemConfigurationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_configuration_transaction_type**](SystemConfigurationApi.md#create_configuration_transaction_type) | **POST** /api/systemconfiguration/transactiontypes | Create transaction type
[**list_configuration_transaction_types**](SystemConfigurationApi.md#list_configuration_transaction_types) | **GET** /api/systemconfiguration/transactiontypes | List transaction types
[**set_configuration_transaction_types**](SystemConfigurationApi.md#set_configuration_transaction_types) | **PUT** /api/systemconfiguration/transactiontypes | Set transaction types


# **create_configuration_transaction_type**
> ResourceListOfTransactionConfigurationData create_configuration_transaction_type(type=type)

Create transaction type

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

# create an instance of the API class
api_instance = lusid.SystemConfigurationApi(lusid.ApiClient(configuration))
type = lusid.TransactionConfigurationDataRequest() # TransactionConfigurationDataRequest | A transaction type definition (optional)

try:
    # Create transaction type
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

[**ResourceListOfTransactionConfigurationData**](ResourceListOfTransactionConfigurationData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_configuration_transaction_types**
> ResourceListOfTransactionConfigurationData list_configuration_transaction_types()

List transaction types

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

# create an instance of the API class
api_instance = lusid.SystemConfigurationApi(lusid.ApiClient(configuration))

try:
    # List transaction types
    api_response = api_instance.list_configuration_transaction_types()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemConfigurationApi->list_configuration_transaction_types: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResourceListOfTransactionConfigurationData**](ResourceListOfTransactionConfigurationData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_configuration_transaction_types**
> ResourceListOfTransactionConfigurationData set_configuration_transaction_types(types=types)

Set transaction types

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

# create an instance of the API class
api_instance = lusid.SystemConfigurationApi(lusid.ApiClient(configuration))
types = None # list[TransactionConfigurationDataRequest] | The complete set of transaction type definitions (optional)

try:
    # Set transaction types
    api_response = api_instance.set_configuration_transaction_types(types=types)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemConfigurationApi->set_configuration_transaction_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **types** | [**list[TransactionConfigurationDataRequest]**](list.md)| The complete set of transaction type definitions | [optional] 

### Return type

[**ResourceListOfTransactionConfigurationData**](ResourceListOfTransactionConfigurationData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

