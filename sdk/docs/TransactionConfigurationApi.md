# lusid.TransactionConfigurationApi

All URIs are relative to *https://fbn-ci.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_transaction_type**](TransactionConfigurationApi.md#delete_transaction_type) | **DELETE** /api/transactionconfiguration/types/{source}/{type} | [EXPERIMENTAL] DeleteTransactionType: Delete a transaction type
[**get_transaction_type**](TransactionConfigurationApi.md#get_transaction_type) | **GET** /api/transactionconfiguration/types/{source}/{type} | [EXPERIMENTAL] GetTransactionType: Get a single transaction configuration type
[**list_transaction_types**](TransactionConfigurationApi.md#list_transaction_types) | **GET** /api/transactionconfiguration/types | [EXPERIMENTAL] ListTransactionTypes: List transaction types
[**set_side_definition**](TransactionConfigurationApi.md#set_side_definition) | **PUT** /api/transactionconfiguration/sides/{side} | [EXPERIMENTAL] SetSideDefinition: Set a side definition
[**set_transaction_type**](TransactionConfigurationApi.md#set_transaction_type) | **PUT** /api/transactionconfiguration/types/{source}/{type} | [EXPERIMENTAL] SetTransactionType: Set a specific transaction type


# **delete_transaction_type**
> DeletedEntityResponse delete_transaction_type(source, type)

[EXPERIMENTAL] DeleteTransactionType: Delete a transaction type

/// WARNING! Changing existing transaction types has a material impact on how data, new and old,  is processed and aggregated by LUSID, and will affect your whole organisation. Only call this API if you are fully aware of the implications of the change.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-ci.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.TransactionConfigurationApi(api_client)
    source = 'source_example' # str | The source that the type is in
    type = 'type_example' # str | One of the type's aliases

    try:
        # [EXPERIMENTAL] DeleteTransactionType: Delete a transaction type
        api_response = await api_instance.delete_transaction_type(source, type)
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

# **get_transaction_type**
> TransactionType get_transaction_type(source, type, as_at=as_at)

[EXPERIMENTAL] GetTransactionType: Get a single transaction configuration type

Get a single transaction type. Returns failure if not found

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-ci.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.TransactionConfigurationApi(api_client)
    source = 'source_example' # str | The source that the type is in
    type = 'type_example' # str | One of the type's aliases
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the transaction configuration.              Defaults to returning the latest version of the transaction configuration type if not specified (optional)

    try:
        # [EXPERIMENTAL] GetTransactionType: Get a single transaction configuration type
        api_response = await api_instance.get_transaction_type(source, type, as_at=as_at)
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

# **list_transaction_types**
> Dict[str, List[TransactionType]] list_transaction_types(as_at=as_at)

[EXPERIMENTAL] ListTransactionTypes: List transaction types

Get the list of current transaction types. For information on the default transaction types provided with  LUSID, see https://support.lusid.com/knowledgebase/article/KA-01873/.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-ci.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.TransactionConfigurationApi(api_client)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the transaction types. Defaults              to returning the latest versions if not specified. (optional)

    try:
        # [EXPERIMENTAL] ListTransactionTypes: List transaction types
        api_response = await api_instance.list_transaction_types(as_at=as_at)
        print("The response of TransactionConfigurationApi->list_transaction_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionConfigurationApi->list_transaction_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to retrieve the transaction types. Defaults              to returning the latest versions if not specified. | [optional] 

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
> SideDefinition set_side_definition(side, side_definition_request)

[EXPERIMENTAL] SetSideDefinition: Set a side definition

Set a new side definition for use in a transaction type. For more information, see https://support.lusid.com/knowledgebase/article/KA-01875.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-ci.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.TransactionConfigurationApi(api_client)
    side = 'side_example' # str | The label to uniquely identify the side.
    side_definition_request = {"security":"Txn:LusidInstrumentId","currency":"Txn:TradeCurrency","rate":"Txn:Units","units":"1","amount":"Transaction/MyScope/TradeAmount","notionalAmount":"Transaction/default/NotionalAmount"} # SideDefinitionRequest | The side definition to create or replace.

    try:
        # [EXPERIMENTAL] SetSideDefinition: Set a side definition
        api_response = await api_instance.set_side_definition(side, side_definition_request)
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

# **set_transaction_type**
> TransactionType set_transaction_type(source, type, transaction_type_request)

[EXPERIMENTAL] SetTransactionType: Set a specific transaction type

Set a transaction type for the given source and type. If the requested transaction type does not exist, it will be created    WARNING! Changing existing transaction types has a material impact on how data, new and old, is processed and aggregated by LUSID, and will affect your whole organisation. Only call this API if you are fully aware of the implications of the change.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-ci.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.TransactionConfigurationApi(api_client)
    source = 'source_example' # str | The source to set the transaction configuration for
    type = 'type_example' # str | One of the transaction configuration alias types to uniquely identify the configuration
    transaction_type_request = {"aliases":[{"type":"CustomBuy","description":"A custom buy type","transactionClass":"Buy","transactionRoles":"Longer","isDefault":false},{"type":"BuyAlias","description":"A similar buy type","transactionClass":"Buy","transactionRoles":"Longer","isDefault":false}],"movements":[{"movementTypes":"StockMovement","side":"Side1","direction":-1,"properties":{"TransactionConfiguration/default/TaxLotSelectionMethod":{"key":"TransactionConfiguration/default/TaxLotSelectionMethod","value":{"labelValue":"FirstInFirstOut"}}},"mappings":[],"movementOptions":[]},{"movementTypes":"CashCommitment","side":"Side1","direction":1,"properties":{},"mappings":[{"propertyKey":"Transaction/scopeA/Strategy","setTo":"Cash"}],"movementOptions":[]}],"properties":{"TransactionConfiguration/default/TotalConsiderationPolicy":{"key":"TransactionConfiguration/default/TotalConsiderationPolicy","value":{"labelValue":"Add"}}}} # TransactionTypeRequest | The transaction configuration to set

    try:
        # [EXPERIMENTAL] SetTransactionType: Set a specific transaction type
        api_response = await api_instance.set_transaction_type(source, type, transaction_type_request)
        print("The response of TransactionConfigurationApi->set_transaction_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionConfigurationApi->set_transaction_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**| The source to set the transaction configuration for | 
 **type** | **str**| One of the transaction configuration alias types to uniquely identify the configuration | 
 **transaction_type_request** | [**TransactionTypeRequest**](TransactionTypeRequest.md)| The transaction configuration to set | 

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

