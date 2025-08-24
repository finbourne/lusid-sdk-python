# lusid.WorkspaceApi

All URIs are relative to *https://fbn-prd.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_item**](WorkspaceApi.md#create_item) | **POST** /api/workspaces/{visibility}/{workspaceName}/items | [EXPERIMENTAL] CreateItem: Create a new item in a workspace.
[**create_workspace**](WorkspaceApi.md#create_workspace) | **POST** /api/workspaces/{visibility} | [EXPERIMENTAL] CreateWorkspace: Create a new workspace.
[**delete_item**](WorkspaceApi.md#delete_item) | **DELETE** /api/workspaces/{visibility}/{workspaceName}/items/{groupName}/{itemName} | [EXPERIMENTAL] DeleteItem: Delete an item from a workspace.
[**delete_workspace**](WorkspaceApi.md#delete_workspace) | **DELETE** /api/workspaces/{visibility}/{workspaceName} | [EXPERIMENTAL] DeleteWorkspace: Delete a workspace.
[**get_item**](WorkspaceApi.md#get_item) | **GET** /api/workspaces/{visibility}/{workspaceName}/items/{groupName}/{itemName} | [EXPERIMENTAL] GetItem: Get a single workspace item.
[**get_workspace**](WorkspaceApi.md#get_workspace) | **GET** /api/workspaces/{visibility}/{workspaceName} | [EXPERIMENTAL] GetWorkspace: Get a workspace.
[**list_items**](WorkspaceApi.md#list_items) | **GET** /api/workspaces/{visibility}/{workspaceName}/items | [EXPERIMENTAL] ListItems: List the items in a workspace.
[**list_workspaces**](WorkspaceApi.md#list_workspaces) | **GET** /api/workspaces/{visibility} | [EXPERIMENTAL] ListWorkspaces: List workspaces.
[**search_items**](WorkspaceApi.md#search_items) | **GET** /api/workspaces/{visibility}/items | [EXPERIMENTAL] SearchItems: List items across all workspaces.
[**update_item**](WorkspaceApi.md#update_item) | **PUT** /api/workspaces/{visibility}/{workspaceName}/items/{groupName}/{itemName} | [EXPERIMENTAL] UpdateItem: Update an item in a workspace.
[**update_workspace**](WorkspaceApi.md#update_workspace) | **PUT** /api/workspaces/{visibility}/{workspaceName} | [EXPERIMENTAL] UpdateWorkspace: Update a workspace.


# **create_item**
> WorkspaceItem create_item(visibility, workspace_name, workspace_item_creation_request=workspace_item_creation_request)

[EXPERIMENTAL] CreateItem: Create a new item in a workspace.

Create a new item in a workspace.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    WorkspaceApi
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
    api_instance = api_client_factory.build(WorkspaceApi)
    visibility = 'visibility_example' # str | The visibility for the containing workspace. Must be `shared` or `personal`; case is important.
    workspace_name = 'workspace_name_example' # str | The item's workspace name.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # workspace_item_creation_request = WorkspaceItemCreationRequest.from_json("")
    # workspace_item_creation_request = WorkspaceItemCreationRequest.from_dict({})
    workspace_item_creation_request = WorkspaceItemCreationRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.create_item(visibility, workspace_name, workspace_item_creation_request=workspace_item_creation_request, opts=opts)

        # [EXPERIMENTAL] CreateItem: Create a new item in a workspace.
        api_response = api_instance.create_item(visibility, workspace_name, workspace_item_creation_request=workspace_item_creation_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling WorkspaceApi->create_item: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **visibility** | **str**| The visibility for the containing workspace. Must be &#x60;shared&#x60; or &#x60;personal&#x60;; case is important. | 
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

# **create_workspace**
> Workspace create_workspace(visibility, workspace_creation_request=workspace_creation_request)

[EXPERIMENTAL] CreateWorkspace: Create a new workspace.

Create a new workspace.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    WorkspaceApi
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
    api_instance = api_client_factory.build(WorkspaceApi)
    visibility = 'visibility_example' # str | The visibility for the workspace being created. Must be `shared` or `personal`; case is important.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # workspace_creation_request = WorkspaceCreationRequest.from_json("")
    # workspace_creation_request = WorkspaceCreationRequest.from_dict({})
    workspace_creation_request = WorkspaceCreationRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.create_workspace(visibility, workspace_creation_request=workspace_creation_request, opts=opts)

        # [EXPERIMENTAL] CreateWorkspace: Create a new workspace.
        api_response = api_instance.create_workspace(visibility, workspace_creation_request=workspace_creation_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling WorkspaceApi->create_workspace: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **visibility** | **str**| The visibility for the workspace being created. Must be &#x60;shared&#x60; or &#x60;personal&#x60;; case is important. | 
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

# **delete_item**
> DeletedEntityResponse delete_item(visibility, workspace_name, group_name, item_name)

[EXPERIMENTAL] DeleteItem: Delete an item from a workspace.

Delete an item from a workspace.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    WorkspaceApi
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
    api_instance = api_client_factory.build(WorkspaceApi)
    visibility = 'visibility_example' # str | The visibility for the containing workspace. Must be `shared` or `personal`; case is important.
    workspace_name = 'workspace_name_example' # str | The name of the workspace.
    group_name = 'group_name_example' # str | The group containing the item.
    item_name = 'item_name_example' # str | The name of the item.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_item(visibility, workspace_name, group_name, item_name, opts=opts)

        # [EXPERIMENTAL] DeleteItem: Delete an item from a workspace.
        api_response = api_instance.delete_item(visibility, workspace_name, group_name, item_name)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling WorkspaceApi->delete_item: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **visibility** | **str**| The visibility for the containing workspace. Must be &#x60;shared&#x60; or &#x60;personal&#x60;; case is important. | 
 **workspace_name** | **str**| The name of the workspace. | 
 **group_name** | **str**| The group containing the item. | 
 **item_name** | **str**| The name of the item. | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The result of deleting a workspace item. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_workspace**
> DeletedEntityResponse delete_workspace(visibility, workspace_name)

[EXPERIMENTAL] DeleteWorkspace: Delete a workspace.

Delete a workspace.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    WorkspaceApi
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
    api_instance = api_client_factory.build(WorkspaceApi)
    visibility = 'visibility_example' # str | The visibility for the workspace. Must be `shared` or `personal`; case is important.
    workspace_name = 'workspace_name_example' # str | The name of the workspace.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_workspace(visibility, workspace_name, opts=opts)

        # [EXPERIMENTAL] DeleteWorkspace: Delete a workspace.
        api_response = api_instance.delete_workspace(visibility, workspace_name)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling WorkspaceApi->delete_workspace: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **visibility** | **str**| The visibility for the workspace. Must be &#x60;shared&#x60; or &#x60;personal&#x60;; case is important. | 
 **workspace_name** | **str**| The name of the workspace. | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The result of deleting a workspace. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_item**
> WorkspaceItem get_item(visibility, workspace_name, group_name, item_name, as_at=as_at)

[EXPERIMENTAL] GetItem: Get a single workspace item.

Get a single workspace item.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    WorkspaceApi
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
    api_instance = api_client_factory.build(WorkspaceApi)
    visibility = 'visibility_example' # str | The visibility for the containing workspace. Must be `shared` or `personal`; case is important.
    workspace_name = 'workspace_name_example' # str | The name of the workspace.
    group_name = 'group_name_example' # str | The group containing the item.
    item_name = 'item_name_example' # str | The name of the item.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The datetime at which to request the workspace item. If not provided, defaults to 'latest'. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_item(visibility, workspace_name, group_name, item_name, as_at=as_at, opts=opts)

        # [EXPERIMENTAL] GetItem: Get a single workspace item.
        api_response = api_instance.get_item(visibility, workspace_name, group_name, item_name, as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling WorkspaceApi->get_item: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **visibility** | **str**| The visibility for the containing workspace. Must be &#x60;shared&#x60; or &#x60;personal&#x60;; case is important. | 
 **workspace_name** | **str**| The name of the workspace. | 
 **group_name** | **str**| The group containing the item. | 
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

# **get_workspace**
> Workspace get_workspace(visibility, workspace_name, as_at=as_at)

[EXPERIMENTAL] GetWorkspace: Get a workspace.

Get a workspace.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    WorkspaceApi
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
    api_instance = api_client_factory.build(WorkspaceApi)
    visibility = 'visibility_example' # str | The visibility for the workspace. Must be `shared` or `personal`; case is important.
    workspace_name = 'workspace_name_example' # str | The workspace name.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve workspaces. Defaults to 'latest' if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_workspace(visibility, workspace_name, as_at=as_at, opts=opts)

        # [EXPERIMENTAL] GetWorkspace: Get a workspace.
        api_response = api_instance.get_workspace(visibility, workspace_name, as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling WorkspaceApi->get_workspace: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **visibility** | **str**| The visibility for the workspace. Must be &#x60;shared&#x60; or &#x60;personal&#x60;; case is important. | 
 **workspace_name** | **str**| The workspace name. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve workspaces. Defaults to &#39;latest&#39; if not specified. | [optional] 

### Return type

[**Workspace**](Workspace.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The workspace. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_items**
> PagedResourceListOfWorkspaceItem list_items(visibility, workspace_name, as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter)

[EXPERIMENTAL] ListItems: List the items in a workspace.

List the items in a workspace.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    WorkspaceApi
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
    api_instance = api_client_factory.build(WorkspaceApi)
    visibility = 'visibility_example' # str | The visibility for the containing workspace. Must be `shared` or `personal`; case is important.
    workspace_name = 'workspace_name_example' # str | The item's workspace name.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve workspace items. Defaults to 'latest' if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing workspaces items from a previous call to list workspaces items.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields              must not have changed since the original request. (optional)
    sort_by = ['sort_by_example'] # List[str] | A list of field names to sort by, each suffixed by \" ASC\" or \" DESC\". (optional)
    limit = 56 # int | When paginating, limit the number of returned results to this many. (optional)
    filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_items(visibility, workspace_name, as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter, opts=opts)

        # [EXPERIMENTAL] ListItems: List the items in a workspace.
        api_response = api_instance.list_items(visibility, workspace_name, as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling WorkspaceApi->list_items: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **visibility** | **str**| The visibility for the containing workspace. Must be &#x60;shared&#x60; or &#x60;personal&#x60;; case is important. | 
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
**200** | The items in a workspace. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_workspaces**
> PagedResourceListOfWorkspace list_workspaces(visibility, as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter)

[EXPERIMENTAL] ListWorkspaces: List workspaces.

List workspaces.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    WorkspaceApi
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
    api_instance = api_client_factory.build(WorkspaceApi)
    visibility = 'visibility_example' # str | The visibility for the workspaces. Must be `shared` or `personal`; case is important.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve workspaces. Defaults to 'latest' if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing workspaces from a previous call to list workspaces.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields              must not have changed since the original request. (optional)
    sort_by = ['sort_by_example'] # List[str] | A list of field names to sort by, each suffixed by \" ASC\" or \" DESC\". (optional)
    limit = 56 # int | When paginating, limit the number of returned results to this many. (optional)
    filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_workspaces(visibility, as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter, opts=opts)

        # [EXPERIMENTAL] ListWorkspaces: List workspaces.
        api_response = api_instance.list_workspaces(visibility, as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling WorkspaceApi->list_workspaces: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **visibility** | **str**| The visibility for the workspaces. Must be &#x60;shared&#x60; or &#x60;personal&#x60;; case is important. | 
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
**200** | The workspaces. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **search_items**
> PagedResourceListOfItemAndWorkspace search_items(visibility, as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter)

[EXPERIMENTAL] SearchItems: List items across all workspaces.

List items across all workspaces.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    WorkspaceApi
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
    api_instance = api_client_factory.build(WorkspaceApi)
    visibility = 'visibility_example' # str | The visibility for the containing workspace. Must be `shared` or `personal`; case is important.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve workspace items. Defaults to 'latest' if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing workspaces items from a previous call to list workspaces items.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields              must not have changed since the original request. (optional)
    sort_by = ['sort_by_example'] # List[str] | A list of field names to sort by, each suffixed by \" ASC\" or \" DESC\". (optional)
    limit = 56 # int | When paginating, limit the number of returned results to this many. (optional)
    filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.search_items(visibility, as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter, opts=opts)

        # [EXPERIMENTAL] SearchItems: List items across all workspaces.
        api_response = api_instance.search_items(visibility, as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling WorkspaceApi->search_items: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **visibility** | **str**| The visibility for the containing workspace. Must be &#x60;shared&#x60; or &#x60;personal&#x60;; case is important. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve workspace items. Defaults to &#39;latest&#39; if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing workspaces items from a previous call to list workspaces items.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields              must not have changed since the original request. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid. | [optional] 

### Return type

[**PagedResourceListOfItemAndWorkspace**](PagedResourceListOfItemAndWorkspace.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Items across all workspaces. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **update_item**
> WorkspaceItem update_item(visibility, workspace_name, group_name, item_name, workspace_item_update_request=workspace_item_update_request)

[EXPERIMENTAL] UpdateItem: Update an item in a workspace.

Update an item in a workspace.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    WorkspaceApi
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
    api_instance = api_client_factory.build(WorkspaceApi)
    visibility = 'visibility_example' # str | The visibility for the containing workspace. Must be `shared` or `personal`; case is important.
    workspace_name = 'workspace_name_example' # str | The workspace name.
    group_name = 'group_name_example' # str | The group containing the item.
    item_name = 'item_name_example' # str | The item name.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # workspace_item_update_request = WorkspaceItemUpdateRequest.from_json("")
    # workspace_item_update_request = WorkspaceItemUpdateRequest.from_dict({})
    workspace_item_update_request = WorkspaceItemUpdateRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.update_item(visibility, workspace_name, group_name, item_name, workspace_item_update_request=workspace_item_update_request, opts=opts)

        # [EXPERIMENTAL] UpdateItem: Update an item in a workspace.
        api_response = api_instance.update_item(visibility, workspace_name, group_name, item_name, workspace_item_update_request=workspace_item_update_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling WorkspaceApi->update_item: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **visibility** | **str**| The visibility for the containing workspace. Must be &#x60;shared&#x60; or &#x60;personal&#x60;; case is important. | 
 **workspace_name** | **str**| The workspace name. | 
 **group_name** | **str**| The group containing the item. | 
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

# **update_workspace**
> Workspace update_workspace(visibility, workspace_name, workspace_update_request=workspace_update_request)

[EXPERIMENTAL] UpdateWorkspace: Update a workspace.

Update a workspace.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    WorkspaceApi
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
    api_instance = api_client_factory.build(WorkspaceApi)
    visibility = 'visibility_example' # str | The visibility for the workspace. Must be `shared` or `personal`; case is important.
    workspace_name = 'workspace_name_example' # str | The workspace name.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # workspace_update_request = WorkspaceUpdateRequest.from_json("")
    # workspace_update_request = WorkspaceUpdateRequest.from_dict({})
    workspace_update_request = WorkspaceUpdateRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.update_workspace(visibility, workspace_name, workspace_update_request=workspace_update_request, opts=opts)

        # [EXPERIMENTAL] UpdateWorkspace: Update a workspace.
        api_response = api_instance.update_workspace(visibility, workspace_name, workspace_update_request=workspace_update_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling WorkspaceApi->update_workspace: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **visibility** | **str**| The visibility for the workspace. Must be &#x60;shared&#x60; or &#x60;personal&#x60;; case is important. | 
 **workspace_name** | **str**| The workspace name. | 
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

