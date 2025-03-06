# lusid.InstrumentEventTypesApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_transaction_template**](InstrumentEventTypesApi.md#create_transaction_template) | **POST** /api/instrumenteventtypes/{instrumentEventType}/transactiontemplates/{instrumentType}/{scope} | CreateTransactionTemplate: Create Transaction Template
[**delete_transaction_template**](InstrumentEventTypesApi.md#delete_transaction_template) | **DELETE** /api/instrumenteventtypes/{instrumentEventType}/transactiontemplates/{instrumentType}/{scope} | DeleteTransactionTemplate: Delete Transaction Template
[**get_transaction_template**](InstrumentEventTypesApi.md#get_transaction_template) | **GET** /api/instrumenteventtypes/{instrumentEventType}/transactiontemplates/{instrumentType}/{scope} | GetTransactionTemplate: Get Transaction Template
[**get_transaction_template_specification**](InstrumentEventTypesApi.md#get_transaction_template_specification) | **GET** /api/instrumenteventtypes/{instrumentEventType}/transactiontemplatespecification | GetTransactionTemplateSpecification: Get Transaction Template Specification.
[**list_transaction_template_specifications**](InstrumentEventTypesApi.md#list_transaction_template_specifications) | **GET** /api/instrumenteventtypes/transactiontemplatespecifications | ListTransactionTemplateSpecifications: List Transaction Template Specifications.
[**list_transaction_templates**](InstrumentEventTypesApi.md#list_transaction_templates) | **GET** /api/instrumenteventtypes/transactiontemplates | ListTransactionTemplates: List Transaction Templates
[**update_transaction_template**](InstrumentEventTypesApi.md#update_transaction_template) | **PUT** /api/instrumenteventtypes/{instrumentEventType}/transactiontemplates/{instrumentType}/{scope} | UpdateTransactionTemplate: Update Transaction Template


# **create_transaction_template**
> TransactionTemplate create_transaction_template(instrument_event_type, instrument_type, scope, transaction_template_request)

CreateTransactionTemplate: Create Transaction Template

Create a transaction template for a particular instrument event type in a scope.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    InstrumentEventTypesApi
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
    api_instance = api_client_factory.build(InstrumentEventTypesApi)
    instrument_event_type = 'instrument_event_type_example' # str | The type of instrument events that the template is applied to.
    instrument_type = 'instrument_type_example' # str | The instrument type of the transaction template. The combination of the instrument              event type, instrument type and scope uniquely identifies a transaction template
    scope = 'scope_example' # str | The scope in which the template lies.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # transaction_template_request = TransactionTemplateRequest.from_json("")
    # transaction_template_request = TransactionTemplateRequest.from_dict({})
    transaction_template_request = TransactionTemplateRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.create_transaction_template(instrument_event_type, instrument_type, scope, transaction_template_request, opts=opts)

        # CreateTransactionTemplate: Create Transaction Template
        api_response = api_instance.create_transaction_template(instrument_event_type, instrument_type, scope, transaction_template_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling InstrumentEventTypesApi->create_transaction_template: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instrument_event_type** | **str**| The type of instrument events that the template is applied to. | 
 **instrument_type** | **str**| The instrument type of the transaction template. The combination of the instrument              event type, instrument type and scope uniquely identifies a transaction template | 
 **scope** | **str**| The scope in which the template lies. | 
 **transaction_template_request** | [**TransactionTemplateRequest**](TransactionTemplateRequest.md)| A request defining a new transaction template to be created. | 

### Return type

[**TransactionTemplate**](TransactionTemplate.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The response of the transaction template that was created. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_transaction_template**
> datetime delete_transaction_template(instrument_event_type, instrument_type, scope)

DeleteTransactionTemplate: Delete Transaction Template

Delete a transaction template for a particular instrument event type in a scope.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    InstrumentEventTypesApi
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
    api_instance = api_client_factory.build(InstrumentEventTypesApi)
    instrument_event_type = 'instrument_event_type_example' # str | The type of instrument events that the template is applied to.
    instrument_type = 'instrument_type_example' # str | The instrument type of the transaction template. The combination of the instrument              event type, instrument type and scope uniquely identifies a transaction template
    scope = 'scope_example' # str | The scope of the template.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_transaction_template(instrument_event_type, instrument_type, scope, opts=opts)

        # DeleteTransactionTemplate: Delete Transaction Template
        api_response = api_instance.delete_transaction_template(instrument_event_type, instrument_type, scope)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling InstrumentEventTypesApi->delete_transaction_template: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instrument_event_type** | **str**| The type of instrument events that the template is applied to. | 
 **instrument_type** | **str**| The instrument type of the transaction template. The combination of the instrument              event type, instrument type and scope uniquely identifies a transaction template | 
 **scope** | **str**| The scope of the template. | 

### Return type

**datetime**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The AsAt Time the Template was deleted. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_transaction_template**
> TransactionTemplate get_transaction_template(instrument_event_type, instrument_type, scope, as_at=as_at)

GetTransactionTemplate: Get Transaction Template

Gets the Transaction Template that for the instrument event type within the scope specified.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    InstrumentEventTypesApi
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
    api_instance = api_client_factory.build(InstrumentEventTypesApi)
    instrument_event_type = 'instrument_event_type_example' # str | The instrument event type of the transaction template
    instrument_type = 'instrument_type_example' # str | The instrument type of the transaction template. The combination of the instrument              event type, instrument type and scope uniquely identifies a transaction template
    scope = 'scope_example' # str | The scope in which the template lies. When not supplied the scope is 'default'.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The AsAt time of the requested Transaction Template (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_transaction_template(instrument_event_type, instrument_type, scope, as_at=as_at, opts=opts)

        # GetTransactionTemplate: Get Transaction Template
        api_response = api_instance.get_transaction_template(instrument_event_type, instrument_type, scope, as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling InstrumentEventTypesApi->get_transaction_template: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instrument_event_type** | **str**| The instrument event type of the transaction template | 
 **instrument_type** | **str**| The instrument type of the transaction template. The combination of the instrument              event type, instrument type and scope uniquely identifies a transaction template | 
 **scope** | **str**| The scope in which the template lies. When not supplied the scope is &#39;default&#39;. | 
 **as_at** | **datetime**| The AsAt time of the requested Transaction Template | [optional] 

### Return type

[**TransactionTemplate**](TransactionTemplate.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The transaction template. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_transaction_template_specification**
> TransactionTemplateSpecification get_transaction_template_specification(instrument_event_type)

GetTransactionTemplateSpecification: Get Transaction Template Specification.

Retrieve the transaction template specification for a particular event type.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    InstrumentEventTypesApi
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
    api_instance = api_client_factory.build(InstrumentEventTypesApi)
    instrument_event_type = 'instrument_event_type_example' # str | The requested instrument event type.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_transaction_template_specification(instrument_event_type, opts=opts)

        # GetTransactionTemplateSpecification: Get Transaction Template Specification.
        api_response = api_instance.get_transaction_template_specification(instrument_event_type)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling InstrumentEventTypesApi->get_transaction_template_specification: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instrument_event_type** | **str**| The requested instrument event type. | 

### Return type

[**TransactionTemplateSpecification**](TransactionTemplateSpecification.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Transaction Template Specification. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_transaction_template_specifications**
> PagedResourceListOfTransactionTemplateSpecification list_transaction_template_specifications(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)

ListTransactionTemplateSpecifications: List Transaction Template Specifications.

Retrieves all transaction template specifications.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    InstrumentEventTypesApi
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
    api_instance = api_client_factory.build(InstrumentEventTypesApi)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | AsAt of the request (optional)
    page = 'page_example' # str | The pagination token to use to continue listing Transaction Template Specifications from              a previous call to list Transaction Template Specifications.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, and asAt              fields must not have changed since the original request. (optional)
    limit = 56 # int | When paginating, limit the number of returned results to this many. (optional)
    filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid. (optional)
    sort_by = ['sort_by_example'] # List[str] | A list of field names to sort by, each suffixed by \" ASC\" or \" DESC\". (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_transaction_template_specifications(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, opts=opts)

        # ListTransactionTemplateSpecifications: List Transaction Template Specifications.
        api_response = api_instance.list_transaction_template_specifications(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling InstrumentEventTypesApi->list_transaction_template_specifications: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| AsAt of the request | [optional] 
 **page** | **str**| The pagination token to use to continue listing Transaction Template Specifications from              a previous call to list Transaction Template Specifications.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, and asAt              fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 

### Return type

[**PagedResourceListOfTransactionTemplateSpecification**](PagedResourceListOfTransactionTemplateSpecification.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Transaction Template Specifications. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_transaction_templates**
> PagedResourceListOfTransactionTemplate list_transaction_templates(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)

ListTransactionTemplates: List Transaction Templates

Lists all Transaction Templates.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    InstrumentEventTypesApi
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
    api_instance = api_client_factory.build(InstrumentEventTypesApi)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The AsAt time at which to retrieve the Transaction Templates (optional)
    page = 'page_example' # str | The pagination token to use to continue listing Transaction Templates from a previous call to list Transaction Templates.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, limit, and asAt fields              must not have changed since the original request. (optional)
    limit = 56 # int | When paginating, limit the number of returned results to this many. (optional)
    filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid. (optional)
    sort_by = ['sort_by_example'] # List[str] | A list of field names to sort by, each suffixed by \" ASC\" or \" DESC\" (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_transaction_templates(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, opts=opts)

        # ListTransactionTemplates: List Transaction Templates
        api_response = api_instance.list_transaction_templates(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling InstrumentEventTypesApi->list_transaction_templates: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The AsAt time at which to retrieve the Transaction Templates | [optional] 
 **page** | **str**| The pagination token to use to continue listing Transaction Templates from a previous call to list Transaction Templates.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, limit, and asAt fields              must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot; | [optional] 

### Return type

[**PagedResourceListOfTransactionTemplate**](PagedResourceListOfTransactionTemplate.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The transaction templates. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **update_transaction_template**
> TransactionTemplate update_transaction_template(instrument_event_type, instrument_type, scope, transaction_template_request)

UpdateTransactionTemplate: Update Transaction Template

Update a transaction template for a particular instrument event type in a scope.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    InstrumentEventTypesApi
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
    api_instance = api_client_factory.build(InstrumentEventTypesApi)
    instrument_event_type = 'instrument_event_type_example' # str | The type of instrument events that the template is applied to.
    instrument_type = 'instrument_type_example' # str | The instrument type of the transaction template. The combination of the instrument              event type, instrument type and scope uniquely identifies a transaction template
    scope = 'scope_example' # str | The scope in which the template lies.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # transaction_template_request = TransactionTemplateRequest.from_json("")
    # transaction_template_request = TransactionTemplateRequest.from_dict({})
    transaction_template_request = TransactionTemplateRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.update_transaction_template(instrument_event_type, instrument_type, scope, transaction_template_request, opts=opts)

        # UpdateTransactionTemplate: Update Transaction Template
        api_response = api_instance.update_transaction_template(instrument_event_type, instrument_type, scope, transaction_template_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling InstrumentEventTypesApi->update_transaction_template: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instrument_event_type** | **str**| The type of instrument events that the template is applied to. | 
 **instrument_type** | **str**| The instrument type of the transaction template. The combination of the instrument              event type, instrument type and scope uniquely identifies a transaction template | 
 **scope** | **str**| The scope in which the template lies. | 
 **transaction_template_request** | [**TransactionTemplateRequest**](TransactionTemplateRequest.md)| A request defining the updated values for the transaction template. | 

### Return type

[**TransactionTemplate**](TransactionTemplate.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response of the transaction template that was updated. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

