# lusid.ProcessingGroupApi

All URIs are relative to *https://fbn-prd.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_processing_group**](ProcessingGroupApi.md#create_processing_group) | **POST** /api/processinggroups/{scope} | [EXPERIMENTAL] CreateProcessingGroup: Create a Processing Group.
[**delete_processing_group**](ProcessingGroupApi.md#delete_processing_group) | **DELETE** /api/processinggroups/{scope}/{code} | [EXPERIMENTAL] DeleteProcessingGroup: Delete a Processing Group.
[**get_processing_group**](ProcessingGroupApi.md#get_processing_group) | **GET** /api/processinggroups/{scope}/{code} | [EXPERIMENTAL] GetProcessingGroup: Get a Processing Group.
[**get_processing_group_next_scheduled_details**](ProcessingGroupApi.md#get_processing_group_next_scheduled_details) | **GET** /api/processinggroups/{scope}/{code}/schedule/$next | [EXPERIMENTAL] GetProcessingGroupNextScheduledDetails: Get the next scheduled date of a Processing Group.
[**get_resolved_processing_group_schedule**](ProcessingGroupApi.md#get_resolved_processing_group_schedule) | **GET** /api/processinggroups/{scope}/{code}/schedule/$dates | [EXPERIMENTAL] GetResolvedProcessingGroupSchedule: Get the resolved schedule of a Processing Group.
[**list_processing_groups**](ProcessingGroupApi.md#list_processing_groups) | **GET** /api/processinggroups | [EXPERIMENTAL] ListProcessingGroups: List Processing Groups.
[**patch_processing_group**](ProcessingGroupApi.md#patch_processing_group) | **PATCH** /api/processinggroups/{scope}/{code} | [EXPERIMENTAL] PatchProcessingGroup: Patch a Processing Group.


# **create_processing_group**
> ProcessingGroup create_processing_group(scope, processing_group_request)

[EXPERIMENTAL] CreateProcessingGroup: Create a Processing Group.

Create the given Processing Group.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    ProcessingGroupApi
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
    api_instance = api_client_factory.build(ProcessingGroupApi)
    scope = 'scope_example' # str | The scope of the Processing Group.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # processing_group_request = ProcessingGroupRequest.from_json("")
    # processing_group_request = ProcessingGroupRequest.from_dict({})
    processing_group_request = ProcessingGroupRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.create_processing_group(scope, processing_group_request, opts=opts)

        # [EXPERIMENTAL] CreateProcessingGroup: Create a Processing Group.
        api_response = api_instance.create_processing_group(scope, processing_group_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ProcessingGroupApi->create_processing_group: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Processing Group. | 
 **processing_group_request** | [**ProcessingGroupRequest**](ProcessingGroupRequest.md)| The definition of the Processing Group. | 

### Return type

[**ProcessingGroup**](ProcessingGroup.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created Processing Group. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_processing_group**
> DeletedEntityResponse delete_processing_group(scope, code)

[EXPERIMENTAL] DeleteProcessingGroup: Delete a Processing Group.

Delete the given Processing Group.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    ProcessingGroupApi
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
    api_instance = api_client_factory.build(ProcessingGroupApi)
    scope = 'scope_example' # str | The scope of the Processing Group to be deleted.
    code = 'code_example' # str | The code of the Processing Group to be deleted. Together with the scope this uniquely identifies the Processing Group.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_processing_group(scope, code, opts=opts)

        # [EXPERIMENTAL] DeleteProcessingGroup: Delete a Processing Group.
        api_response = api_instance.delete_processing_group(scope, code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ProcessingGroupApi->delete_processing_group: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Processing Group to be deleted. | 
 **code** | **str**| The code of the Processing Group to be deleted. Together with the scope this uniquely identifies the Processing Group. | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the Processing Group was deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_processing_group**
> ProcessingGroup get_processing_group(scope, code, effective_at=effective_at, as_at=as_at)

[EXPERIMENTAL] GetProcessingGroup: Get a Processing Group.

Retrieve the definition of a particular Processing Group, including the resolved (executed) contents  of its referenced reference list.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    ProcessingGroupApi
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
    api_instance = api_client_factory.build(ProcessingGroupApi)
    scope = 'scope_example' # str | The scope of the Processing Group.
    code = 'code_example' # str | The code of the Processing Group. Together with the scope this uniquely identifies the Processing Group.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve the Processing Group. Defaults to the current LUSID system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Processing Group. Defaults to returning the latest version if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_processing_group(scope, code, effective_at=effective_at, as_at=as_at, opts=opts)

        # [EXPERIMENTAL] GetProcessingGroup: Get a Processing Group.
        api_response = api_instance.get_processing_group(scope, code, effective_at=effective_at, as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ProcessingGroupApi->get_processing_group: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Processing Group. | 
 **code** | **str**| The code of the Processing Group. Together with the scope this uniquely identifies the Processing Group. | 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the Processing Group. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Processing Group. Defaults to returning the latest version if not specified. | [optional] 

### Return type

[**ProcessingGroup**](ProcessingGroup.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Processing Group definition. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_processing_group_next_scheduled_details**
> ProcessingGroupNextScheduledDetails get_processing_group_next_scheduled_details(scope, code, effective_at, as_at=as_at)

[EXPERIMENTAL] GetProcessingGroupNextScheduledDetails: Get the next scheduled date of a Processing Group.

Return the first execution date strictly after the given date, bounded by the schedule's end,  together with the reference list resolved at that date.  Returns 404 if the schedule has no further dates or the referenced reference list no longer exists,  and fails rather than returning a date without a list if the list cannot be resolved.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    ProcessingGroupApi
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
    api_instance = api_client_factory.build(ProcessingGroupApi)
    scope = 'scope_example' # str | The scope of the Processing Group.
    code = 'code_example' # str | The code of the Processing Group.
    effective_at = 'effective_at_example' # str | The date after which to find the next scheduled date.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to read the Processing Group and its holiday calendars. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_processing_group_next_scheduled_details(scope, code, effective_at, as_at=as_at, opts=opts)

        # [EXPERIMENTAL] GetProcessingGroupNextScheduledDetails: Get the next scheduled date of a Processing Group.
        api_response = api_instance.get_processing_group_next_scheduled_details(scope, code, effective_at, as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ProcessingGroupApi->get_processing_group_next_scheduled_details: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Processing Group. | 
 **code** | **str**| The code of the Processing Group. | 
 **effective_at** | **str**| The date after which to find the next scheduled date. | 
 **as_at** | **datetime**| The asAt datetime at which to read the Processing Group and its holiday calendars. | [optional] 

### Return type

[**ProcessingGroupNextScheduledDetails**](ProcessingGroupNextScheduledDetails.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The next scheduled date and the resolved reference list. |  -  |
**404** | The schedule has no date after the given date, or the referenced reference list does not exist. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_resolved_processing_group_schedule**
> List[datetime] get_resolved_processing_group_schedule(scope, code, from_effective_at, to_effective_at, as_at=as_at)

[EXPERIMENTAL] GetResolvedProcessingGroupSchedule: Get the resolved schedule of a Processing Group.

Resolve the Processing Group's schedule into the concrete set of execution dates that fall within the  given range, applying its tenor, roll convention, business-day convention and holiday calendars.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    ProcessingGroupApi
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
    api_instance = api_client_factory.build(ProcessingGroupApi)
    scope = 'scope_example' # str | The scope of the Processing Group.
    code = 'code_example' # str | The code of the Processing Group.
    from_effective_at = 'from_effective_at_example' # str | The inclusive start of the date range over which to resolve the schedule.
    to_effective_at = 'to_effective_at_example' # str | The inclusive end of the date range over which to resolve the schedule.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to read the Processing Group and its holiday calendars. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_resolved_processing_group_schedule(scope, code, from_effective_at, to_effective_at, as_at=as_at, opts=opts)

        # [EXPERIMENTAL] GetResolvedProcessingGroupSchedule: Get the resolved schedule of a Processing Group.
        api_response = api_instance.get_resolved_processing_group_schedule(scope, code, from_effective_at, to_effective_at, as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ProcessingGroupApi->get_resolved_processing_group_schedule: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Processing Group. | 
 **code** | **str**| The code of the Processing Group. | 
 **from_effective_at** | **str**| The inclusive start of the date range over which to resolve the schedule. | 
 **to_effective_at** | **str**| The inclusive end of the date range over which to resolve the schedule. | 
 **as_at** | **datetime**| The asAt datetime at which to read the Processing Group and its holiday calendars. | [optional] 

### Return type

**List[datetime]**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The resolved schedule dates within the range. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_processing_groups**
> PagedResourceListOfProcessingGroup list_processing_groups(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)

[EXPERIMENTAL] ListProcessingGroups: List Processing Groups.

List all the Processing Groups matching particular criteria.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    ProcessingGroupApi
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
    api_instance = api_client_factory.build(ProcessingGroupApi)
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to list the Processing Groups. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the Processing Groups. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing Processing Groups. (optional)
    limit = 56 # int | When paginating, limit the results to this number. Defaults to 100 if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the results. (optional)
    sort_by = ['sort_by_example'] # List[str] | A list of field names or properties to sort by, each suffixed by \" ASC\" or \" DESC\". (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_processing_groups(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, opts=opts)

        # [EXPERIMENTAL] ListProcessingGroups: List Processing Groups.
        api_response = api_instance.list_processing_groups(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ProcessingGroupApi->list_processing_groups: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **effective_at** | **str**| The effective datetime or cut label at which to list the Processing Groups. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the Processing Groups. | [optional] 
 **page** | **str**| The pagination token to use to continue listing Processing Groups. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 

### Return type

[**PagedResourceListOfProcessingGroup**](PagedResourceListOfProcessingGroup.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Processing Groups. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **patch_processing_group**
> ProcessingGroup patch_processing_group(scope, code, operation)

[EXPERIMENTAL] PatchProcessingGroup: Patch a Processing Group.

Create or update certain fields (display name, description, schedule) for a particular Processing Group.  The behaviour is defined by the JSON Patch specification.    Currently supported fields are: DisplayName, Description, Schedule, WorkflowId, ListExceptionFilter.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    ProcessingGroupApi
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
    api_instance = api_client_factory.build(ProcessingGroupApi)
    scope = 'scope_example' # str | The scope of the Processing Group.
    code = 'code_example' # str | The code of the Processing Group. Together with the scope this uniquely identifies the Processing Group.
    operation = [{"value":"My Renamed Processing Group","path":"/displayName","op":"add"}] # List[Operation] | The json patch document. For more information see: https://datatracker.ietf.org/doc/html/rfc6902.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.patch_processing_group(scope, code, operation, opts=opts)

        # [EXPERIMENTAL] PatchProcessingGroup: Patch a Processing Group.
        api_response = api_instance.patch_processing_group(scope, code, operation)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ProcessingGroupApi->patch_processing_group: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Processing Group. | 
 **code** | **str**| The code of the Processing Group. Together with the scope this uniquely identifies the Processing Group. | 
 **operation** | [**List[Operation]**](Operation.md)| The json patch document. For more information see: https://datatracker.ietf.org/doc/html/rfc6902. | 

### Return type

[**ProcessingGroup**](ProcessingGroup.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The newly patched Processing Group |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

