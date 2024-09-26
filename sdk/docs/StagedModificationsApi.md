# lusid.StagedModificationsApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_decision**](StagedModificationsApi.md#add_decision) | **POST** /api/stagedmodifications/{id}/decision | [EXPERIMENTAL] AddDecision: AddDecision
[**get_staged_modification**](StagedModificationsApi.md#get_staged_modification) | **GET** /api/stagedmodifications/{id} | [EXPERIMENTAL] GetStagedModification: GetStagedModification
[**list_requested_changes**](StagedModificationsApi.md#list_requested_changes) | **GET** /api/stagedmodifications/{id}/requestedChanges | [EXPERIMENTAL] ListRequestedChanges: ListRequestedChanges
[**list_staged_modifications**](StagedModificationsApi.md#list_staged_modifications) | **GET** /api/stagedmodifications | [EXPERIMENTAL] ListStagedModifications: ListStagedModifications


# **add_decision**
> StagedModification add_decision(id, staged_modification_decision_request)

[EXPERIMENTAL] AddDecision: AddDecision

Add decision to staged modification, Approve or Reject.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    StagedModificationsApi
)

async def main():

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

    # Use the lusid ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(StagedModificationsApi)
        id = 'id_example' # str | Unique Id for a staged modification..

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # staged_modification_decision_request = StagedModificationDecisionRequest()
        # staged_modification_decision_request = StagedModificationDecisionRequest.from_json("")
        staged_modification_decision_request = StagedModificationDecisionRequest.from_dict({"decision":"Approve","comment":"Looks Good"}) # StagedModificationDecisionRequest | The decision on the requested staged modification, \"Approve\" or \"Reject\".

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.add_decision(id, staged_modification_decision_request, opts=opts)

            # [EXPERIMENTAL] AddDecision: AddDecision
            api_response = await api_instance.add_decision(id, staged_modification_decision_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling StagedModificationsApi->add_decision: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique Id for a staged modification.. | 
 **staged_modification_decision_request** | [**StagedModificationDecisionRequest**](StagedModificationDecisionRequest.md)| The decision on the requested staged modification, \&quot;Approve\&quot; or \&quot;Reject\&quot;. | 

### Return type

[**StagedModification**](StagedModification.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The staged modification. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_staged_modification**
> StagedModification get_staged_modification(id, as_at=as_at)

[EXPERIMENTAL] GetStagedModification: GetStagedModification

Retrieve the details of a staged modification.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    StagedModificationsApi
)

async def main():

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

    # Use the lusid ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(StagedModificationsApi)
        id = 'id_example' # str | The unique identifier for a staged modification.
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the staged modification. Defaults to latest if not specified. (optional)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.get_staged_modification(id, as_at=as_at, opts=opts)

            # [EXPERIMENTAL] GetStagedModification: GetStagedModification
            api_response = await api_instance.get_staged_modification(id, as_at=as_at)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling StagedModificationsApi->get_staged_modification: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for a staged modification. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the staged modification. Defaults to latest if not specified. | [optional] 

### Return type

[**StagedModification**](StagedModification.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested staged modification. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_requested_changes**
> PagedResourceListOfStagedModificationsRequestedChangeInterval list_requested_changes(id, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)

[EXPERIMENTAL] ListRequestedChanges: ListRequestedChanges

List the requested changes for a staged modification.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    StagedModificationsApi
)

async def main():

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

    # Use the lusid ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(StagedModificationsApi)
        id = 'id_example' # str | Unique Id for a staged modification..
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list changes. Defaults to return the latest version              of each staged change if not specified. (optional)
        page = 'page_example' # str | The pagination token to use to continue listing requested staged modification changes from a previous call to list requested              staged modifications. This value is returned from the previous call. If a pagination token is provided the filter, effectiveAt              and asAt fields must not have changed since the original request. (optional)
        limit = 56 # int | When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. (optional)
        filter = 'filter_example' # str | Expression to filter the result set.              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)
        sort_by = ['sort_by_example'] # List[str] | A list of field names suffixed by \" ASC\" or \" DESC\" (optional)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.list_requested_changes(id, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, opts=opts)

            # [EXPERIMENTAL] ListRequestedChanges: ListRequestedChanges
            api_response = await api_instance.list_requested_changes(id, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling StagedModificationsApi->list_requested_changes: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique Id for a staged modification.. | 
 **as_at** | **datetime**| The asAt datetime at which to list changes. Defaults to return the latest version              of each staged change if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing requested staged modification changes from a previous call to list requested              staged modifications. This value is returned from the previous call. If a pagination token is provided the filter, effectiveAt              and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set.              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot; | [optional] 

### Return type

[**PagedResourceListOfStagedModificationsRequestedChangeInterval**](PagedResourceListOfStagedModificationsRequestedChangeInterval.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Requested changes in staged modification. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_staged_modifications**
> PagedResourceListOfStagedModification list_staged_modifications(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)

[EXPERIMENTAL] ListStagedModifications: ListStagedModifications

List summaries of the staged modifications.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    StagedModificationsApi
)

async def main():

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

    # Use the lusid ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(StagedModificationsApi)
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list staged modifications. Defaults to return the latest version              of each staged modification if not specified. (optional)
        page = 'page_example' # str | The pagination token to use to continue listing staged modifications from a previous call to list staged modifications. This              value is returned from the previous call. If a pagination token is provided the filter, effectiveAt              and asAt fields must not have changed since the original request. (optional)
        limit = 56 # int | When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. (optional)
        filter = 'filter_example' # str | Expression to filter the result set.               Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)
        sort_by = ['sort_by_example'] # List[str] | A list of field names suffixed by \" ASC\" or \" DESC\" (optional)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.list_staged_modifications(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, opts=opts)

            # [EXPERIMENTAL] ListStagedModifications: ListStagedModifications
            api_response = await api_instance.list_staged_modifications(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling StagedModificationsApi->list_staged_modifications: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list staged modifications. Defaults to return the latest version              of each staged modification if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing staged modifications from a previous call to list staged modifications. This              value is returned from the previous call. If a pagination token is provided the filter, effectiveAt              and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set.               Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot; | [optional] 

### Return type

[**PagedResourceListOfStagedModification**](PagedResourceListOfStagedModification.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List summary of staged modifications. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

