# lusid.CheckDefinitionsApi

All URIs are relative to *https://fbn-prd.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_check_definition**](CheckDefinitionsApi.md#create_check_definition) | **POST** /api/dataquality/checkdefinitions | [EXPERIMENTAL] CreateCheckDefinition: Create a Check Definition
[**delete_check_definition**](CheckDefinitionsApi.md#delete_check_definition) | **DELETE** /api/dataquality/checkdefinitions/{scope}/{code} | [EXPERIMENTAL] DeleteCheckDefinition: Deletes a particular Check Definition
[**get_check_definition**](CheckDefinitionsApi.md#get_check_definition) | **GET** /api/dataquality/checkdefinitions/{scope}/{code} | [EXPERIMENTAL] GetCheckDefinition: Get a single Check Definition by scope and code.
[**list_check_definitions**](CheckDefinitionsApi.md#list_check_definitions) | **GET** /api/dataquality/checkdefinitions | [EXPERIMENTAL] ListCheckDefinitions: List Check Definitions
[**update_check_definition**](CheckDefinitionsApi.md#update_check_definition) | **PUT** /api/dataquality/checkdefinitions/{scope}/{code} | [EXPERIMENTAL] UpdateCheckDefinition: Update Check Definition defined by scope and code


# **create_check_definition**
> CheckDefinition create_check_definition(create_check_definition_request=create_check_definition_request)

[EXPERIMENTAL] CreateCheckDefinition: Create a Check Definition

Creates a Check Definition. Returns the created Check Definition at the current effectiveAt. Note that Check Definitions are mono-temporal, however they can have Time-Variant Properties. Upserted Properties will be returned at the latest AsAt and EffectiveAt

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    CheckDefinitionsApi
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
    api_instance = api_client_factory.build(CheckDefinitionsApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # create_check_definition_request = CreateCheckDefinitionRequest.from_json("")
    # create_check_definition_request = CreateCheckDefinitionRequest.from_dict({})
    create_check_definition_request = CreateCheckDefinitionRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.create_check_definition(create_check_definition_request=create_check_definition_request, opts=opts)

        # [EXPERIMENTAL] CreateCheckDefinition: Create a Check Definition
        api_response = api_instance.create_check_definition(create_check_definition_request=create_check_definition_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling CheckDefinitionsApi->create_check_definition: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_check_definition_request** | [**CreateCheckDefinitionRequest**](CreateCheckDefinitionRequest.md)| The request containing the details of the Check Definition | [optional] 

### Return type

[**CheckDefinition**](CheckDefinition.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created Check Definition |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_check_definition**
> DeletedEntityResponse delete_check_definition(scope, code)

[EXPERIMENTAL] DeleteCheckDefinition: Deletes a particular Check Definition

The deletion will take effect from the Check Definition deletion datetime. i.e. will no longer exist at any asAt datetime after the asAt datetime of deletion.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    CheckDefinitionsApi
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
    api_instance = api_client_factory.build(CheckDefinitionsApi)
    scope = 'scope_example' # str | The scope of the specified Check Definition.
    code = 'code_example' # str | The code of the specified Check Definition. Together with the domain and scope this uniquely             identifies the Check Definition.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_check_definition(scope, code, opts=opts)

        # [EXPERIMENTAL] DeleteCheckDefinition: Deletes a particular Check Definition
        api_response = api_instance.delete_check_definition(scope, code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling CheckDefinitionsApi->delete_check_definition: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the specified Check Definition. | 
 **code** | **str**| The code of the specified Check Definition. Together with the domain and scope this uniquely             identifies the Check Definition. | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The deleted entity metadata |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_check_definition**
> CheckDefinition get_check_definition(scope, code, as_at=as_at, effective_at=effective_at, property_keys=property_keys)

[EXPERIMENTAL] GetCheckDefinition: Get a single Check Definition by scope and code.

Retrieves one Check Definition by scope and code. Check Definitions are mono-temporal. The EffectiveAt is only applied to Time-Variant Properties.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    CheckDefinitionsApi
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
    api_instance = api_client_factory.build(CheckDefinitionsApi)
    scope = 'scope_example' # str | The scope of the specified Check Definition.
    code = 'code_example' # str | The code of the specified Check Definition. Together with the scope this uniquely             identifies the Check Definition.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Check Definition definition. Defaults to return             the latest version of the definition if not specified. (optional)
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve the check definition properties.             Defaults to the current LUSID system datetime if not specified. (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the 'CheckDefinition' domain to decorate onto             the Check Definition.             These must have the format {domain}/{scope}/{code}, for example 'CheckDefinition/system/Name'. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_check_definition(scope, code, as_at=as_at, effective_at=effective_at, property_keys=property_keys, opts=opts)

        # [EXPERIMENTAL] GetCheckDefinition: Get a single Check Definition by scope and code.
        api_response = api_instance.get_check_definition(scope, code, as_at=as_at, effective_at=effective_at, property_keys=property_keys)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling CheckDefinitionsApi->get_check_definition: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the specified Check Definition. | 
 **code** | **str**| The code of the specified Check Definition. Together with the scope this uniquely             identifies the Check Definition. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Check Definition definition. Defaults to return             the latest version of the definition if not specified. | [optional] 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the check definition properties.             Defaults to the current LUSID system datetime if not specified. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;CheckDefinition&#39; domain to decorate onto             the Check Definition.             These must have the format {domain}/{scope}/{code}, for example &#39;CheckDefinition/system/Name&#39;. | [optional] 

### Return type

[**CheckDefinition**](CheckDefinition.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Check Definition |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_check_definitions**
> PagedResourceListOfCheckDefinition list_check_definitions(as_at=as_at, effective_at=effective_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)

[EXPERIMENTAL] ListCheckDefinitions: List Check Definitions

List all the Check Definitions matching a particular criteria.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    CheckDefinitionsApi
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
    api_instance = api_client_factory.build(CheckDefinitionsApi)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the Check Definitions. Defaults to returning the latest version of each Check Definition if not specified. (optional)
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to list the Check Definitions.             Note that Check Definitions are monotemporal, the effectiveAt is for Timevariant Properties on the Check Definition only.             Defaults to the current LUSID system datetime if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing Check Definitions; this             value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt             and asAt fields must not have changed since the original request. (optional)
    limit = 56 # int | When paginating, limit the results to this number. Defaults to 100 if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the results.             For example, to filter on the displayName, specify \"displayName eq 'MyCheckDefinition'\". For more information about filtering             results, see https://support.lusid.com/knowledgebase/article/KA-01914. (optional)
    sort_by = ['sort_by_example'] # List[str] | A list of field names or properties to sort by, each suffixed by \" ASC\" or \" DESC\" (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the 'CheckDefinition' domain to decorate onto each Check Definition.             These must take the format {domain}/{scope}/{code}, for example 'CheckDefinition/Account/id'. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_check_definitions(as_at=as_at, effective_at=effective_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys, opts=opts)

        # [EXPERIMENTAL] ListCheckDefinitions: List Check Definitions
        api_response = api_instance.list_check_definitions(as_at=as_at, effective_at=effective_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling CheckDefinitionsApi->list_check_definitions: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list the Check Definitions. Defaults to returning the latest version of each Check Definition if not specified. | [optional] 
 **effective_at** | **str**| The effective datetime or cut label at which to list the Check Definitions.             Note that Check Definitions are monotemporal, the effectiveAt is for Timevariant Properties on the Check Definition only.             Defaults to the current LUSID system datetime if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing Check Definitions; this             value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt             and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results.             For example, to filter on the displayName, specify \&quot;displayName eq &#39;MyCheckDefinition&#39;\&quot;. For more information about filtering             results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot; | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;CheckDefinition&#39; domain to decorate onto each Check Definition.             These must take the format {domain}/{scope}/{code}, for example &#39;CheckDefinition/Account/id&#39;. | [optional] 

### Return type

[**PagedResourceListOfCheckDefinition**](PagedResourceListOfCheckDefinition.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Check Definitions. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **update_check_definition**
> CheckDefinition update_check_definition(scope, code, update_check_definition_request=update_check_definition_request)

[EXPERIMENTAL] UpdateCheckDefinition: Update Check Definition defined by scope and code

Overwrites an existing Check Definition Update request has the same required fields as Create apart from the id. Returns the updated Check Definition at the current effectiveAt. Note that Check Definitions are mono-temporal, however they can have Time-Variant Properties. Updated Properties will be returned at the latest AsAt and EffectiveAt

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    CheckDefinitionsApi
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
    api_instance = api_client_factory.build(CheckDefinitionsApi)
    scope = 'scope_example' # str | The scope of the specified Check Definition.
    code = 'code_example' # str | The code of the specified Check Definition. Together with the domain and scope this uniquely identifies the Check Definition.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # update_check_definition_request = UpdateCheckDefinitionRequest.from_json("")
    # update_check_definition_request = UpdateCheckDefinitionRequest.from_dict({})
    update_check_definition_request = UpdateCheckDefinitionRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.update_check_definition(scope, code, update_check_definition_request=update_check_definition_request, opts=opts)

        # [EXPERIMENTAL] UpdateCheckDefinition: Update Check Definition defined by scope and code
        api_response = api_instance.update_check_definition(scope, code, update_check_definition_request=update_check_definition_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling CheckDefinitionsApi->update_check_definition: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the specified Check Definition. | 
 **code** | **str**| The code of the specified Check Definition. Together with the domain and scope this uniquely identifies the Check Definition. | 
 **update_check_definition_request** | [**UpdateCheckDefinitionRequest**](UpdateCheckDefinitionRequest.md)| The request containing the updated details of the Check Definition | [optional] 

### Return type

[**CheckDefinition**](CheckDefinition.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated version of the requested Check Definition |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

