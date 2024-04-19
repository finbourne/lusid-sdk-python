# lusid.ConventionsApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_cds_flow_conventions**](ConventionsApi.md#delete_cds_flow_conventions) | **DELETE** /api/conventions/credit/conventions/{scope}/{code} | [BETA] DeleteCdsFlowConventions: Delete the CDS Flow Conventions of given scope and code, assuming that it is present.
[**delete_flow_conventions**](ConventionsApi.md#delete_flow_conventions) | **DELETE** /api/conventions/rates/flowconventions/{scope}/{code} | [BETA] DeleteFlowConventions: Delete the Flow Conventions of given scope and code, assuming that it is present.
[**delete_index_convention**](ConventionsApi.md#delete_index_convention) | **DELETE** /api/conventions/rates/indexconventions/{scope}/{code} | [BETA] DeleteIndexConvention: Delete the Index Convention of given scope and code, assuming that it is present.
[**get_cds_flow_conventions**](ConventionsApi.md#get_cds_flow_conventions) | **GET** /api/conventions/credit/conventions/{scope}/{code} | [BETA] GetCdsFlowConventions: Get CDS Flow Conventions
[**get_flow_conventions**](ConventionsApi.md#get_flow_conventions) | **GET** /api/conventions/rates/flowconventions/{scope}/{code} | [BETA] GetFlowConventions: Get Flow Conventions
[**get_index_convention**](ConventionsApi.md#get_index_convention) | **GET** /api/conventions/rates/indexconventions/{scope}/{code} | [BETA] GetIndexConvention: Get Index Convention
[**list_cds_flow_conventions**](ConventionsApi.md#list_cds_flow_conventions) | **GET** /api/conventions/credit/conventions | [BETA] ListCdsFlowConventions: List the set of CDS Flow Conventions
[**list_flow_conventions**](ConventionsApi.md#list_flow_conventions) | **GET** /api/conventions/rates/flowconventions | [BETA] ListFlowConventions: List the set of Flow Conventions
[**list_index_convention**](ConventionsApi.md#list_index_convention) | **GET** /api/conventions/rates/indexconventions | [BETA] ListIndexConvention: List the set of Index Conventions
[**upsert_cds_flow_conventions**](ConventionsApi.md#upsert_cds_flow_conventions) | **POST** /api/conventions/credit/conventions | [BETA] UpsertCdsFlowConventions: Upsert a set of CDS Flow Conventions. This creates or updates the data in Lusid.
[**upsert_flow_conventions**](ConventionsApi.md#upsert_flow_conventions) | **POST** /api/conventions/rates/flowconventions | [BETA] UpsertFlowConventions: Upsert Flow Conventions. This creates or updates the data in Lusid.
[**upsert_index_convention**](ConventionsApi.md#upsert_index_convention) | **POST** /api/conventions/rates/indexconventions | [BETA] UpsertIndexConvention: Upsert a set of Index Convention. This creates or updates the data in Lusid.


# **delete_cds_flow_conventions**
> AnnulSingleStructuredDataResponse delete_cds_flow_conventions(scope, code)

[BETA] DeleteCdsFlowConventions: Delete the CDS Flow Conventions of given scope and code, assuming that it is present.

Delete the specified CDS Flow Conventions from a single scope.  The response will return either detail of the deleted item, or an explanation (failure) as to why this did not succeed.  It is important to always check for any unsuccessful response.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.annul_single_structured_data_response import AnnulSingleStructuredDataResponse
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    ConventionsApi,
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
    api_instance = api_client_factory.build(lusid.ConventionsApi)
    scope = 'scope_example' # str | The scope of the CDS Flow Conventions to delete.
    code = 'code_example' # str | The CDS Flow Conventions to delete.

    try:
        # [BETA] DeleteCdsFlowConventions: Delete the CDS Flow Conventions of given scope and code, assuming that it is present.
        api_response = await api_instance.delete_cds_flow_conventions(scope, code)
        print("The response of ConventionsApi->delete_cds_flow_conventions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConventionsApi->delete_cds_flow_conventions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the CDS Flow Conventions to delete. | 
 **code** | **str**| The CDS Flow Conventions to delete. | 

### Return type

[**AnnulSingleStructuredDataResponse**](AnnulSingleStructuredDataResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The AsAt of deletion or failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_flow_conventions**
> AnnulSingleStructuredDataResponse delete_flow_conventions(scope, code)

[BETA] DeleteFlowConventions: Delete the Flow Conventions of given scope and code, assuming that it is present.

Delete the specified conventions from a single scope.  The response will return either detail of the deleted item, or an explanation (failure) as to why this did not succeed.  It is important to always check for any unsuccessful response.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.annul_single_structured_data_response import AnnulSingleStructuredDataResponse
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    ConventionsApi,
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
    api_instance = api_client_factory.build(lusid.ConventionsApi)
    scope = 'scope_example' # str | The scope of the Flow Conventions to delete.
    code = 'code_example' # str | The Flow Conventions to delete.

    try:
        # [BETA] DeleteFlowConventions: Delete the Flow Conventions of given scope and code, assuming that it is present.
        api_response = await api_instance.delete_flow_conventions(scope, code)
        print("The response of ConventionsApi->delete_flow_conventions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConventionsApi->delete_flow_conventions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Flow Conventions to delete. | 
 **code** | **str**| The Flow Conventions to delete. | 

### Return type

[**AnnulSingleStructuredDataResponse**](AnnulSingleStructuredDataResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The AsAt of deletion or failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_index_convention**
> AnnulSingleStructuredDataResponse delete_index_convention(scope, code)

[BETA] DeleteIndexConvention: Delete the Index Convention of given scope and code, assuming that it is present.

Delete the specified Index Convention from a single scope.  The response will return either detail of the deleted item, or an explanation (failure) as to why this did not succeed.  It is important to always check for any unsuccessful response.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.annul_single_structured_data_response import AnnulSingleStructuredDataResponse
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    ConventionsApi,
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
    api_instance = api_client_factory.build(lusid.ConventionsApi)
    scope = 'scope_example' # str | The scope of the Index Convention to delete.
    code = 'code_example' # str | The Index Convention to delete.

    try:
        # [BETA] DeleteIndexConvention: Delete the Index Convention of given scope and code, assuming that it is present.
        api_response = await api_instance.delete_index_convention(scope, code)
        print("The response of ConventionsApi->delete_index_convention:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConventionsApi->delete_index_convention: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Index Convention to delete. | 
 **code** | **str**| The Index Convention to delete. | 

### Return type

[**AnnulSingleStructuredDataResponse**](AnnulSingleStructuredDataResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The AsAt of deletion or failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cds_flow_conventions**
> GetCdsFlowConventionsResponse get_cds_flow_conventions(scope, code, as_at=as_at)

[BETA] GetCdsFlowConventions: Get CDS Flow Conventions

Get a CDS Flow Conventions from a single scope.  The response will return either the conventions that has been stored, or a failure explaining why the request was unsuccessful.  It is important to always check for any unsuccessful requests (failures).

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.get_cds_flow_conventions_response import GetCdsFlowConventionsResponse
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    ConventionsApi,
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
    api_instance = api_client_factory.build(lusid.ConventionsApi)
    scope = 'scope_example' # str | The scope of the CDS Flow Conventions to retrieve.
    code = 'code_example' # str | The name of the CDS Flow Conventions to retrieve the data for.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the CDS Flow Conventions. Defaults to return the latest version if not specified. (optional)

    try:
        # [BETA] GetCdsFlowConventions: Get CDS Flow Conventions
        api_response = await api_instance.get_cds_flow_conventions(scope, code, as_at=as_at)
        print("The response of ConventionsApi->get_cds_flow_conventions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConventionsApi->get_cds_flow_conventions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the CDS Flow Conventions to retrieve. | 
 **code** | **str**| The name of the CDS Flow Conventions to retrieve the data for. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the CDS Flow Conventions. Defaults to return the latest version if not specified. | [optional] 

### Return type

[**GetCdsFlowConventionsResponse**](GetCdsFlowConventionsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully retrieved CDS Flow Conventions or any failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_flow_conventions**
> GetFlowConventionsResponse get_flow_conventions(scope, code, as_at=as_at)

[BETA] GetFlowConventions: Get Flow Conventions

Get a Flow Conventions from a single scope.  The response will return either the conventions that has been stored, or a failure explaining why the request was unsuccessful.  It is important to always check for any unsuccessful requests (failures).

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.get_flow_conventions_response import GetFlowConventionsResponse
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    ConventionsApi,
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
    api_instance = api_client_factory.build(lusid.ConventionsApi)
    scope = 'scope_example' # str | The scope of the Flow Conventions to retrieve.
    code = 'code_example' # str | The name of the Flow Conventions to retrieve the data for.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Flow Conventions. Defaults to return the latest version if not specified. (optional)

    try:
        # [BETA] GetFlowConventions: Get Flow Conventions
        api_response = await api_instance.get_flow_conventions(scope, code, as_at=as_at)
        print("The response of ConventionsApi->get_flow_conventions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConventionsApi->get_flow_conventions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Flow Conventions to retrieve. | 
 **code** | **str**| The name of the Flow Conventions to retrieve the data for. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Flow Conventions. Defaults to return the latest version if not specified. | [optional] 

### Return type

[**GetFlowConventionsResponse**](GetFlowConventionsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully retrieved Flow Conventions or any failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_index_convention**
> GetIndexConventionResponse get_index_convention(scope, code, as_at=as_at)

[BETA] GetIndexConvention: Get Index Convention

Get a Index Convention from a single scope.  The response will return either the conventions that has been stored, or a failure explaining why the request was unsuccessful.  It is important to always check for any unsuccessful requests (failures).

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.get_index_convention_response import GetIndexConventionResponse
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    ConventionsApi,
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
    api_instance = api_client_factory.build(lusid.ConventionsApi)
    scope = 'scope_example' # str | The scope of the Index Convention to retrieve.
    code = 'code_example' # str | The name of the Index Convention to retrieve the data for.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Index Convention. Defaults to return the latest version if not specified. (optional)

    try:
        # [BETA] GetIndexConvention: Get Index Convention
        api_response = await api_instance.get_index_convention(scope, code, as_at=as_at)
        print("The response of ConventionsApi->get_index_convention:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConventionsApi->get_index_convention: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Index Convention to retrieve. | 
 **code** | **str**| The name of the Index Convention to retrieve the data for. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Index Convention. Defaults to return the latest version if not specified. | [optional] 

### Return type

[**GetIndexConventionResponse**](GetIndexConventionResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully retrieved Index Convention or any failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cds_flow_conventions**
> ResourceListOfGetCdsFlowConventionsResponse list_cds_flow_conventions(as_at=as_at)

[BETA] ListCdsFlowConventions: List the set of CDS Flow Conventions

List the set of CDS Flow Conventions at the specified date/time

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.resource_list_of_get_cds_flow_conventions_response import ResourceListOfGetCdsFlowConventionsResponse
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    ConventionsApi,
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
    api_instance = api_client_factory.build(lusid.ConventionsApi)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the conventions. Defaults to latest if not specified. (optional)

    try:
        # [BETA] ListCdsFlowConventions: List the set of CDS Flow Conventions
        api_response = await api_instance.list_cds_flow_conventions(as_at=as_at)
        print("The response of ConventionsApi->list_cds_flow_conventions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConventionsApi->list_cds_flow_conventions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list the conventions. Defaults to latest if not specified. | [optional] 

### Return type

[**ResourceListOfGetCdsFlowConventionsResponse**](ResourceListOfGetCdsFlowConventionsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested CDS Flow conventions |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_flow_conventions**
> ResourceListOfGetFlowConventionsResponse list_flow_conventions(as_at=as_at)

[BETA] ListFlowConventions: List the set of Flow Conventions

List the set of Flow Conventions at the specified date/time

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.resource_list_of_get_flow_conventions_response import ResourceListOfGetFlowConventionsResponse
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    ConventionsApi,
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
    api_instance = api_client_factory.build(lusid.ConventionsApi)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the conventions. Defaults to latest if not specified. (optional)

    try:
        # [BETA] ListFlowConventions: List the set of Flow Conventions
        api_response = await api_instance.list_flow_conventions(as_at=as_at)
        print("The response of ConventionsApi->list_flow_conventions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConventionsApi->list_flow_conventions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list the conventions. Defaults to latest if not specified. | [optional] 

### Return type

[**ResourceListOfGetFlowConventionsResponse**](ResourceListOfGetFlowConventionsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Flow conventions |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_index_convention**
> ResourceListOfGetIndexConventionResponse list_index_convention(as_at=as_at)

[BETA] ListIndexConvention: List the set of Index Conventions

List the set of Index Conventions at the specified date/time

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.resource_list_of_get_index_convention_response import ResourceListOfGetIndexConventionResponse
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    ConventionsApi,
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
    api_instance = api_client_factory.build(lusid.ConventionsApi)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the conventions. Defaults to latest if not specified. (optional)

    try:
        # [BETA] ListIndexConvention: List the set of Index Conventions
        api_response = await api_instance.list_index_convention(as_at=as_at)
        print("The response of ConventionsApi->list_index_convention:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConventionsApi->list_index_convention: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list the conventions. Defaults to latest if not specified. | [optional] 

### Return type

[**ResourceListOfGetIndexConventionResponse**](ResourceListOfGetIndexConventionResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Index conventions |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_cds_flow_conventions**
> UpsertSingleStructuredDataResponse upsert_cds_flow_conventions(upsert_cds_flow_conventions_request)

[BETA] UpsertCdsFlowConventions: Upsert a set of CDS Flow Conventions. This creates or updates the data in Lusid.

Update or insert CDS Flow Conventions in a single scope. An item will be updated if it already exists  and inserted if it does not.                The response will return the successfully updated or inserted CDS Flow Conventions or failure message if unsuccessful                It is important to always check to verify success (or failure).

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.upsert_cds_flow_conventions_request import UpsertCdsFlowConventionsRequest
from lusid.models.upsert_single_structured_data_response import UpsertSingleStructuredDataResponse
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    ConventionsApi,
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
    api_instance = api_client_factory.build(lusid.ConventionsApi)
    upsert_cds_flow_conventions_request = {"cdsFlowConventions":{"rollFrequency":"3M","currency":"USD","paymentFrequency":"3M","dayCountConvention":"Act360","rollConvention":"20","paymentCalendars":["NYC"],"resetCalendars":["NYC"],"settleDays":0,"resetDays":0,"businessDayConvention":"Following","scope":"someScope","code":"exampleCdsFlowConventionsName"}} # UpsertCdsFlowConventionsRequest | The CDS Flow Conventions to update or insert

    try:
        # [BETA] UpsertCdsFlowConventions: Upsert a set of CDS Flow Conventions. This creates or updates the data in Lusid.
        api_response = await api_instance.upsert_cds_flow_conventions(upsert_cds_flow_conventions_request)
        print("The response of ConventionsApi->upsert_cds_flow_conventions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConventionsApi->upsert_cds_flow_conventions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_cds_flow_conventions_request** | [**UpsertCdsFlowConventionsRequest**](UpsertCdsFlowConventionsRequest.md)| The CDS Flow Conventions to update or insert | 

### Return type

[**UpsertSingleStructuredDataResponse**](UpsertSingleStructuredDataResponse.md)

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

# **upsert_flow_conventions**
> UpsertSingleStructuredDataResponse upsert_flow_conventions(upsert_flow_conventions_request)

[BETA] UpsertFlowConventions: Upsert Flow Conventions. This creates or updates the data in Lusid.

Update or insert Flow Conventions in a single scope. An item will be updated if it already exists  and inserted if it does not.                The response will return the successfully updated or inserted Flow Conventions or failure message if unsuccessful                It is important to always check to verify success (or failure).

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.upsert_flow_conventions_request import UpsertFlowConventionsRequest
from lusid.models.upsert_single_structured_data_response import UpsertSingleStructuredDataResponse
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    ConventionsApi,
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
    api_instance = api_client_factory.build(lusid.ConventionsApi)
    upsert_flow_conventions_request = {"flowConventions":{"currency":"GBP","paymentFrequency":"1Y","dayCountConvention":"Act360","rollConvention":"None","paymentCalendars":["LON"],"resetCalendars":["LON"],"settleDays":2,"resetDays":2,"leapDaysIncluded":true,"accrualDateAdjustment":"Adjusted","businessDayConvention":"Following","accrualDayCountConvention":"Act360","scope":"someScope","code":"exampleFlowConventionsName"}} # UpsertFlowConventionsRequest | The Flow Conventions to update or insert

    try:
        # [BETA] UpsertFlowConventions: Upsert Flow Conventions. This creates or updates the data in Lusid.
        api_response = await api_instance.upsert_flow_conventions(upsert_flow_conventions_request)
        print("The response of ConventionsApi->upsert_flow_conventions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConventionsApi->upsert_flow_conventions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_flow_conventions_request** | [**UpsertFlowConventionsRequest**](UpsertFlowConventionsRequest.md)| The Flow Conventions to update or insert | 

### Return type

[**UpsertSingleStructuredDataResponse**](UpsertSingleStructuredDataResponse.md)

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

# **upsert_index_convention**
> UpsertSingleStructuredDataResponse upsert_index_convention(upsert_index_convention_request)

[BETA] UpsertIndexConvention: Upsert a set of Index Convention. This creates or updates the data in Lusid.

Update or insert Index Convention in a single scope. An item will be updated if it already exists  and inserted if it does not.                The response will return the successfully updated or inserted Index Convention or failure message if unsuccessful                It is important to always check to verify success (or failure).

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.upsert_index_convention_request import UpsertIndexConventionRequest
from lusid.models.upsert_single_structured_data_response import UpsertSingleStructuredDataResponse
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    ConventionsApi,
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
    api_instance = api_client_factory.build(lusid.ConventionsApi)
    upsert_index_convention_request = {"indexConvention":{"fixingReference":"Unknown","publicationDayLag":2,"paymentTenor":"1Y","dayCountConvention":"Act360","currency":"GBP","indexName":"LIBOR","scope":"someScope","code":"exampleIndexonventionsName"}} # UpsertIndexConventionRequest | The Index Conventions to update or insert

    try:
        # [BETA] UpsertIndexConvention: Upsert a set of Index Convention. This creates or updates the data in Lusid.
        api_response = await api_instance.upsert_index_convention(upsert_index_convention_request)
        print("The response of ConventionsApi->upsert_index_convention:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConventionsApi->upsert_index_convention: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_index_convention_request** | [**UpsertIndexConventionRequest**](UpsertIndexConventionRequest.md)| The Index Conventions to update or insert | 

### Return type

[**UpsertSingleStructuredDataResponse**](UpsertSingleStructuredDataResponse.md)

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

