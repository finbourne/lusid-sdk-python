# lusid.ConfigurationRecipeApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_configuration_recipe**](ConfigurationRecipeApi.md#delete_configuration_recipe) | **DELETE** /api/recipes/{scope}/{code} | [EXPERIMENTAL] Delete a Configuration Recipe, assuming that it is present.
[**get_configuration_recipe**](ConfigurationRecipeApi.md#get_configuration_recipe) | **GET** /api/recipes/{scope}/{code} | [EXPERIMENTAL] Get Configuration Recipe
[**list_configuration_recipes**](ConfigurationRecipeApi.md#list_configuration_recipes) | **GET** /api/recipes/{scope} | [EXPERIMENTAL] List the set of Configuration Recipes
[**upsert_configuration_recipe**](ConfigurationRecipeApi.md#upsert_configuration_recipe) | **POST** /api/recipes/{scope} | [EXPERIMENTAL] Upsert a Configuration Recipe. This creates or updates the data in Lusid.


# **delete_configuration_recipe**
> AnnulSingleStructuredDataResponse delete_configuration_recipe(scope, code)

[EXPERIMENTAL] Delete a Configuration Recipe, assuming that it is present.

Delete the specified Configuration Recipe from a single scope.                The response will return either detail of the deleted item, or an explanation (failure) as to why this did not succeed.                It is important to always check for any unsuccessful response.

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
    api_instance = lusid.ConfigurationRecipeApi(api_client)
    scope = 'scope_example' # str | The scope of the Configuration Recipe to delete.
code = 'code_example' # str | The Configuration Recipe to delete.

    try:
        # [EXPERIMENTAL] Delete a Configuration Recipe, assuming that it is present.
        api_response = api_instance.delete_configuration_recipe(scope, code)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationRecipeApi->delete_configuration_recipe: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Configuration Recipe to delete. | 
 **code** | **str**| The Configuration Recipe to delete. | 

### Return type

[**AnnulSingleStructuredDataResponse**](AnnulSingleStructuredDataResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The AsAt of deletion or failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_configuration_recipe**
> GetRecipeResponse get_configuration_recipe(scope, code, as_at=as_at)

[EXPERIMENTAL] Get Configuration Recipe

Get a Configuration Recipe from a single scope.                The response will return either the recipe that has been stored, or a failure explaining why the request was unsuccessful.                It is important to always check for any unsuccessful requests (failures).

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
    api_instance = lusid.ConfigurationRecipeApi(api_client)
    scope = 'scope_example' # str | The scope of the Configuration Recipe to retrieve.
code = 'code_example' # str | The name of the recipe to retrieve the data for.
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Configuration Recipe. Defaults to return the latest version if not specified. (optional)

    try:
        # [EXPERIMENTAL] Get Configuration Recipe
        api_response = api_instance.get_configuration_recipe(scope, code, as_at=as_at)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationRecipeApi->get_configuration_recipe: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Configuration Recipe to retrieve. | 
 **code** | **str**| The name of the recipe to retrieve the data for. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Configuration Recipe. Defaults to return the latest version if not specified. | [optional] 

### Return type

[**GetRecipeResponse**](GetRecipeResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully retrieved Configuration Recipe or any failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_configuration_recipes**
> ResourceListOfGetRecipeResponse list_configuration_recipes(scope, as_at=as_at, filter=filter)

[EXPERIMENTAL] List the set of Configuration Recipes

List the set of  configuration recipes at the specified date/time and scope

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
    api_instance = lusid.ConfigurationRecipeApi(api_client)
    scope = 'scope_example' # str | The scope of the Configuration Recipes to list
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the Configuration Recipes. Defaults to latest if not specified. (optional)
filter = 'filter_example' # str | Expression to filter the result set.              For example, to filter on code, use \"value.code eq 'string'\"              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)

    try:
        # [EXPERIMENTAL] List the set of Configuration Recipes
        api_response = api_instance.list_configuration_recipes(scope, as_at=as_at, filter=filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationRecipeApi->list_configuration_recipes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Configuration Recipes to list | 
 **as_at** | **datetime**| The asAt datetime at which to list the Configuration Recipes. Defaults to latest if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set.              For example, to filter on code, use \&quot;value.code eq &#39;string&#39;\&quot;              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 

### Return type

[**ResourceListOfGetRecipeResponse**](ResourceListOfGetRecipeResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested configuration recipes |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_configuration_recipe**
> UpsertSingleStructuredDataResponse upsert_configuration_recipe(scope, structured_data)

[EXPERIMENTAL] Upsert a Configuration Recipe. This creates or updates the data in Lusid.

Update or insert one Configuration Recipe in a single scope. An item will be updated if it already exists  and inserted if it does not.                The response will return the successfully updated or inserted Configuration Recipe or failure message if unsuccessful                It is important to always check to verify success (or failure).

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
    api_instance = lusid.ConfigurationRecipeApi(api_client)
    scope = 'scope_example' # str | The scope to use when updating or inserting the Configuration Recipe.
structured_data = lusid.UpsertRecipeRequest() # UpsertRecipeRequest | The Configuration Recipe to update or insert

    try:
        # [EXPERIMENTAL] Upsert a Configuration Recipe. This creates or updates the data in Lusid.
        api_response = api_instance.upsert_configuration_recipe(scope, structured_data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationRecipeApi->upsert_configuration_recipe: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope to use when updating or inserting the Configuration Recipe. | 
 **structured_data** | [**UpsertRecipeRequest**](UpsertRecipeRequest.md)| The Configuration Recipe to update or insert | 

### Return type

[**UpsertSingleStructuredDataResponse**](UpsertSingleStructuredDataResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully updated or inserted item or any failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

