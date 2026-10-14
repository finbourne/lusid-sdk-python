# lusid.EligibleCollateralSchedulesApi

All URIs are relative to *https://fbn-prd.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_eligible_collateral_schedule**](EligibleCollateralSchedulesApi.md#create_eligible_collateral_schedule) | **POST** /api/eligiblecollateralschedules/{scope} | [EXPERIMENTAL] CreateEligibleCollateralSchedule: Create an Eligible Collateral Schedule.
[**delete_eligible_collateral_schedule**](EligibleCollateralSchedulesApi.md#delete_eligible_collateral_schedule) | **DELETE** /api/eligiblecollateralschedules/{scope}/{code} | [EXPERIMENTAL] DeleteEligibleCollateralSchedule: Delete an Eligible Collateral Schedule.
[**get_eligible_collateral_schedule**](EligibleCollateralSchedulesApi.md#get_eligible_collateral_schedule) | **GET** /api/eligiblecollateralschedules/{scope}/{code} | [EXPERIMENTAL] GetEligibleCollateralSchedule: Get an Eligible Collateral Schedule.
[**list_eligible_collateral_schedules**](EligibleCollateralSchedulesApi.md#list_eligible_collateral_schedules) | **GET** /api/eligiblecollateralschedules | [EXPERIMENTAL] ListEligibleCollateralSchedules: List Eligible Collateral Schedules.
[**upsert_eligible_collateral_schedule**](EligibleCollateralSchedulesApi.md#upsert_eligible_collateral_schedule) | **PUT** /api/eligiblecollateralschedules/{scope}/{code} | [EXPERIMENTAL] UpsertEligibleCollateralSchedule: Upsert an Eligible Collateral Schedule.


# **create_eligible_collateral_schedule**
> EligibleCollateralSchedule create_eligible_collateral_schedule(scope, eligible_collateral_schedule_request)

[EXPERIMENTAL] CreateEligibleCollateralSchedule: Create an Eligible Collateral Schedule.

Create a new Eligible Collateral Schedule. The scope of the schedule is in the route and its code is in the request body.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    EligibleCollateralSchedulesApi
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
    api_instance = api_client_factory.build(EligibleCollateralSchedulesApi)
    scope = 'scope_example' # str | The scope of the Eligible Collateral Schedule.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # eligible_collateral_schedule_request = EligibleCollateralScheduleRequest.from_json("")
    # eligible_collateral_schedule_request = EligibleCollateralScheduleRequest.from_dict({})
    eligible_collateral_schedule_request = EligibleCollateralScheduleRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.create_eligible_collateral_schedule(scope, eligible_collateral_schedule_request, opts=opts)

        # [EXPERIMENTAL] CreateEligibleCollateralSchedule: Create an Eligible Collateral Schedule.
        api_response = api_instance.create_eligible_collateral_schedule(scope, eligible_collateral_schedule_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling EligibleCollateralSchedulesApi->create_eligible_collateral_schedule: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Eligible Collateral Schedule. | 
 **eligible_collateral_schedule_request** | [**EligibleCollateralScheduleRequest**](EligibleCollateralScheduleRequest.md)| The definition of the Eligible Collateral Schedule. | 

### Return type

[**EligibleCollateralSchedule**](EligibleCollateralSchedule.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created Eligible Collateral Schedule. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_eligible_collateral_schedule**
> DeletedEntityResponse delete_eligible_collateral_schedule(scope, code, effective_at=effective_at)

[EXPERIMENTAL] DeleteEligibleCollateralSchedule: Delete an Eligible Collateral Schedule.

Delete an Eligible Collateral Schedule from the given effective datetime. It remains retrievable at earlier effective datetimes.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    EligibleCollateralSchedulesApi
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
    api_instance = api_client_factory.build(EligibleCollateralSchedulesApi)
    scope = 'scope_example' # str | The scope of the Eligible Collateral Schedule to be deleted.
    code = 'code_example' # str | The code of the Eligible Collateral Schedule to be deleted. Together with the scope this uniquely identifies the Eligible Collateral Schedule.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label from which the Eligible Collateral Schedule is deleted. Defaults to the current LUSID system datetime if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_eligible_collateral_schedule(scope, code, effective_at=effective_at, opts=opts)

        # [EXPERIMENTAL] DeleteEligibleCollateralSchedule: Delete an Eligible Collateral Schedule.
        api_response = api_instance.delete_eligible_collateral_schedule(scope, code, effective_at=effective_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling EligibleCollateralSchedulesApi->delete_eligible_collateral_schedule: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Eligible Collateral Schedule to be deleted. | 
 **code** | **str**| The code of the Eligible Collateral Schedule to be deleted. Together with the scope this uniquely identifies the Eligible Collateral Schedule. | 
 **effective_at** | **str**| The effective datetime or cut label from which the Eligible Collateral Schedule is deleted. Defaults to the current LUSID system datetime if not specified. | [optional] 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the Eligible Collateral Schedule was deleted. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_eligible_collateral_schedule**
> EligibleCollateralSchedule get_eligible_collateral_schedule(scope, code, effective_at=effective_at, as_at=as_at, property_keys=property_keys)

[EXPERIMENTAL] GetEligibleCollateralSchedule: Get an Eligible Collateral Schedule.

Retrieve the definition of a particular Eligible Collateral Schedule at an effective and asAt datetime.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    EligibleCollateralSchedulesApi
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
    api_instance = api_client_factory.build(EligibleCollateralSchedulesApi)
    scope = 'scope_example' # str | The scope of the Eligible Collateral Schedule.
    code = 'code_example' # str | The code of the Eligible Collateral Schedule. Together with the scope this uniquely identifies the Eligible Collateral Schedule.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve the Eligible Collateral Schedule. Defaults to the current LUSID system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Eligible Collateral Schedule. Defaults to returning the latest version if not specified. (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the 'EligibleCollateralSchedule' domain to decorate onto the Eligible Collateral Schedule.              These must take the format {domain}/{scope}/{code}, for example 'EligibleCollateralSchedule/Manager/Id'. If no properties are specified, then no properties will be returned. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_eligible_collateral_schedule(scope, code, effective_at=effective_at, as_at=as_at, property_keys=property_keys, opts=opts)

        # [EXPERIMENTAL] GetEligibleCollateralSchedule: Get an Eligible Collateral Schedule.
        api_response = api_instance.get_eligible_collateral_schedule(scope, code, effective_at=effective_at, as_at=as_at, property_keys=property_keys)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling EligibleCollateralSchedulesApi->get_eligible_collateral_schedule: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Eligible Collateral Schedule. | 
 **code** | **str**| The code of the Eligible Collateral Schedule. Together with the scope this uniquely identifies the Eligible Collateral Schedule. | 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the Eligible Collateral Schedule. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Eligible Collateral Schedule. Defaults to returning the latest version if not specified. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;EligibleCollateralSchedule&#39; domain to decorate onto the Eligible Collateral Schedule.              These must take the format {domain}/{scope}/{code}, for example &#39;EligibleCollateralSchedule/Manager/Id&#39;. If no properties are specified, then no properties will be returned. | [optional] 

### Return type

[**EligibleCollateralSchedule**](EligibleCollateralSchedule.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Eligible Collateral Schedule. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_eligible_collateral_schedules**
> PagedResourceListOfEligibleCollateralSchedule list_eligible_collateral_schedules(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)

[EXPERIMENTAL] ListEligibleCollateralSchedules: List Eligible Collateral Schedules.

List all the Eligible Collateral Schedules matching the given criteria.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    EligibleCollateralSchedulesApi
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
    api_instance = api_client_factory.build(EligibleCollateralSchedulesApi)
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to list the Eligible Collateral Schedules. Defaults to the current LUSID system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list Eligible Collateral Schedules. Defaults to returning the latest version of each Eligible Collateral Schedule if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing Eligible Collateral Schedules; this value is returned from the previous call. If a pagination token is provided, the filter and asAt fields must not have changed since the original request. (optional)
    limit = 56 # int | When paginating, limit the results to this number. Defaults to 100 if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the results. The filterable fields are Id.Scope, Id.Code, Description, Properties and Version. The rows can be filtered with a single-condition any expression on Rows over Code, Description, Selector.Kind, Selector.Currency, Selector.InstrumentFilter, ValuationPercentage, FxHaircut, MinResidualMaturityYears or MaxResidualMaturityYears. For example, to filter on the schedule code, specify \"Id.Code eq 'UsdCashAndGovies'\", and to find schedules with a row for a given asset kind, specify \"Rows any (Selector.Kind eq 'Cash')\". For more information about filtering results, see https://support.lusid.com/docs/filtering-information-retrieved-from-lusid. (optional)
    sort_by = ['sort_by_example'] # List[str] | A list of field names to sort by, each suffixed by \" ASC\" or \" DESC\". (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the 'EligibleCollateralSchedule' domain to decorate onto each Eligible Collateral Schedule.              These must take the format {domain}/{scope}/{code}, for example 'EligibleCollateralSchedule/Manager/Id'. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_eligible_collateral_schedules(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys, opts=opts)

        # [EXPERIMENTAL] ListEligibleCollateralSchedules: List Eligible Collateral Schedules.
        api_response = api_instance.list_eligible_collateral_schedules(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling EligibleCollateralSchedulesApi->list_eligible_collateral_schedules: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **effective_at** | **str**| The effective datetime or cut label at which to list the Eligible Collateral Schedules. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list Eligible Collateral Schedules. Defaults to returning the latest version of each Eligible Collateral Schedule if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing Eligible Collateral Schedules; this value is returned from the previous call. If a pagination token is provided, the filter and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results. The filterable fields are Id.Scope, Id.Code, Description, Properties and Version. The rows can be filtered with a single-condition any expression on Rows over Code, Description, Selector.Kind, Selector.Currency, Selector.InstrumentFilter, ValuationPercentage, FxHaircut, MinResidualMaturityYears or MaxResidualMaturityYears. For example, to filter on the schedule code, specify \&quot;Id.Code eq &#39;UsdCashAndGovies&#39;\&quot;, and to find schedules with a row for a given asset kind, specify \&quot;Rows any (Selector.Kind eq &#39;Cash&#39;)\&quot;. For more information about filtering results, see https://support.lusid.com/docs/filtering-information-retrieved-from-lusid. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;EligibleCollateralSchedule&#39; domain to decorate onto each Eligible Collateral Schedule.              These must take the format {domain}/{scope}/{code}, for example &#39;EligibleCollateralSchedule/Manager/Id&#39;. | [optional] 

### Return type

[**PagedResourceListOfEligibleCollateralSchedule**](PagedResourceListOfEligibleCollateralSchedule.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Eligible Collateral Schedules. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **upsert_eligible_collateral_schedule**
> EligibleCollateralSchedule upsert_eligible_collateral_schedule(scope, code, upsert_eligible_collateral_schedule_request)

[EXPERIMENTAL] UpsertEligibleCollateralSchedule: Upsert an Eligible Collateral Schedule.

Create or replace the full definition of an Eligible Collateral Schedule from an effective datetime. A change to the  definition becomes a new bitemporal version: the schedule as it was declared at earlier effective datetimes,  and as of earlier asAt datetimes, remains retrievable.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    EligibleCollateralSchedulesApi
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
    api_instance = api_client_factory.build(EligibleCollateralSchedulesApi)
    scope = 'scope_example' # str | The scope of the Eligible Collateral Schedule.
    code = 'code_example' # str | The code of the Eligible Collateral Schedule. Together with the scope this uniquely identifies the Eligible Collateral Schedule.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # upsert_eligible_collateral_schedule_request = UpsertEligibleCollateralScheduleRequest.from_json("")
    # upsert_eligible_collateral_schedule_request = UpsertEligibleCollateralScheduleRequest.from_dict({})
    upsert_eligible_collateral_schedule_request = UpsertEligibleCollateralScheduleRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.upsert_eligible_collateral_schedule(scope, code, upsert_eligible_collateral_schedule_request, opts=opts)

        # [EXPERIMENTAL] UpsertEligibleCollateralSchedule: Upsert an Eligible Collateral Schedule.
        api_response = api_instance.upsert_eligible_collateral_schedule(scope, code, upsert_eligible_collateral_schedule_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling EligibleCollateralSchedulesApi->upsert_eligible_collateral_schedule: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Eligible Collateral Schedule. | 
 **code** | **str**| The code of the Eligible Collateral Schedule. Together with the scope this uniquely identifies the Eligible Collateral Schedule. | 
 **upsert_eligible_collateral_schedule_request** | [**UpsertEligibleCollateralScheduleRequest**](UpsertEligibleCollateralScheduleRequest.md)| The full definition of the Eligible Collateral Schedule from the effective datetime in the request, or the current LUSID system datetime if not specified. | 

### Return type

[**EligibleCollateralSchedule**](EligibleCollateralSchedule.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Eligible Collateral Schedule as it stands from the effective datetime. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

