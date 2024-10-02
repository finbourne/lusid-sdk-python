# lusid.FeeTypesApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_fee_type**](FeeTypesApi.md#create_fee_type) | **POST** /api/feetypes/{scope} | [EXPERIMENTAL] CreateFeeType: Create a FeeType.
[**delete_fee_type**](FeeTypesApi.md#delete_fee_type) | **DELETE** /api/feetypes/{scope}/{code} | [EXPERIMENTAL] DeleteFeeType: Delete a FeeType.
[**get_fee_template_specifications**](FeeTypesApi.md#get_fee_template_specifications) | **GET** /api/feetypes/feetransactiontemplatespecification | [EXPERIMENTAL] GetFeeTemplateSpecifications: Get FeeTemplateSpecifications used in the FeeType.
[**get_fee_type**](FeeTypesApi.md#get_fee_type) | **GET** /api/feetypes/{scope}/{code} | [EXPERIMENTAL] GetFeeType: Get a FeeType
[**list_fee_types**](FeeTypesApi.md#list_fee_types) | **GET** /api/feetypes | [EXPERIMENTAL] ListFeeTypes: List FeeTypes
[**update_fee_type**](FeeTypesApi.md#update_fee_type) | **PUT** /api/feetypes/{scope}/{code} | [EXPERIMENTAL] UpdateFeeType: Update a FeeType.


# **create_fee_type**
> FeeType create_fee_type(scope, fee_type_request)

[EXPERIMENTAL] CreateFeeType: Create a FeeType.

Create a FeeType that contains templates used to create fee transactions.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    FeeTypesApi
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
        api_instance = api_client_factory.build(FeeTypesApi)
        scope = 'scope_example' # str | The scope of the FeeType.

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # fee_type_request = FeeTypeRequest.from_json("")
        # fee_type_request = FeeTypeRequest.from_dict({})
        fee_type_request = FeeTypeRequest()

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.create_fee_type(scope, fee_type_request, opts=opts)

            # [EXPERIMENTAL] CreateFeeType: Create a FeeType.
            api_response = await api_instance.create_fee_type(scope, fee_type_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling FeeTypesApi->create_fee_type: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the FeeType. | 
 **fee_type_request** | [**FeeTypeRequest**](FeeTypeRequest.md)| The contents of the FeeType. | 

### Return type

[**FeeType**](FeeType.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Create a FeeType. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_fee_type**
> DeletedEntityResponse delete_fee_type(scope, code)

[EXPERIMENTAL] DeleteFeeType: Delete a FeeType.

Delete a FeeType that contains templates used to create fee transactions.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    FeeTypesApi
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
        api_instance = api_client_factory.build(FeeTypesApi)
        scope = 'scope_example' # str | The scope of the FeeType.
        code = 'code_example' # str | The code of the fee type

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.delete_fee_type(scope, code, opts=opts)

            # [EXPERIMENTAL] DeleteFeeType: Delete a FeeType.
            api_response = await api_instance.delete_fee_type(scope, code)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling FeeTypesApi->delete_fee_type: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the FeeType. | 
 **code** | **str**| The code of the fee type | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete a FeeType. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_fee_template_specifications**
> FeeTransactionTemplateSpecification get_fee_template_specifications()

[EXPERIMENTAL] GetFeeTemplateSpecifications: Get FeeTemplateSpecifications used in the FeeType.

Get FeeTemplateSpecifications used in the FeeType.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    FeeTypesApi
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
        api_instance = api_client_factory.build(FeeTypesApi)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.get_fee_template_specifications(opts=opts)

            # [EXPERIMENTAL] GetFeeTemplateSpecifications: Get FeeTemplateSpecifications used in the FeeType.
            api_response = await api_instance.get_fee_template_specifications()
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling FeeTypesApi->get_fee_template_specifications: %s\n" % e)

asyncio.run(main())
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**FeeTransactionTemplateSpecification**](FeeTransactionTemplateSpecification.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fee template specifications used with a FeeType. |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_fee_type**
> FeeType get_fee_type(scope, code, as_at=as_at)

[EXPERIMENTAL] GetFeeType: Get a FeeType

Get a FeeType that contains templates used to create fee transactions.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    FeeTypesApi
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
        api_instance = api_client_factory.build(FeeTypesApi)
        scope = 'scope_example' # str | The scope of the FeeType
        code = 'code_example' # str | The code of the FeeType
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the FeeType. Defaults to returning the latest version of the FeeType, if not specified. (optional)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.get_fee_type(scope, code, as_at=as_at, opts=opts)

            # [EXPERIMENTAL] GetFeeType: Get a FeeType
            api_response = await api_instance.get_fee_type(scope, code, as_at=as_at)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling FeeTypesApi->get_fee_type: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the FeeType | 
 **code** | **str**| The code of the FeeType | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the FeeType. Defaults to returning the latest version of the FeeType, if not specified. | [optional] 

### Return type

[**FeeType**](FeeType.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested FeeType. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_fee_types**
> PagedResourceListOfFeeType list_fee_types(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)

[EXPERIMENTAL] ListFeeTypes: List FeeTypes

List FeeTypes that contain templates used to create fee transactions.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    FeeTypesApi
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
        api_instance = api_client_factory.build(FeeTypesApi)
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the FeeTypes. Defaults to returning the latest version of each FeeType if not specified. (optional)
        page = 'page_example' # str | The pagination token to use to continue listing FeeTypes; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. (optional)
        limit = 56 # int | When paginating, limit the results to this number. Defaults to 100 if not specified. (optional)
        filter = 'filter_example' # str | Expression to filter the results.              For example, to filter on the Code of the FeeType type, specify \"id.Code eq 'FeeType1'\". For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. (optional)
        sort_by = ['sort_by_example'] # List[str] | A list of field names or properties to sort by, each suffixed by \" ASC\" or \" DESC\" (optional)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.list_fee_types(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, opts=opts)

            # [EXPERIMENTAL] ListFeeTypes: List FeeTypes
            api_response = await api_instance.list_fee_types(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling FeeTypesApi->list_fee_types: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list the FeeTypes. Defaults to returning the latest version of each FeeType if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing FeeTypes; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results.              For example, to filter on the Code of the FeeType type, specify \&quot;id.Code eq &#39;FeeType1&#39;\&quot;. For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot; | [optional] 

### Return type

[**PagedResourceListOfFeeType**](PagedResourceListOfFeeType.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Fee Types |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **update_fee_type**
> FeeType update_fee_type(scope, code, update_fee_type_request)

[EXPERIMENTAL] UpdateFeeType: Update a FeeType.

Update a FeeType that contains templates used to create fee transactions.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    FeeTypesApi
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
        api_instance = api_client_factory.build(FeeTypesApi)
        scope = 'scope_example' # str | The scope of the FeeType.
        code = 'code_example' # str | The code of the fee type

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # update_fee_type_request = UpdateFeeTypeRequest.from_json("")
        # update_fee_type_request = UpdateFeeTypeRequest.from_dict({})
        update_fee_type_request = UpdateFeeTypeRequest()

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.update_fee_type(scope, code, update_fee_type_request, opts=opts)

            # [EXPERIMENTAL] UpdateFeeType: Update a FeeType.
            api_response = await api_instance.update_fee_type(scope, code, update_fee_type_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling FeeTypesApi->update_fee_type: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the FeeType. | 
 **code** | **str**| The code of the fee type | 
 **update_fee_type_request** | [**UpdateFeeTypeRequest**](UpdateFeeTypeRequest.md)| The contents of the FeeType. | 

### Return type

[**FeeType**](FeeType.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update a FeeType. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

