# lusid.ScenariosApi

All URIs are relative to *https://fbn-prd.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_scenario_from_template**](ScenariosApi.md#create_scenario_from_template) | **POST** /api/scenarios/{scope}/$fromTemplate | [EARLY ACCESS] CreateScenarioFromTemplate: [EARLY ACCESS] CreateScenarioFromTemplate: Create a Scenario from a pre-built template.
[**delete_scenario**](ScenariosApi.md#delete_scenario) | **DELETE** /api/scenarios/{scope}/{code} | [EARLY ACCESS] DeleteScenario: Delete a Scenario, assuming that it is present.
[**get_scenario**](ScenariosApi.md#get_scenario) | **GET** /api/scenarios/{scope}/{code} | [EARLY ACCESS] GetScenario: Get Scenario
[**list_scenario_templates**](ScenariosApi.md#list_scenario_templates) | **GET** /api/scenarios/$templates | [EARLY ACCESS] ListScenarioTemplates: [EARLY ACCESS] ListScenarioTemplates: List the pre-built scenario templates.
[**list_scenario_versions**](ScenariosApi.md#list_scenario_versions) | **GET** /api/scenarios/{scope}/{code}/versions | [EARLY ACCESS] ListScenarioVersions: List the versions of a Scenario
[**list_scenarios**](ScenariosApi.md#list_scenarios) | **GET** /api/scenarios | [EARLY ACCESS] ListScenarios: List Scenarios
[**list_scenarios_for_scope**](ScenariosApi.md#list_scenarios_for_scope) | **GET** /api/scenarios/{scope} | [EARLY ACCESS] ListScenariosForScope: List Scenarios for a scope
[**preview_scenario**](ScenariosApi.md#preview_scenario) | **POST** /api/scenarios/$preview | [EARLY ACCESS] PreviewScenario: Preview a Scenario
[**upsert_scenario**](ScenariosApi.md#upsert_scenario) | **POST** /api/scenarios | [EARLY ACCESS] UpsertScenario: Upsert a Scenario. This creates or updates the scenario definition in LUSID.


# **create_scenario_from_template**
> UpsertSingleStructuredDataResponse create_scenario_from_template(scope, create_scenario_from_template_request)

[EARLY ACCESS] CreateScenarioFromTemplate: [EARLY ACCESS] CreateScenarioFromTemplate: Create a Scenario from a pre-built template.

Creates and stores a scenario built from a pre-defined parameterised template, for example a  parallel rates shift or an equity crash. The template determines the scenario's shifts; the  parameters supply the targets (e.g. currency or instrument) and optionally override the default  shift size. The created scenario is stored in the given scope and behaves exactly like a  hand-built scenario.                Use ListScenarioTemplates to discover the available templates and, for each, the parameters it  accepts, their defaults and their units. A parameter the template does not read is rejected  rather than ignored, and parameter names are case-sensitive.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    ScenariosApi
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
    api_instance = api_client_factory.build(ScenariosApi)
    scope = 'scope_example' # str | The scope in which to create the scenario

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # create_scenario_from_template_request = CreateScenarioFromTemplateRequest.from_json("")
    # create_scenario_from_template_request = CreateScenarioFromTemplateRequest.from_dict({})
    create_scenario_from_template_request = CreateScenarioFromTemplateRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.create_scenario_from_template(scope, create_scenario_from_template_request, opts=opts)

        # [EARLY ACCESS] CreateScenarioFromTemplate: [EARLY ACCESS] CreateScenarioFromTemplate: Create a Scenario from a pre-built template.
        api_response = api_instance.create_scenario_from_template(scope, create_scenario_from_template_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ScenariosApi->create_scenario_from_template: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope in which to create the scenario | 
 **create_scenario_from_template_request** | [**CreateScenarioFromTemplateRequest**](CreateScenarioFromTemplateRequest.md)| The template, code and parameters to create the scenario from | 

### Return type

[**UpsertSingleStructuredDataResponse**](UpsertSingleStructuredDataResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully created scenario or any failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_scenario**
> AnnulSingleStructuredDataResponse delete_scenario(scope, code)

[EARLY ACCESS] DeleteScenario: Delete a Scenario, assuming that it is present.

Delete the specified Scenario definition from a single scope.                The response will return either detail of the deleted item, or an explanation (failure) as to why this did not succeed.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    ScenariosApi
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
    api_instance = api_client_factory.build(ScenariosApi)
    scope = 'scope_example' # str | The scope of the Scenario to delete.
    code = 'code_example' # str | The Scenario to delete.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_scenario(scope, code, opts=opts)

        # [EARLY ACCESS] DeleteScenario: Delete a Scenario, assuming that it is present.
        api_response = api_instance.delete_scenario(scope, code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ScenariosApi->delete_scenario: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Scenario to delete. | 
 **code** | **str**| The Scenario to delete. | 

### Return type

[**AnnulSingleStructuredDataResponse**](AnnulSingleStructuredDataResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The AsAt of deletion or failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_scenario**
> GetScenarioResponse get_scenario(scope, code, as_at=as_at)

[EARLY ACCESS] GetScenario: Get Scenario

Get a Scenario definition from a single scope.                The response will return either the scenario that has been stored, or a failure explaining why the request was unsuccessful.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    ScenariosApi
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
    api_instance = api_client_factory.build(ScenariosApi)
    scope = 'scope_example' # str | The scope of the Scenario to retrieve.
    code = 'code_example' # str | The code of the Scenario to retrieve.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Scenario. Defaults to return the latest version if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_scenario(scope, code, as_at=as_at, opts=opts)

        # [EARLY ACCESS] GetScenario: Get Scenario
        api_response = api_instance.get_scenario(scope, code, as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ScenariosApi->get_scenario: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Scenario to retrieve. | 
 **code** | **str**| The code of the Scenario to retrieve. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Scenario. Defaults to return the latest version if not specified. | [optional] 

### Return type

[**GetScenarioResponse**](GetScenarioResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully retrieved Scenario |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_scenario_templates**
> ResourceListOfScenarioTemplateDefinition list_scenario_templates()

[EARLY ACCESS] ListScenarioTemplates: [EARLY ACCESS] ListScenarioTemplates: List the pre-built scenario templates.

Lists every template CreateScenarioFromTemplate accepts, with each template's parameters: the  parameter's name (case-sensitive), whether it is required, what it means, the default used when  it is omitted and the unit a numeric value is read in. The units differ between templates -  basis points, percentage points or a fraction - so read them per template rather than assuming  one convention. The list is static application metadata: it does not vary by tenant, scope or  date, so the endpoint takes no parameters.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    ScenariosApi
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
    api_instance = api_client_factory.build(ScenariosApi)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_scenario_templates(opts=opts)

        # [EARLY ACCESS] ListScenarioTemplates: [EARLY ACCESS] ListScenarioTemplates: List the pre-built scenario templates.
        api_response = api_instance.list_scenario_templates()
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ScenariosApi->list_scenario_templates: %s\n" % e)

main()
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResourceListOfScenarioTemplateDefinition**](ResourceListOfScenarioTemplateDefinition.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The available scenario templates |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_scenario_versions**
> PagedResourceListOfVersion list_scenario_versions(scope, code, as_at=as_at, limit=limit, page=page)

[EARLY ACCESS] ListScenarioVersions: List the versions of a Scenario

List the AsAt versions of a single Scenario definition, newest first: one entry per change,  with the version number, the AsAt datetime it was written, and the user that wrote it.                Scenarios are perpetual (AsAt-only), so a version's AsAt datetime identifies it completely:  pass it as the asAt on GetScenario to view that version, or as the scenario reference's  asAt on a valuation to price under it.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    ScenariosApi
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
    api_instance = api_client_factory.build(ScenariosApi)
    scope = 'scope_example' # str | The scope of the Scenario to list versions for.
    code = 'code_example' # str | The code of the Scenario to list versions for.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime to cap the version history at. Defaults to all versions up to now. (optional)
    limit = 56 # int | Maximum number of results to return. Defaults to 100. (optional)
    page = 'page_example' # str | Pagination token from a previous result to fetch the next page. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_scenario_versions(scope, code, as_at=as_at, limit=limit, page=page, opts=opts)

        # [EARLY ACCESS] ListScenarioVersions: List the versions of a Scenario
        api_response = api_instance.list_scenario_versions(scope, code, as_at=as_at, limit=limit, page=page)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ScenariosApi->list_scenario_versions: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Scenario to list versions for. | 
 **code** | **str**| The code of the Scenario to list versions for. | 
 **as_at** | **datetime**| The asAt datetime to cap the version history at. Defaults to all versions up to now. | [optional] 
 **limit** | **int**| Maximum number of results to return. Defaults to 100. | [optional] 
 **page** | **str**| Pagination token from a previous result to fetch the next page. | [optional] 

### Return type

[**PagedResourceListOfVersion**](PagedResourceListOfVersion.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The versions of the scenario, newest first |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_scenarios**
> PagedResourceListOfGetScenarioResponse list_scenarios(as_at=as_at, filter=filter, limit=limit, page=page)

[EARLY ACCESS] ListScenarios: List Scenarios

List scenario definitions across all scopes at the specified date/time. Each item carries  its scope and code. Scenarios the caller is not entitled to read are omitted.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    ScenariosApi
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
    api_instance = api_client_factory.build(ScenariosApi)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the scenarios. Defaults to latest if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the result set, e.g. \"scope eq 'MyScope'\". (optional)
    limit = 56 # int | Maximum number of results to return. Defaults to 100. (optional)
    page = 'page_example' # str | Pagination token from a previous result to fetch the next page. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_scenarios(as_at=as_at, filter=filter, limit=limit, page=page, opts=opts)

        # [EARLY ACCESS] ListScenarios: List Scenarios
        api_response = api_instance.list_scenarios(as_at=as_at, filter=filter, limit=limit, page=page)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ScenariosApi->list_scenarios: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list the scenarios. Defaults to latest if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set, e.g. \&quot;scope eq &#39;MyScope&#39;\&quot;. | [optional] 
 **limit** | **int**| Maximum number of results to return. Defaults to 100. | [optional] 
 **page** | **str**| Pagination token from a previous result to fetch the next page. | [optional] 

### Return type

[**PagedResourceListOfGetScenarioResponse**](PagedResourceListOfGetScenarioResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested scenarios |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_scenarios_for_scope**
> PagedResourceListOfGetScenarioResponse list_scenarios_for_scope(scope, as_at=as_at, filter=filter, limit=limit, page=page)

[EARLY ACCESS] ListScenariosForScope: List Scenarios for a scope

List the set of scenario definitions in a single scope at the specified date/time.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    ScenariosApi
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
    api_instance = api_client_factory.build(ScenariosApi)
    scope = 'scope_example' # str | The scope to list scenarios for.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the scenarios. Defaults to latest if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the result set. (optional)
    limit = 56 # int | Maximum number of results to return. Defaults to 100. (optional)
    page = 'page_example' # str | Pagination token from a previous result to fetch the next page. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_scenarios_for_scope(scope, as_at=as_at, filter=filter, limit=limit, page=page, opts=opts)

        # [EARLY ACCESS] ListScenariosForScope: List Scenarios for a scope
        api_response = api_instance.list_scenarios_for_scope(scope, as_at=as_at, filter=filter, limit=limit, page=page)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ScenariosApi->list_scenarios_for_scope: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope to list scenarios for. | 
 **as_at** | **datetime**| The asAt datetime at which to list the scenarios. Defaults to latest if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set. | [optional] 
 **limit** | **int**| Maximum number of results to return. Defaults to 100. | [optional] 
 **page** | **str**| Pagination token from a previous result to fetch the next page. | [optional] 

### Return type

[**PagedResourceListOfGetScenarioResponse**](PagedResourceListOfGetScenarioResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested scenarios |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **preview_scenario**
> ScenarioPreviewResponse preview_scenario(scenario_preview_request)

[EARLY ACCESS] PreviewScenario: Preview a Scenario

Preview what a scenario would do to a portfolio's market data, without running a valuation.                The portfolio's market data dependencies are resolved through the given recipe and the scenario's  shifts are applied; the response lists every market data target the shifts changed, with values  before and after, plus any market data that matched a shift but could not honour it. Supply  either a reference to a stored scenario, or inline shift definitions to test a definition before  saving it.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    ScenariosApi
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
    api_instance = api_client_factory.build(ScenariosApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # scenario_preview_request = ScenarioPreviewRequest.from_json("")
    # scenario_preview_request = ScenarioPreviewRequest.from_dict({})
    scenario_preview_request = ScenarioPreviewRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.preview_scenario(scenario_preview_request, opts=opts)

        # [EARLY ACCESS] PreviewScenario: Preview a Scenario
        api_response = api_instance.preview_scenario(scenario_preview_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ScenariosApi->preview_scenario: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scenario_preview_request** | [**ScenarioPreviewRequest**](ScenarioPreviewRequest.md)| The recipe, portfolios, effective date and scenario (stored reference or inline shifts) to preview | 

### Return type

[**ScenarioPreviewResponse**](ScenarioPreviewResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The preview of the scenario&#39;s effect on the portfolio&#39;s market data, or any failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **upsert_scenario**
> UpsertSingleStructuredDataResponse upsert_scenario(upsert_scenario_request)

[EARLY ACCESS] UpsertScenario: Upsert a Scenario. This creates or updates the scenario definition in LUSID.

Update or insert one Scenario definition. An item will be updated if it already exists  and inserted if it does not.                The response will return the successfully updated or inserted scenario or failure message if unsuccessful.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    ScenariosApi
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
    api_instance = api_client_factory.build(ScenariosApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # upsert_scenario_request = UpsertScenarioRequest.from_json("")
    # upsert_scenario_request = UpsertScenarioRequest.from_dict({})
    upsert_scenario_request = UpsertScenarioRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.upsert_scenario(upsert_scenario_request, opts=opts)

        # [EARLY ACCESS] UpsertScenario: Upsert a Scenario. This creates or updates the scenario definition in LUSID.
        api_response = api_instance.upsert_scenario(upsert_scenario_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ScenariosApi->upsert_scenario: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_scenario_request** | [**UpsertScenarioRequest**](UpsertScenarioRequest.md)| The Scenario to update or insert | 

### Return type

[**UpsertSingleStructuredDataResponse**](UpsertSingleStructuredDataResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully updated or inserted item or any failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

