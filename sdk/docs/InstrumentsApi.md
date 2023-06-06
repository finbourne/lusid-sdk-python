# lusid.InstrumentsApi

All URIs are relative to *https://fbn-ci.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_instrument**](InstrumentsApi.md#delete_instrument) | **DELETE** /api/instruments/{identifierType}/{identifier} | [EARLY ACCESS] DeleteInstrument: Soft delete a single instrument
[**delete_instrument_properties**](InstrumentsApi.md#delete_instrument_properties) | **POST** /api/instruments/{identifierType}/{identifier}/properties/$delete | [EARLY ACCESS] DeleteInstrumentProperties: Delete instrument properties
[**delete_instruments**](InstrumentsApi.md#delete_instruments) | **POST** /api/instruments/$delete | [EARLY ACCESS] DeleteInstruments: Soft or hard delete multiple instruments
[**get_all_possible_features**](InstrumentsApi.md#get_all_possible_features) | **GET** /api/instruments/{instrumentType}/allfeatures | [EXPERIMENTAL] GetAllPossibleFeatures: Provides list of all possible features for instrument type.
[**get_existing_instrument_capabilities**](InstrumentsApi.md#get_existing_instrument_capabilities) | **GET** /api/instruments/{identifier}/capabilities | [EXPERIMENTAL] GetExistingInstrumentCapabilities: Retrieve capabilities of an existing instrument identified by LUID. These include instrument features, and if model is provided it also includes supported address keys and economic dependencies.  Given an lusid instrument id provides instrument capabilities, outlining features, and, given the model, the capabilities also include supported addresses as well as economic dependencies.
[**get_existing_instrument_models**](InstrumentsApi.md#get_existing_instrument_models) | **GET** /api/instruments/{identifier}/models | GetExistingInstrumentModels: Retrieve supported pricing models for an existing instrument identified by LUID.
[**get_instrument**](InstrumentsApi.md#get_instrument) | **GET** /api/instruments/{identifierType}/{identifier} | GetInstrument: Get instrument
[**get_instrument_identifier_types**](InstrumentsApi.md#get_instrument_identifier_types) | **GET** /api/instruments/identifierTypes | GetInstrumentIdentifierTypes: Get instrument identifier types
[**get_instrument_payment_diary**](InstrumentsApi.md#get_instrument_payment_diary) | **GET** /api/instruments/{identifierType}/{identifier}/paymentdiary | [EXPERIMENTAL] GetInstrumentPaymentDiary: Get instrument payment diary
[**get_instrument_properties**](InstrumentsApi.md#get_instrument_properties) | **GET** /api/instruments/{identifierType}/{identifier}/properties | [EARLY ACCESS] GetInstrumentProperties: Get instrument properties
[**get_instrument_property_time_series**](InstrumentsApi.md#get_instrument_property_time_series) | **GET** /api/instruments/{identifierType}/{identifier}/properties/time-series | [EARLY ACCESS] GetInstrumentPropertyTimeSeries: Get instrument property time series
[**get_instrument_relationships**](InstrumentsApi.md#get_instrument_relationships) | **GET** /api/instruments/{identifierType}/{identifier}/relationships | [EARLY ACCESS] GetInstrumentRelationships: Get Instrument relationships
[**get_instruments**](InstrumentsApi.md#get_instruments) | **POST** /api/instruments/$get | GetInstruments: Get instruments
[**list_instrument_properties**](InstrumentsApi.md#list_instrument_properties) | **GET** /api/instruments/{identifierType}/{identifier}/properties/list | [EARLY ACCESS] ListInstrumentProperties: Get instrument properties (with Pagination)
[**list_instruments**](InstrumentsApi.md#list_instruments) | **GET** /api/instruments | ListInstruments: List instruments
[**query_instrument_capabilities**](InstrumentsApi.md#query_instrument_capabilities) | **POST** /api/instruments/capabilities | [EXPERIMENTAL] QueryInstrumentCapabilities: Query capabilities of a particular instrument in advance of creating it. These include instrument features, and if model is provided it also includes supported address keys and economic dependencies.
[**update_instrument_identifier**](InstrumentsApi.md#update_instrument_identifier) | **POST** /api/instruments/{identifierType}/{identifier} | UpdateInstrumentIdentifier: Update instrument identifier
[**upsert_instruments**](InstrumentsApi.md#upsert_instruments) | **POST** /api/instruments | UpsertInstruments: Upsert instruments
[**upsert_instruments_properties**](InstrumentsApi.md#upsert_instruments_properties) | **POST** /api/instruments/$upsertproperties | UpsertInstrumentsProperties: Upsert instruments properties


# **delete_instrument**
> DeleteInstrumentResponse delete_instrument(identifier_type, identifier, scope=scope)

[EARLY ACCESS] DeleteInstrument: Soft delete a single instrument

Soft delete a particular instrument, as identified by a particular instrument identifier.                Once deleted, an instrument is marked as inactive and can no longer be referenced when creating or updating  transactions or holdings. You can still query existing transactions and holdings related to the  deleted instrument.

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
    api_instance = lusid.InstrumentsApi(api_client)
    identifier_type = 'identifier_type_example' # str | The unique identifier type to search, for example 'Figi'.
    identifier = 'identifier_example' # str | An <i>identifierType</i> value to use to identify the instrument, for example 'BBG000BLNNV0'.
    scope = 'default' # str | The scope in which the instrument lies. When not supplied the scope is 'default'. (optional) (default to 'default')

    try:
        # [EARLY ACCESS] DeleteInstrument: Soft delete a single instrument
        api_response = await api_instance.delete_instrument(identifier_type, identifier, scope=scope)
        print("The response of InstrumentsApi->delete_instrument:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstrumentsApi->delete_instrument: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier_type** | **str**| The unique identifier type to search, for example &#39;Figi&#39;. | 
 **identifier** | **str**| An &lt;i&gt;identifierType&lt;/i&gt; value to use to identify the instrument, for example &#39;BBG000BLNNV0&#39;. | 
 **scope** | **str**| The scope in which the instrument lies. When not supplied the scope is &#39;default&#39;. | [optional] [default to &#39;default&#39;]

### Return type

[**DeleteInstrumentResponse**](DeleteInstrumentResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the instrument was deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_instrument_properties**
> DeleteInstrumentPropertiesResponse delete_instrument_properties(identifier_type, identifier, request_body, effective_at=effective_at, scope=scope)

[EARLY ACCESS] DeleteInstrumentProperties: Delete instrument properties

Delete one or more properties from a particular instrument. If the properties are time-variant then an effective datetime from which  to delete properties must be specified. If the properties are perpetual then it is invalid to specify an effective datetime for deletion.

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
    api_instance = lusid.InstrumentsApi(api_client)
    identifier_type = 'identifier_type_example' # str | The unique identifier type to search, for example 'Figi'.
    identifier = 'identifier_example' # str | An <i>identifierType</i> value to use to identify the instrument, for example 'BBG000BLNNV0'.
    request_body = ["Instrument/scope/market-sector","Instrument/scope/tenor"] # List[str] | A list of property keys from the 'Instruments' domain whose properties to delete.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to delete time-variant properties from.              The property must exist at the specified 'effectiveAt' datetime. If the 'effectiveAt' is not provided or is              before the time-variant property exists then a failure is returned. Do not specify this parameter if any of              the properties to delete are perpetual. (optional)
    scope = 'default' # str | The scope in which the instrument lies. When not supplied the scope is 'default'. (optional) (default to 'default')

    try:
        # [EARLY ACCESS] DeleteInstrumentProperties: Delete instrument properties
        api_response = await api_instance.delete_instrument_properties(identifier_type, identifier, request_body, effective_at=effective_at, scope=scope)
        print("The response of InstrumentsApi->delete_instrument_properties:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstrumentsApi->delete_instrument_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier_type** | **str**| The unique identifier type to search, for example &#39;Figi&#39;. | 
 **identifier** | **str**| An &lt;i&gt;identifierType&lt;/i&gt; value to use to identify the instrument, for example &#39;BBG000BLNNV0&#39;. | 
 **request_body** | [**List[str]**](str.md)| A list of property keys from the &#39;Instruments&#39; domain whose properties to delete. | 
 **effective_at** | **str**| The effective datetime or cut label at which to delete time-variant properties from.              The property must exist at the specified &#39;effectiveAt&#39; datetime. If the &#39;effectiveAt&#39; is not provided or is              before the time-variant property exists then a failure is returned. Do not specify this parameter if any of              the properties to delete are perpetual. | [optional] 
 **scope** | **str**| The scope in which the instrument lies. When not supplied the scope is &#39;default&#39;. | [optional] [default to &#39;default&#39;]

### Return type

[**DeleteInstrumentPropertiesResponse**](DeleteInstrumentPropertiesResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The asAt datetime at which properties were deleted. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_instruments**
> DeleteInstrumentsResponse delete_instruments(request_body, delete_mode=delete_mode, scope=scope)

[EARLY ACCESS] DeleteInstruments: Soft or hard delete multiple instruments

Deletes a number of instruments identified by LusidInstrumentId.                Soft deletion marks the instrument as inactive so it can no longer be referenced when creating or updating transactions or holdings. You can still query existing transactions and holdings related to the inactive instrument.                In addition to the above behaviour, hard deletion: (i) completely removes all external identifiers from the instrument; (ii) marks the instrument as 'Deleted'; (iii) prepends the instrument's name with 'DELETED '; (iv) prevents the instrument from being returned in list instruments queries.                Following hard deletion, an instrument may only be retrieved by making a direct get instrument request for the LusidInstrumentId. Instrument deletion cannot be undone. Please note that currency instruments cannot currently be deleted.  The maximum number of instruments that this method can delete per request is 2,000.

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
    api_instance = lusid.InstrumentsApi(api_client)
    request_body = ["LUID_12345678","LUID_87654321"] # List[str] | The list of lusidInstrumentId's to delete.
    delete_mode = 'delete_mode_example' # str | The delete mode to use (defaults to 'Soft'). (optional)
    scope = 'default' # str | The scope in which the instruments lie. When not supplied the scope is 'default'. (optional) (default to 'default')

    try:
        # [EARLY ACCESS] DeleteInstruments: Soft or hard delete multiple instruments
        api_response = await api_instance.delete_instruments(request_body, delete_mode=delete_mode, scope=scope)
        print("The response of InstrumentsApi->delete_instruments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstrumentsApi->delete_instruments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)| The list of lusidInstrumentId&#39;s to delete. | 
 **delete_mode** | **str**| The delete mode to use (defaults to &#39;Soft&#39;). | [optional] 
 **scope** | **str**| The scope in which the instruments lie. When not supplied the scope is &#39;default&#39;. | [optional] [default to &#39;default&#39;]

### Return type

[**DeleteInstrumentsResponse**](DeleteInstrumentsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the instruments were deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_possible_features**
> Dict[str, List[str]] get_all_possible_features(instrument_type)

[EXPERIMENTAL] GetAllPossibleFeatures: Provides list of all possible features for instrument type.

Provides all possible instrument features an instrument of a given type can provide.

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
    api_instance = lusid.InstrumentsApi(api_client)
    instrument_type = 'instrument_type_example' # str | A lusid instrument type e.g. Bond, FxOption.

    try:
        # [EXPERIMENTAL] GetAllPossibleFeatures: Provides list of all possible features for instrument type.
        api_response = await api_instance.get_all_possible_features(instrument_type)
        print("The response of InstrumentsApi->get_all_possible_features:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstrumentsApi->get_all_possible_features: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instrument_type** | **str**| A lusid instrument type e.g. Bond, FxOption. | 

### Return type

**Dict[str, List[str]]**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Provides all possible instrument features an instrument of a given type can provide. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_existing_instrument_capabilities**
> InstrumentCapabilities get_existing_instrument_capabilities(identifier, model=model, effective_at=effective_at, as_at=as_at, instrument_scope=instrument_scope, recipe_scope=recipe_scope, recipe_code=recipe_code)

[EXPERIMENTAL] GetExistingInstrumentCapabilities: Retrieve capabilities of an existing instrument identified by LUID. These include instrument features, and if model is provided it also includes supported address keys and economic dependencies.  Given an lusid instrument id provides instrument capabilities, outlining features, and, given the model, the capabilities also include supported addresses as well as economic dependencies.

Returns instrument capabilities containing useful information about the instrument and the model. This includes  - features corresponding to the instrument e.g. Optionality:American, Other:InflationLinked  - supported addresses (if model provided) e.g. Valuation/Pv, Valuation/DirtyPriceKey, Valuation/Accrued  - economic dependencies (if model provided) e.g. Cash:USD, Fx:GBP.USD, Rates:GBP.GBPOIS

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
    api_instance = lusid.InstrumentsApi(api_client)
    identifier = 'identifier_example' # str | A lusid instrument id identifying the instrument.
    model = 'model_example' # str | A pricing model for the instrument. Defaults to Unknown if not specified. If not specified the SupportedAddresses and EconomicDependencies are not provided. (optional)
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve the instrument.              Defaults to the current LUSID system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the instrument. Defaults to              returning the latest version if not specified. (optional)
    instrument_scope = 'default' # str | The scope in which the instrument lies. When not supplied the scope is 'default'. (optional) (default to 'default')
    recipe_scope = 'default' # str | The scope in which the recipe lies. When not supplied the scope is 'default'. (optional) (default to 'default')
    recipe_code = 'recipe_code_example' # str | A unique identifier for an entity, used to obtain configuration recipe details. Default configuration recipe is used if not provided. (optional)

    try:
        # [EXPERIMENTAL] GetExistingInstrumentCapabilities: Retrieve capabilities of an existing instrument identified by LUID. These include instrument features, and if model is provided it also includes supported address keys and economic dependencies.  Given an lusid instrument id provides instrument capabilities, outlining features, and, given the model, the capabilities also include supported addresses as well as economic dependencies.
        api_response = await api_instance.get_existing_instrument_capabilities(identifier, model=model, effective_at=effective_at, as_at=as_at, instrument_scope=instrument_scope, recipe_scope=recipe_scope, recipe_code=recipe_code)
        print("The response of InstrumentsApi->get_existing_instrument_capabilities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstrumentsApi->get_existing_instrument_capabilities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| A lusid instrument id identifying the instrument. | 
 **model** | **str**| A pricing model for the instrument. Defaults to Unknown if not specified. If not specified the SupportedAddresses and EconomicDependencies are not provided. | [optional] 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the instrument.              Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the instrument. Defaults to              returning the latest version if not specified. | [optional] 
 **instrument_scope** | **str**| The scope in which the instrument lies. When not supplied the scope is &#39;default&#39;. | [optional] [default to &#39;default&#39;]
 **recipe_scope** | **str**| The scope in which the recipe lies. When not supplied the scope is &#39;default&#39;. | [optional] [default to &#39;default&#39;]
 **recipe_code** | **str**| A unique identifier for an entity, used to obtain configuration recipe details. Default configuration recipe is used if not provided. | [optional] 

### Return type

[**InstrumentCapabilities**](InstrumentCapabilities.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Capabilities for a given instrument, with more details should the model be provided. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_existing_instrument_models**
> InstrumentModels get_existing_instrument_models(identifier, effective_at=effective_at, as_at=as_at, instrument_scope=instrument_scope, recipe_scope=recipe_scope, recipe_code=recipe_code)

GetExistingInstrumentModels: Retrieve supported pricing models for an existing instrument identified by LUID.

Get the supported pricing models of a single instrument.

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
    api_instance = lusid.InstrumentsApi(api_client)
    identifier = 'identifier_example' # str | A lusid instrument id identifying the instrument.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve the instrument.              Defaults to the current LUSID system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the instrument. Defaults to              returning the latest version if not specified. (optional)
    instrument_scope = 'default' # str | The scope in which the instrument lies. When not supplied the scope is 'default'. (optional) (default to 'default')
    recipe_scope = 'default' # str | The scope in which the recipe lies. When not supplied the scope is 'default'. (optional) (default to 'default')
    recipe_code = 'recipe_code_example' # str | A unique identifier for an entity, used to obtain configuration recipe details. Default configuration recipe is used if not provided. (optional)

    try:
        # GetExistingInstrumentModels: Retrieve supported pricing models for an existing instrument identified by LUID.
        api_response = await api_instance.get_existing_instrument_models(identifier, effective_at=effective_at, as_at=as_at, instrument_scope=instrument_scope, recipe_scope=recipe_scope, recipe_code=recipe_code)
        print("The response of InstrumentsApi->get_existing_instrument_models:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstrumentsApi->get_existing_instrument_models: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| A lusid instrument id identifying the instrument. | 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the instrument.              Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the instrument. Defaults to              returning the latest version if not specified. | [optional] 
 **instrument_scope** | **str**| The scope in which the instrument lies. When not supplied the scope is &#39;default&#39;. | [optional] [default to &#39;default&#39;]
 **recipe_scope** | **str**| The scope in which the recipe lies. When not supplied the scope is &#39;default&#39;. | [optional] [default to &#39;default&#39;]
 **recipe_code** | **str**| A unique identifier for an entity, used to obtain configuration recipe details. Default configuration recipe is used if not provided. | [optional] 

### Return type

[**InstrumentModels**](InstrumentModels.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Models which can be used to value a given instrument. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_instrument**
> Instrument get_instrument(identifier_type, identifier, effective_at=effective_at, as_at=as_at, property_keys=property_keys, scope=scope, relationship_definition_ids=relationship_definition_ids)

GetInstrument: Get instrument

Retrieve the definition of a particular instrument, as identified by a particular unique identifier.

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
    api_instance = lusid.InstrumentsApi(api_client)
    identifier_type = 'identifier_type_example' # str | The unique identifier type to use, for example 'Figi'.
    identifier = 'identifier_example' # str | An <i>identifierType</i> value to use to identify the instrument, for example 'BBG000BLNNV0'.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve the instrument.              Defaults to the current LUSID system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the instrument. Defaults to              returning the latest version if not specified. (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the 'Instrument' domain to decorate onto              the instrument, or from any domain that supports relationships to decorate onto related entities.              These must have the format {domain}/{scope}/{code}, for example 'Instrument/system/Name'. (optional)
    scope = 'default' # str | The scope in which the instrument lies. When not supplied the scope is 'default'. (optional) (default to 'default')
    relationship_definition_ids = ['relationship_definition_ids_example'] # List[str] | A list of relationship definitions that are used to decorate related entities              onto the instrument in the response. These must take the form {relationshipDefinitionScope}/{relationshipDefinitionCode}. (optional)

    try:
        # GetInstrument: Get instrument
        api_response = await api_instance.get_instrument(identifier_type, identifier, effective_at=effective_at, as_at=as_at, property_keys=property_keys, scope=scope, relationship_definition_ids=relationship_definition_ids)
        print("The response of InstrumentsApi->get_instrument:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstrumentsApi->get_instrument: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier_type** | **str**| The unique identifier type to use, for example &#39;Figi&#39;. | 
 **identifier** | **str**| An &lt;i&gt;identifierType&lt;/i&gt; value to use to identify the instrument, for example &#39;BBG000BLNNV0&#39;. | 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the instrument.              Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the instrument. Defaults to              returning the latest version if not specified. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;Instrument&#39; domain to decorate onto              the instrument, or from any domain that supports relationships to decorate onto related entities.              These must have the format {domain}/{scope}/{code}, for example &#39;Instrument/system/Name&#39;. | [optional] 
 **scope** | **str**| The scope in which the instrument lies. When not supplied the scope is &#39;default&#39;. | [optional] [default to &#39;default&#39;]
 **relationship_definition_ids** | [**List[str]**](str.md)| A list of relationship definitions that are used to decorate related entities              onto the instrument in the response. These must take the form {relationshipDefinitionScope}/{relationshipDefinitionCode}. | [optional] 

### Return type

[**Instrument**](Instrument.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested instrument. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_instrument_identifier_types**
> ResourceListOfInstrumentIdTypeDescriptor get_instrument_identifier_types()

GetInstrumentIdentifierTypes: Get instrument identifier types

Retrieve a list of all valid instrument identifier types and whether they are unique or not.                An instrument must have a value for at least one unique identifier type (it can have more than one unique type and value).  In addition, a value is automatically generated for a LUSID Instrument ID (LUID) unique type by the system.                An instrument can have values for multiple non-unique identifier types (or it can have zero non-unique types and values).

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
    api_instance = lusid.InstrumentsApi(api_client)

    try:
        # GetInstrumentIdentifierTypes: Get instrument identifier types
        api_response = await api_instance.get_instrument_identifier_types()
        print("The response of InstrumentsApi->get_instrument_identifier_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstrumentsApi->get_instrument_identifier_types: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResourceListOfInstrumentIdTypeDescriptor**](ResourceListOfInstrumentIdTypeDescriptor.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of valid instrument identifier types. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_instrument_payment_diary**
> InstrumentPaymentDiary get_instrument_payment_diary(identifier_type, identifier, recipe_scope, recipe_code, effective_at=effective_at, as_at=as_at, scope=scope)

[EXPERIMENTAL] GetInstrumentPaymentDiary: Get instrument payment diary

Get the payment diary of a single instrument.

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
    api_instance = lusid.InstrumentsApi(api_client)
    identifier_type = 'identifier_type_example' # str | The identifier being supplied e.g. \"Figi\".
    identifier = 'identifier_example' # str | The value of the identifier for the requested instrument.
    recipe_scope = 'recipe_scope_example' # str | The scope of the valuation recipe being used to generate the payment diary
    recipe_code = 'recipe_code_example' # str | The code of the valuation recipe being used to generate the payment diary
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to list the instrument's properties. Defaults to the current LUSID system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the instrument's properties. Defaults to return the latest version of each property if not specified. (optional)
    scope = 'default' # str | The scope in which the instrument lies. When not supplied the scope is 'default'. (optional) (default to 'default')

    try:
        # [EXPERIMENTAL] GetInstrumentPaymentDiary: Get instrument payment diary
        api_response = await api_instance.get_instrument_payment_diary(identifier_type, identifier, recipe_scope, recipe_code, effective_at=effective_at, as_at=as_at, scope=scope)
        print("The response of InstrumentsApi->get_instrument_payment_diary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstrumentsApi->get_instrument_payment_diary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier_type** | **str**| The identifier being supplied e.g. \&quot;Figi\&quot;. | 
 **identifier** | **str**| The value of the identifier for the requested instrument. | 
 **recipe_scope** | **str**| The scope of the valuation recipe being used to generate the payment diary | 
 **recipe_code** | **str**| The code of the valuation recipe being used to generate the payment diary | 
 **effective_at** | **str**| The effective datetime or cut label at which to list the instrument&#39;s properties. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the instrument&#39;s properties. Defaults to return the latest version of each property if not specified. | [optional] 
 **scope** | **str**| The scope in which the instrument lies. When not supplied the scope is &#39;default&#39;. | [optional] [default to &#39;default&#39;]

### Return type

[**InstrumentPaymentDiary**](InstrumentPaymentDiary.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The payment diary of the specified instrument |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_instrument_properties**
> InstrumentProperties get_instrument_properties(identifier_type, identifier, effective_at=effective_at, as_at=as_at, scope=scope)

[EARLY ACCESS] GetInstrumentProperties: Get instrument properties

List all the properties of a particular instrument, as identified by a particular unique identifier.

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
    api_instance = lusid.InstrumentsApi(api_client)
    identifier_type = 'identifier_type_example' # str | The unique identifier type to search, for example 'Figi'.
    identifier = 'identifier_example' # str | An <i>identifierType</i> value to use to identify the instrument, for example 'BBG000BLNNV0'.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to list the instrument's properties.              Defaults to the current LUSID system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the instrument's properties. Defaults to returning              the latest version of each property if not specified. (optional)
    scope = 'default' # str | The scope in which the instrument lies. When not supplied the scope is 'default'. (optional) (default to 'default')

    try:
        # [EARLY ACCESS] GetInstrumentProperties: Get instrument properties
        api_response = await api_instance.get_instrument_properties(identifier_type, identifier, effective_at=effective_at, as_at=as_at, scope=scope)
        print("The response of InstrumentsApi->get_instrument_properties:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstrumentsApi->get_instrument_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier_type** | **str**| The unique identifier type to search, for example &#39;Figi&#39;. | 
 **identifier** | **str**| An &lt;i&gt;identifierType&lt;/i&gt; value to use to identify the instrument, for example &#39;BBG000BLNNV0&#39;. | 
 **effective_at** | **str**| The effective datetime or cut label at which to list the instrument&#39;s properties.              Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the instrument&#39;s properties. Defaults to returning              the latest version of each property if not specified. | [optional] 
 **scope** | **str**| The scope in which the instrument lies. When not supplied the scope is &#39;default&#39;. | [optional] [default to &#39;default&#39;]

### Return type

[**InstrumentProperties**](InstrumentProperties.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The properties of the specified instrument |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_instrument_property_time_series**
> ResourceListOfPropertyInterval get_instrument_property_time_series(identifier_type, identifier, property_key, identifier_effective_at=identifier_effective_at, as_at=as_at, filter=filter, page=page, limit=limit, scope=scope)

[EARLY ACCESS] GetInstrumentPropertyTimeSeries: Get instrument property time series

Retrieve the complete time series (history) for a particular property of an instrument.

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
    api_instance = lusid.InstrumentsApi(api_client)
    identifier_type = 'identifier_type_example' # str | The unique identifier type to search, for example 'Figi'.
    identifier = 'identifier_example' # str | An <i>identifierType</i> value to use to identify the instrument, for example 'BBG000BLNNV0'.
    property_key = 'property_key_example' # str | The property key of a property from the 'Instrument' domain whose history to retrieve.              This must have the format {domain}/{scope}/{code}, for example 'Instrument/system/Name'.
    identifier_effective_at = 'identifier_effective_at_example' # str | The effective datetime used to resolve the instrument from the identifier.              Defaults to the current LUSID system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the instrument's property history. Defaults to              returning the current datetime if not supplied. (optional)
    filter = 'filter_example' # str | Expression to filter the results. For more information about filtering,              see https://support.lusid.com/knowledgebase/article/KA-01914. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing properties; this value is returned from              the previous call. If a pagination token is provided, the <i>filter</i>, <i>effectiveAt</i> and              <i>asAt</i> fields must not have changed since the original request. For more information, see              https://support.lusid.com/knowledgebase/article/KA-01915. (optional)
    limit = 56 # int | When paginating, limit the results to this number. (optional)
    scope = 'default' # str | The scope in which the instrument lies. When not supplied the scope is 'default'. (optional) (default to 'default')

    try:
        # [EARLY ACCESS] GetInstrumentPropertyTimeSeries: Get instrument property time series
        api_response = await api_instance.get_instrument_property_time_series(identifier_type, identifier, property_key, identifier_effective_at=identifier_effective_at, as_at=as_at, filter=filter, page=page, limit=limit, scope=scope)
        print("The response of InstrumentsApi->get_instrument_property_time_series:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstrumentsApi->get_instrument_property_time_series: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier_type** | **str**| The unique identifier type to search, for example &#39;Figi&#39;. | 
 **identifier** | **str**| An &lt;i&gt;identifierType&lt;/i&gt; value to use to identify the instrument, for example &#39;BBG000BLNNV0&#39;. | 
 **property_key** | **str**| The property key of a property from the &#39;Instrument&#39; domain whose history to retrieve.              This must have the format {domain}/{scope}/{code}, for example &#39;Instrument/system/Name&#39;. | 
 **identifier_effective_at** | **str**| The effective datetime used to resolve the instrument from the identifier.              Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the instrument&#39;s property history. Defaults to              returning the current datetime if not supplied. | [optional] 
 **filter** | **str**| Expression to filter the results. For more information about filtering,              see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **page** | **str**| The pagination token to use to continue listing properties; this value is returned from              the previous call. If a pagination token is provided, the &lt;i&gt;filter&lt;/i&gt;, &lt;i&gt;effectiveAt&lt;/i&gt; and              &lt;i&gt;asAt&lt;/i&gt; fields must not have changed since the original request. For more information, see              https://support.lusid.com/knowledgebase/article/KA-01915. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. | [optional] 
 **scope** | **str**| The scope in which the instrument lies. When not supplied the scope is &#39;default&#39;. | [optional] [default to &#39;default&#39;]

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

# **get_instrument_relationships**
> ResourceListOfRelationship get_instrument_relationships(identifier_type, identifier, effective_at=effective_at, as_at=as_at, filter=filter, identifier_types=identifier_types, scope=scope)

[EARLY ACCESS] GetInstrumentRelationships: Get Instrument relationships

Get relationships for a particular Instrument.

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
    api_instance = lusid.InstrumentsApi(api_client)
    identifier_type = 'identifier_type_example' # str | An identifier type attached to the Instrument.
    identifier = 'identifier_example' # str | The identifier value.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to get relationships. Defaults to the current LUSID system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve relationships. Defaults to return the latest LUSID AsAt time if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter relationships. Users should provide null or empty string for this field until further notice. (optional)
    identifier_types = ['identifier_types_example'] # List[str] | Identifier types (as property keys) used for referencing Persons or Legal Entities.              These can be specified from the 'Person' or 'LegalEntity' domains and have the format {domain}/{scope}/{code}, for example              'Person/CompanyDetails/Role'. An Empty array may be used to return all related Entities. (optional)
    scope = 'default' # str | The entity scope in which the instrument lies. When not supplied the scope is 'default'. (optional) (default to 'default')

    try:
        # [EARLY ACCESS] GetInstrumentRelationships: Get Instrument relationships
        api_response = await api_instance.get_instrument_relationships(identifier_type, identifier, effective_at=effective_at, as_at=as_at, filter=filter, identifier_types=identifier_types, scope=scope)
        print("The response of InstrumentsApi->get_instrument_relationships:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstrumentsApi->get_instrument_relationships: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier_type** | **str**| An identifier type attached to the Instrument. | 
 **identifier** | **str**| The identifier value. | 
 **effective_at** | **str**| The effective datetime or cut label at which to get relationships. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve relationships. Defaults to return the latest LUSID AsAt time if not specified. | [optional] 
 **filter** | **str**| Expression to filter relationships. Users should provide null or empty string for this field until further notice. | [optional] 
 **identifier_types** | [**List[str]**](str.md)| Identifier types (as property keys) used for referencing Persons or Legal Entities.              These can be specified from the &#39;Person&#39; or &#39;LegalEntity&#39; domains and have the format {domain}/{scope}/{code}, for example              &#39;Person/CompanyDetails/Role&#39;. An Empty array may be used to return all related Entities. | [optional] 
 **scope** | **str**| The entity scope in which the instrument lies. When not supplied the scope is &#39;default&#39;. | [optional] [default to &#39;default&#39;]

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
**200** | The relationships for the specified instrument. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_instruments**
> GetInstrumentsResponse get_instruments(identifier_type, request_body, effective_at=effective_at, as_at=as_at, property_keys=property_keys, scope=scope, relationship_definition_ids=relationship_definition_ids)

GetInstruments: Get instruments

Retrieve the definition of one or more instruments, as identified by a collection of unique identifiers.                Note that to retrieve all the instruments in the instrument master, use the List instruments endpoint instead.

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
    api_instance = lusid.InstrumentsApi(api_client)
    identifier_type = 'identifier_type_example' # str | The unique identifier type to use, for example 'Figi'.
    request_body = ["instrument-identifier-1","instrument-identifier-2"] # List[str] | A list of one or more <i>identifierType</i> values to use to identify instruments.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve the instrument definitions.               Defaults to the current LUSID system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the instrument definitions.               Defaults to returning the latest version of each instrument definition if not specified. (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the 'Instrument' domain to decorate onto               each instrument, or from any domain that supports relationships to decorate onto related entities.               These must have the format {domain}/{scope}/{code}, for example 'Instrument/system/Name'. (optional)
    scope = 'default' # str | The scope in which the instrument lies. When not supplied the scope is 'default'. (optional) (default to 'default')
    relationship_definition_ids = ['relationship_definition_ids_example'] # List[str] | A list of relationship definitions that are used to decorate related entities               onto each instrument in the response. These must take the form {relationshipDefinitionScope}/{relationshipDefinitionCode}. (optional)

    try:
        # GetInstruments: Get instruments
        api_response = await api_instance.get_instruments(identifier_type, request_body, effective_at=effective_at, as_at=as_at, property_keys=property_keys, scope=scope, relationship_definition_ids=relationship_definition_ids)
        print("The response of InstrumentsApi->get_instruments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstrumentsApi->get_instruments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier_type** | **str**| The unique identifier type to use, for example &#39;Figi&#39;. | 
 **request_body** | [**List[str]**](str.md)| A list of one or more &lt;i&gt;identifierType&lt;/i&gt; values to use to identify instruments. | 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the instrument definitions.               Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the instrument definitions.               Defaults to returning the latest version of each instrument definition if not specified. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;Instrument&#39; domain to decorate onto               each instrument, or from any domain that supports relationships to decorate onto related entities.               These must have the format {domain}/{scope}/{code}, for example &#39;Instrument/system/Name&#39;. | [optional] 
 **scope** | **str**| The scope in which the instrument lies. When not supplied the scope is &#39;default&#39;. | [optional] [default to &#39;default&#39;]
 **relationship_definition_ids** | [**List[str]**](str.md)| A list of relationship definitions that are used to decorate related entities               onto each instrument in the response. These must take the form {relationshipDefinitionScope}/{relationshipDefinitionCode}. | [optional] 

### Return type

[**GetInstrumentsResponse**](GetInstrumentsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested instruments which could be identified along with any failures |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_instrument_properties**
> ResourceListOfProperty list_instrument_properties(identifier_type, identifier, effective_at=effective_at, as_at=as_at, page=page, limit=limit, scope=scope)

[EARLY ACCESS] ListInstrumentProperties: Get instrument properties (with Pagination)

List all the properties of a particular instrument, as identified by a particular unique identifier.

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
    api_instance = lusid.InstrumentsApi(api_client)
    identifier_type = 'identifier_type_example' # str | The unique identifier type to search, for example 'Figi'.
    identifier = 'identifier_example' # str | An <i>identifierType</i> value to use to identify the instrument, for example 'BBG000BLNNV0'.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to list the instrument's properties.              Defaults to the current LUSID system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the instrument's properties. Defaults to returning              the latest version of each property if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing commands; this value is returned from the previous call. (optional)
    limit = 56 # int | When paginating, limit the results per page to this number. (optional)
    scope = 'default' # str | The scope in which the instrument lies. When not supplied the scope is 'default'. (optional) (default to 'default')

    try:
        # [EARLY ACCESS] ListInstrumentProperties: Get instrument properties (with Pagination)
        api_response = await api_instance.list_instrument_properties(identifier_type, identifier, effective_at=effective_at, as_at=as_at, page=page, limit=limit, scope=scope)
        print("The response of InstrumentsApi->list_instrument_properties:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstrumentsApi->list_instrument_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier_type** | **str**| The unique identifier type to search, for example &#39;Figi&#39;. | 
 **identifier** | **str**| An &lt;i&gt;identifierType&lt;/i&gt; value to use to identify the instrument, for example &#39;BBG000BLNNV0&#39;. | 
 **effective_at** | **str**| The effective datetime or cut label at which to list the instrument&#39;s properties.              Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the instrument&#39;s properties. Defaults to returning              the latest version of each property if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing commands; this value is returned from the previous call. | [optional] 
 **limit** | **int**| When paginating, limit the results per page to this number. | [optional] 
 **scope** | **str**| The scope in which the instrument lies. When not supplied the scope is &#39;default&#39;. | [optional] [default to &#39;default&#39;]

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
**200** | The properties of the specified instrument |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_instruments**
> PagedResourceListOfInstrument list_instruments(as_at=as_at, effective_at=effective_at, page=page, sort_by=sort_by, start=start, limit=limit, filter=filter, instrument_property_keys=instrument_property_keys, scope=scope, relationship_definition_ids=relationship_definition_ids)

ListInstruments: List instruments

List all the instruments in the instrument master.                To retrieve a particular set of instruments instead, use the Get instruments endpoint.  The maximum number of instruments that this method can list per request is 2,000.

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
    api_instance = lusid.InstrumentsApi(api_client)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list instruments. Defaults to returning the latest               version of each instrument if not specified. (optional)
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to list instruments.               Defaults to the current LUSID system datetime if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing instruments; this value is returned from               the previous call. If a pagination token is provided, the <i>sortBy</i>, <i>filter</i>, <i>effectiveAt</i> and               <i>asAt</i> fields must not have changed since the original request. Also, a <i>start</i> value cannot be               provided. For more information, see https://support.lusid.com/knowledgebase/article/KA-01915. (optional)
    sort_by = ['sort_by_example'] # List[str] | Order results by particular fields. Use the '-' sign to denote descending order, for               example '-MyFieldName'. (optional)
    start = 56 # int | When paginating, skip this number of results. (optional)
    limit = 56 # int | When paginating, limit the results to this number. (optional)
    filter = 'State eq 'Active'' # str | Expression to filter the result set. Defaults to filtering out inactive instruments               (that is, those that have been deleted). For more information about filtering results,               see https://support.lusid.com/knowledgebase/article/KA-01914. (optional) (default to 'State eq 'Active'')
    instrument_property_keys = ['instrument_property_keys_example'] # List[str] | A list of property keys from the 'Instrument' domain to decorate onto               instruments, or from any domain that supports relationships to decorate onto related entities.               These must have the format {domain}/{scope}/{code}, for example 'Instrument/system/Name'. (optional)
    scope = 'default' # str | The scope in which the instrument lies. When not supplied the scope is 'default'. (optional) (default to 'default')
    relationship_definition_ids = ['relationship_definition_ids_example'] # List[str] | A list of relationship definitions that are used to decorate related entities               onto each instrument in the response. These must take the form {relationshipDefinitionScope}/{relationshipDefinitionCode}. (optional)

    try:
        # ListInstruments: List instruments
        api_response = await api_instance.list_instruments(as_at=as_at, effective_at=effective_at, page=page, sort_by=sort_by, start=start, limit=limit, filter=filter, instrument_property_keys=instrument_property_keys, scope=scope, relationship_definition_ids=relationship_definition_ids)
        print("The response of InstrumentsApi->list_instruments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstrumentsApi->list_instruments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list instruments. Defaults to returning the latest               version of each instrument if not specified. | [optional] 
 **effective_at** | **str**| The effective datetime or cut label at which to list instruments.               Defaults to the current LUSID system datetime if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing instruments; this value is returned from               the previous call. If a pagination token is provided, the &lt;i&gt;sortBy&lt;/i&gt;, &lt;i&gt;filter&lt;/i&gt;, &lt;i&gt;effectiveAt&lt;/i&gt; and               &lt;i&gt;asAt&lt;/i&gt; fields must not have changed since the original request. Also, a &lt;i&gt;start&lt;/i&gt; value cannot be               provided. For more information, see https://support.lusid.com/knowledgebase/article/KA-01915. | [optional] 
 **sort_by** | [**List[str]**](str.md)| Order results by particular fields. Use the &#39;-&#39; sign to denote descending order, for               example &#39;-MyFieldName&#39;. | [optional] 
 **start** | **int**| When paginating, skip this number of results. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. | [optional] 
 **filter** | **str**| Expression to filter the result set. Defaults to filtering out inactive instruments               (that is, those that have been deleted). For more information about filtering results,               see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] [default to &#39;State eq &#39;Active&#39;&#39;]
 **instrument_property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;Instrument&#39; domain to decorate onto               instruments, or from any domain that supports relationships to decorate onto related entities.               These must have the format {domain}/{scope}/{code}, for example &#39;Instrument/system/Name&#39;. | [optional] 
 **scope** | **str**| The scope in which the instrument lies. When not supplied the scope is &#39;default&#39;. | [optional] [default to &#39;default&#39;]
 **relationship_definition_ids** | [**List[str]**](str.md)| A list of relationship definitions that are used to decorate related entities               onto each instrument in the response. These must take the form {relationshipDefinitionScope}/{relationshipDefinitionCode}. | [optional] 

### Return type

[**PagedResourceListOfInstrument**](PagedResourceListOfInstrument.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested instruments |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_instrument_capabilities**
> InstrumentCapabilities query_instrument_capabilities(lusid_instrument, model=model)

[EXPERIMENTAL] QueryInstrumentCapabilities: Query capabilities of a particular instrument in advance of creating it. These include instrument features, and if model is provided it also includes supported address keys and economic dependencies.

Returns instrument capabilities containing useful information about the instrument and the model. This includes  - features corresponding to the instrument e.g. Optionality:American, Other:InflationLinked  - supported addresses (if model provided) e.g. Valuation/Pv, Valuation/DirtyPriceKey, Valuation/Accrued  - economic dependencies (if model provided) e.g. Cash:USD, Fx:GBP.USD, Rates:GBP.GBPOIS

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
    api_instance = lusid.InstrumentsApi(api_client)
    lusid_instrument = {"startDate":"2022-01-01T05:10:00.0000000+00:00","domCcy":"GBP","domAmount":1,"fgnCcy":"USD","strike":1,"barriers":[],"exerciseType":"European","isCallNotPut":true,"isDeliveryNotCash":true,"isPayoffDigital":false,"optionMaturityDate":"2023-01-01T05:10:00.0000000+00:00","optionSettlementDate":"2023-01-03T05:10:00.0000000+00:00","payoutStyle":"None","touches":[],"instrumentType":"FxOption"} # LusidInstrument | The definition of the instrument.
    model = 'model_example' # str | A pricing model for the instrument. Defaults to Unknown if not specified. If not specified the SupportedAddresses and EconomicDependencies are not provided. (optional)

    try:
        # [EXPERIMENTAL] QueryInstrumentCapabilities: Query capabilities of a particular instrument in advance of creating it. These include instrument features, and if model is provided it also includes supported address keys and economic dependencies.
        api_response = await api_instance.query_instrument_capabilities(lusid_instrument, model=model)
        print("The response of InstrumentsApi->query_instrument_capabilities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstrumentsApi->query_instrument_capabilities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lusid_instrument** | [**LusidInstrument**](LusidInstrument.md)| The definition of the instrument. | 
 **model** | **str**| A pricing model for the instrument. Defaults to Unknown if not specified. If not specified the SupportedAddresses and EconomicDependencies are not provided. | [optional] 

### Return type

[**InstrumentCapabilities**](InstrumentCapabilities.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Capabilities for a given instrument, with more details should the model be provided. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_instrument_identifier**
> Instrument update_instrument_identifier(identifier_type, identifier, update_instrument_identifier_request, scope=scope)

UpdateInstrumentIdentifier: Update instrument identifier

Create, update or delete a particular instrument identifier for an instrument.                To delete the identifier, leave the value unspecified in the request. If not being deleted, the  identifier is updated if it exists and created if it does not.

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
    api_instance = lusid.InstrumentsApi(api_client)
    identifier_type = 'identifier_type_example' # str | The unique identifier type to search, for example 'Figi'.
    identifier = 'identifier_example' # str | An <i>identifierType</i> value to use to identify the instrument, for example 'BBG000BLNNV0'.
    update_instrument_identifier_request = {"type":"Figi","value":"updated-figi","effectiveAt":"2018-02-01T10:00:00.0000000+00:00"} # UpdateInstrumentIdentifierRequest | The identifier to update or delete. This need not be the same value as the               'identifier' parameter used to retrieve the instrument.
    scope = 'default' # str | The scope in which the instrument lies. When not supplied the scope is 'default'. (optional) (default to 'default')

    try:
        # UpdateInstrumentIdentifier: Update instrument identifier
        api_response = await api_instance.update_instrument_identifier(identifier_type, identifier, update_instrument_identifier_request, scope=scope)
        print("The response of InstrumentsApi->update_instrument_identifier:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstrumentsApi->update_instrument_identifier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier_type** | **str**| The unique identifier type to search, for example &#39;Figi&#39;. | 
 **identifier** | **str**| An &lt;i&gt;identifierType&lt;/i&gt; value to use to identify the instrument, for example &#39;BBG000BLNNV0&#39;. | 
 **update_instrument_identifier_request** | [**UpdateInstrumentIdentifierRequest**](UpdateInstrumentIdentifierRequest.md)| The identifier to update or delete. This need not be the same value as the               &#39;identifier&#39; parameter used to retrieve the instrument. | 
 **scope** | **str**| The scope in which the instrument lies. When not supplied the scope is &#39;default&#39;. | [optional] [default to &#39;default&#39;]

### Return type

[**Instrument**](Instrument.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated instrument definition with the identifier created, updated or deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_instruments**
> UpsertInstrumentsResponse upsert_instruments(request_body, scope=scope)

UpsertInstruments: Upsert instruments

Create or update one or more instruments in the instrument master. An instrument is updated  if it already exists and created if it does not.                In the request, each instrument definition should be keyed by a unique correlation ID. This ID is ephemeral  and not stored by LUSID. It serves only to easily identify each instrument in the response.                Note that an instrument must have at least one unique identifier, which is a combination of a type  (such as 'Figi') and a value (such as 'BBG000BS1N49'). In addition, a random value is automatically  generated for a LUSID Instrument ID (LUID) unique type by the system. For more information, see  https://support.lusid.com/knowledgebase/article/KA-01862.                The response returns both the collection of successfully created or updated instruments, as well as those  that failed. For each failure, a reason is provided. It is important to check the failed set for  unsuccessful results.  The maximum number of instruments that this method can upsert per request is 2,000.

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
    api_instance = lusid.InstrumentsApi(api_client)
    request_body = {"request_id_1":{"name":"Instrument name","identifiers":{"ClientInternal":{"value":"some-identifier","effectiveAt":"0001-01-01T00:00:00.0000000+00:00"},"Figi":{"value":"some-figi-code","effectiveAt":"0001-01-01T00:00:00.0000000+00:00"},"Isin":{"value":"some-isin-code","effectiveAt":"0001-01-01T00:00:00.0000000+00:00"}},"properties":[{"key":"Instrument/someScope/somePropertyName","value":{"labelValue":"some-property-value"},"effectiveFrom":"2018-06-18T09:00:00.0000000+00:00"}],"lookThroughPortfolioId":{"scope":"MyScope","code":"portfolio-code"},"definition":{"instrumentFormat":{"sourceSystem":"systemA","vendor":"Unknown","version":"1.0.0"},"content":"{\"some-key\": \"some-value\"}","instrumentType":"ExoticInstrument"}},"request_id_2":{"name":"Instrument name","identifiers":{"ClientInternal":{"value":"some-identifier-2","effectiveAt":"0001-01-01T00:00:00.0000000+00:00"},"Figi":{"value":"some-figi-code-2","effectiveAt":"0001-01-01T00:00:00.0000000+00:00"}},"properties":[],"lookThroughPortfolioId":{"scope":"MyScope","code":"portfolio-code"},"definition":{"instrumentFormat":{"sourceSystem":"systemA","vendor":"Unknown","version":"1.0.0"},"content":"{\"some-key\": \"some-value\"}","instrumentType":"ExoticInstrument"}}} # Dict[str, InstrumentDefinition] | The definitions of the instruments to create or update.
    scope = 'default' # str | The scope in which the instrument lies. When not supplied the scope is 'default'. (optional) (default to 'default')

    try:
        # UpsertInstruments: Upsert instruments
        api_response = await api_instance.upsert_instruments(request_body, scope=scope)
        print("The response of InstrumentsApi->upsert_instruments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstrumentsApi->upsert_instruments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, InstrumentDefinition]**](InstrumentDefinition.md)| The definitions of the instruments to create or update. | 
 **scope** | **str**| The scope in which the instrument lies. When not supplied the scope is &#39;default&#39;. | [optional] [default to &#39;default&#39;]

### Return type

[**UpsertInstrumentsResponse**](UpsertInstrumentsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The successfully created or updated instruments along with any failures |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_instruments_properties**
> UpsertInstrumentPropertiesResponse upsert_instruments_properties(upsert_instrument_property_request, scope=scope)

UpsertInstrumentsProperties: Upsert instruments properties

Create or update one or more properties for particular instruments.                Each instrument property is updated if it exists and created if it does not. For any failures, a reason  is provided.                Properties have an <i>effectiveFrom</i> datetime from which the property is valid, and an <i>effectiveUntil</i>  datetime until which the property is valid. Not supplying an <i>effectiveUntil</i> datetime results in the property being  valid indefinitely, or until the next <i>effectiveFrom</i> datetime of the property.

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
    api_instance = lusid.InstrumentsApi(api_client)
    upsert_instrument_property_request = [{"identifierType":"LusidInstrumentId","identifier":"LUID_00000000","properties":[{"key":"Instrument/MyScope/SomePropertyName","value":{"labelValue":"SomeValue1"},"effectiveFrom":"2016-09-15T12:00:00.0000000+00:00"},{"key":"Instrument/MyScope/SomePropertyName","value":{"labelValue":"SomeValue2"},"effectiveFrom":"2017-08-10T12:00:00.0000000+00:00"},{"key":"Instrument/MyScope/AnotherPropertyName","value":{"labelValue":"AnotherValue1"},"effectiveFrom":"2018-03-05T12:00:00.0000000+00:00","effectiveUntil":"2019-06-01T12:00:00.0000000+00:00"},{"key":"Instrument/MyScope/AnotherPropertyName","value":{"labelValue":"AnotherValue2"},"effectiveFrom":"2020-03-15T12:00:00.0000000+00:00","effectiveUntil":"2021-01-15T12:00:00.0000000+00:00"}]}] # List[UpsertInstrumentPropertyRequest] | A list of instruments and associated instrument properties to create or update.
    scope = 'default' # str | The scope in which the instrument lies. When not supplied the scope is 'default'. (optional) (default to 'default')

    try:
        # UpsertInstrumentsProperties: Upsert instruments properties
        api_response = await api_instance.upsert_instruments_properties(upsert_instrument_property_request, scope=scope)
        print("The response of InstrumentsApi->upsert_instruments_properties:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstrumentsApi->upsert_instruments_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_instrument_property_request** | [**List[UpsertInstrumentPropertyRequest]**](UpsertInstrumentPropertyRequest.md)| A list of instruments and associated instrument properties to create or update. | 
 **scope** | **str**| The scope in which the instrument lies. When not supplied the scope is &#39;default&#39;. | [optional] [default to &#39;default&#39;]

### Return type

[**UpsertInstrumentPropertiesResponse**](UpsertInstrumentPropertiesResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The asAt datetime at which the properties were created or updated. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

