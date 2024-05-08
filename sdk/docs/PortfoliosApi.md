# lusid.PortfoliosApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_instrument_event_instruction**](PortfoliosApi.md#delete_instrument_event_instruction) | **DELETE** /api/portfolios/{scope}/{code}/instrumenteventinstructions/{instrumentEventInstructionId} | [EARLY ACCESS] DeleteInstrumentEventInstruction: Delete Instrument Event Instruction
[**delete_key_from_portfolio_access_metadata**](PortfoliosApi.md#delete_key_from_portfolio_access_metadata) | **DELETE** /api/portfolios/{scope}/{code}/metadata/{metadataKey} | [EARLY ACCESS] DeleteKeyFromPortfolioAccessMetadata: Delete a Portfolio Access Metadata Rule
[**delete_portfolio**](PortfoliosApi.md#delete_portfolio) | **DELETE** /api/portfolios/{scope}/{code} | DeletePortfolio: Delete portfolio
[**delete_portfolio_properties**](PortfoliosApi.md#delete_portfolio_properties) | **DELETE** /api/portfolios/{scope}/{code}/properties | DeletePortfolioProperties: Delete portfolio properties
[**delete_portfolio_returns**](PortfoliosApi.md#delete_portfolio_returns) | **DELETE** /api/portfolios/{scope}/{code}/returns/{returnScope}/{returnCode}/$delete | [EARLY ACCESS] DeletePortfolioReturns: Delete Returns
[**get_aggregated_returns_dispersion_metrics**](PortfoliosApi.md#get_aggregated_returns_dispersion_metrics) | **POST** /api/portfolios/{scope}/{code}/returns/dispersion/$aggregated | [EARLY ACCESS] GetAggregatedReturnsDispersionMetrics: Get the Aggregated Returns Dispersion metric
[**get_composite_breakdown**](PortfoliosApi.md#get_composite_breakdown) | **POST** /api/portfolios/{scope}/{code}/returns/breakdown | [EARLY ACCESS] GetCompositeBreakdown: Get the Composite Breakdown on how the composite Returns are calculated
[**get_instrument_event_instruction**](PortfoliosApi.md#get_instrument_event_instruction) | **GET** /api/portfolios/{scope}/{code}/instrumenteventinstructions/{instrumentEventInstructionId} | [EARLY ACCESS] GetInstrumentEventInstruction: Get Instrument Event Instruction
[**get_portfolio**](PortfoliosApi.md#get_portfolio) | **GET** /api/portfolios/{scope}/{code} | GetPortfolio: Get portfolio
[**get_portfolio_aggregate_returns**](PortfoliosApi.md#get_portfolio_aggregate_returns) | **GET** /api/portfolios/{scope}/{code}/returns/{returnScope}/{returnCode}/aggregated | [DEPRECATED] GetPortfolioAggregateReturns: Aggregate Returns (This is a deprecated endpoint).
[**get_portfolio_aggregated_returns**](PortfoliosApi.md#get_portfolio_aggregated_returns) | **POST** /api/portfolios/{scope}/{code}/returns/$aggregated | [EARLY ACCESS] GetPortfolioAggregatedReturns: Aggregated Returns
[**get_portfolio_commands**](PortfoliosApi.md#get_portfolio_commands) | **GET** /api/portfolios/{scope}/{code}/commands | GetPortfolioCommands: Get portfolio commands
[**get_portfolio_metadata**](PortfoliosApi.md#get_portfolio_metadata) | **GET** /api/portfolios/{scope}/{code}/metadata | [EARLY ACCESS] GetPortfolioMetadata: Get access metadata rules for a portfolio
[**get_portfolio_properties**](PortfoliosApi.md#get_portfolio_properties) | **GET** /api/portfolios/{scope}/{code}/properties | GetPortfolioProperties: Get portfolio properties
[**get_portfolio_property_time_series**](PortfoliosApi.md#get_portfolio_property_time_series) | **GET** /api/portfolios/{scope}/{code}/properties/time-series | [EARLY ACCESS] GetPortfolioPropertyTimeSeries: Get portfolio property time series
[**get_portfolio_relations**](PortfoliosApi.md#get_portfolio_relations) | **GET** /api/portfolios/{scope}/{code}/relations | [EXPERIMENTAL] GetPortfolioRelations: Get portfolio relations
[**get_portfolio_relationships**](PortfoliosApi.md#get_portfolio_relationships) | **GET** /api/portfolios/{scope}/{code}/relationships | [EARLY ACCESS] GetPortfolioRelationships: Get portfolio relationships
[**get_portfolio_returns**](PortfoliosApi.md#get_portfolio_returns) | **GET** /api/portfolios/{scope}/{code}/returns/{returnScope}/{returnCode} | [EARLY ACCESS] GetPortfolioReturns: Get Returns
[**get_portfolios_access_metadata_by_key**](PortfoliosApi.md#get_portfolios_access_metadata_by_key) | **GET** /api/portfolios/{scope}/{code}/metadata/{metadataKey} | [EARLY ACCESS] GetPortfoliosAccessMetadataByKey: Get an entry identified by a metadataKey in the access metadata object
[**list_portfolio_properties**](PortfoliosApi.md#list_portfolio_properties) | **GET** /api/portfolios/{scope}/{code}/properties/list | [EARLY ACCESS] ListPortfolioProperties: Get portfolio properties
[**list_portfolios**](PortfoliosApi.md#list_portfolios) | **GET** /api/portfolios | ListPortfolios: List portfolios
[**list_portfolios_for_scope**](PortfoliosApi.md#list_portfolios_for_scope) | **GET** /api/portfolios/{scope} | ListPortfoliosForScope: List portfolios for scope
[**patch_portfolio**](PortfoliosApi.md#patch_portfolio) | **PATCH** /api/portfolios/{scope}/{code} | [EARLY ACCESS] PatchPortfolio: Patch portfolio.
[**patch_portfolio_access_metadata**](PortfoliosApi.md#patch_portfolio_access_metadata) | **PATCH** /api/portfolios/{scope}/{code}/metadata | [EARLY ACCESS] PatchPortfolioAccessMetadata: Patch Access Metadata rules for a Portfolio.
[**update_portfolio**](PortfoliosApi.md#update_portfolio) | **PUT** /api/portfolios/{scope}/{code} | UpdatePortfolio: Update portfolio
[**upsert_instrument_event_instructions**](PortfoliosApi.md#upsert_instrument_event_instructions) | **POST** /api/portfolios/{scope}/{code}/instrumenteventinstructions | [EARLY ACCESS] UpsertInstrumentEventInstructions: Upsert Instrument Event Instructions
[**upsert_portfolio_access_metadata**](PortfoliosApi.md#upsert_portfolio_access_metadata) | **PUT** /api/portfolios/{scope}/{code}/metadata/{metadataKey} | [EARLY ACCESS] UpsertPortfolioAccessMetadata: Upsert a Portfolio Access Metadata Rule associated with specific metadataKey. This creates or updates the data in LUSID.
[**upsert_portfolio_properties**](PortfoliosApi.md#upsert_portfolio_properties) | **POST** /api/portfolios/{scope}/{code}/properties | UpsertPortfolioProperties: Upsert portfolio properties
[**upsert_portfolio_returns**](PortfoliosApi.md#upsert_portfolio_returns) | **POST** /api/portfolios/{scope}/{code}/returns/{returnScope}/{returnCode} | [EARLY ACCESS] UpsertPortfolioReturns: Upsert Returns


# **delete_instrument_event_instruction**
> DeletedEntityResponse delete_instrument_event_instruction(scope, code, instrument_event_instruction_id, portfolio_effective_at=portfolio_effective_at)

[EARLY ACCESS] DeleteInstrumentEventInstruction: Delete Instrument Event Instruction

Delete a particular instruction for a particular portfolio

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
    PortfoliosApi,
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
    api_instance = api_client_factory.build(lusid.PortfoliosApi)
    scope = 'scope_example' # str | The scope of the portfolio.
    code = 'code_example' # str | The code of the portfolio. Together with the scope this uniquely identifies the portfolio.
    instrument_event_instruction_id = 'instrument_event_instruction_id_example' # str | The id of the instruction to be deleted.
    portfolio_effective_at = 'portfolio_effective_at_example' # str | The effective date at which the portfolio will be resolved. Defaults to current time if not specified. (optional)

    try:
        # [EARLY ACCESS] DeleteInstrumentEventInstruction: Delete Instrument Event Instruction
        api_response = await api_instance.delete_instrument_event_instruction(scope, code, instrument_event_instruction_id, portfolio_effective_at=portfolio_effective_at)
        print("The response of PortfoliosApi->delete_instrument_event_instruction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfoliosApi->delete_instrument_event_instruction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio. | 
 **code** | **str**| The code of the portfolio. Together with the scope this uniquely identifies the portfolio. | 
 **instrument_event_instruction_id** | **str**| The id of the instruction to be deleted. | 
 **portfolio_effective_at** | **str**| The effective date at which the portfolio will be resolved. Defaults to current time if not specified. | [optional] 

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
**200** | The datetime that the instruction was deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_key_from_portfolio_access_metadata**
> DeletedEntityResponse delete_key_from_portfolio_access_metadata(scope, code, metadata_key, effective_at=effective_at, effective_until=effective_until)

[EARLY ACCESS] DeleteKeyFromPortfolioAccessMetadata: Delete a Portfolio Access Metadata Rule

Delete the Portfolio Access Metadata Rule that exactly matches the provided identifier parts

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
    PortfoliosApi,
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
    api_instance = api_client_factory.build(lusid.PortfoliosApi)
    scope = 'scope_example' # str | The scope of the Quote Access Metadata Rule to retrieve.
    code = 'code_example' # str | Portfolio code
    metadata_key = 'metadata_key_example' # str | The metadataKey identifying the access metadata entry to delete
    effective_at = 'effective_at_example' # str | The effective date to delete at, if this is not supplied, it will delete all data found (optional)
    effective_until = '2013-10-20T19:20:30+01:00' # datetime | The effective date until which the delete is valid. If not supplied this will be valid indefinitely, or until the next 'effectiveAt' date of the Access Metadata (optional)

    try:
        # [EARLY ACCESS] DeleteKeyFromPortfolioAccessMetadata: Delete a Portfolio Access Metadata Rule
        api_response = await api_instance.delete_key_from_portfolio_access_metadata(scope, code, metadata_key, effective_at=effective_at, effective_until=effective_until)
        print("The response of PortfoliosApi->delete_key_from_portfolio_access_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfoliosApi->delete_key_from_portfolio_access_metadata: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Quote Access Metadata Rule to retrieve. | 
 **code** | **str**| Portfolio code | 
 **metadata_key** | **str**| The metadataKey identifying the access metadata entry to delete | 
 **effective_at** | **str**| The effective date to delete at, if this is not supplied, it will delete all data found | [optional] 
 **effective_until** | **datetime**| The effective date until which the delete is valid. If not supplied this will be valid indefinitely, or until the next &#39;effectiveAt&#39; date of the Access Metadata | [optional] 

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
**200** | The rule that has been deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_portfolio**
> DeletedEntityResponse delete_portfolio(scope, code)

DeletePortfolio: Delete portfolio

Delete a particular portfolio.                The deletion will take effect from the portfolio's creation datetime. This means that the portfolio will no longer exist at any effective datetime, as per the asAt datetime of deletion.

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
    PortfoliosApi,
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
    api_instance = api_client_factory.build(lusid.PortfoliosApi)
    scope = 'scope_example' # str | The scope of the portfolio.
    code = 'code_example' # str | The code of the portfolio. Together with the scope this uniquely identifies the portfolio.

    try:
        # DeletePortfolio: Delete portfolio
        api_response = await api_instance.delete_portfolio(scope, code)
        print("The response of PortfoliosApi->delete_portfolio:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfoliosApi->delete_portfolio: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio. | 
 **code** | **str**| The code of the portfolio. Together with the scope this uniquely identifies the portfolio. | 

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
**200** | The datetime that the portfolio was deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_portfolio_properties**
> DeletedEntityResponse delete_portfolio_properties(scope, code, property_keys, effective_at=effective_at)

DeletePortfolioProperties: Delete portfolio properties

Delete one or more properties from a particular portfolio. If the properties are time-variant then an effective datetime from which  to delete properties must be specified. If the properties are perpetual then it is invalid to specify an effective datetime for deletion.

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
    PortfoliosApi,
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
    api_instance = api_client_factory.build(lusid.PortfoliosApi)
    scope = 'scope_example' # str | The scope of the portfolio.
    code = 'code_example' # str | The code of the portfolio. Together with the scope this uniquely identifies the portfolio.
    property_keys = ['property_keys_example'] # List[str] | The property keys of the properties to delete. These must take the format              {domain}/{scope}/{code}, for example 'Portfolio/Manager/Id'. Each property must be from the 'Portfolio' domain.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to delete time-variant properties from.              The property must exist at the specified 'effectiveAt' datetime. If the 'effectiveAt' is not provided or is              before the time-variant property exists then a failure is returned. Do not specify this parameter if any of              the properties to delete are perpetual. (optional)

    try:
        # DeletePortfolioProperties: Delete portfolio properties
        api_response = await api_instance.delete_portfolio_properties(scope, code, property_keys, effective_at=effective_at)
        print("The response of PortfoliosApi->delete_portfolio_properties:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfoliosApi->delete_portfolio_properties: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio. | 
 **code** | **str**| The code of the portfolio. Together with the scope this uniquely identifies the portfolio. | 
 **property_keys** | [**List[str]**](str.md)| The property keys of the properties to delete. These must take the format              {domain}/{scope}/{code}, for example &#39;Portfolio/Manager/Id&#39;. Each property must be from the &#39;Portfolio&#39; domain. | 
 **effective_at** | **str**| The effective datetime or cut label at which to delete time-variant properties from.              The property must exist at the specified &#39;effectiveAt&#39; datetime. If the &#39;effectiveAt&#39; is not provided or is              before the time-variant property exists then a failure is returned. Do not specify this parameter if any of              the properties to delete are perpetual. | [optional] 

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
**200** | The datetime that the properties were deleted from the specified portfolio |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_portfolio_returns**
> DeletedEntityResponse delete_portfolio_returns(scope, code, return_scope, return_code, from_effective_at, to_effective_at, period=period)

[EARLY ACCESS] DeletePortfolioReturns: Delete Returns

Cancel one or more Returns which exist into the specified portfolio.

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
    PortfoliosApi,
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
    api_instance = api_client_factory.build(lusid.PortfoliosApi)
    scope = 'scope_example' # str | The scope of the Portfolio.
    code = 'code_example' # str | The code of the  Portfolio.
    return_scope = 'return_scope_example' # str | The scope of the Returns.
    return_code = 'return_code_example' # str | The code of the Returns.
    from_effective_at = 'from_effective_at_example' # str | The start date from which to delete the Returns.
    to_effective_at = 'to_effective_at_example' # str | The end date from which to delete the Returns.
    period = 'period_example' # str | The Period (Daily or Monthly) of the Returns to be deleted. Defaults to Daily. (optional)

    try:
        # [EARLY ACCESS] DeletePortfolioReturns: Delete Returns
        api_response = await api_instance.delete_portfolio_returns(scope, code, return_scope, return_code, from_effective_at, to_effective_at, period=period)
        print("The response of PortfoliosApi->delete_portfolio_returns:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfoliosApi->delete_portfolio_returns: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Portfolio. | 
 **code** | **str**| The code of the  Portfolio. | 
 **return_scope** | **str**| The scope of the Returns. | 
 **return_code** | **str**| The code of the Returns. | 
 **from_effective_at** | **str**| The start date from which to delete the Returns. | 
 **to_effective_at** | **str**| The end date from which to delete the Returns. | 
 **period** | **str**| The Period (Daily or Monthly) of the Returns to be deleted. Defaults to Daily. | [optional] 

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
**200** | The successfully deleted Returns data along with any failures |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_aggregated_returns_dispersion_metrics**
> CompositeDispersionResponse get_aggregated_returns_dispersion_metrics(scope, code, aggregated_returns_dispersion_request, as_at=as_at)

[EARLY ACCESS] GetAggregatedReturnsDispersionMetrics: Get the Aggregated Returns Dispersion metric

Calculate the dispersion metric with the Aggregate Returns which are on the specified portfolio.             This works only for composites which have at least 6 constituents for a full year in.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.aggregated_returns_dispersion_request import AggregatedReturnsDispersionRequest
from lusid.models.composite_dispersion_response import CompositeDispersionResponse
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    PortfoliosApi,
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
    api_instance = api_client_factory.build(lusid.PortfoliosApi)
    scope = 'scope_example' # str | The scope of the Portfolio.
    code = 'code_example' # str | The code of the  Portfolio.
    aggregated_returns_dispersion_request = {"toEffectiveAt":"2023-01-01","yearsCount":10,"returnIds":[{"scope":"TestScope","code":"default"}],"recipeId":{"scope":"ReturnsScope","code":"ReturnCode"},"compositeMethod":"Asset","alternativeInceptionDate":"2020-01-01"} # AggregatedReturnsDispersionRequest | The request used in the AggregatedReturnsDispersionMetric.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Returns. Defaults to the latest. (optional)

    try:
        # [EARLY ACCESS] GetAggregatedReturnsDispersionMetrics: Get the Aggregated Returns Dispersion metric
        api_response = await api_instance.get_aggregated_returns_dispersion_metrics(scope, code, aggregated_returns_dispersion_request, as_at=as_at)
        print("The response of PortfoliosApi->get_aggregated_returns_dispersion_metrics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfoliosApi->get_aggregated_returns_dispersion_metrics: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Portfolio. | 
 **code** | **str**| The code of the  Portfolio. | 
 **aggregated_returns_dispersion_request** | [**AggregatedReturnsDispersionRequest**](AggregatedReturnsDispersionRequest.md)| The request used in the AggregatedReturnsDispersionMetric. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Returns. Defaults to the latest. | [optional] 

### Return type

[**CompositeDispersionResponse**](CompositeDispersionResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The aggregated returns grouped by return stream. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_composite_breakdown**
> CompositeBreakdownResponse get_composite_breakdown(scope, code, composite_breakdown_request, from_effective_at=from_effective_at, to_effective_at=to_effective_at, as_at=as_at)

[EARLY ACCESS] GetCompositeBreakdown: Get the Composite Breakdown on how the composite Returns are calculated

Calculate the Composite Returns and return this with the constituents which are included in this calculation

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.composite_breakdown_request import CompositeBreakdownRequest
from lusid.models.composite_breakdown_response import CompositeBreakdownResponse
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    PortfoliosApi,
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
    api_instance = api_client_factory.build(lusid.PortfoliosApi)
    scope = 'scope_example' # str | The scope of the Portfolio.
    code = 'code_example' # str | The code of the  Portfolio.
    composite_breakdown_request = {"returnIds":[{"scope":"TestScope","code":"default"}],"recipeId":{"scope":"ReturnsScope","code":"ReturnCode"},"compositeMethod":"Asset","period":"Monthly","holidayCalendars":[]} # CompositeBreakdownRequest | The request used in the GetCompositeBreakdown.
    from_effective_at = 'from_effective_at_example' # str | The start date from which to calculate the Returns. (optional)
    to_effective_at = 'to_effective_at_example' # str | The end date for which to calculate the Returns. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Returns. Defaults to the latest. (optional)

    try:
        # [EARLY ACCESS] GetCompositeBreakdown: Get the Composite Breakdown on how the composite Returns are calculated
        api_response = await api_instance.get_composite_breakdown(scope, code, composite_breakdown_request, from_effective_at=from_effective_at, to_effective_at=to_effective_at, as_at=as_at)
        print("The response of PortfoliosApi->get_composite_breakdown:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfoliosApi->get_composite_breakdown: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Portfolio. | 
 **code** | **str**| The code of the  Portfolio. | 
 **composite_breakdown_request** | [**CompositeBreakdownRequest**](CompositeBreakdownRequest.md)| The request used in the GetCompositeBreakdown. | 
 **from_effective_at** | **str**| The start date from which to calculate the Returns. | [optional] 
 **to_effective_at** | **str**| The end date for which to calculate the Returns. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Returns. Defaults to the latest. | [optional] 

### Return type

[**CompositeBreakdownResponse**](CompositeBreakdownResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The aggregated returns grouped by return stream. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_instrument_event_instruction**
> InstrumentEventInstruction get_instrument_event_instruction(scope, code, instrument_event_instruction_id, portfolio_effective_at=portfolio_effective_at, as_at=as_at)

[EARLY ACCESS] GetInstrumentEventInstruction: Get Instrument Event Instruction

Get a particular instruction for a particular portfolio

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.instrument_event_instruction import InstrumentEventInstruction
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    PortfoliosApi,
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
    api_instance = api_client_factory.build(lusid.PortfoliosApi)
    scope = 'scope_example' # str | The scope of the portfolio.
    code = 'code_example' # str | The code of the portfolio. Together with the scope this uniquely identifies the portfolio.
    instrument_event_instruction_id = 'instrument_event_instruction_id_example' # str | The id of the instruction to be retrieved.
    portfolio_effective_at = 'portfolio_effective_at_example' # str | The effective date at which the portfolio will be resolved. Defaults to current time if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the instruction. Defaults to return the latest version of the instruction if not specified. (optional)

    try:
        # [EARLY ACCESS] GetInstrumentEventInstruction: Get Instrument Event Instruction
        api_response = await api_instance.get_instrument_event_instruction(scope, code, instrument_event_instruction_id, portfolio_effective_at=portfolio_effective_at, as_at=as_at)
        print("The response of PortfoliosApi->get_instrument_event_instruction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfoliosApi->get_instrument_event_instruction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio. | 
 **code** | **str**| The code of the portfolio. Together with the scope this uniquely identifies the portfolio. | 
 **instrument_event_instruction_id** | **str**| The id of the instruction to be retrieved. | 
 **portfolio_effective_at** | **str**| The effective date at which the portfolio will be resolved. Defaults to current time if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the instruction. Defaults to return the latest version of the instruction if not specified. | [optional] 

### Return type

[**InstrumentEventInstruction**](InstrumentEventInstruction.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested instrument event instruction |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_portfolio**
> Portfolio get_portfolio(scope, code, effective_at=effective_at, as_at=as_at, property_keys=property_keys, relationship_definition_ids=relationship_definition_ids)

GetPortfolio: Get portfolio

Retrieve the definition of a particular portfolio.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.portfolio import Portfolio
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    PortfoliosApi,
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
    api_instance = api_client_factory.build(lusid.PortfoliosApi)
    scope = 'scope_example' # str | The scope of the portfolio.
    code = 'code_example' # str | The code of the portfolio. Together with the scope this uniquely identifies the portfolio.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve the portfolio definition. Defaults to the current LUSID system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the portfolio definition. Defaults to returning the latest version of the portfolio definition if not specified. (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the 'Portfolio' domain to decorate onto the portfolio,              or from any domain that supports relationships to decorate onto related entities. These must take the format              {domain}/{scope}/{code}, for example 'Portfolio/Manager/Id'. (optional)
    relationship_definition_ids = ['relationship_definition_ids_example'] # List[str] | A list of relationship definitions that are used to decorate related entities              onto the portfolio in the response. These must take the form {relationshipDefinitionScope}/{relationshipDefinitionCode}. (optional)

    try:
        # GetPortfolio: Get portfolio
        api_response = await api_instance.get_portfolio(scope, code, effective_at=effective_at, as_at=as_at, property_keys=property_keys, relationship_definition_ids=relationship_definition_ids)
        print("The response of PortfoliosApi->get_portfolio:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfoliosApi->get_portfolio: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio. | 
 **code** | **str**| The code of the portfolio. Together with the scope this uniquely identifies the portfolio. | 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the portfolio definition. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the portfolio definition. Defaults to returning the latest version of the portfolio definition if not specified. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;Portfolio&#39; domain to decorate onto the portfolio,              or from any domain that supports relationships to decorate onto related entities. These must take the format              {domain}/{scope}/{code}, for example &#39;Portfolio/Manager/Id&#39;. | [optional] 
 **relationship_definition_ids** | [**List[str]**](str.md)| A list of relationship definitions that are used to decorate related entities              onto the portfolio in the response. These must take the form {relationshipDefinitionScope}/{relationshipDefinitionCode}. | [optional] 

### Return type

[**Portfolio**](Portfolio.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested portfolio definition |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_portfolio_aggregate_returns**
> ResourceListOfAggregatedReturn get_portfolio_aggregate_returns(scope, code, return_scope, return_code, recipe_id_scope=recipe_id_scope, recipe_id_code=recipe_id_code, from_effective_at=from_effective_at, to_effective_at=to_effective_at, composite_method=composite_method, period=period, output_frequency=output_frequency, metrics=metrics, as_at=as_at, alternative_inc_date=alternative_inc_date)

[DEPRECATED] GetPortfolioAggregateReturns: Aggregate Returns (This is a deprecated endpoint).

Aggregate Returns which are on the specified portfolio.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.resource_list_of_aggregated_return import ResourceListOfAggregatedReturn
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    PortfoliosApi,
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
    api_instance = api_client_factory.build(lusid.PortfoliosApi)
    scope = 'scope_example' # str | The scope of the Portfolio.
    code = 'code_example' # str | The code of the  Portfolio.
    return_scope = 'return_scope_example' # str | The scope of the Returns.
    return_code = 'return_code_example' # str | The code of the Returns.
    recipe_id_scope = 'recipe_id_scope_example' # str | The Recipe Scope for getting the fx rates (optional)
    recipe_id_code = 'recipe_id_code_example' # str | The Recipe Code for getting the fx rates (optional)
    from_effective_at = 'from_effective_at_example' # str | The start date from which to calculate the Returns. (optional)
    to_effective_at = 'to_effective_at_example' # str | The end date for which to calculate the Returns. (optional)
    composite_method = 'composite_method_example' # str | The method used to calculate the Portfolio performance:              Equal/Asset. (optional)
    period = 'period_example' # str | The type of the returns used to calculate the aggregation result: Daily/Monthly. (optional)
    output_frequency = 'output_frequency_example' # str | The type of calculated output: Daily/Weekly/Monthly/Quarterly/Half-Yearly/Yearly. (optional)
    metrics = ['metrics_example'] # List[str] | Determines what type of returns should be calculated, see https://support.lusid.com/knowledgebase/article/KA-01675/en-us for a list of available metrics. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Returns. Defaults to the latest. (optional)
    alternative_inc_date = 'alternative_inc_date_example' # str | The date from which to consider the Returns on the Portfolio, if this is different from the date when Returns begin. Can be a date string or Portfolio property. (optional)

    try:
        # [DEPRECATED] GetPortfolioAggregateReturns: Aggregate Returns (This is a deprecated endpoint).
        api_response = await api_instance.get_portfolio_aggregate_returns(scope, code, return_scope, return_code, recipe_id_scope=recipe_id_scope, recipe_id_code=recipe_id_code, from_effective_at=from_effective_at, to_effective_at=to_effective_at, composite_method=composite_method, period=period, output_frequency=output_frequency, metrics=metrics, as_at=as_at, alternative_inc_date=alternative_inc_date)
        print("The response of PortfoliosApi->get_portfolio_aggregate_returns:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfoliosApi->get_portfolio_aggregate_returns: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Portfolio. | 
 **code** | **str**| The code of the  Portfolio. | 
 **return_scope** | **str**| The scope of the Returns. | 
 **return_code** | **str**| The code of the Returns. | 
 **recipe_id_scope** | **str**| The Recipe Scope for getting the fx rates | [optional] 
 **recipe_id_code** | **str**| The Recipe Code for getting the fx rates | [optional] 
 **from_effective_at** | **str**| The start date from which to calculate the Returns. | [optional] 
 **to_effective_at** | **str**| The end date for which to calculate the Returns. | [optional] 
 **composite_method** | **str**| The method used to calculate the Portfolio performance:              Equal/Asset. | [optional] 
 **period** | **str**| The type of the returns used to calculate the aggregation result: Daily/Monthly. | [optional] 
 **output_frequency** | **str**| The type of calculated output: Daily/Weekly/Monthly/Quarterly/Half-Yearly/Yearly. | [optional] 
 **metrics** | [**List[str]**](str.md)| Determines what type of returns should be calculated, see https://support.lusid.com/knowledgebase/article/KA-01675/en-us for a list of available metrics. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Returns. Defaults to the latest. | [optional] 
 **alternative_inc_date** | **str**| The date from which to consider the Returns on the Portfolio, if this is different from the date when Returns begin. Can be a date string or Portfolio property. | [optional] 

### Return type

[**ResourceListOfAggregatedReturn**](ResourceListOfAggregatedReturn.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The aggregated returns. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_portfolio_aggregated_returns**
> AggregatedReturnsResponse get_portfolio_aggregated_returns(scope, code, aggregated_returns_request, from_effective_at=from_effective_at, to_effective_at=to_effective_at, as_at=as_at)

[EARLY ACCESS] GetPortfolioAggregatedReturns: Aggregated Returns

Aggregate Returns which are on the specified portfolio.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.aggregated_returns_request import AggregatedReturnsRequest
from lusid.models.aggregated_returns_response import AggregatedReturnsResponse
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    PortfoliosApi,
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
    api_instance = api_client_factory.build(lusid.PortfoliosApi)
    scope = 'scope_example' # str | The scope of the Portfolio.
    code = 'code_example' # str | The code of the  Portfolio.
    aggregated_returns_request = {"metrics":[{"type":"Return","window":"1Y","allowPartial":false,"annualised":false,"withFee":true,"alias":"1M"}],"returnIds":[{"scope":"TestScope","code":"default"}],"recipeId":{"scope":"ReturnsScope","code":"ReturnCode"},"compositeMethod":"Asset","period":"Daily","outputFrequency":"Daily","alternativeInceptionDate":"2020-01-01","holidayCalendars":[],"currency":"USD","runMode":"ReturnData"} # AggregatedReturnsRequest | The request used in the AggregatedReturns.
    from_effective_at = 'from_effective_at_example' # str | The start date from which to calculate the Returns. (optional)
    to_effective_at = 'to_effective_at_example' # str | The end date for which to calculate the Returns. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Returns. Defaults to the latest. (optional)

    try:
        # [EARLY ACCESS] GetPortfolioAggregatedReturns: Aggregated Returns
        api_response = await api_instance.get_portfolio_aggregated_returns(scope, code, aggregated_returns_request, from_effective_at=from_effective_at, to_effective_at=to_effective_at, as_at=as_at)
        print("The response of PortfoliosApi->get_portfolio_aggregated_returns:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfoliosApi->get_portfolio_aggregated_returns: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Portfolio. | 
 **code** | **str**| The code of the  Portfolio. | 
 **aggregated_returns_request** | [**AggregatedReturnsRequest**](AggregatedReturnsRequest.md)| The request used in the AggregatedReturns. | 
 **from_effective_at** | **str**| The start date from which to calculate the Returns. | [optional] 
 **to_effective_at** | **str**| The end date for which to calculate the Returns. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Returns. Defaults to the latest. | [optional] 

### Return type

[**AggregatedReturnsResponse**](AggregatedReturnsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The aggregated returns grouped by return stream. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_portfolio_commands**
> ResourceListOfProcessedCommand get_portfolio_commands(scope, code, from_as_at=from_as_at, to_as_at=to_as_at, filter=filter, page=page, limit=limit)

GetPortfolioCommands: Get portfolio commands

Get all the commands that modified a particular portfolio, including any input transactions.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.resource_list_of_processed_command import ResourceListOfProcessedCommand
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    PortfoliosApi,
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
    api_instance = api_client_factory.build(lusid.PortfoliosApi)
    scope = 'scope_example' # str | The scope of the portfolio.
    code = 'code_example' # str | The code of the portfolio. Together with the scope this uniquely identifies the portfolio.
    from_as_at = '2013-10-20T19:20:30+01:00' # datetime | The lower bound asAt datetime (inclusive) from which to retrieve commands. There is no lower bound if this is not specified. (optional)
    to_as_at = '2013-10-20T19:20:30+01:00' # datetime | The upper bound asAt datetime (inclusive) from which to retrieve commands. There is no upper bound if this is not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the results.              For example, to filter on the User ID, specify \"userId.id eq 'string'\".              For more information about filtering, see https://support.lusid.com/knowledgebase/article/KA-01914. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing commands; this value is returned from the previous call. (optional)
    limit = 56 # int | When paginating, limit the results to this number. Defaults to 500 if not specified. (optional)

    try:
        # GetPortfolioCommands: Get portfolio commands
        api_response = await api_instance.get_portfolio_commands(scope, code, from_as_at=from_as_at, to_as_at=to_as_at, filter=filter, page=page, limit=limit)
        print("The response of PortfoliosApi->get_portfolio_commands:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfoliosApi->get_portfolio_commands: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio. | 
 **code** | **str**| The code of the portfolio. Together with the scope this uniquely identifies the portfolio. | 
 **from_as_at** | **datetime**| The lower bound asAt datetime (inclusive) from which to retrieve commands. There is no lower bound if this is not specified. | [optional] 
 **to_as_at** | **datetime**| The upper bound asAt datetime (inclusive) from which to retrieve commands. There is no upper bound if this is not specified. | [optional] 
 **filter** | **str**| Expression to filter the results.              For example, to filter on the User ID, specify \&quot;userId.id eq &#39;string&#39;\&quot;.              For more information about filtering, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **page** | **str**| The pagination token to use to continue listing commands; this value is returned from the previous call. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 500 if not specified. | [optional] 

### Return type

[**ResourceListOfProcessedCommand**](ResourceListOfProcessedCommand.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The commands that modified the specified portfolio. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_portfolio_metadata**
> Dict[str, List[AccessMetadataValue]] get_portfolio_metadata(scope, code, effective_at=effective_at, as_at=as_at)

[EARLY ACCESS] GetPortfolioMetadata: Get access metadata rules for a portfolio

Pass the scope and portfolio code parameters to retrieve the AccessMetadata associated with a portfolio

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.access_metadata_value import AccessMetadataValue
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    PortfoliosApi,
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
    api_instance = api_client_factory.build(lusid.PortfoliosApi)
    scope = 'scope_example' # str | The scope of the Portfolio Access Metadata Rule to retrieve.
    code = 'code_example' # str | Portfolio code
    effective_at = 'effective_at_example' # str | The effectiveAt datetime at which to retrieve the access metadata rule. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the portfolio access metadata. (optional)

    try:
        # [EARLY ACCESS] GetPortfolioMetadata: Get access metadata rules for a portfolio
        api_response = await api_instance.get_portfolio_metadata(scope, code, effective_at=effective_at, as_at=as_at)
        print("The response of PortfoliosApi->get_portfolio_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfoliosApi->get_portfolio_metadata: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Portfolio Access Metadata Rule to retrieve. | 
 **code** | **str**| Portfolio code | 
 **effective_at** | **str**| The effectiveAt datetime at which to retrieve the access metadata rule. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the portfolio access metadata. | [optional] 

### Return type

**Dict[str, List[AccessMetadataValue]]**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The filtered list of results |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_portfolio_properties**
> PortfolioProperties get_portfolio_properties(scope, code, effective_at=effective_at, as_at=as_at)

GetPortfolioProperties: Get portfolio properties

List all the properties of a particular portfolio.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.portfolio_properties import PortfolioProperties
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    PortfoliosApi,
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
    api_instance = api_client_factory.build(lusid.PortfoliosApi)
    scope = 'scope_example' # str | The scope of the portfolio.
    code = 'code_example' # str | The code of the portfolio. Together with the scope this uniquely identifies the portfolio.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to list the portfolio's properties. Defaults to the current LUSID system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the portfolio's properties. Defaults to returning the latest version of each property if not specified. (optional)

    try:
        # GetPortfolioProperties: Get portfolio properties
        api_response = await api_instance.get_portfolio_properties(scope, code, effective_at=effective_at, as_at=as_at)
        print("The response of PortfoliosApi->get_portfolio_properties:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfoliosApi->get_portfolio_properties: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio. | 
 **code** | **str**| The code of the portfolio. Together with the scope this uniquely identifies the portfolio. | 
 **effective_at** | **str**| The effective datetime or cut label at which to list the portfolio&#39;s properties. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the portfolio&#39;s properties. Defaults to returning the latest version of each property if not specified. | [optional] 

### Return type

[**PortfolioProperties**](PortfolioProperties.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The properties of the specified portfolio |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_portfolio_property_time_series**
> ResourceListOfPropertyInterval get_portfolio_property_time_series(scope, code, property_key, portfolio_effective_at=portfolio_effective_at, as_at=as_at, filter=filter, page=page, limit=limit)

[EARLY ACCESS] GetPortfolioPropertyTimeSeries: Get portfolio property time series

Show the complete time series (history) for a particular portfolio property.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.resource_list_of_property_interval import ResourceListOfPropertyInterval
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    PortfoliosApi,
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
    api_instance = api_client_factory.build(lusid.PortfoliosApi)
    scope = 'scope_example' # str | The scope of the portfolio.
    code = 'code_example' # str | The code of the portfolio. Together with the scope this uniquely identifies the portfolio.
    property_key = 'property_key_example' # str | The property key of the property whose history to show.              This must be from the 'Portfolio' domain and in the format {domain}/{scope}/{code}, for example 'Portfolio/Manager/Id'.
    portfolio_effective_at = 'portfolio_effective_at_example' # str | The effective datetime used to resolve the portfolio. Defaults to the current LUSID system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to show the history. Defaults to returning the current datetime if not supplied. (optional)
    filter = 'filter_example' # str | Expression to filter the results. For more information about filtering,              see https://support.lusid.com/knowledgebase/article/KA-01914. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing properties; this value is returned from              the previous call. If a pagination token is provided, the filter, portfolioEffectiveAt, and asAt fields              must not have changed since the original request. (optional)
    limit = 56 # int | When paginating, limit the results to this number. (optional)

    try:
        # [EARLY ACCESS] GetPortfolioPropertyTimeSeries: Get portfolio property time series
        api_response = await api_instance.get_portfolio_property_time_series(scope, code, property_key, portfolio_effective_at=portfolio_effective_at, as_at=as_at, filter=filter, page=page, limit=limit)
        print("The response of PortfoliosApi->get_portfolio_property_time_series:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfoliosApi->get_portfolio_property_time_series: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio. | 
 **code** | **str**| The code of the portfolio. Together with the scope this uniquely identifies the portfolio. | 
 **property_key** | **str**| The property key of the property whose history to show.              This must be from the &#39;Portfolio&#39; domain and in the format {domain}/{scope}/{code}, for example &#39;Portfolio/Manager/Id&#39;. | 
 **portfolio_effective_at** | **str**| The effective datetime used to resolve the portfolio. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to show the history. Defaults to returning the current datetime if not supplied. | [optional] 
 **filter** | **str**| Expression to filter the results. For more information about filtering,              see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **page** | **str**| The pagination token to use to continue listing properties; this value is returned from              the previous call. If a pagination token is provided, the filter, portfolioEffectiveAt, and asAt fields              must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. | [optional] 

### Return type

[**ResourceListOfPropertyInterval**](ResourceListOfPropertyInterval.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The time series of the property |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_portfolio_relations**
> ResourceListOfRelation get_portfolio_relations(scope, code, effective_at=effective_at, as_at=as_at, filter=filter, identifier_types=identifier_types)

[EXPERIMENTAL] GetPortfolioRelations: Get portfolio relations

Get relations for a particular portfolio.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.resource_list_of_relation import ResourceListOfRelation
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    PortfoliosApi,
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
    api_instance = api_client_factory.build(lusid.PortfoliosApi)
    scope = 'scope_example' # str | The scope of the portfolio.
    code = 'code_example' # str | The code of the portfolio. Together with the scope this uniquely identifies the portfolio.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve relations. Defaults to the current LUSID system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve relations. Defaults to returning the latest LUSID AsAt time if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the relations. Provide a null or empty string for this field until further notice. (optional)
    identifier_types = ['identifier_types_example'] # List[str] | Identifier types (as property keys) used for referencing Persons or Legal Entities.              These must be from the 'Person' or 'LegalEntity' domains and have the format {domain}/{scope}/{code}, for example              'Person/CompanyDetails/Role'. Only identifier types provided will be used to look up relevant entities in relations. If not applicable, provide an empty array. (optional)

    try:
        # [EXPERIMENTAL] GetPortfolioRelations: Get portfolio relations
        api_response = await api_instance.get_portfolio_relations(scope, code, effective_at=effective_at, as_at=as_at, filter=filter, identifier_types=identifier_types)
        print("The response of PortfoliosApi->get_portfolio_relations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfoliosApi->get_portfolio_relations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio. | 
 **code** | **str**| The code of the portfolio. Together with the scope this uniquely identifies the portfolio. | 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve relations. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve relations. Defaults to returning the latest LUSID AsAt time if not specified. | [optional] 
 **filter** | **str**| Expression to filter the relations. Provide a null or empty string for this field until further notice. | [optional] 
 **identifier_types** | [**List[str]**](str.md)| Identifier types (as property keys) used for referencing Persons or Legal Entities.              These must be from the &#39;Person&#39; or &#39;LegalEntity&#39; domains and have the format {domain}/{scope}/{code}, for example              &#39;Person/CompanyDetails/Role&#39;. Only identifier types provided will be used to look up relevant entities in relations. If not applicable, provide an empty array. | [optional] 

### Return type

[**ResourceListOfRelation**](ResourceListOfRelation.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The relations for the specified portfolio. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_portfolio_relationships**
> ResourceListOfRelationship get_portfolio_relationships(scope, code, effective_at=effective_at, as_at=as_at, filter=filter, identifier_types=identifier_types)

[EARLY ACCESS] GetPortfolioRelationships: Get portfolio relationships

Get relationships for a particular portfolio.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.resource_list_of_relationship import ResourceListOfRelationship
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    PortfoliosApi,
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
    api_instance = api_client_factory.build(lusid.PortfoliosApi)
    scope = 'scope_example' # str | The scope of the portfolio.
    code = 'code_example' # str | The code of the portfolio. Together with the scope this uniquely identifies the portfolio.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve relationships. Defaults to the current LUSID system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve relationships. Defaults to returning the latest LUSID AsAt time if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the relationships. Provide a null or empty string for this field until further notice. (optional)
    identifier_types = ['identifier_types_example'] # List[str] | Identifier types (as property keys) used for referencing Persons or Legal Entities.              These can be specified from the 'Person' or 'LegalEntity' domains and have the format {domain}/{scope}/{code}, for example              'Person/CompanyDetails/Role'. An Empty array may be used to return all related Entities. (optional)

    try:
        # [EARLY ACCESS] GetPortfolioRelationships: Get portfolio relationships
        api_response = await api_instance.get_portfolio_relationships(scope, code, effective_at=effective_at, as_at=as_at, filter=filter, identifier_types=identifier_types)
        print("The response of PortfoliosApi->get_portfolio_relationships:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfoliosApi->get_portfolio_relationships: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio. | 
 **code** | **str**| The code of the portfolio. Together with the scope this uniquely identifies the portfolio. | 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve relationships. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve relationships. Defaults to returning the latest LUSID AsAt time if not specified. | [optional] 
 **filter** | **str**| Expression to filter the relationships. Provide a null or empty string for this field until further notice. | [optional] 
 **identifier_types** | [**List[str]**](str.md)| Identifier types (as property keys) used for referencing Persons or Legal Entities.              These can be specified from the &#39;Person&#39; or &#39;LegalEntity&#39; domains and have the format {domain}/{scope}/{code}, for example              &#39;Person/CompanyDetails/Role&#39;. An Empty array may be used to return all related Entities. | [optional] 

### Return type

[**ResourceListOfRelationship**](ResourceListOfRelationship.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The relationships for the specified portfolio. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_portfolio_returns**
> ResourceListOfPerformanceReturn get_portfolio_returns(scope, code, return_scope, return_code, from_effective_at=from_effective_at, to_effective_at=to_effective_at, period=period, as_at=as_at)

[EARLY ACCESS] GetPortfolioReturns: Get Returns

Get Returns which are on the specified portfolio.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.resource_list_of_performance_return import ResourceListOfPerformanceReturn
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    PortfoliosApi,
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
    api_instance = api_client_factory.build(lusid.PortfoliosApi)
    scope = 'scope_example' # str | The scope of the Portfolio.
    code = 'code_example' # str | The code of the  Portfolio.
    return_scope = 'return_scope_example' # str | The scope of the Returns.
    return_code = 'return_code_example' # str | The code of the Returns.
    from_effective_at = 'from_effective_at_example' # str | The start date from which to get the Returns. (optional)
    to_effective_at = 'to_effective_at_example' # str | The end date from which to get the Returns. (optional)
    period = 'period_example' # str | Show the Returns on a Daily or Monthly period. Defaults to Daily. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Returns. Defaults to the latest. (optional)

    try:
        # [EARLY ACCESS] GetPortfolioReturns: Get Returns
        api_response = await api_instance.get_portfolio_returns(scope, code, return_scope, return_code, from_effective_at=from_effective_at, to_effective_at=to_effective_at, period=period, as_at=as_at)
        print("The response of PortfoliosApi->get_portfolio_returns:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfoliosApi->get_portfolio_returns: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Portfolio. | 
 **code** | **str**| The code of the  Portfolio. | 
 **return_scope** | **str**| The scope of the Returns. | 
 **return_code** | **str**| The code of the Returns. | 
 **from_effective_at** | **str**| The start date from which to get the Returns. | [optional] 
 **to_effective_at** | **str**| The end date from which to get the Returns. | [optional] 
 **period** | **str**| Show the Returns on a Daily or Monthly period. Defaults to Daily. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Returns. Defaults to the latest. | [optional] 

### Return type

[**ResourceListOfPerformanceReturn**](ResourceListOfPerformanceReturn.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Returns on the given time period. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_portfolios_access_metadata_by_key**
> List[AccessMetadataValue] get_portfolios_access_metadata_by_key(scope, code, metadata_key, effective_at=effective_at, as_at=as_at)

[EARLY ACCESS] GetPortfoliosAccessMetadataByKey: Get an entry identified by a metadataKey in the access metadata object

Get a specific portfolio access metadata rule by specifying the corresponding identifier parts                No matching will be performed through this endpoint. To retrieve a rule, it is necessary to specify, exactly, the identifier of the rule

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.access_metadata_value import AccessMetadataValue
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    PortfoliosApi,
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
    api_instance = api_client_factory.build(lusid.PortfoliosApi)
    scope = 'scope_example' # str | The scope of the Portfolio Access Metadata Rule to retrieve.
    code = 'code_example' # str | The code of the portfolio
    metadata_key = 'metadata_key_example' # str | Key of the metadata to retrieve
    effective_at = 'effective_at_example' # str | The effective date of the rule (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the portfolio access metadata. (optional)

    try:
        # [EARLY ACCESS] GetPortfoliosAccessMetadataByKey: Get an entry identified by a metadataKey in the access metadata object
        api_response = await api_instance.get_portfolios_access_metadata_by_key(scope, code, metadata_key, effective_at=effective_at, as_at=as_at)
        print("The response of PortfoliosApi->get_portfolios_access_metadata_by_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfoliosApi->get_portfolios_access_metadata_by_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Portfolio Access Metadata Rule to retrieve. | 
 **code** | **str**| The code of the portfolio | 
 **metadata_key** | **str**| Key of the metadata to retrieve | 
 **effective_at** | **str**| The effective date of the rule | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the portfolio access metadata. | [optional] 

### Return type

[**List[AccessMetadataValue]**](AccessMetadataValue.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully retrieved Portfolio Access Metadata Rule or any failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_portfolio_properties**
> ResourceListOfProperty list_portfolio_properties(scope, code, effective_at=effective_at, as_at=as_at, page=page, limit=limit)

[EARLY ACCESS] ListPortfolioProperties: Get portfolio properties

List all the properties of a particular portfolio.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.resource_list_of_property import ResourceListOfProperty
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    PortfoliosApi,
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
    api_instance = api_client_factory.build(lusid.PortfoliosApi)
    scope = 'scope_example' # str | The scope of the portfolio.
    code = 'code_example' # str | The code of the portfolio. Together with the scope this uniquely identifies the portfolio.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to list the portfolio's properties. Defaults to the current LUSID system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the portfolio's properties. Defaults to returning the latest version of each property if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing commands; this value is returned from the previous call. (optional)
    limit = 56 # int | When paginating, limit the results per page to this number. (optional)

    try:
        # [EARLY ACCESS] ListPortfolioProperties: Get portfolio properties
        api_response = await api_instance.list_portfolio_properties(scope, code, effective_at=effective_at, as_at=as_at, page=page, limit=limit)
        print("The response of PortfoliosApi->list_portfolio_properties:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfoliosApi->list_portfolio_properties: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio. | 
 **code** | **str**| The code of the portfolio. Together with the scope this uniquely identifies the portfolio. | 
 **effective_at** | **str**| The effective datetime or cut label at which to list the portfolio&#39;s properties. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the portfolio&#39;s properties. Defaults to returning the latest version of each property if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing commands; this value is returned from the previous call. | [optional] 
 **limit** | **int**| When paginating, limit the results per page to this number. | [optional] 

### Return type

[**ResourceListOfProperty**](ResourceListOfProperty.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The properties of the specified portfolio |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_portfolios**
> ResourceListOfPortfolio list_portfolios(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, query=query, property_keys=property_keys, relationship_definition_ids=relationship_definition_ids)

ListPortfolios: List portfolios

List all the portfolios matching particular criteria.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.resource_list_of_portfolio import ResourceListOfPortfolio
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    PortfoliosApi,
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
    api_instance = api_client_factory.build(lusid.PortfoliosApi)
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to list the portfolios. Defaults to the current LUSID              system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the portfolios. Defaults to returning the latest version              of each portfolio if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing portfolios; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. (optional)
    limit = 56 # int | When paginating, limit the results to this number. Defaults to 100 if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the results.              For example, to filter on the transaction type, specify \"type eq 'Transaction'\". For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. (optional)
    sort_by = ['sort_by_example'] # List[str] | A list of field names or properties to sort by, each suffixed by \" ASC\" or \" DESC\". (optional)
    query = 'query_example' # str | Expression specifying the criteria that the returned portfolios must meet. For example, to see which              portfolios have holdings in instruments with a LusidInstrumentId (LUID) of 'LUID_PPA8HI6M' or a Figi of 'BBG000BLNNH6',              specify \"instrument.identifiers in (('LusidInstrumentId', 'LUID_PPA8HI6M'), ('Figi', 'BBG000BLNNH6'))\". (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the 'Portfolio' domain to decorate onto each portfolio,              or from any domain that supports relationships to decorate onto related entities. These must take the              format {domain}/{scope}/{code}, for example 'Portfolio/Manager/Id'. (optional)
    relationship_definition_ids = ['relationship_definition_ids_example'] # List[str] | A list of relationship definitions that are used to decorate related entities              onto the portfolios in the response. These must take the form {relationshipDefinitionScope}/{relationshipDefinitionCode}. (optional)

    try:
        # ListPortfolios: List portfolios
        api_response = await api_instance.list_portfolios(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, query=query, property_keys=property_keys, relationship_definition_ids=relationship_definition_ids)
        print("The response of PortfoliosApi->list_portfolios:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfoliosApi->list_portfolios: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **effective_at** | **str**| The effective datetime or cut label at which to list the portfolios. Defaults to the current LUSID              system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the portfolios. Defaults to returning the latest version              of each portfolio if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing portfolios; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results.              For example, to filter on the transaction type, specify \&quot;type eq &#39;Transaction&#39;\&quot;. For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 
 **query** | **str**| Expression specifying the criteria that the returned portfolios must meet. For example, to see which              portfolios have holdings in instruments with a LusidInstrumentId (LUID) of &#39;LUID_PPA8HI6M&#39; or a Figi of &#39;BBG000BLNNH6&#39;,              specify \&quot;instrument.identifiers in ((&#39;LusidInstrumentId&#39;, &#39;LUID_PPA8HI6M&#39;), (&#39;Figi&#39;, &#39;BBG000BLNNH6&#39;))\&quot;. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;Portfolio&#39; domain to decorate onto each portfolio,              or from any domain that supports relationships to decorate onto related entities. These must take the              format {domain}/{scope}/{code}, for example &#39;Portfolio/Manager/Id&#39;. | [optional] 
 **relationship_definition_ids** | [**List[str]**](str.md)| A list of relationship definitions that are used to decorate related entities              onto the portfolios in the response. These must take the form {relationshipDefinitionScope}/{relationshipDefinitionCode}. | [optional] 

### Return type

[**ResourceListOfPortfolio**](ResourceListOfPortfolio.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested portfolios |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_portfolios_for_scope**
> ResourceListOfPortfolio list_portfolios_for_scope(scope, effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys, relationship_definition_ids=relationship_definition_ids)

ListPortfoliosForScope: List portfolios for scope

List all the portfolios in a particular scope.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.resource_list_of_portfolio import ResourceListOfPortfolio
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    PortfoliosApi,
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
    api_instance = api_client_factory.build(lusid.PortfoliosApi)
    scope = 'scope_example' # str | The scope whose portfolios to list.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to list the portfolios. Defaults to the current LUSID              system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the portfolios. Defaults to returning the latest version              of each portfolio if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing portfolios. This  value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt  and asAt fields must not have changed since the original request. (optional)
    limit = 56 # int | When paginating, limit the results to this number. Defaults to 100 if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the results.              For example, to return only transactions with a transaction type of 'Buy', specify \"type eq 'Buy'\".              For more information about filtering results, see https://support.lusid.com/knowledgebase/article/KA-01914. (optional)
    sort_by = ['sort_by_example'] # List[str] | A list of field names or properties to sort by, each suffixed by \" ASC\" or \" DESC\". (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the 'Portfolio' domain to decorate onto each portfolio,              or from any domain that supports relationships to decorate onto related entities. These must take the              format {domain}/{scope}/{code}, for example 'Portfolio/Manager/Id'. (optional)
    relationship_definition_ids = ['relationship_definition_ids_example'] # List[str] | A list of relationship definitions that are used to decorate related entities              onto the portfolios in the response. These must take the form {relationshipDefinitionScope}/{relationshipDefinitionCode}. (optional)

    try:
        # ListPortfoliosForScope: List portfolios for scope
        api_response = await api_instance.list_portfolios_for_scope(scope, effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys, relationship_definition_ids=relationship_definition_ids)
        print("The response of PortfoliosApi->list_portfolios_for_scope:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfoliosApi->list_portfolios_for_scope: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope whose portfolios to list. | 
 **effective_at** | **str**| The effective datetime or cut label at which to list the portfolios. Defaults to the current LUSID              system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the portfolios. Defaults to returning the latest version              of each portfolio if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing portfolios. This  value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt  and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results.              For example, to return only transactions with a transaction type of &#39;Buy&#39;, specify \&quot;type eq &#39;Buy&#39;\&quot;.              For more information about filtering results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;Portfolio&#39; domain to decorate onto each portfolio,              or from any domain that supports relationships to decorate onto related entities. These must take the              format {domain}/{scope}/{code}, for example &#39;Portfolio/Manager/Id&#39;. | [optional] 
 **relationship_definition_ids** | [**List[str]**](str.md)| A list of relationship definitions that are used to decorate related entities              onto the portfolios in the response. These must take the form {relationshipDefinitionScope}/{relationshipDefinitionCode}. | [optional] 

### Return type

[**ResourceListOfPortfolio**](ResourceListOfPortfolio.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The portfolios in the specified scope |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_portfolio**
> Portfolio patch_portfolio(scope, code, operation)

[EARLY ACCESS] PatchPortfolio: Patch portfolio.

Create or update certain fields for a particular  portfolio.  The behaviour is defined by the JSON Patch specification.                Currently supported are: CreationDate, InstrumentScopes.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.operation import Operation
from lusid.models.portfolio import Portfolio
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    PortfoliosApi,
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
    api_instance = api_client_factory.build(lusid.PortfoliosApi)
    scope = 'scope_example' # str | The scope of the portfolio.
    code = 'code_example' # str | The code of the portfolio. Together with the               scope this uniquely identifies the portfolio.
    operation = [{"value":"2020-01-01","path":"/creationDate","op":"add"}] # List[Operation] | The json patch document. For more check: https://datatracker.ietf.org/doc/html/rfc6902.

    try:
        # [EARLY ACCESS] PatchPortfolio: Patch portfolio.
        api_response = await api_instance.patch_portfolio(scope, code, operation)
        print("The response of PortfoliosApi->patch_portfolio:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfoliosApi->patch_portfolio: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio. | 
 **code** | **str**| The code of the portfolio. Together with the               scope this uniquely identifies the portfolio. | 
 **operation** | [**List[Operation]**](Operation.md)| The json patch document. For more check: https://datatracker.ietf.org/doc/html/rfc6902. | 

### Return type

[**Portfolio**](Portfolio.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The newly patched portfolio |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_portfolio_access_metadata**
> Dict[str, List[AccessMetadataValue]] patch_portfolio_access_metadata(scope, code, access_metadata_operation, effective_at=effective_at, effective_until=effective_until)

[EARLY ACCESS] PatchPortfolioAccessMetadata: Patch Access Metadata rules for a Portfolio.

Patch Portfolio Access Metadata Rules in a single scope.  The behaviour is defined by the JSON Patch specification.                Currently only 'add' is a supported operation on the patch document.    Currently only valid metadata keys are supported paths on the patch document.    The response will return any affected Portfolio Access Metadata rules or a failure message if unsuccessful.    It is important to always check to verify success (or failure).                Multiple rules for a metadataKey can exist with different effective at dates, when resources are accessed the rule that is active for the current time will be fetched.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.access_metadata_operation import AccessMetadataOperation
from lusid.models.access_metadata_value import AccessMetadataValue
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    PortfoliosApi,
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
    api_instance = api_client_factory.build(lusid.PortfoliosApi)
    scope = 'scope_example' # str | The scope of the Portfolio Access Metadata Rule.
    code = 'code_example' # str | Portfolio code
    access_metadata_operation = [{"value":[{"value":"SilverLicence","provider":"TestDataProvider"}],"path":"/exampleMetadataKey","op":"add"}] # List[AccessMetadataOperation] | The Json Patch document
    effective_at = 'effective_at_example' # str | The date this rule will effective from (optional)
    effective_until = '2013-10-20T19:20:30+01:00' # datetime | The effective date until which the Access Metadata is valid. If not supplied this will be valid indefinitely, or until the next 'effectiveAt' date of the Access Metadata (optional)

    try:
        # [EARLY ACCESS] PatchPortfolioAccessMetadata: Patch Access Metadata rules for a Portfolio.
        api_response = await api_instance.patch_portfolio_access_metadata(scope, code, access_metadata_operation, effective_at=effective_at, effective_until=effective_until)
        print("The response of PortfoliosApi->patch_portfolio_access_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfoliosApi->patch_portfolio_access_metadata: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Portfolio Access Metadata Rule. | 
 **code** | **str**| Portfolio code | 
 **access_metadata_operation** | [**List[AccessMetadataOperation]**](AccessMetadataOperation.md)| The Json Patch document | 
 **effective_at** | **str**| The date this rule will effective from | [optional] 
 **effective_until** | **datetime**| The effective date until which the Access Metadata is valid. If not supplied this will be valid indefinitely, or until the next &#39;effectiveAt&#39; date of the Access Metadata | [optional] 

### Return type

**Dict[str, List[AccessMetadataValue]]**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully patched items. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_portfolio**
> Portfolio update_portfolio(scope, code, update_portfolio_request, effective_at=effective_at)

UpdatePortfolio: Update portfolio

Update the definition of a particular portfolio.                Note that not all elements of a portfolio definition are  modifiable due to the potential implications for data already stored.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.portfolio import Portfolio
from lusid.models.update_portfolio_request import UpdatePortfolioRequest
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    PortfoliosApi,
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
    api_instance = api_client_factory.build(lusid.PortfoliosApi)
    scope = 'scope_example' # str | The scope of the portfolio.
    code = 'code_example' # str | The code of the portfolio. Together with the scope this uniquely identifies the portfolio.
    update_portfolio_request = {"displayName":"MyPortfolioName","description":"Long form description of portfolio"} # UpdatePortfolioRequest | The updated portfolio definition.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to update the definition. Defaults to the current               LUSID system datetime if not specified. (optional)

    try:
        # UpdatePortfolio: Update portfolio
        api_response = await api_instance.update_portfolio(scope, code, update_portfolio_request, effective_at=effective_at)
        print("The response of PortfoliosApi->update_portfolio:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfoliosApi->update_portfolio: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio. | 
 **code** | **str**| The code of the portfolio. Together with the scope this uniquely identifies the portfolio. | 
 **update_portfolio_request** | [**UpdatePortfolioRequest**](UpdatePortfolioRequest.md)| The updated portfolio definition. | 
 **effective_at** | **str**| The effective datetime or cut label at which to update the definition. Defaults to the current               LUSID system datetime if not specified. | [optional] 

### Return type

[**Portfolio**](Portfolio.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated definition of the portfolio |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_instrument_event_instructions**
> InstrumentEventInstructionsResponse upsert_instrument_event_instructions(scope, code, success_mode, request_body, portfolio_effective_at=portfolio_effective_at)

[EARLY ACCESS] UpsertInstrumentEventInstructions: Upsert Instrument Event Instructions

Batch upsert for instrument event instructions, for the portfolio or individual holdings

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.instrument_event_instruction_request import InstrumentEventInstructionRequest
from lusid.models.instrument_event_instructions_response import InstrumentEventInstructionsResponse
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    PortfoliosApi,
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
    api_instance = api_client_factory.build(lusid.PortfoliosApi)
    scope = 'scope_example' # str | The scope of the portfolio.
    code = 'code_example' # str | The code of the portfolio. Together with the scope this uniquely identifies the portfolio.
    success_mode = 'Partial' # str | Whether the batch request should fail atomically or in a partial fashion - allowed values: Atomic, Partial (default) (default to 'Partial')
    request_body = {"request":{"instrumentEventInstructionId":"ExampleInstructionId","instrumentEventId":"ExampleInstrumentEventId","instructionType":"ElectForHolding","electionKey":"GBP","holdingId":123456789}} # Dict[str, InstrumentEventInstructionRequest] | The instructions to be upserted to the portfolio.
    portfolio_effective_at = 'portfolio_effective_at_example' # str | The effective date at which the portfolio will be resolved. Defaults to current time if not specified. (optional)

    try:
        # [EARLY ACCESS] UpsertInstrumentEventInstructions: Upsert Instrument Event Instructions
        api_response = await api_instance.upsert_instrument_event_instructions(scope, code, success_mode, request_body, portfolio_effective_at=portfolio_effective_at)
        print("The response of PortfoliosApi->upsert_instrument_event_instructions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfoliosApi->upsert_instrument_event_instructions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio. | 
 **code** | **str**| The code of the portfolio. Together with the scope this uniquely identifies the portfolio. | 
 **success_mode** | **str**| Whether the batch request should fail atomically or in a partial fashion - allowed values: Atomic, Partial (default) | [default to &#39;Partial&#39;]
 **request_body** | [**Dict[str, InstrumentEventInstructionRequest]**](InstrumentEventInstructionRequest.md)| The instructions to be upserted to the portfolio. | 
 **portfolio_effective_at** | **str**| The effective date at which the portfolio will be resolved. Defaults to current time if not specified. | [optional] 

### Return type

[**InstrumentEventInstructionsResponse**](InstrumentEventInstructionsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The newly inserted or updated instrument event instructions |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_portfolio_access_metadata**
> ResourceListOfAccessMetadataValueOf upsert_portfolio_access_metadata(scope, code, metadata_key, upsert_portfolio_access_metadata_request, effective_at=effective_at, effective_until=effective_until)

[EARLY ACCESS] UpsertPortfolioAccessMetadata: Upsert a Portfolio Access Metadata Rule associated with specific metadataKey. This creates or updates the data in LUSID.

Update or insert one Portfolio Access Metadata Rule in a single scope. An item will be updated if it already exists  and inserted if it does not.    The response will return the successfully updated or inserted Portfolio Access Metadata Rule or failure message if unsuccessful    It is important to always check to verify success (or failure).                Multiple rules for a metadataKey can exists with different effective at dates, when resources are accessed the rule that is active for the current time will be fetched

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.resource_list_of_access_metadata_value_of import ResourceListOfAccessMetadataValueOf
from lusid.models.upsert_portfolio_access_metadata_request import UpsertPortfolioAccessMetadataRequest
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    PortfoliosApi,
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
    api_instance = api_client_factory.build(lusid.PortfoliosApi)
    scope = 'scope_example' # str | The scope to use when updating or inserting the Portfolio Access Metadata Rule.
    code = 'code_example' # str | Portfolio code
    metadata_key = 'metadata_key_example' # str | Key of the access metadata to upsert
    upsert_portfolio_access_metadata_request = {"metadata":[{"value":"SilverLicence","provider":"TestDataProvider"}]} # UpsertPortfolioAccessMetadataRequest | The Portfolio Access Metadata Rule to update or insert
    effective_at = 'effective_at_example' # str | The date this rule will effective from (optional)
    effective_until = '2013-10-20T19:20:30+01:00' # datetime | The effective date until which the Access Metadata is valid. If not supplied this will be valid indefinitely, or until the next 'effectiveAt' date of the Access Metadata (optional)

    try:
        # [EARLY ACCESS] UpsertPortfolioAccessMetadata: Upsert a Portfolio Access Metadata Rule associated with specific metadataKey. This creates or updates the data in LUSID.
        api_response = await api_instance.upsert_portfolio_access_metadata(scope, code, metadata_key, upsert_portfolio_access_metadata_request, effective_at=effective_at, effective_until=effective_until)
        print("The response of PortfoliosApi->upsert_portfolio_access_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfoliosApi->upsert_portfolio_access_metadata: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope to use when updating or inserting the Portfolio Access Metadata Rule. | 
 **code** | **str**| Portfolio code | 
 **metadata_key** | **str**| Key of the access metadata to upsert | 
 **upsert_portfolio_access_metadata_request** | [**UpsertPortfolioAccessMetadataRequest**](UpsertPortfolioAccessMetadataRequest.md)| The Portfolio Access Metadata Rule to update or insert | 
 **effective_at** | **str**| The date this rule will effective from | [optional] 
 **effective_until** | **datetime**| The effective date until which the Access Metadata is valid. If not supplied this will be valid indefinitely, or until the next &#39;effectiveAt&#39; date of the Access Metadata | [optional] 

### Return type

[**ResourceListOfAccessMetadataValueOf**](ResourceListOfAccessMetadataValueOf.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully updated or inserted item or any failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_portfolio_properties**
> PortfolioProperties upsert_portfolio_properties(scope, code, request_body)

UpsertPortfolioProperties: Upsert portfolio properties

Create or update one or more properties for a particular portfolio. A property is updated if it  already exists and created if it does not. All properties must be from the 'Portfolio' domain.                Properties have an <i>effectiveFrom</i> datetime from which the property is valid, and an <i>effectiveUntil</i>  datetime until which it is valid. Not supplying an <i>effectiveUntil</i> datetime results in the property being  valid indefinitely, or until the next <i>effectiveFrom</i> datetime of the property.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.model_property import ModelProperty
from lusid.models.portfolio_properties import PortfolioProperties
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    PortfoliosApi,
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
    api_instance = api_client_factory.build(lusid.PortfoliosApi)
    scope = 'scope_example' # str | The scope of the portfolio.
    code = 'code_example' # str | The code of the portfolio. Together with the scope this uniquely identifies the portfolio.
    request_body = {"Portfolio/MyScope/FundManagerName":{"key":"Portfolio/MyScope/FundManagerName","value":{"labelValue":"Smith"},"effectiveFrom":"2018-03-05T00:00:00.0000000+00:00"},"Portfolio/MyScope/SomeProperty":{"key":"Portfolio/MyScope/SomeProperty","value":{"labelValue":"SomeValue"},"effectiveFrom":"2016-01-01T00:00:00.0000000+00:00"},"Portfolio/MyScope/AnotherProperty":{"key":"Portfolio/MyScope/AnotherProperty","value":{"labelValue":"AnotherValue"},"effectiveFrom":"2018-03-05T00:00:00.0000000+00:00","effectiveUntil":"2020-01-01T00:00:00.0000000+00:00"},"Portfolio/MyScope/ReBalanceInterval":{"key":"Portfolio/MyScope/ReBalanceInterval","value":{"metricValue":{"value":30,"unit":"Days"}}}} # Dict[str, ModelProperty] | The properties to be created or updated. Each property in               the request must be keyed by its unique property key. This has the format {domain}/{scope}/{code}, for example               'Portfolio/Manager/Id'.

    try:
        # UpsertPortfolioProperties: Upsert portfolio properties
        api_response = await api_instance.upsert_portfolio_properties(scope, code, request_body)
        print("The response of PortfoliosApi->upsert_portfolio_properties:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfoliosApi->upsert_portfolio_properties: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio. | 
 **code** | **str**| The code of the portfolio. Together with the scope this uniquely identifies the portfolio. | 
 **request_body** | [**Dict[str, ModelProperty]**](ModelProperty.md)| The properties to be created or updated. Each property in               the request must be keyed by its unique property key. This has the format {domain}/{scope}/{code}, for example               &#39;Portfolio/Manager/Id&#39;. | 

### Return type

[**PortfolioProperties**](PortfolioProperties.md)

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

# **upsert_portfolio_returns**
> UpsertReturnsResponse upsert_portfolio_returns(scope, code, return_scope, return_code, performance_return)

[EARLY ACCESS] UpsertPortfolioReturns: Upsert Returns

Update or insert returns into the specified portfolio.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.performance_return import PerformanceReturn
from lusid.models.upsert_returns_response import UpsertReturnsResponse
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    PortfoliosApi,
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
    api_instance = api_client_factory.build(lusid.PortfoliosApi)
    scope = 'scope_example' # str | The scope of the Portfolio.
    code = 'code_example' # str | The code of the  Portfolio.
    return_scope = 'return_scope_example' # str | The scope of the Returns.
    return_code = 'return_code_example' # str | The code of the Returns.
    performance_return = [{"effectiveAt":"2019-11-28T00:00:00.0000000+00:00","rateOfReturn":0.1,"openingMarketValue":500,"closingMarketValue":550,"period":"Daily"},{"effectiveAt":"2019-11-29T00:00:00.0000000+00:00","rateOfReturn":-0.2,"openingMarketValue":550,"closingMarketValue":440,"period":"Daily"}] # List[PerformanceReturn] | This contains the Returns which need to be upsert.

    try:
        # [EARLY ACCESS] UpsertPortfolioReturns: Upsert Returns
        api_response = await api_instance.upsert_portfolio_returns(scope, code, return_scope, return_code, performance_return)
        print("The response of PortfoliosApi->upsert_portfolio_returns:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfoliosApi->upsert_portfolio_returns: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Portfolio. | 
 **code** | **str**| The code of the  Portfolio. | 
 **return_scope** | **str**| The scope of the Returns. | 
 **return_code** | **str**| The code of the Returns. | 
 **performance_return** | [**List[PerformanceReturn]**](PerformanceReturn.md)| This contains the Returns which need to be upsert. | 

### Return type

[**UpsertReturnsResponse**](UpsertReturnsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The version of the portfolio that contains the newly updated or inserted Returns. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

