# lusid.SystemConfigurationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_configuration_transaction_type**](SystemConfigurationApi.md#create_configuration_transaction_type) | **POST** /api/systemconfiguration/transactiontypes | [EARLY ACCESS] Create transaction type
[**list_configuration_transaction_types**](SystemConfigurationApi.md#list_configuration_transaction_types) | **GET** /api/systemconfiguration/transactiontypes | [EARLY ACCESS] List transaction types


# **create_configuration_transaction_type**
> ResourceListOfTransactionConfigurationData create_configuration_transaction_type(type=type)

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

# create an instance of the API class
api_instance = lusid.SystemConfigurationApi(lusid.ApiClient(configuration))
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

[**ResourceListOfTransactionConfigurationData**](ResourceListOfTransactionConfigurationData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_configuration_transaction_types**
> ResourceListOfTransactionConfigurationData list_configuration_transaction_types()

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

# create an instance of the API class
api_instance = lusid.SystemConfigurationApi(lusid.ApiClient(configuration))

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

[**ResourceListOfTransactionConfigurationData**](ResourceListOfTransactionConfigurationData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

