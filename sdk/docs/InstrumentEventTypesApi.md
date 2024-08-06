# lusid.InstrumentEventTypesApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_transaction_template**](InstrumentEventTypesApi.md#create_transaction_template) | **POST** /api/instrumenteventtypes/{instrumentEventType}/transactiontemplates/{instrumentType}/{scope} | [EXPERIMENTAL] CreateTransactionTemplate: Create Transaction Template
[**delete_transaction_template**](InstrumentEventTypesApi.md#delete_transaction_template) | **DELETE** /api/instrumenteventtypes/{instrumentEventType}/transactiontemplates/{instrumentType}/{scope} | [EXPERIMENTAL] DeleteTransactionTemplate: Delete Transaction Template
[**get_transaction_template**](InstrumentEventTypesApi.md#get_transaction_template) | **GET** /api/instrumenteventtypes/{instrumentEventType}/transactiontemplates/{instrumentType}/{scope} | [EXPERIMENTAL] GetTransactionTemplate: Get Transaction Template
[**get_transaction_template_specification**](InstrumentEventTypesApi.md#get_transaction_template_specification) | **GET** /api/instrumenteventtypes/{instrumentEventType}/transactiontemplatespecification | [EXPERIMENTAL] GetTransactionTemplateSpecification: Get Transaction Template Specification.
[**list_transaction_template_specifications**](InstrumentEventTypesApi.md#list_transaction_template_specifications) | **GET** /api/instrumenteventtypes/transactiontemplatespecifications | [EXPERIMENTAL] ListTransactionTemplateSpecifications: List Transaction Template Specifications.
[**list_transaction_templates**](InstrumentEventTypesApi.md#list_transaction_templates) | **GET** /api/instrumenteventtypes/transactiontemplates | [EXPERIMENTAL] ListTransactionTemplates: List Transaction Templates
[**update_transaction_template**](InstrumentEventTypesApi.md#update_transaction_template) | **PUT** /api/instrumenteventtypes/{instrumentEventType}/transactiontemplates/{instrumentType}/{scope} | [EXPERIMENTAL] UpdateTransactionTemplate: Update Transaction Template


# **create_transaction_template**
> TransactionTemplate create_transaction_template(instrument_event_type, instrument_type, scope, transaction_template_request)

[EXPERIMENTAL] CreateTransactionTemplate: Create Transaction Template

Create a transaction template for a particular instrument event type in a scope.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    InstrumentEventTypesApi
)

async def main():

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

    # Use the lusid ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(InstrumentEventTypesApi)
        instrument_event_type = 'instrument_event_type_example' # str | The type of instrument events that the template is applied to.
        instrument_type = 'instrument_type_example' # str | The instrument type of the transaction template. The combination of the instrument              event type, instrument type and scope uniquely identifies a transaction template
        scope = 'scope_example' # str | The scope in which the template lies.

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # transaction_template_request = TransactionTemplateRequest()
        # transaction_template_request = TransactionTemplateRequest.from_json("")
        transaction_template_request = TransactionTemplateRequest.from_dict({"description":"User-created template for overriding the default bond coupon template.","componentTransactions":[{"displayName":"Bond Income Override","transactionFieldMap":{"transactionId":"{{instrumentEventId}}-{{holdingId}}","type":"BondCoupon","source":"MyTransactionTypeSource","instrument":"{{instrument}}","transactionDate":"{{BondCouponEvent.exDate}}","settlementDate":"{{BondCouponEvent.paymentDate}}","units":"{{eligibleBalance}}","transactionPrice":{"price":"{{BondCouponEvent.couponPerUnit}}","type":"CashFlowPerUnit"},"transactionCurrency":"{{BondCouponEvent.currency}}","exchangeRate":"1","totalConsideration":{"currency":"{{BondCouponEvent.currency}}","amount":"{{BondCouponEvent.couponAmount}}"}},"transactionPropertyMap":[{"propertyKey":"Transaction/MyScope/MyCurrencyProperty","value":"{{BondCouponEvent.currency}}"}]}]}) # TransactionTemplateRequest | A request defining a new transaction template to be created.

        try:
            # [EXPERIMENTAL] CreateTransactionTemplate: Create Transaction Template
            api_response = await api_instance.create_transaction_template(instrument_event_type, instrument_type, scope, transaction_template_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling InstrumentEventTypesApi->create_transaction_template: %s\n" % e)

asyncio.run(main())
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

[EXPERIMENTAL] DeleteTransactionTemplate: Delete Transaction Template

Delete a transaction template for a particular instrument event type in a scope.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    InstrumentEventTypesApi
)

async def main():

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

    # Use the lusid ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(InstrumentEventTypesApi)
        instrument_event_type = 'instrument_event_type_example' # str | The type of instrument events that the template is applied to.
        instrument_type = 'instrument_type_example' # str | The instrument type of the transaction template. The combination of the instrument              event type, instrument type and scope uniquely identifies a transaction template
        scope = 'scope_example' # str | The scope of the template.

        try:
            # [EXPERIMENTAL] DeleteTransactionTemplate: Delete Transaction Template
            api_response = await api_instance.delete_transaction_template(instrument_event_type, instrument_type, scope)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling InstrumentEventTypesApi->delete_transaction_template: %s\n" % e)

asyncio.run(main())
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

[EXPERIMENTAL] GetTransactionTemplate: Get Transaction Template

Gets the Transaction Template that for the instrument event type within the scope specified.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    InstrumentEventTypesApi
)

async def main():

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

    # Use the lusid ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(InstrumentEventTypesApi)
        instrument_event_type = 'instrument_event_type_example' # str | The instrument event type of the transaction template
        instrument_type = 'instrument_type_example' # str | The instrument type of the transaction template. The combination of the instrument              event type, instrument type and scope uniquely identifies a transaction template
        scope = 'scope_example' # str | The scope in which the template lies. When not supplied the scope is 'default'.
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The AsAt time of the requested Transaction Template (optional)

        try:
            # [EXPERIMENTAL] GetTransactionTemplate: Get Transaction Template
            api_response = await api_instance.get_transaction_template(instrument_event_type, instrument_type, scope, as_at=as_at)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling InstrumentEventTypesApi->get_transaction_template: %s\n" % e)

asyncio.run(main())
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

[EXPERIMENTAL] GetTransactionTemplateSpecification: Get Transaction Template Specification.

Retrieve the transaction template specification for a particular event type.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    InstrumentEventTypesApi
)

async def main():

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

    # Use the lusid ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(InstrumentEventTypesApi)
        instrument_event_type = 'instrument_event_type_example' # str | The requested instrument event type.

        try:
            # [EXPERIMENTAL] GetTransactionTemplateSpecification: Get Transaction Template Specification.
            api_response = await api_instance.get_transaction_template_specification(instrument_event_type)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling InstrumentEventTypesApi->get_transaction_template_specification: %s\n" % e)

asyncio.run(main())
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

[EXPERIMENTAL] ListTransactionTemplateSpecifications: List Transaction Template Specifications.

Retrieves all transaction template specifications.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    InstrumentEventTypesApi
)

async def main():

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

    # Use the lusid ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(InstrumentEventTypesApi)
        as_at = '2013-10-20T19:20:30+01:00' # datetime | AsAt of the request (optional)
        page = 'page_example' # str | The pagination token to use to continue listing Transaction Template Specifications from              a previous call to list Transaction Template Specifications.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, and asAt              fields must not have changed since the original request. (optional)
        limit = 56 # int | When paginating, limit the number of returned results to this many. (optional)
        filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid. (optional)
        sort_by = ['sort_by_example'] # List[str] | A list of field names to sort by, each suffixed by \" ASC\" or \" DESC\". (optional)

        try:
            # [EXPERIMENTAL] ListTransactionTemplateSpecifications: List Transaction Template Specifications.
            api_response = await api_instance.list_transaction_template_specifications(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling InstrumentEventTypesApi->list_transaction_template_specifications: %s\n" % e)

asyncio.run(main())
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

[EXPERIMENTAL] ListTransactionTemplates: List Transaction Templates

Lists all Transaction Templates.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    InstrumentEventTypesApi
)

async def main():

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

    # Use the lusid ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(InstrumentEventTypesApi)
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The AsAt time at which to retrieve the Transaction Templates (optional)
        page = 'page_example' # str | The pagination token to use to continue listing Transaction Templates from a previous call to list Transaction Templates.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, limit, and asAt fields              must not have changed since the original request. (optional)
        limit = 56 # int | When paginating, limit the number of returned results to this many. (optional)
        filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid. (optional)
        sort_by = ['sort_by_example'] # List[str] | A list of field names to sort by, each suffixed by \" ASC\" or \" DESC\" (optional)

        try:
            # [EXPERIMENTAL] ListTransactionTemplates: List Transaction Templates
            api_response = await api_instance.list_transaction_templates(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling InstrumentEventTypesApi->list_transaction_templates: %s\n" % e)

asyncio.run(main())
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

[EXPERIMENTAL] UpdateTransactionTemplate: Update Transaction Template

Update a transaction template for a particular instrument event type in a scope.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    InstrumentEventTypesApi
)

async def main():

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

    # Use the lusid ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(InstrumentEventTypesApi)
        instrument_event_type = 'instrument_event_type_example' # str | The type of instrument events that the template is applied to.
        instrument_type = 'instrument_type_example' # str | The instrument type of the transaction template. The combination of the instrument              event type, instrument type and scope uniquely identifies a transaction template
        scope = 'scope_example' # str | The scope in which the template lies.

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # transaction_template_request = TransactionTemplateRequest()
        # transaction_template_request = TransactionTemplateRequest.from_json("")
        transaction_template_request = TransactionTemplateRequest.from_dict({"description":"User-created template for overriding the default bond coupon template.","componentTransactions":[{"displayName":"Bond Income Override","transactionFieldMap":{"transactionId":"{{instrumentEventId}}-{{holdingId}}","type":"BondCoupon","source":"MyTransactionTypeSource","instrument":"{{instrument}}","transactionDate":"{{BondCouponEvent.exDate}}","settlementDate":"{{BondCouponEvent.paymentDate}}","units":"{{eligibleBalance}}","transactionPrice":{"price":"{{BondCouponEvent.couponPerUnit}}","type":"CashFlowPerUnit"},"transactionCurrency":"{{BondCouponEvent.currency}}","exchangeRate":"1","totalConsideration":{"currency":"{{BondCouponEvent.currency}}","amount":"{{BondCouponEvent.couponAmount}}"}},"transactionPropertyMap":[{"propertyKey":"Transaction/MyScope/MyCurrencyProperty","value":"{{BondCouponEvent.currency}}"}]}]}) # TransactionTemplateRequest | A request defining the updated values for the transaction template.

        try:
            # [EXPERIMENTAL] UpdateTransactionTemplate: Update Transaction Template
            api_response = await api_instance.update_transaction_template(instrument_event_type, instrument_type, scope, transaction_template_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling InstrumentEventTypesApi->update_transaction_template: %s\n" % e)

asyncio.run(main())
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

