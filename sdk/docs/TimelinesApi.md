# lusid.TimelinesApi

All URIs are relative to *https://fbn-prd.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**confirm_closed_period**](TimelinesApi.md#confirm_closed_period) | **POST** /api/timelines/{scope}/{code}/closedperiods/{closedPeriodId}/$confirm | [EXPERIMENTAL] ConfirmClosedPeriod: Confirm a Closed Period against a Timeline Entity
[**create_closed_period**](TimelinesApi.md#create_closed_period) | **POST** /api/timelines/{scope}/{code}/closedperiods | [EXPERIMENTAL] CreateClosedPeriod: Create a new closed period against a timeline entity
[**create_closed_period_candidate**](TimelinesApi.md#create_closed_period_candidate) | **POST** /api/timelines/{scope}/{code}/closedperiods/candidate | [EXPERIMENTAL] CreateClosedPeriodCandidate: Create a new closed period candidate against a timeline entity
[**create_timeline**](TimelinesApi.md#create_timeline) | **POST** /api/timelines | [EXPERIMENTAL] CreateTimeline: Create a Timeline
[**delete_timeline**](TimelinesApi.md#delete_timeline) | **DELETE** /api/timelines/{scope}/{code} | [EXPERIMENTAL] DeleteTimeline: Deletes a particular Timeline
[**get_closed_period**](TimelinesApi.md#get_closed_period) | **GET** /api/timelines/{scope}/{code}/closedperiods/{closedPeriodId} | [EXPERIMENTAL] GetClosedPeriod: Gets a Closed Period entity.
[**get_timeline**](TimelinesApi.md#get_timeline) | **GET** /api/timelines/{scope}/{code} | [EXPERIMENTAL] GetTimeline: Get a single Timeline by scope and code.
[**list_closed_periods**](TimelinesApi.md#list_closed_periods) | **GET** /api/timelines/{scope}/{code}/closedperiods | [EXPERIMENTAL] ListClosedPeriods: List ClosedPeriods for a specified Timeline.
[**list_timelines**](TimelinesApi.md#list_timelines) | **GET** /api/timelines | [EXPERIMENTAL] ListTimelines: List Timelines
[**set_post_close_activity**](TimelinesApi.md#set_post_close_activity) | **POST** /api/timelines/{scope}/{code}/closedperiods/{closedPeriodId}/postcloseactivity | [EXPERIMENTAL] SetPostCloseActivity: Sets post-close activities to a Closed Period.
[**unconfirm_closed_period**](TimelinesApi.md#unconfirm_closed_period) | **POST** /api/timelines/{scope}/{code}/closedperiods/{closedPeriodId}/$unconfirm | [EXPERIMENTAL] UnconfirmClosedPeriod: Unconfirm the last confirmed Closed Period against a Timeline Entity
[**update_timeline**](TimelinesApi.md#update_timeline) | **PUT** /api/timelines/{scope}/{code} | [EXPERIMENTAL] UpdateTimeline: Update Timeline defined by scope and code


# **confirm_closed_period**
> ClosedPeriod confirm_closed_period(scope, code, closed_period_id, body=body)

[EXPERIMENTAL] ConfirmClosedPeriod: Confirm a Closed Period against a Timeline Entity

Confirms a Closed Period against a Timeline Entity. Deletes any other unconfirmed Closed Periods on the Timeline.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TimelinesApi
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
    api_instance = api_client_factory.build(TimelinesApi)
    scope = 'scope_example' # str | The scope of the specified Timeline.
    code = 'code_example' # str | The code of the specified Timeline. Together with the scope this uniquely identifies the Timeline.
    closed_period_id = 'closed_period_id_example' # str | The id of the Closed Period. Together with the scope and code of the Timeline,              this uniquely identifies the ClosedPeriod
    body = {} # object | Not in use at the moment (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.confirm_closed_period(scope, code, closed_period_id, body=body, opts=opts)

        # [EXPERIMENTAL] ConfirmClosedPeriod: Confirm a Closed Period against a Timeline Entity
        api_response = api_instance.confirm_closed_period(scope, code, closed_period_id, body=body)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TimelinesApi->confirm_closed_period: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the specified Timeline. | 
 **code** | **str**| The code of the specified Timeline. Together with the scope this uniquely identifies the Timeline. | 
 **closed_period_id** | **str**| The id of the Closed Period. Together with the scope and code of the Timeline,              this uniquely identifies the ClosedPeriod | 
 **body** | **object**| Not in use at the moment | [optional] 

### Return type

[**ClosedPeriod**](ClosedPeriod.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The confirmed closed period |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **create_closed_period**
> ClosedPeriod create_closed_period(scope, code, create_closed_period_request=create_closed_period_request)

[EXPERIMENTAL] CreateClosedPeriod: Create a new closed period against a timeline entity

Creates a new closed period against a timeline entity  Returns the newly created closed period entity with properties

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TimelinesApi
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
    api_instance = api_client_factory.build(TimelinesApi)
    scope = 'scope_example' # str | The scope of the specified Timeline.
    code = 'code_example' # str | The code of the specified Timeline. Together with the domain and scope this uniquely identifies the Timeline.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # create_closed_period_request = CreateClosedPeriodRequest.from_json("")
    # create_closed_period_request = CreateClosedPeriodRequest.from_dict({})
    create_closed_period_request = CreateClosedPeriodRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.create_closed_period(scope, code, create_closed_period_request=create_closed_period_request, opts=opts)

        # [EXPERIMENTAL] CreateClosedPeriod: Create a new closed period against a timeline entity
        api_response = api_instance.create_closed_period(scope, code, create_closed_period_request=create_closed_period_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TimelinesApi->create_closed_period: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the specified Timeline. | 
 **code** | **str**| The code of the specified Timeline. Together with the domain and scope this uniquely identifies the Timeline. | 
 **create_closed_period_request** | [**CreateClosedPeriodRequest**](CreateClosedPeriodRequest.md)| The request containing the details of the Closed Period | [optional] 

### Return type

[**ClosedPeriod**](ClosedPeriod.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created closed period |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **create_closed_period_candidate**
> ClosedPeriod create_closed_period_candidate(scope, code, create_closed_period_request=create_closed_period_request)

[EXPERIMENTAL] CreateClosedPeriodCandidate: Create a new closed period candidate against a timeline entity

Creates a new closed period candidate against a timeline entity  Returns the newly created closed period candidate entity with properties

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TimelinesApi
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
    api_instance = api_client_factory.build(TimelinesApi)
    scope = 'scope_example' # str | The scope of the specified Timeline.
    code = 'code_example' # str | The code of the specified Timeline. Together with the scope this uniquely identifies the Timeline.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # create_closed_period_request = CreateClosedPeriodRequest.from_json("")
    # create_closed_period_request = CreateClosedPeriodRequest.from_dict({})
    create_closed_period_request = CreateClosedPeriodRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.create_closed_period_candidate(scope, code, create_closed_period_request=create_closed_period_request, opts=opts)

        # [EXPERIMENTAL] CreateClosedPeriodCandidate: Create a new closed period candidate against a timeline entity
        api_response = api_instance.create_closed_period_candidate(scope, code, create_closed_period_request=create_closed_period_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TimelinesApi->create_closed_period_candidate: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the specified Timeline. | 
 **code** | **str**| The code of the specified Timeline. Together with the scope this uniquely identifies the Timeline. | 
 **create_closed_period_request** | [**CreateClosedPeriodRequest**](CreateClosedPeriodRequest.md)| The request containing the details of the Closed Period | [optional] 

### Return type

[**ClosedPeriod**](ClosedPeriod.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created closed period |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **create_timeline**
> Timeline create_timeline(create_timeline_request=create_timeline_request)

[EXPERIMENTAL] CreateTimeline: Create a Timeline

Creates a Timeline. Returns the created Timeline at the current effectiveAt.  Note that Timelines are mono-temporal, however they can have Time-Variant Properties.  Upserted Properties will be returned at the latest AsAt and EffectiveAt

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TimelinesApi
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
    api_instance = api_client_factory.build(TimelinesApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # create_timeline_request = CreateTimelineRequest.from_json("")
    # create_timeline_request = CreateTimelineRequest.from_dict({})
    create_timeline_request = CreateTimelineRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.create_timeline(create_timeline_request=create_timeline_request, opts=opts)

        # [EXPERIMENTAL] CreateTimeline: Create a Timeline
        api_response = api_instance.create_timeline(create_timeline_request=create_timeline_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TimelinesApi->create_timeline: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_timeline_request** | [**CreateTimelineRequest**](CreateTimelineRequest.md)| The request containing the details of the Timeline | [optional] 

### Return type

[**Timeline**](Timeline.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created Timeline |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_timeline**
> DeletedEntityResponse delete_timeline(scope, code)

[EXPERIMENTAL] DeleteTimeline: Deletes a particular Timeline

The deletion will take effect from the Timeline deletion datetime.  i.e. will no longer exist at any asAt datetime after the asAt datetime of deletion.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TimelinesApi
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
    api_instance = api_client_factory.build(TimelinesApi)
    scope = 'scope_example' # str | The scope of the specified Timeline.
    code = 'code_example' # str | The code of the specified Timeline. Together with the domain and scope this uniquely              identifies the Timeline.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_timeline(scope, code, opts=opts)

        # [EXPERIMENTAL] DeleteTimeline: Deletes a particular Timeline
        api_response = api_instance.delete_timeline(scope, code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TimelinesApi->delete_timeline: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the specified Timeline. | 
 **code** | **str**| The code of the specified Timeline. Together with the domain and scope this uniquely              identifies the Timeline. | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The deleted entity metadata |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_closed_period**
> ClosedPeriod get_closed_period(scope, code, closed_period_id, as_at=as_at, property_keys=property_keys)

[EXPERIMENTAL] GetClosedPeriod: Gets a Closed Period entity.

Retrieves one ClosedPeriod uniquely defined by the Timelines Scope/Code and a ClosedPeriodId.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TimelinesApi
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
    api_instance = api_client_factory.build(TimelinesApi)
    scope = 'scope_example' # str | The scope of the Timeline.
    code = 'code_example' # str | The code of the Timeline. Together with the scope this uniquely              identifies the Timeline.
    closed_period_id = 'closed_period_id_example' # str | The id of the Closed Period. Together with the scope and code of the Timeline,              this uniquely identifies the ClosedPeriod
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the ClosedPeriod definition. Defaults to return              the latest version of the definition if not specified. (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the 'ClosedPeriod' domain to decorate onto              the ClosedPeriod.              These must have the format {domain}/{scope}/{code}, for example 'ClosedPeriod/system/Name'. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_closed_period(scope, code, closed_period_id, as_at=as_at, property_keys=property_keys, opts=opts)

        # [EXPERIMENTAL] GetClosedPeriod: Gets a Closed Period entity.
        api_response = api_instance.get_closed_period(scope, code, closed_period_id, as_at=as_at, property_keys=property_keys)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TimelinesApi->get_closed_period: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Timeline. | 
 **code** | **str**| The code of the Timeline. Together with the scope this uniquely              identifies the Timeline. | 
 **closed_period_id** | **str**| The id of the Closed Period. Together with the scope and code of the Timeline,              this uniquely identifies the ClosedPeriod | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the ClosedPeriod definition. Defaults to return              the latest version of the definition if not specified. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;ClosedPeriod&#39; domain to decorate onto              the ClosedPeriod.              These must have the format {domain}/{scope}/{code}, for example &#39;ClosedPeriod/system/Name&#39;. | [optional] 

### Return type

[**ClosedPeriod**](ClosedPeriod.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested closed period |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_timeline**
> Timeline get_timeline(scope, code, as_at=as_at, effective_at=effective_at, property_keys=property_keys)

[EXPERIMENTAL] GetTimeline: Get a single Timeline by scope and code.

Retrieves one Timeline by scope and code.  Timelines are mono-temporal. The EffectiveAt is only applied to Time-Variant Properties.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TimelinesApi
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
    api_instance = api_client_factory.build(TimelinesApi)
    scope = 'scope_example' # str | The scope of the specified Timeline.
    code = 'code_example' # str | The code of the specified Timeline. Together with the scope this uniquely              identifies the Timeline.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Timeline definition. Defaults to return              the latest version of the definition if not specified. (optional)
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve the timeline properties.              Defaults to the current LUSID system datetime if not specified. (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the 'Timeline' domain to decorate onto              the Timeline.              These must have the format {domain}/{scope}/{code}, for example 'Timeline/system/Name'. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_timeline(scope, code, as_at=as_at, effective_at=effective_at, property_keys=property_keys, opts=opts)

        # [EXPERIMENTAL] GetTimeline: Get a single Timeline by scope and code.
        api_response = api_instance.get_timeline(scope, code, as_at=as_at, effective_at=effective_at, property_keys=property_keys)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TimelinesApi->get_timeline: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the specified Timeline. | 
 **code** | **str**| The code of the specified Timeline. Together with the scope this uniquely              identifies the Timeline. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Timeline definition. Defaults to return              the latest version of the definition if not specified. | [optional] 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the timeline properties.              Defaults to the current LUSID system datetime if not specified. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;Timeline&#39; domain to decorate onto              the Timeline.              These must have the format {domain}/{scope}/{code}, for example &#39;Timeline/system/Name&#39;. | [optional] 

### Return type

[**Timeline**](Timeline.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Timeline |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_closed_periods**
> PagedResourceListOfClosedPeriod list_closed_periods(scope, code, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)

[EXPERIMENTAL] ListClosedPeriods: List ClosedPeriods for a specified Timeline.

List all the ClosedPeriods matching a particular criteria.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TimelinesApi
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
    api_instance = api_client_factory.build(TimelinesApi)
    scope = 'scope_example' # str | The scope of the Timeline.
    code = 'code_example' # str | The code of the Timeline.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the ClosedPeriods. Defaults to returning the latest version of each ClosedPeriod if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing ClosedPeriods; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. (optional)
    limit = 56 # int | When paginating, limit the results to this number. Defaults to 100 if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the results.              For example, to filter on the effectiveEnd, specify \"effectiveEnd gt 2019-01-15T10:00:00\". For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. (optional)
    sort_by = ['sort_by_example'] # List[str] | A list of field names or properties to sort by, each suffixed by \" ASC\" or \" DESC\" (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the 'ClosedPeriod' domain to decorate onto each ClosedPeriod.              These must take the format {domain}/{scope}/{code}, for example 'ClosedPeriod/Account/id'. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_closed_periods(scope, code, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys, opts=opts)

        # [EXPERIMENTAL] ListClosedPeriods: List ClosedPeriods for a specified Timeline.
        api_response = api_instance.list_closed_periods(scope, code, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TimelinesApi->list_closed_periods: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Timeline. | 
 **code** | **str**| The code of the Timeline. | 
 **as_at** | **datetime**| The asAt datetime at which to list the ClosedPeriods. Defaults to returning the latest version of each ClosedPeriod if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing ClosedPeriods; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results.              For example, to filter on the effectiveEnd, specify \&quot;effectiveEnd gt 2019-01-15T10:00:00\&quot;. For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot; | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;ClosedPeriod&#39; domain to decorate onto each ClosedPeriod.              These must take the format {domain}/{scope}/{code}, for example &#39;ClosedPeriod/Account/id&#39;. | [optional] 

### Return type

[**PagedResourceListOfClosedPeriod**](PagedResourceListOfClosedPeriod.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested ClosedPeriods. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_timelines**
> PagedResourceListOfTimeline list_timelines(as_at=as_at, effective_at=effective_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)

[EXPERIMENTAL] ListTimelines: List Timelines

List all the Timelines matching a particular criteria.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TimelinesApi
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
    api_instance = api_client_factory.build(TimelinesApi)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the Timelines. Defaults to returning the latest version of each Timeline if not specified. (optional)
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to list the Timelines.              Note that Timelines are monotemporal, the effectiveAt is for Timevariant Properties on the Timeline only.              Defaults to the current LUSID system datetime if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing Timelines; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. (optional)
    limit = 56 # int | When paginating, limit the results to this number. Defaults to 100 if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the results.              For example, to filter on the displayName, specify \"displayName eq 'AccountingTimeline'\". For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. (optional)
    sort_by = ['sort_by_example'] # List[str] | A list of field names or properties to sort by, each suffixed by \" ASC\" or \" DESC\" (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the 'Timeline' domain to decorate onto each Timeline.              These must take the format {domain}/{scope}/{code}, for example 'Timeline/Account/id'. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_timelines(as_at=as_at, effective_at=effective_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys, opts=opts)

        # [EXPERIMENTAL] ListTimelines: List Timelines
        api_response = api_instance.list_timelines(as_at=as_at, effective_at=effective_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TimelinesApi->list_timelines: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list the Timelines. Defaults to returning the latest version of each Timeline if not specified. | [optional] 
 **effective_at** | **str**| The effective datetime or cut label at which to list the Timelines.              Note that Timelines are monotemporal, the effectiveAt is for Timevariant Properties on the Timeline only.              Defaults to the current LUSID system datetime if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing Timelines; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results.              For example, to filter on the displayName, specify \&quot;displayName eq &#39;AccountingTimeline&#39;\&quot;. For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot; | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;Timeline&#39; domain to decorate onto each Timeline.              These must take the format {domain}/{scope}/{code}, for example &#39;Timeline/Account/id&#39;. | [optional] 

### Return type

[**PagedResourceListOfTimeline**](PagedResourceListOfTimeline.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Timelines. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **set_post_close_activity**
> ClosedPeriod set_post_close_activity(scope, code, closed_period_id, post_close_activities_request=post_close_activities_request)

[EXPERIMENTAL] SetPostCloseActivity: Sets post-close activities to a Closed Period.

This sets the given post-close activities to the given Closed Period.                **This is an overwriting action!**                The possible types of entity are:  * `PortfolioTransaction`,  * `Instrument`,  * `InstrumentEvent`,  * `InstrumentEventInstruction`,  * `PortfolioSettlementInstruction`, and,  * `Quote`.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TimelinesApi
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
    api_instance = api_client_factory.build(TimelinesApi)
    scope = 'scope_example' # str | The scope of the Timeline.
    code = 'code_example' # str | The code of the Timeline.
    closed_period_id = 'closed_period_id_example' # str | The ID of the Closed Period.               This ID together with the scope and code of the Timeline uniquely defines the Closed Period.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # post_close_activities_request = PostCloseActivitiesRequest.from_json("")
    # post_close_activities_request = PostCloseActivitiesRequest.from_dict({})
    post_close_activities_request = PostCloseActivitiesRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.set_post_close_activity(scope, code, closed_period_id, post_close_activities_request=post_close_activities_request, opts=opts)

        # [EXPERIMENTAL] SetPostCloseActivity: Sets post-close activities to a Closed Period.
        api_response = api_instance.set_post_close_activity(scope, code, closed_period_id, post_close_activities_request=post_close_activities_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TimelinesApi->set_post_close_activity: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Timeline. | 
 **code** | **str**| The code of the Timeline. | 
 **closed_period_id** | **str**| The ID of the Closed Period.               This ID together with the scope and code of the Timeline uniquely defines the Closed Period. | 
 **post_close_activities_request** | [**PostCloseActivitiesRequest**](PostCloseActivitiesRequest.md)| This specifies a collection of post-close activities. | [optional] 

### Return type

[**ClosedPeriod**](ClosedPeriod.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated Closed Period. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **unconfirm_closed_period**
> ClosedPeriod unconfirm_closed_period(scope, code, closed_period_id, body=body)

[EXPERIMENTAL] UnconfirmClosedPeriod: Unconfirm the last confirmed Closed Period against a Timeline Entity

Unconfirm the last confirmed Closed Period against a Timeline Entity

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TimelinesApi
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
    api_instance = api_client_factory.build(TimelinesApi)
    scope = 'scope_example' # str | The scope of the specified Timeline.
    code = 'code_example' # str | The code of the specified Timeline. Together with the scope this uniquely identifies the Timeline.
    closed_period_id = 'closed_period_id_example' # str | The id of the Closed Period. Together with the scope and code of the Timeline,              this uniquely identifies the ClosedPeriod. The closed period must be the last closed period on the Timeline.
    body = {} # object | Not in use at the moment (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.unconfirm_closed_period(scope, code, closed_period_id, body=body, opts=opts)

        # [EXPERIMENTAL] UnconfirmClosedPeriod: Unconfirm the last confirmed Closed Period against a Timeline Entity
        api_response = api_instance.unconfirm_closed_period(scope, code, closed_period_id, body=body)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TimelinesApi->unconfirm_closed_period: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the specified Timeline. | 
 **code** | **str**| The code of the specified Timeline. Together with the scope this uniquely identifies the Timeline. | 
 **closed_period_id** | **str**| The id of the Closed Period. Together with the scope and code of the Timeline,              this uniquely identifies the ClosedPeriod. The closed period must be the last closed period on the Timeline. | 
 **body** | **object**| Not in use at the moment | [optional] 

### Return type

[**ClosedPeriod**](ClosedPeriod.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The unconfirmed closed period |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **update_timeline**
> Timeline update_timeline(scope, code, update_timeline_request=update_timeline_request)

[EXPERIMENTAL] UpdateTimeline: Update Timeline defined by scope and code

Overwrites an existing Timeline  Update request has the same required fields as Create apart from the id.  Returns the updated Timeline at the current effectiveAt.  Note that Timelines are mono-temporal, however they can have Time-Variant Properties.  Updated Properties will be returned at the latest AsAt and EffectiveAt

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TimelinesApi
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
    api_instance = api_client_factory.build(TimelinesApi)
    scope = 'scope_example' # str | The scope of the specified Timeline.
    code = 'code_example' # str | The code of the specified Timeline. Together with the domain and scope this uniquely identifies the Timeline.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # update_timeline_request = UpdateTimelineRequest.from_json("")
    # update_timeline_request = UpdateTimelineRequest.from_dict({})
    update_timeline_request = UpdateTimelineRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.update_timeline(scope, code, update_timeline_request=update_timeline_request, opts=opts)

        # [EXPERIMENTAL] UpdateTimeline: Update Timeline defined by scope and code
        api_response = api_instance.update_timeline(scope, code, update_timeline_request=update_timeline_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TimelinesApi->update_timeline: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the specified Timeline. | 
 **code** | **str**| The code of the specified Timeline. Together with the domain and scope this uniquely identifies the Timeline. | 
 **update_timeline_request** | [**UpdateTimelineRequest**](UpdateTimelineRequest.md)| The request containing the updated details of the Timeline | [optional] 

### Return type

[**Timeline**](Timeline.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated version of the requested Timeline |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

