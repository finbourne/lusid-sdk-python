# lusid.TimelinesApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_closed_period**](TimelinesApi.md#create_closed_period) | **POST** /api/timelines/{scope}/{code}/closedperiods | [EXPERIMENTAL] CreateClosedPeriod: Create a new closed period against a timeline entity
[**create_timeline**](TimelinesApi.md#create_timeline) | **POST** /api/timelines | [EXPERIMENTAL] CreateTimeline: Create a Timeline
[**delete_timeline**](TimelinesApi.md#delete_timeline) | **DELETE** /api/timelines/{scope}/{code} | [EXPERIMENTAL] DeleteTimeline: Deletes a particular Timeline
[**get_closed_period**](TimelinesApi.md#get_closed_period) | **GET** /api/timelines/{scope}/{code}/closedperiods/{closedPeriodId} | [EXPERIMENTAL] GetClosedPeriod: Gets a Closed Period entity.
[**get_timeline**](TimelinesApi.md#get_timeline) | **GET** /api/timelines/{scope}/{code} | [EXPERIMENTAL] GetTimeline: Get a single Timeline by scope and code.
[**update_timeline**](TimelinesApi.md#update_timeline) | **PUT** /api/timelines/{scope}/{code} | [EXPERIMENTAL] UpdateTimeline: Update Timeline defined by scope and code


# **create_closed_period**
> ClosedPeriod create_closed_period(scope, code, create_closed_period_request=create_closed_period_request)

[EXPERIMENTAL] CreateClosedPeriod: Create a new closed period against a timeline entity

Creates a new closed period against a timeline entity  Returns the newly created closed period entity with properties

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    TimelinesApi
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
            # api_response = await api_instance.create_closed_period(scope, code, create_closed_period_request=create_closed_period_request, opts=opts)

            # [EXPERIMENTAL] CreateClosedPeriod: Create a new closed period against a timeline entity
            api_response = await api_instance.create_closed_period(scope, code, create_closed_period_request=create_closed_period_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling TimelinesApi->create_closed_period: %s\n" % e)

asyncio.run(main())
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

# **create_timeline**
> Timeline create_timeline(create_timeline_request=create_timeline_request)

[EXPERIMENTAL] CreateTimeline: Create a Timeline

Creates a Timeline. Returns the created Timeline at the current effectiveAt.  Note that Timelines are mono-temporal, however they can have Time-Variant Properties.  Upserted Properties will be returned at the latest AsAt and EffectiveAt

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    TimelinesApi
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
        api_instance = api_client_factory.build(TimelinesApi)

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # create_timeline_request = CreateTimelineRequest.from_json("")
        # create_timeline_request = CreateTimelineRequest.from_dict({})
        create_timeline_request = CreateTimelineRequest()

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.create_timeline(create_timeline_request=create_timeline_request, opts=opts)

            # [EXPERIMENTAL] CreateTimeline: Create a Timeline
            api_response = await api_instance.create_timeline(create_timeline_request=create_timeline_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling TimelinesApi->create_timeline: %s\n" % e)

asyncio.run(main())
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
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    TimelinesApi
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
        api_instance = api_client_factory.build(TimelinesApi)
        scope = 'scope_example' # str | The scope of the specified Timeline.
        code = 'code_example' # str | The code of the specified Timeline. Together with the domain and scope this uniquely              identifies the Timeline.

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.delete_timeline(scope, code, opts=opts)

            # [EXPERIMENTAL] DeleteTimeline: Deletes a particular Timeline
            api_response = await api_instance.delete_timeline(scope, code)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling TimelinesApi->delete_timeline: %s\n" % e)

asyncio.run(main())
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
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    TimelinesApi
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
        api_instance = api_client_factory.build(TimelinesApi)
        scope = 'scope_example' # str | The scope of the Timeline.
        code = 'code_example' # str | The code of the Timeline. Together with the scope this uniquely              identifies the Timeline.
        closed_period_id = 'closed_period_id_example' # str | The id of the Closed Period. Together with the scope and code of the Timeline,              this uniquely identifies the ClosedPeriod
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the ClosedPeriod definition. Defaults to return              the latest version of the definition if not specified. (optional)
        property_keys = ['property_keys_example'] # List[str] | A list of property keys from the 'ClosedPeriod' domain to decorate onto              the ClosedPeriod.              These must have the format {domain}/{scope}/{code}, for example 'ClosedPeriod/system/Name'. (optional)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.get_closed_period(scope, code, closed_period_id, as_at=as_at, property_keys=property_keys, opts=opts)

            # [EXPERIMENTAL] GetClosedPeriod: Gets a Closed Period entity.
            api_response = await api_instance.get_closed_period(scope, code, closed_period_id, as_at=as_at, property_keys=property_keys)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling TimelinesApi->get_closed_period: %s\n" % e)

asyncio.run(main())
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
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    TimelinesApi
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
        api_instance = api_client_factory.build(TimelinesApi)
        scope = 'scope_example' # str | The scope of the specified Timeline.
        code = 'code_example' # str | The code of the specified Timeline. Together with the scope this uniquely              identifies the Timeline.
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Timeline definition. Defaults to return              the latest version of the definition if not specified. (optional)
        effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve the timeline properties.              Defaults to the current LUSID system datetime if not specified. (optional)
        property_keys = ['property_keys_example'] # List[str] | A list of property keys from the 'Timeline' domain to decorate onto              the Timeline.              These must have the format {domain}/{scope}/{code}, for example 'Timeline/system/Name'. (optional)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.get_timeline(scope, code, as_at=as_at, effective_at=effective_at, property_keys=property_keys, opts=opts)

            # [EXPERIMENTAL] GetTimeline: Get a single Timeline by scope and code.
            api_response = await api_instance.get_timeline(scope, code, as_at=as_at, effective_at=effective_at, property_keys=property_keys)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling TimelinesApi->get_timeline: %s\n" % e)

asyncio.run(main())
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

# **update_timeline**
> Timeline update_timeline(scope, code, update_timeline_request=update_timeline_request)

[EXPERIMENTAL] UpdateTimeline: Update Timeline defined by scope and code

Overwrites an existing Timeline  Update request has the same required fields as Create apart from the Id.  Returns the updated Timeline at the current effectiveAt.  Note that Timelines are mono-temporal, however they can have Time-Variant Properties.  Updated Properties will be returned at the latest AsAt and EffectiveAt

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    TimelinesApi
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
            # api_response = await api_instance.update_timeline(scope, code, update_timeline_request=update_timeline_request, opts=opts)

            # [EXPERIMENTAL] UpdateTimeline: Update Timeline defined by scope and code
            api_response = await api_instance.update_timeline(scope, code, update_timeline_request=update_timeline_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling TimelinesApi->update_timeline: %s\n" % e)

asyncio.run(main())
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

