# lusid.EntitiesApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_data_type_by_entity_unique_id**](EntitiesApi.md#get_data_type_by_entity_unique_id) | **GET** /api/entities/datatypes/{entityUniqueId} | [EXPERIMENTAL] GetDataTypeByEntityUniqueId: Get DataType by EntityUniqueId
[**get_instrument_by_entity_unique_id**](EntitiesApi.md#get_instrument_by_entity_unique_id) | **GET** /api/entities/instruments/{entityUniqueId} | [EXPERIMENTAL] GetInstrumentByEntityUniqueId: Get instrument by EntityUniqueId
[**get_portfolio_by_entity_unique_id**](EntitiesApi.md#get_portfolio_by_entity_unique_id) | **GET** /api/entities/portfolios/{entityUniqueId} | [EXPERIMENTAL] GetPortfolioByEntityUniqueId: Get portfolio by EntityUniqueId
[**get_portfolio_changes**](EntitiesApi.md#get_portfolio_changes) | **GET** /api/entities/changes/portfolios | GetPortfolioChanges: Get the next change to each portfolio in a scope.
[**get_property_definition_by_entity_unique_id**](EntitiesApi.md#get_property_definition_by_entity_unique_id) | **GET** /api/entities/propertydefinitions/{entityUniqueId} | [EXPERIMENTAL] GetPropertyDefinitionByEntityUniqueId: Get property definition by EntityUniqueId


# **get_data_type_by_entity_unique_id**
> DataTypeEntity get_data_type_by_entity_unique_id(entity_unique_id, as_at=as_at, previews=previews)

[EXPERIMENTAL] GetDataTypeByEntityUniqueId: Get DataType by EntityUniqueId

Retrieve the definition of a particular DataType.  If the DataType is deleted, this will return the state of the DataType immediately prior to deletion.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    EntitiesApi
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
        api_instance = api_client_factory.build(EntitiesApi)
        entity_unique_id = 'entity_unique_id_example' # str | The universally unique identifier of the DataType definition.
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the DataType definition. Defaults to returning the latest version of the DataType definition if not specified. (optional)
        previews = ['previews_example'] # List[str] | The ids of the staged modifications to be previewed in the response. (optional)

        try:
            # [EXPERIMENTAL] GetDataTypeByEntityUniqueId: Get DataType by EntityUniqueId
            api_response = await api_instance.get_data_type_by_entity_unique_id(entity_unique_id, as_at=as_at, previews=previews)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling EntitiesApi->get_data_type_by_entity_unique_id: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_unique_id** | **str**| The universally unique identifier of the DataType definition. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the DataType definition. Defaults to returning the latest version of the DataType definition if not specified. | [optional] 
 **previews** | [**List[str]**](str.md)| The ids of the staged modifications to be previewed in the response. | [optional] 

### Return type

[**DataTypeEntity**](DataTypeEntity.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested DataType entity |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_instrument_by_entity_unique_id**
> InstrumentEntity get_instrument_by_entity_unique_id(entity_unique_id, effective_at=effective_at, as_at=as_at, previews=previews)

[EXPERIMENTAL] GetInstrumentByEntityUniqueId: Get instrument by EntityUniqueId

Retrieve the definition of a particular instrument.  If the instrument is deleted, this will return the state of the instrument immediately prior to deletion.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    EntitiesApi
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
        api_instance = api_client_factory.build(EntitiesApi)
        entity_unique_id = 'entity_unique_id_example' # str | The universally unique identifier of the instrument definition.
        effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve the Instrument definition. Defaults to the current LUSID system datetime if not specified. (optional)
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the instrument definition. Defaults to returning the latest version of the instrument definition if not specified. (optional)
        previews = ['previews_example'] # List[str] | The ids of the staged modifications to be previewed in the response. (optional)

        try:
            # [EXPERIMENTAL] GetInstrumentByEntityUniqueId: Get instrument by EntityUniqueId
            api_response = await api_instance.get_instrument_by_entity_unique_id(entity_unique_id, effective_at=effective_at, as_at=as_at, previews=previews)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling EntitiesApi->get_instrument_by_entity_unique_id: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_unique_id** | **str**| The universally unique identifier of the instrument definition. | 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the Instrument definition. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the instrument definition. Defaults to returning the latest version of the instrument definition if not specified. | [optional] 
 **previews** | [**List[str]**](str.md)| The ids of the staged modifications to be previewed in the response. | [optional] 

### Return type

[**InstrumentEntity**](InstrumentEntity.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested instrument entity |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_portfolio_by_entity_unique_id**
> PortfolioEntity get_portfolio_by_entity_unique_id(entity_unique_id, effective_at=effective_at, as_at=as_at, previews=previews)

[EXPERIMENTAL] GetPortfolioByEntityUniqueId: Get portfolio by EntityUniqueId

Retrieve the definition of a particular portfolio.  If the portfolio is deleted, this will return the state of the portfolio immediately prior to deletion.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    EntitiesApi
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
        api_instance = api_client_factory.build(EntitiesApi)
        entity_unique_id = 'entity_unique_id_example' # str | The universally unique identifier of the portfolio definition.
        effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve the portfolio definition. Defaults to the current LUSID system datetime if not specified. (optional)
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the portfolio definition. Defaults to returning the latest version of the portfolio definition if not specified. (optional)
        previews = ['previews_example'] # List[str] | The ids of the staged modifications to be previewed in the response. (optional)

        try:
            # [EXPERIMENTAL] GetPortfolioByEntityUniqueId: Get portfolio by EntityUniqueId
            api_response = await api_instance.get_portfolio_by_entity_unique_id(entity_unique_id, effective_at=effective_at, as_at=as_at, previews=previews)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling EntitiesApi->get_portfolio_by_entity_unique_id: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_unique_id** | **str**| The universally unique identifier of the portfolio definition. | 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the portfolio definition. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the portfolio definition. Defaults to returning the latest version of the portfolio definition if not specified. | [optional] 
 **previews** | [**List[str]**](str.md)| The ids of the staged modifications to be previewed in the response. | [optional] 

### Return type

[**PortfolioEntity**](PortfolioEntity.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested portfolio entity |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_portfolio_changes**
> ResourceListOfChange get_portfolio_changes(scope, effective_at, as_at=as_at)

GetPortfolioChanges: Get the next change to each portfolio in a scope.

Gets the time of the next (earliest effective at) modification (correction and/or amendment) to each portfolio in a scope relative to a point in bitemporal time.  Includes changes from parent portfolios in different scopes.  Excludes changes from subscriptions (e.g corporate actions).

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    EntitiesApi
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
        api_instance = api_client_factory.build(EntitiesApi)
        scope = 'scope_example' # str | The scope
        effective_at = 'effective_at_example' # str | The effective date of the origin.
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The as-at date of the origin. (optional)

        try:
            # GetPortfolioChanges: Get the next change to each portfolio in a scope.
            api_response = await api_instance.get_portfolio_changes(scope, effective_at, as_at=as_at)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling EntitiesApi->get_portfolio_changes: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope | 
 **effective_at** | **str**| The effective date of the origin. | 
 **as_at** | **datetime**| The as-at date of the origin. | [optional] 

### Return type

[**ResourceListOfChange**](ResourceListOfChange.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | The details of the input related failure |  -  |
**200** | A list of portfolio changes in the requested scope relative to the specified time. |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_property_definition_by_entity_unique_id**
> PropertyDefinitionEntity get_property_definition_by_entity_unique_id(entity_unique_id, effective_at=effective_at, as_at=as_at, previews=previews)

[EXPERIMENTAL] GetPropertyDefinitionByEntityUniqueId: Get property definition by EntityUniqueId

Retrieve a particular property definition.  If the property definition is deleted, this will return the state of the property definition immediately prior to deletion.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    EntitiesApi
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
        api_instance = api_client_factory.build(EntitiesApi)
        entity_unique_id = 'entity_unique_id_example' # str | The universally unique identifier of the property definition.
        effective_at = 'effective_at_example' # str | The effective datetime at which to retrieve the property definition. Defaults to the current LUSID system datetime if not specified. (optional)
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the property definition. Defaults to returning the latest version of the property definition if not specified. (optional)
        previews = ['previews_example'] # List[str] | The ids of the staged modifications to be previewed in the response. (optional)

        try:
            # [EXPERIMENTAL] GetPropertyDefinitionByEntityUniqueId: Get property definition by EntityUniqueId
            api_response = await api_instance.get_property_definition_by_entity_unique_id(entity_unique_id, effective_at=effective_at, as_at=as_at, previews=previews)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling EntitiesApi->get_property_definition_by_entity_unique_id: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_unique_id** | **str**| The universally unique identifier of the property definition. | 
 **effective_at** | **str**| The effective datetime at which to retrieve the property definition. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the property definition. Defaults to returning the latest version of the property definition if not specified. | [optional] 
 **previews** | [**List[str]**](str.md)| The ids of the staged modifications to be previewed in the response. | [optional] 

### Return type

[**PropertyDefinitionEntity**](PropertyDefinitionEntity.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested property definition entity |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

