# lusid.FeeTypesApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_fee_type**](FeeTypesApi.md#create_fee_type) | **POST** /api/feetypes/{scope} | [EXPERIMENTAL] CreateFeeType: Create a FeeType.
[**delete_fee_type**](FeeTypesApi.md#delete_fee_type) | **DELETE** /api/feetypes/{scope}/{code} | [EXPERIMENTAL] DeleteFeeType: Delete a FeeType.
[**get_fee_template_specifications**](FeeTypesApi.md#get_fee_template_specifications) | **GET** /api/feetypes/feetransactiontemplatespecification | [EXPERIMENTAL] GetFeeTemplateSpecifications: Get FeeTemplateSpecifications used in the FeeType.
[**get_fee_type**](FeeTypesApi.md#get_fee_type) | **GET** /api/feetypes/{scope}/{code} | [EXPERIMENTAL] GetFeeType: Get a FeeType
[**list_fee_types**](FeeTypesApi.md#list_fee_types) | **GET** /api/feetypes | [EXPERIMENTAL] ListFeeTypes: List FeeTypes
[**update_fee_type**](FeeTypesApi.md#update_fee_type) | **PUT** /api/feetypes/{scope}/{code} | [EXPERIMENTAL] UpdateFeeType: Update a FeeType.


# **create_fee_type**
> FeeType create_fee_type(scope, fee_type_request)

[EXPERIMENTAL] CreateFeeType: Create a FeeType.

Create a FeeType that contains templates used to create fee transactions.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.fee_type import FeeType
from lusid.models.fee_type_request import FeeTypeRequest
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    FeeTypesApi,
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
    api_instance = api_client_factory.build(lusid.FeeTypesApi)
    scope = 'scope_example' # str | The scope of the FeeType.
    fee_type_request = {"code":"FeeTypeCode","name":"Fee Type Name","description":"Fee Type Description","componentTransactions":[{"displayName":"FeeTypeTemplateName","transactionFieldMap":{"transactionId":"{{FundFee.name}}-100","type":"FundsIn","source":"InputTransaction","instrument":"{{FundFee.feeInstrument}}","transactionDate":"2022-12-21T00:00:00.0000000","settlementDate":"2022-12-21T00:00:00.0000000","units":"{{FundFee.totalAccrual}}","transactionPrice":{"price":"1.0","type":"Price"},"transactionCurrency":"{{FundFee.feeCurrency}}","exchangeRate":"2.0","totalConsideration":{"currency":"{{FundFee.feeCurrency}}","amount":"{{FundFee.totalAccrual}}"}},"transactionPropertyMap":[{"propertyKey":"Transaction/scope/txnId","value":"propertyValue1"}]}]} # FeeTypeRequest | The contents of the FeeType.

    try:
        # [EXPERIMENTAL] CreateFeeType: Create a FeeType.
        api_response = await api_instance.create_fee_type(scope, fee_type_request)
        print("The response of FeeTypesApi->create_fee_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeeTypesApi->create_fee_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the FeeType. | 
 **fee_type_request** | [**FeeTypeRequest**](FeeTypeRequest.md)| The contents of the FeeType. | 

### Return type

[**FeeType**](FeeType.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Create a FeeType. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_fee_type**
> DeletedEntityResponse delete_fee_type(scope, code)

[EXPERIMENTAL] DeleteFeeType: Delete a FeeType.

Delete a FeeType that contains templates used to create fee transactions.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.deleted_entity_response import DeletedEntityResponse
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    FeeTypesApi,
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
    api_instance = api_client_factory.build(lusid.FeeTypesApi)
    scope = 'scope_example' # str | The scope of the FeeType.
    code = 'code_example' # str | The code of the fee type

    try:
        # [EXPERIMENTAL] DeleteFeeType: Delete a FeeType.
        api_response = await api_instance.delete_fee_type(scope, code)
        print("The response of FeeTypesApi->delete_fee_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeeTypesApi->delete_fee_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the FeeType. | 
 **code** | **str**| The code of the fee type | 

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
**200** | Delete a FeeType. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fee_template_specifications**
> FeeTransactionTemplateSpecification get_fee_template_specifications()

[EXPERIMENTAL] GetFeeTemplateSpecifications: Get FeeTemplateSpecifications used in the FeeType.

Get FeeTemplateSpecifications used in the FeeType.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.fee_transaction_template_specification import FeeTransactionTemplateSpecification
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    FeeTypesApi,
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
    api_instance = api_client_factory.build(lusid.FeeTypesApi)

    try:
        # [EXPERIMENTAL] GetFeeTemplateSpecifications: Get FeeTemplateSpecifications used in the FeeType.
        api_response = await api_instance.get_fee_template_specifications()
        print("The response of FeeTypesApi->get_fee_template_specifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeeTypesApi->get_fee_template_specifications: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**FeeTransactionTemplateSpecification**](FeeTransactionTemplateSpecification.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fee template specifications used with a FeeType. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fee_type**
> FeeType get_fee_type(scope, code, as_at=as_at)

[EXPERIMENTAL] GetFeeType: Get a FeeType

Get a FeeType that contains templates used to create fee transactions.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.fee_type import FeeType
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    FeeTypesApi,
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
    api_instance = api_client_factory.build(lusid.FeeTypesApi)
    scope = 'scope_example' # str | The scope of the FeeType
    code = 'code_example' # str | The code of the FeeType
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the FeeType. Defaults to returning the latest version of the FeeType, if not specified. (optional)

    try:
        # [EXPERIMENTAL] GetFeeType: Get a FeeType
        api_response = await api_instance.get_fee_type(scope, code, as_at=as_at)
        print("The response of FeeTypesApi->get_fee_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeeTypesApi->get_fee_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the FeeType | 
 **code** | **str**| The code of the FeeType | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the FeeType. Defaults to returning the latest version of the FeeType, if not specified. | [optional] 

### Return type

[**FeeType**](FeeType.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested FeeType. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_fee_types**
> PagedResourceListOfFeeType list_fee_types(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)

[EXPERIMENTAL] ListFeeTypes: List FeeTypes

List FeeTypes that contain templates used to create fee transactions.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.paged_resource_list_of_fee_type import PagedResourceListOfFeeType
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    FeeTypesApi,
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
    api_instance = api_client_factory.build(lusid.FeeTypesApi)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the FeeTypes. Defaults to returning the latest version of each FeeType if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing FeeTypes; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. (optional)
    limit = 56 # int | When paginating, limit the results to this number. Defaults to 100 if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the results.              For example, to filter on the Code of the FeeType type, specify \"id.Code eq 'FeeType1'\". For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. (optional)
    sort_by = ['sort_by_example'] # List[str] | A list of field names or properties to sort by, each suffixed by \" ASC\" or \" DESC\" (optional)

    try:
        # [EXPERIMENTAL] ListFeeTypes: List FeeTypes
        api_response = await api_instance.list_fee_types(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)
        print("The response of FeeTypesApi->list_fee_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeeTypesApi->list_fee_types: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list the FeeTypes. Defaults to returning the latest version of each FeeType if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing FeeTypes; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results.              For example, to filter on the Code of the FeeType type, specify \&quot;id.Code eq &#39;FeeType1&#39;\&quot;. For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot; | [optional] 

### Return type

[**PagedResourceListOfFeeType**](PagedResourceListOfFeeType.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Fee Types |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_fee_type**
> FeeType update_fee_type(scope, code, update_fee_type_request)

[EXPERIMENTAL] UpdateFeeType: Update a FeeType.

Update a FeeType that contains templates used to create fee transactions.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.fee_type import FeeType
from lusid.models.update_fee_type_request import UpdateFeeTypeRequest
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    FeeTypesApi,
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
    api_instance = api_client_factory.build(lusid.FeeTypesApi)
    scope = 'scope_example' # str | The scope of the FeeType.
    code = 'code_example' # str | The code of the fee type
    update_fee_type_request = {"name":"Fee Type Name","description":"Fee Type Description","componentTransactions":[{"displayName":"FeeTypeTemplateName","transactionFieldMap":{"transactionId":"{{FundFee.name}}-100","type":"FundsIn","source":"InputTransaction","instrument":"{{FundFee.feeInstrument}}","transactionDate":"2022-12-21T00:00:00.0000000","settlementDate":"2022-12-21T00:00:00.0000000","units":"{{FundFee.totalAccrual}}","transactionPrice":{"price":"1.0","type":"Price"},"transactionCurrency":"{{FundFee.feeCurrency}}","exchangeRate":"2.0","totalConsideration":{"currency":"{{FundFee.feeCurrency}}","amount":"{{FundFee.totalAccrual}}"}},"transactionPropertyMap":[{"propertyKey":"Transaction/scope/txnId","value":"propertyValue1"}]}]} # UpdateFeeTypeRequest | The contents of the FeeType.

    try:
        # [EXPERIMENTAL] UpdateFeeType: Update a FeeType.
        api_response = await api_instance.update_fee_type(scope, code, update_fee_type_request)
        print("The response of FeeTypesApi->update_fee_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeeTypesApi->update_fee_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the FeeType. | 
 **code** | **str**| The code of the fee type | 
 **update_fee_type_request** | [**UpdateFeeTypeRequest**](UpdateFeeTypeRequest.md)| The contents of the FeeType. | 

### Return type

[**FeeType**](FeeType.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update a FeeType. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

