# lusid.DeemedDisposalDefinitionsApi

All URIs are relative to *https://fbn-prd.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_deemed_disposal_definition**](DeemedDisposalDefinitionsApi.md#create_deemed_disposal_definition) | **POST** /api/deemeddisposaldefinitions/{scope} | [EXPERIMENTAL] CreateDeemedDisposalDefinition: Create a Deemed Disposal Definition.
[**delete_deemed_disposal_definition**](DeemedDisposalDefinitionsApi.md#delete_deemed_disposal_definition) | **DELETE** /api/deemeddisposaldefinitions/{scope}/{code} | [EXPERIMENTAL] DeleteDeemedDisposalDefinition: Delete a Deemed Disposal Definition.
[**get_deemed_disposal_definition**](DeemedDisposalDefinitionsApi.md#get_deemed_disposal_definition) | **GET** /api/deemeddisposaldefinitions/{scope}/{code} | [EXPERIMENTAL] GetDeemedDisposalDefinition: Get a Deemed Disposal Definition.
[**list_deemed_disposal_definitions**](DeemedDisposalDefinitionsApi.md#list_deemed_disposal_definitions) | **GET** /api/deemeddisposaldefinitions | [EXPERIMENTAL] ListDeemedDisposalDefinitions: List Deemed Disposal Definitions.
[**update_deemed_disposal_definition**](DeemedDisposalDefinitionsApi.md#update_deemed_disposal_definition) | **PUT** /api/deemeddisposaldefinitions/{scope}/{code} | [EXPERIMENTAL] UpdateDeemedDisposalDefinition: Update a Deemed Disposal Definition.


# **create_deemed_disposal_definition**
> DeemedDisposalDefinition create_deemed_disposal_definition(scope, deemed_disposal_definition_request)

[EXPERIMENTAL] CreateDeemedDisposalDefinition: Create a Deemed Disposal Definition.

Create a Deemed Disposal Definition whose filter selects the holdings a valuation point deems disposed of  and re-acquired at market value. The filter must be a valid holdings filter.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    DeemedDisposalDefinitionsApi
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
    api_instance = api_client_factory.build(DeemedDisposalDefinitionsApi)
    scope = 'scope_example' # str | The scope of the Deemed Disposal Definition.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # deemed_disposal_definition_request = DeemedDisposalDefinitionRequest.from_json("")
    # deemed_disposal_definition_request = DeemedDisposalDefinitionRequest.from_dict({})
    deemed_disposal_definition_request = DeemedDisposalDefinitionRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.create_deemed_disposal_definition(scope, deemed_disposal_definition_request, opts=opts)

        # [EXPERIMENTAL] CreateDeemedDisposalDefinition: Create a Deemed Disposal Definition.
        api_response = api_instance.create_deemed_disposal_definition(scope, deemed_disposal_definition_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling DeemedDisposalDefinitionsApi->create_deemed_disposal_definition: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Deemed Disposal Definition. | 
 **deemed_disposal_definition_request** | [**DeemedDisposalDefinitionRequest**](DeemedDisposalDefinitionRequest.md)| The contents of the Deemed Disposal Definition. | 

### Return type

[**DeemedDisposalDefinition**](DeemedDisposalDefinition.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created Deemed Disposal Definition. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_deemed_disposal_definition**
> DeletedEntityResponse delete_deemed_disposal_definition(scope, code)

[EXPERIMENTAL] DeleteDeemedDisposalDefinition: Delete a Deemed Disposal Definition.

Delete the given Deemed Disposal Definition. A definition that is applied by a valuation point cannot be deleted.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    DeemedDisposalDefinitionsApi
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
    api_instance = api_client_factory.build(DeemedDisposalDefinitionsApi)
    scope = 'scope_example' # str | The scope of the Deemed Disposal Definition to be deleted.
    code = 'code_example' # str | The code of the Deemed Disposal Definition to be deleted. Together with the scope this uniquely identifies the Deemed Disposal Definition.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_deemed_disposal_definition(scope, code, opts=opts)

        # [EXPERIMENTAL] DeleteDeemedDisposalDefinition: Delete a Deemed Disposal Definition.
        api_response = api_instance.delete_deemed_disposal_definition(scope, code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling DeemedDisposalDefinitionsApi->delete_deemed_disposal_definition: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Deemed Disposal Definition to be deleted. | 
 **code** | **str**| The code of the Deemed Disposal Definition to be deleted. Together with the scope this uniquely identifies the Deemed Disposal Definition. | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the Deemed Disposal Definition was deleted. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_deemed_disposal_definition**
> DeemedDisposalDefinition get_deemed_disposal_definition(scope, code, as_at=as_at)

[EXPERIMENTAL] GetDeemedDisposalDefinition: Get a Deemed Disposal Definition.

Retrieve the definition of a particular Deemed Disposal Definition.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    DeemedDisposalDefinitionsApi
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
    api_instance = api_client_factory.build(DeemedDisposalDefinitionsApi)
    scope = 'scope_example' # str | The scope of the Deemed Disposal Definition.
    code = 'code_example' # str | The code of the Deemed Disposal Definition. Together with the scope this uniquely identifies the Deemed Disposal Definition.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Deemed Disposal Definition. Defaults to returning the latest version if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_deemed_disposal_definition(scope, code, as_at=as_at, opts=opts)

        # [EXPERIMENTAL] GetDeemedDisposalDefinition: Get a Deemed Disposal Definition.
        api_response = api_instance.get_deemed_disposal_definition(scope, code, as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling DeemedDisposalDefinitionsApi->get_deemed_disposal_definition: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Deemed Disposal Definition. | 
 **code** | **str**| The code of the Deemed Disposal Definition. Together with the scope this uniquely identifies the Deemed Disposal Definition. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Deemed Disposal Definition. Defaults to returning the latest version if not specified. | [optional] 

### Return type

[**DeemedDisposalDefinition**](DeemedDisposalDefinition.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Deemed Disposal Definition. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_deemed_disposal_definitions**
> PagedResourceListOfDeemedDisposalDefinition list_deemed_disposal_definitions(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)

[EXPERIMENTAL] ListDeemedDisposalDefinitions: List Deemed Disposal Definitions.

List all the Deemed Disposal Definitions matching particular criteria.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    DeemedDisposalDefinitionsApi
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
    api_instance = api_client_factory.build(DeemedDisposalDefinitionsApi)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the Deemed Disposal Definitions. Defaults to returning the latest version of each if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing Deemed Disposal Definitions; this              value is returned from the previous call. If a pagination token is provided, the filter and asAt fields              must not have changed since the original request. (optional)
    limit = 56 # int | When paginating, limit the results to this number. Defaults to 100 if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the results.              For example, to filter on the code, specify \"id.Code eq 'Definition1'\". For more information about filtering              results, see https://support.lusid.com/docs/filtering-information-retrieved-from-lusid. (optional)
    sort_by = ['sort_by_example'] # List[str] | A list of field names to sort by, each suffixed by \" ASC\" or \" DESC\". (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_deemed_disposal_definitions(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, opts=opts)

        # [EXPERIMENTAL] ListDeemedDisposalDefinitions: List Deemed Disposal Definitions.
        api_response = api_instance.list_deemed_disposal_definitions(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling DeemedDisposalDefinitionsApi->list_deemed_disposal_definitions: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list the Deemed Disposal Definitions. Defaults to returning the latest version of each if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing Deemed Disposal Definitions; this              value is returned from the previous call. If a pagination token is provided, the filter and asAt fields              must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results.              For example, to filter on the code, specify \&quot;id.Code eq &#39;Definition1&#39;\&quot;. For more information about filtering              results, see https://support.lusid.com/docs/filtering-information-retrieved-from-lusid. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 

### Return type

[**PagedResourceListOfDeemedDisposalDefinition**](PagedResourceListOfDeemedDisposalDefinition.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Deemed Disposal Definitions. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **update_deemed_disposal_definition**
> DeemedDisposalDefinition update_deemed_disposal_definition(scope, code, update_deemed_disposal_definition_request)

[EXPERIMENTAL] UpdateDeemedDisposalDefinition: Update a Deemed Disposal Definition.

Replace the display name, description and filter of an existing Deemed Disposal Definition, creating a new  version. The filter must be a valid holdings filter.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    DeemedDisposalDefinitionsApi
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
    api_instance = api_client_factory.build(DeemedDisposalDefinitionsApi)
    scope = 'scope_example' # str | The scope of the Deemed Disposal Definition.
    code = 'code_example' # str | The code of the Deemed Disposal Definition. Together with the scope this uniquely identifies the Deemed Disposal Definition.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # update_deemed_disposal_definition_request = UpdateDeemedDisposalDefinitionRequest.from_json("")
    # update_deemed_disposal_definition_request = UpdateDeemedDisposalDefinitionRequest.from_dict({})
    update_deemed_disposal_definition_request = UpdateDeemedDisposalDefinitionRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.update_deemed_disposal_definition(scope, code, update_deemed_disposal_definition_request, opts=opts)

        # [EXPERIMENTAL] UpdateDeemedDisposalDefinition: Update a Deemed Disposal Definition.
        api_response = api_instance.update_deemed_disposal_definition(scope, code, update_deemed_disposal_definition_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling DeemedDisposalDefinitionsApi->update_deemed_disposal_definition: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Deemed Disposal Definition. | 
 **code** | **str**| The code of the Deemed Disposal Definition. Together with the scope this uniquely identifies the Deemed Disposal Definition. | 
 **update_deemed_disposal_definition_request** | [**UpdateDeemedDisposalDefinitionRequest**](UpdateDeemedDisposalDefinitionRequest.md)| The new contents of the Deemed Disposal Definition. | 

### Return type

[**DeemedDisposalDefinition**](DeemedDisposalDefinition.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated Deemed Disposal Definition. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

