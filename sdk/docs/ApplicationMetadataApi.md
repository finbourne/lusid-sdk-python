# lusid.ApplicationMetadataApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_excel_addin**](ApplicationMetadataApi.md#get_excel_addin) | **GET** /api/metadata/downloads/exceladdin | GetExcelAddin: Download Excel Addin
[**get_lusid_versions**](ApplicationMetadataApi.md#get_lusid_versions) | **GET** /api/metadata/versions | GetLusidVersions: Get LUSID versions
[**list_access_controlled_resources**](ApplicationMetadataApi.md#list_access_controlled_resources) | **GET** /api/metadata/access/resources | ListAccessControlledResources: Get resources available for access control


# **get_excel_addin**
> FileResponse get_excel_addin(version=version)

GetExcelAddin: Download Excel Addin

Download the LUSID Excel Addin for Microsoft Excel. Not providing a specific value will return the latest version being returned

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    ApplicationMetadataApi
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
        api_instance = api_client_factory.build(ApplicationMetadataApi)
        version = 'version_example' # str | The requested version of the Excel plugin (optional)

        try:
            # GetExcelAddin: Download Excel Addin
            api_response = await api_instance.get_excel_addin(version=version)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling ApplicationMetadataApi->get_excel_addin: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| The requested version of the Excel plugin | [optional] 

### Return type

[**FileResponse**](FileResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_lusid_versions**
> VersionSummaryDto get_lusid_versions()

GetLusidVersions: Get LUSID versions

Get the semantic versions associated with LUSID and its ecosystem

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    ApplicationMetadataApi
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
        api_instance = api_client_factory.build(ApplicationMetadataApi)

        try:
            # GetLusidVersions: Get LUSID versions
            api_response = await api_instance.get_lusid_versions()
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling ApplicationMetadataApi->get_lusid_versions: %s\n" % e)

asyncio.run(main())
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**VersionSummaryDto**](VersionSummaryDto.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Collection of versions associated with LUSID |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_access_controlled_resources**
> ResourceListOfAccessControlledResource list_access_controlled_resources(filter=filter)

ListAccessControlledResources: Get resources available for access control

Get the comprehensive set of resources that are available for access control

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    ApplicationMetadataApi
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
        api_instance = api_client_factory.build(ApplicationMetadataApi)
        filter = 'filter_example' # str | Optional. Expression to filter the result set.               For example, to filter on the Application, use \"application eq 'string'\"              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)

        try:
            # ListAccessControlledResources: Get resources available for access control
            api_response = await api_instance.list_access_controlled_resources(filter=filter)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling ApplicationMetadataApi->list_access_controlled_resources: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Optional. Expression to filter the result set.               For example, to filter on the Application, use \&quot;application eq &#39;string&#39;\&quot;              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 

### Return type

[**ResourceListOfAccessControlledResource**](ResourceListOfAccessControlledResource.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

