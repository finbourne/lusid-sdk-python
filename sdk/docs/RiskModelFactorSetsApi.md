# lusid.RiskModelFactorSetsApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_risk_model_factor_set**](RiskModelFactorSetsApi.md#create_risk_model_factor_set) | **POST** /api/riskmodels/factorsets | [EXPERIMENTAL] CreateRiskModelFactorSet: Create a Factor Set
[**delete_risk_model_factor_set**](RiskModelFactorSetsApi.md#delete_risk_model_factor_set) | **DELETE** /api/riskmodels/factorsets/{scope}/{code} | [EXPERIMENTAL] DeleteRiskModelFactorSet: Deletes a particular Factor Set
[**get_risk_model_factor_set**](RiskModelFactorSetsApi.md#get_risk_model_factor_set) | **GET** /api/riskmodels/factorsets/{scope}/{code} | [EXPERIMENTAL] GetRiskModelFactorSet: Get a single Factor Set by scope and code.
[**list_risk_model_factor_sets**](RiskModelFactorSetsApi.md#list_risk_model_factor_sets) | **GET** /api/riskmodels/factorsets | [EXPERIMENTAL] ListRiskModelFactorSets: Get a set of Factor Sets
[**update_risk_model_factor_set_name**](RiskModelFactorSetsApi.md#update_risk_model_factor_set_name) | **PUT** /api/riskmodels/factorsets/{scope}/{code} | [EXPERIMENTAL] UpdateRiskModelFactorSetName: Update Factor Set Display Name


# **create_risk_model_factor_set**
> RiskModelFactorSet create_risk_model_factor_set(create_risk_model_factor_set_request=create_risk_model_factor_set_request)

[EXPERIMENTAL] CreateRiskModelFactorSet: Create a Factor Set

Creates a factor set definition with a scoped Id and Name

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    RiskModelFactorSetsApi
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

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(RiskModelFactorSetsApi)

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # create_risk_model_factor_set_request = CreateRiskModelFactorSetRequest.from_json("")
        # create_risk_model_factor_set_request = CreateRiskModelFactorSetRequest.from_dict({})
        create_risk_model_factor_set_request = CreateRiskModelFactorSetRequest()

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.create_risk_model_factor_set(create_risk_model_factor_set_request=create_risk_model_factor_set_request, opts=opts)

            # [EXPERIMENTAL] CreateRiskModelFactorSet: Create a Factor Set
            api_response = await api_instance.create_risk_model_factor_set(create_risk_model_factor_set_request=create_risk_model_factor_set_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling RiskModelFactorSetsApi->create_risk_model_factor_set: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_risk_model_factor_set_request** | [**CreateRiskModelFactorSetRequest**](CreateRiskModelFactorSetRequest.md)| The request containing the details of the factor set | [optional] 

### Return type

[**RiskModelFactorSet**](RiskModelFactorSet.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created factor set. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_risk_model_factor_set**
> DeletedEntityResponse delete_risk_model_factor_set(scope, code)

[EXPERIMENTAL] DeleteRiskModelFactorSet: Deletes a particular Factor Set

The deletion will take effect from the factor set deletion datetime.  i.e. will no longer exist at any asAt datetime after the asAt datetime of deletion.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    RiskModelFactorSetsApi
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

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(RiskModelFactorSetsApi)
        scope = 'scope_example' # str | The scope of the specified factor set.
        code = 'code_example' # str | The code of the specified factor set. Together with the domain and scope this uniquely              identifies the factor set.

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.delete_risk_model_factor_set(scope, code, opts=opts)

            # [EXPERIMENTAL] DeleteRiskModelFactorSet: Deletes a particular Factor Set
            api_response = await api_instance.delete_risk_model_factor_set(scope, code)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling RiskModelFactorSetsApi->delete_risk_model_factor_set: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the specified factor set. | 
 **code** | **str**| The code of the specified factor set. Together with the domain and scope this uniquely              identifies the factor set. | 

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

# **get_risk_model_factor_set**
> RiskModelFactorSet get_risk_model_factor_set(scope, code, as_at=as_at)

[EXPERIMENTAL] GetRiskModelFactorSet: Get a single Factor Set by scope and code.

Retrieves one Factor Set by scope and code.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    RiskModelFactorSetsApi
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

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(RiskModelFactorSetsApi)
        scope = 'scope_example' # str | The scope of the specified factor set.
        code = 'code_example' # str | The code of the specified factor set. Together with the domain and scope this uniquely              identifies the factor set.
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the factor set definition. Defaults to return              the latest version of the definition if not specified. (optional)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.get_risk_model_factor_set(scope, code, as_at=as_at, opts=opts)

            # [EXPERIMENTAL] GetRiskModelFactorSet: Get a single Factor Set by scope and code.
            api_response = await api_instance.get_risk_model_factor_set(scope, code, as_at=as_at)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling RiskModelFactorSetsApi->get_risk_model_factor_set: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the specified factor set. | 
 **code** | **str**| The code of the specified factor set. Together with the domain and scope this uniquely              identifies the factor set. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the factor set definition. Defaults to return              the latest version of the definition if not specified. | [optional] 

### Return type

[**RiskModelFactorSet**](RiskModelFactorSet.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested factor set. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_risk_model_factor_sets**
> PagedResourceListOfRiskModelFactorSet list_risk_model_factor_sets(as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter)

[EXPERIMENTAL] ListRiskModelFactorSets: Get a set of Factor Sets

Retrieves all Factor Sets (without related Factors) that fit the filter, in a specific order if sortBy is provided.  Supports pagination

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    RiskModelFactorSetsApi
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

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(RiskModelFactorSetsApi)
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the factor sets. Defaults to return the latest              version of the factor sets if not specified. (optional)
        page = 'page_example' # str | The pagination token to use to continue listing factor sets from a previous call to list              factor sets. This value is returned from the previous call. If a pagination token is provided the sortBy,              filter, effectiveAt, and asAt fields must not have changed since the original request. (optional)
        sort_by = ['sort_by_example'] # List[str] | A list of field names to sort by, each suffixed by \" ASC\" or \" DESC\" (optional)
        limit = 56 # int | Page size. (optional)
        filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid. (optional)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.list_risk_model_factor_sets(as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter, opts=opts)

            # [EXPERIMENTAL] ListRiskModelFactorSets: Get a set of Factor Sets
            api_response = await api_instance.list_risk_model_factor_sets(as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling RiskModelFactorSetsApi->list_risk_model_factor_sets: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to retrieve the factor sets. Defaults to return the latest              version of the factor sets if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing factor sets from a previous call to list              factor sets. This value is returned from the previous call. If a pagination token is provided the sortBy,              filter, effectiveAt, and asAt fields must not have changed since the original request. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot; | [optional] 
 **limit** | **int**| Page size. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid. | [optional] 

### Return type

[**PagedResourceListOfRiskModelFactorSet**](PagedResourceListOfRiskModelFactorSet.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested list of factor sets. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **update_risk_model_factor_set_name**
> RiskModelFactorSet update_risk_model_factor_set_name(scope, code, update_risk_model_factor_set_request=update_risk_model_factor_set_request)

[EXPERIMENTAL] UpdateRiskModelFactorSetName: Update Factor Set Display Name

Overwrites an existing Factor Set as per scope and code from the route  Update request has a single property - DisplayName

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    RiskModelFactorSetsApi
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

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(RiskModelFactorSetsApi)
        scope = 'scope_example' # str | The scope of the specified factor set.
        code = 'code_example' # str | The code of the specified factor set. Together with the domain and scope this uniquely              identifies the factor set.

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # update_risk_model_factor_set_request = UpdateRiskModelFactorSetRequest.from_json("")
        # update_risk_model_factor_set_request = UpdateRiskModelFactorSetRequest.from_dict({})
        update_risk_model_factor_set_request = UpdateRiskModelFactorSetRequest()

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.update_risk_model_factor_set_name(scope, code, update_risk_model_factor_set_request=update_risk_model_factor_set_request, opts=opts)

            # [EXPERIMENTAL] UpdateRiskModelFactorSetName: Update Factor Set Display Name
            api_response = await api_instance.update_risk_model_factor_set_name(scope, code, update_risk_model_factor_set_request=update_risk_model_factor_set_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling RiskModelFactorSetsApi->update_risk_model_factor_set_name: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the specified factor set. | 
 **code** | **str**| The code of the specified factor set. Together with the domain and scope this uniquely              identifies the factor set. | 
 **update_risk_model_factor_set_request** | [**UpdateRiskModelFactorSetRequest**](UpdateRiskModelFactorSetRequest.md)| The request containing the updated name of the factor set. | [optional] 

### Return type

[**RiskModelFactorSet**](RiskModelFactorSet.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated version of the requested factor set. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

