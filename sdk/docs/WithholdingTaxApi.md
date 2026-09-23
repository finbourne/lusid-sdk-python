# lusid.WithholdingTaxApi

All URIs are relative to *https://fbn-prd.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_withholding_tax_dataset_definitions**](WithholdingTaxApi.md#create_withholding_tax_dataset_definitions) | **POST** /api/withholdingtax/datasetdefinitions | [EARLY ACCESS] CreateWithholdingTaxDatasetDefinitions: Create the Withholding Tax dataset definitions.
[**delete_withholding_tax_configuration**](WithholdingTaxApi.md#delete_withholding_tax_configuration) | **DELETE** /api/withholdingtax/configurations/{scope}/{code} | [EARLY ACCESS] DeleteWithholdingTaxConfiguration: Delete a Withholding Tax Configuration.
[**delete_withholding_tax_dataset_definition**](WithholdingTaxApi.md#delete_withholding_tax_dataset_definition) | **DELETE** /api/withholdingtax/datasetdefinitions/{scope}/{code} | [EARLY ACCESS] DeleteWithholdingTaxDatasetDefinition: Delete a Withholding Tax dataset definition.
[**get_withholding_tax_configuration**](WithholdingTaxApi.md#get_withholding_tax_configuration) | **GET** /api/withholdingtax/configurations/{scope}/{code} | [EARLY ACCESS] GetWithholdingTaxConfiguration: Get a Withholding Tax Configuration.
[**get_withholding_tax_dataset_definition**](WithholdingTaxApi.md#get_withholding_tax_dataset_definition) | **GET** /api/withholdingtax/datasetdefinitions/{scope}/{code} | [EARLY ACCESS] GetWithholdingTaxDatasetDefinition: Get a Withholding Tax dataset definition.
[**list_withholding_tax_configurations**](WithholdingTaxApi.md#list_withholding_tax_configurations) | **GET** /api/withholdingtax/configurations | [EARLY ACCESS] ListWithholdingTaxConfigurations: List Withholding Tax Configurations.
[**list_withholding_tax_dataset_definitions**](WithholdingTaxApi.md#list_withholding_tax_dataset_definitions) | **GET** /api/withholdingtax/datasetdefinitions | [EARLY ACCESS] ListWithholdingTaxDatasetDefinitions: List Withholding Tax dataset definitions.
[**patch_withholding_tax_dataset_definition**](WithholdingTaxApi.md#patch_withholding_tax_dataset_definition) | **PATCH** /api/withholdingtax/datasetdefinitions/{scope}/{code} | [EARLY ACCESS] PatchWithholdingTaxDatasetDefinition: Patch a Withholding Tax dataset definition.
[**upsert_withholding_tax_configuration**](WithholdingTaxApi.md#upsert_withholding_tax_configuration) | **POST** /api/withholdingtax/configurations/{scope}/{code} | [EARLY ACCESS] UpsertWithholdingTaxConfiguration: Upsert a Withholding Tax Configuration.


# **create_withholding_tax_dataset_definitions**
> WithholdingTaxDatasetDefinitions create_withholding_tax_dataset_definitions(create_withholding_tax_dataset_definitions_request)

[EARLY ACCESS] CreateWithholdingTaxDatasetDefinitions: Create the Withholding Tax dataset definitions.

Create the anomaly and the main relational dataset definition for a customer domain, in a single call.                The definitions are constructed rather than accepted as given, so the fields the engine reads by name cannot  be absent, misspelled or created in the wrong field category. LUSID adds the mandatory core to both: taxCountry  and profileType as series identifiers, countryRate, treatyRate, betterRate and enhancedRate as value fields,  treatyRAS, betterRAS and enhancedRAS as value fields, and rank as a value field on the anomaly definition only.                The caller supplies only their own matching dimensions, given per dataset. The two schemas need not be  identical: a dimension present on only one dataset is simply not matched on when the other is queried, an ISIN  dimension on the anomaly dataset alone being the usual case. The request is rejected if it names a dimension  that collides with a mandatory core field, or if it omits a scope or a code.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    WithholdingTaxApi
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
    api_instance = api_client_factory.build(WithholdingTaxApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # create_withholding_tax_dataset_definitions_request = CreateWithholdingTaxDatasetDefinitionsRequest.from_json("")
    # create_withholding_tax_dataset_definitions_request = CreateWithholdingTaxDatasetDefinitionsRequest.from_dict({})
    create_withholding_tax_dataset_definitions_request = CreateWithholdingTaxDatasetDefinitionsRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.create_withholding_tax_dataset_definitions(create_withholding_tax_dataset_definitions_request, opts=opts)

        # [EARLY ACCESS] CreateWithholdingTaxDatasetDefinitions: Create the Withholding Tax dataset definitions.
        api_response = api_instance.create_withholding_tax_dataset_definitions(create_withholding_tax_dataset_definitions_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling WithholdingTaxApi->create_withholding_tax_dataset_definitions: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_withholding_tax_dataset_definitions_request** | [**CreateWithholdingTaxDatasetDefinitionsRequest**](CreateWithholdingTaxDatasetDefinitionsRequest.md)| The scope, code and matching dimensions of each of the two datasets to create. | 

### Return type

[**WithholdingTaxDatasetDefinitions**](WithholdingTaxDatasetDefinitions.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created anomaly and main relational dataset definitions. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_withholding_tax_configuration**
> DeletedEntityResponse delete_withholding_tax_configuration(scope, code)

[EARLY ACCESS] DeleteWithholdingTaxConfiguration: Delete a Withholding Tax Configuration.

Delete the Withholding Tax Configuration at the given scope and code. Rejected if a portfolio, fund or share  class still references the configuration, rather than orphaning those references.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    WithholdingTaxApi
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
    api_instance = api_client_factory.build(WithholdingTaxApi)
    scope = 'scope_example' # str | The scope of the Withholding Tax Configuration to be deleted.
    code = 'code_example' # str | The code of the Withholding Tax Configuration to be deleted. Together with the scope this uniquely identifies the configuration.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_withholding_tax_configuration(scope, code, opts=opts)

        # [EARLY ACCESS] DeleteWithholdingTaxConfiguration: Delete a Withholding Tax Configuration.
        api_response = api_instance.delete_withholding_tax_configuration(scope, code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling WithholdingTaxApi->delete_withholding_tax_configuration: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Withholding Tax Configuration to be deleted. | 
 **code** | **str**| The code of the Withholding Tax Configuration to be deleted. Together with the scope this uniquely identifies the configuration. | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the Withholding Tax Configuration was deleted. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_withholding_tax_dataset_definition**
> DeletedEntityResponse delete_withholding_tax_dataset_definition(scope, code)

[EARLY ACCESS] DeleteWithholdingTaxDatasetDefinition: Delete a Withholding Tax dataset definition.

Delete one Withholding Tax relational dataset definition, subject to the platform's own rules on what may be  changed on a populated dataset.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    WithholdingTaxApi
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
    api_instance = api_client_factory.build(WithholdingTaxApi)
    scope = 'scope_example' # str | The scope of the dataset definition to be deleted.
    code = 'code_example' # str | The code of the dataset definition to be deleted. Together with the scope this uniquely identifies the definition.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_withholding_tax_dataset_definition(scope, code, opts=opts)

        # [EARLY ACCESS] DeleteWithholdingTaxDatasetDefinition: Delete a Withholding Tax dataset definition.
        api_response = api_instance.delete_withholding_tax_dataset_definition(scope, code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling WithholdingTaxApi->delete_withholding_tax_dataset_definition: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the dataset definition to be deleted. | 
 **code** | **str**| The code of the dataset definition to be deleted. Together with the scope this uniquely identifies the definition. | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the relational dataset definition was deleted. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_withholding_tax_configuration**
> WithholdingTaxConfiguration get_withholding_tax_configuration(scope, code, as_at=as_at)

[EARLY ACCESS] GetWithholdingTaxConfiguration: Get a Withholding Tax Configuration.

Retrieve a single Withholding Tax Configuration by scope and code.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    WithholdingTaxApi
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
    api_instance = api_client_factory.build(WithholdingTaxApi)
    scope = 'scope_example' # str | The scope of the Withholding Tax Configuration.
    code = 'code_example' # str | The code of the Withholding Tax Configuration. Together with the scope this uniquely identifies the configuration.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Withholding Tax Configuration. Defaults to returning the latest version if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_withholding_tax_configuration(scope, code, as_at=as_at, opts=opts)

        # [EARLY ACCESS] GetWithholdingTaxConfiguration: Get a Withholding Tax Configuration.
        api_response = api_instance.get_withholding_tax_configuration(scope, code, as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling WithholdingTaxApi->get_withholding_tax_configuration: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Withholding Tax Configuration. | 
 **code** | **str**| The code of the Withholding Tax Configuration. Together with the scope this uniquely identifies the configuration. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Withholding Tax Configuration. Defaults to returning the latest version if not specified. | [optional] 

### Return type

[**WithholdingTaxConfiguration**](WithholdingTaxConfiguration.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Withholding Tax Configuration. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_withholding_tax_dataset_definition**
> WithholdingTaxDataset get_withholding_tax_dataset_definition(scope, code, as_at=as_at)

[EARLY ACCESS] GetWithholdingTaxDatasetDefinition: Get a Withholding Tax dataset definition.

Retrieve one Withholding Tax dataset definition by scope and code, in the same shape the create returns: the  matching dimensions the caller supplied. The mandatory core is not returned here; read the full field schema  from the relational dataset definition at the returned href.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    WithholdingTaxApi
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
    api_instance = api_client_factory.build(WithholdingTaxApi)
    scope = 'scope_example' # str | The scope of the dataset definition.
    code = 'code_example' # str | The code of the dataset definition. Together with the scope this uniquely identifies the definition.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the dataset definition. Defaults to returning the latest version if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_withholding_tax_dataset_definition(scope, code, as_at=as_at, opts=opts)

        # [EARLY ACCESS] GetWithholdingTaxDatasetDefinition: Get a Withholding Tax dataset definition.
        api_response = api_instance.get_withholding_tax_dataset_definition(scope, code, as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling WithholdingTaxApi->get_withholding_tax_dataset_definition: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the dataset definition. | 
 **code** | **str**| The code of the dataset definition. Together with the scope this uniquely identifies the definition. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the dataset definition. Defaults to returning the latest version if not specified. | [optional] 

### Return type

[**WithholdingTaxDataset**](WithholdingTaxDataset.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Withholding Tax dataset definition. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_withholding_tax_configurations**
> PagedResourceListOfWithholdingTaxConfiguration list_withholding_tax_configurations(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)

[EARLY ACCESS] ListWithholdingTaxConfigurations: List Withholding Tax Configurations.

List the Withholding Tax Configurations across every scope the caller is entitled to. To list the  configurations of a single scope, filter on the scope.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    WithholdingTaxApi
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
    api_instance = api_client_factory.build(WithholdingTaxApi)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the Withholding Tax Configurations. Defaults to returning the latest version of each configuration if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing Withholding Tax Configurations; this value is              returned from the previous call. If a pagination token is provided, the filter and asAt fields must not have              changed since the original request. (optional)
    limit = 56 # int | When paginating, limit the results to this number. Defaults to 100 if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the results. For example, to filter on the scope, specify              \"id.Scope eq 'WithholdingTax'\", and to filter on the code, specify \"id.Code eq 'UK-LIFE-BLAGAB'\". For more              information about filtering results, see              https://support.lusid.com/docs/filtering-information-retrieved-from-lusid. (optional)
    sort_by = ['sort_by_example'] # List[str] | A list of field names or properties to sort by, each suffixed by \" ASC\" or \" DESC\". (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_withholding_tax_configurations(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, opts=opts)

        # [EARLY ACCESS] ListWithholdingTaxConfigurations: List Withholding Tax Configurations.
        api_response = api_instance.list_withholding_tax_configurations(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling WithholdingTaxApi->list_withholding_tax_configurations: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list the Withholding Tax Configurations. Defaults to returning the latest version of each configuration if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing Withholding Tax Configurations; this value is              returned from the previous call. If a pagination token is provided, the filter and asAt fields must not have              changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results. For example, to filter on the scope, specify              \&quot;id.Scope eq &#39;WithholdingTax&#39;\&quot;, and to filter on the code, specify \&quot;id.Code eq &#39;UK-LIFE-BLAGAB&#39;\&quot;. For more              information about filtering results, see              https://support.lusid.com/docs/filtering-information-retrieved-from-lusid. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 

### Return type

[**PagedResourceListOfWithholdingTaxConfiguration**](PagedResourceListOfWithholdingTaxConfiguration.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Withholding Tax Configurations. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_withholding_tax_dataset_definitions**
> PagedResourceListOfWithholdingTaxDataset list_withholding_tax_dataset_definitions(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)

[EARLY ACCESS] ListWithholdingTaxDatasetDefinitions: List Withholding Tax dataset definitions.

List the Withholding Tax dataset definitions across every scope the caller is entitled to, each in the same  shape the create returns. To list the definitions of a single scope, filter on the scope.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    WithholdingTaxApi
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
    api_instance = api_client_factory.build(WithholdingTaxApi)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the dataset definitions. Defaults to returning the latest version of each definition if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing dataset definitions; this value is returned              from the previous call. If a pagination token is provided, the filter and asAt fields must not have changed              since the original request. (optional)
    limit = 56 # int | When paginating, limit the results to this number. Defaults to 100 if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the results. For example, to filter on the scope, specify              \"scope eq 'WithholdingTax'\", and to filter on the code, specify \"code eq 'wht-main-rates'\". For more              information about filtering results, see              https://support.lusid.com/docs/filtering-information-retrieved-from-lusid. (optional)
    sort_by = ['sort_by_example'] # List[str] | A list of field names or properties to sort by, each suffixed by \" ASC\" or \" DESC\". (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_withholding_tax_dataset_definitions(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, opts=opts)

        # [EARLY ACCESS] ListWithholdingTaxDatasetDefinitions: List Withholding Tax dataset definitions.
        api_response = api_instance.list_withholding_tax_dataset_definitions(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling WithholdingTaxApi->list_withholding_tax_dataset_definitions: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list the dataset definitions. Defaults to returning the latest version of each definition if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing dataset definitions; this value is returned              from the previous call. If a pagination token is provided, the filter and asAt fields must not have changed              since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results. For example, to filter on the scope, specify              \&quot;scope eq &#39;WithholdingTax&#39;\&quot;, and to filter on the code, specify \&quot;code eq &#39;wht-main-rates&#39;\&quot;. For more              information about filtering results, see              https://support.lusid.com/docs/filtering-information-retrieved-from-lusid. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 

### Return type

[**PagedResourceListOfWithholdingTaxDataset**](PagedResourceListOfWithholdingTaxDataset.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Withholding Tax dataset definitions. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **patch_withholding_tax_dataset_definition**
> WithholdingTaxDataset patch_withholding_tax_dataset_definition(scope, code, operation)

[EARLY ACCESS] PatchWithholdingTaxDatasetDefinition: Patch a Withholding Tax dataset definition.

Amend one Withholding Tax relational dataset definition, adding a matching dimension being the common case.  Subject to the platform's own rules on what may be changed on a populated dataset.                Only the matching dimensions the document addresses are affected; a dimension it does not address is left as  it is. Append a dimension with an add on \"/dimensions/-\", and amend one in place with an add on its index.                A dimension whose name collides with a mandatory core field is rejected, as is any attempt to add a rate tier:  the tier set is fixed at four and cannot be extended by schema evolution, because the engine could never read  a tier it does not know by name. The mandatory core is not addressable by this endpoint at all.                The amended dataset is returned in the same shape the get and the list return: the matching dimensions alone.  Read the full field schema from the relational dataset definition at the returned href.  The behaviour is defined by the JSON Patch specification.    Currently supported fields are: Dimensions.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    WithholdingTaxApi
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
    api_instance = api_client_factory.build(WithholdingTaxApi)
    scope = 'scope_example' # str | The scope of the dataset definition to amend.
    code = 'code_example' # str | The code of the dataset definition to amend. Together with the scope this uniquely identifies the definition.
    operation = [{"value":{"fieldName":"isin","displayName":"ISIN","description":"The ISIN of the instrument the rate row applies to.","dataTypeId":{"scope":"system","code":"string"}},"path":"/dimensions/-","op":"add"},{"value":{"fieldName":"custodian","displayName":"Custodian","description":"The custodian holding the position the rate row applies to.","dataTypeId":{"scope":"system","code":"string"}},"path":"/dimensions/1","op":"add"}] # List[Operation] | The json patch document. For more information see: https://datatracker.ietf.org/doc/html/rfc6902.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.patch_withholding_tax_dataset_definition(scope, code, operation, opts=opts)

        # [EARLY ACCESS] PatchWithholdingTaxDatasetDefinition: Patch a Withholding Tax dataset definition.
        api_response = api_instance.patch_withholding_tax_dataset_definition(scope, code, operation)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling WithholdingTaxApi->patch_withholding_tax_dataset_definition: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the dataset definition to amend. | 
 **code** | **str**| The code of the dataset definition to amend. Together with the scope this uniquely identifies the definition. | 
 **operation** | [**List[Operation]**](Operation.md)| The json patch document. For more information see: https://datatracker.ietf.org/doc/html/rfc6902. | 

### Return type

[**WithholdingTaxDataset**](WithholdingTaxDataset.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The amended Withholding Tax dataset. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **upsert_withholding_tax_configuration**
> WithholdingTaxConfiguration upsert_withholding_tax_configuration(scope, code, upsert_withholding_tax_configuration_request)

[EARLY ACCESS] UpsertWithholdingTaxConfiguration: Upsert a Withholding Tax Configuration.

Create or replace the Withholding Tax Configuration at the given scope and code. The write is a full replace  on the object rather than a partial update, so the request must carry the complete configuration.                The write is rejected if either referenced dataset does not exist, if either is missing a mandatory core field  or has one in the wrong field category, if any customer-defined dimension in either dataset has no value source  declaration, or if a declaration names a dimension neither dataset has. Errors name the specific field.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    WithholdingTaxApi
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
    api_instance = api_client_factory.build(WithholdingTaxApi)
    scope = 'scope_example' # str | The scope of the Withholding Tax Configuration.
    code = 'code_example' # str | The code of the Withholding Tax Configuration. Together with the scope this uniquely identifies the configuration.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # upsert_withholding_tax_configuration_request = UpsertWithholdingTaxConfigurationRequest.from_json("")
    # upsert_withholding_tax_configuration_request = UpsertWithholdingTaxConfigurationRequest.from_dict({})
    upsert_withholding_tax_configuration_request = UpsertWithholdingTaxConfigurationRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.upsert_withholding_tax_configuration(scope, code, upsert_withholding_tax_configuration_request, opts=opts)

        # [EARLY ACCESS] UpsertWithholdingTaxConfiguration: Upsert a Withholding Tax Configuration.
        api_response = api_instance.upsert_withholding_tax_configuration(scope, code, upsert_withholding_tax_configuration_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling WithholdingTaxApi->upsert_withholding_tax_configuration: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Withholding Tax Configuration. | 
 **code** | **str**| The code of the Withholding Tax Configuration. Together with the scope this uniquely identifies the configuration. | 
 **upsert_withholding_tax_configuration_request** | [**UpsertWithholdingTaxConfigurationRequest**](UpsertWithholdingTaxConfigurationRequest.md)| The complete Withholding Tax Configuration to create or replace. | 

### Return type

[**WithholdingTaxConfiguration**](WithholdingTaxConfiguration.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The created or replaced Withholding Tax Configuration. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

