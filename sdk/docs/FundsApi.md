# lusid.FundsApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accept_estimate_point**](FundsApi.md#accept_estimate_point) | **POST** /api/funds/{scope}/{code}/valuationpoints/$acceptestimate | [EXPERIMENTAL] AcceptEstimatePoint: Accepts an Estimate Valuation Point.
[**create_fee**](FundsApi.md#create_fee) | **POST** /api/funds/{scope}/{code}/fees/{feeCode} | [EXPERIMENTAL] CreateFee: Create a Fee.
[**create_fund**](FundsApi.md#create_fund) | **POST** /api/funds/{scope} | [EXPERIMENTAL] CreateFund: Create a Fund.
[**delete_fee**](FundsApi.md#delete_fee) | **DELETE** /api/funds/{scope}/{code}/fees/{feeCode} | [EXPERIMENTAL] DeleteFee: Delete a Fee.
[**delete_fund**](FundsApi.md#delete_fund) | **DELETE** /api/funds/{scope}/{code} | [EXPERIMENTAL] DeleteFund: Delete a Fund.
[**delete_valuation_point**](FundsApi.md#delete_valuation_point) | **DELETE** /api/funds/{scope}/{code}/valuationpoints/{diaryEntryCode} | [EXPERIMENTAL] DeleteValuationPoint: Delete a Valuation Point.
[**finalise_candidate_valuation**](FundsApi.md#finalise_candidate_valuation) | **POST** /api/funds/{scope}/{code}/valuationpoints/$finalisecandidate | [EXPERIMENTAL] FinaliseCandidateValuation: Finalise Candidate.
[**get_fee**](FundsApi.md#get_fee) | **GET** /api/funds/{scope}/{code}/fees/{feeCode} | [EXPERIMENTAL] GetFee: Get a Fee for a specified Fund.
[**get_fund**](FundsApi.md#get_fund) | **GET** /api/funds/{scope}/{code} | [EXPERIMENTAL] GetFund: Get a Fund.
[**get_valuation_point_data**](FundsApi.md#get_valuation_point_data) | **POST** /api/funds/{scope}/{code}/valuationpoints | [EXPERIMENTAL] GetValuationPointData: Get Valuation Point Data for a Fund.
[**list_fees**](FundsApi.md#list_fees) | **GET** /api/funds/{scope}/{code}/fees | [EXPERIMENTAL] ListFees: List Fees for a specified Fund.
[**list_funds**](FundsApi.md#list_funds) | **GET** /api/funds | [EXPERIMENTAL] ListFunds: List Funds.
[**patch_fee**](FundsApi.md#patch_fee) | **PATCH** /api/funds/{scope}/{code}/fees/{feeCode} | [EXPERIMENTAL] PatchFee: Patch Fee.
[**set_share_class_instruments**](FundsApi.md#set_share_class_instruments) | **PUT** /api/funds/{scope}/{code}/shareclasses | [EXPERIMENTAL] SetShareClassInstruments: Set the ShareClass Instruments on a fund.
[**upsert_fund_properties**](FundsApi.md#upsert_fund_properties) | **POST** /api/funds/{scope}/{code}/properties/$upsert | [EXPERIMENTAL] UpsertFundProperties: Upsert Fund properties.
[**upsert_valuation_point**](FundsApi.md#upsert_valuation_point) | **POST** /api/funds/{scope}/{code}/valuationpoints/$upsert | [EXPERIMENTAL] UpsertValuationPoint: Upsert Valuation Point.


# **accept_estimate_point**
> ValuationPointDataResponse accept_estimate_point(scope, code, valuation_point_data_request)

[EXPERIMENTAL] AcceptEstimatePoint: Accepts an Estimate Valuation Point.

Accepts the specified estimate Valuation Point. Should the Valuation Point differ since the valuation Point was last run, status will be marked as 'Candidate', otherwise it will be marked as 'Final'

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.valuation_point_data_request import ValuationPointDataRequest
from lusid.models.valuation_point_data_response import ValuationPointDataResponse
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    FundsApi,
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
    api_instance = api_client_factory.build(lusid.FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund. Together with the scope this uniquely identifies the Fund.
    valuation_point_data_request = {"diaryEntryCode":"DiaryEntryCode"} # ValuationPointDataRequest | The valuationPointDataRequest which contains the Diary Entry code for the Estimate Valuation Point to move to Final state.

    try:
        # [EXPERIMENTAL] AcceptEstimatePoint: Accepts an Estimate Valuation Point.
        api_response = await api_instance.accept_estimate_point(scope, code, valuation_point_data_request)
        print("The response of FundsApi->accept_estimate_point:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FundsApi->accept_estimate_point: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | 
 **valuation_point_data_request** | [**ValuationPointDataRequest**](ValuationPointDataRequest.md)| The valuationPointDataRequest which contains the Diary Entry code for the Estimate Valuation Point to move to Final state. | 

### Return type

[**ValuationPointDataResponse**](ValuationPointDataResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Accepted Estimate point and status after being Accepted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_fee**
> Fee create_fee(scope, code, fee_code, fee_request)

[EXPERIMENTAL] CreateFee: Create a Fee.

Create the given Fee.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.fee import Fee
from lusid.models.fee_request import FeeRequest
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    FundsApi,
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
    api_instance = api_client_factory.build(lusid.FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund. Together with the scope this uniquely identifies the Fund.
    fee_code = 'fee_code_example' # str | The code of the Fee.
    fee_request = {"feeType":{"scope":"FeeTypeScope","code":"FeeTypeCode"},"name":"Legal Fees","description":"Legal Fees","origin":"Separate Agreement","accrualCurrency":"GBP","treatment":"Monthly","totalAnnualAccrualAmount":75000,"payableFrequency":"Annually","businessDayConvention":"Previous","startDate":"2020-10-25T00:00:00.0000000+00:00","endDate":"2023-10-25T00:00:00.0000000+00:00","anchorDate":{"day":1,"month":1},"properties":{}} # FeeRequest | The Fee to create.

    try:
        # [EXPERIMENTAL] CreateFee: Create a Fee.
        api_response = await api_instance.create_fee(scope, code, fee_code, fee_request)
        print("The response of FundsApi->create_fee:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FundsApi->create_fee: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | 
 **fee_code** | **str**| The code of the Fee. | 
 **fee_request** | [**FeeRequest**](FeeRequest.md)| The Fee to create. | 

### Return type

[**Fee**](Fee.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created Fee. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_fund**
> Fund create_fund(scope, fund_request)

[EXPERIMENTAL] CreateFund: Create a Fund.

Create the given Fund.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.fund import Fund
from lusid.models.fund_request import FundRequest
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    FundsApi,
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
    api_instance = api_client_factory.build(lusid.FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    fund_request = {"code":"FundCode","displayName":"Fund Name","description":"Standard Fund","aborId":{"scope":"AborScope","code":"AborCode"},"shareClassInstrumentScopes":["Scope1","Scope2"],"shareClassInstruments":[{"instrumentIdentifiers":{"Instrument/default/Figi":"GB0007980598"}}],"type":"Master","inceptionDate":"9999-12-31T23:59:59.9999999+00:00","decimalPlaces":6,"yearEndDate":{"day":1,"month":12},"properties":{"Fund/MyScope/FundManagerName":{"key":"Fund/MyScope/FundManagerName","value":{"labelValue":"Smith"},"effectiveFrom":"2020-03-05T00:00:00.0000000+00:00"}}} # FundRequest | The definition of the Fund.

    try:
        # [EXPERIMENTAL] CreateFund: Create a Fund.
        api_response = await api_instance.create_fund(scope, fund_request)
        print("The response of FundsApi->create_fund:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FundsApi->create_fund: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **fund_request** | [**FundRequest**](FundRequest.md)| The definition of the Fund. | 

### Return type

[**Fund**](Fund.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created Fund. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_fee**
> DeletedEntityResponse delete_fee(scope, code, fee_code)

[EXPERIMENTAL] DeleteFee: Delete a Fee.

Delete the given Fee.

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
    FundsApi,
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
    api_instance = api_client_factory.build(lusid.FundsApi)
    scope = 'scope_example' # str | The scope of the Fund
    code = 'code_example' # str | The code of the Fund. Together with the scope this uniquely identifies the Fund.
    fee_code = 'fee_code_example' # str | The code of the Fee to be deleted.

    try:
        # [EXPERIMENTAL] DeleteFee: Delete a Fee.
        api_response = await api_instance.delete_fee(scope, code, fee_code)
        print("The response of FundsApi->delete_fee:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FundsApi->delete_fee: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund | 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | 
 **fee_code** | **str**| The code of the Fee to be deleted. | 

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
**200** | The datetime that the Fee was deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_fund**
> DeletedEntityResponse delete_fund(scope, code)

[EXPERIMENTAL] DeleteFund: Delete a Fund.

Delete the given Fund.

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
    FundsApi,
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
    api_instance = api_client_factory.build(lusid.FundsApi)
    scope = 'scope_example' # str | The scope of the Fund to be deleted.
    code = 'code_example' # str | The code of the Fund to be deleted. Together with the scope this uniquely identifies the Fund.

    try:
        # [EXPERIMENTAL] DeleteFund: Delete a Fund.
        api_response = await api_instance.delete_fund(scope, code)
        print("The response of FundsApi->delete_fund:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FundsApi->delete_fund: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund to be deleted. | 
 **code** | **str**| The code of the Fund to be deleted. Together with the scope this uniquely identifies the Fund. | 

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
**200** | The datetime that the Fund was deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_valuation_point**
> DeletedEntityResponse delete_valuation_point(scope, code, diary_entry_code)

[EXPERIMENTAL] DeleteValuationPoint: Delete a Valuation Point.

Deletes the given Valuation Point.

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
    FundsApi,
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
    api_instance = api_client_factory.build(lusid.FundsApi)
    scope = 'scope_example' # str | The scope of the Fund for the valuation point to be deleted.
    code = 'code_example' # str | The code of the Fund containing the Valuation Point to be deleted. Together with the scope this uniquely identifies the Fund.
    diary_entry_code = 'diary_entry_code_example' # str | The diary entry code for the valuation Point to be deleted.

    try:
        # [EXPERIMENTAL] DeleteValuationPoint: Delete a Valuation Point.
        api_response = await api_instance.delete_valuation_point(scope, code, diary_entry_code)
        print("The response of FundsApi->delete_valuation_point:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FundsApi->delete_valuation_point: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund for the valuation point to be deleted. | 
 **code** | **str**| The code of the Fund containing the Valuation Point to be deleted. Together with the scope this uniquely identifies the Fund. | 
 **diary_entry_code** | **str**| The diary entry code for the valuation Point to be deleted. | 

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
**200** | The datetime that the Valuation Point was deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **finalise_candidate_valuation**
> ValuationPointDataResponse finalise_candidate_valuation(scope, code, valuation_point_data_request)

[EXPERIMENTAL] FinaliseCandidateValuation: Finalise Candidate.

Moves a 'Candidate' status Valuation Point to status 'Final'.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.valuation_point_data_request import ValuationPointDataRequest
from lusid.models.valuation_point_data_response import ValuationPointDataResponse
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    FundsApi,
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
    api_instance = api_client_factory.build(lusid.FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund. Together with the scope this uniquely identifies the Fund.
    valuation_point_data_request = {"diaryEntryCode":"DiaryEntryCode"} # ValuationPointDataRequest | The valuationPointDataRequest which contains the diary entry code to mark as final.

    try:
        # [EXPERIMENTAL] FinaliseCandidateValuation: Finalise Candidate.
        api_response = await api_instance.finalise_candidate_valuation(scope, code, valuation_point_data_request)
        print("The response of FundsApi->finalise_candidate_valuation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FundsApi->finalise_candidate_valuation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | 
 **valuation_point_data_request** | [**ValuationPointDataRequest**](ValuationPointDataRequest.md)| The valuationPointDataRequest which contains the diary entry code to mark as final. | 

### Return type

[**ValuationPointDataResponse**](ValuationPointDataResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated Valuation Point response as a result of it be marked as Final. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fee**
> Fee get_fee(scope, code, fee_code, effective_at=effective_at, as_at=as_at, property_keys=property_keys)

[EXPERIMENTAL] GetFee: Get a Fee for a specified Fund.

Retrieve a fee for a specified Fund

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.fee import Fee
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    FundsApi,
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
    api_instance = api_client_factory.build(lusid.FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund. Together with the scope this uniquely identifies the Fund.
    fee_code = 'fee_code_example' # str | The code of the Fee.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve the Fee properties. Defaults to the current LUSID system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Fee. Defaults to returning the latest version of the Fee if not specified. (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the 'Fee' domain to decorate onto the Fee.              These must take the format {domain}/{scope}/{code}, for example 'Fee/Account/Id'. If no properties are specified, then no properties will be returned. (optional)

    try:
        # [EXPERIMENTAL] GetFee: Get a Fee for a specified Fund.
        api_response = await api_instance.get_fee(scope, code, fee_code, effective_at=effective_at, as_at=as_at, property_keys=property_keys)
        print("The response of FundsApi->get_fee:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FundsApi->get_fee: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | 
 **fee_code** | **str**| The code of the Fee. | 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the Fee properties. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Fee. Defaults to returning the latest version of the Fee if not specified. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;Fee&#39; domain to decorate onto the Fee.              These must take the format {domain}/{scope}/{code}, for example &#39;Fee/Account/Id&#39;. If no properties are specified, then no properties will be returned. | [optional] 

### Return type

[**Fee**](Fee.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Fee definition. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fund**
> Fund get_fund(scope, code, effective_at=effective_at, as_at=as_at, property_keys=property_keys)

[EXPERIMENTAL] GetFund: Get a Fund.

Retrieve the definition of a particular Fund.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.fund import Fund
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    FundsApi,
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
    api_instance = api_client_factory.build(lusid.FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund. Together with the scope this uniquely identifies the Fund.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve the Fund properties. Defaults to the current LUSID system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Fund definition. Defaults to returning the latest version of the Fund definition if not specified. (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the 'Fund' domain to decorate onto the Fund.              These must take the format {domain}/{scope}/{code}, for example 'Fund/Manager/Id'. If no properties are specified, then no properties will be returned. (optional)

    try:
        # [EXPERIMENTAL] GetFund: Get a Fund.
        api_response = await api_instance.get_fund(scope, code, effective_at=effective_at, as_at=as_at, property_keys=property_keys)
        print("The response of FundsApi->get_fund:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FundsApi->get_fund: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the Fund properties. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Fund definition. Defaults to returning the latest version of the Fund definition if not specified. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;Fund&#39; domain to decorate onto the Fund.              These must take the format {domain}/{scope}/{code}, for example &#39;Fund/Manager/Id&#39;. If no properties are specified, then no properties will be returned. | [optional] 

### Return type

[**Fund**](Fund.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Fund definition. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_valuation_point_data**
> ValuationPointDataResponse get_valuation_point_data(scope, code, valuation_point_data_query_parameters, as_at=as_at)

[EXPERIMENTAL] GetValuationPointData: Get Valuation Point Data for a Fund.

Retrieves the Valuation Point data for a date or specified Diary Entry Id.  The endpoint will internally extract all 'Assets' and 'Liabilities' from the related ABOR's Trial balance to produce a GAV.  Start date will be assumed from the last 'official' DiaryEntry and EndDate will be as provided.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.valuation_point_data_query_parameters import ValuationPointDataQueryParameters
from lusid.models.valuation_point_data_response import ValuationPointDataResponse
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    FundsApi,
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
    api_instance = api_client_factory.build(lusid.FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund. Together with the scope this uniquely identifies the Fund.
    valuation_point_data_query_parameters = {"end":{"diaryEntry":"DiaryEntryCode"}} # ValuationPointDataQueryParameters | The arguments to use for querying the Valuation Point data
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Fund definition. Defaults to returning the latest version of the Fund definition if not specified. (optional)

    try:
        # [EXPERIMENTAL] GetValuationPointData: Get Valuation Point Data for a Fund.
        api_response = await api_instance.get_valuation_point_data(scope, code, valuation_point_data_query_parameters, as_at=as_at)
        print("The response of FundsApi->get_valuation_point_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FundsApi->get_valuation_point_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | 
 **valuation_point_data_query_parameters** | [**ValuationPointDataQueryParameters**](ValuationPointDataQueryParameters.md)| The arguments to use for querying the Valuation Point data | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Fund definition. Defaults to returning the latest version of the Fund definition if not specified. | [optional] 

### Return type

[**ValuationPointDataResponse**](ValuationPointDataResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The specified Valuation Point for the Fund. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_fees**
> PagedResourceListOfFee list_fees(scope, code, effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)

[EXPERIMENTAL] ListFees: List Fees for a specified Fund.

List all the Fees matching a particular criteria.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.paged_resource_list_of_fee import PagedResourceListOfFee
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    FundsApi,
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
    api_instance = api_client_factory.build(lusid.FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to list the TimeVariant properties for the Fees. Defaults to the current LUSID              system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the Fees. Defaults to returning the latest version of each Fee if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing fees; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. (optional)
    limit = 56 # int | When paginating, limit the results to this number. Defaults to 100 if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the results.              For example, to filter on the treatment, specify \"treatment eq 'Monthly'\". For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. (optional)
    sort_by = ['sort_by_example'] # List[str] | A list of field names or properties to sort by, each suffixed by \" ASC\" or \" DESC\" (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the 'Fee' domain to decorate onto each Fee.              These must take the format {domain}/{scope}/{code}, for example 'Fee/Account/Id'. (optional)

    try:
        # [EXPERIMENTAL] ListFees: List Fees for a specified Fund.
        api_response = await api_instance.list_fees(scope, code, effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)
        print("The response of FundsApi->list_fees:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FundsApi->list_fees: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. | 
 **effective_at** | **str**| The effective datetime or cut label at which to list the TimeVariant properties for the Fees. Defaults to the current LUSID              system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the Fees. Defaults to returning the latest version of each Fee if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing fees; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results.              For example, to filter on the treatment, specify \&quot;treatment eq &#39;Monthly&#39;\&quot;. For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot; | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;Fee&#39; domain to decorate onto each Fee.              These must take the format {domain}/{scope}/{code}, for example &#39;Fee/Account/Id&#39;. | [optional] 

### Return type

[**PagedResourceListOfFee**](PagedResourceListOfFee.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Fees. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_funds**
> PagedResourceListOfFund list_funds(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)

[EXPERIMENTAL] ListFunds: List Funds.

List all the Funds matching particular criteria.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.paged_resource_list_of_fund import PagedResourceListOfFund
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    FundsApi,
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
    api_instance = api_client_factory.build(lusid.FundsApi)
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to list the TimeVariant properties for the Funds. Defaults to the current LUSID              system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the Funds. Defaults to returning the latest version of each Fund if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing Funds; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. (optional)
    limit = 56 # int | When paginating, limit the results to this number. Defaults to 100 if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the results.              For example, to filter on the Fund type, specify \"id.Code eq 'Fund1'\". For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. (optional)
    sort_by = ['sort_by_example'] # List[str] | A list of field names or properties to sort by, each suffixed by \" ASC\" or \" DESC\" (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the 'Fund' domain to decorate onto each Fund.              These must take the format {domain}/{scope}/{code}, for example 'Fund/Manager/Id'. (optional)

    try:
        # [EXPERIMENTAL] ListFunds: List Funds.
        api_response = await api_instance.list_funds(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)
        print("The response of FundsApi->list_funds:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FundsApi->list_funds: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **effective_at** | **str**| The effective datetime or cut label at which to list the TimeVariant properties for the Funds. Defaults to the current LUSID              system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the Funds. Defaults to returning the latest version of each Fund if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing Funds; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results.              For example, to filter on the Fund type, specify \&quot;id.Code eq &#39;Fund1&#39;\&quot;. For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot; | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;Fund&#39; domain to decorate onto each Fund.              These must take the format {domain}/{scope}/{code}, for example &#39;Fund/Manager/Id&#39;. | [optional] 

### Return type

[**PagedResourceListOfFund**](PagedResourceListOfFund.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Funds. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_fee**
> Fee patch_fee(scope, code, fee_code, operation)

[EXPERIMENTAL] PatchFee: Patch Fee.

Create or update certain fields for a particular Fee.  The behaviour is defined by the JSON Patch specification.                Currently supported fields are: EndDate.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.fee import Fee
from lusid.models.operation import Operation
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    FundsApi,
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
    api_instance = api_client_factory.build(lusid.FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund. Together with the scope this uniquely identifies the Fund.
    fee_code = 'fee_code_example' # str | The code of the Fee.
    operation = [{"value":"2027-12-31T00:00:00.0000000+00:00","path":"/endDate","op":"add"}] # List[Operation] | The json patch document. For more information see: https://datatracker.ietf.org/doc/html/rfc6902.

    try:
        # [EXPERIMENTAL] PatchFee: Patch Fee.
        api_response = await api_instance.patch_fee(scope, code, fee_code, operation)
        print("The response of FundsApi->patch_fee:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FundsApi->patch_fee: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | 
 **fee_code** | **str**| The code of the Fee. | 
 **operation** | [**List[Operation]**](Operation.md)| The json patch document. For more information see: https://datatracker.ietf.org/doc/html/rfc6902. | 

### Return type

[**Fee**](Fee.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The newly patched Fee. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_share_class_instruments**
> Fund set_share_class_instruments(scope, code, set_share_class_instruments_request)

[EXPERIMENTAL] SetShareClassInstruments: Set the ShareClass Instruments on a fund.

Update the ShareClass Instruments on an existing fund with the set of instruments provided.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.fund import Fund
from lusid.models.set_share_class_instruments_request import SetShareClassInstrumentsRequest
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    FundsApi,
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
    api_instance = api_client_factory.build(lusid.FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund.
    set_share_class_instruments_request = {"shareClassInstrumentScopes":["UKInstrumentScope"],"shareClassInstruments":[{"instrumentIdentifiers":{"Instrument/default/ClientInternal":"UK_12345"}}]} # SetShareClassInstrumentsRequest | The scopes and instrument identifiers for the instruments to be set.

    try:
        # [EXPERIMENTAL] SetShareClassInstruments: Set the ShareClass Instruments on a fund.
        api_response = await api_instance.set_share_class_instruments(scope, code, set_share_class_instruments_request)
        print("The response of FundsApi->set_share_class_instruments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FundsApi->set_share_class_instruments: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. | 
 **set_share_class_instruments_request** | [**SetShareClassInstrumentsRequest**](SetShareClassInstrumentsRequest.md)| The scopes and instrument identifiers for the instruments to be set. | 

### Return type

[**Fund**](Fund.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The updated fund. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_fund_properties**
> FundProperties upsert_fund_properties(scope, code, request_body=request_body)

[EXPERIMENTAL] UpsertFundProperties: Upsert Fund properties.

Update or insert one or more properties onto a single Fund. A property will be updated if it  already exists and inserted if it does not. All properties must be of the domain 'Fund'.                Upserting a property that exists for an Fund, with a null value, will delete the instance of the property for that group.                Properties have an <i>effectiveFrom</i> datetime for which the property is valid, and an <i>effectiveUntil</i>  datetime until which the property is valid. Not supplying an <i>effectiveUntil</i> datetime results in the property being  valid indefinitely, or until the next <i>effectiveFrom</i> datetime of the property.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.fund_properties import FundProperties
from lusid.models.model_property import ModelProperty
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    FundsApi,
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
    api_instance = api_client_factory.build(lusid.FundsApi)
    scope = 'scope_example' # str | The scope of the Fund to update or insert the properties onto.
    code = 'code_example' # str | The code of the Fund to update or insert the properties onto. Together with the scope this uniquely identifies the Fund.
    request_body = {"Fund/MyScope/FundManagerName":{"key":"Fund/MyScope/FundManagerName","value":{"labelValue":"Smith"},"effectiveFrom":"2018-03-05T00:00:00.0000000+00:00"},"Fund/MyScope/SomeProperty":{"key":"Fund/MyScope/SomeProperty","value":{"labelValue":"SomeValue"},"effectiveFrom":"2016-01-01T00:00:00.0000000+00:00"},"Fund/MyScope/AnotherProperty":{"key":"Fund/MyScope/AnotherProperty","value":{"labelValue":"AnotherValue"},"effectiveFrom":"2018-03-05T00:00:00.0000000+00:00","effectiveUntil":"2020-01-01T00:00:00.0000000+00:00"},"Fund/MyScope/ReBalanceInterval":{"key":"Fund/MyScope/ReBalanceInterval","value":{"metricValue":{"value":30,"unit":"Days"}}}} # Dict[str, ModelProperty] | The properties to be updated or inserted onto the Fund. Each property in               the request must be keyed by its unique property key. This has the format {domain}/{scope}/{code} e.g. \"Fund/Manager/Id\". (optional)

    try:
        # [EXPERIMENTAL] UpsertFundProperties: Upsert Fund properties.
        api_response = await api_instance.upsert_fund_properties(scope, code, request_body=request_body)
        print("The response of FundsApi->upsert_fund_properties:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FundsApi->upsert_fund_properties: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund to update or insert the properties onto. | 
 **code** | **str**| The code of the Fund to update or insert the properties onto. Together with the scope this uniquely identifies the Fund. | 
 **request_body** | [**Dict[str, ModelProperty]**](ModelProperty.md)| The properties to be updated or inserted onto the Fund. Each property in               the request must be keyed by its unique property key. This has the format {domain}/{scope}/{code} e.g. \&quot;Fund/Manager/Id\&quot;. | [optional] 

### Return type

[**FundProperties**](FundProperties.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated or inserted properties |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_valuation_point**
> DiaryEntry upsert_valuation_point(scope, code, upsert_valuation_point_request)

[EXPERIMENTAL] UpsertValuationPoint: Upsert Valuation Point.

Update or insert the estimate Valuation Point.                If the Valuation Point does not exist, this method will create it in estimate state.                If the Valuation Point already exists and is in estimate state, the Valuation Point will be updated with the newly specified information in this request.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.diary_entry import DiaryEntry
from lusid.models.upsert_valuation_point_request import UpsertValuationPointRequest
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    FundsApi,
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
    api_instance = api_client_factory.build(lusid.FundsApi)
    scope = 'scope_example' # str | The scope of the Fund.
    code = 'code_example' # str | The code of the Fund. Together with the scope this uniquely identifies the Fund.
    upsert_valuation_point_request = {"diaryEntryCode":"ValuationJan2024","name":"ValuationJan2024","effectiveAt":"2024-01-31T23:59:59.0000000+00:00","queryAsAt":"2024-01-31T23:59:59.0000000+00:00","properties":{}} # UpsertValuationPointRequest | The Valuation Point Estimate definition to Upsert

    try:
        # [EXPERIMENTAL] UpsertValuationPoint: Upsert Valuation Point.
        api_response = await api_instance.upsert_valuation_point(scope, code, upsert_valuation_point_request)
        print("The response of FundsApi->upsert_valuation_point:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FundsApi->upsert_valuation_point: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | 
 **upsert_valuation_point_request** | [**UpsertValuationPointRequest**](UpsertValuationPointRequest.md)| The Valuation Point Estimate definition to Upsert | 

### Return type

[**DiaryEntry**](DiaryEntry.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated or inserted estimated Valuation Point |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

