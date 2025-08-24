# lusid.PropertyDefinitionsApi

All URIs are relative to *https://fbn-prd.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_derived_property_definition**](PropertyDefinitionsApi.md#create_derived_property_definition) | **POST** /api/propertydefinitions/derived | [EARLY ACCESS] CreateDerivedPropertyDefinition: Create derived property definition
[**create_property_definition**](PropertyDefinitionsApi.md#create_property_definition) | **POST** /api/propertydefinitions | CreatePropertyDefinition: Create property definition
[**delete_property_definition**](PropertyDefinitionsApi.md#delete_property_definition) | **DELETE** /api/propertydefinitions/{domain}/{scope}/{code} | DeletePropertyDefinition: Delete property definition
[**delete_property_definition_properties**](PropertyDefinitionsApi.md#delete_property_definition_properties) | **POST** /api/propertydefinitions/{domain}/{scope}/{code}/properties/$delete | [EARLY ACCESS] DeletePropertyDefinitionProperties: Delete property definition properties
[**get_multiple_property_definitions**](PropertyDefinitionsApi.md#get_multiple_property_definitions) | **GET** /api/propertydefinitions | GetMultiplePropertyDefinitions: Get multiple property definitions
[**get_property_definition**](PropertyDefinitionsApi.md#get_property_definition) | **GET** /api/propertydefinitions/{domain}/{scope}/{code} | GetPropertyDefinition: Get property definition
[**get_property_definition_property_time_series**](PropertyDefinitionsApi.md#get_property_definition_property_time_series) | **GET** /api/propertydefinitions/{domain}/{scope}/{code}/properties/time-series | [EARLY ACCESS] GetPropertyDefinitionPropertyTimeSeries: Get Property Definition Property Time Series
[**list_property_definitions**](PropertyDefinitionsApi.md#list_property_definitions) | **GET** /api/propertydefinitions/$list | ListPropertyDefinitions: List property definitions
[**update_derived_property_definition**](PropertyDefinitionsApi.md#update_derived_property_definition) | **PUT** /api/propertydefinitions/derived/{domain}/{scope}/{code} | [EARLY ACCESS] UpdateDerivedPropertyDefinition: Update a pre-existing derived property definition
[**update_property_definition**](PropertyDefinitionsApi.md#update_property_definition) | **PUT** /api/propertydefinitions/{domain}/{scope}/{code} | UpdatePropertyDefinition: Update property definition
[**upsert_property_definition_properties**](PropertyDefinitionsApi.md#upsert_property_definition_properties) | **POST** /api/propertydefinitions/{domain}/{scope}/{code}/properties | UpsertPropertyDefinitionProperties: Upsert properties to a property definition


# **create_derived_property_definition**
> PropertyDefinition create_derived_property_definition(create_derived_property_definition_request)

[EARLY ACCESS] CreateDerivedPropertyDefinition: Create derived property definition

Define a new derived property.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    PropertyDefinitionsApi
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
    api_instance = api_client_factory.build(PropertyDefinitionsApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # create_derived_property_definition_request = CreateDerivedPropertyDefinitionRequest.from_json("")
    # create_derived_property_definition_request = CreateDerivedPropertyDefinitionRequest.from_dict({})
    create_derived_property_definition_request = CreateDerivedPropertyDefinitionRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.create_derived_property_definition(create_derived_property_definition_request, opts=opts)

        # [EARLY ACCESS] CreateDerivedPropertyDefinition: Create derived property definition
        api_response = api_instance.create_derived_property_definition(create_derived_property_definition_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling PropertyDefinitionsApi->create_derived_property_definition: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_derived_property_definition_request** | [**CreateDerivedPropertyDefinitionRequest**](CreateDerivedPropertyDefinitionRequest.md)| The definition of the new derived property. | 

### Return type

[**PropertyDefinition**](PropertyDefinition.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created derived property definition |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **create_property_definition**
> PropertyDefinition create_property_definition(create_property_definition_request)

CreatePropertyDefinition: Create property definition

Define a new property.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    PropertyDefinitionsApi
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
    api_instance = api_client_factory.build(PropertyDefinitionsApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # create_property_definition_request = CreatePropertyDefinitionRequest.from_json("")
    # create_property_definition_request = CreatePropertyDefinitionRequest.from_dict({})
    create_property_definition_request = CreatePropertyDefinitionRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.create_property_definition(create_property_definition_request, opts=opts)

        # CreatePropertyDefinition: Create property definition
        api_response = api_instance.create_property_definition(create_property_definition_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling PropertyDefinitionsApi->create_property_definition: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_property_definition_request** | [**CreatePropertyDefinitionRequest**](CreatePropertyDefinitionRequest.md)| The definition of the new property. | 

### Return type

[**PropertyDefinition**](PropertyDefinition.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created property definition |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_property_definition**
> DeletedEntityResponse delete_property_definition(domain, scope, code)

DeletePropertyDefinition: Delete property definition

Delete the definition of the specified property.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    PropertyDefinitionsApi
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
    api_instance = api_client_factory.build(PropertyDefinitionsApi)
    domain = 'domain_example' # str | The domain of the property to be deleted.
    scope = 'scope_example' # str | The scope of the property to be deleted.
    code = 'code_example' # str | The code of the property to be deleted. Together with the domain and scope this uniquely              identifies the property.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_property_definition(domain, scope, code, opts=opts)

        # DeletePropertyDefinition: Delete property definition
        api_response = api_instance.delete_property_definition(domain, scope, code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling PropertyDefinitionsApi->delete_property_definition: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain of the property to be deleted. | 
 **scope** | **str**| The scope of the property to be deleted. | 
 **code** | **str**| The code of the property to be deleted. Together with the domain and scope this uniquely              identifies the property. | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The time that the property definition was deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_property_definition_properties**
> DeletedEntityResponse delete_property_definition_properties(domain, scope, code, request_body, effective_at=effective_at)

[EARLY ACCESS] DeletePropertyDefinitionProperties: Delete property definition properties

Delete one or more properties from a single property definition. If the properties are time-variant then an effective date time from which the  properties will be deleted must be specified. If the properties are perpetual then it is invalid to specify an effective date time for deletion.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    PropertyDefinitionsApi
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
    api_instance = api_client_factory.build(PropertyDefinitionsApi)
    domain = 'domain_example' # str | The domain of the property definition to delete properties from.
    scope = 'scope_example' # str | The scope of the property definition to delete properties from.
    code = 'code_example' # str | The code of the property definition to delete properties from.
    request_body = ["PropertyDefinition/MyScope/MyPropertyName","PropertyDefinition/MyScope/MyPropertyName2"] # List[str] | The property keys of the properties to delete. These must take the format              {domain}/{scope}/{code} e.g \"PropertyDefinition/myScope/someAttributeKey\". Each property must be from the \"PropertyDefinition\" domain.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to delete time-variant properties from.              The property must exist at the specified 'effectiveAt' datetime. If the 'effectiveAt' is not provided or is before              the time-variant property exists then a failure is returned. Do not specify this parameter if an of the properties to delete are perpetual. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_property_definition_properties(domain, scope, code, request_body, effective_at=effective_at, opts=opts)

        # [EARLY ACCESS] DeletePropertyDefinitionProperties: Delete property definition properties
        api_response = api_instance.delete_property_definition_properties(domain, scope, code, request_body, effective_at=effective_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling PropertyDefinitionsApi->delete_property_definition_properties: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain of the property definition to delete properties from. | 
 **scope** | **str**| The scope of the property definition to delete properties from. | 
 **code** | **str**| The code of the property definition to delete properties from. | 
 **request_body** | [**List[str]**](str.md)| The property keys of the properties to delete. These must take the format              {domain}/{scope}/{code} e.g \&quot;PropertyDefinition/myScope/someAttributeKey\&quot;. Each property must be from the \&quot;PropertyDefinition\&quot; domain. | 
 **effective_at** | **str**| The effective datetime or cut label at which to delete time-variant properties from.              The property must exist at the specified &#39;effectiveAt&#39; datetime. If the &#39;effectiveAt&#39; is not provided or is before              the time-variant property exists then a failure is returned. Do not specify this parameter if an of the properties to delete are perpetual. | [optional] 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the properties were deleted from the specified definition |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_multiple_property_definitions**
> ResourceListOfPropertyDefinition get_multiple_property_definitions(property_keys, as_at=as_at, filter=filter, effective_at=effective_at)

GetMultiplePropertyDefinitions: Get multiple property definitions

Retrieve the definition of one or more specified properties.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    PropertyDefinitionsApi
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
    api_instance = api_client_factory.build(PropertyDefinitionsApi)
    property_keys = ['property_keys_example'] # List[str] | One or more property keys which identify each property that a definition should              be retrieved for. The format for each property key is {domain}/{scope}/{code}, e.g. 'Portfolio/Manager/Id'.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the property definitions. Defaults to return              the latest version of each definition if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the result set.               For example, to filter on the Lifetime, use \"lifeTime eq 'Perpetual'\"              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to list properties attached to the Property Definition.              Defaults to the current LUSID system datetime if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_multiple_property_definitions(property_keys, as_at=as_at, filter=filter, effective_at=effective_at, opts=opts)

        # GetMultiplePropertyDefinitions: Get multiple property definitions
        api_response = api_instance.get_multiple_property_definitions(property_keys, as_at=as_at, filter=filter, effective_at=effective_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling PropertyDefinitionsApi->get_multiple_property_definitions: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_keys** | [**List[str]**](str.md)| One or more property keys which identify each property that a definition should              be retrieved for. The format for each property key is {domain}/{scope}/{code}, e.g. &#39;Portfolio/Manager/Id&#39;. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the property definitions. Defaults to return              the latest version of each definition if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set.               For example, to filter on the Lifetime, use \&quot;lifeTime eq &#39;Perpetual&#39;\&quot;              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **effective_at** | **str**| The effective datetime or cut label at which to list properties attached to the Property Definition.              Defaults to the current LUSID system datetime if not specified. | [optional] 

### Return type

[**ResourceListOfPropertyDefinition**](ResourceListOfPropertyDefinition.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested property definitions |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_property_definition**
> PropertyDefinition get_property_definition(domain, scope, code, as_at=as_at, effective_at=effective_at)

GetPropertyDefinition: Get property definition

Retrieve the definition of a specified property.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    PropertyDefinitionsApi
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
    api_instance = api_client_factory.build(PropertyDefinitionsApi)
    domain = 'domain_example' # str | The domain of the specified property.
    scope = 'scope_example' # str | The scope of the specified property.
    code = 'code_example' # str | The code of the specified property. Together with the domain and scope this uniquely              identifies the property.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the property definition. Defaults to return              the latest version of the definition if not specified. (optional)
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to list properties attached to the Property Definition.              Defaults to the current LUSID system datetime if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_property_definition(domain, scope, code, as_at=as_at, effective_at=effective_at, opts=opts)

        # GetPropertyDefinition: Get property definition
        api_response = api_instance.get_property_definition(domain, scope, code, as_at=as_at, effective_at=effective_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling PropertyDefinitionsApi->get_property_definition: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain of the specified property. | 
 **scope** | **str**| The scope of the specified property. | 
 **code** | **str**| The code of the specified property. Together with the domain and scope this uniquely              identifies the property. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the property definition. Defaults to return              the latest version of the definition if not specified. | [optional] 
 **effective_at** | **str**| The effective datetime or cut label at which to list properties attached to the Property Definition.              Defaults to the current LUSID system datetime if not specified. | [optional] 

### Return type

[**PropertyDefinition**](PropertyDefinition.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested property definition |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_property_definition_property_time_series**
> ResourceListOfPropertyInterval get_property_definition_property_time_series(domain, scope, code, property_key, as_at=as_at, filter=filter, page=page, limit=limit)

[EARLY ACCESS] GetPropertyDefinitionPropertyTimeSeries: Get Property Definition Property Time Series

List the complete time series of a property definition property.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    PropertyDefinitionsApi
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
    api_instance = api_client_factory.build(PropertyDefinitionsApi)
    domain = 'domain_example' # str | The domain of the property definition to which the property is attached
    scope = 'scope_example' # str | The scope of the property definition to which the property is attached
    code = 'code_example' # str | The code of the property definition to which the property is attached
    property_key = 'property_key_example' # str | The property key of the property whose history to show. This must be from the \"Property Definition\" domain and in the format              {domain}/{scope}/{code}, for example \"PropertyDefinition/myScope/someAttributeKey\".
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to show the history. Defaults to the current datetime if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the results. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing properties from a previous call to get property time series.              This value is returned from the previous call. If a pagination token is provided the filter and asAt fields              must not have changed since the original request. (optional)
    limit = 56 # int | When paginating, limit the number of returned results to this many. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_property_definition_property_time_series(domain, scope, code, property_key, as_at=as_at, filter=filter, page=page, limit=limit, opts=opts)

        # [EARLY ACCESS] GetPropertyDefinitionPropertyTimeSeries: Get Property Definition Property Time Series
        api_response = api_instance.get_property_definition_property_time_series(domain, scope, code, property_key, as_at=as_at, filter=filter, page=page, limit=limit)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling PropertyDefinitionsApi->get_property_definition_property_time_series: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain of the property definition to which the property is attached | 
 **scope** | **str**| The scope of the property definition to which the property is attached | 
 **code** | **str**| The code of the property definition to which the property is attached | 
 **property_key** | **str**| The property key of the property whose history to show. This must be from the \&quot;Property Definition\&quot; domain and in the format              {domain}/{scope}/{code}, for example \&quot;PropertyDefinition/myScope/someAttributeKey\&quot;. | 
 **as_at** | **datetime**| The asAt datetime at which to show the history. Defaults to the current datetime if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **page** | **str**| The pagination token to use to continue listing properties from a previous call to get property time series.              This value is returned from the previous call. If a pagination token is provided the filter and asAt fields              must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] 

### Return type

[**ResourceListOfPropertyInterval**](ResourceListOfPropertyInterval.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The time series of the property |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_property_definitions**
> PagedResourceListOfPropertyDefinition list_property_definitions(effective_at=effective_at, as_at=as_at, property_keys=property_keys, page=page, limit=limit, filter=filter, sort_by=sort_by)

ListPropertyDefinitions: List property definitions

List all the property definitions matching particular criteria.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    PropertyDefinitionsApi
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
    api_instance = api_client_factory.build(PropertyDefinitionsApi)
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to list the property definitions. Defaults to the current LUSID              system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the property definitions. Defaults to returning the latest version              of each property definition if not specified. (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the 'Property Definition' domain to decorate onto              property definitions. These must take the format              {domain}/{scope}/{code} e.g \"PropertyDefinition/myScope/someAttributeKey\". Each property must be from the \"PropertyDefinition\" domain. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing property definitions; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. (optional)
    limit = 56 # int | When paginating, limit the results to this number. Defaults to 100 if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the results.              For example, to filter on the display name, specify \"DisplayName eq 'DisplayName'\". For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. (optional)
    sort_by = ['sort_by_example'] # List[str] | A list of field names or properties to sort by, each suffixed by \" ASC\" or \" DESC\" (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_property_definitions(effective_at=effective_at, as_at=as_at, property_keys=property_keys, page=page, limit=limit, filter=filter, sort_by=sort_by, opts=opts)

        # ListPropertyDefinitions: List property definitions
        api_response = api_instance.list_property_definitions(effective_at=effective_at, as_at=as_at, property_keys=property_keys, page=page, limit=limit, filter=filter, sort_by=sort_by)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling PropertyDefinitionsApi->list_property_definitions: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **effective_at** | **str**| The effective datetime or cut label at which to list the property definitions. Defaults to the current LUSID              system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the property definitions. Defaults to returning the latest version              of each property definition if not specified. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;Property Definition&#39; domain to decorate onto              property definitions. These must take the format              {domain}/{scope}/{code} e.g \&quot;PropertyDefinition/myScope/someAttributeKey\&quot;. Each property must be from the \&quot;PropertyDefinition\&quot; domain. | [optional] 
 **page** | **str**| The pagination token to use to continue listing property definitions; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results.              For example, to filter on the display name, specify \&quot;DisplayName eq &#39;DisplayName&#39;\&quot;. For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot; | [optional] 

### Return type

[**PagedResourceListOfPropertyDefinition**](PagedResourceListOfPropertyDefinition.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested property definitions |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **update_derived_property_definition**
> PropertyDefinition update_derived_property_definition(domain, scope, code, update_derived_property_definition_request)

[EARLY ACCESS] UpdateDerivedPropertyDefinition: Update a pre-existing derived property definition

This will fail if the property definition does not exist

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    PropertyDefinitionsApi
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
    api_instance = api_client_factory.build(PropertyDefinitionsApi)
    domain = 'domain_example' # str | Domain of the property definition
    scope = 'scope_example' # str | Scope of the property definition
    code = 'code_example' # str | Code of the property definition

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # update_derived_property_definition_request = UpdateDerivedPropertyDefinitionRequest.from_json("")
    # update_derived_property_definition_request = UpdateDerivedPropertyDefinitionRequest.from_dict({})
    update_derived_property_definition_request = UpdateDerivedPropertyDefinitionRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.update_derived_property_definition(domain, scope, code, update_derived_property_definition_request, opts=opts)

        # [EARLY ACCESS] UpdateDerivedPropertyDefinition: Update a pre-existing derived property definition
        api_response = api_instance.update_derived_property_definition(domain, scope, code, update_derived_property_definition_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling PropertyDefinitionsApi->update_derived_property_definition: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain of the property definition | 
 **scope** | **str**| Scope of the property definition | 
 **code** | **str**| Code of the property definition | 
 **update_derived_property_definition_request** | [**UpdateDerivedPropertyDefinitionRequest**](UpdateDerivedPropertyDefinitionRequest.md)| Information about the derived property definition being updated | 

### Return type

[**PropertyDefinition**](PropertyDefinition.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated derived property definition |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **update_property_definition**
> PropertyDefinition update_property_definition(domain, scope, code, update_property_definition_request)

UpdatePropertyDefinition: Update property definition

Update the definition of a specified existing property. Not all elements within a property definition  are modifiable due to the potential implications for values already stored against the property.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    PropertyDefinitionsApi
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
    api_instance = api_client_factory.build(PropertyDefinitionsApi)
    domain = 'domain_example' # str | The domain of the property being updated.
    scope = 'scope_example' # str | The scope of the property being updated.
    code = 'code_example' # str | The code of the property being updated. Together with the domain and scope this uniquely              identifies the property.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # update_property_definition_request = UpdatePropertyDefinitionRequest.from_json("")
    # update_property_definition_request = UpdatePropertyDefinitionRequest.from_dict({})
    update_property_definition_request = UpdatePropertyDefinitionRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.update_property_definition(domain, scope, code, update_property_definition_request, opts=opts)

        # UpdatePropertyDefinition: Update property definition
        api_response = api_instance.update_property_definition(domain, scope, code, update_property_definition_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling PropertyDefinitionsApi->update_property_definition: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain of the property being updated. | 
 **scope** | **str**| The scope of the property being updated. | 
 **code** | **str**| The code of the property being updated. Together with the domain and scope this uniquely              identifies the property. | 
 **update_property_definition_request** | [**UpdatePropertyDefinitionRequest**](UpdatePropertyDefinitionRequest.md)| The updated definition of the property. | 

### Return type

[**PropertyDefinition**](PropertyDefinition.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated property definition |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **upsert_property_definition_properties**
> BatchUpsertPropertyDefinitionPropertiesResponse upsert_property_definition_properties(domain, scope, code, request_body, success_mode=success_mode)

UpsertPropertyDefinitionProperties: Upsert properties to a property definition

Create or update properties for a particular property definition

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    PropertyDefinitionsApi
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
    api_instance = api_client_factory.build(PropertyDefinitionsApi)
    domain = 'domain_example' # str | The domain of the specified property.
    scope = 'scope_example' # str | The scope of the specified property.
    code = 'code_example' # str | The code of the specified property. Together with the domain and scope this uniquely
    request_body = {"PropertyDefinition/MyScope/FundManagerName":{"key":"PropertyDefinition/MyScope/FundManagerName","value":{"labelValue":"Smith"},"effectiveFrom":"2018-03-05T00:00:00.0000000+00:00"},"PropertyDefinition/MyScope/SomeProperty":{"key":"PropertyDefinition/MyScope/SomeProperty","value":{"labelValue":"SomeValue"},"effectiveFrom":"2016-01-01T00:00:00.0000000+00:00"},"PropertyDefinition/MyScope/AnotherProperty":{"key":"PropertyDefinition/MyScope/AnotherProperty","value":{"labelValue":"AnotherValue"},"effectiveFrom":"2018-03-05T00:00:00.0000000+00:00","effectiveUntil":"2020-01-01T00:00:00.0000000+00:00"},"PropertyDefinition/MyScope/ReBalanceInterval":{"key":"PropertyDefinition/MyScope/ReBalanceInterval","value":{"metricValue":{"value":30,"unit":"Days"}}}} # Dict[str, ModelProperty] | The properties to be created or updated. Each property in              the request must be keyed by its unique property key. This has the format {domain}/{scope}/{code}, for example              'PropertyDefinition/Manager/Id'.
    success_mode = 'Partial' # str | Whether the batch request should fail Atomically or in a Partial fashion - Allowed Values: Atomic, Partial. (optional) (default to 'Partial')

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.upsert_property_definition_properties(domain, scope, code, request_body, success_mode=success_mode, opts=opts)

        # UpsertPropertyDefinitionProperties: Upsert properties to a property definition
        api_response = api_instance.upsert_property_definition_properties(domain, scope, code, request_body, success_mode=success_mode)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling PropertyDefinitionsApi->upsert_property_definition_properties: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain of the specified property. | 
 **scope** | **str**| The scope of the specified property. | 
 **code** | **str**| The code of the specified property. Together with the domain and scope this uniquely | 
 **request_body** | [**Dict[str, ModelProperty]**](ModelProperty.md)| The properties to be created or updated. Each property in              the request must be keyed by its unique property key. This has the format {domain}/{scope}/{code}, for example              &#39;PropertyDefinition/Manager/Id&#39;. | 
 **success_mode** | **str**| Whether the batch request should fail Atomically or in a Partial fashion - Allowed Values: Atomic, Partial. | [optional] [default to &#39;Partial&#39;]

### Return type

[**BatchUpsertPropertyDefinitionPropertiesResponse**](BatchUpsertPropertyDefinitionPropertiesResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The asAt datetime at which the properties were updated or created. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

