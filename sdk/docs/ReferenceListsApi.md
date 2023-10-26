# lusid.ReferenceListsApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_reference_list**](ReferenceListsApi.md#delete_reference_list) | **DELETE** /api/referencelists/{scope}/{code} | [EARLY ACCESS] DeleteReferenceList: Delete Reference List
[**get_reference_list**](ReferenceListsApi.md#get_reference_list) | **GET** /api/referencelists/{scope}/{code} | [EARLY ACCESS] GetReferenceList: Get Reference List
[**list_reference_lists**](ReferenceListsApi.md#list_reference_lists) | **GET** /api/referencelists | [EARLY ACCESS] ListReferenceLists: List Reference Lists
[**upsert_reference_list**](ReferenceListsApi.md#upsert_reference_list) | **POST** /api/referencelists | [EARLY ACCESS] UpsertReferenceList: Upsert Reference List


# **delete_reference_list**
> DeletedEntityResponse delete_reference_list(scope, code)

[EARLY ACCESS] DeleteReferenceList: Delete Reference List

Delete a Reference List instance.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from lusid.models.deleted_entity_response import DeletedEntityResponse
from pprint import pprint

from lusid import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
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
    api_instance = api_client_factory.build(lusid.ReferenceListsApi)
    scope = 'scope_example' # str | The scope to which the Reference List belongs.
    code = 'code_example' # str | The Reference List's unique identifier.

    try:
        # [EARLY ACCESS] DeleteReferenceList: Delete Reference List
        api_response = await api_instance.delete_reference_list(scope, code)
        print("The response of ReferenceListsApi->delete_reference_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferenceListsApi->delete_reference_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope to which the Reference List belongs. | 
 **code** | **str**| The Reference List&#39;s unique identifier. | 

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
**200** | The deleted reference list response. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reference_list**
> ReferenceListResponse get_reference_list(scope, code, as_at=as_at)

[EARLY ACCESS] GetReferenceList: Get Reference List

Retrieve a Reference List instance at a point in AsAt time.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from lusid.models.reference_list_response import ReferenceListResponse
from pprint import pprint

from lusid import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
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
    api_instance = api_client_factory.build(lusid.ReferenceListsApi)
    scope = 'scope_example' # str | The scope to which the Reference List belongs.
    code = 'code_example' # str | The Reference List's unique identifier.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Reference List. Defaults to return the latest version of the Reference List if not specified. (optional)

    try:
        # [EARLY ACCESS] GetReferenceList: Get Reference List
        api_response = await api_instance.get_reference_list(scope, code, as_at=as_at)
        print("The response of ReferenceListsApi->get_reference_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferenceListsApi->get_reference_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope to which the Reference List belongs. | 
 **code** | **str**| The Reference List&#39;s unique identifier. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Reference List. Defaults to return the latest version of the Reference List if not specified. | [optional] 

### Return type

[**ReferenceListResponse**](ReferenceListResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Reference List matching the requested identifier. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_reference_lists**
> PagedResourceListOfReferenceListResponse list_reference_lists(as_at=as_at, page=page, limit=limit, filter=filter)

[EARLY ACCESS] ListReferenceLists: List Reference Lists

List all the Reference Lists matching particular criteria.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from lusid.models.paged_resource_list_of_reference_list_response import PagedResourceListOfReferenceListResponse
from pprint import pprint

from lusid import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
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
    api_instance = api_client_factory.build(lusid.ReferenceListsApi)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list Reference Lists. Defaults to return the latest version of Reference Lists if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing Reference Lists from a previous call to list Reference Lists.              This value is returned from the previous call. If a pagination token is provided, the filter, limit and asAt fields              must not have changed since the original request. (optional)
    limit = 56 # int | When paginating, limit the number of returned results to this number. Defaults to 100 if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid. (optional)

    try:
        # [EARLY ACCESS] ListReferenceLists: List Reference Lists
        api_response = await api_instance.list_reference_lists(as_at=as_at, page=page, limit=limit, filter=filter)
        print("The response of ReferenceListsApi->list_reference_lists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferenceListsApi->list_reference_lists: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list Reference Lists. Defaults to return the latest version of Reference Lists if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing Reference Lists from a previous call to list Reference Lists.              This value is returned from the previous call. If a pagination token is provided, the filter, limit and asAt fields              must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid. | [optional] 

### Return type

[**PagedResourceListOfReferenceListResponse**](PagedResourceListOfReferenceListResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of Reference Lists. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_reference_list**
> ReferenceListResponse upsert_reference_list(reference_list_request=reference_list_request)

[EARLY ACCESS] UpsertReferenceList: Upsert Reference List

Insert the Reference List if it does not exist or update the Reference List with the supplied state if it does exist.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from lusid.models.reference_list_request import ReferenceListRequest
from lusid.models.reference_list_response import ReferenceListResponse
from pprint import pprint

from lusid import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
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
    api_instance = api_client_factory.build(lusid.ReferenceListsApi)
    reference_list_request = {"id":{"scope":"MyScope","code":"MyStringList"},"name":"MyReferenceListName","description":"My reference list description","tags":["tags","associated","with","my","list"],"referenceList":{"values":["value1","value2"],"referenceListType":"StringList"}} # ReferenceListRequest | The payload describing the Reference List instance. (optional)

    try:
        # [EARLY ACCESS] UpsertReferenceList: Upsert Reference List
        api_response = await api_instance.upsert_reference_list(reference_list_request=reference_list_request)
        print("The response of ReferenceListsApi->upsert_reference_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferenceListsApi->upsert_reference_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reference_list_request** | [**ReferenceListRequest**](ReferenceListRequest.md)| The payload describing the Reference List instance. | [optional] 

### Return type

[**ReferenceListResponse**](ReferenceListResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The upserted Reference List instance. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

