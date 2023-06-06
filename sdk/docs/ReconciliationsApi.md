# lusid.ReconciliationsApi

All URIs are relative to *https://fbn-ci.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_scheduled_reconciliation**](ReconciliationsApi.md#create_scheduled_reconciliation) | **POST** /api/portfolios/$scheduledReconciliations/{scope} | [EXPERIMENTAL] CreateScheduledReconciliation: Create a scheduled reconciliation
[**delete_reconciliation**](ReconciliationsApi.md#delete_reconciliation) | **DELETE** /api/portfolios/$scheduledReconciliations/{scope}/{code} | [EXPERIMENTAL] DeleteReconciliation: Delete scheduled reconciliation
[**delete_reconciliation_break**](ReconciliationsApi.md#delete_reconciliation_break) | **DELETE** /api/portfolios/$scheduledReconciliations/{scope}/{code}/runs/{runDate}/{version}/breaks/{breakId} | [EXPERIMENTAL] DeleteReconciliationBreak: Delete reconciliation break
[**delete_reconciliation_mapping**](ReconciliationsApi.md#delete_reconciliation_mapping) | **DELETE** /api/portfolios/mapping/{scope}/{code} | [EARLY ACCESS] DeleteReconciliationMapping: Delete a mapping
[**delete_reconciliation_run**](ReconciliationsApi.md#delete_reconciliation_run) | **DELETE** /api/portfolios/$scheduledReconciliations/{scope}/{code}/runs/{runDate}/{version} | [EXPERIMENTAL] DeleteReconciliationRun: Delete reconciliation run
[**get_reconciliation**](ReconciliationsApi.md#get_reconciliation) | **GET** /api/portfolios/$scheduledReconciliations/{scope}/{code} | [EXPERIMENTAL] GetReconciliation: Get scheduled reconciliation
[**get_reconciliation_break**](ReconciliationsApi.md#get_reconciliation_break) | **GET** /api/portfolios/$scheduledReconciliations/{scope}/{code}/runs/{runDate}/{version}/breaks/{breakId} | [EXPERIMENTAL] GetReconciliationBreak: Get reconciliation break
[**get_reconciliation_mapping**](ReconciliationsApi.md#get_reconciliation_mapping) | **GET** /api/portfolios/mapping/{scope}/{code} | [EARLY ACCESS] GetReconciliationMapping: Get a mapping
[**get_reconciliation_run**](ReconciliationsApi.md#get_reconciliation_run) | **GET** /api/portfolios/$scheduledReconciliations/{scope}/{code}/runs/{runDate}/{version} | [EXPERIMENTAL] GetReconciliationRun: Get a reconciliation run
[**list_reconciliation_breaks**](ReconciliationsApi.md#list_reconciliation_breaks) | **GET** /api/portfolios/$scheduledReconciliations/{scope}/{code}/runs/{runDate}/{version}/breaks | [EXPERIMENTAL] ListReconciliationBreaks: List reconciliation breaks
[**list_reconciliation_mappings**](ReconciliationsApi.md#list_reconciliation_mappings) | **GET** /api/portfolios/mapping | [EARLY ACCESS] ListReconciliationMappings: List the reconciliation mappings
[**list_reconciliation_runs**](ReconciliationsApi.md#list_reconciliation_runs) | **GET** /api/portfolios/$scheduledReconciliations/{scope}/{code}/runs | [EXPERIMENTAL] ListReconciliationRuns: List Reconciliation runs
[**list_reconciliations**](ReconciliationsApi.md#list_reconciliations) | **GET** /api/portfolios/$scheduledReconciliations | [EXPERIMENTAL] ListReconciliations: List scheduled reconciliations
[**reconcile_generic**](ReconciliationsApi.md#reconcile_generic) | **POST** /api/portfolios/$reconcileGeneric | ReconcileGeneric: Reconcile either holdings or valuations performed on one or two sets of holdings using one or two configuration recipes.                The output is configurable for various types of comparisons, to allow tolerances on numerical and date-time data or case-insensitivity on strings,  and elision of resulting differences where they are &#39;empty&#39; or null or zero.
[**reconcile_holdings**](ReconciliationsApi.md#reconcile_holdings) | **POST** /api/portfolios/$reconcileholdings | [EARLY ACCESS] ReconcileHoldings: Reconcile portfolio holdings
[**reconcile_inline**](ReconciliationsApi.md#reconcile_inline) | **POST** /api/portfolios/$reconcileInline | ReconcileInline: Reconcile valuations performed on one or two sets of inline instruments using one or two configuration recipes.
[**reconcile_transactions**](ReconciliationsApi.md#reconcile_transactions) | **POST** /api/portfolios/$reconcileTransactions | [EARLY ACCESS] ReconcileTransactions: Perform a Transactions Reconciliation.
[**reconcile_valuation**](ReconciliationsApi.md#reconcile_valuation) | **POST** /api/portfolios/$reconcileValuation | ReconcileValuation: Reconcile valuations performed on one or two sets of holdings using one or two configuration recipes.
[**update_reconciliation**](ReconciliationsApi.md#update_reconciliation) | **POST** /api/portfolios/$scheduledReconciliations/{scope}/{code} | [EXPERIMENTAL] UpdateReconciliation: Update scheduled reconciliation
[**upsert_reconciliation_break**](ReconciliationsApi.md#upsert_reconciliation_break) | **POST** /api/portfolios/$scheduledReconciliations/{scope}/{code}/runs/{runDate}/{version} | [EXPERIMENTAL] UpsertReconciliationBreak: Upsert a reconciliation break
[**upsert_reconciliation_mapping**](ReconciliationsApi.md#upsert_reconciliation_mapping) | **POST** /api/portfolios/mapping | [EARLY ACCESS] UpsertReconciliationMapping: Create or update a mapping
[**upsert_reconciliation_run**](ReconciliationsApi.md#upsert_reconciliation_run) | **POST** /api/portfolios/$scheduledReconciliations/{scope}/{code}/runs | [EXPERIMENTAL] UpsertReconciliationRun: Update or Create a reconciliation run


# **create_scheduled_reconciliation**
> Reconciliation create_scheduled_reconciliation(scope, create_reconciliation_request=create_reconciliation_request)

[EXPERIMENTAL] CreateScheduledReconciliation: Create a scheduled reconciliation

Create a scheduled reconciliation for the given request

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
    api_instance = lusid.ReconciliationsApi(api_client)
    scope = 'scope_example' # str | The scope of the reconciliation
    create_reconciliation_request = {"code":"Reconciliation","name":"ReconciliationName","description":"Reconciliation description","isPortfolioGroup":false,"left":{"scope":"MyScope","code":"SideA"},"right":{"scope":"MyScope","code":"SideB"},"transactions":{"transactionWindow":{"fromDate":"2018-03-04T00:00:00.0000000+00:00","untilDate":"2018-03-05T00:00:00.0000000+00:00"},"mappingId":{"scope":"MyScope","code":"TestMapping"}},"positions":{"left":{"recipeId":{"scope":"MyScope","code":"PMS"},"effectiveAt":"2019-01-01T12:00:00.0000000+00:00","asAt":"2019-01-01T12:00:00.0100000+00:00"},"right":{"recipeId":{"scope":"MyScope","code":"PMS"},"effectiveAt":"2019-01-01T12:00:00.0000000+00:00","asAt":"2019-01-01T12:00:00.0100000+00:00"},"mappingId":{"scope":"MyScope","code":"TestMapping"}},"valuations":{"left":{"recipeId":{"scope":"MyScope","code":"PMS"},"effectiveAt":"2019-01-01T12:00:00.0000000+00:00","asAt":"2019-01-01T12:00:00.0100000+00:00","currency":"GBP"},"right":{"recipeId":{"scope":"MyScope","code":"PMS"},"effectiveAt":"2019-01-01T12:00:00.0000000+00:00","asAt":"2019-01-01T12:00:00.0100000+00:00"},"mappingId":{"scope":"MyScope","code":"TestMapping"}},"properties":{"Reconciliation/MyScope/BrokerName":{"key":"Reconciliation/MyScope/BrokerName","value":{"labelValue":"BrokerA"},"effectiveFrom":"2018-03-05T00:00:00.0000000+00:00"}}} # CreateReconciliationRequest | The definition of the reconciliation (optional)

    try:
        # [EXPERIMENTAL] CreateScheduledReconciliation: Create a scheduled reconciliation
        api_response = await api_instance.create_scheduled_reconciliation(scope, create_reconciliation_request=create_reconciliation_request)
        print("The response of ReconciliationsApi->create_scheduled_reconciliation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReconciliationsApi->create_scheduled_reconciliation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the reconciliation | 
 **create_reconciliation_request** | [**CreateReconciliationRequest**](CreateReconciliationRequest.md)| The definition of the reconciliation | [optional] 

### Return type

[**Reconciliation**](Reconciliation.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created scheduled reconciliation |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_reconciliation**
> DeletedEntityResponse delete_reconciliation(scope, code)

[EXPERIMENTAL] DeleteReconciliation: Delete scheduled reconciliation

Delete the given scheduled reconciliation

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
    api_instance = lusid.ReconciliationsApi(api_client)
    scope = 'scope_example' # str | The scope of the scheduled reconciliation
    code = 'code_example' # str | The code of the scheduled reconciliation

    try:
        # [EXPERIMENTAL] DeleteReconciliation: Delete scheduled reconciliation
        api_response = await api_instance.delete_reconciliation(scope, code)
        print("The response of ReconciliationsApi->delete_reconciliation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReconciliationsApi->delete_reconciliation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the scheduled reconciliation | 
 **code** | **str**| The code of the scheduled reconciliation | 

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
**200** | The reconciliation at the requested as at was deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_reconciliation_break**
> DeletedEntityResponse delete_reconciliation_break(scope, code, run_date, version, break_id)

[EXPERIMENTAL] DeleteReconciliationBreak: Delete reconciliation break

Delete the given reconciliation break

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
    api_instance = lusid.ReconciliationsApi(api_client)
    scope = 'scope_example' # str | The scope of the reconciliation associated with the break
    code = 'code_example' # str | The code of the reconciliation associated with the break
    run_date = '2013-10-20T19:20:30+01:00' # datetime | The date of the run associated with the break
    version = 56 # int | The version number of the run associated with the break
    break_id = 'break_id_example' # str | The unique identifier for the break

    try:
        # [EXPERIMENTAL] DeleteReconciliationBreak: Delete reconciliation break
        api_response = await api_instance.delete_reconciliation_break(scope, code, run_date, version, break_id)
        print("The response of ReconciliationsApi->delete_reconciliation_break:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReconciliationsApi->delete_reconciliation_break: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the reconciliation associated with the break | 
 **code** | **str**| The code of the reconciliation associated with the break | 
 **run_date** | **datetime**| The date of the run associated with the break | 
 **version** | **int**| The version number of the run associated with the break | 
 **break_id** | **str**| The unique identifier for the break | 

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
**200** | The datetime that the reconciliation break was deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_reconciliation_mapping**
> str delete_reconciliation_mapping(scope, code)

[EARLY ACCESS] DeleteReconciliationMapping: Delete a mapping

Deletes the mapping identified by the scope and code

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
    api_instance = lusid.ReconciliationsApi(api_client)
    scope = 'scope_example' # str | The scope of the mapping.
    code = 'code_example' # str | The code fof the mapping.

    try:
        # [EARLY ACCESS] DeleteReconciliationMapping: Delete a mapping
        api_response = await api_instance.delete_reconciliation_mapping(scope, code)
        print("The response of ReconciliationsApi->delete_reconciliation_mapping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReconciliationsApi->delete_reconciliation_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the mapping. | 
 **code** | **str**| The code fof the mapping. | 

### Return type

**str**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A string specifying the scope and code that were deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_reconciliation_run**
> DeletedEntityResponse delete_reconciliation_run(scope, code, run_date, version)

[EXPERIMENTAL] DeleteReconciliationRun: Delete reconciliation run

Delete the given reconciliation run

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
    api_instance = lusid.ReconciliationsApi(api_client)
    scope = 'scope_example' # str | The scope of the reconciliation associated with the run
    code = 'code_example' # str | The code of the reconciliation associated with the run
    run_date = '2013-10-20T19:20:30+01:00' # datetime | The date of the reconciliation run
    version = 56 # int | The version number of the reconciliation run

    try:
        # [EXPERIMENTAL] DeleteReconciliationRun: Delete reconciliation run
        api_response = await api_instance.delete_reconciliation_run(scope, code, run_date, version)
        print("The response of ReconciliationsApi->delete_reconciliation_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReconciliationsApi->delete_reconciliation_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the reconciliation associated with the run | 
 **code** | **str**| The code of the reconciliation associated with the run | 
 **run_date** | **datetime**| The date of the reconciliation run | 
 **version** | **int**| The version number of the reconciliation run | 

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
**200** | The datetime that the reconciliation run was deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reconciliation**
> Reconciliation get_reconciliation(scope, code, effective_at=effective_at, as_at=as_at, property_keys=property_keys)

[EXPERIMENTAL] GetReconciliation: Get scheduled reconciliation

Get the requested scheduled reconciliation

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
    api_instance = lusid.ReconciliationsApi(api_client)
    scope = 'scope_example' # str | The scope of the scheduled reconciliation
    code = 'code_example' # str | The code of the scheduled reconciliation
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve the scheduled reconciliation. Defaults to the current LUSID system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the scheduled reconciliation. Defaults to returning the latest version of the reconciliation if not specified. (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the 'Reconciliation' property domain to decorate onto the reconciliation.              These must take the form {domain}/{scope}/{code}, for example 'Reconciliation/Broker/Id'. (optional)

    try:
        # [EXPERIMENTAL] GetReconciliation: Get scheduled reconciliation
        api_response = await api_instance.get_reconciliation(scope, code, effective_at=effective_at, as_at=as_at, property_keys=property_keys)
        print("The response of ReconciliationsApi->get_reconciliation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReconciliationsApi->get_reconciliation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the scheduled reconciliation | 
 **code** | **str**| The code of the scheduled reconciliation | 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the scheduled reconciliation. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the scheduled reconciliation. Defaults to returning the latest version of the reconciliation if not specified. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;Reconciliation&#39; property domain to decorate onto the reconciliation.              These must take the form {domain}/{scope}/{code}, for example &#39;Reconciliation/Broker/Id&#39;. | [optional] 

### Return type

[**Reconciliation**](Reconciliation.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested scheduled reconciliation |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reconciliation_break**
> ReconciliationRunBreak get_reconciliation_break(scope, code, run_date, version, break_id, as_at=as_at)

[EXPERIMENTAL] GetReconciliationBreak: Get reconciliation break

Get the requested reconciliation break

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
    api_instance = lusid.ReconciliationsApi(api_client)
    scope = 'scope_example' # str | The scope of the reconciliation associated with the break
    code = 'code_example' # str | The code of the reconciliation associated with the break
    run_date = '2013-10-20T19:20:30+01:00' # datetime | The date of the run associated with the break
    version = 56 # int | The version number of the run associated with the break
    break_id = 'break_id_example' # str | The unique identifier for the break
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the reconciliation break. Defaults to returning the latest version of the reconciliation break if not specified. (optional)

    try:
        # [EXPERIMENTAL] GetReconciliationBreak: Get reconciliation break
        api_response = await api_instance.get_reconciliation_break(scope, code, run_date, version, break_id, as_at=as_at)
        print("The response of ReconciliationsApi->get_reconciliation_break:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReconciliationsApi->get_reconciliation_break: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the reconciliation associated with the break | 
 **code** | **str**| The code of the reconciliation associated with the break | 
 **run_date** | **datetime**| The date of the run associated with the break | 
 **version** | **int**| The version number of the run associated with the break | 
 **break_id** | **str**| The unique identifier for the break | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the reconciliation break. Defaults to returning the latest version of the reconciliation break if not specified. | [optional] 

### Return type

[**ReconciliationRunBreak**](ReconciliationRunBreak.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested reconciliation break |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reconciliation_mapping**
> Mapping get_reconciliation_mapping(scope, code)

[EARLY ACCESS] GetReconciliationMapping: Get a mapping

Gets a mapping identified by the given scope and code

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
    api_instance = lusid.ReconciliationsApi(api_client)
    scope = 'scope_example' # str | The scope of the mapping.
    code = 'code_example' # str | The code of the mapping.

    try:
        # [EARLY ACCESS] GetReconciliationMapping: Get a mapping
        api_response = await api_instance.get_reconciliation_mapping(scope, code)
        print("The response of ReconciliationsApi->get_reconciliation_mapping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReconciliationsApi->get_reconciliation_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the mapping. | 
 **code** | **str**| The code of the mapping. | 

### Return type

[**Mapping**](Mapping.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The mapping with the specified scope/code. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reconciliation_run**
> ReconciliationRun get_reconciliation_run(scope, code, run_date, version, effective_at=effective_at, as_at=as_at)

[EXPERIMENTAL] GetReconciliationRun: Get a reconciliation run

Get the requested reconciliation run

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
    api_instance = lusid.ReconciliationsApi(api_client)
    scope = 'scope_example' # str | The scope of the reconciliation associated with the run
    code = 'code_example' # str | The code of the reconciliation associated with the run
    run_date = '2013-10-20T19:20:30+01:00' # datetime | The date of the run
    version = 56 # int | The version number of the run
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve the reconciliation run. Defaults to the current LUSID system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the reconciliation run. Defaults to returning the latest version of the reconciliation run if not specified. (optional)

    try:
        # [EXPERIMENTAL] GetReconciliationRun: Get a reconciliation run
        api_response = await api_instance.get_reconciliation_run(scope, code, run_date, version, effective_at=effective_at, as_at=as_at)
        print("The response of ReconciliationsApi->get_reconciliation_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReconciliationsApi->get_reconciliation_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the reconciliation associated with the run | 
 **code** | **str**| The code of the reconciliation associated with the run | 
 **run_date** | **datetime**| The date of the run | 
 **version** | **int**| The version number of the run | 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the reconciliation run. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the reconciliation run. Defaults to returning the latest version of the reconciliation run if not specified. | [optional] 

### Return type

[**ReconciliationRun**](ReconciliationRun.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested reconciliation run |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_reconciliation_breaks**
> PagedResourceListOfReconciliationRunBreak list_reconciliation_breaks(scope, code, run_date, version, effective_at=effective_at, as_at=as_at, page=page, start=start, limit=limit, filter=filter)

[EXPERIMENTAL] ListReconciliationBreaks: List reconciliation breaks

List all reconciliation breaks associated with a given run

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
    api_instance = lusid.ReconciliationsApi(api_client)
    scope = 'scope_example' # str | The scope of the reconciliation associated with the break
    code = 'code_example' # str | The code of the reconciliation associated with the break
    run_date = '2013-10-20T19:20:30+01:00' # datetime | The date of the run associated with the break
    version = 56 # int | The version number of the run associated with the break
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to list the reconciliation runs. Defaults to the current LUSID              system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the reconciliation runs. Defaults to returning the latest version              of each run if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing reconciliation runs; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. Also, if set, a start value cannot be provided. (optional)
    start = 56 # int | When paginating, skip this number of results. (optional)
    limit = 56 # int | When paginating, limit the results to this number. Defaults to 100 if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the results. (optional)

    try:
        # [EXPERIMENTAL] ListReconciliationBreaks: List reconciliation breaks
        api_response = await api_instance.list_reconciliation_breaks(scope, code, run_date, version, effective_at=effective_at, as_at=as_at, page=page, start=start, limit=limit, filter=filter)
        print("The response of ReconciliationsApi->list_reconciliation_breaks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReconciliationsApi->list_reconciliation_breaks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the reconciliation associated with the break | 
 **code** | **str**| The code of the reconciliation associated with the break | 
 **run_date** | **datetime**| The date of the run associated with the break | 
 **version** | **int**| The version number of the run associated with the break | 
 **effective_at** | **str**| The effective datetime or cut label at which to list the reconciliation runs. Defaults to the current LUSID              system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the reconciliation runs. Defaults to returning the latest version              of each run if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing reconciliation runs; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. Also, if set, a start value cannot be provided. | [optional] 
 **start** | **int**| When paginating, skip this number of results. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results. | [optional] 

### Return type

[**PagedResourceListOfReconciliationRunBreak**](PagedResourceListOfReconciliationRunBreak.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested reconciliation breaks |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_reconciliation_mappings**
> ResourceListOfMapping list_reconciliation_mappings(reconciliation_type=reconciliation_type)

[EARLY ACCESS] ListReconciliationMappings: List the reconciliation mappings

Lists all mappings this user is entitled to see

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
    api_instance = lusid.ReconciliationsApi(api_client)
    reconciliation_type = 'reconciliation_type_example' # str | Optional parameter to specify which type of mappings should be returned.  Defaults to Transaction if not provided. (optional)

    try:
        # [EARLY ACCESS] ListReconciliationMappings: List the reconciliation mappings
        api_response = await api_instance.list_reconciliation_mappings(reconciliation_type=reconciliation_type)
        print("The response of ReconciliationsApi->list_reconciliation_mappings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReconciliationsApi->list_reconciliation_mappings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reconciliation_type** | **str**| Optional parameter to specify which type of mappings should be returned.  Defaults to Transaction if not provided. | [optional] 

### Return type

[**ResourceListOfMapping**](ResourceListOfMapping.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The mappings that the caller has access to. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_reconciliation_runs**
> PagedResourceListOfReconciliationRun list_reconciliation_runs(scope, code, effective_at=effective_at, as_at=as_at, page=page, start=start, limit=limit, filter=filter)

[EXPERIMENTAL] ListReconciliationRuns: List Reconciliation runs

List all runs for a given reconciliation

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
    api_instance = lusid.ReconciliationsApi(api_client)
    scope = 'scope_example' # str | The scope of the reconciliation
    code = 'code_example' # str | The code of the reconciliation
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to list the reconciliation runs. Defaults to the current LUSID              system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the reconciliation runs. Defaults to returning the latest version              of each run if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing reconciliation runs; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. Also, if set, a start value cannot be provided. (optional)
    start = 56 # int | When paginating, skip this number of results. (optional)
    limit = 56 # int | When paginating, limit the results to this number. Defaults to 100 if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the results.              For example, to filter on the run date, specify \"Date eq 10/03/2018\". For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. (optional)

    try:
        # [EXPERIMENTAL] ListReconciliationRuns: List Reconciliation runs
        api_response = await api_instance.list_reconciliation_runs(scope, code, effective_at=effective_at, as_at=as_at, page=page, start=start, limit=limit, filter=filter)
        print("The response of ReconciliationsApi->list_reconciliation_runs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReconciliationsApi->list_reconciliation_runs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the reconciliation | 
 **code** | **str**| The code of the reconciliation | 
 **effective_at** | **str**| The effective datetime or cut label at which to list the reconciliation runs. Defaults to the current LUSID              system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the reconciliation runs. Defaults to returning the latest version              of each run if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing reconciliation runs; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. Also, if set, a start value cannot be provided. | [optional] 
 **start** | **int**| When paginating, skip this number of results. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results.              For example, to filter on the run date, specify \&quot;Date eq 10/03/2018\&quot;. For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 

### Return type

[**PagedResourceListOfReconciliationRun**](PagedResourceListOfReconciliationRun.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested reconciliation runs |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_reconciliations**
> PagedResourceListOfReconciliation list_reconciliations(effective_at=effective_at, as_at=as_at, page=page, start=start, limit=limit, filter=filter, property_keys=property_keys)

[EXPERIMENTAL] ListReconciliations: List scheduled reconciliations

List all the scheduled reconciliations matching particular criteria

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
    api_instance = lusid.ReconciliationsApi(api_client)
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to list the TimeVariant properties for the reconciliation. Defaults to the current LUSID              system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the reconciliation. Defaults to returning the latest version              of each reconciliation if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing reconciliations; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. Also, if set, a start value cannot be provided. (optional)
    start = 56 # int | When paginating, skip this number of results. (optional)
    limit = 56 # int | When paginating, limit the results to this number. Defaults to 100 if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the results.              For example, to filter on the reconciliation type, specify \"id.Code eq '001'\". For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the 'Reconciliation' domain to decorate onto each reconciliation.              These must take the format {domain}/{scope}/{code}, for example 'Reconciliation/Broker/Id'. (optional)

    try:
        # [EXPERIMENTAL] ListReconciliations: List scheduled reconciliations
        api_response = await api_instance.list_reconciliations(effective_at=effective_at, as_at=as_at, page=page, start=start, limit=limit, filter=filter, property_keys=property_keys)
        print("The response of ReconciliationsApi->list_reconciliations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReconciliationsApi->list_reconciliations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **effective_at** | **str**| The effective datetime or cut label at which to list the TimeVariant properties for the reconciliation. Defaults to the current LUSID              system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the reconciliation. Defaults to returning the latest version              of each reconciliation if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing reconciliations; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. Also, if set, a start value cannot be provided. | [optional] 
 **start** | **int**| When paginating, skip this number of results. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results.              For example, to filter on the reconciliation type, specify \&quot;id.Code eq &#39;001&#39;\&quot;. For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;Reconciliation&#39; domain to decorate onto each reconciliation.              These must take the format {domain}/{scope}/{code}, for example &#39;Reconciliation/Broker/Id&#39;. | [optional] 

### Return type

[**PagedResourceListOfReconciliation**](PagedResourceListOfReconciliation.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of all scheduled reconciliations |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reconcile_generic**
> ReconciliationResponse reconcile_generic(reconciliation_request=reconciliation_request)

ReconcileGeneric: Reconcile either holdings or valuations performed on one or two sets of holdings using one or two configuration recipes.                The output is configurable for various types of comparisons, to allow tolerances on numerical and date-time data or case-insensitivity on strings,  and elision of resulting differences where they are 'empty' or null or zero.

Perform evaluation of one or two set of holdings (a portfolio of instruments) using one or two (potentially different) configuration recipes.  Produce a breakdown of the resulting differences in evaluation that can be iterated through.

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
    api_instance = lusid.ReconciliationsApi(api_client)
    reconciliation_request = {"left":{"recipeId":{"scope":"MySourceScope","code":"MySourcePortfolioCode"},"asAt":"2018-03-05T00:00:00.0000000+00:00","metrics":[{"key":"Instrument/default/Name","op":"Value","options":{}},{"key":"Holding/default/PV","op":"Sum","options":{}}],"groupBy":["Instrument/default/Name"],"sort":[],"reportCurrency":"USD","equipWithSubtotals":false,"returnResultAsExpandedTypes":false,"portfolioEntityIds":[{"scope":"PortfolioScope1","code":"MyPortfolioAbC","portfolioEntityType":"SinglePortfolio"},{"scope":"PortfolioScope2","code":"MyPortfolioDeF","portfolioEntityType":"SinglePortfolio"}],"valuationSchedule":{"effectiveFrom":"2018-03-05T00:00:00.0000000+00:00","effectiveAt":"2018-03-05T00:00:00.0000000+00:00","tenor":"1D","rollConvention":"F","holidayCalendars":[],"valuationDateTimes":[]}},"right":{"recipeId":{"scope":"MyTargetScope","code":"MyTargetPortfolioCode"},"asAt":"2018-03-05T00:00:00.0000000+00:00","metrics":[{"key":"Instrument/default/Name","op":"Value","options":{}},{"key":"Holding/default/PV","op":"Sum","options":{}}],"groupBy":["Instrument/default/Name"],"sort":[],"reportCurrency":"USD","equipWithSubtotals":false,"returnResultAsExpandedTypes":false,"portfolioEntityIds":[{"scope":"PortfolioScope1","code":"MyPortfolioAbC","portfolioEntityType":"SinglePortfolio"},{"scope":"PortfolioScope2","code":"MyPortfolioDeF","portfolioEntityType":"SinglePortfolio"}],"valuationSchedule":{"effectiveFrom":"2018-03-05T00:00:00.0000000+00:00","effectiveAt":"2018-03-05T00:00:00.0000000+00:00","tenor":"1D","rollConvention":"F","holidayCalendars":[],"valuationDateTimes":[]}},"leftToRightMapping":[],"comparisonRules":[{"comparisonType":"AbsoluteDifference","tolerance":1.2345,"appliesTo":{"key":"Holding/default/PV","op":"Sum","options":{}},"ruleType":"ReconcileNumericRule"}],"preserveKeys":["Instrument/default/Name"]} # ReconciliationRequest | The specifications of the inputs to the reconciliation (optional)

    try:
        # ReconcileGeneric: Reconcile either holdings or valuations performed on one or two sets of holdings using one or two configuration recipes.                The output is configurable for various types of comparisons, to allow tolerances on numerical and date-time data or case-insensitivity on strings,  and elision of resulting differences where they are 'empty' or null or zero.
        api_response = await api_instance.reconcile_generic(reconciliation_request=reconciliation_request)
        print("The response of ReconciliationsApi->reconcile_generic:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReconciliationsApi->reconcile_generic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reconciliation_request** | [**ReconciliationRequest**](ReconciliationRequest.md)| The specifications of the inputs to the reconciliation | [optional] 

### Return type

[**ReconciliationResponse**](ReconciliationResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested reconciliation |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reconcile_holdings**
> ResourceListOfReconciliationBreak reconcile_holdings(sort_by=sort_by, start=start, limit=limit, filter=filter, portfolios_reconciliation_request=portfolios_reconciliation_request)

[EARLY ACCESS] ReconcileHoldings: Reconcile portfolio holdings

Reconcile the holdings of two portfolios.

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
    api_instance = lusid.ReconciliationsApi(api_client)
    sort_by = ['sort_by_example'] # List[str] | Optional. Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName (optional)
    start = 56 # int | Optional. When paginating, skip this number of results (optional)
    limit = 56 # int | Optional. When paginating, limit the number of returned results to this many. (optional)
    filter = 'filter_example' # str | Optional. Expression to filter the result set.              For example, to filter on the left portfolio Code, use \"left.portfolioId.code eq 'string'\"              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)
    portfolios_reconciliation_request = {"left":{"portfolioId":{"scope":"MySourceScope","code":"MySourcePortfolioCode"},"effectiveAt":"2018-03-05T00:00:00.0000000+00:00","asAt":"2018-03-05T00:00:00.0000000+00:00"},"right":{"portfolioId":{"scope":"MyTargetScope","code":"MyTargetPortfolioCode"},"effectiveAt":"2018-03-05T00:00:00.0000000+00:00","asAt":"2018-03-05T00:00:00.0000000+00:00"},"instrumentPropertyKeys":["Instrument/default/Name"]} # PortfoliosReconciliationRequest | The specifications of the inputs to the reconciliation (optional)

    try:
        # [EARLY ACCESS] ReconcileHoldings: Reconcile portfolio holdings
        api_response = await api_instance.reconcile_holdings(sort_by=sort_by, start=start, limit=limit, filter=filter, portfolios_reconciliation_request=portfolios_reconciliation_request)
        print("The response of ReconciliationsApi->reconcile_holdings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReconciliationsApi->reconcile_holdings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort_by** | [**List[str]**](str.md)| Optional. Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName | [optional] 
 **start** | **int**| Optional. When paginating, skip this number of results | [optional] 
 **limit** | **int**| Optional. When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Optional. Expression to filter the result set.              For example, to filter on the left portfolio Code, use \&quot;left.portfolioId.code eq &#39;string&#39;\&quot;              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **portfolios_reconciliation_request** | [**PortfoliosReconciliationRequest**](PortfoliosReconciliationRequest.md)| The specifications of the inputs to the reconciliation | [optional] 

### Return type

[**ResourceListOfReconciliationBreak**](ResourceListOfReconciliationBreak.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested reconciliation |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reconcile_inline**
> ListAggregationReconciliation reconcile_inline(inline_valuations_reconciliation_request=inline_valuations_reconciliation_request)

ReconcileInline: Reconcile valuations performed on one or two sets of inline instruments using one or two configuration recipes.

Perform valuation of one or two set of inline instruments using different one or two configuration recipes. Produce a breakdown of the resulting differences in valuation.

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
    api_instance = lusid.ReconciliationsApi(api_client)
    inline_valuations_reconciliation_request = {"left":{"recipeId":{"scope":"MyScope","code":"default"},"asAt":"2018-03-05T00:00:00.0000000+00:00","metrics":[{"key":"Instrument/default/Name","op":"Value","options":{}},{"key":"Holding/default/PV","op":"Value","options":{}}],"groupBy":["Instrument/default/Name"],"reportCurrency":"USD","equipWithSubtotals":false,"returnResultAsExpandedTypes":false,"valuationSchedule":{"effectiveFrom":"2018-03-05T00:00:00.0000000+00:00","effectiveAt":"2018-03-05T00:00:00.0000000+00:00","tenor":"1D","rollConvention":"F","holidayCalendars":[],"valuationDateTimes":[]},"instruments":[{"quantity":10000,"holdingIdentifier":"fx-fwd-GBPUSD","instrument":{"startDate":"2018-03-01T00:00:00.0000000+00:00","maturityDate":"2018-03-30T00:00:00.0000000+00:00","domAmount":100,"domCcy":"GBP","fgnAmount":-150,"fgnCcy":"USD","refSpotRate":1.5,"isNdf":false,"fixingDate":"0001-01-01T00:00:00.0000000+00:00","instrumentType":"FxForward"}}]},"right":{"recipeId":{"scope":"MyScope","code":"default"},"asAt":"2018-03-05T00:00:00.0000000+00:00","metrics":[{"key":"Instrument/default/Name","op":"Value","options":{}},{"key":"Holding/default/PV","op":"Value","options":{}}],"groupBy":["Instrument/default/Name"],"reportCurrency":"USD","equipWithSubtotals":false,"returnResultAsExpandedTypes":false,"valuationSchedule":{"effectiveFrom":"2018-03-05T00:00:00.0000000+00:00","effectiveAt":"2018-03-05T00:00:00.0000000+00:00","tenor":"1D","rollConvention":"F","holidayCalendars":[],"valuationDateTimes":[]},"instruments":[{"quantity":10000,"holdingIdentifier":"fx-fwd-GBPJPY","instrument":{"startDate":"2018-03-01T00:00:00.0000000+00:00","maturityDate":"2018-03-30T00:00:00.0000000+00:00","domAmount":100,"domCcy":"GBP","fgnAmount":-150,"fgnCcy":"JPY","refSpotRate":132,"isNdf":false,"fixingDate":"0001-01-01T00:00:00.0000000+00:00","instrumentType":"FxForward"}}]},"leftToRightMapping":[],"preserveKeys":[]} # InlineValuationsReconciliationRequest | The specifications of the inputs to the reconciliation (optional)

    try:
        # ReconcileInline: Reconcile valuations performed on one or two sets of inline instruments using one or two configuration recipes.
        api_response = await api_instance.reconcile_inline(inline_valuations_reconciliation_request=inline_valuations_reconciliation_request)
        print("The response of ReconciliationsApi->reconcile_inline:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReconciliationsApi->reconcile_inline: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_valuations_reconciliation_request** | [**InlineValuationsReconciliationRequest**](InlineValuationsReconciliationRequest.md)| The specifications of the inputs to the reconciliation | [optional] 

### Return type

[**ListAggregationReconciliation**](ListAggregationReconciliation.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested reconciliation |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reconcile_transactions**
> TransactionsReconciliationsResponse reconcile_transactions(transaction_reconciliation_request=transaction_reconciliation_request)

[EARLY ACCESS] ReconcileTransactions: Perform a Transactions Reconciliation.

Evaluates two sets of transactions to determine which transactions from each set likely match  using the rules of a specified mapping.

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
    api_instance = lusid.ReconciliationsApi(api_client)
    transaction_reconciliation_request = {"leftPortfolioId":{"scope":"street","code":"Global-Equity"},"rightPortfolioId":{"scope":"custodian","code":"Global-Equity"},"fromTransactionDate":"2019-04-01T12:00:00.0000000+00:00","toTransactionDate":"2019-05-01T12:00:00.0000000+00:00","propertyKeys":["Instrument/default/Name","Transaction/common/Strategy"]} # TransactionReconciliationRequest |  (optional)

    try:
        # [EARLY ACCESS] ReconcileTransactions: Perform a Transactions Reconciliation.
        api_response = await api_instance.reconcile_transactions(transaction_reconciliation_request=transaction_reconciliation_request)
        print("The response of ReconciliationsApi->reconcile_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReconciliationsApi->reconcile_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_reconciliation_request** | [**TransactionReconciliationRequest**](TransactionReconciliationRequest.md)|  | [optional] 

### Return type

[**TransactionsReconciliationsResponse**](TransactionsReconciliationsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The transaction reconciliation data for the supplied portfolios. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reconcile_valuation**
> ListAggregationReconciliation reconcile_valuation(valuations_reconciliation_request=valuations_reconciliation_request)

ReconcileValuation: Reconcile valuations performed on one or two sets of holdings using one or two configuration recipes.

Perform valuation of one or two set of holdings using different one or two configuration recipes. Produce a breakdown of the resulting differences in valuation.

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
    api_instance = lusid.ReconciliationsApi(api_client)
    valuations_reconciliation_request = {"left":{"recipeId":{"scope":"MySourceScope","code":"MySourcePortfolioCode"},"asAt":"2018-03-05T00:00:00.0000000+00:00","metrics":[{"key":"Instrument/default/Name","op":"Value","options":{}},{"key":"Holding/default/PV","op":"Sum","options":{}}],"groupBy":["Instrument/default/Name"],"sort":[],"reportCurrency":"USD","equipWithSubtotals":false,"returnResultAsExpandedTypes":false,"portfolioEntityIds":[{"scope":"PortfolioScope1","code":"MyPortfolioAbC","portfolioEntityType":"SinglePortfolio"},{"scope":"PortfolioScope2","code":"MyPortfolioDeF","portfolioEntityType":"SinglePortfolio"}],"valuationSchedule":{"effectiveFrom":"2018-03-05T00:00:00.0000000+00:00","effectiveAt":"2018-03-05T00:00:00.0000000+00:00","tenor":"1D","rollConvention":"F","holidayCalendars":[],"valuationDateTimes":[]}},"right":{"recipeId":{"scope":"MyTargetScope","code":"MyTargetPortfolioCode"},"asAt":"2018-03-05T00:00:00.0000000+00:00","metrics":[{"key":"Instrument/default/Name","op":"Value","options":{}},{"key":"Holding/default/PV","op":"Sum","options":{}}],"groupBy":["Instrument/default/Name"],"sort":[],"reportCurrency":"USD","equipWithSubtotals":false,"returnResultAsExpandedTypes":false,"portfolioEntityIds":[{"scope":"PortfolioScope1","code":"MyPortfolioAbC","portfolioEntityType":"SinglePortfolio"},{"scope":"PortfolioScope2","code":"MyPortfolioDeF","portfolioEntityType":"SinglePortfolio"}],"valuationSchedule":{"effectiveFrom":"2018-03-05T00:00:00.0000000+00:00","effectiveAt":"2018-03-05T00:00:00.0000000+00:00","tenor":"1D","rollConvention":"F","holidayCalendars":[],"valuationDateTimes":[]}},"leftToRightMapping":[],"preserveKeys":["Instrument/default/Name"]} # ValuationsReconciliationRequest | The specifications of the inputs to the reconciliation (optional)

    try:
        # ReconcileValuation: Reconcile valuations performed on one or two sets of holdings using one or two configuration recipes.
        api_response = await api_instance.reconcile_valuation(valuations_reconciliation_request=valuations_reconciliation_request)
        print("The response of ReconciliationsApi->reconcile_valuation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReconciliationsApi->reconcile_valuation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **valuations_reconciliation_request** | [**ValuationsReconciliationRequest**](ValuationsReconciliationRequest.md)| The specifications of the inputs to the reconciliation | [optional] 

### Return type

[**ListAggregationReconciliation**](ListAggregationReconciliation.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested reconciliation |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_reconciliation**
> Reconciliation update_reconciliation(scope, code, update_reconciliation_request=update_reconciliation_request)

[EXPERIMENTAL] UpdateReconciliation: Update scheduled reconciliation

Update a given scheduled reconciliation

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
    api_instance = lusid.ReconciliationsApi(api_client)
    scope = 'scope_example' # str | The scope of the reconciliation to be updated
    code = 'code_example' # str | The code of the reconciliation to be updated
    update_reconciliation_request = {"name":"UpdatedReconciliationName","description":"Updated reconciliation description","isPortfolioGroup":false,"left":{"scope":"MyScope","code":"SideA"},"right":{"scope":"MyScope","code":"SideB"},"transactions":{"transactionWindow":{"fromDate":"2018-03-04T00:00:00.0000000+00:00","untilDate":"2018-03-05T00:00:00.0000000+00:00"},"mappingId":{"scope":"MyScope","code":"TestMapping"}},"positions":{"left":{"recipeId":{"scope":"MyScope","code":"PMS"},"effectiveAt":"2018-03-05T00:00:00.0000000+00:00","asAt":"2018-03-05T00:00:00.0000000+00:00"},"right":{"recipeId":{"scope":"MyScope","code":"PMS"},"effectiveAt":"2018-03-05T00:00:00.0000000+00:00","asAt":"2018-03-05T00:00:00.0000000+00:00"},"mappingId":{"scope":"MyScope","code":"TestMapping"}},"valuations":{"left":{"recipeId":{"scope":"MyScope","code":"PMS"},"effectiveAt":"2018-03-05T00:00:00.0000000+00:00","asAt":"2018-03-05T00:00:00.0000000+00:00","currency":"GBP"},"right":{"recipeId":{"scope":"MyScope","code":"PMS"},"effectiveAt":"2018-03-05T00:00:00.0000000+00:00","asAt":"2018-03-05T00:00:00.0000000+00:00","currency":"GBP"},"mappingId":{"scope":"MyScope","code":"TestMapping"}},"properties":{"Reconciliation/MyScope/BrokerName":{"key":"Reconciliation/MyScope/BrokerName","value":{"labelValue":"BrokerA"},"effectiveFrom":"2018-03-05T00:00:00.0000000+00:00"}}} # UpdateReconciliationRequest | The updated definition of the reconciliation (optional)

    try:
        # [EXPERIMENTAL] UpdateReconciliation: Update scheduled reconciliation
        api_response = await api_instance.update_reconciliation(scope, code, update_reconciliation_request=update_reconciliation_request)
        print("The response of ReconciliationsApi->update_reconciliation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReconciliationsApi->update_reconciliation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the reconciliation to be updated | 
 **code** | **str**| The code of the reconciliation to be updated | 
 **update_reconciliation_request** | [**UpdateReconciliationRequest**](UpdateReconciliationRequest.md)| The updated definition of the reconciliation | [optional] 

### Return type

[**Reconciliation**](Reconciliation.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated scheduled reconciliation |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_reconciliation_break**
> ReconciliationRunBreak upsert_reconciliation_break(scope, code, run_date, version, upsert_reconciliation_break_request=upsert_reconciliation_break_request)

[EXPERIMENTAL] UpsertReconciliationBreak: Upsert a reconciliation break

Update or create a given reconciliation break

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
    api_instance = lusid.ReconciliationsApi(api_client)
    scope = 'scope_example' # str | The scope of the reconciliation associated with the break
    code = 'code_example' # str | The code of the reconciliation associated with the break
    run_date = '2013-10-20T19:20:30+01:00' # datetime | The date of the run associated with the break
    version = 56 # int | The version number of the run associated with the break
    upsert_reconciliation_break_request = {"leftFields":{"Type":"Buy","Units":"100,000.00","Instrument Name":"Legal & General Group plc (Ordinary Shares)","Transaction Price":"8"},"rightFields":{"Type":"Buy","Units":"90,000.00","Instrument Name":"Legal & General Group plc (Ordinary Shares)","Transaction Price":"8"},"diff":"1,000.00"} # UpsertReconciliationBreakRequest | The definition of the reconciliation break request (optional)

    try:
        # [EXPERIMENTAL] UpsertReconciliationBreak: Upsert a reconciliation break
        api_response = await api_instance.upsert_reconciliation_break(scope, code, run_date, version, upsert_reconciliation_break_request=upsert_reconciliation_break_request)
        print("The response of ReconciliationsApi->upsert_reconciliation_break:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReconciliationsApi->upsert_reconciliation_break: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the reconciliation associated with the break | 
 **code** | **str**| The code of the reconciliation associated with the break | 
 **run_date** | **datetime**| The date of the run associated with the break | 
 **version** | **int**| The version number of the run associated with the break | 
 **upsert_reconciliation_break_request** | [**UpsertReconciliationBreakRequest**](UpsertReconciliationBreakRequest.md)| The definition of the reconciliation break request | [optional] 

### Return type

[**ReconciliationRunBreak**](ReconciliationRunBreak.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created reconciliation break |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_reconciliation_mapping**
> Mapping upsert_reconciliation_mapping(mapping=mapping)

[EARLY ACCESS] UpsertReconciliationMapping: Create or update a mapping

If no mapping exists with the specified scope and code will create a new one.  Else will update the existing mapping

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
    api_instance = lusid.ReconciliationsApi(api_client)
    mapping = {"scope":"default","code":"TransactionReconciliationMapping","name":"Mapping Name","reconciliationType":"Transaction","rules":[{"left":"TransactionId","right":"TransactionId","comparisonType":"Equals","weight":10,"isCaseSensitive":false},{"left":"InstrumentUid","right":"InstrumentUid","comparisonType":"Equals","weight":5,"isCaseSensitive":false},{"left":"TransactionPrice","right":"TransactionPrice","comparisonType":"Equals","weight":1,"isCaseSensitive":false},{"left":"TransactionCurrency","right":"TransactionCurrency","comparisonType":"Equals","weight":1,"isCaseSensitive":false},{"left":"TransactionDate","right":"TransactionDate","comparisonType":"SameDate","weight":1,"isCaseSensitive":false},{"left":"SettlementDate","right":"SettlementDate","comparisonType":"SameDate","weight":1,"isCaseSensitive":false},{"left":"CounterpartyId","right":"CounterpartyId","comparisonType":"Equals","weight":1,"isCaseSensitive":false},{"left":"ExchangeRate","right":"ExchangeRate","comparisonType":"WithinPercentage","comparisonValue":0.5,"weight":1,"isCaseSensitive":false},{"left":"Type","right":"Type","comparisonType":"MappedString","weight":1,"mappedStrings":[{"leftValue":"Buy","rightValue":"Purchase","mappingDirection":"BothWays","isCaseSensitive":false}],"isCaseSensitive":false}]} # Mapping | The mapping to be created / updated. (optional)

    try:
        # [EARLY ACCESS] UpsertReconciliationMapping: Create or update a mapping
        api_response = await api_instance.upsert_reconciliation_mapping(mapping=mapping)
        print("The response of ReconciliationsApi->upsert_reconciliation_mapping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReconciliationsApi->upsert_reconciliation_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mapping** | [**Mapping**](Mapping.md)| The mapping to be created / updated. | [optional] 

### Return type

[**Mapping**](Mapping.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The created / updated mapping. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_reconciliation_run**
> ReconciliationRun upsert_reconciliation_run(scope, code, upsert_reconciliation_run_request=upsert_reconciliation_run_request)

[EXPERIMENTAL] UpsertReconciliationRun: Update or Create a reconciliation run

Existing reconciliations will be updated, non-existing ones will be created

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
    api_instance = lusid.ReconciliationsApi(api_client)
    scope = 'scope_example' # str | The scope of the reconciliation associated with the run
    code = 'code_example' # str | The code of the reconciliation associated with the run
    upsert_reconciliation_run_request = {"date":"2018-03-05T00:00:00.0000000+00:00","version":1} # UpsertReconciliationRunRequest | The definition of the reconciliation run (optional)

    try:
        # [EXPERIMENTAL] UpsertReconciliationRun: Update or Create a reconciliation run
        api_response = await api_instance.upsert_reconciliation_run(scope, code, upsert_reconciliation_run_request=upsert_reconciliation_run_request)
        print("The response of ReconciliationsApi->upsert_reconciliation_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReconciliationsApi->upsert_reconciliation_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the reconciliation associated with the run | 
 **code** | **str**| The code of the reconciliation associated with the run | 
 **upsert_reconciliation_run_request** | [**UpsertReconciliationRunRequest**](UpsertReconciliationRunRequest.md)| The definition of the reconciliation run | [optional] 

### Return type

[**ReconciliationRun**](ReconciliationRun.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created reconciliation run |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

