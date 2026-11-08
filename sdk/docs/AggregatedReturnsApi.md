# lusid.AggregatedReturnsApi

All URIs are relative to *https://fbn-prd.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_returns**](AggregatedReturnsApi.md#delete_returns) | **DELETE** /api/returns/{scope}/{code}/{entityType}/{entityScope}/{entityCode}/$delete | [EXPERIMENTAL] DeleteReturns: Delete Returns
[**delete_returns_entity**](AggregatedReturnsApi.md#delete_returns_entity) | **DELETE** /api/returns/{scope}/{code} | [EXPERIMENTAL] DeleteReturnsEntity: Delete returns entity.
[**get_aggregated_returns**](AggregatedReturnsApi.md#get_aggregated_returns) | **POST** /api/returns/$aggregated | [EXPERIMENTAL] GetAggregatedReturns: Calculate aggregated returns for an entity.
[**get_returns**](AggregatedReturnsApi.md#get_returns) | **GET** /api/returns/{scope}/{code}/{entityType}/{entityScope}/{entityCode} | [EXPERIMENTAL] GetReturns: Get Returns
[**get_returns_entity**](AggregatedReturnsApi.md#get_returns_entity) | **GET** /api/returns/{scope}/{code} | [EXPERIMENTAL] GetReturnsEntity: Get returns entity.
[**list_returns_entities**](AggregatedReturnsApi.md#list_returns_entities) | **GET** /api/returns | [EXPERIMENTAL] ListReturnsEntities: List returns entities.
[**upsert_returns**](AggregatedReturnsApi.md#upsert_returns) | **POST** /api/returns/{scope}/{code}/{entityType}/{entityScope}/{entityCode} | [EXPERIMENTAL] UpsertReturns: Upsert Returns
[**upsert_returns_entity**](AggregatedReturnsApi.md#upsert_returns_entity) | **POST** /api/returns | [EXPERIMENTAL] UpsertReturnsEntity: Upsert returns entity.


# **delete_returns**
> DeletedEntityResponse delete_returns(scope, code, entity_type, entity_scope, entity_code, from_effective_at, to_effective_at, period=period)

[EXPERIMENTAL] DeleteReturns: Delete Returns

Cancel the Returns stored under the returns series against the specified entity inside the window.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    AggregatedReturnsApi
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
    api_instance = api_client_factory.build(AggregatedReturnsApi)
    scope = 'scope_example' # str | The scope of the Returns.
    code = 'code_example' # str | The code of the Returns.
    entity_type = 'entity_type_example' # str | The type of the entity the Returns are stored against: 'Portfolio' or 'PortfolioGroup'. Available values: Portfolio, PortfolioGroup.
    entity_scope = 'entity_scope_example' # str | The scope of the entity.
    entity_code = 'entity_code_example' # str | The code of the entity.
    from_effective_at = 'from_effective_at_example' # str | The start date from which to delete the Returns.
    to_effective_at = 'to_effective_at_example' # str | The end date from which to delete the Returns.
    period = 'period_example' # str | The period of the Returns to be deleted. Default value: Daily. Available values: Daily, Monthly. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_returns(scope, code, entity_type, entity_scope, entity_code, from_effective_at, to_effective_at, period=period, opts=opts)

        # [EXPERIMENTAL] DeleteReturns: Delete Returns
        api_response = api_instance.delete_returns(scope, code, entity_type, entity_scope, entity_code, from_effective_at, to_effective_at, period=period)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling AggregatedReturnsApi->delete_returns: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Returns. | 
 **code** | **str**| The code of the Returns. | 
 **entity_type** | **str**| The type of the entity the Returns are stored against: &#39;Portfolio&#39; or &#39;PortfolioGroup&#39;. Available values: Portfolio, PortfolioGroup. | 
 **entity_scope** | **str**| The scope of the entity. | 
 **entity_code** | **str**| The code of the entity. | 
 **from_effective_at** | **str**| The start date from which to delete the Returns. | 
 **to_effective_at** | **str**| The end date from which to delete the Returns. | 
 **period** | **str**| The period of the Returns to be deleted. Default value: Daily. Available values: Daily, Monthly. | [optional] 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully deleted Returns data along with any failures |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_returns_entity**
> DeletedEntityResponse delete_returns_entity(scope, code)

[EXPERIMENTAL] DeleteReturnsEntity: Delete returns entity.

Delete returns entity.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    AggregatedReturnsApi
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
    api_instance = api_client_factory.build(AggregatedReturnsApi)
    scope = 'scope_example' # str | Returns entity scope.
    code = 'code_example' # str | Returns entity code.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_returns_entity(scope, code, opts=opts)

        # [EXPERIMENTAL] DeleteReturnsEntity: Delete returns entity.
        api_response = api_instance.delete_returns_entity(scope, code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling AggregatedReturnsApi->delete_returns_entity: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Returns entity scope. | 
 **code** | **str**| Returns entity code. | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The time that the returns entity was deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_aggregated_returns**
> AggregatedReturnsResponse get_aggregated_returns(aggregated_returns_entity_request)

[EXPERIMENTAL] GetAggregatedReturns: Calculate aggregated returns for an entity.

Report daily returns for the entity specified in the request body over the effective window.              Supports a Portfolio, or a PortfolioGroup whose members' returns are rolled up in their common base              currency, on a daily return grid. Returns upserted to the Returns store under the supplied returns id              take precedence: if any exist in the window for a portfolio they are reported as-is and nothing is              calculated for it. A group member's upserted returns are weighted by their stored (net) opening market              value and contribute only on the days they cover; a day with no upserted return for that member is              reported from the other members alone. Otherwise time-weighted returns are calculated using the              recipe, fee handling and flow-discrepancy handling of the persisted Returns entity identified by the              returns id, and the request fails if no such entity exists. A calculated day's return is the day's              profit and loss over the portfolio's net opening value, cash included and signed, so a portfolio              financed by overdraft reports a return on its negative capital; a portfolio whose net opening value is              zero and that takes in no capital during the day reports a zero return, with the day's gain or loss              visible in its market values. When a reporting currency is requested the Returns entity is also              required, as its recipe supplies the FX rates.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    AggregatedReturnsApi
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
    api_instance = api_client_factory.build(AggregatedReturnsApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # aggregated_returns_entity_request = AggregatedReturnsEntityRequest.from_json("")
    # aggregated_returns_entity_request = AggregatedReturnsEntityRequest.from_dict({})
    aggregated_returns_entity_request = AggregatedReturnsEntityRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_aggregated_returns(aggregated_returns_entity_request, opts=opts)

        # [EXPERIMENTAL] GetAggregatedReturns: Calculate aggregated returns for an entity.
        api_response = api_instance.get_aggregated_returns(aggregated_returns_entity_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling AggregatedReturnsApi->get_aggregated_returns: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aggregated_returns_entity_request** | [**AggregatedReturnsEntityRequest**](AggregatedReturnsEntityRequest.md)| The entity to report returns for, the returns id under which upserted returns              are stored and the Returns entity that configures a calculation, the effective window and the metrics              to report. | 

### Return type

[**AggregatedReturnsResponse**](AggregatedReturnsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The aggregated returns grouped by entity. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_returns**
> ResourceListOfPerformanceReturn get_returns(scope, code, entity_type, entity_scope, entity_code, from_effective_at=from_effective_at, to_effective_at=to_effective_at, period=period, as_at=as_at)

[EXPERIMENTAL] GetReturns: Get Returns

Get the Returns stored under the returns series against the specified entity.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    AggregatedReturnsApi
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
    api_instance = api_client_factory.build(AggregatedReturnsApi)
    scope = 'scope_example' # str | The scope of the Returns.
    code = 'code_example' # str | The code of the Returns.
    entity_type = 'entity_type_example' # str | The type of the entity the Returns are stored against: 'Portfolio' or 'PortfolioGroup'. Available values: Portfolio, PortfolioGroup.
    entity_scope = 'entity_scope_example' # str | The scope of the entity.
    entity_code = 'entity_code_example' # str | The code of the entity.
    from_effective_at = 'from_effective_at_example' # str | The start date from which to get the Returns. (optional)
    to_effective_at = 'to_effective_at_example' # str | The end date from which to get the Returns. (optional)
    period = 'period_example' # str | The period for which to show the Returns. Default value: Daily. Available values: Daily, Monthly. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Returns. Defaults to the latest. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_returns(scope, code, entity_type, entity_scope, entity_code, from_effective_at=from_effective_at, to_effective_at=to_effective_at, period=period, as_at=as_at, opts=opts)

        # [EXPERIMENTAL] GetReturns: Get Returns
        api_response = api_instance.get_returns(scope, code, entity_type, entity_scope, entity_code, from_effective_at=from_effective_at, to_effective_at=to_effective_at, period=period, as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling AggregatedReturnsApi->get_returns: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Returns. | 
 **code** | **str**| The code of the Returns. | 
 **entity_type** | **str**| The type of the entity the Returns are stored against: &#39;Portfolio&#39; or &#39;PortfolioGroup&#39;. Available values: Portfolio, PortfolioGroup. | 
 **entity_scope** | **str**| The scope of the entity. | 
 **entity_code** | **str**| The code of the entity. | 
 **from_effective_at** | **str**| The start date from which to get the Returns. | [optional] 
 **to_effective_at** | **str**| The end date from which to get the Returns. | [optional] 
 **period** | **str**| The period for which to show the Returns. Default value: Daily. Available values: Daily, Monthly. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Returns. Defaults to the latest. | [optional] 

### Return type

[**ResourceListOfPerformanceReturn**](ResourceListOfPerformanceReturn.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Returns on the given time period. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_returns_entity**
> ReturnsEntity get_returns_entity(scope, code, as_at=as_at)

[EXPERIMENTAL] GetReturnsEntity: Get returns entity.

Get returns entity.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    AggregatedReturnsApi
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
    api_instance = api_client_factory.build(AggregatedReturnsApi)
    scope = 'scope_example' # str | Returns entity scope.
    code = 'code_example' # str | Returns entity code.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the returns entity. Defaults to return              the latest version of the definition if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_returns_entity(scope, code, as_at=as_at, opts=opts)

        # [EXPERIMENTAL] GetReturnsEntity: Get returns entity.
        api_response = api_instance.get_returns_entity(scope, code, as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling AggregatedReturnsApi->get_returns_entity: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Returns entity scope. | 
 **code** | **str**| Returns entity code. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the returns entity. Defaults to return              the latest version of the definition if not specified. | [optional] 

### Return type

[**ReturnsEntity**](ReturnsEntity.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested returns entity |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_returns_entities**
> ResourceListOfReturnsEntity list_returns_entities(as_at=as_at)

[EXPERIMENTAL] ListReturnsEntities: List returns entities.

List returns entities.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    AggregatedReturnsApi
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
    api_instance = api_client_factory.build(AggregatedReturnsApi)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the relation definitions. Defaults to return              the latest version of each definition if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_returns_entities(as_at=as_at, opts=opts)

        # [EXPERIMENTAL] ListReturnsEntities: List returns entities.
        api_response = api_instance.list_returns_entities(as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling AggregatedReturnsApi->list_returns_entities: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to retrieve the relation definitions. Defaults to return              the latest version of each definition if not specified. | [optional] 

### Return type

[**ResourceListOfReturnsEntity**](ResourceListOfReturnsEntity.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested returns entities |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **upsert_returns**
> UpsertReturnsResponse upsert_returns(scope, code, entity_type, entity_scope, entity_code, performance_return)

[EXPERIMENTAL] UpsertReturns: Upsert Returns

Update or insert returns stored under the returns series against the specified entity. Stored              returns take precedence over a calculation in the aggregated returns of that entity.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    AggregatedReturnsApi
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
    api_instance = api_client_factory.build(AggregatedReturnsApi)
    scope = 'scope_example' # str | The scope of the Returns.
    code = 'code_example' # str | The code of the Returns.
    entity_type = 'entity_type_example' # str | The type of the entity the Returns are stored against: 'Portfolio' or 'PortfolioGroup'. Available values: Portfolio, PortfolioGroup.
    entity_scope = 'entity_scope_example' # str | The scope of the entity.
    entity_code = 'entity_code_example' # str | The code of the entity.
    performance_return = [{"effectiveAt":"2019-11-28T00:00:00.0000000+00:00","rateOfReturn":0.1,"openingMarketValue":500,"closingMarketValue":550,"period":"Daily"},{"effectiveAt":"2019-11-29T00:00:00.0000000+00:00","rateOfReturn":-0.2,"openingMarketValue":550,"closingMarketValue":440,"period":"Daily"}] # List[PerformanceReturn] | This contains the Returns which need to be upsert.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.upsert_returns(scope, code, entity_type, entity_scope, entity_code, performance_return, opts=opts)

        # [EXPERIMENTAL] UpsertReturns: Upsert Returns
        api_response = api_instance.upsert_returns(scope, code, entity_type, entity_scope, entity_code, performance_return)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling AggregatedReturnsApi->upsert_returns: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Returns. | 
 **code** | **str**| The code of the Returns. | 
 **entity_type** | **str**| The type of the entity the Returns are stored against: &#39;Portfolio&#39; or &#39;PortfolioGroup&#39;. Available values: Portfolio, PortfolioGroup. | 
 **entity_scope** | **str**| The scope of the entity. | 
 **entity_code** | **str**| The code of the entity. | 
 **performance_return** | [**List[PerformanceReturn]**](PerformanceReturn.md)| This contains the Returns which need to be upsert. | 

### Return type

[**UpsertReturnsResponse**](UpsertReturnsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The version of the entity that contains the newly updated or inserted Returns. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **upsert_returns_entity**
> ReturnsEntity upsert_returns_entity(returns_entity)

[EXPERIMENTAL] UpsertReturnsEntity: Upsert returns entity.

Upsert returns entity.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    AggregatedReturnsApi
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
    api_instance = api_client_factory.build(AggregatedReturnsApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # returns_entity = ReturnsEntity.from_json("")
    # returns_entity = ReturnsEntity.from_dict({})
    returns_entity = ReturnsEntity()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.upsert_returns_entity(returns_entity, opts=opts)

        # [EXPERIMENTAL] UpsertReturnsEntity: Upsert returns entity.
        api_response = api_instance.upsert_returns_entity(returns_entity)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling AggregatedReturnsApi->upsert_returns_entity: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **returns_entity** | [**ReturnsEntity**](ReturnsEntity.md)| Definition of the returns entity. | 

### Return type

[**ReturnsEntity**](ReturnsEntity.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The upserted returns entity |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

