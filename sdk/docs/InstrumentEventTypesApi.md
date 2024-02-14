# lusid.InstrumentEventTypesApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_transaction_template**](InstrumentEventTypesApi.md#create_transaction_template) | **POST** /api/instrumenteventtypes/{instrumentEventType}/transactiontemplates/{instrumentType}/{scope} | [EXPERIMENTAL] CreateTransactionTemplate: Create Transaction Template
[**get_transaction_template**](InstrumentEventTypesApi.md#get_transaction_template) | **GET** /api/instrumenteventtypes/{instrumentEventType}/transactiontemplates/{instrumentType}/{scope} | [EXPERIMENTAL] GetTransactionTemplate: Get Transaction Template
[**get_transaction_template_specification**](InstrumentEventTypesApi.md#get_transaction_template_specification) | **GET** /api/instrumenteventtypes/{instrumentEventType}/transactiontemplatespecification | [EXPERIMENTAL] GetTransactionTemplateSpecification: Get Transaction Template Specification.


# **create_transaction_template**
> TransactionTemplate create_transaction_template(instrument_event_type, instrument_type, scope, transaction_template_request)

[EXPERIMENTAL] CreateTransactionTemplate: Create Transaction Template

Create a transaction template for a particular instrument event type in a scope.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from lusid.models.transaction_template import TransactionTemplate
from lusid.models.transaction_template_request import TransactionTemplateRequest
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
    api_instance = api_client_factory.build(lusid.InstrumentEventTypesApi)
    instrument_event_type = 'instrument_event_type_example' # str | The type of instrument events that the template is applied to.
    instrument_type = 'instrument_type_example' # str | The instrument type of the transaction template. The combination of the instrument              event type, instrument type and scope uniquely identifies a transaction template
    scope = 'scope_example' # str | The scope in which the template lies.
    transaction_template_request = {"description":"User-created template for overriding the default bond coupon template.","componentTransactions":[{"displayName":"Bond Income Override","transactionFieldMap":{"transactionId":"{{instrumentEventId}}-{{holdingId}}","type":"BondCoupon","source":"MyTransactionTypeScope","instrument":"{{lusidInstrumentId}}","transactionDate":"{{BondCouponEvent.exDate}}","settlementDate":"{{BondCouponEvent.paymentDate}}","units":"{{eligibleBalance}}","transactionPrice":{"price":"{{BondCouponEvent.couponPerUnit}}","type":"CashFlowPerUnit"},"transactionCurrency":"{{BondCouponEvent.currency}}","exchangeRate":"1","totalConsideration":{"currency":"{{BondCouponEvent.couponAmount}}","amount":"{{BondCouponEvent.currency}}"}}}]} # TransactionTemplateRequest | A request defining a new transaction template to be created.

    try:
        # [EXPERIMENTAL] CreateTransactionTemplate: Create Transaction Template
        api_response = await api_instance.create_transaction_template(instrument_event_type, instrument_type, scope, transaction_template_request)
        print("The response of InstrumentEventTypesApi->create_transaction_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstrumentEventTypesApi->create_transaction_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instrument_event_type** | **str**| The type of instrument events that the template is applied to. | 
 **instrument_type** | **str**| The instrument type of the transaction template. The combination of the instrument              event type, instrument type and scope uniquely identifies a transaction template | 
 **scope** | **str**| The scope in which the template lies. | 
 **transaction_template_request** | [**TransactionTemplateRequest**](TransactionTemplateRequest.md)| A request defining a new transaction template to be created. | 

### Return type

[**TransactionTemplate**](TransactionTemplate.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The response of the transaction template that was created. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction_template**
> TransactionTemplate get_transaction_template(instrument_event_type, instrument_type, scope, as_at=as_at)

[EXPERIMENTAL] GetTransactionTemplate: Get Transaction Template

Gets the Transaction Template that for the instrument event type within the scope specified.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from lusid.models.transaction_template import TransactionTemplate
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
    api_instance = api_client_factory.build(lusid.InstrumentEventTypesApi)
    instrument_event_type = 'instrument_event_type_example' # str | The instrument event type of the transaction template
    instrument_type = 'instrument_type_example' # str | The instrument type of the transaction template. The combination of the instrument              event type, instrument type and scope uniquely identifies a transaction template
    scope = 'scope_example' # str | The scope in which the template lies. When not supplied the scope is 'default'.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The AsAt time of the requested Transaction Template (optional)

    try:
        # [EXPERIMENTAL] GetTransactionTemplate: Get Transaction Template
        api_response = await api_instance.get_transaction_template(instrument_event_type, instrument_type, scope, as_at=as_at)
        print("The response of InstrumentEventTypesApi->get_transaction_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstrumentEventTypesApi->get_transaction_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instrument_event_type** | **str**| The instrument event type of the transaction template | 
 **instrument_type** | **str**| The instrument type of the transaction template. The combination of the instrument              event type, instrument type and scope uniquely identifies a transaction template | 
 **scope** | **str**| The scope in which the template lies. When not supplied the scope is &#39;default&#39;. | 
 **as_at** | **datetime**| The AsAt time of the requested Transaction Template | [optional] 

### Return type

[**TransactionTemplate**](TransactionTemplate.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The asAt datetime at which the transaction template was created. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction_template_specification**
> TransactionTemplateSpecification get_transaction_template_specification(instrument_event_type)

[EXPERIMENTAL] GetTransactionTemplateSpecification: Get Transaction Template Specification.

Retrieve the transaction template specification for a particular event type.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from lusid.models.transaction_template_specification import TransactionTemplateSpecification
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
    api_instance = api_client_factory.build(lusid.InstrumentEventTypesApi)
    instrument_event_type = 'instrument_event_type_example' # str | The requested instrument event type.

    try:
        # [EXPERIMENTAL] GetTransactionTemplateSpecification: Get Transaction Template Specification.
        api_response = await api_instance.get_transaction_template_specification(instrument_event_type)
        print("The response of InstrumentEventTypesApi->get_transaction_template_specification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstrumentEventTypesApi->get_transaction_template_specification: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instrument_event_type** | **str**| The requested instrument event type. | 

### Return type

[**TransactionTemplateSpecification**](TransactionTemplateSpecification.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Transaction Template Specification. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

