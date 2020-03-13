# lusid.CorporateActionSourcesApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_upsert_corporate_actions**](CorporateActionSourcesApi.md#batch_upsert_corporate_actions) | **POST** /api/corporateactionsources/{scope}/{code}/corporateactions | [BETA] Upsert corporate actions
[**create_corporate_action_source**](CorporateActionSourcesApi.md#create_corporate_action_source) | **POST** /api/corporateactionsources | [BETA] Create Corporate Action Source
[**delete_corporate_action_source**](CorporateActionSourcesApi.md#delete_corporate_action_source) | **DELETE** /api/corporateactionsources/{scope}/{code} | [BETA] Delete a corporate action source
[**get_corporate_actions**](CorporateActionSourcesApi.md#get_corporate_actions) | **GET** /api/corporateactionsources/{scope}/{code}/corporateactions | [BETA] Get corporate actions
[**list_corporate_action_sources**](CorporateActionSourcesApi.md#list_corporate_action_sources) | **GET** /api/corporateactionsources | [BETA] List corporate action sources


# **batch_upsert_corporate_actions**
> UpsertCorporateActionsResponse batch_upsert_corporate_actions(scope, code, actions=actions)

[BETA] Upsert corporate actions

Attempt to create/update one or more corporate action in a specified corporate action source. Failed actions will be identified in the body of the response.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://localhost/api
configuration.host = "http://localhost/api"

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.CorporateActionSourcesApi(api_client)
    scope = 'scope_example' # str | The scope of corporate action source
code = 'code_example' # str | The code of the corporate action source
actions = [lusid.UpsertCorporateActionRequest()] # list[UpsertCorporateActionRequest] | The corporate action definitions (optional)

    try:
        # [BETA] Upsert corporate actions
        api_response = api_instance.batch_upsert_corporate_actions(scope, code, actions=actions)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CorporateActionSourcesApi->batch_upsert_corporate_actions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of corporate action source | 
 **code** | **str**| The code of the corporate action source | 
 **actions** | [**list[UpsertCorporateActionRequest]**](UpsertCorporateActionRequest.md)| The corporate action definitions | [optional] 

### Return type

[**UpsertCorporateActionsResponse**](UpsertCorporateActionsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created corporate actions |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_corporate_action_source**
> CorporateActionSource create_corporate_action_source(request)

[BETA] Create Corporate Action Source

Attempt to create a corporate action source.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://localhost/api
configuration.host = "http://localhost/api"

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.CorporateActionSourcesApi(api_client)
    request = lusid.CreateCorporateActionSourceRequest() # CreateCorporateActionSourceRequest | The corporate action source definition

    try:
        # [BETA] Create Corporate Action Source
        api_response = api_instance.create_corporate_action_source(request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CorporateActionSourcesApi->create_corporate_action_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CreateCorporateActionSourceRequest**](CreateCorporateActionSourceRequest.md)| The corporate action source definition | 

### Return type

[**CorporateActionSource**](CorporateActionSource.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created corporate action source |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_corporate_action_source**
> DeletedEntityResponse delete_corporate_action_source(scope, code)

[BETA] Delete a corporate action source

Deletes a single corporate action source

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://localhost/api
configuration.host = "http://localhost/api"

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.CorporateActionSourcesApi(api_client)
    scope = 'scope_example' # str | The Scope of the Corporate Action Source to be deleted
code = 'code_example' # str | The Code of the Corporate Action Source to be deleted

    try:
        # [BETA] Delete a corporate action source
        api_response = api_instance.delete_corporate_action_source(scope, code)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CorporateActionSourcesApi->delete_corporate_action_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The Scope of the Corporate Action Source to be deleted | 
 **code** | **str**| The Code of the Corporate Action Source to be deleted | 

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
**200** | Corporate Action Source Deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_corporate_actions**
> ResourceListOfCorporateAction get_corporate_actions(scope, code, from_effective_at=from_effective_at, to_effective_at=to_effective_at, as_at=as_at, sort_by=sort_by, start=start, limit=limit, filter=filter)

[BETA] Get corporate actions

Gets corporate actions from a specific corporate action source

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://localhost/api
configuration.host = "http://localhost/api"

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.CorporateActionSourcesApi(api_client)
    scope = 'scope_example' # str | The scope of the corporate action source
code = 'code_example' # str | The code of the corporate action source
from_effective_at = 'from_effective_at_example' # str | Optional. The start effective date of the data range (optional)
to_effective_at = 'to_effective_at_example' # str | Optional. The end effective date of the data range (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The AsAt date of the data (optional)
sort_by = ['sort_by_example'] # list[str] | Optional. Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName (optional)
start = 56 # int | Optional. When paginating, skip this number of results (optional)
limit = 56 # int | Optional. When paginating, limit the number of returned results to this many (optional)
filter = 'filter_example' # str | Optional. Expression to filter the result set.              For example, to filter on the Announcement Date, use \"announcementDate eq '2020-03-06'\"               Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)

    try:
        # [BETA] Get corporate actions
        api_response = api_instance.get_corporate_actions(scope, code, from_effective_at=from_effective_at, to_effective_at=to_effective_at, as_at=as_at, sort_by=sort_by, start=start, limit=limit, filter=filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CorporateActionSourcesApi->get_corporate_actions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the corporate action source | 
 **code** | **str**| The code of the corporate action source | 
 **from_effective_at** | **str**| Optional. The start effective date of the data range | [optional] 
 **to_effective_at** | **str**| Optional. The end effective date of the data range | [optional] 
 **as_at** | **datetime**| Optional. The AsAt date of the data | [optional] 
 **sort_by** | [**list[str]**](str.md)| Optional. Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName | [optional] 
 **start** | **int**| Optional. When paginating, skip this number of results | [optional] 
 **limit** | **int**| Optional. When paginating, limit the number of returned results to this many | [optional] 
 **filter** | **str**| Optional. Expression to filter the result set.              For example, to filter on the Announcement Date, use \&quot;announcementDate eq &#39;2020-03-06&#39;\&quot;               Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 

### Return type

[**ResourceListOfCorporateAction**](ResourceListOfCorporateAction.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Corporate Actions |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_corporate_action_sources**
> ResourceListOfCorporateActionSource list_corporate_action_sources(as_at=as_at, sort_by=sort_by, start=start, limit=limit, filter=filter)

[BETA] List corporate action sources

Gets a list of all corporate action sources

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://localhost/api
configuration.host = "http://localhost/api"

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.CorporateActionSourcesApi(api_client)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The AsAt date of the data (optional)
sort_by = ['sort_by_example'] # list[str] | Optional. Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName (optional)
start = 56 # int | Optional. When paginating, skip this number of results (optional)
limit = 56 # int | Optional. When paginating, limit the number of returned results to this many (optional)
filter = 'filter_example' # str | Optional. Expression to filter the result set.               For example, to filter on the Display Name, use \"displayName eq 'string'\"              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)

    try:
        # [BETA] List corporate action sources
        api_response = api_instance.list_corporate_action_sources(as_at=as_at, sort_by=sort_by, start=start, limit=limit, filter=filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CorporateActionSourcesApi->list_corporate_action_sources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| Optional. The AsAt date of the data | [optional] 
 **sort_by** | [**list[str]**](str.md)| Optional. Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName | [optional] 
 **start** | **int**| Optional. When paginating, skip this number of results | [optional] 
 **limit** | **int**| Optional. When paginating, limit the number of returned results to this many | [optional] 
 **filter** | **str**| Optional. Expression to filter the result set.               For example, to filter on the Display Name, use \&quot;displayName eq &#39;string&#39;\&quot;              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 

### Return type

[**ResourceListOfCorporateActionSource**](ResourceListOfCorporateActionSource.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All Existing Corporate Action Sources |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

