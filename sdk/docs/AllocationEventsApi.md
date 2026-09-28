# lusid.AllocationEventsApi

All URIs are relative to *https://fbn-prd.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**book_allocation_event**](AllocationEventsApi.md#book_allocation_event) | **POST** /api/allocationevents/{scope}/{code}/book | [EXPERIMENTAL] BookAllocationEvent: Book an Allocation Event.
[**create_allocation_event**](AllocationEventsApi.md#create_allocation_event) | **POST** /api/allocationevents/{scope} | [EXPERIMENTAL] CreateAllocationEvent: Create an Allocation Event.
[**delete_allocation_event**](AllocationEventsApi.md#delete_allocation_event) | **DELETE** /api/allocationevents/{scope}/{code} | [EXPERIMENTAL] DeleteAllocationEvent: Delete an Allocation Event.
[**get_allocation_event**](AllocationEventsApi.md#get_allocation_event) | **GET** /api/allocationevents/{scope}/{code} | [EXPERIMENTAL] GetAllocationEvent: Get an Allocation Event.
[**list_allocation_events**](AllocationEventsApi.md#list_allocation_events) | **GET** /api/allocationevents | [EXPERIMENTAL] ListAllocationEvents: List Allocation Events.
[**reallocate_allocation_event**](AllocationEventsApi.md#reallocate_allocation_event) | **POST** /api/allocationevents/{scope}/{code}/reallocate | [EXPERIMENTAL] ReallocateAllocationEvent: Reallocate an Allocation Event.
[**upsert_allocation_event**](AllocationEventsApi.md#upsert_allocation_event) | **PUT** /api/allocationevents/{scope}/{code} | [EXPERIMENTAL] UpsertAllocationEvent: Upsert an Allocation Event.


# **book_allocation_event**
> AllocationEvent book_allocation_event(scope, code, allocation_event_book_request, effective_at=effective_at)

[EXPERIMENTAL] BookAllocationEvent: Book an Allocation Event.

Freeze a computed Allocation Event under a booking reference, from an effective datetime. Once booked the  event can no longer be replaced or reallocated. Booking again under the same reference returns the event  unchanged; booking under a different reference is refused.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    AllocationEventsApi
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
    api_instance = api_client_factory.build(AllocationEventsApi)
    scope = 'scope_example' # str | The scope of the Allocation Event.
    code = 'code_example' # str | The code of the Allocation Event. Together with the scope this uniquely identifies the Allocation Event.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # allocation_event_book_request = AllocationEventBookRequest.from_json("")
    # allocation_event_book_request = AllocationEventBookRequest.from_dict({})
    allocation_event_book_request = AllocationEventBookRequest()
    effective_at = 'effective_at_example' # str | The effective datetime or cut label from which the booking applies. Defaults to the current LUSID system datetime if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.book_allocation_event(scope, code, allocation_event_book_request, effective_at=effective_at, opts=opts)

        # [EXPERIMENTAL] BookAllocationEvent: Book an Allocation Event.
        api_response = api_instance.book_allocation_event(scope, code, allocation_event_book_request, effective_at=effective_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling AllocationEventsApi->book_allocation_event: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Allocation Event. | 
 **code** | **str**| The code of the Allocation Event. Together with the scope this uniquely identifies the Allocation Event. | 
 **allocation_event_book_request** | [**AllocationEventBookRequest**](AllocationEventBookRequest.md)| The booking reference to freeze the event under. | 
 **effective_at** | **str**| The effective datetime or cut label from which the booking applies. Defaults to the current LUSID system datetime if not specified. | [optional] 

### Return type

[**AllocationEvent**](AllocationEvent.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The booked Allocation Event. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **create_allocation_event**
> AllocationEvent create_allocation_event(scope, allocation_event_request)

[EXPERIMENTAL] CreateAllocationEvent: Create an Allocation Event.

Raise a new Allocation Event. The scope is provided in the route and the code in the request body. The event  names the Allocation Map it is shared by, the kind of event, the amount and the date. Its per-investor shares  are computed on creation from the map as it stood on the event date, so the response comes back Computed.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    AllocationEventsApi
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
    api_instance = api_client_factory.build(AllocationEventsApi)
    scope = 'scope_example' # str | The scope of the Allocation Event.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # allocation_event_request = AllocationEventRequest.from_json("")
    # allocation_event_request = AllocationEventRequest.from_dict({})
    allocation_event_request = AllocationEventRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.create_allocation_event(scope, allocation_event_request, opts=opts)

        # [EXPERIMENTAL] CreateAllocationEvent: Create an Allocation Event.
        api_response = api_instance.create_allocation_event(scope, allocation_event_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling AllocationEventsApi->create_allocation_event: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Allocation Event. | 
 **allocation_event_request** | [**AllocationEventRequest**](AllocationEventRequest.md)| The definition of the Allocation Event. | 

### Return type

[**AllocationEvent**](AllocationEvent.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created Allocation Event. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_allocation_event**
> DeletedEntityResponse delete_allocation_event(scope, code, effective_at=effective_at)

[EXPERIMENTAL] DeleteAllocationEvent: Delete an Allocation Event.

Delete an Allocation Event from an effective datetime. The Allocation Event remains retrievable at earlier  effective datetimes.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    AllocationEventsApi
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
    api_instance = api_client_factory.build(AllocationEventsApi)
    scope = 'scope_example' # str | The scope of the Allocation Event.
    code = 'code_example' # str | The code of the Allocation Event. Together with the scope this uniquely identifies the Allocation Event.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label from which to delete the Allocation Event. Defaults to the current LUSID system datetime if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_allocation_event(scope, code, effective_at=effective_at, opts=opts)

        # [EXPERIMENTAL] DeleteAllocationEvent: Delete an Allocation Event.
        api_response = api_instance.delete_allocation_event(scope, code, effective_at=effective_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling AllocationEventsApi->delete_allocation_event: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Allocation Event. | 
 **code** | **str**| The code of the Allocation Event. Together with the scope this uniquely identifies the Allocation Event. | 
 **effective_at** | **str**| The effective datetime or cut label from which to delete the Allocation Event. Defaults to the current LUSID system datetime if not specified. | [optional] 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the Allocation Event was deleted. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_allocation_event**
> AllocationEvent get_allocation_event(scope, code, effective_at=effective_at, as_at=as_at)

[EXPERIMENTAL] GetAllocationEvent: Get an Allocation Event.

Retrieve a particular Allocation Event at an effective and asAt datetime, including its computed  per-investor shares and, once booked, its booking reference.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    AllocationEventsApi
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
    api_instance = api_client_factory.build(AllocationEventsApi)
    scope = 'scope_example' # str | The scope of the Allocation Event.
    code = 'code_example' # str | The code of the Allocation Event. Together with the scope this uniquely identifies the Allocation Event.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve the Allocation Event. Defaults to the current LUSID system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Allocation Event. Defaults to returning the latest version if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_allocation_event(scope, code, effective_at=effective_at, as_at=as_at, opts=opts)

        # [EXPERIMENTAL] GetAllocationEvent: Get an Allocation Event.
        api_response = api_instance.get_allocation_event(scope, code, effective_at=effective_at, as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling AllocationEventsApi->get_allocation_event: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Allocation Event. | 
 **code** | **str**| The code of the Allocation Event. Together with the scope this uniquely identifies the Allocation Event. | 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the Allocation Event. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Allocation Event. Defaults to returning the latest version if not specified. | [optional] 

### Return type

[**AllocationEvent**](AllocationEvent.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Allocation Event. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_allocation_events**
> PagedResourceListOfAllocationEvent list_allocation_events(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)

[EXPERIMENTAL] ListAllocationEvents: List Allocation Events.

List all the Allocation Events matching a particular criteria.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    AllocationEventsApi
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
    api_instance = api_client_factory.build(AllocationEventsApi)
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to list the Allocation Events. Defaults to the current LUSID system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the Allocation Events. Defaults to returning the latest version of each Allocation Event if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing Allocation Events; this value is returned from the previous call.              If a pagination token is provided, the filter, effectiveAt and asAt fields must not have changed since the original request. (optional)
    limit = 56 # int | When paginating, limit the results to this number. Defaults to 100 if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the results. For example, to filter on the Allocation Event status, specify \"status eq 'Booked'\".              For more information about filtering LUSID results, see https://support.lusid.com/knowledgebase/article/KA-01914. (optional)
    sort_by = ['sort_by_example'] # List[str] | A list of field names or properties to sort by, each suffixed by \" ASC\" or \" DESC\". (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_allocation_events(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, opts=opts)

        # [EXPERIMENTAL] ListAllocationEvents: List Allocation Events.
        api_response = api_instance.list_allocation_events(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling AllocationEventsApi->list_allocation_events: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **effective_at** | **str**| The effective datetime or cut label at which to list the Allocation Events. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the Allocation Events. Defaults to returning the latest version of each Allocation Event if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing Allocation Events; this value is returned from the previous call.              If a pagination token is provided, the filter, effectiveAt and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results. For example, to filter on the Allocation Event status, specify \&quot;status eq &#39;Booked&#39;\&quot;.              For more information about filtering LUSID results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 

### Return type

[**PagedResourceListOfAllocationEvent**](PagedResourceListOfAllocationEvent.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Allocation Events. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **reallocate_allocation_event**
> AllocationEvent reallocate_allocation_event(scope, code, allocation_event_reallocate_request, effective_at=effective_at)

[EXPERIMENTAL] ReallocateAllocationEvent: Reallocate an Allocation Event.

Recompute the per-investor shares of an unbooked Allocation Event against its map, from an effective  datetime, recording the reason. Any basis values supplied replace those used before. A booked Allocation  Event cannot be reallocated.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    AllocationEventsApi
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
    api_instance = api_client_factory.build(AllocationEventsApi)
    scope = 'scope_example' # str | The scope of the Allocation Event.
    code = 'code_example' # str | The code of the Allocation Event. Together with the scope this uniquely identifies the Allocation Event.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # allocation_event_reallocate_request = AllocationEventReallocateRequest.from_json("")
    # allocation_event_reallocate_request = AllocationEventReallocateRequest.from_dict({})
    allocation_event_reallocate_request = AllocationEventReallocateRequest()
    effective_at = 'effective_at_example' # str | The effective datetime or cut label from which the reallocation applies. Defaults to the current LUSID system datetime if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.reallocate_allocation_event(scope, code, allocation_event_reallocate_request, effective_at=effective_at, opts=opts)

        # [EXPERIMENTAL] ReallocateAllocationEvent: Reallocate an Allocation Event.
        api_response = api_instance.reallocate_allocation_event(scope, code, allocation_event_reallocate_request, effective_at=effective_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling AllocationEventsApi->reallocate_allocation_event: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Allocation Event. | 
 **code** | **str**| The code of the Allocation Event. Together with the scope this uniquely identifies the Allocation Event. | 
 **allocation_event_reallocate_request** | [**AllocationEventReallocateRequest**](AllocationEventReallocateRequest.md)| The reason for the reallocation and any basis values to use. | 
 **effective_at** | **str**| The effective datetime or cut label from which the reallocation applies. Defaults to the current LUSID system datetime if not specified. | [optional] 

### Return type

[**AllocationEvent**](AllocationEvent.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The reallocated Allocation Event. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **upsert_allocation_event**
> AllocationEvent upsert_allocation_event(scope, code, allocation_event_request)

[EXPERIMENTAL] UpsertAllocationEvent: Upsert an Allocation Event.

Update or insert an Allocation Event. If the Allocation Event does not exist it is created, otherwise it is  replaced and its shares recomputed. The code in the request body must match the code in the route. A booked  Allocation Event is frozen and cannot be replaced.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    AllocationEventsApi
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
    api_instance = api_client_factory.build(AllocationEventsApi)
    scope = 'scope_example' # str | The scope of the Allocation Event.
    code = 'code_example' # str | The code of the Allocation Event. Together with the scope this uniquely identifies the Allocation Event.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # allocation_event_request = AllocationEventRequest.from_json("")
    # allocation_event_request = AllocationEventRequest.from_dict({})
    allocation_event_request = AllocationEventRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.upsert_allocation_event(scope, code, allocation_event_request, opts=opts)

        # [EXPERIMENTAL] UpsertAllocationEvent: Upsert an Allocation Event.
        api_response = api_instance.upsert_allocation_event(scope, code, allocation_event_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling AllocationEventsApi->upsert_allocation_event: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Allocation Event. | 
 **code** | **str**| The code of the Allocation Event. Together with the scope this uniquely identifies the Allocation Event. | 
 **allocation_event_request** | [**AllocationEventRequest**](AllocationEventRequest.md)| The definition of the Allocation Event. | 

### Return type

[**AllocationEvent**](AllocationEvent.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The upserted Allocation Event. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

