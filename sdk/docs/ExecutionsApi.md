# lusid.ExecutionsApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_execution**](ExecutionsApi.md#delete_execution) | **DELETE** /api/executions/{scope}/{code} | [EARLY ACCESS] DeleteExecution: Delete execution
[**get_execution**](ExecutionsApi.md#get_execution) | **GET** /api/executions/{scope}/{code} | [EARLY ACCESS] GetExecution: Get Execution
[**list_executions**](ExecutionsApi.md#list_executions) | **GET** /api/executions | [EARLY ACCESS] ListExecutions: List Executions
[**upsert_executions**](ExecutionsApi.md#upsert_executions) | **POST** /api/executions | [EARLY ACCESS] UpsertExecutions: Upsert Execution


# **delete_execution**
> DeletedEntityResponse delete_execution(scope, code)

[EARLY ACCESS] DeleteExecution: Delete execution

Delete an execution. Deletion will be valid from the execution's creation datetime.  This means that the execution will no longer exist at any effective datetime from the asAt datetime of deletion.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from lusid.models.deleted_entity_response import DeletedEntityResponse
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
    api_instance = api_client_factory.build(lusid.ExecutionsApi)
    scope = 'scope_example' # str | The execution scope.
    code = 'code_example' # str | The execution's code. This, together with the scope uniquely identifies the execution to delete.

    try:
        # [EARLY ACCESS] DeleteExecution: Delete execution
        api_response = await api_instance.delete_execution(scope, code)
        print("The response of ExecutionsApi->delete_execution:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExecutionsApi->delete_execution: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The execution scope. | 
 **code** | **str**| The execution&#39;s code. This, together with the scope uniquely identifies the execution to delete. | 

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
**200** | The response from deleting an execution. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_execution**
> Execution get_execution(scope, code, as_at=as_at, property_keys=property_keys)

[EARLY ACCESS] GetExecution: Get Execution

Fetch a Execution that matches the specified identifier

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from lusid.models.execution import Execution
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
    api_instance = api_client_factory.build(lusid.ExecutionsApi)
    scope = 'scope_example' # str | The scope to which the execution belongs.
    code = 'code_example' # str | The execution's unique identifier.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the execution. Defaults to return the latest version of the execution if not specified. (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the \"Execution\" domain to decorate onto the execution.              These take the format {domain}/{scope}/{code} e.g. \"Execution/system/Name\". (optional)

    try:
        # [EARLY ACCESS] GetExecution: Get Execution
        api_response = await api_instance.get_execution(scope, code, as_at=as_at, property_keys=property_keys)
        print("The response of ExecutionsApi->get_execution:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExecutionsApi->get_execution: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope to which the execution belongs. | 
 **code** | **str**| The execution&#39;s unique identifier. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the execution. Defaults to return the latest version of the execution if not specified. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the \&quot;Execution\&quot; domain to decorate onto the execution.              These take the format {domain}/{scope}/{code} e.g. \&quot;Execution/system/Name\&quot;. | [optional] 

### Return type

[**Execution**](Execution.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The execution matching the given identifier. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_executions**
> PagedResourceListOfExecution list_executions(as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter, property_keys=property_keys)

[EARLY ACCESS] ListExecutions: List Executions

Fetch the last pre-AsAt date version of each execution in scope (does not fetch the entire history).

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from lusid.models.paged_resource_list_of_execution import PagedResourceListOfExecution
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
    api_instance = api_client_factory.build(lusid.ExecutionsApi)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the execution. Defaults to return the latest version of the execution if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing execution from a previous call to list executions.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields              must not have changed since the original request. (optional)
    sort_by = ['sort_by_example'] # List[str] | A list of field names or properties to sort by, each suffixed by \" ASC\" or \" DESC\" (optional)
    limit = 56 # int | When paginating, limit the number of returned results to this many. (optional)
    filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid. (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the \"Execution\" domain to decorate onto each execution.                  These take the format {domain}/{scope}/{code} e.g. \"Execution/system/Name\". (optional)

    try:
        # [EARLY ACCESS] ListExecutions: List Executions
        api_response = await api_instance.list_executions(as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter, property_keys=property_keys)
        print("The response of ExecutionsApi->list_executions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExecutionsApi->list_executions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to retrieve the execution. Defaults to return the latest version of the execution if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing execution from a previous call to list executions.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields              must not have changed since the original request. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot; | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the \&quot;Execution\&quot; domain to decorate onto each execution.                  These take the format {domain}/{scope}/{code} e.g. \&quot;Execution/system/Name\&quot;. | [optional] 

### Return type

[**PagedResourceListOfExecution**](PagedResourceListOfExecution.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Executions in scope. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_executions**
> ResourceListOfExecution upsert_executions(execution_set_request=execution_set_request)

[EARLY ACCESS] UpsertExecutions: Upsert Execution

Upsert; update existing executions with given ids, or create new executions otherwise.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from lusid.models.execution_set_request import ExecutionSetRequest
from lusid.models.resource_list_of_execution import ResourceListOfExecution
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
    api_instance = api_client_factory.build(lusid.ExecutionsApi)
    execution_set_request = {"requests":[{"id":{"scope":"MyScope","code":"EXEC00000123"},"placementId":{"scope":"MyScope","code":"PLAC00000123"},"properties":{"Execution/MyScope/SomeExecutionProperty":{"key":"Execution/MyScope/SomeExecutionProperty","value":{"labelValue":"XYZ000034567"}}},"instrumentIdentifiers":{"Instrument/default/Currency":"GBP"},"quantity":100,"state":"New","side":"Buy","type":"Limit","createdDate":"2006-04-11T00:00:00.0000000+00:00","settlementDate":"2006-04-13T00:00:00.0000000+00:00","price":{"amount":12413.33,"currency":"USD"},"settlementCurrency":"GBP","settlementCurrencyFxRate":0.67,"counterparty":"SomeCounterparty","averagePrice":12419.2}]} # ExecutionSetRequest | The collection of execution requests. (optional)

    try:
        # [EARLY ACCESS] UpsertExecutions: Upsert Execution
        api_response = await api_instance.upsert_executions(execution_set_request=execution_set_request)
        print("The response of ExecutionsApi->upsert_executions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExecutionsApi->upsert_executions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execution_set_request** | [**ExecutionSetRequest**](ExecutionSetRequest.md)| The collection of execution requests. | [optional] 

### Return type

[**ResourceListOfExecution**](ResourceListOfExecution.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A collection of executions. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

