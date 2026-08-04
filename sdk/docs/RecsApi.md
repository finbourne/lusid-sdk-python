# lusid.RecsApi

All URIs are relative to *https://fbn-prd.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_rec_result_set_approval_decision**](RecsApi.md#add_rec_result_set_approval_decision) | **POST** /api/recs/resultsets/{entityUniqueId}/$decide | [EXPERIMENTAL] AddRecResultSetApprovalDecision: AddRecResultSetApprovalDecision
[**get_rec_instance**](RecsApi.md#get_rec_instance) | **GET** /api/recs/instances/{instanceIdType}/{instanceIdValue} | [EXPERIMENTAL] GetRecInstance: GetRecInstance
[**get_rec_result_set**](RecsApi.md#get_rec_result_set) | **GET** /api/recs/resultsets/{entityUniqueId} | [EXPERIMENTAL] GetRecResultSet: GetRecResultSet
[**instantiate_rec**](RecsApi.md#instantiate_rec) | **POST** /api/recs/instances | [EXPERIMENTAL] InstantiateRec: InstantiateRec
[**list_rec_instances**](RecsApi.md#list_rec_instances) | **GET** /api/recs/instances | [EXPERIMENTAL] ListRecInstances: ListRecInstances
[**list_rec_result_sets**](RecsApi.md#list_rec_result_sets) | **GET** /api/recs/resultsets | [EXPERIMENTAL] ListRecResultSets: ListRecResultSets
[**submit_rec_result_set_review**](RecsApi.md#submit_rec_result_set_review) | **POST** /api/recs/resultsets/{entityUniqueId}/$submit | [EXPERIMENTAL] SubmitRecResultSetReview: Submit a rec result set review for approval, or resubmit after addressing requested revisions.
[**transition_rec_instance**](RecsApi.md#transition_rec_instance) | **POST** /api/recs/instances/{instanceIdType}/{instanceIdValue}/$transition | [EXPERIMENTAL] TransitionRecInstance: TransitionRecInstance


# **add_rec_result_set_approval_decision**
> RecResultSet add_rec_result_set_approval_decision(entity_unique_id, rec_result_set_approval_decision_request)

[EXPERIMENTAL] AddRecResultSetApprovalDecision: AddRecResultSetApprovalDecision

Add an approver decision (approve or request revisions) to a rec result set.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    RecsApi
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
    api_instance = api_client_factory.build(RecsApi)
    entity_unique_id = 'entity_unique_id_example' # str | The entity unique id of the rec result set (its version.entityUniqueId).

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # rec_result_set_approval_decision_request = RecResultSetApprovalDecisionRequest.from_json("")
    # rec_result_set_approval_decision_request = RecResultSetApprovalDecisionRequest.from_dict({})
    rec_result_set_approval_decision_request = RecResultSetApprovalDecisionRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.add_rec_result_set_approval_decision(entity_unique_id, rec_result_set_approval_decision_request, opts=opts)

        # [EXPERIMENTAL] AddRecResultSetApprovalDecision: AddRecResultSetApprovalDecision
        api_response = api_instance.add_rec_result_set_approval_decision(entity_unique_id, rec_result_set_approval_decision_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling RecsApi->add_rec_result_set_approval_decision: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_unique_id** | **str**| The entity unique id of the rec result set (its version.entityUniqueId). | 
 **rec_result_set_approval_decision_request** | [**RecResultSetApprovalDecisionRequest**](RecResultSetApprovalDecisionRequest.md)| The approval decision request. | 

### Return type

[**RecResultSet**](RecResultSet.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated rec result set. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_rec_instance**
> RecInstance get_rec_instance(instance_id_type, instance_id_value, as_at=as_at)

[EXPERIMENTAL] GetRecInstance: GetRecInstance

Retrieve a single rec instance by its identifier.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    RecsApi
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
    api_instance = api_client_factory.build(RecsApi)
    instance_id_type = 'instance_id_type_example' # str | How the instance was created: \"WorkflowServiceTaskId\" or \"Manual\". Available values: WorkflowServiceTaskId, Manual.
    instance_id_value = 'instance_id_value_example' # str | The instance identifier value (a GUID).
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the instance. Defaults to latest if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_rec_instance(instance_id_type, instance_id_value, as_at=as_at, opts=opts)

        # [EXPERIMENTAL] GetRecInstance: GetRecInstance
        api_response = api_instance.get_rec_instance(instance_id_type, instance_id_value, as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling RecsApi->get_rec_instance: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id_type** | **str**| How the instance was created: \&quot;WorkflowServiceTaskId\&quot; or \&quot;Manual\&quot;. Available values: WorkflowServiceTaskId, Manual. | 
 **instance_id_value** | **str**| The instance identifier value (a GUID). | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the instance. Defaults to latest if not specified. | [optional] 

### Return type

[**RecInstance**](RecInstance.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested rec instance. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_rec_result_set**
> RecResultSet get_rec_result_set(entity_unique_id, as_at=as_at, include_previous_runs=include_previous_runs)

[EXPERIMENTAL] GetRecResultSet: GetRecResultSet

Retrieve a single rec result set by its entity unique id.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    RecsApi
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
    api_instance = api_client_factory.build(RecsApi)
    entity_unique_id = 'entity_unique_id_example' # str | The entity unique id of the rec result set (its version.entityUniqueId).
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the result set. Defaults to latest if not specified. (optional)
    include_previous_runs = False # bool | When true, the previousRuns array is populated with prior run snapshots. Defaults to false. (optional) (default to False)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_rec_result_set(entity_unique_id, as_at=as_at, include_previous_runs=include_previous_runs, opts=opts)

        # [EXPERIMENTAL] GetRecResultSet: GetRecResultSet
        api_response = api_instance.get_rec_result_set(entity_unique_id, as_at=as_at, include_previous_runs=include_previous_runs)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling RecsApi->get_rec_result_set: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_unique_id** | **str**| The entity unique id of the rec result set (its version.entityUniqueId). | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the result set. Defaults to latest if not specified. | [optional] 
 **include_previous_runs** | **bool**| When true, the previousRuns array is populated with prior run snapshots. Defaults to false. | [optional] [default to False]

### Return type

[**RecResultSet**](RecResultSet.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested rec result set. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **instantiate_rec**
> RecInstance instantiate_rec(instantiate_rec_request)

[EXPERIMENTAL] InstantiateRec: InstantiateRec

Instantiate a new rec instance from a rec definition and start its first run. The run              executes asynchronously; the response returns once the run has started, with the instance Running.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    RecsApi
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
    api_instance = api_client_factory.build(RecsApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # instantiate_rec_request = InstantiateRecRequest.from_json("")
    # instantiate_rec_request = InstantiateRecRequest.from_dict({})
    instantiate_rec_request = InstantiateRecRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.instantiate_rec(instantiate_rec_request, opts=opts)

        # [EXPERIMENTAL] InstantiateRec: InstantiateRec
        api_response = api_instance.instantiate_rec(instantiate_rec_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling RecsApi->instantiate_rec: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instantiate_rec_request** | [**InstantiateRecRequest**](InstantiateRecRequest.md)| The instantiation request. | 

### Return type

[**RecInstance**](RecInstance.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The instantiated rec instance, in a Running state. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_rec_instances**
> PagedResourceListOfRecInstance list_rec_instances(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)

[EXPERIMENTAL] ListRecInstances: ListRecInstances

List rec instances.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    RecsApi
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
    api_instance = api_client_factory.build(RecsApi)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list instances. Defaults to latest if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing instances from a previous call. If a pagination token is provided the filter and asAt fields must not have changed since the original request. (optional)
    limit = 56 # int | When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)
    sort_by = ['sort_by_example'] # List[str] | A list of field names suffixed by \" ASC\" or \" DESC\". (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_rec_instances(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, opts=opts)

        # [EXPERIMENTAL] ListRecInstances: ListRecInstances
        api_response = api_instance.list_rec_instances(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling RecsApi->list_rec_instances: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list instances. Defaults to latest if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing instances from a previous call. If a pagination token is provided the filter and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 

### Return type

[**PagedResourceListOfRecInstance**](PagedResourceListOfRecInstance.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The rec instances. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_rec_result_sets**
> PagedResourceListOfRecResultSet list_rec_result_sets(as_at=as_at, include_previous_runs=include_previous_runs, page=page, limit=limit, filter=filter, sort_by=sort_by)

[EXPERIMENTAL] ListRecResultSets: ListRecResultSets

List rec result sets.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    RecsApi
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
    api_instance = api_client_factory.build(RecsApi)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list result sets. Defaults to latest if not specified. (optional)
    include_previous_runs = False # bool | When true, each item's previousRuns array is populated with prior run snapshots. Defaults to false. (optional) (default to False)
    page = 'page_example' # str | The pagination token to use to continue listing result sets from a previous call. If a pagination token is provided the filter and asAt fields must not have changed since the original request. (optional)
    limit = 56 # int | When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)
    sort_by = ['sort_by_example'] # List[str] | A list of field names suffixed by \" ASC\" or \" DESC\". (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_rec_result_sets(as_at=as_at, include_previous_runs=include_previous_runs, page=page, limit=limit, filter=filter, sort_by=sort_by, opts=opts)

        # [EXPERIMENTAL] ListRecResultSets: ListRecResultSets
        api_response = api_instance.list_rec_result_sets(as_at=as_at, include_previous_runs=include_previous_runs, page=page, limit=limit, filter=filter, sort_by=sort_by)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling RecsApi->list_rec_result_sets: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list result sets. Defaults to latest if not specified. | [optional] 
 **include_previous_runs** | **bool**| When true, each item&#39;s previousRuns array is populated with prior run snapshots. Defaults to false. | [optional] [default to False]
 **page** | **str**| The pagination token to use to continue listing result sets from a previous call. If a pagination token is provided the filter and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 

### Return type

[**PagedResourceListOfRecResultSet**](PagedResourceListOfRecResultSet.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The rec result sets. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **submit_rec_result_set_review**
> RecResultSet submit_rec_result_set_review(entity_unique_id, submit_rec_result_set_review_request)

[EXPERIMENTAL] SubmitRecResultSetReview: Submit a rec result set review for approval, or resubmit after addressing requested revisions.

Submit a rec result set review for approval, or resubmit after addressing requested revisions.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    RecsApi
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
    api_instance = api_client_factory.build(RecsApi)
    entity_unique_id = 'entity_unique_id_example' # str | The entity unique id of the rec result set (its version.entityUniqueId).

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # submit_rec_result_set_review_request = SubmitRecResultSetReviewRequest.from_json("")
    # submit_rec_result_set_review_request = SubmitRecResultSetReviewRequest.from_dict({})
    submit_rec_result_set_review_request = SubmitRecResultSetReviewRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.submit_rec_result_set_review(entity_unique_id, submit_rec_result_set_review_request, opts=opts)

        # [EXPERIMENTAL] SubmitRecResultSetReview: Submit a rec result set review for approval, or resubmit after addressing requested revisions.
        api_response = api_instance.submit_rec_result_set_review(entity_unique_id, submit_rec_result_set_review_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling RecsApi->submit_rec_result_set_review: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_unique_id** | **str**| The entity unique id of the rec result set (its version.entityUniqueId). | 
 **submit_rec_result_set_review_request** | [**SubmitRecResultSetReviewRequest**](SubmitRecResultSetReviewRequest.md)| The submission request. | 

### Return type

[**RecResultSet**](RecResultSet.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated rec result set. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **transition_rec_instance**
> RecInstance transition_rec_instance(instance_id_type, instance_id_value, transition_rec_instance_request)

[EXPERIMENTAL] TransitionRecInstance: TransitionRecInstance

Apply a lifecycle transition (re-run, lock or unlock) to a rec instance.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    RecsApi
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
    api_instance = api_client_factory.build(RecsApi)
    instance_id_type = 'instance_id_type_example' # str | How the instance was created: \"WorkflowServiceTaskId\" or \"Manual\". Available values: WorkflowServiceTaskId, Manual.
    instance_id_value = 'instance_id_value_example' # str | The instance identifier value (a GUID).

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # transition_rec_instance_request = TransitionRecInstanceRequest.from_json("")
    # transition_rec_instance_request = TransitionRecInstanceRequest.from_dict({})
    transition_rec_instance_request = TransitionRecInstanceRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.transition_rec_instance(instance_id_type, instance_id_value, transition_rec_instance_request, opts=opts)

        # [EXPERIMENTAL] TransitionRecInstance: TransitionRecInstance
        api_response = api_instance.transition_rec_instance(instance_id_type, instance_id_value, transition_rec_instance_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling RecsApi->transition_rec_instance: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id_type** | **str**| How the instance was created: \&quot;WorkflowServiceTaskId\&quot; or \&quot;Manual\&quot;. Available values: WorkflowServiceTaskId, Manual. | 
 **instance_id_value** | **str**| The instance identifier value (a GUID). | 
 **transition_rec_instance_request** | [**TransitionRecInstanceRequest**](TransitionRecInstanceRequest.md)| The transition request. | 

### Return type

[**RecInstance**](RecInstance.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The rec instance in its post-transition state. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

