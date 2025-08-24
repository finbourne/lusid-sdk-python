# lusid.IdentifierDefinitionsApi

All URIs are relative to *https://fbn-prd.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_identifier_definition**](IdentifierDefinitionsApi.md#create_identifier_definition) | **POST** /api/identifierdefinitions | [EXPERIMENTAL] CreateIdentifierDefinition: Create an Identifier Definition
[**delete_identifier_definition**](IdentifierDefinitionsApi.md#delete_identifier_definition) | **DELETE** /api/identifierdefinitions/{domain}/{identifierScope}/{identifierType} | [EXPERIMENTAL] DeleteIdentifierDefinition: Delete a particular Identifier Definition
[**get_identifier_definition**](IdentifierDefinitionsApi.md#get_identifier_definition) | **GET** /api/identifierdefinitions/{domain}/{identifierScope}/{identifierType} | [EXPERIMENTAL] GetIdentifierDefinition: Get a single Identifier Definition
[**list_identifier_definitions**](IdentifierDefinitionsApi.md#list_identifier_definitions) | **GET** /api/identifierdefinitions | [EXPERIMENTAL] ListIdentifierDefinitions: List Identifier Definitions
[**update_identifier_definition**](IdentifierDefinitionsApi.md#update_identifier_definition) | **PUT** /api/identifierdefinitions/{domain}/{identifierScope}/{identifierType} | [EXPERIMENTAL] UpdateIdentifierDefinition: Update Identifier Definition defined by domain, identifierScope, and identifierType


# **create_identifier_definition**
> IdentifierDefinition create_identifier_definition(create_identifier_definition_request=create_identifier_definition_request)

[EXPERIMENTAL] CreateIdentifierDefinition: Create an Identifier Definition

Define a new Identifier Definition

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    IdentifierDefinitionsApi
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
    api_instance = api_client_factory.build(IdentifierDefinitionsApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # create_identifier_definition_request = CreateIdentifierDefinitionRequest.from_json("")
    # create_identifier_definition_request = CreateIdentifierDefinitionRequest.from_dict({})
    create_identifier_definition_request = CreateIdentifierDefinitionRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.create_identifier_definition(create_identifier_definition_request=create_identifier_definition_request, opts=opts)

        # [EXPERIMENTAL] CreateIdentifierDefinition: Create an Identifier Definition
        api_response = api_instance.create_identifier_definition(create_identifier_definition_request=create_identifier_definition_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling IdentifierDefinitionsApi->create_identifier_definition: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_identifier_definition_request** | [**CreateIdentifierDefinitionRequest**](CreateIdentifierDefinitionRequest.md)| The request defining the new definition | [optional] 

### Return type

[**IdentifierDefinition**](IdentifierDefinition.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created Identifier Definition |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_identifier_definition**
> DeletedEntityResponse delete_identifier_definition(domain, identifier_scope, identifier_type)

[EXPERIMENTAL] DeleteIdentifierDefinition: Delete a particular Identifier Definition

The deletion will take effect from the Identifier Definition deletion datetime.  i.e. will no longer exist at any asAt datetime after the asAt datetime of deletion.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    IdentifierDefinitionsApi
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
    api_instance = api_client_factory.build(IdentifierDefinitionsApi)
    domain = 'domain_example' # str | The type of entity to which the identifier relates
    identifier_scope = 'identifier_scope_example' # str | The scope that the identifier exists in
    identifier_type = 'identifier_type_example' # str | What the identifier represents. Together with \"domain\" and \"identifierScope\" this uniquely identifies the identifier definition

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_identifier_definition(domain, identifier_scope, identifier_type, opts=opts)

        # [EXPERIMENTAL] DeleteIdentifierDefinition: Delete a particular Identifier Definition
        api_response = api_instance.delete_identifier_definition(domain, identifier_scope, identifier_type)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling IdentifierDefinitionsApi->delete_identifier_definition: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The type of entity to which the identifier relates | 
 **identifier_scope** | **str**| The scope that the identifier exists in | 
 **identifier_type** | **str**| What the identifier represents. Together with \&quot;domain\&quot; and \&quot;identifierScope\&quot; this uniquely identifies the identifier definition | 

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

# **get_identifier_definition**
> IdentifierDefinition get_identifier_definition(domain, identifier_scope, identifier_type, as_at=as_at, effective_at=effective_at, property_keys=property_keys)

[EXPERIMENTAL] GetIdentifierDefinition: Get a single Identifier Definition

Get a single Identifier Definition using domain, identifierScope, identifierType, and an optional asAt              - defaulting to latest if not specified

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    IdentifierDefinitionsApi
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
    api_instance = api_client_factory.build(IdentifierDefinitionsApi)
    domain = 'domain_example' # str | The type of entity to which the identifier relates.
    identifier_scope = 'identifier_scope_example' # str | The scope that the identifier exists in
    identifier_type = 'identifier_type_example' # str | What the identifier represents. Together with \"domain\" and \"identifierScope\" this uniquely identifies the identifier definition
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Identifier Definition. Defaults to return              the latest version of the definition if not specified. (optional)
    effective_at = 'effective_at_example' # str | The effectiveAt datetime at which to retrieve the Identifier Definitions.              Since Identifier Definitions exist for all effective time, this will only apply to properties (if requested)              on the Identifier Definition. (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the 'IdentifierDefinition' domain to decorate onto the Identifier Definition.              These must take the format {domain}/{scope}/{code}. If no properties are specified, then no properties will be returned. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_identifier_definition(domain, identifier_scope, identifier_type, as_at=as_at, effective_at=effective_at, property_keys=property_keys, opts=opts)

        # [EXPERIMENTAL] GetIdentifierDefinition: Get a single Identifier Definition
        api_response = api_instance.get_identifier_definition(domain, identifier_scope, identifier_type, as_at=as_at, effective_at=effective_at, property_keys=property_keys)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling IdentifierDefinitionsApi->get_identifier_definition: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The type of entity to which the identifier relates. | 
 **identifier_scope** | **str**| The scope that the identifier exists in | 
 **identifier_type** | **str**| What the identifier represents. Together with \&quot;domain\&quot; and \&quot;identifierScope\&quot; this uniquely identifies the identifier definition | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Identifier Definition. Defaults to return              the latest version of the definition if not specified. | [optional] 
 **effective_at** | **str**| The effectiveAt datetime at which to retrieve the Identifier Definitions.              Since Identifier Definitions exist for all effective time, this will only apply to properties (if requested)              on the Identifier Definition. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;IdentifierDefinition&#39; domain to decorate onto the Identifier Definition.              These must take the format {domain}/{scope}/{code}. If no properties are specified, then no properties will be returned. | [optional] 

### Return type

[**IdentifierDefinition**](IdentifierDefinition.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Identifier Definition |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_identifier_definitions**
> PagedResourceListOfIdentifierDefinition list_identifier_definitions(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)

[EXPERIMENTAL] ListIdentifierDefinitions: List Identifier Definitions

Retrieves all Identifier Definitions that fit the filter, in a specific order if sortBy is provided  Supports pagination

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    IdentifierDefinitionsApi
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
    api_instance = api_client_factory.build(IdentifierDefinitionsApi)
    effective_at = 'effective_at_example' # str | The effectiveAt datetime at which to retrieve the Identifier Definitions.              Since Identifier Definitions exist for all effective time, this will only apply to properties (if requested)              on the Identifier Definition. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Identifier Definitions. Defaults to return the latest              version of the Identifier Definitions if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing Identifier Definitions from a previous call to list              Identifier Definitions. This value is returned from the previous call. If a pagination token is provided the sortBy,              filter, effectiveAt, and asAt fields must not have changed since the original request. (optional)
    limit = 56 # int | When paginating, limit the number of returned results to this many per page. (optional)
    filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid. (optional)
    sort_by = ['sort_by_example'] # List[str] | A list of field names to sort by, each suffixed by \" ASC\" or \" DESC\" (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the 'IdentifierDefinition' domain to decorate onto the Identifier Definition.              These must take the format {domain}/{scope}/{code}. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_identifier_definitions(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys, opts=opts)

        # [EXPERIMENTAL] ListIdentifierDefinitions: List Identifier Definitions
        api_response = api_instance.list_identifier_definitions(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling IdentifierDefinitionsApi->list_identifier_definitions: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **effective_at** | **str**| The effectiveAt datetime at which to retrieve the Identifier Definitions.              Since Identifier Definitions exist for all effective time, this will only apply to properties (if requested)              on the Identifier Definition. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Identifier Definitions. Defaults to return the latest              version of the Identifier Definitions if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing Identifier Definitions from a previous call to list              Identifier Definitions. This value is returned from the previous call. If a pagination token is provided the sortBy,              filter, effectiveAt, and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many per page. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot; | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;IdentifierDefinition&#39; domain to decorate onto the Identifier Definition.              These must take the format {domain}/{scope}/{code}. | [optional] 

### Return type

[**PagedResourceListOfIdentifierDefinition**](PagedResourceListOfIdentifierDefinition.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested list of Identifier Definitions |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **update_identifier_definition**
> IdentifierDefinition update_identifier_definition(domain, identifier_scope, identifier_type, update_identifier_definition_request=update_identifier_definition_request)

[EXPERIMENTAL] UpdateIdentifierDefinition: Update Identifier Definition defined by domain, identifierScope, and identifierType

Overwrites an existing Identifier Definition.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    IdentifierDefinitionsApi
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
    api_instance = api_client_factory.build(IdentifierDefinitionsApi)
    domain = 'domain_example' # str | The type of entity to which the identifier relates
    identifier_scope = 'identifier_scope_example' # str | The scope that the identifier exists in
    identifier_type = 'identifier_type_example' # str | What the identifier represents. Together with \"domain\" and \"identifierScope\" this uniquely identifies the Identifier Definition

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # update_identifier_definition_request = UpdateIdentifierDefinitionRequest.from_json("")
    # update_identifier_definition_request = UpdateIdentifierDefinitionRequest.from_dict({})
    update_identifier_definition_request = UpdateIdentifierDefinitionRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.update_identifier_definition(domain, identifier_scope, identifier_type, update_identifier_definition_request=update_identifier_definition_request, opts=opts)

        # [EXPERIMENTAL] UpdateIdentifierDefinition: Update Identifier Definition defined by domain, identifierScope, and identifierType
        api_response = api_instance.update_identifier_definition(domain, identifier_scope, identifier_type, update_identifier_definition_request=update_identifier_definition_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling IdentifierDefinitionsApi->update_identifier_definition: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The type of entity to which the identifier relates | 
 **identifier_scope** | **str**| The scope that the identifier exists in | 
 **identifier_type** | **str**| What the identifier represents. Together with \&quot;domain\&quot; and \&quot;identifierScope\&quot; this uniquely identifies the Identifier Definition | 
 **update_identifier_definition_request** | [**UpdateIdentifierDefinitionRequest**](UpdateIdentifierDefinitionRequest.md)| The request containing the updated details of the Identifier Definition. | [optional] 

### Return type

[**IdentifierDefinition**](IdentifierDefinition.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated version of the requested Identifier Definition |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

