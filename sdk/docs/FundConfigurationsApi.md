# lusid.FundConfigurationsApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_fund_configuration**](FundConfigurationsApi.md#create_fund_configuration) | **POST** /api/fundconfigurations/{scope} | [EXPERIMENTAL] CreateFundConfiguration: Create a FundConfiguration.
[**delete_fund_configuration**](FundConfigurationsApi.md#delete_fund_configuration) | **DELETE** /api/fundconfigurations/{scope}/{code} | [EXPERIMENTAL] DeleteFundConfiguration: Delete a FundConfiguration.
[**get_fund_configuration**](FundConfigurationsApi.md#get_fund_configuration) | **GET** /api/fundconfigurations/{scope}/{code} | [EXPERIMENTAL] GetFundConfiguration: Get FundConfiguration.
[**list_fund_configurations**](FundConfigurationsApi.md#list_fund_configurations) | **GET** /api/fundconfigurations | [EXPERIMENTAL] ListFundConfigurations: List FundConfiguration.
[**upsert_fund_configuration_properties**](FundConfigurationsApi.md#upsert_fund_configuration_properties) | **POST** /api/fundconfigurations/{scope}/{code}/properties/$upsert | [EXPERIMENTAL] UpsertFundConfigurationProperties: Upsert FundConfiguration properties


# **create_fund_configuration**
> FundConfiguration create_fund_configuration(scope, fund_configuration_request)

[EXPERIMENTAL] CreateFundConfiguration: Create a FundConfiguration.

Create the given FundConfiguration.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    FundConfigurationsApi
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
        api_instance = api_client_factory.build(FundConfigurationsApi)
        scope = 'scope_example' # str | The scope of the FundConfiguration.

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # fund_configuration_request = FundConfigurationRequest()
        # fund_configuration_request = FundConfigurationRequest.from_json("")
        fund_configuration_request = FundConfigurationRequest.from_dict({"code":"FundConfigurationCode","displayName":"My Fund Configuration","description":"Standard Fund Configuration","dealingRule":{"components":[{"filterId":"SUB","filter":"account startswith 3001"},{"filterId":"RED","filter":"account startswith 3002"}]},"pnlRule":{"components":[{"filterId":"SUB","filter":"account startswith 3001"},{"filterId":"RED","filter":"account startswith 3002"}]},"backOutRule":{"components":[{"filterId":"SUB","filter":"account startswith 3001"},{"filterId":"RED","filter":"account startswith 3002"}]},"properties":{"FundConfiguration/MyScope/FundManagerName":{"key":"FundConfiguration/MyScope/FundManagerName","value":{"labelValue":"Smith"},"effectiveFrom":"2020-03-05T00:00:00.0000000+00:00"}}}) # FundConfigurationRequest | The definition of the FundConfiguration.

        try:
            # [EXPERIMENTAL] CreateFundConfiguration: Create a FundConfiguration.
            api_response = await api_instance.create_fund_configuration(scope, fund_configuration_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling FundConfigurationsApi->create_fund_configuration: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the FundConfiguration. | 
 **fund_configuration_request** | [**FundConfigurationRequest**](FundConfigurationRequest.md)| The definition of the FundConfiguration. | 

### Return type

[**FundConfiguration**](FundConfiguration.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created Fund configuration. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_fund_configuration**
> DeletedEntityResponse delete_fund_configuration(scope, code)

[EXPERIMENTAL] DeleteFundConfiguration: Delete a FundConfiguration.

Delete the given FundConfiguration.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    FundConfigurationsApi
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
        api_instance = api_client_factory.build(FundConfigurationsApi)
        scope = 'scope_example' # str | The scope of the FundConfiguration to be deleted.
        code = 'code_example' # str | The code of the FundConfiguration to be deleted.               Together with the scope this uniquely identifies the FundConfiguration.

        try:
            # [EXPERIMENTAL] DeleteFundConfiguration: Delete a FundConfiguration.
            api_response = await api_instance.delete_fund_configuration(scope, code)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling FundConfigurationsApi->delete_fund_configuration: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the FundConfiguration to be deleted. | 
 **code** | **str**| The code of the FundConfiguration to be deleted.               Together with the scope this uniquely identifies the FundConfiguration. | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the FundConfiguration was deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_fund_configuration**
> FundConfiguration get_fund_configuration(scope, code, effective_at=effective_at, as_at=as_at, property_keys=property_keys)

[EXPERIMENTAL] GetFundConfiguration: Get FundConfiguration.

Retrieve the definition of a particular FundConfiguration.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    FundConfigurationsApi
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
        api_instance = api_client_factory.build(FundConfigurationsApi)
        scope = 'scope_example' # str | The scope of the FundConfiguration.
        code = 'code_example' # str | The code of the FundConfiguration. Together with the scope this uniquely identifies the FundConfiguration.
        effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve the FundConfiguration properties. Defaults to the current LUSID system datetime if not specified. (optional)
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the FundConfiguration definition. Defaults to returning the latest version of the FundConfiguration definition if not specified. (optional)
        property_keys = ['property_keys_example'] # List[str] | A list of property keys from the 'FundConfiguration' domain to decorate onto the FundConfiguration.              These must take the format {domain}/{scope}/{code}, for example 'FundConfiguration/Manager/Id'. If no properties are specified, then no properties will be returned. (optional)

        try:
            # [EXPERIMENTAL] GetFundConfiguration: Get FundConfiguration.
            api_response = await api_instance.get_fund_configuration(scope, code, effective_at=effective_at, as_at=as_at, property_keys=property_keys)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling FundConfigurationsApi->get_fund_configuration: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the FundConfiguration. | 
 **code** | **str**| The code of the FundConfiguration. Together with the scope this uniquely identifies the FundConfiguration. | 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the FundConfiguration properties. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the FundConfiguration definition. Defaults to returning the latest version of the FundConfiguration definition if not specified. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;FundConfiguration&#39; domain to decorate onto the FundConfiguration.              These must take the format {domain}/{scope}/{code}, for example &#39;FundConfiguration/Manager/Id&#39;. If no properties are specified, then no properties will be returned. | [optional] 

### Return type

[**FundConfiguration**](FundConfiguration.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested FundConfiguration definition. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_fund_configurations**
> PagedResourceListOfFundConfiguration list_fund_configurations(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)

[EXPERIMENTAL] ListFundConfigurations: List FundConfiguration.

List all the FundConfiguration matching particular criteria.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    FundConfigurationsApi
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
        api_instance = api_client_factory.build(FundConfigurationsApi)
        effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to list the TimeVariant properties for the FundConfiguration.              Defaults to the current LUSID system datetime if not specified. (optional)
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the FundConfiguration. Defaults to returning the latest version of each FundConfiguration if not specified. (optional)
        page = 'page_example' # str | The pagination token to use to continue listing FundConfiguration; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. (optional)
        limit = 56 # int | When paginating, limit the results to this number. Defaults to 100 if not specified. (optional)
        filter = 'filter_example' # str | Expression to filter the results.              For example, to filter on the FundConfiguration type, specify \"id.Code eq 'FundConfiguration1'\". For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. (optional)
        sort_by = ['sort_by_example'] # List[str] | A list of field names or properties to sort by, each suffixed by \" ASC\" or \" DESC\". (optional)
        property_keys = ['property_keys_example'] # List[str] | A list of property keys from the 'FundConfiguration' domain to decorate onto each FundConfiguration.              These must take the format {domain}/{scope}/{code}, for example 'FundConfiguration/Manager/Id'. (optional)

        try:
            # [EXPERIMENTAL] ListFundConfigurations: List FundConfiguration.
            api_response = await api_instance.list_fund_configurations(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling FundConfigurationsApi->list_fund_configurations: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **effective_at** | **str**| The effective datetime or cut label at which to list the TimeVariant properties for the FundConfiguration.              Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the FundConfiguration. Defaults to returning the latest version of each FundConfiguration if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing FundConfiguration; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results.              For example, to filter on the FundConfiguration type, specify \&quot;id.Code eq &#39;FundConfiguration1&#39;\&quot;. For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;FundConfiguration&#39; domain to decorate onto each FundConfiguration.              These must take the format {domain}/{scope}/{code}, for example &#39;FundConfiguration/Manager/Id&#39;. | [optional] 

### Return type

[**PagedResourceListOfFundConfiguration**](PagedResourceListOfFundConfiguration.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Fund configurations. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **upsert_fund_configuration_properties**
> FundConfigurationProperties upsert_fund_configuration_properties(scope, code, request_body=request_body)

[EXPERIMENTAL] UpsertFundConfigurationProperties: Upsert FundConfiguration properties

Update or insert one or more properties onto a single FundConfiguration. A property will be updated if it  already exists and inserted if it does not. All properties must be of the domain 'FundConfiguration'.                Upserting a property that exists for an FundConfiguration, with a null value, will delete the instance of the property for that group.                Properties have an <i>effectiveFrom</i> datetime for which the property is valid, and an <i>effectiveUntil</i>  datetime until which the property is valid. Not supplying an <i>effectiveUntil</i> datetime results in the property being  valid indefinitely, or until the next <i>effectiveFrom</i> datetime of the property.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    FundConfigurationsApi
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
        api_instance = api_client_factory.build(FundConfigurationsApi)
        scope = 'scope_example' # str | The scope of the FundConfiguration to update or insert the properties onto.
        code = 'code_example' # str | The code of the FundConfiguration to update or insert the properties onto. Together with the scope this uniquely identifies the FundConfiguration.
        request_body = {"FundConfiguration/MyScope/FundManagerName":{"key":"FundConfiguration/MyScope/FundManagerName","value":{"labelValue":"Smith"},"effectiveFrom":"2018-03-05T00:00:00.0000000+00:00"},"FundConfiguration/MyScope/SomeProperty":{"key":"FundConfiguration/MyScope/SomeProperty","value":{"labelValue":"SomeValue"},"effectiveFrom":"2016-01-01T00:00:00.0000000+00:00"},"FundConfiguration/MyScope/AnotherProperty":{"key":"FundConfiguration/MyScope/AnotherProperty","value":{"labelValue":"AnotherValue"},"effectiveFrom":"2018-03-05T00:00:00.0000000+00:00","effectiveUntil":"2020-01-01T00:00:00.0000000+00:00"},"FundConfiguration/MyScope/ReBalanceInterval":{"key":"FundConfiguration/MyScope/ReBalanceInterval","value":{"metricValue":{"value":30,"unit":"Days"}}}} # Dict[str, ModelProperty] | The properties to be updated or inserted onto the Fund Configuration. Each property in               the request must be keyed by its unique property key. This has the format {domain}/{scope}/{code} e.g. \"FundConfiguration/Manager/Id\". (optional)

        try:
            # [EXPERIMENTAL] UpsertFundConfigurationProperties: Upsert FundConfiguration properties
            api_response = await api_instance.upsert_fund_configuration_properties(scope, code, request_body=request_body)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling FundConfigurationsApi->upsert_fund_configuration_properties: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the FundConfiguration to update or insert the properties onto. | 
 **code** | **str**| The code of the FundConfiguration to update or insert the properties onto. Together with the scope this uniquely identifies the FundConfiguration. | 
 **request_body** | [**Dict[str, ModelProperty]**](ModelProperty.md)| The properties to be updated or inserted onto the Fund Configuration. Each property in               the request must be keyed by its unique property key. This has the format {domain}/{scope}/{code} e.g. \&quot;FundConfiguration/Manager/Id\&quot;. | [optional] 

### Return type

[**FundConfigurationProperties**](FundConfigurationProperties.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated or inserted properties |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

