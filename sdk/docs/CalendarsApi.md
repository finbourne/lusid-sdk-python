# lusid.CalendarsApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_business_days_to_date**](CalendarsApi.md#add_business_days_to_date) | **POST** /api/calendars/businessday/{scope}/add | [EARLY ACCESS] AddBusinessDaysToDate: Adds the requested number of Business Days to the provided date.
[**add_date_to_calendar**](CalendarsApi.md#add_date_to_calendar) | **PUT** /api/calendars/generic/{scope}/{code}/dates | AddDateToCalendar: Add a date to a calendar
[**batch_upsert_dates_for_calendar**](CalendarsApi.md#batch_upsert_dates_for_calendar) | **POST** /api/calendars/generic/{scope}/{code}/dates/$batchUpsert | BatchUpsertDatesForCalendar: Batch upsert dates to a calendar
[**create_calendar**](CalendarsApi.md#create_calendar) | **POST** /api/calendars/generic | [EARLY ACCESS] CreateCalendar: Create a calendar in its generic form
[**delete_calendar**](CalendarsApi.md#delete_calendar) | **DELETE** /api/calendars/generic/{scope}/{code} | [EARLY ACCESS] DeleteCalendar: Delete a calendar
[**delete_date_from_calendar**](CalendarsApi.md#delete_date_from_calendar) | **DELETE** /api/calendars/generic/{scope}/{code}/dates/{dateId} | DeleteDateFromCalendar: Remove a date from a calendar
[**delete_dates_from_calendar**](CalendarsApi.md#delete_dates_from_calendar) | **POST** /api/calendars/generic/{scope}/{code}/dates/$delete | DeleteDatesFromCalendar: Delete dates from a calendar
[**generate_schedule**](CalendarsApi.md#generate_schedule) | **POST** /api/calendars/schedule/{scope} | [EARLY ACCESS] GenerateSchedule: Generate an ordered schedule of dates.
[**get_calendar**](CalendarsApi.md#get_calendar) | **GET** /api/calendars/generic/{scope}/{code} | GetCalendar: Get a calendar in its generic form
[**get_dates**](CalendarsApi.md#get_dates) | **GET** /api/calendars/generic/{scope}/{code}/dates | [EARLY ACCESS] GetDates: Get dates for a specific calendar
[**is_business_date_time**](CalendarsApi.md#is_business_date_time) | **GET** /api/calendars/businessday/{scope}/{code} | [EARLY ACCESS] IsBusinessDateTime: Check whether a DateTime is a \&quot;Business DateTime\&quot;
[**list_calendars**](CalendarsApi.md#list_calendars) | **GET** /api/calendars/generic | [EARLY ACCESS] ListCalendars: List Calendars
[**list_calendars_in_scope**](CalendarsApi.md#list_calendars_in_scope) | **GET** /api/calendars/generic/{scope} | ListCalendarsInScope: List all calenders in a specified scope
[**update_calendar**](CalendarsApi.md#update_calendar) | **POST** /api/calendars/generic/{scope}/{code} | [EARLY ACCESS] UpdateCalendar: Update a calendar


# **add_business_days_to_date**
> AddBusinessDaysToDateResponse add_business_days_to_date(scope, add_business_days_to_date_request)

[EARLY ACCESS] AddBusinessDaysToDate: Adds the requested number of Business Days to the provided date.

A Business day is defined as a point in time that:      * Does not represent a day in the calendar's weekend      * Does not represent a day in the calendar's list of holidays (e.g. Christmas Day in the UK)                 All dates specified must be UTC and the upper bound of a calendar is not inclusive                 e.g. From: 2020-12-24-00-00-00:       Adding 3 business days returns 2020-12-30, assuming Saturday and Sunday are weekends, and the 25th and 28th are holidays.       Adding -2 business days returns 2020-12-22 under the same assumptions.                If the provided number of days to add is zero, returns a failure.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    CalendarsApi
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
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(CalendarsApi)
        scope = 'scope_example' # str | Scope within which to search for the calendars

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # add_business_days_to_date_request = AddBusinessDaysToDateRequest()
        # add_business_days_to_date_request = AddBusinessDaysToDateRequest.from_json("")
        add_business_days_to_date_request = AddBusinessDaysToDateRequest.from_dict({"businessDayOffset":5,"holidayCodes":["GBP"],"startDate":"2020-02-10T00:00:00.0000000+00:00"}) # AddBusinessDaysToDateRequest | Request Details: start date, number of days to add (which can be negative, but not zero), calendar codes and optionally an AsAt date for searching the calendar store

        try:
            # [EARLY ACCESS] AddBusinessDaysToDate: Adds the requested number of Business Days to the provided date.
            api_response = await api_instance.add_business_days_to_date(scope, add_business_days_to_date_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CalendarsApi->add_business_days_to_date: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Scope within which to search for the calendars | 
 **add_business_days_to_date_request** | [**AddBusinessDaysToDateRequest**](AddBusinessDaysToDateRequest.md)| Request Details: start date, number of days to add (which can be negative, but not zero), calendar codes and optionally an AsAt date for searching the calendar store | 

### Return type

[**AddBusinessDaysToDateResponse**](AddBusinessDaysToDateResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The business day that is a number of business days after the given date as determined by the given calendar codes |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **add_date_to_calendar**
> CalendarDate add_date_to_calendar(scope, code, create_date_request)

AddDateToCalendar: Add a date to a calendar

Add an event to the calendar. These Events can be a maximum of 24 hours and must be specified in UTC.  A local date will be calculated by the system and applied to the calendar before processing.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    CalendarsApi
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
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(CalendarsApi)
        scope = 'scope_example' # str | Scope of the calendar
        code = 'code_example' # str | Code of the calendar

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # create_date_request = CreateDateRequest()
        # create_date_request = CreateDateRequest.from_json("")
        create_date_request = CreateDateRequest.from_dict({"dateId":"TestDate","fromUtc":"2020-01-25T00:00:00.0000000+00:00","toUtc":"2020-01-26T00:00:00.0000000+00:00","timeZone":"CET","description":"Chinese New year","type":"Holiday","sourceData":{}}) # CreateDateRequest | Add date to calendar request

        try:
            # AddDateToCalendar: Add a date to a calendar
            api_response = await api_instance.add_date_to_calendar(scope, code, create_date_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CalendarsApi->add_date_to_calendar: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Scope of the calendar | 
 **code** | **str**| Code of the calendar | 
 **create_date_request** | [**CreateDateRequest**](CreateDateRequest.md)| Add date to calendar request | 

### Return type

[**CalendarDate**](CalendarDate.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The created date |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **batch_upsert_dates_for_calendar**
> BatchUpsertDatesForCalendarResponse batch_upsert_dates_for_calendar(scope, code, success_mode, request_body)

BatchUpsertDatesForCalendar: Batch upsert dates to a calendar

Create or update events in the calendar. These Events can be a maximum of 24 hours and must be specified in UTC.  A local date will be calculated by the system and applied to the calendar before processing.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    CalendarsApi
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
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(CalendarsApi)
        scope = 'scope_example' # str | Scope of the calendar
        code = 'code_example' # str | Code of the calendar
        success_mode = 'Partial' # str | Whether the batch request should fail Atomically or in a Partial fashion - Allowed Values: Atomic, Partial. (default to 'Partial')
        request_body = {"ChineseNewYear":{"dateId":"TestDate","fromUtc":"2020-01-25T00:00:00.0000000+00:00","toUtc":"2020-01-26T00:00:00.0000000+00:00","timeZone":"CET","description":"Chinese New Year","type":"Holiday","sourceData":{}}} # Dict[str, CreateDateRequest] | Create Date Requests of dates to upsert

        try:
            # BatchUpsertDatesForCalendar: Batch upsert dates to a calendar
            api_response = await api_instance.batch_upsert_dates_for_calendar(scope, code, success_mode, request_body)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CalendarsApi->batch_upsert_dates_for_calendar: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Scope of the calendar | 
 **code** | **str**| Code of the calendar | 
 **success_mode** | **str**| Whether the batch request should fail Atomically or in a Partial fashion - Allowed Values: Atomic, Partial. | [default to &#39;Partial&#39;]
 **request_body** | [**Dict[str, CreateDateRequest]**](CreateDateRequest.md)| Create Date Requests of dates to upsert | 

### Return type

[**BatchUpsertDatesForCalendarResponse**](BatchUpsertDatesForCalendarResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully upserted date requests along with any failures |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **create_calendar**
> Calendar create_calendar(create_calendar_request)

[EARLY ACCESS] CreateCalendar: Create a calendar in its generic form

Create a calendar in a generic form which can be used to store date events.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    CalendarsApi
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
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(CalendarsApi)

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # create_calendar_request = CreateCalendarRequest()
        # create_calendar_request = CreateCalendarRequest.from_json("")
        create_calendar_request = CreateCalendarRequest.from_dict({"calendarId":{"scope":"TestScope","code":"TestCode"},"calendarType":"Holiday","weekendMask":{"days":["Saturday","Sunday"],"timeZone":"UTC"},"sourceProvider":"Finbourne-Calendar-Service","properties":[{"key":"Calendar/HolidayType/Statutory","value":{"labelValue":"CBTR"}}]}) # CreateCalendarRequest | A request to create the calendar

        try:
            # [EARLY ACCESS] CreateCalendar: Create a calendar in its generic form
            api_response = await api_instance.create_calendar(create_calendar_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CalendarsApi->create_calendar: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_calendar_request** | [**CreateCalendarRequest**](CreateCalendarRequest.md)| A request to create the calendar | 

### Return type

[**Calendar**](Calendar.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The created calendar |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_calendar**
> Calendar delete_calendar(scope, code)

[EARLY ACCESS] DeleteCalendar: Delete a calendar

Delete a calendar and all of its respective dates

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    CalendarsApi
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
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(CalendarsApi)
        scope = 'scope_example' # str | Scope of the calendar
        code = 'code_example' # str | Code of the calendar

        try:
            # [EARLY ACCESS] DeleteCalendar: Delete a calendar
            api_response = await api_instance.delete_calendar(scope, code)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CalendarsApi->delete_calendar: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Scope of the calendar | 
 **code** | **str**| Code of the calendar | 

### Return type

[**Calendar**](Calendar.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The deleted calendar |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_date_from_calendar**
> CalendarDate delete_date_from_calendar(scope, code, date_id)

DeleteDateFromCalendar: Remove a date from a calendar

Remove a date from a calendar.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    CalendarsApi
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
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(CalendarsApi)
        scope = 'scope_example' # str | Scope of the calendar
        code = 'code_example' # str | Code of the calendar
        date_id = 'date_id_example' # str | Identifier of the date to be removed

        try:
            # DeleteDateFromCalendar: Remove a date from a calendar
            api_response = await api_instance.delete_date_from_calendar(scope, code, date_id)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CalendarsApi->delete_date_from_calendar: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Scope of the calendar | 
 **code** | **str**| Code of the calendar | 
 **date_id** | **str**| Identifier of the date to be removed | 

### Return type

[**CalendarDate**](CalendarDate.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The deleted date |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_dates_from_calendar**
> Dict[str, CalendarDate] delete_dates_from_calendar(scope, code, request_body)

DeleteDatesFromCalendar: Delete dates from a calendar

Delete dates from a calendar.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    CalendarsApi
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
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(CalendarsApi)
        scope = 'scope_example' # str | Scope of the calendar
        code = 'code_example' # str | Code of the calendar
        request_body = ["dateId1","dateId2"] # List[str] | Identifiers of the dates to be removed

        try:
            # DeleteDatesFromCalendar: Delete dates from a calendar
            api_response = await api_instance.delete_dates_from_calendar(scope, code, request_body)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CalendarsApi->delete_dates_from_calendar: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Scope of the calendar | 
 **code** | **str**| Code of the calendar | 
 **request_body** | [**List[str]**](str.md)| Identifiers of the dates to be removed | 

### Return type

[**Dict[str, CalendarDate]**](CalendarDate.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The dateIds and details of the dates that were deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **generate_schedule**
> List[datetime] generate_schedule(scope, valuation_schedule, as_at=as_at)

[EARLY ACCESS] GenerateSchedule: Generate an ordered schedule of dates.

Returns an ordered array of dates. The dates will only fall on business  days as defined by the scope and calendar codes in the valuation schedule.                Valuations are made at a frequency defined by the valuation schedule's tenor, e.g. every day (\"1D\"),  every other week (\"2W\") etc. These dates will be adjusted onto business days as defined by the schedule's  rollConvention.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    CalendarsApi
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
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(CalendarsApi)
        scope = 'scope_example' # str | Scope of the calendars to use

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # valuation_schedule = ValuationSchedule()
        # valuation_schedule = ValuationSchedule.from_json("")
        valuation_schedule = ValuationSchedule.from_dict({"effectiveFrom":"2020-01-01","effectiveAt":"2021-01-01","tenor":"1M","rollConvention":"None","holidayCalendars":["GBP","USD"],"valuationDateTimes":[],"businessDayConvention":"F"}) # ValuationSchedule | The ValuationSchedule to generate schedule dates from
        as_at = '2013-10-20T19:20:30+01:00' # datetime | Optional AsAt for searching the calendar store. Defaults to Latest. (optional)

        try:
            # [EARLY ACCESS] GenerateSchedule: Generate an ordered schedule of dates.
            api_response = await api_instance.generate_schedule(scope, valuation_schedule, as_at=as_at)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CalendarsApi->generate_schedule: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Scope of the calendars to use | 
 **valuation_schedule** | [**ValuationSchedule**](ValuationSchedule.md)| The ValuationSchedule to generate schedule dates from | 
 **as_at** | **datetime**| Optional AsAt for searching the calendar store. Defaults to Latest. | [optional] 

### Return type

**List[datetime]**

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of dates in chronological order. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_calendar**
> Calendar get_calendar(scope, code, property_keys=property_keys, as_at=as_at)

GetCalendar: Get a calendar in its generic form

Retrieve a generic calendar by a specific ID at a point in AsAt time

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    CalendarsApi
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
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(CalendarsApi)
        scope = 'scope_example' # str | Scope of the calendar identifier
        code = 'code_example' # str | Code of the calendar identifier
        property_keys = ['property_keys_example'] # List[str] | A list of property keys from the \"Calendar\" domain to decorate onto the calendar,               These take the format {domain}/{scope}/{code} e.g. \"Calendar/System/Name\". (optional)
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The AsAt datetime at which to retrieve the calendar (optional)

        try:
            # GetCalendar: Get a calendar in its generic form
            api_response = await api_instance.get_calendar(scope, code, property_keys=property_keys, as_at=as_at)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CalendarsApi->get_calendar: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Scope of the calendar identifier | 
 **code** | **str**| Code of the calendar identifier | 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the \&quot;Calendar\&quot; domain to decorate onto the calendar,               These take the format {domain}/{scope}/{code} e.g. \&quot;Calendar/System/Name\&quot;. | [optional] 
 **as_at** | **datetime**| The AsAt datetime at which to retrieve the calendar | [optional] 

### Return type

[**Calendar**](Calendar.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested calendar |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_dates**
> ResourceListOfCalendarDate get_dates(scope, code, from_effective_at=from_effective_at, to_effective_at=to_effective_at, as_at=as_at, id_filter=id_filter)

[EARLY ACCESS] GetDates: Get dates for a specific calendar

Get dates from a specific calendar within a specific window of effective time, at a point in AsAt time.  Providing an id filter can further refine the results.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    CalendarsApi
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
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(CalendarsApi)
        scope = 'scope_example' # str | Scope of the calendar
        code = 'code_example' # str | Code of the calendar
        from_effective_at = 'from_effective_at_example' # str | Where the effective window of dates should begin from (optional)
        to_effective_at = 'to_effective_at_example' # str | Where the effective window of dates should end (optional)
        as_at = '2013-10-20T19:20:30+01:00' # datetime | AsAt the dates should be retrieved at (optional)
        id_filter = ['id_filter_example'] # List[str] | An additional filter that will filter dates based on their identifer (optional)

        try:
            # [EARLY ACCESS] GetDates: Get dates for a specific calendar
            api_response = await api_instance.get_dates(scope, code, from_effective_at=from_effective_at, to_effective_at=to_effective_at, as_at=as_at, id_filter=id_filter)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CalendarsApi->get_dates: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Scope of the calendar | 
 **code** | **str**| Code of the calendar | 
 **from_effective_at** | **str**| Where the effective window of dates should begin from | [optional] 
 **to_effective_at** | **str**| Where the effective window of dates should end | [optional] 
 **as_at** | **datetime**| AsAt the dates should be retrieved at | [optional] 
 **id_filter** | [**List[str]**](str.md)| An additional filter that will filter dates based on their identifer | [optional] 

### Return type

[**ResourceListOfCalendarDate**](ResourceListOfCalendarDate.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested date |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **is_business_date_time**
> IsBusinessDayResponse is_business_date_time(date_time, scope, code, as_at=as_at)

[EARLY ACCESS] IsBusinessDateTime: Check whether a DateTime is a \"Business DateTime\"

A Business DateTime is defined as a point in time that:      * Does not represent a day that overlaps with the calendars WeekendMask      * If the calendar is a \"Holiday Calendar\" Does not overlap with any dates in the calendar      * If the calendar is a \"TradingHours Calendar\" Does overlap with a date in the calendar                All dates specified must be UTC and the upper bound of a calendar is not inclusive   e.g. From: 2020-12-25-00-00-00        To: 2020-12-26-00-00-00  IsBusinessDay(2020-12-26-00-00-00) == false

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    CalendarsApi
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
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(CalendarsApi)
        date_time = '2013-10-20T19:20:30+01:00' # datetime | DateTime to check - This DateTime must be UTC
        scope = 'scope_example' # str | Scope of the calendar
        code = 'code_example' # str | Code of the calendar
        as_at = '2013-10-20T19:20:30+01:00' # datetime | AsAt for the request (optional)

        try:
            # [EARLY ACCESS] IsBusinessDateTime: Check whether a DateTime is a \"Business DateTime\"
            api_response = await api_instance.is_business_date_time(date_time, scope, code, as_at=as_at)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CalendarsApi->is_business_date_time: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **date_time** | **datetime**| DateTime to check - This DateTime must be UTC | 
 **scope** | **str**| Scope of the calendar | 
 **code** | **str**| Code of the calendar | 
 **as_at** | **datetime**| AsAt for the request | [optional] 

### Return type

[**IsBusinessDayResponse**](IsBusinessDayResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Whether or not the requested DateTime is a BusinessDay or not |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_calendars**
> PagedResourceListOfCalendar list_calendars(as_at=as_at, page=page, limit=limit, property_keys=property_keys, filter=filter)

[EARLY ACCESS] ListCalendars: List Calendars

List calendars at a point in AsAt time.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    CalendarsApi
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
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(CalendarsApi)
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The AsAt datetime at which to retrieve the calendars (optional)
        page = 'page_example' # str | The pagination token to use to continue listing calendars from a previous call to list calendars.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, and asAt fields              must not have changed since the original request. (optional)
        limit = 56 # int | When paginating, limit the number of returned results to this many. (optional)
        property_keys = ['property_keys_example'] # List[str] | A list of property keys from the \"Calendar\" domain to decorate onto the calendar,               These take the format {domain}/{scope}/{code} e.g. \"Calendar/System/Name\". (optional)
        filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)

        try:
            # [EARLY ACCESS] ListCalendars: List Calendars
            api_response = await api_instance.list_calendars(as_at=as_at, page=page, limit=limit, property_keys=property_keys, filter=filter)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CalendarsApi->list_calendars: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The AsAt datetime at which to retrieve the calendars | [optional] 
 **page** | **str**| The pagination token to use to continue listing calendars from a previous call to list calendars.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, and asAt fields              must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the \&quot;Calendar\&quot; domain to decorate onto the calendar,               These take the format {domain}/{scope}/{code} e.g. \&quot;Calendar/System/Name\&quot;. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 

### Return type

[**PagedResourceListOfCalendar**](PagedResourceListOfCalendar.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List Calendars |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_calendars_in_scope**
> PagedResourceListOfCalendar list_calendars_in_scope(scope, as_at=as_at, page=page, limit=limit, property_keys=property_keys, filter=filter)

ListCalendarsInScope: List all calenders in a specified scope

List calendars in a Scope at a point in AsAt time.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    CalendarsApi
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
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(CalendarsApi)
        scope = 'scope_example' # str | Scope of the calendars
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The AsAt datetime at which to retrieve the calendars (optional)
        page = 'page_example' # str | The pagination token to use to continue listing calendars from a previous call to list calendars.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, and asAt fields              must not have changed since the original request. (optional)
        limit = 56 # int | When paginating, limit the number of returned results to this many. (optional)
        property_keys = ['property_keys_example'] # List[str] | A list of property keys from the \"Calendar\" domain to decorate onto the calendar,               These take the format {domain}/{scope}/{code} e.g. \"Calendar/System/Name\". (optional)
        filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)

        try:
            # ListCalendarsInScope: List all calenders in a specified scope
            api_response = await api_instance.list_calendars_in_scope(scope, as_at=as_at, page=page, limit=limit, property_keys=property_keys, filter=filter)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CalendarsApi->list_calendars_in_scope: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Scope of the calendars | 
 **as_at** | **datetime**| The AsAt datetime at which to retrieve the calendars | [optional] 
 **page** | **str**| The pagination token to use to continue listing calendars from a previous call to list calendars.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, and asAt fields              must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the \&quot;Calendar\&quot; domain to decorate onto the calendar,               These take the format {domain}/{scope}/{code} e.g. \&quot;Calendar/System/Name\&quot;. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 

### Return type

[**PagedResourceListOfCalendar**](PagedResourceListOfCalendar.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Calendars in the requested scope |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **update_calendar**
> Calendar update_calendar(scope, code, update_calendar_request)

[EARLY ACCESS] UpdateCalendar: Update a calendar

Update the calendars WeekendMask, SourceProvider or Properties

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    CalendarsApi
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
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(CalendarsApi)
        scope = 'scope_example' # str | Scope of the request
        code = 'code_example' # str | Code of the request

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # update_calendar_request = UpdateCalendarRequest()
        # update_calendar_request = UpdateCalendarRequest.from_json("")
        update_calendar_request = UpdateCalendarRequest.from_dict({"weekendMask":{"days":["Saturday","Sunday"],"timeZone":"UTC"},"sourceProvider":"Finbourne-Calendar-Service","properties":[{"key":"Calendar/HolidayType/Statutory","value":{"labelValue":"CBTR"}}]}) # UpdateCalendarRequest | The new state of the calendar

        try:
            # [EARLY ACCESS] UpdateCalendar: Update a calendar
            api_response = await api_instance.update_calendar(scope, code, update_calendar_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CalendarsApi->update_calendar: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Scope of the request | 
 **code** | **str**| Code of the request | 
 **update_calendar_request** | [**UpdateCalendarRequest**](UpdateCalendarRequest.md)| The new state of the calendar | 

### Return type

[**Calendar**](Calendar.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated calendar |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

