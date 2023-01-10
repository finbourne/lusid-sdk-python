# lusid.ParticipationsApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_participation**](ParticipationsApi.md#delete_participation) | **DELETE** /api/participations/{scope}/{code} | [EARLY ACCESS] DeleteParticipation: Delete participation
[**get_participation**](ParticipationsApi.md#get_participation) | **GET** /api/participations/{scope}/{code} | [EARLY ACCESS] GetParticipation: Get Participation
[**list_participations**](ParticipationsApi.md#list_participations) | **GET** /api/participations | [EARLY ACCESS] ListParticipations: List Participations
[**upsert_participations**](ParticipationsApi.md#upsert_participations) | **POST** /api/participations | [EARLY ACCESS] UpsertParticipations: Upsert Participation


# **delete_participation**
> DeletedEntityResponse delete_participation(scope, code)

[EARLY ACCESS] DeleteParticipation: Delete participation

Delete an participation. Deletion will be valid from the participation's creation datetime.  This means that the participation will no longer exist at any effective datetime from the asAt datetime of deletion.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://www.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://www.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://www.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.ParticipationsApi(api_client)
    scope = 'scope_example' # str | The participation scope.
code = 'code_example' # str | The participation's code. This, together with the scope uniquely identifies the participation to delete.

    try:
        # [EARLY ACCESS] DeleteParticipation: Delete participation
        api_response = api_instance.delete_participation(scope, code)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ParticipationsApi->delete_participation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The participation scope. | 
 **code** | **str**| The participation&#39;s code. This, together with the scope uniquely identifies the participation to delete. | 

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
**200** | The response from deleting an participation. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_participation**
> Participation get_participation(scope, code, as_at=as_at, property_keys=property_keys)

[EARLY ACCESS] GetParticipation: Get Participation

Fetch a Participation that matches the specified identifier

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://www.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://www.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://www.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.ParticipationsApi(api_client)
    scope = 'scope_example' # str | The scope to which the participation belongs.
code = 'code_example' # str | The participation's unique identifier.
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the participation. Defaults to return the latest version of the participation if not specified. (optional)
property_keys = ['property_keys_example'] # list[str] | A list of property keys from the \"Participation\" domain to decorate onto the participation.              These take the format {domain}/{scope}/{code} e.g. \"Participation/system/Name\". (optional)

    try:
        # [EARLY ACCESS] GetParticipation: Get Participation
        api_response = api_instance.get_participation(scope, code, as_at=as_at, property_keys=property_keys)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ParticipationsApi->get_participation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope to which the participation belongs. | 
 **code** | **str**| The participation&#39;s unique identifier. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the participation. Defaults to return the latest version of the participation if not specified. | [optional] 
 **property_keys** | [**list[str]**](str.md)| A list of property keys from the \&quot;Participation\&quot; domain to decorate onto the participation.              These take the format {domain}/{scope}/{code} e.g. \&quot;Participation/system/Name\&quot;. | [optional] 

### Return type

[**Participation**](Participation.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The participation matching the given identifier. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_participations**
> PagedResourceListOfParticipation list_participations(as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter, property_keys=property_keys)

[EARLY ACCESS] ListParticipations: List Participations

Fetch the last pre-AsAt date version of each Participation in scope (does not fetch the entire history).

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://www.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://www.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://www.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.ParticipationsApi(api_client)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the participation. Defaults to return the latest version of the participation if not specified. (optional)
page = 'page_example' # str | The pagination token to use to continue listing participations from a previous call to list participations.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields              must not have changed since the original request. (optional)
sort_by = ['sort_by_example'] # list[str] | Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName. (optional)
limit = 56 # int | When paginating, limit the number of returned results to this many. (optional)
filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid. (optional)
property_keys = ['property_keys_example'] # list[str] | A list of property keys from the \"Participation\" domain to decorate onto each participation.                  These take the format {domain}/{scope}/{code} e.g. \"Participation/system/Name\". (optional)

    try:
        # [EARLY ACCESS] ListParticipations: List Participations
        api_response = api_instance.list_participations(as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter, property_keys=property_keys)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ParticipationsApi->list_participations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to retrieve the participation. Defaults to return the latest version of the participation if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing participations from a previous call to list participations.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields              must not have changed since the original request. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **property_keys** | [**list[str]**](str.md)| A list of property keys from the \&quot;Participation\&quot; domain to decorate onto each participation.                  These take the format {domain}/{scope}/{code} e.g. \&quot;Participation/system/Name\&quot;. | [optional] 

### Return type

[**PagedResourceListOfParticipation**](PagedResourceListOfParticipation.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Participations in scope. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_participations**
> ResourceListOfParticipation upsert_participations(participation_set_request=participation_set_request)

[EARLY ACCESS] UpsertParticipations: Upsert Participation

Upsert; update existing participations with given ids, or create new participations otherwise.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://www.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://www.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://www.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.ParticipationsApi(api_client)
    participation_set_request = {"requests":[{"id":{"scope":"MyScope","code":"PART00000123"},"placementId":{"scope":"MyScope","code":"PLAC00000123"},"orderId":{"scope":"MyScope","code":"ORDER00000123"}}]} # ParticipationSetRequest | The collection of participation requests. (optional)

    try:
        # [EARLY ACCESS] UpsertParticipations: Upsert Participation
        api_response = api_instance.upsert_participations(participation_set_request=participation_set_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ParticipationsApi->upsert_participations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **participation_set_request** | [**ParticipationSetRequest**](ParticipationSetRequest.md)| The collection of participation requests. | [optional] 

### Return type

[**ResourceListOfParticipation**](ResourceListOfParticipation.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A collection of participations. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

