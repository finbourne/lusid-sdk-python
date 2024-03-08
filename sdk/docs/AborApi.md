# lusid.AborApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_diary_entry**](AborApi.md#add_diary_entry) | **POST** /api/abor/{scope}/{code}/accountingdiary/{diaryEntryCode} | [EXPERIMENTAL] AddDiaryEntry: Add a diary entry to the specified Abor.
[**close_period**](AborApi.md#close_period) | **POST** /api/abor/{scope}/{code}/accountingdiary/$closeperiod | [EXPERIMENTAL] ClosePeriod: Closes or locks the current period for the given Abor.
[**create_abor**](AborApi.md#create_abor) | **POST** /api/abor/{scope} | [EXPERIMENTAL] CreateAbor: Create an Abor.
[**delete_abor**](AborApi.md#delete_abor) | **DELETE** /api/abor/{scope}/{code} | [EXPERIMENTAL] DeleteAbor: Delete an Abor.
[**get_abor**](AborApi.md#get_abor) | **GET** /api/abor/{scope}/{code} | [EXPERIMENTAL] GetAbor: Get Abor.
[**get_journal_entry_lines**](AborApi.md#get_journal_entry_lines) | **POST** /api/abor/{scope}/{code}/journalentrylines/$query | [EXPERIMENTAL] GetJournalEntryLines: Get the Journal Entry lines for the given Abor.
[**get_trial_balance**](AborApi.md#get_trial_balance) | **POST** /api/abor/{scope}/{code}/trialbalance/$query | [EXPERIMENTAL] GetTrialBalance: Get the Trial balance for the given Abor.
[**list_abors**](AborApi.md#list_abors) | **GET** /api/abor | [EXPERIMENTAL] ListAbors: List Abors.
[**list_diary_entries**](AborApi.md#list_diary_entries) | **GET** /api/abor/{scope}/{code}/accountingdiary | [EXPERIMENTAL] ListDiaryEntries: List diary entries.
[**lock_period**](AborApi.md#lock_period) | **POST** /api/abor/{scope}/{code}/accountingdiary/$lockperiod | [EXPERIMENTAL] LockPeriod: Locks the last Closed or given Closed Period.
[**re_open_periods**](AborApi.md#re_open_periods) | **POST** /api/abor/{scope}/{code}/accountingdiary/$reopenperiods | [EXPERIMENTAL] ReOpenPeriods: Reopen periods from a seed Diary Entry Code or when not specified, the last Closed Period for the given Abor.
[**upsert_abor_properties**](AborApi.md#upsert_abor_properties) | **POST** /api/abor/{scope}/{code}/properties/$upsert | [EXPERIMENTAL] UpsertAborProperties: Upsert Abor properties


# **add_diary_entry**
> DiaryEntry add_diary_entry(scope, code, diary_entry_code, diary_entry_request)

[EXPERIMENTAL] AddDiaryEntry: Add a diary entry to the specified Abor.

Adds a new diary entry to the specified Abor

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.diary_entry import DiaryEntry
from lusid.models.diary_entry_request import DiaryEntryRequest
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    AborApi,
    EnvironmentVariablesConfigurationLoader,
    SecretsFileConfigurationLoader,
    ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.AborApi)
    scope = 'scope_example' # str | The scope of the Abor.
    code = 'code_example' # str | The code of the Abor.
    diary_entry_code = 'diary_entry_code_example' # str | Diary entry code
    diary_entry_request = {"name":"2023_Q1","status":"Final","effectiveAt":"2023-04-02T15:10:10.0000000+00:00","queryAsAt":"2023-04-15T15:10:10.0000000+00:00","properties":{"DiaryEntry/AccountingDiary/Reports":{"key":"DiaryEntry/AccountingDiary/Reports","value":{"labelValue":"Some comments"}}}} # DiaryEntryRequest | The diary entry to add.

    try:
        # [EXPERIMENTAL] AddDiaryEntry: Add a diary entry to the specified Abor.
        api_response = await api_instance.add_diary_entry(scope, code, diary_entry_code, diary_entry_request)
        print("The response of AborApi->add_diary_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AborApi->add_diary_entry: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Abor. | 
 **code** | **str**| The code of the Abor. | 
 **diary_entry_code** | **str**| Diary entry code | 
 **diary_entry_request** | [**DiaryEntryRequest**](DiaryEntryRequest.md)| The diary entry to add. | 

### Return type

[**DiaryEntry**](DiaryEntry.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly added diary entry. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **close_period**
> DiaryEntry close_period(scope, code, close_period_diary_entry_request)

[EXPERIMENTAL] ClosePeriod: Closes or locks the current period for the given Abor.

Closes or Locks the current open period for the given Abor.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.close_period_diary_entry_request import ClosePeriodDiaryEntryRequest
from lusid.models.diary_entry import DiaryEntry
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    AborApi,
    EnvironmentVariablesConfigurationLoader,
    SecretsFileConfigurationLoader,
    ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.AborApi)
    scope = 'scope_example' # str | The scope of the Abor.
    code = 'code_example' # str | The code of the Abor.
    close_period_diary_entry_request = {"diaryEntryCode":"2023","name":"2023","effectiveAt":"2023-04-02T15:10:10.0000000+00:00","queryAsAt":"2023-04-15T15:10:10.0000000+00:00","status":"Estimate","properties":{"DiaryEntry/AccountingDiary/Reports":{"key":"DiaryEntry/AccountingDiary/Reports","value":{"labelValue":"Some comments"}}},"closingOptions":[]} # ClosePeriodDiaryEntryRequest | The request body, containing details to apply to the closing/locking period.

    try:
        # [EXPERIMENTAL] ClosePeriod: Closes or locks the current period for the given Abor.
        api_response = await api_instance.close_period(scope, code, close_period_diary_entry_request)
        print("The response of AborApi->close_period:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AborApi->close_period: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Abor. | 
 **code** | **str**| The code of the Abor. | 
 **close_period_diary_entry_request** | [**ClosePeriodDiaryEntryRequest**](ClosePeriodDiaryEntryRequest.md)| The request body, containing details to apply to the closing/locking period. | 

### Return type

[**DiaryEntry**](DiaryEntry.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The DiaryEntry created as a result of the closing of the Period. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_abor**
> Abor create_abor(scope, abor_request)

[EXPERIMENTAL] CreateAbor: Create an Abor.

Create the given Abor.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.abor import Abor
from lusid.models.abor_request import AborRequest
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    AborApi,
    EnvironmentVariablesConfigurationLoader,
    SecretsFileConfigurationLoader,
    ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.AborApi)
    scope = 'scope_example' # str | The scope of the Abor.
    abor_request = {"code":"AborCode","displayName":"Standard Abor","description":"A standard Abor","portfolioIds":[{"scope":"portfolioScope","code":"portfolioCode","portfolioEntityType":"SinglePortfolio"}],"aborConfigurationId":{"scope":"ConfigScope","code":"ConfigCode"},"properties":{"Abor/MyScope/FundManagerName":{"key":"Abor/MyScope/FundManagerName","value":{"labelValue":"Smith"},"effectiveFrom":"2020-03-05T00:00:00.0000000+00:00"}}} # AborRequest | The definition of the Abor.

    try:
        # [EXPERIMENTAL] CreateAbor: Create an Abor.
        api_response = await api_instance.create_abor(scope, abor_request)
        print("The response of AborApi->create_abor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AborApi->create_abor: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Abor. | 
 **abor_request** | [**AborRequest**](AborRequest.md)| The definition of the Abor. | 

### Return type

[**Abor**](Abor.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created abor. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_abor**
> DeletedEntityResponse delete_abor(scope, code)

[EXPERIMENTAL] DeleteAbor: Delete an Abor.

Delete the given Abor.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.deleted_entity_response import DeletedEntityResponse
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    AborApi,
    EnvironmentVariablesConfigurationLoader,
    SecretsFileConfigurationLoader,
    ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.AborApi)
    scope = 'scope_example' # str | The scope of the Abor to be deleted.
    code = 'code_example' # str | The code of the Abor to be deleted. Together with the scope this uniquely identifies the Abor.

    try:
        # [EXPERIMENTAL] DeleteAbor: Delete an Abor.
        api_response = await api_instance.delete_abor(scope, code)
        print("The response of AborApi->delete_abor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AborApi->delete_abor: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Abor to be deleted. | 
 **code** | **str**| The code of the Abor to be deleted. Together with the scope this uniquely identifies the Abor. | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the Abor was deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_abor**
> Abor get_abor(scope, code, effective_at=effective_at, as_at=as_at, property_keys=property_keys)

[EXPERIMENTAL] GetAbor: Get Abor.

Retrieve the definition of a particular Abor.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.abor import Abor
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    AborApi,
    EnvironmentVariablesConfigurationLoader,
    SecretsFileConfigurationLoader,
    ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.AborApi)
    scope = 'scope_example' # str | The scope of the Abor.
    code = 'code_example' # str | The code of the Abor. Together with the scope this uniquely identifies the Abor.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve the Abor properties. Defaults to the current LUSID system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Abor definition. Defaults to returning the latest version of the Abor definition if not specified. (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the 'Abor' domain to decorate onto the Abor.              These must take the format {domain}/{scope}/{code}, for example 'Abor/Manager/Id'. If not provided will return all the entitled properties for that Abor. (optional)

    try:
        # [EXPERIMENTAL] GetAbor: Get Abor.
        api_response = await api_instance.get_abor(scope, code, effective_at=effective_at, as_at=as_at, property_keys=property_keys)
        print("The response of AborApi->get_abor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AborApi->get_abor: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Abor. | 
 **code** | **str**| The code of the Abor. Together with the scope this uniquely identifies the Abor. | 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the Abor properties. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Abor definition. Defaults to returning the latest version of the Abor definition if not specified. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;Abor&#39; domain to decorate onto the Abor.              These must take the format {domain}/{scope}/{code}, for example &#39;Abor/Manager/Id&#39;. If not provided will return all the entitled properties for that Abor. | [optional] 

### Return type

[**Abor**](Abor.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Abor definition. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_journal_entry_lines**
> VersionedResourceListOfJournalEntryLine get_journal_entry_lines(scope, code, journal_entry_lines_query_parameters, as_at=as_at, filter=filter, limit=limit, page=page)

[EXPERIMENTAL] GetJournalEntryLines: Get the Journal Entry lines for the given Abor.

Gets the Journal Entry lines for the given Abor                The Journal Entry lines have been generated from transactions and translated via posting rules

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.journal_entry_lines_query_parameters import JournalEntryLinesQueryParameters
from lusid.models.versioned_resource_list_of_journal_entry_line import VersionedResourceListOfJournalEntryLine
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    AborApi,
    EnvironmentVariablesConfigurationLoader,
    SecretsFileConfigurationLoader,
    ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.AborApi)
    scope = 'scope_example' # str | The scope of the Abor.
    code = 'code_example' # str | The code of the Abor. Together with the scope is creating the unique identifier for the given Abor.
    journal_entry_lines_query_parameters = {"start":{"date":"2018-03-05T00:00:00.0000000+00:00"},"end":{"diaryEntry":"2023_01"},"dateMode":"ActivityDate","generalLedgerProfileCode":"STEMProfile1","propertyKeys":[]} # JournalEntryLinesQueryParameters | The query parameters used in running the generation of the Journal Entry lines.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve Journal Entry lines. Defaults to returning the latest version               of each transaction if not specified. (optional)
    filter = 'filter_example' # str | \"Expression to filter the result set.\" (optional)
    limit = 56 # int | When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing Journal Entry lines from a previous call to GetJournalEntryLines. (optional)

    try:
        # [EXPERIMENTAL] GetJournalEntryLines: Get the Journal Entry lines for the given Abor.
        api_response = await api_instance.get_journal_entry_lines(scope, code, journal_entry_lines_query_parameters, as_at=as_at, filter=filter, limit=limit, page=page)
        print("The response of AborApi->get_journal_entry_lines:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AborApi->get_journal_entry_lines: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Abor. | 
 **code** | **str**| The code of the Abor. Together with the scope is creating the unique identifier for the given Abor. | 
 **journal_entry_lines_query_parameters** | [**JournalEntryLinesQueryParameters**](JournalEntryLinesQueryParameters.md)| The query parameters used in running the generation of the Journal Entry lines. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve Journal Entry lines. Defaults to returning the latest version               of each transaction if not specified. | [optional] 
 **filter** | **str**| \&quot;Expression to filter the result set.\&quot; | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing Journal Entry lines from a previous call to GetJournalEntryLines. | [optional] 

### Return type

[**VersionedResourceListOfJournalEntryLine**](VersionedResourceListOfJournalEntryLine.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Journal Entry lines for the specified Abor. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_trial_balance**
> VersionedResourceListOfTrialBalance get_trial_balance(scope, code, trial_balance_query_parameters, as_at=as_at, filter=filter, limit=limit, page=page)

[EXPERIMENTAL] GetTrialBalance: Get the Trial balance for the given Abor.

Gets the Trial balance for the given Abor    The Trial balance has been generated from transactions, translated via posting rules and aggregated based on a General Ledger Profile (where specified)

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.trial_balance_query_parameters import TrialBalanceQueryParameters
from lusid.models.versioned_resource_list_of_trial_balance import VersionedResourceListOfTrialBalance
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    AborApi,
    EnvironmentVariablesConfigurationLoader,
    SecretsFileConfigurationLoader,
    ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.AborApi)
    scope = 'scope_example' # str | The scope of the Abor.
    code = 'code_example' # str | The code of the Abor. Together with the scope is the unique identifier for the given Abor.
    trial_balance_query_parameters = {"start":{"date":"2018-03-05T00:00:00.0000000+00:00"},"end":{"diaryEntry":"2023_01"},"dateMode":"ActivityDate","generalLedgerProfileCode":"STEMProfile1","propertyKeys":[],"excludeCleardownModule":true} # TrialBalanceQueryParameters | The query parameters used in running the generation of the Trial Balance.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve trial balance. Defaults to returning the latest version              of each transaction if not specified. (optional)
    filter = 'filter_example' # str | \"Expression to filter the result set.\" (optional)
    limit = 56 # int | When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing Trial balance from a previous call to Trial balance. (optional)

    try:
        # [EXPERIMENTAL] GetTrialBalance: Get the Trial balance for the given Abor.
        api_response = await api_instance.get_trial_balance(scope, code, trial_balance_query_parameters, as_at=as_at, filter=filter, limit=limit, page=page)
        print("The response of AborApi->get_trial_balance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AborApi->get_trial_balance: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Abor. | 
 **code** | **str**| The code of the Abor. Together with the scope is the unique identifier for the given Abor. | 
 **trial_balance_query_parameters** | [**TrialBalanceQueryParameters**](TrialBalanceQueryParameters.md)| The query parameters used in running the generation of the Trial Balance. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve trial balance. Defaults to returning the latest version              of each transaction if not specified. | [optional] 
 **filter** | **str**| \&quot;Expression to filter the result set.\&quot; | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing Trial balance from a previous call to Trial balance. | [optional] 

### Return type

[**VersionedResourceListOfTrialBalance**](VersionedResourceListOfTrialBalance.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Trial Balance for the specified Abor. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_abors**
> PagedResourceListOfAbor list_abors(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)

[EXPERIMENTAL] ListAbors: List Abors.

List all the Abors matching particular criteria.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.paged_resource_list_of_abor import PagedResourceListOfAbor
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    AborApi,
    EnvironmentVariablesConfigurationLoader,
    SecretsFileConfigurationLoader,
    ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.AborApi)
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to list the TimeVariant properties for the Abor. Defaults to the current LUSID              system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the Abor. Defaults to returning the latest version of each Abor if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing Abor; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. (optional)
    limit = 56 # int | When paginating, limit the results to this number. Defaults to 100 if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the results.              For example, to filter on the Abor type, specify \"id.Code eq 'Abor1'\". For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. (optional)
    sort_by = ['sort_by_example'] # List[str] | A list of field names or properties to sort by, each suffixed by \" ASC\" or \" DESC\". (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the 'Abor' domain to decorate onto each Abor.              These must take the format {domain}/{scope}/{code}, for example 'Abor/Manager/Id'. (optional)

    try:
        # [EXPERIMENTAL] ListAbors: List Abors.
        api_response = await api_instance.list_abors(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)
        print("The response of AborApi->list_abors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AborApi->list_abors: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **effective_at** | **str**| The effective datetime or cut label at which to list the TimeVariant properties for the Abor. Defaults to the current LUSID              system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the Abor. Defaults to returning the latest version of each Abor if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing Abor; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results.              For example, to filter on the Abor type, specify \&quot;id.Code eq &#39;Abor1&#39;\&quot;. For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;Abor&#39; domain to decorate onto each Abor.              These must take the format {domain}/{scope}/{code}, for example &#39;Abor/Manager/Id&#39;. | [optional] 

### Return type

[**PagedResourceListOfAbor**](PagedResourceListOfAbor.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested abors. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_diary_entries**
> PagedResourceListOfDiaryEntry list_diary_entries(scope, code, effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)

[EXPERIMENTAL] ListDiaryEntries: List diary entries.

List all the diary entries matching particular criteria.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.paged_resource_list_of_diary_entry import PagedResourceListOfDiaryEntry
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    AborApi,
    EnvironmentVariablesConfigurationLoader,
    SecretsFileConfigurationLoader,
    ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.AborApi)
    scope = 'scope_example' # str | The scope of the Abor.
    code = 'code_example' # str | The code of the Abor.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to list the TimeVariant properties for the Diary Entries. Defaults to the current LUSID              system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the DiaryEntry. Defaults to returning the latest version of each DiaryEntry if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing diary entries; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. (optional)
    limit = 56 # int | When paginating, limit the results to this number. Defaults to 100 if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the results.              For example, to filter on the DiaryEntry type, specify \"type eq 'PeriodBoundary'\". For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. (optional)
    sort_by = ['sort_by_example'] # List[str] | A list of field names or properties to sort by, each suffixed by \" ASC\" or \" DESC\". (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the 'DiaryEntry' domain to decorate onto each DiaryEntry.              These must take the format {domain}/{scope}/{code}, for example 'DiaryEntry/Report/Id'. (optional)

    try:
        # [EXPERIMENTAL] ListDiaryEntries: List diary entries.
        api_response = await api_instance.list_diary_entries(scope, code, effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)
        print("The response of AborApi->list_diary_entries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AborApi->list_diary_entries: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Abor. | 
 **code** | **str**| The code of the Abor. | 
 **effective_at** | **str**| The effective datetime or cut label at which to list the TimeVariant properties for the Diary Entries. Defaults to the current LUSID              system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the DiaryEntry. Defaults to returning the latest version of each DiaryEntry if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing diary entries; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results.              For example, to filter on the DiaryEntry type, specify \&quot;type eq &#39;PeriodBoundary&#39;\&quot;. For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;DiaryEntry&#39; domain to decorate onto each DiaryEntry.              These must take the format {domain}/{scope}/{code}, for example &#39;DiaryEntry/Report/Id&#39;. | [optional] 

### Return type

[**PagedResourceListOfDiaryEntry**](PagedResourceListOfDiaryEntry.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested diary entries. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lock_period**
> DiaryEntry lock_period(scope, code, lock_period_diary_entry_request=lock_period_diary_entry_request)

[EXPERIMENTAL] LockPeriod: Locks the last Closed or given Closed Period.

Locks the specified or last locked period for the given Abor.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.diary_entry import DiaryEntry
from lusid.models.lock_period_diary_entry_request import LockPeriodDiaryEntryRequest
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    AborApi,
    EnvironmentVariablesConfigurationLoader,
    SecretsFileConfigurationLoader,
    ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.AborApi)
    scope = 'scope_example' # str | The scope of the Abor.
    code = 'code_example' # str | The code of the Abor.
    lock_period_diary_entry_request = {"diaryEntryCode":"YearEnd2023","closingOptions":[]} # LockPeriodDiaryEntryRequest | The request body, detailing lock details (optional)

    try:
        # [EXPERIMENTAL] LockPeriod: Locks the last Closed or given Closed Period.
        api_response = await api_instance.lock_period(scope, code, lock_period_diary_entry_request=lock_period_diary_entry_request)
        print("The response of AborApi->lock_period:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AborApi->lock_period: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Abor. | 
 **code** | **str**| The code of the Abor. | 
 **lock_period_diary_entry_request** | [**LockPeriodDiaryEntryRequest**](LockPeriodDiaryEntryRequest.md)| The request body, detailing lock details | [optional] 

### Return type

[**DiaryEntry**](DiaryEntry.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated DiaryEntry as a result of the locking of the Period. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **re_open_periods**
> PeriodDiaryEntriesReopenedResponse re_open_periods(scope, code, re_open_period_diary_entry_request=re_open_period_diary_entry_request)

[EXPERIMENTAL] ReOpenPeriods: Reopen periods from a seed Diary Entry Code or when not specified, the last Closed Period for the given Abor.

Reopens one or more periods.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.period_diary_entries_reopened_response import PeriodDiaryEntriesReopenedResponse
from lusid.models.re_open_period_diary_entry_request import ReOpenPeriodDiaryEntryRequest
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    AborApi,
    EnvironmentVariablesConfigurationLoader,
    SecretsFileConfigurationLoader,
    ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.AborApi)
    scope = 'scope_example' # str | The scope of the Abor to be deleted.
    code = 'code_example' # str | The code of the Abor to be deleted. Together with the scope this uniquely identifies the Abor.
    re_open_period_diary_entry_request = {"diaryEntryCode":"YearEnd2023"} # ReOpenPeriodDiaryEntryRequest | The request body, detailing re open details (optional)

    try:
        # [EXPERIMENTAL] ReOpenPeriods: Reopen periods from a seed Diary Entry Code or when not specified, the last Closed Period for the given Abor.
        api_response = await api_instance.re_open_periods(scope, code, re_open_period_diary_entry_request=re_open_period_diary_entry_request)
        print("The response of AborApi->re_open_periods:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AborApi->re_open_periods: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Abor to be deleted. | 
 **code** | **str**| The code of the Abor to be deleted. Together with the scope this uniquely identifies the Abor. | 
 **re_open_period_diary_entry_request** | [**ReOpenPeriodDiaryEntryRequest**](ReOpenPeriodDiaryEntryRequest.md)| The request body, detailing re open details | [optional] 

### Return type

[**PeriodDiaryEntriesReopenedResponse**](PeriodDiaryEntriesReopenedResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the DiaryEntryCodes were deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_abor_properties**
> AborProperties upsert_abor_properties(scope, code, request_body=request_body)

[EXPERIMENTAL] UpsertAborProperties: Upsert Abor properties

Update or insert one or more properties onto a single Abor. A property will be updated if it  already exists and inserted if it does not. All properties must be of the domain 'Abor'.                Upserting a property that exists for an Abor, with a null value, will delete the instance of the property for that group.                Properties have an <i>effectiveFrom</i> datetime for which the property is valid, and an <i>effectiveUntil</i>  datetime until which the property is valid. Not supplying an <i>effectiveUntil</i> datetime results in the property being  valid indefinitely, or until the next <i>effectiveFrom</i> datetime of the property.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from lusid.models.abor_properties import AborProperties
from lusid.models.model_property import ModelProperty
from pprint import pprint

import os
from lusid import (
    ApiClientFactory,
    AborApi,
    EnvironmentVariablesConfigurationLoader,
    SecretsFileConfigurationLoader,
    ArgsConfigurationLoader
)

# Use the lusid ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://www.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.AborApi)
    scope = 'scope_example' # str | The scope of the Abor to update or insert the properties onto.
    code = 'code_example' # str | The code of the Abor to update or insert the properties onto. Together with the scope this uniquely identifies the Abor.
    request_body = {"Abor/MyScope/FundManagerName":{"key":"Abor/MyScope/FundManagerName","value":{"labelValue":"Smith"},"effectiveFrom":"2018-03-05T00:00:00.0000000+00:00"},"Abor/MyScope/SomeProperty":{"key":"Abor/MyScope/SomeProperty","value":{"labelValue":"SomeValue"},"effectiveFrom":"2016-01-01T00:00:00.0000000+00:00"},"Abor/MyScope/AnotherProperty":{"key":"Abor/MyScope/AnotherProperty","value":{"labelValue":"AnotherValue"},"effectiveFrom":"2018-03-05T00:00:00.0000000+00:00","effectiveUntil":"2020-01-01T00:00:00.0000000+00:00"},"Abor/MyScope/ReBalanceInterval":{"key":"Abor/MyScope/ReBalanceInterval","value":{"metricValue":{"value":30,"unit":"Days"}}}} # Dict[str, ModelProperty] | The properties to be updated or inserted onto the Abor. Each property in               the request must be keyed by its unique property key. This has the format {domain}/{scope}/{code} e.g. \"Abor/Manager/Id\". (optional)

    try:
        # [EXPERIMENTAL] UpsertAborProperties: Upsert Abor properties
        api_response = await api_instance.upsert_abor_properties(scope, code, request_body=request_body)
        print("The response of AborApi->upsert_abor_properties:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AborApi->upsert_abor_properties: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Abor to update or insert the properties onto. | 
 **code** | **str**| The code of the Abor to update or insert the properties onto. Together with the scope this uniquely identifies the Abor. | 
 **request_body** | [**Dict[str, ModelProperty]**](ModelProperty.md)| The properties to be updated or inserted onto the Abor. Each property in               the request must be keyed by its unique property key. This has the format {domain}/{scope}/{code} e.g. \&quot;Abor/Manager/Id\&quot;. | [optional] 

### Return type

[**AborProperties**](AborProperties.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated or inserted properties |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

