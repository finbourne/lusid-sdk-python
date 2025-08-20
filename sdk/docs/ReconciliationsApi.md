# lusid.ReconciliationsApi

All URIs are relative to *https://fbn-prd.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_scheduled_reconciliation**](ReconciliationsApi.md#create_scheduled_reconciliation) | **POST** /api/portfolios/$scheduledReconciliations/{scope} | [EXPERIMENTAL] CreateScheduledReconciliation: Create a scheduled reconciliation
[**delete_reconciliation**](ReconciliationsApi.md#delete_reconciliation) | **DELETE** /api/portfolios/$scheduledReconciliations/{scope}/{code} | [EXPERIMENTAL] DeleteReconciliation: Delete scheduled reconciliation
[**delete_reconciliation_mapping**](ReconciliationsApi.md#delete_reconciliation_mapping) | **DELETE** /api/portfolios/mapping/{scope}/{code} | [EARLY ACCESS] DeleteReconciliationMapping: Delete a mapping
[**get_reconciliation**](ReconciliationsApi.md#get_reconciliation) | **GET** /api/portfolios/$scheduledReconciliations/{scope}/{code} | [EXPERIMENTAL] GetReconciliation: Get scheduled reconciliation
[**get_reconciliation_mapping**](ReconciliationsApi.md#get_reconciliation_mapping) | **GET** /api/portfolios/mapping/{scope}/{code} | [EARLY ACCESS] GetReconciliationMapping: Get a mapping
[**list_reconciliation_mappings**](ReconciliationsApi.md#list_reconciliation_mappings) | **GET** /api/portfolios/mapping | [EARLY ACCESS] ListReconciliationMappings: List the reconciliation mappings
[**list_reconciliations**](ReconciliationsApi.md#list_reconciliations) | **GET** /api/portfolios/$scheduledReconciliations | [EXPERIMENTAL] ListReconciliations: List scheduled reconciliations
[**reconcile_generic**](ReconciliationsApi.md#reconcile_generic) | **POST** /api/portfolios/$reconcileGeneric | ReconcileGeneric: Reconcile either holdings or valuations performed on one or two sets of holdings using one or two configuration recipes.              The output is configurable for various types of comparisons, to allow tolerances on numerical and date-time data or case-insensitivity on strings, and elision of resulting differences where they are &#39;empty&#39; or null or zero.
[**reconcile_holdings**](ReconciliationsApi.md#reconcile_holdings) | **POST** /api/portfolios/$reconcileholdings | [EARLY ACCESS] ReconcileHoldings: Reconcile portfolio holdings
[**reconcile_inline**](ReconciliationsApi.md#reconcile_inline) | **POST** /api/portfolios/$reconcileInline | ReconcileInline: Reconcile valuations performed on one or two sets of inline instruments using one or two configuration recipes.
[**reconcile_transactions**](ReconciliationsApi.md#reconcile_transactions) | **POST** /api/portfolios/$reconcileTransactions | [EARLY ACCESS] ReconcileTransactions: Perform a Transactions Reconciliation.
[**reconcile_transactions_v2**](ReconciliationsApi.md#reconcile_transactions_v2) | **POST** /api/portfolios/$reconcileTransactionsV2 | [EXPERIMENTAL] ReconcileTransactionsV2: Perform a Transactions Reconciliation.
[**reconcile_valuation**](ReconciliationsApi.md#reconcile_valuation) | **POST** /api/portfolios/$reconcileValuation | ReconcileValuation: Reconcile valuations performed on one or two sets of holdings using one or two configuration recipes.
[**update_reconciliation**](ReconciliationsApi.md#update_reconciliation) | **POST** /api/portfolios/$scheduledReconciliations/{scope}/{code} | [EXPERIMENTAL] UpdateReconciliation: Update scheduled reconciliation
[**upsert_reconciliation_mapping**](ReconciliationsApi.md#upsert_reconciliation_mapping) | **POST** /api/portfolios/mapping | [EARLY ACCESS] UpsertReconciliationMapping: Create or update a mapping


# **create_scheduled_reconciliation**
> Reconciliation create_scheduled_reconciliation(scope, create_reconciliation_request=create_reconciliation_request)

[EXPERIMENTAL] CreateScheduledReconciliation: Create a scheduled reconciliation

Create a scheduled reconciliation for the given request

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    ReconciliationsApi
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
    api_instance = api_client_factory.build(ReconciliationsApi)
    scope = 'scope_example' # str | The scope of the reconciliation

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # create_reconciliation_request = CreateReconciliationRequest.from_json("")
    # create_reconciliation_request = CreateReconciliationRequest.from_dict({})
    create_reconciliation_request = CreateReconciliationRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.create_scheduled_reconciliation(scope, create_reconciliation_request=create_reconciliation_request, opts=opts)

        # [EXPERIMENTAL] CreateScheduledReconciliation: Create a scheduled reconciliation
        api_response = api_instance.create_scheduled_reconciliation(scope, create_reconciliation_request=create_reconciliation_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ReconciliationsApi->create_scheduled_reconciliation: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the reconciliation | 
 **create_reconciliation_request** | [**CreateReconciliationRequest**](CreateReconciliationRequest.md)| The definition of the reconciliation | [optional] 

### Return type

[**Reconciliation**](Reconciliation.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created scheduled reconciliation |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_reconciliation**
> DeletedEntityResponse delete_reconciliation(scope, code)

[EXPERIMENTAL] DeleteReconciliation: Delete scheduled reconciliation

Delete the given scheduled reconciliation

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    ReconciliationsApi
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
    api_instance = api_client_factory.build(ReconciliationsApi)
    scope = 'scope_example' # str | The scope of the scheduled reconciliation
    code = 'code_example' # str | The code of the scheduled reconciliation

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_reconciliation(scope, code, opts=opts)

        # [EXPERIMENTAL] DeleteReconciliation: Delete scheduled reconciliation
        api_response = api_instance.delete_reconciliation(scope, code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ReconciliationsApi->delete_reconciliation: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the scheduled reconciliation | 
 **code** | **str**| The code of the scheduled reconciliation | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The reconciliation at the requested as at was deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_reconciliation_mapping**
> str delete_reconciliation_mapping(scope, code)

[EARLY ACCESS] DeleteReconciliationMapping: Delete a mapping

Deletes the mapping identified by the scope and code

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    ReconciliationsApi
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
    api_instance = api_client_factory.build(ReconciliationsApi)
    scope = 'scope_example' # str | The scope of the mapping.
    code = 'code_example' # str | The code fof the mapping.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_reconciliation_mapping(scope, code, opts=opts)

        # [EARLY ACCESS] DeleteReconciliationMapping: Delete a mapping
        api_response = api_instance.delete_reconciliation_mapping(scope, code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ReconciliationsApi->delete_reconciliation_mapping: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the mapping. | 
 **code** | **str**| The code fof the mapping. | 

### Return type

**str**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A string specifying the scope and code that were deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_reconciliation**
> Reconciliation get_reconciliation(scope, code, effective_at=effective_at, as_at=as_at, property_keys=property_keys)

[EXPERIMENTAL] GetReconciliation: Get scheduled reconciliation

Get the requested scheduled reconciliation

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    ReconciliationsApi
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
    api_instance = api_client_factory.build(ReconciliationsApi)
    scope = 'scope_example' # str | The scope of the scheduled reconciliation
    code = 'code_example' # str | The code of the scheduled reconciliation
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve the scheduled reconciliation. Defaults to the current LUSID system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the scheduled reconciliation. Defaults to returning the latest version of the reconciliation if not specified. (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the 'Reconciliation' property domain to decorate onto the reconciliation.             These must take the form {domain}/{scope}/{code}, for example 'Reconciliation/Broker/Id'. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_reconciliation(scope, code, effective_at=effective_at, as_at=as_at, property_keys=property_keys, opts=opts)

        # [EXPERIMENTAL] GetReconciliation: Get scheduled reconciliation
        api_response = api_instance.get_reconciliation(scope, code, effective_at=effective_at, as_at=as_at, property_keys=property_keys)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ReconciliationsApi->get_reconciliation: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the scheduled reconciliation | 
 **code** | **str**| The code of the scheduled reconciliation | 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the scheduled reconciliation. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the scheduled reconciliation. Defaults to returning the latest version of the reconciliation if not specified. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;Reconciliation&#39; property domain to decorate onto the reconciliation.             These must take the form {domain}/{scope}/{code}, for example &#39;Reconciliation/Broker/Id&#39;. | [optional] 

### Return type

[**Reconciliation**](Reconciliation.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested scheduled reconciliation |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_reconciliation_mapping**
> Mapping get_reconciliation_mapping(scope, code)

[EARLY ACCESS] GetReconciliationMapping: Get a mapping

Gets a mapping identified by the given scope and code

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    ReconciliationsApi
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
    api_instance = api_client_factory.build(ReconciliationsApi)
    scope = 'scope_example' # str | The scope of the mapping.
    code = 'code_example' # str | The code of the mapping.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_reconciliation_mapping(scope, code, opts=opts)

        # [EARLY ACCESS] GetReconciliationMapping: Get a mapping
        api_response = api_instance.get_reconciliation_mapping(scope, code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ReconciliationsApi->get_reconciliation_mapping: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the mapping. | 
 **code** | **str**| The code of the mapping. | 

### Return type

[**Mapping**](Mapping.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The mapping with the specified scope/code. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_reconciliation_mappings**
> ResourceListOfMapping list_reconciliation_mappings(reconciliation_type=reconciliation_type)

[EARLY ACCESS] ListReconciliationMappings: List the reconciliation mappings

Lists all mappings this user is entitled to see

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    ReconciliationsApi
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
    api_instance = api_client_factory.build(ReconciliationsApi)
    reconciliation_type = 'reconciliation_type_example' # str | Optional parameter to specify which type of mappings should be returned. Defaults to Transaction if not provided. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_reconciliation_mappings(reconciliation_type=reconciliation_type, opts=opts)

        # [EARLY ACCESS] ListReconciliationMappings: List the reconciliation mappings
        api_response = api_instance.list_reconciliation_mappings(reconciliation_type=reconciliation_type)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ReconciliationsApi->list_reconciliation_mappings: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reconciliation_type** | **str**| Optional parameter to specify which type of mappings should be returned. Defaults to Transaction if not provided. | [optional] 

### Return type

[**ResourceListOfMapping**](ResourceListOfMapping.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The mappings that the caller has access to. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_reconciliations**
> PagedResourceListOfReconciliation list_reconciliations(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, property_keys=property_keys)

[EXPERIMENTAL] ListReconciliations: List scheduled reconciliations

List all the scheduled reconciliations matching particular criteria

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    ReconciliationsApi
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
    api_instance = api_client_factory.build(ReconciliationsApi)
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to list the TimeVariant properties for the reconciliation. Defaults to the current LUSID             system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the reconciliation. Defaults to returning the latest version             of each reconciliation if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing reconciliations; this             value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt             and asAt fields must not have changed since the original request. (optional)
    limit = 56 # int | When paginating, limit the results to this number. Defaults to 100 if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the results.             For example, to filter on the reconciliation type, specify \"id.Code eq '001'\". For more information about filtering             results, see https://support.lusid.com/knowledgebase/article/KA-01914. (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the 'Reconciliation' domain to decorate onto each reconciliation.             These must take the format {domain}/{scope}/{code}, for example 'Reconciliation/Broker/Id'. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_reconciliations(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, property_keys=property_keys, opts=opts)

        # [EXPERIMENTAL] ListReconciliations: List scheduled reconciliations
        api_response = api_instance.list_reconciliations(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, property_keys=property_keys)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ReconciliationsApi->list_reconciliations: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **effective_at** | **str**| The effective datetime or cut label at which to list the TimeVariant properties for the reconciliation. Defaults to the current LUSID             system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the reconciliation. Defaults to returning the latest version             of each reconciliation if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing reconciliations; this             value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt             and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results.             For example, to filter on the reconciliation type, specify \&quot;id.Code eq &#39;001&#39;\&quot;. For more information about filtering             results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;Reconciliation&#39; domain to decorate onto each reconciliation.             These must take the format {domain}/{scope}/{code}, for example &#39;Reconciliation/Broker/Id&#39;. | [optional] 

### Return type

[**PagedResourceListOfReconciliation**](PagedResourceListOfReconciliation.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of all scheduled reconciliations |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **reconcile_generic**
> ReconciliationResponse reconcile_generic(reconciliation_request=reconciliation_request)

ReconcileGeneric: Reconcile either holdings or valuations performed on one or two sets of holdings using one or two configuration recipes.              The output is configurable for various types of comparisons, to allow tolerances on numerical and date-time data or case-insensitivity on strings, and elision of resulting differences where they are 'empty' or null or zero.

Perform evaluation of one or two set of holdings (a portfolio of instruments) using one or two (potentially different) configuration recipes. Produce a breakdown of the resulting differences in evaluation that can be iterated through.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    ReconciliationsApi
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
    api_instance = api_client_factory.build(ReconciliationsApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # reconciliation_request = ReconciliationRequest.from_json("")
    # reconciliation_request = ReconciliationRequest.from_dict({})
    reconciliation_request = ReconciliationRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.reconcile_generic(reconciliation_request=reconciliation_request, opts=opts)

        # ReconcileGeneric: Reconcile either holdings or valuations performed on one or two sets of holdings using one or two configuration recipes.              The output is configurable for various types of comparisons, to allow tolerances on numerical and date-time data or case-insensitivity on strings, and elision of resulting differences where they are 'empty' or null or zero.
        api_response = api_instance.reconcile_generic(reconciliation_request=reconciliation_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ReconciliationsApi->reconcile_generic: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reconciliation_request** | [**ReconciliationRequest**](ReconciliationRequest.md)| The specifications of the inputs to the reconciliation | [optional] 

### Return type

[**ReconciliationResponse**](ReconciliationResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested reconciliation |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **reconcile_holdings**
> ResourceListOfReconciliationBreak reconcile_holdings(sort_by=sort_by, limit=limit, filter=filter, portfolios_reconciliation_request=portfolios_reconciliation_request)

[EARLY ACCESS] ReconcileHoldings: Reconcile portfolio holdings

Reconcile the holdings of two portfolios.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    ReconciliationsApi
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
    api_instance = api_client_factory.build(ReconciliationsApi)
    sort_by = ['sort_by_example'] # List[str] | Optional. Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName (optional)
    limit = 56 # int | Optional. When paginating, limit the number of returned results to this many. (optional)
    filter = 'filter_example' # str | Optional. Expression to filter the result set.             For example, to filter on the left portfolio Code, use \"left.portfolioId.code eq 'string'\"             Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # portfolios_reconciliation_request = PortfoliosReconciliationRequest.from_json("")
    # portfolios_reconciliation_request = PortfoliosReconciliationRequest.from_dict({})
    portfolios_reconciliation_request = PortfoliosReconciliationRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.reconcile_holdings(sort_by=sort_by, limit=limit, filter=filter, portfolios_reconciliation_request=portfolios_reconciliation_request, opts=opts)

        # [EARLY ACCESS] ReconcileHoldings: Reconcile portfolio holdings
        api_response = api_instance.reconcile_holdings(sort_by=sort_by, limit=limit, filter=filter, portfolios_reconciliation_request=portfolios_reconciliation_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ReconciliationsApi->reconcile_holdings: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort_by** | [**List[str]**](str.md)| Optional. Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName | [optional] 
 **limit** | **int**| Optional. When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Optional. Expression to filter the result set.             For example, to filter on the left portfolio Code, use \&quot;left.portfolioId.code eq &#39;string&#39;\&quot;             Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **portfolios_reconciliation_request** | [**PortfoliosReconciliationRequest**](PortfoliosReconciliationRequest.md)| The specifications of the inputs to the reconciliation | [optional] 

### Return type

[**ResourceListOfReconciliationBreak**](ResourceListOfReconciliationBreak.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested reconciliation |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **reconcile_inline**
> ListAggregationReconciliation reconcile_inline(inline_valuations_reconciliation_request=inline_valuations_reconciliation_request)

ReconcileInline: Reconcile valuations performed on one or two sets of inline instruments using one or two configuration recipes.

Perform valuation of one or two set of inline instruments using different one or two configuration recipes. Produce a breakdown of the resulting differences in valuation.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    ReconciliationsApi
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
    api_instance = api_client_factory.build(ReconciliationsApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # inline_valuations_reconciliation_request = InlineValuationsReconciliationRequest.from_json("")
    # inline_valuations_reconciliation_request = InlineValuationsReconciliationRequest.from_dict({})
    inline_valuations_reconciliation_request = InlineValuationsReconciliationRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.reconcile_inline(inline_valuations_reconciliation_request=inline_valuations_reconciliation_request, opts=opts)

        # ReconcileInline: Reconcile valuations performed on one or two sets of inline instruments using one or two configuration recipes.
        api_response = api_instance.reconcile_inline(inline_valuations_reconciliation_request=inline_valuations_reconciliation_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ReconciliationsApi->reconcile_inline: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_valuations_reconciliation_request** | [**InlineValuationsReconciliationRequest**](InlineValuationsReconciliationRequest.md)| The specifications of the inputs to the reconciliation | [optional] 

### Return type

[**ListAggregationReconciliation**](ListAggregationReconciliation.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested reconciliation |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **reconcile_transactions**
> TransactionsReconciliationsResponse reconcile_transactions(transaction_reconciliation_request=transaction_reconciliation_request)

[EARLY ACCESS] ReconcileTransactions: Perform a Transactions Reconciliation.

Evaluates two sets of transactions to determine which transactions from each set likely match using the rules of a specified mapping.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    ReconciliationsApi
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
    api_instance = api_client_factory.build(ReconciliationsApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # transaction_reconciliation_request = TransactionReconciliationRequest.from_json("")
    # transaction_reconciliation_request = TransactionReconciliationRequest.from_dict({})
    transaction_reconciliation_request = TransactionReconciliationRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.reconcile_transactions(transaction_reconciliation_request=transaction_reconciliation_request, opts=opts)

        # [EARLY ACCESS] ReconcileTransactions: Perform a Transactions Reconciliation.
        api_response = api_instance.reconcile_transactions(transaction_reconciliation_request=transaction_reconciliation_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ReconciliationsApi->reconcile_transactions: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_reconciliation_request** | [**TransactionReconciliationRequest**](TransactionReconciliationRequest.md)|  | [optional] 

### Return type

[**TransactionsReconciliationsResponse**](TransactionsReconciliationsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The transaction reconciliation data for the supplied portfolios. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **reconcile_transactions_v2**
> ReconciliationResponse reconcile_transactions_v2(transaction_reconciliation_request_v2=transaction_reconciliation_request_v2)

[EXPERIMENTAL] ReconcileTransactionsV2: Perform a Transactions Reconciliation.

Evaluates two sets of transactions to determine which transactions from each set likely match using the rules of a specified mapping.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    ReconciliationsApi
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
    api_instance = api_client_factory.build(ReconciliationsApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # transaction_reconciliation_request_v2 = TransactionReconciliationRequestV2.from_json("")
    # transaction_reconciliation_request_v2 = TransactionReconciliationRequestV2.from_dict({})
    transaction_reconciliation_request_v2 = TransactionReconciliationRequestV2()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.reconcile_transactions_v2(transaction_reconciliation_request_v2=transaction_reconciliation_request_v2, opts=opts)

        # [EXPERIMENTAL] ReconcileTransactionsV2: Perform a Transactions Reconciliation.
        api_response = api_instance.reconcile_transactions_v2(transaction_reconciliation_request_v2=transaction_reconciliation_request_v2)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ReconciliationsApi->reconcile_transactions_v2: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_reconciliation_request_v2** | [**TransactionReconciliationRequestV2**](TransactionReconciliationRequestV2.md)|  | [optional] 

### Return type

[**ReconciliationResponse**](ReconciliationResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested reconciliation |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **reconcile_valuation**
> ListAggregationReconciliation reconcile_valuation(valuations_reconciliation_request=valuations_reconciliation_request)

ReconcileValuation: Reconcile valuations performed on one or two sets of holdings using one or two configuration recipes.

Perform valuation of one or two set of holdings using different one or two configuration recipes. Produce a breakdown of the resulting differences in valuation.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    ReconciliationsApi
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
    api_instance = api_client_factory.build(ReconciliationsApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # valuations_reconciliation_request = ValuationsReconciliationRequest.from_json("")
    # valuations_reconciliation_request = ValuationsReconciliationRequest.from_dict({})
    valuations_reconciliation_request = ValuationsReconciliationRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.reconcile_valuation(valuations_reconciliation_request=valuations_reconciliation_request, opts=opts)

        # ReconcileValuation: Reconcile valuations performed on one or two sets of holdings using one or two configuration recipes.
        api_response = api_instance.reconcile_valuation(valuations_reconciliation_request=valuations_reconciliation_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ReconciliationsApi->reconcile_valuation: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **valuations_reconciliation_request** | [**ValuationsReconciliationRequest**](ValuationsReconciliationRequest.md)| The specifications of the inputs to the reconciliation | [optional] 

### Return type

[**ListAggregationReconciliation**](ListAggregationReconciliation.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested reconciliation |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **update_reconciliation**
> Reconciliation update_reconciliation(scope, code, update_reconciliation_request=update_reconciliation_request)

[EXPERIMENTAL] UpdateReconciliation: Update scheduled reconciliation

Update a given scheduled reconciliation

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    ReconciliationsApi
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
    api_instance = api_client_factory.build(ReconciliationsApi)
    scope = 'scope_example' # str | The scope of the reconciliation to be updated
    code = 'code_example' # str | The code of the reconciliation to be updated

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # update_reconciliation_request = UpdateReconciliationRequest.from_json("")
    # update_reconciliation_request = UpdateReconciliationRequest.from_dict({})
    update_reconciliation_request = UpdateReconciliationRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.update_reconciliation(scope, code, update_reconciliation_request=update_reconciliation_request, opts=opts)

        # [EXPERIMENTAL] UpdateReconciliation: Update scheduled reconciliation
        api_response = api_instance.update_reconciliation(scope, code, update_reconciliation_request=update_reconciliation_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ReconciliationsApi->update_reconciliation: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the reconciliation to be updated | 
 **code** | **str**| The code of the reconciliation to be updated | 
 **update_reconciliation_request** | [**UpdateReconciliationRequest**](UpdateReconciliationRequest.md)| The updated definition of the reconciliation | [optional] 

### Return type

[**Reconciliation**](Reconciliation.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated scheduled reconciliation |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **upsert_reconciliation_mapping**
> Mapping upsert_reconciliation_mapping(mapping=mapping)

[EARLY ACCESS] UpsertReconciliationMapping: Create or update a mapping

If no mapping exists with the specified scope and code will create a new one. Else will update the existing mapping

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    ReconciliationsApi
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
    api_instance = api_client_factory.build(ReconciliationsApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # mapping = Mapping.from_json("")
    # mapping = Mapping.from_dict({})
    mapping = Mapping()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.upsert_reconciliation_mapping(mapping=mapping, opts=opts)

        # [EARLY ACCESS] UpsertReconciliationMapping: Create or update a mapping
        api_response = api_instance.upsert_reconciliation_mapping(mapping=mapping)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ReconciliationsApi->upsert_reconciliation_mapping: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mapping** | [**Mapping**](Mapping.md)| The mapping to be created / updated. | [optional] 

### Return type

[**Mapping**](Mapping.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The created / updated mapping. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

