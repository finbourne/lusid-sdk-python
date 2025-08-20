# lusid.LegacyComplianceApi

All URIs are relative to *https://fbn-prd.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_legacy_compliance_rule**](LegacyComplianceApi.md#delete_legacy_compliance_rule) | **DELETE** /api/legacy/compliance/rules/{scope}/{code} | [EXPERIMENTAL] DeleteLegacyComplianceRule: Deletes a compliance rule.
[**get_legacy_breached_orders_info**](LegacyComplianceApi.md#get_legacy_breached_orders_info) | **GET** /api/legacy/compliance/runs/breached/{runId} | [EXPERIMENTAL] GetLegacyBreachedOrdersInfo: Get the Ids of Breached orders in a given compliance run and the corresponding list of rules that could have caused it.
[**get_legacy_compliance_rule**](LegacyComplianceApi.md#get_legacy_compliance_rule) | **GET** /api/legacy/compliance/rules/{scope}/{code} | [EXPERIMENTAL] GetLegacyComplianceRule: Retrieve the definition of single compliance rule.
[**get_legacy_compliance_run_results**](LegacyComplianceApi.md#get_legacy_compliance_run_results) | **GET** /api/legacy/compliance/runs/{runId} | [EXPERIMENTAL] GetLegacyComplianceRunResults: Get the details of a single compliance run.
[**list_legacy_compliance_rules**](LegacyComplianceApi.md#list_legacy_compliance_rules) | **GET** /api/legacy/compliance/rules | [EXPERIMENTAL] ListLegacyComplianceRules: List compliance rules, with optional filtering.
[**list_legacy_compliance_run_info**](LegacyComplianceApi.md#list_legacy_compliance_run_info) | **GET** /api/legacy/compliance/runs | [EXPERIMENTAL] ListLegacyComplianceRunInfo: List historical compliance run ids.
[**run_legacy_compliance**](LegacyComplianceApi.md#run_legacy_compliance) | **POST** /api/legacy/compliance/runs | [EXPERIMENTAL] RunLegacyCompliance: Kick off the compliance check process
[**upsert_legacy_compliance_rules**](LegacyComplianceApi.md#upsert_legacy_compliance_rules) | **POST** /api/legacy/compliance/rules | [EXPERIMENTAL] UpsertLegacyComplianceRules: Upsert compliance rules.


# **delete_legacy_compliance_rule**
> DeletedEntityResponse delete_legacy_compliance_rule(scope, code)

[EXPERIMENTAL] DeleteLegacyComplianceRule: Deletes a compliance rule.

Deletes the rule for all effective time.              The rule will remain viewable at previous as at times, and as part of the results of compliance runs, but it will no longer be considered in new compliance runs.              This cannot be undone.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    LegacyComplianceApi
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
    api_instance = api_client_factory.build(LegacyComplianceApi)
    scope = 'scope_example' # str | The compliance rule scope.
    code = 'code_example' # str | The compliance rule code.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_legacy_compliance_rule(scope, code, opts=opts)

        # [EXPERIMENTAL] DeleteLegacyComplianceRule: Deletes a compliance rule.
        api_response = api_instance.delete_legacy_compliance_rule(scope, code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling LegacyComplianceApi->delete_legacy_compliance_rule: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The compliance rule scope. | 
 **code** | **str**| The compliance rule code. | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_legacy_breached_orders_info**
> ResourceListOfComplianceBreachedOrderInfo get_legacy_breached_orders_info(run_id, order_scope=order_scope, order_code=order_code, limit=limit)

[EXPERIMENTAL] GetLegacyBreachedOrdersInfo: Get the Ids of Breached orders in a given compliance run and the corresponding list of rules that could have caused it.

Use this endpoint to get a list or breached orders and the set of rules that may have caused the breach.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    LegacyComplianceApi
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
    api_instance = api_client_factory.build(LegacyComplianceApi)
    run_id = 'run_id_example' # str | The RunId that the results should be checked for
    order_scope = 'order_scope_example' # str | Optional. Find rules related to a specific order by providing an Order Scope/Code combination (optional)
    order_code = 'order_code_example' # str | Optional. Find rules related to a specific order by providing an Order Scope/Code combination (optional)
    limit = 56 # int | When paginating, limit the number of returned results to this many. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_legacy_breached_orders_info(run_id, order_scope=order_scope, order_code=order_code, limit=limit, opts=opts)

        # [EXPERIMENTAL] GetLegacyBreachedOrdersInfo: Get the Ids of Breached orders in a given compliance run and the corresponding list of rules that could have caused it.
        api_response = api_instance.get_legacy_breached_orders_info(run_id, order_scope=order_scope, order_code=order_code, limit=limit)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling LegacyComplianceApi->get_legacy_breached_orders_info: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**| The RunId that the results should be checked for | 
 **order_scope** | **str**| Optional. Find rules related to a specific order by providing an Order Scope/Code combination | [optional] 
 **order_code** | **str**| Optional. Find rules related to a specific order by providing an Order Scope/Code combination | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] 

### Return type

[**ResourceListOfComplianceBreachedOrderInfo**](ResourceListOfComplianceBreachedOrderInfo.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The potentially breached orders and their rules from a specific compliance run |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_legacy_compliance_rule**
> ComplianceRule get_legacy_compliance_rule(scope, code, effective_at=effective_at, as_at=as_at)

[EXPERIMENTAL] GetLegacyComplianceRule: Retrieve the definition of single compliance rule.

Retrieves the compliance rule definition at the given effective and as at times.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    LegacyComplianceApi
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
    api_instance = api_client_factory.build(LegacyComplianceApi)
    scope = 'scope_example' # str | The compliance rule scope.
    code = 'code_example' # str | The compliance rule code.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve the rule definition. Defaults to the current LUSID system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the rule definition. Defaults to returning the latest version if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_legacy_compliance_rule(scope, code, effective_at=effective_at, as_at=as_at, opts=opts)

        # [EXPERIMENTAL] GetLegacyComplianceRule: Retrieve the definition of single compliance rule.
        api_response = api_instance.get_legacy_compliance_rule(scope, code, effective_at=effective_at, as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling LegacyComplianceApi->get_legacy_compliance_rule: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The compliance rule scope. | 
 **code** | **str**| The compliance rule code. | 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the rule definition. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the rule definition. Defaults to returning the latest version if not specified. | [optional] 

### Return type

[**ComplianceRule**](ComplianceRule.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details of one compliance rule. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_legacy_compliance_run_results**
> ResourceListOfComplianceRuleResult get_legacy_compliance_run_results(run_id, page=page, limit=limit, filter=filter)

[EXPERIMENTAL] GetLegacyComplianceRunResults: Get the details of a single compliance run.

Use this endpoint to fetch the detail associated with a specific compliance run, including a breakdown of the passing state of each rule, portfolio combination.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    LegacyComplianceApi
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
    api_instance = api_client_factory.build(LegacyComplianceApi)
    run_id = 'run_id_example' # str | The unique identifier of the compliance run requested.
    page = 'page_example' # str | The pagination token to use to continue listing compliance rule results from a previous call to list compliance rule result.             This value is returned from the previous call. If a pagination token is provided the sortBy, filter, and asAt fields             must not have changed since the original request. (optional)
    limit = 56 # int | When paginating, limit the number of returned results to this many. (optional)
    filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_legacy_compliance_run_results(run_id, page=page, limit=limit, filter=filter, opts=opts)

        # [EXPERIMENTAL] GetLegacyComplianceRunResults: Get the details of a single compliance run.
        api_response = api_instance.get_legacy_compliance_run_results(run_id, page=page, limit=limit, filter=filter)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling LegacyComplianceApi->get_legacy_compliance_run_results: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**| The unique identifier of the compliance run requested. | 
 **page** | **str**| The pagination token to use to continue listing compliance rule results from a previous call to list compliance rule result.             This value is returned from the previous call. If a pagination token is provided the sortBy, filter, and asAt fields             must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 

### Return type

[**ResourceListOfComplianceRuleResult**](ResourceListOfComplianceRuleResult.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The rule results of a specific compliance run |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_legacy_compliance_rules**
> ResourceListOfComplianceRule list_legacy_compliance_rules(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter)

[EXPERIMENTAL] ListLegacyComplianceRules: List compliance rules, with optional filtering.

For more information about filtering results, see https://support.lusid.com/knowledgebase/article/KA-01914.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    LegacyComplianceApi
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
    api_instance = api_client_factory.build(LegacyComplianceApi)
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve the rule definitions. Defaults to the current LUSID system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the rule definitions. Defaults to returning the latest version if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing entities; this value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt and asAt fields must not have changed since the original request. (optional)
    limit = 56 # int | When paginating, limit the results to this number. Defaults to 100 if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the results. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_legacy_compliance_rules(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, opts=opts)

        # [EXPERIMENTAL] ListLegacyComplianceRules: List compliance rules, with optional filtering.
        api_response = api_instance.list_legacy_compliance_rules(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling LegacyComplianceApi->list_legacy_compliance_rules: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the rule definitions. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the rule definitions. Defaults to returning the latest version if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing entities; this value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results. | [optional] 

### Return type

[**ResourceListOfComplianceRule**](ResourceListOfComplianceRule.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A filtered list of compliance rules available. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_legacy_compliance_run_info**
> ResourceListOfComplianceRunInfo list_legacy_compliance_run_info(as_at=as_at, page=page, limit=limit, filter=filter)

[EXPERIMENTAL] ListLegacyComplianceRunInfo: List historical compliance run ids.

Use this endpoint to fetch a list of all historical compliance runs.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    LegacyComplianceApi
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
    api_instance = api_client_factory.build(LegacyComplianceApi)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The time at which to get results from. Default : latest (optional)
    page = 'page_example' # str | The pagination token to use to continue listing compliance runs from a previous call to list compliance runs.             This value is returned from the previous call. If a pagination token is provided the sortBy, filter, and asAt fields             must not have changed since the original request. (optional)
    limit = 56 # int | When paginating, limit the number of returned results to this many. (optional)
    filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_legacy_compliance_run_info(as_at=as_at, page=page, limit=limit, filter=filter, opts=opts)

        # [EXPERIMENTAL] ListLegacyComplianceRunInfo: List historical compliance run ids.
        api_response = api_instance.list_legacy_compliance_run_info(as_at=as_at, page=page, limit=limit, filter=filter)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling LegacyComplianceApi->list_legacy_compliance_run_info: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| Optional. The time at which to get results from. Default : latest | [optional] 
 **page** | **str**| The pagination token to use to continue listing compliance runs from a previous call to list compliance runs.             This value is returned from the previous call. If a pagination token is provided the sortBy, filter, and asAt fields             must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 

### Return type

[**ResourceListOfComplianceRunInfo**](ResourceListOfComplianceRunInfo.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The List of IDs and information for all compliance runs completed |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **run_legacy_compliance**
> ComplianceRunInfo run_legacy_compliance(is_pre_trade, recipe_id_scope, recipe_id_code=recipe_id_code, by_taxlots=by_taxlots)

[EXPERIMENTAL] RunLegacyCompliance: Kick off the compliance check process

Use this endpoint to fetch the start a compliance run, based on a pre-set mapping file.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    LegacyComplianceApi
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
    api_instance = api_client_factory.build(LegacyComplianceApi)
    is_pre_trade = True # bool | Required: Boolean flag indicating if a run should be PreTrade (Including orders). For post-trade only, set to false
    recipe_id_scope = 'recipe_id_scope_example' # str | Required: the scope of the recipe to be used
    recipe_id_code = 'recipe_id_code_example' # str | Optional: The code of the recipe to be used. If left blank, the default recipe will be used. (optional)
    by_taxlots = True # bool | Optional. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.run_legacy_compliance(is_pre_trade, recipe_id_scope, recipe_id_code=recipe_id_code, by_taxlots=by_taxlots, opts=opts)

        # [EXPERIMENTAL] RunLegacyCompliance: Kick off the compliance check process
        api_response = api_instance.run_legacy_compliance(is_pre_trade, recipe_id_scope, recipe_id_code=recipe_id_code, by_taxlots=by_taxlots)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling LegacyComplianceApi->run_legacy_compliance: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_pre_trade** | **bool**| Required: Boolean flag indicating if a run should be PreTrade (Including orders). For post-trade only, set to false | 
 **recipe_id_scope** | **str**| Required: the scope of the recipe to be used | 
 **recipe_id_code** | **str**| Optional: The code of the recipe to be used. If left blank, the default recipe will be used. | [optional] 
 **by_taxlots** | **bool**| Optional. | [optional] 

### Return type

[**ComplianceRunInfo**](ComplianceRunInfo.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The identifying information of a compliance run |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **upsert_legacy_compliance_rules**
> ComplianceRuleUpsertResponse upsert_legacy_compliance_rules(request_body, effective_at=effective_at)

[EXPERIMENTAL] UpsertLegacyComplianceRules: Upsert compliance rules.

To upsert a new rule, the code field must be left empty, a code will then be assigned and returned as part of the response. To update an existing rule, include the rule code. It is possible to both create and update compliance rules in the same request.              The upsert is transactional - either all create/update operations will succeed or none of them will.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    LegacyComplianceApi
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
    api_instance = api_client_factory.build(LegacyComplianceApi)
    request_body = {"Create":{"scope":"CompanyPolicies","displayName":"Max 200 Securities","type":"RangeNumberSecurities","lowerBound":0,"upperBound":200,"schedule":"PreAndPostTrade","hardRequirement":true,"targetPortfolioIds":[{"scope":"CorePortfolios","code":"UK"},{"scope":"CorePortfolios","code":"World"}],"description":"Portfolio must contain no more than 200 securities.","addressKey":"Valuation/PvInPortfolioCcy"},"Update":{"scope":"FundObjectives","code":"ComplianceRule_1","displayName":"30 percent bonds","type":"RangePercentSecurityType","value":"Bond","lowerBound":25,"upperBound":35,"schedule":"PostTrade","hardRequirement":false,"targetPortfolioIds":[{"scope":"CorePortfolios","code":"Balanced"}],"description":"Portfolio must contain 30% bonds by value.","addressKey":"Valuation/ExposureInPortfolioCcy"}} # Dict[str, ComplianceRuleUpsertRequest] | A dictionary of upsert request identifiers to rule upsert requests. The request              identifiers are valid for the request only and can be used to link the upserted compliance rule to the code              of a created compliance rule.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which the rule will take effect. Defaults to the current LUSID system datetime if not specified. In the case of an update, the changes will take place from this effective time until the next effective time that the rule as been upserted at. For example, consider a rule that already exists, and has previously had an update applied so that the definition will change on the first day of the coming month. An upsert effective from the current day will only change the definition until the first day of the coming month. An additional upsert at the same time (first day of the month) is required if the newly-updated definition is to supersede the future definition. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.upsert_legacy_compliance_rules(request_body, effective_at=effective_at, opts=opts)

        # [EXPERIMENTAL] UpsertLegacyComplianceRules: Upsert compliance rules.
        api_response = api_instance.upsert_legacy_compliance_rules(request_body, effective_at=effective_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling LegacyComplianceApi->upsert_legacy_compliance_rules: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, ComplianceRuleUpsertRequest]**](ComplianceRuleUpsertRequest.md)| A dictionary of upsert request identifiers to rule upsert requests. The request              identifiers are valid for the request only and can be used to link the upserted compliance rule to the code              of a created compliance rule. | 
 **effective_at** | **str**| The effective datetime or cut label at which the rule will take effect. Defaults to the current LUSID system datetime if not specified. In the case of an update, the changes will take place from this effective time until the next effective time that the rule as been upserted at. For example, consider a rule that already exists, and has previously had an update applied so that the definition will change on the first day of the coming month. An upsert effective from the current day will only change the definition until the first day of the coming month. An additional upsert at the same time (first day of the month) is required if the newly-updated definition is to supersede the future definition. | [optional] 

### Return type

[**ComplianceRuleUpsertResponse**](ComplianceRuleUpsertResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Upsert compliance rules. New compliance rules must have an empty code field. Where a codeis given, this rule must already exist and will be updated. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

