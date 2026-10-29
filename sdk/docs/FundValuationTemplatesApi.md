# lusid.FundValuationTemplatesApi

All URIs are relative to *https://fbn-prd.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_valuation_address_key_template**](FundValuationTemplatesApi.md#delete_valuation_address_key_template) | **DELETE** /api/fundvaluationtemplates/{scope}/{code} | [EXPERIMENTAL] DeleteValuationAddressKeyTemplate: Delete a Valuation Template.
[**get_valuation_address_key_template**](FundValuationTemplatesApi.md#get_valuation_address_key_template) | **GET** /api/fundvaluationtemplates/{scope}/{code} | [EXPERIMENTAL] GetValuationAddressKeyTemplate: Get a Valuation Template.
[**list_valuation_address_key_templates**](FundValuationTemplatesApi.md#list_valuation_address_key_templates) | **GET** /api/fundvaluationtemplates | [EXPERIMENTAL] ListValuationAddressKeyTemplates: List Valuation Templates.
[**upsert_valuation_address_key_template**](FundValuationTemplatesApi.md#upsert_valuation_address_key_template) | **PUT** /api/fundvaluationtemplates/{scope}/{code} | [EXPERIMENTAL] UpsertValuationAddressKeyTemplate: Upsert a Valuation Template.


# **delete_valuation_address_key_template**
> DeletedEntityResponse delete_valuation_address_key_template(scope, code)

[EXPERIMENTAL] DeleteValuationAddressKeyTemplate: Delete a Valuation Template.

Delete the given Valuation Template. A template that any Fund or NAV Type references cannot be deleted.  If the deleted template is the domain default, the system default defined by LUSID applies again.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundValuationTemplatesApi
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
    api_instance = api_client_factory.build(FundValuationTemplatesApi)
    scope = 'scope_example' # str | The scope of the Valuation Template.
    code = 'code_example' # str | The code of the Valuation Template to delete.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_valuation_address_key_template(scope, code, opts=opts)

        # [EXPERIMENTAL] DeleteValuationAddressKeyTemplate: Delete a Valuation Template.
        api_response = api_instance.delete_valuation_address_key_template(scope, code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundValuationTemplatesApi->delete_valuation_address_key_template: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Valuation Template. | 
 **code** | **str**| The code of the Valuation Template to delete. | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the Valuation Template was deleted. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_valuation_address_key_template**
> ValuationAddressKeyTemplate get_valuation_address_key_template(scope, code, as_at=as_at)

[EXPERIMENTAL] GetValuationAddressKeyTemplate: Get a Valuation Template.

Retrieve a Valuation Template.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundValuationTemplatesApi
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
    api_instance = api_client_factory.build(FundValuationTemplatesApi)
    scope = 'scope_example' # str | The scope of the Valuation Template.
    code = 'code_example' # str | The code of the Valuation Template. Together with the scope this uniquely identifies the template.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Valuation Template. Defaults to returning the latest version if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_valuation_address_key_template(scope, code, as_at=as_at, opts=opts)

        # [EXPERIMENTAL] GetValuationAddressKeyTemplate: Get a Valuation Template.
        api_response = api_instance.get_valuation_address_key_template(scope, code, as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundValuationTemplatesApi->get_valuation_address_key_template: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Valuation Template. | 
 **code** | **str**| The code of the Valuation Template. Together with the scope this uniquely identifies the template. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Valuation Template. Defaults to returning the latest version if not specified. | [optional] 

### Return type

[**ValuationAddressKeyTemplate**](ValuationAddressKeyTemplate.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Valuation Template. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_valuation_address_key_templates**
> PagedResourceListOfValuationAddressKeyTemplate list_valuation_address_key_templates(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)

[EXPERIMENTAL] ListValuationAddressKeyTemplates: List Valuation Templates.

List the stored Valuation Templates matching the given criteria. To find the domain default, filter on  \"isDefault eq true\". The system default is not stored, so it is not listed. If no stored template is the  default, the system default applies. Get it with scope \"default\" and code \"DefaultTemplate\".

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundValuationTemplatesApi
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
    api_instance = api_client_factory.build(FundValuationTemplatesApi)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the Valuation Templates. Defaults to returning the latest version of each template if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing Valuation Templates; this              value is returned from the previous call. If a pagination token is provided, the filter, sortBy and asAt              fields must not have changed since the original request. (optional)
    limit = 56 # int | When paginating, limit the results to this number. Defaults to 100 if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the results.              For example, to filter on the display name, specify \"displayName eq 'Default keys'\". For more information about filtering              results, see https://support.lusid.com/docs/filtering-information-retrieved-from-lusid. (optional)
    sort_by = ['sort_by_example'] # List[str] | A list of field names to sort by, each suffixed by \" ASC\" or \" DESC\". (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_valuation_address_key_templates(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, opts=opts)

        # [EXPERIMENTAL] ListValuationAddressKeyTemplates: List Valuation Templates.
        api_response = api_instance.list_valuation_address_key_templates(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundValuationTemplatesApi->list_valuation_address_key_templates: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list the Valuation Templates. Defaults to returning the latest version of each template if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing Valuation Templates; this              value is returned from the previous call. If a pagination token is provided, the filter, sortBy and asAt              fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results.              For example, to filter on the display name, specify \&quot;displayName eq &#39;Default keys&#39;\&quot;. For more information about filtering              results, see https://support.lusid.com/docs/filtering-information-retrieved-from-lusid. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 

### Return type

[**PagedResourceListOfValuationAddressKeyTemplate**](PagedResourceListOfValuationAddressKeyTemplate.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Valuation Templates. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **upsert_valuation_address_key_template**
> ValuationAddressKeyTemplate upsert_valuation_address_key_template(scope, code, upsert_valuation_address_key_template_request)

[EXPERIMENTAL] UpsertValuationAddressKeyTemplate: Upsert a Valuation Template.

Create a Valuation Template, or replace the whole content of an existing one. Every Fund and NAV Type that  references the template uses the new content. Set isDefault to make the template the domain default.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundValuationTemplatesApi
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
    api_instance = api_client_factory.build(FundValuationTemplatesApi)
    scope = 'scope_example' # str | The scope of the Valuation Template.
    code = 'code_example' # str | The code of the Valuation Template. Together with the scope this uniquely identifies the template.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # upsert_valuation_address_key_template_request = UpsertValuationAddressKeyTemplateRequest.from_json("")
    # upsert_valuation_address_key_template_request = UpsertValuationAddressKeyTemplateRequest.from_dict({})
    upsert_valuation_address_key_template_request = UpsertValuationAddressKeyTemplateRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.upsert_valuation_address_key_template(scope, code, upsert_valuation_address_key_template_request, opts=opts)

        # [EXPERIMENTAL] UpsertValuationAddressKeyTemplate: Upsert a Valuation Template.
        api_response = api_instance.upsert_valuation_address_key_template(scope, code, upsert_valuation_address_key_template_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundValuationTemplatesApi->upsert_valuation_address_key_template: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Valuation Template. | 
 **code** | **str**| The code of the Valuation Template. Together with the scope this uniquely identifies the template. | 
 **upsert_valuation_address_key_template_request** | [**UpsertValuationAddressKeyTemplateRequest**](UpsertValuationAddressKeyTemplateRequest.md)| The full content of the Valuation Template. | 

### Return type

[**ValuationAddressKeyTemplate**](ValuationAddressKeyTemplate.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The upserted Valuation Address Key Template. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

