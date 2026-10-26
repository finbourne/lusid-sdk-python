# lusid.CollateralApi

All URIs are relative to *https://fbn-prd.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accept_margin_call**](CollateralApi.md#accept_margin_call) | **POST** /api/collateral/margincalls/{runId}/{agreementScope}/{agreementCode}/{item}/{marginType}/{direction}/$accept | [EXPERIMENTAL] AcceptMarginCall: Accept a margin call.
[**batch_accept_margin_calls**](CollateralApi.md#batch_accept_margin_calls) | **POST** /api/collateral/margincalls/$batchAccept | [EXPERIMENTAL] BatchAcceptMarginCalls: Accept several margin calls.
[**dispute_margin_call**](CollateralApi.md#dispute_margin_call) | **POST** /api/collateral/margincalls/{runId}/{agreementScope}/{agreementCode}/{item}/{marginType}/{direction}/$dispute | [EXPERIMENTAL] DisputeMarginCall: Dispute a margin call.
[**get_margin_call**](CollateralApi.md#get_margin_call) | **GET** /api/collateral/margincalls/{runId}/{agreementScope}/{agreementCode}/{item}/{marginType}/{direction} | [EXPERIMENTAL] GetMarginCall: Get a margin call.
[**get_margin_run**](CollateralApi.md#get_margin_run) | **GET** /api/collateral/runs/{runId} | [EXPERIMENTAL] GetMarginRun: Get a margin run.
[**list_margin_call_lines**](CollateralApi.md#list_margin_call_lines) | **GET** /api/collateral/margincalls/{runId}/{agreementScope}/{agreementCode}/{item}/{marginType}/{direction}/lines | [EXPERIMENTAL] ListMarginCallLines: List the margin lines of a call.
[**list_margin_calls**](CollateralApi.md#list_margin_calls) | **GET** /api/collateral/margincalls | [EXPERIMENTAL] ListMarginCalls: List margin calls.
[**list_margin_lines**](CollateralApi.md#list_margin_lines) | **GET** /api/collateral/runs/{runId}/lines | [EXPERIMENTAL] ListMarginLines: List the margin lines of a run.
[**list_margin_runs**](CollateralApi.md#list_margin_runs) | **GET** /api/collateral/runs | [EXPERIMENTAL] ListMarginRuns: List margin runs.
[**record_counterparty_demand**](CollateralApi.md#record_counterparty_demand) | **POST** /api/collateral/margincalls/{runId}/{agreementScope}/{agreementCode}/{item}/{marginType}/{direction}/$recordCounterpartyDemand | [EXPERIMENTAL] RecordCounterpartyDemand: Record the counterparty&#39;s demand against a margin call.
[**retry_margin_run**](CollateralApi.md#retry_margin_run) | **POST** /api/collateral/runs/{runId}/$retry | [EXPERIMENTAL] RetryMarginRun: Retry a margin run.
[**run_margin_calculation**](CollateralApi.md#run_margin_calculation) | **POST** /api/collateral/$run | [EXPERIMENTAL] RunMarginCalculation: Run the margin calculation.


# **accept_margin_call**
> MarginCall accept_margin_call(run_id, agreement_scope, agreement_code, item, margin_type, direction, accept_margin_call_request=accept_margin_call_request)

[EXPERIMENTAL] AcceptMarginCall: Accept a margin call.

Accept a margin call at the agreed amount: our figure when matched, the counterparty's when within tolerance, or  the amount given, which is required when the demand breaks tolerance or has not been recorded. Allowed from the  calculated and disputed states.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    CollateralApi
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
    api_instance = api_client_factory.build(CollateralApi)
    run_id = 'run_id_example' # str | The identifier of the margin run.
    agreement_scope = 'agreement_scope_example' # str | The scope of the call's collateral agreement.
    agreement_code = 'agreement_code_example' # str | The code of the call's collateral agreement.
    item = 'item_example' # str | The margin item of the call.
    margin_type = 'margin_type_example' # str | The margin type of the call. Currently VariationMargin.
    direction = 'direction_example' # str | Who posts under the call. One of WePost, TheyPost or None.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # accept_margin_call_request = AcceptMarginCallRequest.from_json("")
    # accept_margin_call_request = AcceptMarginCallRequest.from_dict({})
    accept_margin_call_request = AcceptMarginCallRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.accept_margin_call(run_id, agreement_scope, agreement_code, item, margin_type, direction, accept_margin_call_request=accept_margin_call_request, opts=opts)

        # [EXPERIMENTAL] AcceptMarginCall: Accept a margin call.
        api_response = api_instance.accept_margin_call(run_id, agreement_scope, agreement_code, item, margin_type, direction, accept_margin_call_request=accept_margin_call_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling CollateralApi->accept_margin_call: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**| The identifier of the margin run. | 
 **agreement_scope** | **str**| The scope of the call&#39;s collateral agreement. | 
 **agreement_code** | **str**| The code of the call&#39;s collateral agreement. | 
 **item** | **str**| The margin item of the call. | 
 **margin_type** | **str**| The margin type of the call. Currently VariationMargin. | 
 **direction** | **str**| Who posts under the call. One of WePost, TheyPost or None. | 
 **accept_margin_call_request** | [**AcceptMarginCallRequest**](AcceptMarginCallRequest.md)| The amount to accept, when the default does not apply. | [optional] 

### Return type

[**MarginCall**](MarginCall.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The accepted margin call. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **batch_accept_margin_calls**
> BatchAcceptMarginCallsResponse batch_accept_margin_calls(batch_accept_margin_calls_request)

[EXPERIMENTAL] BatchAcceptMarginCalls: Accept several margin calls.

Accept each of the given margin calls at its default agreed amount. A call that cannot be accepted is reported  in the response and does not stop the others.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    CollateralApi
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
    api_instance = api_client_factory.build(CollateralApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # batch_accept_margin_calls_request = BatchAcceptMarginCallsRequest.from_json("")
    # batch_accept_margin_calls_request = BatchAcceptMarginCallsRequest.from_dict({})
    batch_accept_margin_calls_request = BatchAcceptMarginCallsRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.batch_accept_margin_calls(batch_accept_margin_calls_request, opts=opts)

        # [EXPERIMENTAL] BatchAcceptMarginCalls: Accept several margin calls.
        api_response = api_instance.batch_accept_margin_calls(batch_accept_margin_calls_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling CollateralApi->batch_accept_margin_calls: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_accept_margin_calls_request** | [**BatchAcceptMarginCallsRequest**](BatchAcceptMarginCallsRequest.md)| The margin calls to accept. | 

### Return type

[**BatchAcceptMarginCallsResponse**](BatchAcceptMarginCallsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The calls accepted, and those that could not be. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **dispute_margin_call**
> MarginCall dispute_margin_call(run_id, agreement_scope, agreement_code, item, margin_type, direction, dispute_margin_call_request)

[EXPERIMENTAL] DisputeMarginCall: Dispute a margin call.

Dispute a margin call: move the agreed amount now and leave the rest of the counterparty's demand in dispute,  with a reason and an owner. Allowed from the calculated and accepted states.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    CollateralApi
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
    api_instance = api_client_factory.build(CollateralApi)
    run_id = 'run_id_example' # str | The identifier of the margin run.
    agreement_scope = 'agreement_scope_example' # str | The scope of the call's collateral agreement.
    agreement_code = 'agreement_code_example' # str | The code of the call's collateral agreement.
    item = 'item_example' # str | The margin item of the call.
    margin_type = 'margin_type_example' # str | The margin type of the call. Currently VariationMargin.
    direction = 'direction_example' # str | Who posts under the call. One of WePost, TheyPost or None.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # dispute_margin_call_request = DisputeMarginCallRequest.from_json("")
    # dispute_margin_call_request = DisputeMarginCallRequest.from_dict({})
    dispute_margin_call_request = DisputeMarginCallRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.dispute_margin_call(run_id, agreement_scope, agreement_code, item, margin_type, direction, dispute_margin_call_request, opts=opts)

        # [EXPERIMENTAL] DisputeMarginCall: Dispute a margin call.
        api_response = api_instance.dispute_margin_call(run_id, agreement_scope, agreement_code, item, margin_type, direction, dispute_margin_call_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling CollateralApi->dispute_margin_call: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**| The identifier of the margin run. | 
 **agreement_scope** | **str**| The scope of the call&#39;s collateral agreement. | 
 **agreement_code** | **str**| The code of the call&#39;s collateral agreement. | 
 **item** | **str**| The margin item of the call. | 
 **margin_type** | **str**| The margin type of the call. Currently VariationMargin. | 
 **direction** | **str**| Who posts under the call. One of WePost, TheyPost or None. | 
 **dispute_margin_call_request** | [**DisputeMarginCallRequest**](DisputeMarginCallRequest.md)| The amount to move now, the reason and the owner. | 

### Return type

[**MarginCall**](MarginCall.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The disputed margin call. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_margin_call**
> MarginCall get_margin_call(run_id, agreement_scope, agreement_code, item, margin_type, direction)

[EXPERIMENTAL] GetMarginCall: Get a margin call.

Retrieve one margin call of a run by its business key.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    CollateralApi
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
    api_instance = api_client_factory.build(CollateralApi)
    run_id = 'run_id_example' # str | The identifier of the margin run.
    agreement_scope = 'agreement_scope_example' # str | The scope of the call's collateral agreement.
    agreement_code = 'agreement_code_example' # str | The code of the call's collateral agreement.
    item = 'item_example' # str | The margin item of the call.
    margin_type = 'margin_type_example' # str | The margin type of the call. Currently VariationMargin.
    direction = 'direction_example' # str | Who posts under the call. One of WePost, TheyPost or None.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_margin_call(run_id, agreement_scope, agreement_code, item, margin_type, direction, opts=opts)

        # [EXPERIMENTAL] GetMarginCall: Get a margin call.
        api_response = api_instance.get_margin_call(run_id, agreement_scope, agreement_code, item, margin_type, direction)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling CollateralApi->get_margin_call: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**| The identifier of the margin run. | 
 **agreement_scope** | **str**| The scope of the call&#39;s collateral agreement. | 
 **agreement_code** | **str**| The code of the call&#39;s collateral agreement. | 
 **item** | **str**| The margin item of the call. | 
 **margin_type** | **str**| The margin type of the call. Currently VariationMargin. | 
 **direction** | **str**| Who posts under the call. One of WePost, TheyPost or None. | 

### Return type

[**MarginCall**](MarginCall.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested margin call. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_margin_run**
> MarginRun get_margin_run(run_id)

[EXPERIMENTAL] GetMarginRun: Get a margin run.

Retrieve a margin run with its progress: the status of each shard, the calls and lines published so far, and  anything it could not value.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    CollateralApi
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
    api_instance = api_client_factory.build(CollateralApi)
    run_id = 'run_id_example' # str | The identifier of the margin run.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_margin_run(run_id, opts=opts)

        # [EXPERIMENTAL] GetMarginRun: Get a margin run.
        api_response = api_instance.get_margin_run(run_id)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling CollateralApi->get_margin_run: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**| The identifier of the margin run. | 

### Return type

[**MarginRun**](MarginRun.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested margin run. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_margin_call_lines**
> PagedResourceListOfMarginLine list_margin_call_lines(run_id, agreement_scope, agreement_code, item, margin_type, direction, page=page, limit=limit, filter=filter)

[EXPERIMENTAL] ListMarginCallLines: List the margin lines of a call.

List the holding lines behind one margin call: our side of the figure the counterparty's statement is matched against.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    CollateralApi
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
    api_instance = api_client_factory.build(CollateralApi)
    run_id = 'run_id_example' # str | The identifier of the margin run.
    agreement_scope = 'agreement_scope_example' # str | The scope of the call's collateral agreement.
    agreement_code = 'agreement_code_example' # str | The code of the call's collateral agreement.
    item = 'item_example' # str | The margin item of the call.
    margin_type = 'margin_type_example' # str | The margin type of the call. Currently VariationMargin.
    direction = 'direction_example' # str | Who posts under the call. One of WePost, TheyPost or None.
    page = 'page_example' # str | The pagination token to use to continue listing margin lines; this value is returned from the previous call. (optional)
    limit = 56 # int | When paginating, limit the results to this number. Defaults to 100 if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the results. The filterable fields are PortfolioId.Scope, PortfolioId.Code, HoldingId, CustodianAccountScope, CustodianAccountCode, CustodianAccountName, Units, Pv, VariationMargin and CollateralValue. For more information about filtering results, see https://support.lusid.com/docs/filtering-information-retrieved-from-lusid. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_margin_call_lines(run_id, agreement_scope, agreement_code, item, margin_type, direction, page=page, limit=limit, filter=filter, opts=opts)

        # [EXPERIMENTAL] ListMarginCallLines: List the margin lines of a call.
        api_response = api_instance.list_margin_call_lines(run_id, agreement_scope, agreement_code, item, margin_type, direction, page=page, limit=limit, filter=filter)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling CollateralApi->list_margin_call_lines: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**| The identifier of the margin run. | 
 **agreement_scope** | **str**| The scope of the call&#39;s collateral agreement. | 
 **agreement_code** | **str**| The code of the call&#39;s collateral agreement. | 
 **item** | **str**| The margin item of the call. | 
 **margin_type** | **str**| The margin type of the call. Currently VariationMargin. | 
 **direction** | **str**| Who posts under the call. One of WePost, TheyPost or None. | 
 **page** | **str**| The pagination token to use to continue listing margin lines; this value is returned from the previous call. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results. The filterable fields are PortfolioId.Scope, PortfolioId.Code, HoldingId, CustodianAccountScope, CustodianAccountCode, CustodianAccountName, Units, Pv, VariationMargin and CollateralValue. For more information about filtering results, see https://support.lusid.com/docs/filtering-information-retrieved-from-lusid. | [optional] 

### Return type

[**PagedResourceListOfMarginLine**](PagedResourceListOfMarginLine.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested margin lines. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_margin_calls**
> PagedResourceListOfMarginCall list_margin_calls(effective_at=effective_at, run_id=run_id, page=page, limit=limit, filter=filter, scenarios=scenarios, effective_from=effective_from)

[EXPERIMENTAL] ListMarginCalls: List margin calls.

List the margin calls of one run when a run id is given. Otherwise list the current calls for a business date:  those of the latest run for the date, with an agreement that run could not value served from the most recent run  that did. With an effectiveFrom the current calls of each date from it to effectiveAt are listed, in date order.  Restricted to the agreements the caller may read.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    CollateralApi
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
    api_instance = api_client_factory.build(CollateralApi)
    effective_at = 'effective_at_example' # str | The business date, datetime or cut label to list the current margin calls for, or the last date of the range when effectiveFrom is given. Defaults to today if not specified. Ignored when a run id is given. (optional)
    run_id = 'run_id_example' # str | The identifier of the margin run to list the calls of. Lists the current calls for the business date if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing margin calls; this value is returned from the previous call. (optional)
    limit = 56 # int | When paginating, limit the results to this number. Defaults to 100 if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the results. The filterable fields are RunId, AgreementId.Scope, AgreementId.Code, Counterparty.Code, Counterparty.IdTypeScope, Counterparty.IdTypeCode, Item, MarginType, Method, Settlement, Direction, Currency, Required, Held, Call, CounterpartyDemand, Difference, MatchStatus, AgreedAmount, DisputedAmount, DisputeOwner, State and Deadline. For example, to find the breaks, specify \"MatchStatus eq 'Break'\". For more information about filtering results, see https://support.lusid.com/docs/filtering-information-retrieved-from-lusid. (optional)
    scenarios = ['scenarios_example'] # List[str] | The scenarios, each as scope/code, whose calls are listed beside the base case calls, which are always listed. Lists the base case calls only if not specified. (optional)
    effective_from = 'effective_from_example' # str | The first business date, datetime or cut label of a range ending at effectiveAt, for a time series of calls. Lists the one business date if not specified. Ignored when a run id is given. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_margin_calls(effective_at=effective_at, run_id=run_id, page=page, limit=limit, filter=filter, scenarios=scenarios, effective_from=effective_from, opts=opts)

        # [EXPERIMENTAL] ListMarginCalls: List margin calls.
        api_response = api_instance.list_margin_calls(effective_at=effective_at, run_id=run_id, page=page, limit=limit, filter=filter, scenarios=scenarios, effective_from=effective_from)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling CollateralApi->list_margin_calls: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **effective_at** | **str**| The business date, datetime or cut label to list the current margin calls for, or the last date of the range when effectiveFrom is given. Defaults to today if not specified. Ignored when a run id is given. | [optional] 
 **run_id** | **str**| The identifier of the margin run to list the calls of. Lists the current calls for the business date if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing margin calls; this value is returned from the previous call. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results. The filterable fields are RunId, AgreementId.Scope, AgreementId.Code, Counterparty.Code, Counterparty.IdTypeScope, Counterparty.IdTypeCode, Item, MarginType, Method, Settlement, Direction, Currency, Required, Held, Call, CounterpartyDemand, Difference, MatchStatus, AgreedAmount, DisputedAmount, DisputeOwner, State and Deadline. For example, to find the breaks, specify \&quot;MatchStatus eq &#39;Break&#39;\&quot;. For more information about filtering results, see https://support.lusid.com/docs/filtering-information-retrieved-from-lusid. | [optional] 
 **scenarios** | [**List[str]**](str.md)| The scenarios, each as scope/code, whose calls are listed beside the base case calls, which are always listed. Lists the base case calls only if not specified. | [optional] 
 **effective_from** | **str**| The first business date, datetime or cut label of a range ending at effectiveAt, for a time series of calls. Lists the one business date if not specified. Ignored when a run id is given. | [optional] 

### Return type

[**PagedResourceListOfMarginCall**](PagedResourceListOfMarginCall.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested margin calls. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_margin_lines**
> PagedResourceListOfMarginLine list_margin_lines(run_id, page=page, limit=limit, filter=filter, scenarios=scenarios)

[EXPERIMENTAL] ListMarginLines: List the margin lines of a run.

List the holding lines behind every margin call of a run, restricted to the agreements the caller may read.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    CollateralApi
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
    api_instance = api_client_factory.build(CollateralApi)
    run_id = 'run_id_example' # str | The identifier of the margin run.
    page = 'page_example' # str | The pagination token to use to continue listing margin lines; this value is returned from the previous call. (optional)
    limit = 56 # int | When paginating, limit the results to this number. Defaults to 100 if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the results. The filterable fields are AgreementId.Scope, AgreementId.Code, Item, PortfolioId.Scope, PortfolioId.Code, HoldingId, CustodianAccountScope, CustodianAccountCode, CustodianAccountName, Units, Pv, VariationMargin and CollateralValue. For more information about filtering results, see https://support.lusid.com/docs/filtering-information-retrieved-from-lusid. (optional)
    scenarios = ['scenarios_example'] # List[str] | The scenarios, each as scope/code, whose lines are listed beside the base case lines, which are always listed. Lists the base case lines only if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_margin_lines(run_id, page=page, limit=limit, filter=filter, scenarios=scenarios, opts=opts)

        # [EXPERIMENTAL] ListMarginLines: List the margin lines of a run.
        api_response = api_instance.list_margin_lines(run_id, page=page, limit=limit, filter=filter, scenarios=scenarios)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling CollateralApi->list_margin_lines: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**| The identifier of the margin run. | 
 **page** | **str**| The pagination token to use to continue listing margin lines; this value is returned from the previous call. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results. The filterable fields are AgreementId.Scope, AgreementId.Code, Item, PortfolioId.Scope, PortfolioId.Code, HoldingId, CustodianAccountScope, CustodianAccountCode, CustodianAccountName, Units, Pv, VariationMargin and CollateralValue. For more information about filtering results, see https://support.lusid.com/docs/filtering-information-retrieved-from-lusid. | [optional] 
 **scenarios** | [**List[str]**](str.md)| The scenarios, each as scope/code, whose lines are listed beside the base case lines, which are always listed. Lists the base case lines only if not specified. | [optional] 

### Return type

[**PagedResourceListOfMarginLine**](PagedResourceListOfMarginLine.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested margin lines. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_margin_runs**
> PagedResourceListOfMarginRun list_margin_runs(page=page, limit=limit, filter=filter)

[EXPERIMENTAL] ListMarginRuns: List margin runs.

List the margin runs on record, most recent first.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    CollateralApi
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
    api_instance = api_client_factory.build(CollateralApi)
    page = 'page_example' # str | The pagination token to use to continue listing margin runs; this value is returned from the previous call. (optional)
    limit = 56 # int | When paginating, limit the results to this number. Defaults to 100 if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the results. The filterable fields are Id, EffectiveAt, AsAt, Status, CallCount and LineCount. For example, to find the runs for a business date, specify \"EffectiveAt eq 2026-09-04\". For more information about filtering results, see https://support.lusid.com/docs/filtering-information-retrieved-from-lusid. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_margin_runs(page=page, limit=limit, filter=filter, opts=opts)

        # [EXPERIMENTAL] ListMarginRuns: List margin runs.
        api_response = api_instance.list_margin_runs(page=page, limit=limit, filter=filter)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling CollateralApi->list_margin_runs: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **str**| The pagination token to use to continue listing margin runs; this value is returned from the previous call. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results. The filterable fields are Id, EffectiveAt, AsAt, Status, CallCount and LineCount. For example, to find the runs for a business date, specify \&quot;EffectiveAt eq 2026-09-04\&quot;. For more information about filtering results, see https://support.lusid.com/docs/filtering-information-retrieved-from-lusid. | [optional] 

### Return type

[**PagedResourceListOfMarginRun**](PagedResourceListOfMarginRun.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested margin runs. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **record_counterparty_demand**
> MarginCall record_counterparty_demand(run_id, agreement_scope, agreement_code, item, margin_type, direction, record_counterparty_demand_request)

[EXPERIMENTAL] RecordCounterpartyDemand: Record the counterparty's demand against a margin call.

Record the counterparty's figure for a margin call and match it to ours: equal is matched, a difference within the  agreement's tolerance is within tolerance, and a larger difference is a break. The call's state is not changed,  except that a call already accepted or disputed returns to calculated when its demand changes.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    CollateralApi
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
    api_instance = api_client_factory.build(CollateralApi)
    run_id = 'run_id_example' # str | The identifier of the margin run.
    agreement_scope = 'agreement_scope_example' # str | The scope of the call's collateral agreement.
    agreement_code = 'agreement_code_example' # str | The code of the call's collateral agreement.
    item = 'item_example' # str | The margin item of the call.
    margin_type = 'margin_type_example' # str | The margin type of the call. Currently VariationMargin.
    direction = 'direction_example' # str | Who posts under the call. One of WePost, TheyPost or None.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # record_counterparty_demand_request = RecordCounterpartyDemandRequest.from_json("")
    # record_counterparty_demand_request = RecordCounterpartyDemandRequest.from_dict({})
    record_counterparty_demand_request = RecordCounterpartyDemandRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.record_counterparty_demand(run_id, agreement_scope, agreement_code, item, margin_type, direction, record_counterparty_demand_request, opts=opts)

        # [EXPERIMENTAL] RecordCounterpartyDemand: Record the counterparty's demand against a margin call.
        api_response = api_instance.record_counterparty_demand(run_id, agreement_scope, agreement_code, item, margin_type, direction, record_counterparty_demand_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling CollateralApi->record_counterparty_demand: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**| The identifier of the margin run. | 
 **agreement_scope** | **str**| The scope of the call&#39;s collateral agreement. | 
 **agreement_code** | **str**| The code of the call&#39;s collateral agreement. | 
 **item** | **str**| The margin item of the call. | 
 **margin_type** | **str**| The margin type of the call. Currently VariationMargin. | 
 **direction** | **str**| Who posts under the call. One of WePost, TheyPost or None. | 
 **record_counterparty_demand_request** | [**RecordCounterpartyDemandRequest**](RecordCounterpartyDemandRequest.md)| The counterparty&#39;s demand. | 

### Return type

[**MarginCall**](MarginCall.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The margin call with the demand matched against it. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **retry_margin_run**
> MarginRun retry_margin_run(run_id)

[EXPERIMENTAL] RetryMarginRun: Retry a margin run.

Value the failed shards of a completed margin run again, at the run's asAt. Refused while the run is in progress  or when no shard failed.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    CollateralApi
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
    api_instance = api_client_factory.build(CollateralApi)
    run_id = 'run_id_example' # str | The identifier of the margin run.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.retry_margin_run(run_id, opts=opts)

        # [EXPERIMENTAL] RetryMarginRun: Retry a margin run.
        api_response = api_instance.retry_margin_run(run_id)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling CollateralApi->retry_margin_run: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**| The identifier of the margin run. | 

### Return type

[**MarginRun**](MarginRun.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | The margin run with its failed shards pending again. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **run_margin_calculation**
> PagedResourceListOfMarginRun run_margin_calculation(margin_run_request)

[EXPERIMENTAL] RunMarginCalculation: Run the margin calculation.

Value the collateral agreements for a business date, or for each weekday of a span, in the background and publish  their margin calls as a run for each date. The base case is always valued, with each scenario named in the request  valued beside it as a case of the same run. A date after the asAt is a projection on the market as at the asAt.  The runs are returned as planned, in date order; poll GetMarginRun for the progress of each, and list the calls as they are published.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    CollateralApi
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
    api_instance = api_client_factory.build(CollateralApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # margin_run_request = MarginRunRequest.from_json("")
    # margin_run_request = MarginRunRequest.from_dict({})
    margin_run_request = MarginRunRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.run_margin_calculation(margin_run_request, opts=opts)

        # [EXPERIMENTAL] RunMarginCalculation: Run the margin calculation.
        api_response = api_instance.run_margin_calculation(margin_run_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling CollateralApi->run_margin_calculation: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **margin_run_request** | [**MarginRunRequest**](MarginRunRequest.md)| The business date to value, or the span of dates ending at it, and optionally the asAt, the agreements to include and the scenarios to value beside the base case. | 

### Return type

[**PagedResourceListOfMarginRun**](PagedResourceListOfMarginRun.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | The margin runs as planned, one for each date valued. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

