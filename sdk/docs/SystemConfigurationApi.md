# lusid.SystemConfigurationApi

All URIs are relative to *http://local-unit-test-server.lusid.com:60304*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_configuration_transaction_type**](SystemConfigurationApi.md#create_configuration_transaction_type) | **POST** /api/systemconfiguration/transactions/type | [EARLY ACCESS] Create transaction type
[**list_configuration_transaction_types**](SystemConfigurationApi.md#list_configuration_transaction_types) | **GET** /api/systemconfiguration/transactions | [EARLY ACCESS] List transaction types


# **create_configuration_transaction_type**
> TransactionSetConfigurationData create_configuration_transaction_type(transaction_configuration_data_request=transaction_configuration_data_request)

[EARLY ACCESS] Create transaction type

Create a new transaction type by specifying a definition and mappings to movements.

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

# Defining host is optional and default to http://local-unit-test-server.lusid.com:60304
configuration.host = "http://local-unit-test-server.lusid.com:60304"
# Create an instance of the API class
api_instance = lusid.SystemConfigurationApi(lusid.ApiClient(configuration))
transaction_configuration_data_request = {"aliases":[{"type":"Another-Sell","description":"Sale","transactionClass":"MyDefault","transactionGroup":"MyGroup","transactionRoles":"LongShorter"}],"movements":[{"movementTypes":"StockMovement","side":"Side1","direction":-1,"properties":{},"mappings":[]},{"movementTypes":"CashCommitment","side":"Side2","direction":1,"properties":{},"mappings":[]}],"properties":{}} # TransactionConfigurationDataRequest | A transaction type definition. (optional)

try:
    # [EARLY ACCESS] Create transaction type
    api_response = api_instance.create_configuration_transaction_type(transaction_configuration_data_request=transaction_configuration_data_request)
    pprint(api_response)
except ApiException as e:
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
**201** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_configuration_transaction_types**
> TransactionSetConfigurationData list_configuration_transaction_types(as_at=as_at)

[EARLY ACCESS] List transaction types

Get the list of current transaction types. For information on the default transaction types provided with  LUSID, see https://support.lusid.com/knowledgebase/article/KA-01873/.

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

# Defining host is optional and default to http://local-unit-test-server.lusid.com:60304
configuration.host = "http://local-unit-test-server.lusid.com:60304"
# Create an instance of the API class
api_instance = lusid.SystemConfigurationApi(lusid.ApiClient(configuration))
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the transaction types. Defaults              to returning the latest versions if not specified. (optional)

try:
    # [EARLY ACCESS] List transaction types
    api_response = api_instance.list_configuration_transaction_types(as_at=as_at)
    pprint(api_response)
except ApiException as e:
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

