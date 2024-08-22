# lusid.WorkspaceApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_personal_item**](WorkspaceApi.md#create_personal_item) | **POST** /api/workspaces/personal/{workspaceName}/items | [EXPERIMENTAL] CreatePersonalItem: Create a new item in a personal workspace.
[**create_personal_workspace**](WorkspaceApi.md#create_personal_workspace) | **POST** /api/workspaces/personal | [EXPERIMENTAL] CreatePersonalWorkspace: Create a new personal workspace.
[**create_shared_item**](WorkspaceApi.md#create_shared_item) | **POST** /api/workspaces/shared/{workspaceName}/items | [EXPERIMENTAL] CreateSharedItem: Create a new item in a shared workspace.
[**create_shared_workspace**](WorkspaceApi.md#create_shared_workspace) | **POST** /api/workspaces/shared | [EXPERIMENTAL] CreateSharedWorkspace: Create a new shared workspace.
[**delete_personal_item**](WorkspaceApi.md#delete_personal_item) | **DELETE** /api/workspaces/personal/{workspaceName}/items/{itemName} | [EXPERIMENTAL] DeletePersonalItem: Delete an item from a personal workspace.
[**delete_personal_workspace**](WorkspaceApi.md#delete_personal_workspace) | **DELETE** /api/workspaces/personal/{workspaceName} | [EXPERIMENTAL] DeletePersonalWorkspace: Delete a personal workspace.
[**delete_shared_item**](WorkspaceApi.md#delete_shared_item) | **DELETE** /api/workspaces/shared/{workspaceName}/items/{itemName} | [EXPERIMENTAL] DeleteSharedItem: Delete an item from a shared workspace.
[**delete_shared_workspace**](WorkspaceApi.md#delete_shared_workspace) | **DELETE** /api/workspaces/shared/{workspaceName} | [EXPERIMENTAL] DeleteSharedWorkspace: Delete a shared workspace.
[**get_personal_item**](WorkspaceApi.md#get_personal_item) | **GET** /api/workspaces/personal/{workspaceName}/items/{itemName} | [EXPERIMENTAL] GetPersonalItem: Get a single personal workspace item.
[**get_personal_workspace**](WorkspaceApi.md#get_personal_workspace) | **GET** /api/workspaces/personal/{workspaceName} | [EXPERIMENTAL] GetPersonalWorkspace: Get a personal workspace.
[**get_shared_item**](WorkspaceApi.md#get_shared_item) | **GET** /api/workspaces/shared/{workspaceName}/items/{itemName} | [EXPERIMENTAL] GetSharedItem: Get a single shared workspace item.
[**get_shared_workspace**](WorkspaceApi.md#get_shared_workspace) | **GET** /api/workspaces/shared/{workspaceName} | [EXPERIMENTAL] GetSharedWorkspace: Get a shared workspace.
[**list_personal_items**](WorkspaceApi.md#list_personal_items) | **GET** /api/workspaces/personal/{workspaceName}/items | [EXPERIMENTAL] ListPersonalItems: List the items in a personal workspace.
[**list_personal_workspaces**](WorkspaceApi.md#list_personal_workspaces) | **GET** /api/workspaces/personal | [EXPERIMENTAL] ListPersonalWorkspaces: List personal workspaces.
[**list_shared_items**](WorkspaceApi.md#list_shared_items) | **GET** /api/workspaces/shared/{workspaceName}/items | [EXPERIMENTAL] ListSharedItems: List the items in a shared workspace.
[**list_shared_workspaces**](WorkspaceApi.md#list_shared_workspaces) | **GET** /api/workspaces/shared | [EXPERIMENTAL] ListSharedWorkspaces: List shared workspaces.
[**update_personal_item**](WorkspaceApi.md#update_personal_item) | **PUT** /api/workspaces/personal/{workspaceName}/items/{itemName} | [EXPERIMENTAL] UpdatePersonalItem: Update an item in a personal workspace.
[**update_personal_workspace**](WorkspaceApi.md#update_personal_workspace) | **PUT** /api/workspaces/personal/{workspaceName} | [EXPERIMENTAL] UpdatePersonalWorkspace: Update a personal workspace.
[**update_shared_item**](WorkspaceApi.md#update_shared_item) | **PUT** /api/workspaces/shared/{workspaceName}/items/{itemName} | [EXPERIMENTAL] UpdateSharedItem: Update an item in a shared workspace.
[**update_shared_workspace**](WorkspaceApi.md#update_shared_workspace) | **PUT** /api/workspaces/shared/{workspaceName} | [EXPERIMENTAL] UpdateSharedWorkspace: Update a shared workspace.


# **create_personal_item**
> WorkspaceItem create_personal_item(workspace_name, workspace_item_creation_request=workspace_item_creation_request)

[EXPERIMENTAL] CreatePersonalItem: Create a new item in a personal workspace.

Create a new item in a personal workspace.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    WorkspaceApi
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
        api_instance = api_client_factory.build(WorkspaceApi)
        workspace_name = 'workspace_name_example' # str | The item's workspace name.

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # workspace_item_creation_request = WorkspaceItemCreationRequest()
        # workspace_item_creation_request = WorkspaceItemCreationRequest.from_json("")
        workspace_item_creation_request = WorkspaceItemCreationRequest.from_dict({"format":1,"name":"example-name","description":"example-description","content":"example-content"}) # WorkspaceItemCreationRequest | The item to be created. (optional)

        try:
            # [EXPERIMENTAL] CreatePersonalItem: Create a new item in a personal workspace.
            api_response = await api_instance.create_personal_item(workspace_name, workspace_item_creation_request=workspace_item_creation_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling WorkspaceApi->create_personal_item: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_name** | **str**| The item&#39;s workspace name. | 
 **workspace_item_creation_request** | [**WorkspaceItemCreationRequest**](WorkspaceItemCreationRequest.md)| The item to be created. | [optional] 

### Return type

[**WorkspaceItem**](WorkspaceItem.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The workspace item created. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **create_personal_workspace**
> Workspace create_personal_workspace(workspace_creation_request=workspace_creation_request)

[EXPERIMENTAL] CreatePersonalWorkspace: Create a new personal workspace.

Create a new personal workspace.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    WorkspaceApi
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
        api_instance = api_client_factory.build(WorkspaceApi)

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # workspace_creation_request = WorkspaceCreationRequest()
        # workspace_creation_request = WorkspaceCreationRequest.from_json("")
        workspace_creation_request = WorkspaceCreationRequest.from_dict({"name":"example-name","description":"example description"}) # WorkspaceCreationRequest | The workspace to be created. (optional)

        try:
            # [EXPERIMENTAL] CreatePersonalWorkspace: Create a new personal workspace.
            api_response = await api_instance.create_personal_workspace(workspace_creation_request=workspace_creation_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling WorkspaceApi->create_personal_workspace: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_creation_request** | [**WorkspaceCreationRequest**](WorkspaceCreationRequest.md)| The workspace to be created. | [optional] 

### Return type

[**Workspace**](Workspace.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The workspace created. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **create_shared_item**
> WorkspaceItem create_shared_item(workspace_name, workspace_item_creation_request=workspace_item_creation_request)

[EXPERIMENTAL] CreateSharedItem: Create a new item in a shared workspace.

Create a new item in a shared workspace.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    WorkspaceApi
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
        api_instance = api_client_factory.build(WorkspaceApi)
        workspace_name = 'workspace_name_example' # str | The item's workspace name.

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # workspace_item_creation_request = WorkspaceItemCreationRequest()
        # workspace_item_creation_request = WorkspaceItemCreationRequest.from_json("")
        workspace_item_creation_request = WorkspaceItemCreationRequest.from_dict({"format":1,"name":"example-name","description":"example-description","content":"example-content"}) # WorkspaceItemCreationRequest | The item to be created. (optional)

        try:
            # [EXPERIMENTAL] CreateSharedItem: Create a new item in a shared workspace.
            api_response = await api_instance.create_shared_item(workspace_name, workspace_item_creation_request=workspace_item_creation_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling WorkspaceApi->create_shared_item: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_name** | **str**| The item&#39;s workspace name. | 
 **workspace_item_creation_request** | [**WorkspaceItemCreationRequest**](WorkspaceItemCreationRequest.md)| The item to be created. | [optional] 

### Return type

[**WorkspaceItem**](WorkspaceItem.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The workspace item created. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **create_shared_workspace**
> Workspace create_shared_workspace(workspace_creation_request=workspace_creation_request)

[EXPERIMENTAL] CreateSharedWorkspace: Create a new shared workspace.

Create a new shared workspace.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    WorkspaceApi
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
        api_instance = api_client_factory.build(WorkspaceApi)

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # workspace_creation_request = WorkspaceCreationRequest()
        # workspace_creation_request = WorkspaceCreationRequest.from_json("")
        workspace_creation_request = WorkspaceCreationRequest.from_dict({"name":"example-name","description":"example description"}) # WorkspaceCreationRequest | The workspace to be created. (optional)

        try:
            # [EXPERIMENTAL] CreateSharedWorkspace: Create a new shared workspace.
            api_response = await api_instance.create_shared_workspace(workspace_creation_request=workspace_creation_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling WorkspaceApi->create_shared_workspace: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_creation_request** | [**WorkspaceCreationRequest**](WorkspaceCreationRequest.md)| The workspace to be created. | [optional] 

### Return type

[**Workspace**](Workspace.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The workspace created. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_personal_item**
> DeletedEntityResponse delete_personal_item(workspace_name, item_name)

[EXPERIMENTAL] DeletePersonalItem: Delete an item from a personal workspace.

Delete an item from a personal workspace.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    WorkspaceApi
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
        api_instance = api_client_factory.build(WorkspaceApi)
        workspace_name = 'workspace_name_example' # str | The name of the personal workspace.
        item_name = 'item_name_example' # str | The name of the item.

        try:
            # [EXPERIMENTAL] DeletePersonalItem: Delete an item from a personal workspace.
            api_response = await api_instance.delete_personal_item(workspace_name, item_name)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling WorkspaceApi->delete_personal_item: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_name** | **str**| The name of the personal workspace. | 
 **item_name** | **str**| The name of the item. | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The result of deleting a personal workspace item. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_personal_workspace**
> DeletedEntityResponse delete_personal_workspace(workspace_name)

[EXPERIMENTAL] DeletePersonalWorkspace: Delete a personal workspace.

Delete a personal workspace.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    WorkspaceApi
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
        api_instance = api_client_factory.build(WorkspaceApi)
        workspace_name = 'workspace_name_example' # str | The name of the personal workspace.

        try:
            # [EXPERIMENTAL] DeletePersonalWorkspace: Delete a personal workspace.
            api_response = await api_instance.delete_personal_workspace(workspace_name)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling WorkspaceApi->delete_personal_workspace: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_name** | **str**| The name of the personal workspace. | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The result of deleting a personal workspace. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_shared_item**
> DeletedEntityResponse delete_shared_item(workspace_name, item_name)

[EXPERIMENTAL] DeleteSharedItem: Delete an item from a shared workspace.

Delete an item from a shared workspace.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    WorkspaceApi
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
        api_instance = api_client_factory.build(WorkspaceApi)
        workspace_name = 'workspace_name_example' # str | The name of the shared workspace.
        item_name = 'item_name_example' # str | The name of the item.

        try:
            # [EXPERIMENTAL] DeleteSharedItem: Delete an item from a shared workspace.
            api_response = await api_instance.delete_shared_item(workspace_name, item_name)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling WorkspaceApi->delete_shared_item: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_name** | **str**| The name of the shared workspace. | 
 **item_name** | **str**| The name of the item. | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The result of deleting a shared workspace item. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_shared_workspace**
> DeletedEntityResponse delete_shared_workspace(workspace_name)

[EXPERIMENTAL] DeleteSharedWorkspace: Delete a shared workspace.

Delete a shared workspace.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    WorkspaceApi
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
        api_instance = api_client_factory.build(WorkspaceApi)
        workspace_name = 'workspace_name_example' # str | The name of the shared workspace.

        try:
            # [EXPERIMENTAL] DeleteSharedWorkspace: Delete a shared workspace.
            api_response = await api_instance.delete_shared_workspace(workspace_name)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling WorkspaceApi->delete_shared_workspace: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_name** | **str**| The name of the shared workspace. | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The result of deleting a shared workspace. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_personal_item**
> WorkspaceItem get_personal_item(workspace_name, item_name, as_at=as_at)

[EXPERIMENTAL] GetPersonalItem: Get a single personal workspace item.

Get a single personal workspace item.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    WorkspaceApi
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
        api_instance = api_client_factory.build(WorkspaceApi)
        workspace_name = 'workspace_name_example' # str | The name of the personal workspace.
        item_name = 'item_name_example' # str | The name of the item.
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The datetime at which to request the workspace item. If not provided, defaults to 'latest'. (optional)

        try:
            # [EXPERIMENTAL] GetPersonalItem: Get a single personal workspace item.
            api_response = await api_instance.get_personal_item(workspace_name, item_name, as_at=as_at)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling WorkspaceApi->get_personal_item: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_name** | **str**| The name of the personal workspace. | 
 **item_name** | **str**| The name of the item. | 
 **as_at** | **datetime**| The datetime at which to request the workspace item. If not provided, defaults to &#39;latest&#39;. | [optional] 

### Return type

[**WorkspaceItem**](WorkspaceItem.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The workspace item requested. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_personal_workspace**
> Workspace get_personal_workspace(workspace_name, as_at=as_at)

[EXPERIMENTAL] GetPersonalWorkspace: Get a personal workspace.

Get a personal workspace.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    WorkspaceApi
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
        api_instance = api_client_factory.build(WorkspaceApi)
        workspace_name = 'workspace_name_example' # str | The personal workspace name.
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve workspaces. Defaults to 'latest' if not specified. (optional)

        try:
            # [EXPERIMENTAL] GetPersonalWorkspace: Get a personal workspace.
            api_response = await api_instance.get_personal_workspace(workspace_name, as_at=as_at)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling WorkspaceApi->get_personal_workspace: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_name** | **str**| The personal workspace name. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve workspaces. Defaults to &#39;latest&#39; if not specified. | [optional] 

### Return type

[**Workspace**](Workspace.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The personal workspace. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_shared_item**
> WorkspaceItem get_shared_item(workspace_name, item_name, as_at=as_at)

[EXPERIMENTAL] GetSharedItem: Get a single shared workspace item.

Get a single shared workspace item.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    WorkspaceApi
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
        api_instance = api_client_factory.build(WorkspaceApi)
        workspace_name = 'workspace_name_example' # str | The name of the shared workspace.
        item_name = 'item_name_example' # str | The name of the item.
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The datetime at which to request the workspace item. If not provided, defaults to 'latest'. (optional)

        try:
            # [EXPERIMENTAL] GetSharedItem: Get a single shared workspace item.
            api_response = await api_instance.get_shared_item(workspace_name, item_name, as_at=as_at)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling WorkspaceApi->get_shared_item: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_name** | **str**| The name of the shared workspace. | 
 **item_name** | **str**| The name of the item. | 
 **as_at** | **datetime**| The datetime at which to request the workspace item. If not provided, defaults to &#39;latest&#39;. | [optional] 

### Return type

[**WorkspaceItem**](WorkspaceItem.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The workspace item requested. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_shared_workspace**
> Workspace get_shared_workspace(workspace_name, as_at=as_at)

[EXPERIMENTAL] GetSharedWorkspace: Get a shared workspace.

Get a shared workspace.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    WorkspaceApi
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
        api_instance = api_client_factory.build(WorkspaceApi)
        workspace_name = 'workspace_name_example' # str | The shared workspace name.
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve workspaces. Defaults to 'latest' if not specified. (optional)

        try:
            # [EXPERIMENTAL] GetSharedWorkspace: Get a shared workspace.
            api_response = await api_instance.get_shared_workspace(workspace_name, as_at=as_at)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling WorkspaceApi->get_shared_workspace: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_name** | **str**| The shared workspace name. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve workspaces. Defaults to &#39;latest&#39; if not specified. | [optional] 

### Return type

[**Workspace**](Workspace.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The shared workspace. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_personal_items**
> PagedResourceListOfWorkspaceItem list_personal_items(workspace_name, as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter)

[EXPERIMENTAL] ListPersonalItems: List the items in a personal workspace.

List the items in a personal workspace.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    WorkspaceApi
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
        api_instance = api_client_factory.build(WorkspaceApi)
        workspace_name = 'workspace_name_example' # str | The item's workspace name.
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve workspace items. Defaults to 'latest' if not specified. (optional)
        page = 'page_example' # str | The pagination token to use to continue listing workspaces items from a previous call to list workspaces items.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields              must not have changed since the original request. (optional)
        sort_by = ['sort_by_example'] # List[str] | A list of field names to sort by, each suffixed by \" ASC\" or \" DESC\". (optional)
        limit = 56 # int | When paginating, limit the number of returned results to this many. (optional)
        filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid. (optional)

        try:
            # [EXPERIMENTAL] ListPersonalItems: List the items in a personal workspace.
            api_response = await api_instance.list_personal_items(workspace_name, as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling WorkspaceApi->list_personal_items: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_name** | **str**| The item&#39;s workspace name. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve workspace items. Defaults to &#39;latest&#39; if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing workspaces items from a previous call to list workspaces items.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields              must not have changed since the original request. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid. | [optional] 

### Return type

[**PagedResourceListOfWorkspaceItem**](PagedResourceListOfWorkspaceItem.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The items in a personal workspace. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_personal_workspaces**
> PagedResourceListOfWorkspace list_personal_workspaces(as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter)

[EXPERIMENTAL] ListPersonalWorkspaces: List personal workspaces.

List personal workspaces.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    WorkspaceApi
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
        api_instance = api_client_factory.build(WorkspaceApi)
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve workspaces. Defaults to 'latest' if not specified. (optional)
        page = 'page_example' # str | The pagination token to use to continue listing workspaces from a previous call to list workspaces.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields              must not have changed since the original request. (optional)
        sort_by = ['sort_by_example'] # List[str] | A list of field names to sort by, each suffixed by \" ASC\" or \" DESC\". (optional)
        limit = 56 # int | When paginating, limit the number of returned results to this many. (optional)
        filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid. (optional)

        try:
            # [EXPERIMENTAL] ListPersonalWorkspaces: List personal workspaces.
            api_response = await api_instance.list_personal_workspaces(as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling WorkspaceApi->list_personal_workspaces: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to retrieve workspaces. Defaults to &#39;latest&#39; if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing workspaces from a previous call to list workspaces.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields              must not have changed since the original request. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid. | [optional] 

### Return type

[**PagedResourceListOfWorkspace**](PagedResourceListOfWorkspace.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The personal workspaces. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_shared_items**
> PagedResourceListOfWorkspaceItem list_shared_items(workspace_name, as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter)

[EXPERIMENTAL] ListSharedItems: List the items in a shared workspace.

List the items in a shared workspace.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    WorkspaceApi
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
        api_instance = api_client_factory.build(WorkspaceApi)
        workspace_name = 'workspace_name_example' # str | The item's workspace name.
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve workspace items. Defaults to 'latest' if not specified. (optional)
        page = 'page_example' # str | The pagination token to use to continue listing workspaces items from a previous call to list workspaces items.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields              must not have changed since the original request. (optional)
        sort_by = ['sort_by_example'] # List[str] | A list of field names to sort by, each suffixed by \" ASC\" or \" DESC\". (optional)
        limit = 56 # int | When paginating, limit the number of returned results to this many. (optional)
        filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid. (optional)

        try:
            # [EXPERIMENTAL] ListSharedItems: List the items in a shared workspace.
            api_response = await api_instance.list_shared_items(workspace_name, as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling WorkspaceApi->list_shared_items: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_name** | **str**| The item&#39;s workspace name. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve workspace items. Defaults to &#39;latest&#39; if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing workspaces items from a previous call to list workspaces items.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields              must not have changed since the original request. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid. | [optional] 

### Return type

[**PagedResourceListOfWorkspaceItem**](PagedResourceListOfWorkspaceItem.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The items in a shared workspace. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_shared_workspaces**
> PagedResourceListOfWorkspace list_shared_workspaces(as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter)

[EXPERIMENTAL] ListSharedWorkspaces: List shared workspaces.

List shared workspaces.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    WorkspaceApi
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
        api_instance = api_client_factory.build(WorkspaceApi)
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve workspaces. Defaults to 'latest' if not specified. (optional)
        page = 'page_example' # str | The pagination token to use to continue listing workspaces from a previous call to list workspaces.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields              must not have changed since the original request. (optional)
        sort_by = ['sort_by_example'] # List[str] | A list of field names to sort by, each suffixed by \" ASC\" or \" DESC\". (optional)
        limit = 56 # int | When paginating, limit the number of returned results to this many. (optional)
        filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid. (optional)

        try:
            # [EXPERIMENTAL] ListSharedWorkspaces: List shared workspaces.
            api_response = await api_instance.list_shared_workspaces(as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling WorkspaceApi->list_shared_workspaces: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to retrieve workspaces. Defaults to &#39;latest&#39; if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing workspaces from a previous call to list workspaces.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields              must not have changed since the original request. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid. | [optional] 

### Return type

[**PagedResourceListOfWorkspace**](PagedResourceListOfWorkspace.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The shared workspaces. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **update_personal_item**
> WorkspaceItem update_personal_item(workspace_name, item_name, workspace_item_update_request=workspace_item_update_request)

[EXPERIMENTAL] UpdatePersonalItem: Update an item in a personal workspace.

Update an item in a personal workspace.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    WorkspaceApi
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
        api_instance = api_client_factory.build(WorkspaceApi)
        workspace_name = 'workspace_name_example' # str | The personal workspace name.
        item_name = 'item_name_example' # str | The item name.

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # workspace_item_update_request = WorkspaceItemUpdateRequest()
        # workspace_item_update_request = WorkspaceItemUpdateRequest.from_json("")
        workspace_item_update_request = WorkspaceItemUpdateRequest.from_dict({"format":2,"description":"updated-example-description","content":"updated-example-content"}) # WorkspaceItemUpdateRequest | The new item details. (optional)

        try:
            # [EXPERIMENTAL] UpdatePersonalItem: Update an item in a personal workspace.
            api_response = await api_instance.update_personal_item(workspace_name, item_name, workspace_item_update_request=workspace_item_update_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling WorkspaceApi->update_personal_item: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_name** | **str**| The personal workspace name. | 
 **item_name** | **str**| The item name. | 
 **workspace_item_update_request** | [**WorkspaceItemUpdateRequest**](WorkspaceItemUpdateRequest.md)| The new item details. | [optional] 

### Return type

[**WorkspaceItem**](WorkspaceItem.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The workspace item updated. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **update_personal_workspace**
> Workspace update_personal_workspace(workspace_name, workspace_update_request=workspace_update_request)

[EXPERIMENTAL] UpdatePersonalWorkspace: Update a personal workspace.

Update a personal workspace.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    WorkspaceApi
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
        api_instance = api_client_factory.build(WorkspaceApi)
        workspace_name = 'workspace_name_example' # str | The personal workspace name.

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # workspace_update_request = WorkspaceUpdateRequest()
        # workspace_update_request = WorkspaceUpdateRequest.from_json("")
        workspace_update_request = WorkspaceUpdateRequest.from_dict({"description":"updated example description"}) # WorkspaceUpdateRequest | The new workspace details. (optional)

        try:
            # [EXPERIMENTAL] UpdatePersonalWorkspace: Update a personal workspace.
            api_response = await api_instance.update_personal_workspace(workspace_name, workspace_update_request=workspace_update_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling WorkspaceApi->update_personal_workspace: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_name** | **str**| The personal workspace name. | 
 **workspace_update_request** | [**WorkspaceUpdateRequest**](WorkspaceUpdateRequest.md)| The new workspace details. | [optional] 

### Return type

[**Workspace**](Workspace.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The workspace updated. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **update_shared_item**
> WorkspaceItem update_shared_item(workspace_name, item_name, workspace_item_update_request=workspace_item_update_request)

[EXPERIMENTAL] UpdateSharedItem: Update an item in a shared workspace.

Update an item in a shared workspace.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    WorkspaceApi
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
        api_instance = api_client_factory.build(WorkspaceApi)
        workspace_name = 'workspace_name_example' # str | The shared workspace name.
        item_name = 'item_name_example' # str | The item name.

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # workspace_item_update_request = WorkspaceItemUpdateRequest()
        # workspace_item_update_request = WorkspaceItemUpdateRequest.from_json("")
        workspace_item_update_request = WorkspaceItemUpdateRequest.from_dict({"format":2,"description":"updated-example-description","content":"updated-example-content"}) # WorkspaceItemUpdateRequest | The new item details. (optional)

        try:
            # [EXPERIMENTAL] UpdateSharedItem: Update an item in a shared workspace.
            api_response = await api_instance.update_shared_item(workspace_name, item_name, workspace_item_update_request=workspace_item_update_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling WorkspaceApi->update_shared_item: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_name** | **str**| The shared workspace name. | 
 **item_name** | **str**| The item name. | 
 **workspace_item_update_request** | [**WorkspaceItemUpdateRequest**](WorkspaceItemUpdateRequest.md)| The new item details. | [optional] 

### Return type

[**WorkspaceItem**](WorkspaceItem.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The workspace item updated. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **update_shared_workspace**
> Workspace update_shared_workspace(workspace_name, workspace_update_request=workspace_update_request)

[EXPERIMENTAL] UpdateSharedWorkspace: Update a shared workspace.

Update a shared workspace.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    WorkspaceApi
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
        api_instance = api_client_factory.build(WorkspaceApi)
        workspace_name = 'workspace_name_example' # str | The shared workspace name.

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # workspace_update_request = WorkspaceUpdateRequest()
        # workspace_update_request = WorkspaceUpdateRequest.from_json("")
        workspace_update_request = WorkspaceUpdateRequest.from_dict({"description":"updated example description"}) # WorkspaceUpdateRequest | The new workspace details. (optional)

        try:
            # [EXPERIMENTAL] UpdateSharedWorkspace: Update a shared workspace.
            api_response = await api_instance.update_shared_workspace(workspace_name, workspace_update_request=workspace_update_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling WorkspaceApi->update_shared_workspace: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_name** | **str**| The shared workspace name. | 
 **workspace_update_request** | [**WorkspaceUpdateRequest**](WorkspaceUpdateRequest.md)| The new workspace details. | [optional] 

### Return type

[**Workspace**](Workspace.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The workspace updated. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

