# lusid.ConventionsApi

All URIs are relative to *https://fbn-prd.lusid.com/api*

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

Delete the specified CDS Flow Conventions from a single scope. The response will return either detail of the deleted item, or an explanation (failure) as to why this did not succeed. It is important to always check for any unsuccessful response.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    ConventionsApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "lusidUrl":"https://<your-domain>.lusid.com/api",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the lusid SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(ConventionsApi)
    scope = 'scope_example' # str | The scope of the CDS Flow Conventions to delete.
    code = 'code_example' # str | The CDS Flow Conventions to delete.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_cds_flow_conventions(scope, code, opts=opts)

        # [BETA] DeleteCdsFlowConventions: Delete the CDS Flow Conventions of given scope and code, assuming that it is present.
        api_response = api_instance.delete_cds_flow_conventions(scope, code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ConventionsApi->delete_cds_flow_conventions: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the CDS Flow Conventions to delete. | 
 **code** | **str**| The CDS Flow Conventions to delete. | 

### Return type

[**AnnulSingleStructuredDataResponse**](AnnulSingleStructuredDataResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The AsAt of deletion or failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_flow_conventions**
> AnnulSingleStructuredDataResponse delete_flow_conventions(scope, code)

[BETA] DeleteFlowConventions: Delete the Flow Conventions of given scope and code, assuming that it is present.

Delete the specified conventions from a single scope. The response will return either detail of the deleted item, or an explanation (failure) as to why this did not succeed. It is important to always check for any unsuccessful response.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    ConventionsApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "lusidUrl":"https://<your-domain>.lusid.com/api",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the lusid SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(ConventionsApi)
    scope = 'scope_example' # str | The scope of the Flow Conventions to delete.
    code = 'code_example' # str | The Flow Conventions to delete.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_flow_conventions(scope, code, opts=opts)

        # [BETA] DeleteFlowConventions: Delete the Flow Conventions of given scope and code, assuming that it is present.
        api_response = api_instance.delete_flow_conventions(scope, code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ConventionsApi->delete_flow_conventions: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Flow Conventions to delete. | 
 **code** | **str**| The Flow Conventions to delete. | 

### Return type

[**AnnulSingleStructuredDataResponse**](AnnulSingleStructuredDataResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The AsAt of deletion or failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_index_convention**
> AnnulSingleStructuredDataResponse delete_index_convention(scope, code)

[BETA] DeleteIndexConvention: Delete the Index Convention of given scope and code, assuming that it is present.

Delete the specified Index Convention from a single scope. The response will return either detail of the deleted item, or an explanation (failure) as to why this did not succeed. It is important to always check for any unsuccessful response.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    ConventionsApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "lusidUrl":"https://<your-domain>.lusid.com/api",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the lusid SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(ConventionsApi)
    scope = 'scope_example' # str | The scope of the Index Convention to delete.
    code = 'code_example' # str | The Index Convention to delete.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_index_convention(scope, code, opts=opts)

        # [BETA] DeleteIndexConvention: Delete the Index Convention of given scope and code, assuming that it is present.
        api_response = api_instance.delete_index_convention(scope, code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ConventionsApi->delete_index_convention: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Index Convention to delete. | 
 **code** | **str**| The Index Convention to delete. | 

### Return type

[**AnnulSingleStructuredDataResponse**](AnnulSingleStructuredDataResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The AsAt of deletion or failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_cds_flow_conventions**
> GetCdsFlowConventionsResponse get_cds_flow_conventions(scope, code, as_at=as_at)

[BETA] GetCdsFlowConventions: Get CDS Flow Conventions

Get a CDS Flow Conventions from a single scope. The response will return either the conventions that has been stored, or a failure explaining why the request was unsuccessful. It is important to always check for any unsuccessful requests (failures).

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    ConventionsApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "lusidUrl":"https://<your-domain>.lusid.com/api",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the lusid SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(ConventionsApi)
    scope = 'scope_example' # str | The scope of the CDS Flow Conventions to retrieve.
    code = 'code_example' # str | The name of the CDS Flow Conventions to retrieve the data for.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the CDS Flow Conventions. Defaults to return the latest version if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_cds_flow_conventions(scope, code, as_at=as_at, opts=opts)

        # [BETA] GetCdsFlowConventions: Get CDS Flow Conventions
        api_response = api_instance.get_cds_flow_conventions(scope, code, as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ConventionsApi->get_cds_flow_conventions: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the CDS Flow Conventions to retrieve. | 
 **code** | **str**| The name of the CDS Flow Conventions to retrieve the data for. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the CDS Flow Conventions. Defaults to return the latest version if not specified. | [optional] 

### Return type

[**GetCdsFlowConventionsResponse**](GetCdsFlowConventionsResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully retrieved CDS Flow Conventions or any failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_flow_conventions**
> GetFlowConventionsResponse get_flow_conventions(scope, code, as_at=as_at)

[BETA] GetFlowConventions: Get Flow Conventions

Get a Flow Conventions from a single scope. The response will return either the conventions that has been stored, or a failure explaining why the request was unsuccessful. It is important to always check for any unsuccessful requests (failures).

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    ConventionsApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "lusidUrl":"https://<your-domain>.lusid.com/api",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the lusid SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(ConventionsApi)
    scope = 'scope_example' # str | The scope of the Flow Conventions to retrieve.
    code = 'code_example' # str | The name of the Flow Conventions to retrieve the data for.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Flow Conventions. Defaults to return the latest version if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_flow_conventions(scope, code, as_at=as_at, opts=opts)

        # [BETA] GetFlowConventions: Get Flow Conventions
        api_response = api_instance.get_flow_conventions(scope, code, as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ConventionsApi->get_flow_conventions: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Flow Conventions to retrieve. | 
 **code** | **str**| The name of the Flow Conventions to retrieve the data for. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Flow Conventions. Defaults to return the latest version if not specified. | [optional] 

### Return type

[**GetFlowConventionsResponse**](GetFlowConventionsResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully retrieved Flow Conventions or any failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_index_convention**
> GetIndexConventionResponse get_index_convention(scope, code, as_at=as_at)

[BETA] GetIndexConvention: Get Index Convention

Get a Index Convention from a single scope. The response will return either the conventions that has been stored, or a failure explaining why the request was unsuccessful. It is important to always check for any unsuccessful requests (failures).

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    ConventionsApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "lusidUrl":"https://<your-domain>.lusid.com/api",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the lusid SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(ConventionsApi)
    scope = 'scope_example' # str | The scope of the Index Convention to retrieve.
    code = 'code_example' # str | The name of the Index Convention to retrieve the data for.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Index Convention. Defaults to return the latest version if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_index_convention(scope, code, as_at=as_at, opts=opts)

        # [BETA] GetIndexConvention: Get Index Convention
        api_response = api_instance.get_index_convention(scope, code, as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ConventionsApi->get_index_convention: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Index Convention to retrieve. | 
 **code** | **str**| The name of the Index Convention to retrieve the data for. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Index Convention. Defaults to return the latest version if not specified. | [optional] 

### Return type

[**GetIndexConventionResponse**](GetIndexConventionResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully retrieved Index Convention or any failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_cds_flow_conventions**
> ResourceListOfGetCdsFlowConventionsResponse list_cds_flow_conventions(as_at=as_at)

[BETA] ListCdsFlowConventions: List the set of CDS Flow Conventions

List the set of CDS Flow Conventions at the specified date/time

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    ConventionsApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "lusidUrl":"https://<your-domain>.lusid.com/api",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the lusid SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(ConventionsApi)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the conventions. Defaults to latest if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_cds_flow_conventions(as_at=as_at, opts=opts)

        # [BETA] ListCdsFlowConventions: List the set of CDS Flow Conventions
        api_response = api_instance.list_cds_flow_conventions(as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ConventionsApi->list_cds_flow_conventions: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list the conventions. Defaults to latest if not specified. | [optional] 

### Return type

[**ResourceListOfGetCdsFlowConventionsResponse**](ResourceListOfGetCdsFlowConventionsResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested CDS Flow conventions |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_flow_conventions**
> ResourceListOfGetFlowConventionsResponse list_flow_conventions(as_at=as_at)

[BETA] ListFlowConventions: List the set of Flow Conventions

List the set of Flow Conventions at the specified date/time

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    ConventionsApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "lusidUrl":"https://<your-domain>.lusid.com/api",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the lusid SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(ConventionsApi)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the conventions. Defaults to latest if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_flow_conventions(as_at=as_at, opts=opts)

        # [BETA] ListFlowConventions: List the set of Flow Conventions
        api_response = api_instance.list_flow_conventions(as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ConventionsApi->list_flow_conventions: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list the conventions. Defaults to latest if not specified. | [optional] 

### Return type

[**ResourceListOfGetFlowConventionsResponse**](ResourceListOfGetFlowConventionsResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Flow conventions |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_index_convention**
> ResourceListOfGetIndexConventionResponse list_index_convention(as_at=as_at)

[BETA] ListIndexConvention: List the set of Index Conventions

List the set of Index Conventions at the specified date/time

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    ConventionsApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "lusidUrl":"https://<your-domain>.lusid.com/api",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the lusid SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(ConventionsApi)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the conventions. Defaults to latest if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_index_convention(as_at=as_at, opts=opts)

        # [BETA] ListIndexConvention: List the set of Index Conventions
        api_response = api_instance.list_index_convention(as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ConventionsApi->list_index_convention: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list the conventions. Defaults to latest if not specified. | [optional] 

### Return type

[**ResourceListOfGetIndexConventionResponse**](ResourceListOfGetIndexConventionResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Index conventions |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **upsert_cds_flow_conventions**
> UpsertSingleStructuredDataResponse upsert_cds_flow_conventions(upsert_cds_flow_conventions_request)

[BETA] UpsertCdsFlowConventions: Upsert a set of CDS Flow Conventions. This creates or updates the data in Lusid.

Update or insert CDS Flow Conventions in a single scope. An item will be updated if it already exists and inserted if it does not.              The response will return the successfully updated or inserted CDS Flow Conventions or failure message if unsuccessful              It is important to always check to verify success (or failure).

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    ConventionsApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "lusidUrl":"https://<your-domain>.lusid.com/api",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the lusid SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(ConventionsApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # upsert_cds_flow_conventions_request = UpsertCdsFlowConventionsRequest.from_json("")
    # upsert_cds_flow_conventions_request = UpsertCdsFlowConventionsRequest.from_dict({})
    upsert_cds_flow_conventions_request = UpsertCdsFlowConventionsRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.upsert_cds_flow_conventions(upsert_cds_flow_conventions_request, opts=opts)

        # [BETA] UpsertCdsFlowConventions: Upsert a set of CDS Flow Conventions. This creates or updates the data in Lusid.
        api_response = api_instance.upsert_cds_flow_conventions(upsert_cds_flow_conventions_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ConventionsApi->upsert_cds_flow_conventions: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_cds_flow_conventions_request** | [**UpsertCdsFlowConventionsRequest**](UpsertCdsFlowConventionsRequest.md)| The CDS Flow Conventions to update or insert | 

### Return type

[**UpsertSingleStructuredDataResponse**](UpsertSingleStructuredDataResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully updated or inserted item or any failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **upsert_flow_conventions**
> UpsertSingleStructuredDataResponse upsert_flow_conventions(upsert_flow_conventions_request)

[BETA] UpsertFlowConventions: Upsert Flow Conventions. This creates or updates the data in Lusid.

Update or insert Flow Conventions in a single scope. An item will be updated if it already exists and inserted if it does not.              The response will return the successfully updated or inserted Flow Conventions or failure message if unsuccessful              It is important to always check to verify success (or failure).

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    ConventionsApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "lusidUrl":"https://<your-domain>.lusid.com/api",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the lusid SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(ConventionsApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # upsert_flow_conventions_request = UpsertFlowConventionsRequest.from_json("")
    # upsert_flow_conventions_request = UpsertFlowConventionsRequest.from_dict({})
    upsert_flow_conventions_request = UpsertFlowConventionsRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.upsert_flow_conventions(upsert_flow_conventions_request, opts=opts)

        # [BETA] UpsertFlowConventions: Upsert Flow Conventions. This creates or updates the data in Lusid.
        api_response = api_instance.upsert_flow_conventions(upsert_flow_conventions_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ConventionsApi->upsert_flow_conventions: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_flow_conventions_request** | [**UpsertFlowConventionsRequest**](UpsertFlowConventionsRequest.md)| The Flow Conventions to update or insert | 

### Return type

[**UpsertSingleStructuredDataResponse**](UpsertSingleStructuredDataResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully updated or inserted item or any failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **upsert_index_convention**
> UpsertSingleStructuredDataResponse upsert_index_convention(upsert_index_convention_request)

[BETA] UpsertIndexConvention: Upsert a set of Index Convention. This creates or updates the data in Lusid.

Update or insert Index Convention in a single scope. An item will be updated if it already exists and inserted if it does not.              The response will return the successfully updated or inserted Index Convention or failure message if unsuccessful              It is important to always check to verify success (or failure).

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    ConventionsApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "lusidUrl":"https://<your-domain>.lusid.com/api",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the lusid SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(ConventionsApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # upsert_index_convention_request = UpsertIndexConventionRequest.from_json("")
    # upsert_index_convention_request = UpsertIndexConventionRequest.from_dict({})
    upsert_index_convention_request = UpsertIndexConventionRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.upsert_index_convention(upsert_index_convention_request, opts=opts)

        # [BETA] UpsertIndexConvention: Upsert a set of Index Convention. This creates or updates the data in Lusid.
        api_response = api_instance.upsert_index_convention(upsert_index_convention_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ConventionsApi->upsert_index_convention: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_index_convention_request** | [**UpsertIndexConventionRequest**](UpsertIndexConventionRequest.md)| The Index Conventions to update or insert | 

### Return type

[**UpsertSingleStructuredDataResponse**](UpsertSingleStructuredDataResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully updated or inserted item or any failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

