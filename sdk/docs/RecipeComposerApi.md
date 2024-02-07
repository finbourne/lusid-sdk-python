# lusid.RecipeComposerApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_recipe_composer**](RecipeComposerApi.md#delete_recipe_composer) | **DELETE** /api/recipecomposers/{scope}/{code} | [EXPERIMENTAL] DeleteRecipeComposer: Delete a Recipe Composer, assuming that it is present.
[**get_recipe_composer**](RecipeComposerApi.md#get_recipe_composer) | **GET** /api/recipecomposers/{scope}/{code} | [EXPERIMENTAL] GetRecipeComposer: Get Recipe Composer
[**get_recipe_composer_resolved_inline**](RecipeComposerApi.md#get_recipe_composer_resolved_inline) | **POST** /api/recipecomposers/inline | [EXPERIMENTAL] GetRecipeComposerResolvedInline: Given a Recipe Composer, this endpoint shows what configuration recipe it would resolve to, able to access the already upserted configuration recipes as well as plain inline string inputs.
[**list_recipe_composers**](RecipeComposerApi.md#list_recipe_composers) | **GET** /api/recipecomposers | [EXPERIMENTAL] ListRecipeComposers: List the set of Recipe Composers
[**upsert_recipe_composer**](RecipeComposerApi.md#upsert_recipe_composer) | **POST** /api/recipecomposers | [EXPERIMENTAL] UpsertRecipeComposer: Upsert a Recipe Composer. This creates or updates the data in Lusid.


# **delete_recipe_composer**
> AnnulSingleStructuredDataResponse delete_recipe_composer(scope, code)

[EXPERIMENTAL] DeleteRecipeComposer: Delete a Recipe Composer, assuming that it is present.

Delete the specified Recipe Composer from a single scope.                The response will return either detail of the deleted item, or an explanation (failure) as to why this did not succeed.                It is important to always check for any unsuccessful response.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from lusid.models.annul_single_structured_data_response import AnnulSingleStructuredDataResponse
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
    api_instance = api_client_factory.build(lusid.RecipeComposerApi)
    scope = 'scope_example' # str | The scope of the Recipe Composer to delete.
    code = 'code_example' # str | The Recipe Composer to delete.

    try:
        # [EXPERIMENTAL] DeleteRecipeComposer: Delete a Recipe Composer, assuming that it is present.
        api_response = await api_instance.delete_recipe_composer(scope, code)
        print("The response of RecipeComposerApi->delete_recipe_composer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecipeComposerApi->delete_recipe_composer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Recipe Composer to delete. | 
 **code** | **str**| The Recipe Composer to delete. | 

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

# **get_recipe_composer**
> GetRecipeComposerResponse get_recipe_composer(scope, code, as_at=as_at)

[EXPERIMENTAL] GetRecipeComposer: Get Recipe Composer

Get a Recipe Composer from a single scope.                The response will return either the recipe composer that has been stored, or a failure explaining why the request was unsuccessful.                It is important to always check for any unsuccessful requests (failures).

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from lusid.models.get_recipe_composer_response import GetRecipeComposerResponse
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
    api_instance = api_client_factory.build(lusid.RecipeComposerApi)
    scope = 'scope_example' # str | The scope of the Recipe Composer to retrieve.
    code = 'code_example' # str | The name of the Recipe Composer to retrieve the data for.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Recipe Composer. Defaults to return the latest version if not specified. (optional)

    try:
        # [EXPERIMENTAL] GetRecipeComposer: Get Recipe Composer
        api_response = await api_instance.get_recipe_composer(scope, code, as_at=as_at)
        print("The response of RecipeComposerApi->get_recipe_composer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecipeComposerApi->get_recipe_composer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Recipe Composer to retrieve. | 
 **code** | **str**| The name of the Recipe Composer to retrieve the data for. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Recipe Composer. Defaults to return the latest version if not specified. | [optional] 

### Return type

[**GetRecipeComposerResponse**](GetRecipeComposerResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully retrieved Recipe Composer or any failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recipe_composer_resolved_inline**
> GetRecipeResponse get_recipe_composer_resolved_inline(upsert_recipe_composer_request)

[EXPERIMENTAL] GetRecipeComposerResolvedInline: Given a Recipe Composer, this endpoint shows what configuration recipe it would resolve to, able to access the already upserted configuration recipes as well as plain inline string inputs.

Resolves an inline recipe composer into a ConfigurationRecipe.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from lusid.models.get_recipe_response import GetRecipeResponse
from lusid.models.upsert_recipe_composer_request import UpsertRecipeComposerRequest
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
    api_instance = api_client_factory.build(lusid.RecipeComposerApi)
    upsert_recipe_composer_request = {"recipeComposer":{"scope":"someScope","code":"someCode","operations":[{"value":{"fromRecipe":{"scope":"someRecipeScope","code":"SomeRecipeCode"}},"path":".","op":"Insert"},{"value":{"asString":"SimpleStatic"},"path":"Pricing.ModelRules.[*].ModelName","op":"Update"}]}} # UpsertRecipeComposerRequest | Recipe composer used to resolve into the Configuration Recipe.

    try:
        # [EXPERIMENTAL] GetRecipeComposerResolvedInline: Given a Recipe Composer, this endpoint shows what configuration recipe it would resolve to, able to access the already upserted configuration recipes as well as plain inline string inputs.
        api_response = await api_instance.get_recipe_composer_resolved_inline(upsert_recipe_composer_request)
        print("The response of RecipeComposerApi->get_recipe_composer_resolved_inline:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecipeComposerApi->get_recipe_composer_resolved_inline: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_recipe_composer_request** | [**UpsertRecipeComposerRequest**](UpsertRecipeComposerRequest.md)| Recipe composer used to resolve into the Configuration Recipe. | 

### Return type

[**GetRecipeResponse**](GetRecipeResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully resolved Configuration Recipe. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_recipe_composers**
> ResourceListOfGetRecipeComposerResponse list_recipe_composers(as_at=as_at, filter=filter)

[EXPERIMENTAL] ListRecipeComposers: List the set of Recipe Composers

List the set of Recipe Composers at the specified date/time and scope

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from lusid.models.resource_list_of_get_recipe_composer_response import ResourceListOfGetRecipeComposerResponse
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
    api_instance = api_client_factory.build(lusid.RecipeComposerApi)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the Recipes Composers. Defaults to latest if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid. (optional)

    try:
        # [EXPERIMENTAL] ListRecipeComposers: List the set of Recipe Composers
        api_response = await api_instance.list_recipe_composers(as_at=as_at, filter=filter)
        print("The response of RecipeComposerApi->list_recipe_composers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecipeComposerApi->list_recipe_composers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list the Recipes Composers. Defaults to latest if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid. | [optional] 

### Return type

[**ResourceListOfGetRecipeComposerResponse**](ResourceListOfGetRecipeComposerResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested recipe composers |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_recipe_composer**
> UpsertSingleStructuredDataResponse upsert_recipe_composer(upsert_recipe_composer_request)

[EXPERIMENTAL] UpsertRecipeComposer: Upsert a Recipe Composer. This creates or updates the data in Lusid.

Update or insert one Recipe Composer in a single scope. An item will be updated if it already exists  and inserted if it does not.                The response will return the successfully updated or inserted Recipe Composer or failure message if unsuccessful                It is important to always check to verify success (or failure).

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid.rest import ApiException
from lusid.models.upsert_recipe_composer_request import UpsertRecipeComposerRequest
from lusid.models.upsert_single_structured_data_response import UpsertSingleStructuredDataResponse
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
    api_instance = api_client_factory.build(lusid.RecipeComposerApi)
    upsert_recipe_composer_request = {"recipeComposer":{"scope":"someScope","code":"someCode","operations":[{"value":{"fromRecipe":{"scope":"someRecipeScope","code":"SomeRecipeCode"}},"path":".","op":"Insert"},{"value":{"asString":"SimpleStatic"},"path":"Pricing.ModelRules.[*].ModelName","op":"Update"}]}} # UpsertRecipeComposerRequest | The Recipe Composer to update or insert

    try:
        # [EXPERIMENTAL] UpsertRecipeComposer: Upsert a Recipe Composer. This creates or updates the data in Lusid.
        api_response = await api_instance.upsert_recipe_composer(upsert_recipe_composer_request)
        print("The response of RecipeComposerApi->upsert_recipe_composer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecipeComposerApi->upsert_recipe_composer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_recipe_composer_request** | [**UpsertRecipeComposerRequest**](UpsertRecipeComposerRequest.md)| The Recipe Composer to update or insert | 

### Return type

[**UpsertSingleStructuredDataResponse**](UpsertSingleStructuredDataResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully updated or inserted item or any failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

