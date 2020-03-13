# lusid.PortfolioGroupsApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_portfolio_to_group**](PortfolioGroupsApi.md#add_portfolio_to_group) | **POST** /api/portfoliogroups/{scope}/{code}/portfolios | [EARLY ACCESS] Add portfolio to group
[**add_sub_group_to_group**](PortfolioGroupsApi.md#add_sub_group_to_group) | **POST** /api/portfoliogroups/{scope}/{code}/subgroups | [EARLY ACCESS] Add sub group to group
[**create_portfolio_group**](PortfolioGroupsApi.md#create_portfolio_group) | **POST** /api/portfoliogroups/{scope} | [EARLY ACCESS] Create portfolio group
[**delete_group_properties**](PortfolioGroupsApi.md#delete_group_properties) | **POST** /api/portfoliogroups/{scope}/{code}/properties/$delete | [EARLY ACCESS] Delete group properties
[**delete_key_from_portfolio_group_access_metadata**](PortfolioGroupsApi.md#delete_key_from_portfolio_group_access_metadata) | **DELETE** /api/portfoliogroups/{scope}/{code}/metadata/{key} | [EXPERIMENTAL] Delete a Portfolio Group Access Metadata entry
[**delete_portfolio_from_group**](PortfolioGroupsApi.md#delete_portfolio_from_group) | **DELETE** /api/portfoliogroups/{scope}/{code}/portfolios/{portfolioScope}/{portfolioCode} | [EARLY ACCESS] Delete portfolio from group
[**delete_portfolio_group**](PortfolioGroupsApi.md#delete_portfolio_group) | **DELETE** /api/portfoliogroups/{scope}/{code} | [EARLY ACCESS] Delete portfolio group
[**delete_sub_group_from_group**](PortfolioGroupsApi.md#delete_sub_group_from_group) | **DELETE** /api/portfoliogroups/{scope}/{code}/subgroups/{subgroupScope}/{subgroupCode} | [EARLY ACCESS] Delete sub group from group
[**get_group_properties**](PortfolioGroupsApi.md#get_group_properties) | **GET** /api/portfoliogroups/{scope}/{code}/properties | [EARLY ACCESS] Get group properties
[**get_portfolio_group**](PortfolioGroupsApi.md#get_portfolio_group) | **GET** /api/portfoliogroups/{scope}/{code} | [EARLY ACCESS] Get portfolio group
[**get_portfolio_group_access_metadata_by_key**](PortfolioGroupsApi.md#get_portfolio_group_access_metadata_by_key) | **GET** /api/portfoliogroups/{scope}/{code}/metadata/{key} | [EXPERIMENTAL] Get an entry identified by a key in the Access Metadata of a Portfolio Group
[**get_portfolio_group_commands**](PortfolioGroupsApi.md#get_portfolio_group_commands) | **GET** /api/portfoliogroups/{scope}/{code}/commands | [EARLY ACCESS] Get portfolio group commands
[**get_portfolio_group_expansion**](PortfolioGroupsApi.md#get_portfolio_group_expansion) | **GET** /api/portfoliogroups/{scope}/{code}/expansion | [EARLY ACCESS] Get portfolio group expansion
[**get_portfolio_group_metadata**](PortfolioGroupsApi.md#get_portfolio_group_metadata) | **GET** /api/portfoliogroups/{scope}/{code}/metadata | [EXPERIMENTAL] Get Access Metadata rules for Portfolio Group
[**list_portfolio_groups**](PortfolioGroupsApi.md#list_portfolio_groups) | **GET** /api/portfoliogroups/{scope} | [EARLY ACCESS] List portfolio groups
[**update_portfolio_group**](PortfolioGroupsApi.md#update_portfolio_group) | **PUT** /api/portfoliogroups/{scope}/{code} | [EARLY ACCESS] Update portfolio group
[**upsert_group_properties**](PortfolioGroupsApi.md#upsert_group_properties) | **POST** /api/portfoliogroups/{scope}/{code}/properties/$upsert | [EARLY ACCESS] Upsert group properties
[**upsert_portfolio_group_access_metadata**](PortfolioGroupsApi.md#upsert_portfolio_group_access_metadata) | **PUT** /api/portfoliogroups/{scope}/{code}/metadata/{key} | [EXPERIMENTAL] Upsert a Portfolio Group Access Metadata entry associated with a specific key. This creates or updates the data in LUSID.


# **add_portfolio_to_group**
> PortfolioGroup add_portfolio_to_group(scope, code, effective_at, portfolio_id=portfolio_id)

[EARLY ACCESS] Add portfolio to group

Add a single portfolio to a portfolio group.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://localhost/api
configuration.host = "http://localhost/api"

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.PortfolioGroupsApi(api_client)
    scope = 'scope_example' # str | The scope of the portfolio group to add a portfolio to.
code = 'code_example' # str | The code of the portfolio group to add a portfolio to. Together with the scope this uniquely identifies the portfolio group.
effective_at = '2013-10-20T19:20:30+01:00' # datetime | The effective datetime from which the portfolio will be added to the group.
portfolio_id = lusid.ResourceId() # ResourceId | The resource identifier of the portfolio to add to the portfolio group. (optional)

    try:
        # [EARLY ACCESS] Add portfolio to group
        api_response = api_instance.add_portfolio_to_group(scope, code, effective_at, portfolio_id=portfolio_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PortfolioGroupsApi->add_portfolio_to_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio group to add a portfolio to. | 
 **code** | **str**| The code of the portfolio group to add a portfolio to. Together with the scope this uniquely identifies the portfolio group. | 
 **effective_at** | **datetime**| The effective datetime from which the portfolio will be added to the group. | 
 **portfolio_id** | [**ResourceId**](ResourceId.md)| The resource identifier of the portfolio to add to the portfolio group. | [optional] 

### Return type

[**PortfolioGroup**](PortfolioGroup.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The portfolio group containing the newly added portfolio |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_sub_group_to_group**
> PortfolioGroup add_sub_group_to_group(scope, code, effective_at, portfolio_group_id=portfolio_group_id)

[EARLY ACCESS] Add sub group to group

Add a portfolio group to a portfolio group as a sub group.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://localhost/api
configuration.host = "http://localhost/api"

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.PortfolioGroupsApi(api_client)
    scope = 'scope_example' # str | The scope of the portfolio group to add a portfolio group to.
code = 'code_example' # str | The code of the portfolio group to add a portfolio group to. Together with the scope this uniquely identifies the portfolio group.
effective_at = '2013-10-20T19:20:30+01:00' # datetime | The effective datetime from which the sub group will be added to the group.
portfolio_group_id = lusid.ResourceId() # ResourceId | The resource identifier of the portfolio group to add to the portfolio group as a sub group. (optional)

    try:
        # [EARLY ACCESS] Add sub group to group
        api_response = api_instance.add_sub_group_to_group(scope, code, effective_at, portfolio_group_id=portfolio_group_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PortfolioGroupsApi->add_sub_group_to_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio group to add a portfolio group to. | 
 **code** | **str**| The code of the portfolio group to add a portfolio group to. Together with the scope this uniquely identifies the portfolio group. | 
 **effective_at** | **datetime**| The effective datetime from which the sub group will be added to the group. | 
 **portfolio_group_id** | [**ResourceId**](ResourceId.md)| The resource identifier of the portfolio group to add to the portfolio group as a sub group. | [optional] 

### Return type

[**PortfolioGroup**](PortfolioGroup.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The portfolio group containing the newly added portfolio group as a sub group |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_portfolio_group**
> PortfolioGroup create_portfolio_group(scope, request=request)

[EARLY ACCESS] Create portfolio group

Create a portfolio group in a specific scope.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://localhost/api
configuration.host = "http://localhost/api"

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.PortfolioGroupsApi(api_client)
    scope = 'scope_example' # str | The scope that the portfolio group will be created in.
request = lusid.CreatePortfolioGroupRequest() # CreatePortfolioGroupRequest | The definition and details of the portfolio group. (optional)

    try:
        # [EARLY ACCESS] Create portfolio group
        api_response = api_instance.create_portfolio_group(scope, request=request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PortfolioGroupsApi->create_portfolio_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that the portfolio group will be created in. | 
 **request** | [**CreatePortfolioGroupRequest**](CreatePortfolioGroupRequest.md)| The definition and details of the portfolio group. | [optional] 

### Return type

[**PortfolioGroup**](PortfolioGroup.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created portfolio group |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group_properties**
> DeletedEntityResponse delete_group_properties(scope, code, property_keys, effective_at=effective_at)

[EARLY ACCESS] Delete group properties

Delete one or more properties from a single portfolio group. If the properties are time variant then an effective date time from which the properties  will be deleted must be specified. If the properties are perpetual then it is invalid to specify an effective date time for deletion.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://localhost/api
configuration.host = "http://localhost/api"

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.PortfolioGroupsApi(api_client)
    scope = 'scope_example' # str | The scope of the group to delete properties from.
code = 'code_example' # str | The code of the group to delete properties from. Together with the scope this uniquely identifies the group.
property_keys = ['property_keys_example'] # list[str] | The property keys of the properties to delete. These take the format              {domain}/{scope}/{code} e.g. \"PortfolioGroup/Manager/Id\". Each property must be from the \"PortfolioGroup\" domain.
effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to delete the properties. (optional)

    try:
        # [EARLY ACCESS] Delete group properties
        api_response = api_instance.delete_group_properties(scope, code, property_keys, effective_at=effective_at)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PortfolioGroupsApi->delete_group_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the group to delete properties from. | 
 **code** | **str**| The code of the group to delete properties from. Together with the scope this uniquely identifies the group. | 
 **property_keys** | [**list[str]**](str.md)| The property keys of the properties to delete. These take the format              {domain}/{scope}/{code} e.g. \&quot;PortfolioGroup/Manager/Id\&quot;. Each property must be from the \&quot;PortfolioGroup\&quot; domain. | 
 **effective_at** | **str**| The effective datetime or cut label at which to delete the properties. | [optional] 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the properties were deleted from the specified group |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_key_from_portfolio_group_access_metadata**
> DeletedEntityResponse delete_key_from_portfolio_group_access_metadata(scope, code, key, effective_at=effective_at)

[EXPERIMENTAL] Delete a Portfolio Group Access Metadata entry

Deletes the Portfolio Group Access Metadata entry that exactly matches the provided identifier parts.    It is important to always check to verify success (or failure).

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://localhost/api
configuration.host = "http://localhost/api"

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.PortfolioGroupsApi(api_client)
    scope = 'scope_example' # str | The scope of the Portfolio Group
code = 'code_example' # str | The Portfolio Group code
key = 'key_example' # str | Key of the Access Metadata entry to delete
effective_at = 'effective_at_example' # str | The effective date to delete at, if this is not supplied, it will delete all data found (optional)

    try:
        # [EXPERIMENTAL] Delete a Portfolio Group Access Metadata entry
        api_response = api_instance.delete_key_from_portfolio_group_access_metadata(scope, code, key, effective_at=effective_at)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PortfolioGroupsApi->delete_key_from_portfolio_group_access_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Portfolio Group | 
 **code** | **str**| The Portfolio Group code | 
 **key** | **str**| Key of the Access Metadata entry to delete | 
 **effective_at** | **str**| The effective date to delete at, if this is not supplied, it will delete all data found | [optional] 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The has been deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_portfolio_from_group**
> PortfolioGroup delete_portfolio_from_group(scope, code, portfolio_scope, portfolio_code, effective_at)

[EARLY ACCESS] Delete portfolio from group

Remove a single portfolio from a portfolio group.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://localhost/api
configuration.host = "http://localhost/api"

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.PortfolioGroupsApi(api_client)
    scope = 'scope_example' # str | The scope of the portfolio group to remove the portfolio from.
code = 'code_example' # str | The code of the portfolio group to remove the portfolio from. Together with the scope this uniquely identifies the portfolio group.
portfolio_scope = 'portfolio_scope_example' # str | The scope of the portfolio being removed from the portfolio group.
portfolio_code = 'portfolio_code_example' # str | The code of the portfolio being removed from the portfolio group. Together with the scope this uniquely identifies the portfolio to remove.
effective_at = '2013-10-20T19:20:30+01:00' # datetime | The effective datetime from which the portfolio will be removed from the portfolio group.

    try:
        # [EARLY ACCESS] Delete portfolio from group
        api_response = api_instance.delete_portfolio_from_group(scope, code, portfolio_scope, portfolio_code, effective_at)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PortfolioGroupsApi->delete_portfolio_from_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio group to remove the portfolio from. | 
 **code** | **str**| The code of the portfolio group to remove the portfolio from. Together with the scope this uniquely identifies the portfolio group. | 
 **portfolio_scope** | **str**| The scope of the portfolio being removed from the portfolio group. | 
 **portfolio_code** | **str**| The code of the portfolio being removed from the portfolio group. Together with the scope this uniquely identifies the portfolio to remove. | 
 **effective_at** | **datetime**| The effective datetime from which the portfolio will be removed from the portfolio group. | 

### Return type

[**PortfolioGroup**](PortfolioGroup.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The portfolio group with the portfolio removed from the group |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_portfolio_group**
> DeletedEntityResponse delete_portfolio_group(scope, code)

[EARLY ACCESS] Delete portfolio group

Delete a single portfolio group. A portfolio group can be deleted while it still contains portfolios or sub groups.  In this case any portfolios or sub groups contained in this group will not be deleted, however they will no longer be grouped together by this portfolio group.  The deletion will be valid from the portfolio group's creation datetime, ie. the portfolio group will no longer exist at any effective datetime from the asAt datetime of deletion.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://localhost/api
configuration.host = "http://localhost/api"

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.PortfolioGroupsApi(api_client)
    scope = 'scope_example' # str | The scope of the portfolio group to delete.
code = 'code_example' # str | The code of the portfolio group to delete. Together with the scope this uniquely identifies the portfolio group to delete.

    try:
        # [EARLY ACCESS] Delete portfolio group
        api_response = api_instance.delete_portfolio_group(scope, code)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PortfolioGroupsApi->delete_portfolio_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio group to delete. | 
 **code** | **str**| The code of the portfolio group to delete. Together with the scope this uniquely identifies the portfolio group to delete. | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the portfolio group was deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sub_group_from_group**
> PortfolioGroup delete_sub_group_from_group(scope, code, subgroup_scope, subgroup_code, effective_at)

[EARLY ACCESS] Delete sub group from group

Remove a single portfolio group (sub group) from a portfolio group.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://localhost/api
configuration.host = "http://localhost/api"

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.PortfolioGroupsApi(api_client)
    scope = 'scope_example' # str | The scope of the portfolio group to remove the sub group from.
code = 'code_example' # str | The code of the portfolio group to remove the sub group from. Together with the scope this uniquely identifies the portfolio group.
subgroup_scope = 'subgroup_scope_example' # str | The scope of the sub group to remove from the portfolio group.
subgroup_code = 'subgroup_code_example' # str | The code of the sub group to remove from the portfolio group. Together with the scope this uniquely identifies the sub group.
effective_at = '2013-10-20T19:20:30+01:00' # datetime | The effective datetime from which the sub group will be removed from the portfolio group.

    try:
        # [EARLY ACCESS] Delete sub group from group
        api_response = api_instance.delete_sub_group_from_group(scope, code, subgroup_scope, subgroup_code, effective_at)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PortfolioGroupsApi->delete_sub_group_from_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio group to remove the sub group from. | 
 **code** | **str**| The code of the portfolio group to remove the sub group from. Together with the scope this uniquely identifies the portfolio group. | 
 **subgroup_scope** | **str**| The scope of the sub group to remove from the portfolio group. | 
 **subgroup_code** | **str**| The code of the sub group to remove from the portfolio group. Together with the scope this uniquely identifies the sub group. | 
 **effective_at** | **datetime**| The effective datetime from which the sub group will be removed from the portfolio group. | 

### Return type

[**PortfolioGroup**](PortfolioGroup.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The portfolio group with the sub group removed from the group |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_properties**
> PortfolioGroupProperties get_group_properties(scope, code, effective_at=effective_at, as_at=as_at)

[EARLY ACCESS] Get group properties

List all the properties of a single portfolio group.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://localhost/api
configuration.host = "http://localhost/api"

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.PortfolioGroupsApi(api_client)
    scope = 'scope_example' # str | The scope of the group to list the properties for.
code = 'code_example' # str | The code of the group to list the properties for. Together with the scope this uniquely identifies the group.
effective_at = 'effective_at_example' # str | The effective date time or cut label at which to list the group's properties. Defaults to the current LUSID system datetime if not specified. (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt date time at which to list the group's properties. Defaults to return the latest version of each property if not specified. (optional)

    try:
        # [EARLY ACCESS] Get group properties
        api_response = api_instance.get_group_properties(scope, code, effective_at=effective_at, as_at=as_at)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PortfolioGroupsApi->get_group_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the group to list the properties for. | 
 **code** | **str**| The code of the group to list the properties for. Together with the scope this uniquely identifies the group. | 
 **effective_at** | **str**| The effective date time or cut label at which to list the group&#39;s properties. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt date time at which to list the group&#39;s properties. Defaults to return the latest version of each property if not specified. | [optional] 

### Return type

[**PortfolioGroupProperties**](PortfolioGroupProperties.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The properties of the specified group |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_portfolio_group**
> PortfolioGroup get_portfolio_group(scope, code, effective_at=effective_at, as_at=as_at)

[EARLY ACCESS] Get portfolio group

Retrieve the definition of a single portfolio group.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://localhost/api
configuration.host = "http://localhost/api"

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.PortfolioGroupsApi(api_client)
    scope = 'scope_example' # str | The scope of the portfolio group to retrieve the definition for.
code = 'code_example' # str | The code of the portfolio group to retrieve the definition for. Together with the scope              this uniquely identifies the portfolio group.
effective_at = '2013-10-20T19:20:30+01:00' # datetime | The effective datetime at which to retrieve the portfolio group definition. Defaults to the current LUSID system datetime if not specified. (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the portfolio group definition. Defaults to return              the latest version of the portfolio group definition if not specified. (optional)

    try:
        # [EARLY ACCESS] Get portfolio group
        api_response = api_instance.get_portfolio_group(scope, code, effective_at=effective_at, as_at=as_at)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PortfolioGroupsApi->get_portfolio_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio group to retrieve the definition for. | 
 **code** | **str**| The code of the portfolio group to retrieve the definition for. Together with the scope              this uniquely identifies the portfolio group. | 
 **effective_at** | **datetime**| The effective datetime at which to retrieve the portfolio group definition. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the portfolio group definition. Defaults to return              the latest version of the portfolio group definition if not specified. | [optional] 

### Return type

[**PortfolioGroup**](PortfolioGroup.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested portfolio group definition |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_portfolio_group_access_metadata_by_key**
> list[AccessMetadataValue] get_portfolio_group_access_metadata_by_key(scope, code, key, effective_at=effective_at, as_at=as_at)

[EXPERIMENTAL] Get an entry identified by a key in the Access Metadata of a Portfolio Group

Get a specific Portfolio Group access metadata by specifying the corresponding identifier parts                No matching will be performed through this endpoint. To retrieve a rule, it is necessary to specify, exactly, the identifier of the rule

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://localhost/api
configuration.host = "http://localhost/api"

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.PortfolioGroupsApi(api_client)
    scope = 'scope_example' # str | The scope of the Portfolio Group
code = 'code_example' # str | The Portfolio Group code
key = 'key_example' # str | Key of the metadata entry to retrieve
effective_at = 'effective_at_example' # str | The effectiveAt datetime at which to retrieve the access metadata (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the access metadata (optional)

    try:
        # [EXPERIMENTAL] Get an entry identified by a key in the Access Metadata of a Portfolio Group
        api_response = api_instance.get_portfolio_group_access_metadata_by_key(scope, code, key, effective_at=effective_at, as_at=as_at)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PortfolioGroupsApi->get_portfolio_group_access_metadata_by_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Portfolio Group | 
 **code** | **str**| The Portfolio Group code | 
 **key** | **str**| Key of the metadata entry to retrieve | 
 **effective_at** | **str**| The effectiveAt datetime at which to retrieve the access metadata | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the access metadata | [optional] 

### Return type

[**list[AccessMetadataValue]**](AccessMetadataValue.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully retrieved Portfolio group access metadata filtered by key or any failure. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_portfolio_group_commands**
> ResourceListOfProcessedCommand get_portfolio_group_commands(scope, code, from_as_at=from_as_at, to_as_at=to_as_at, filter=filter)

[EARLY ACCESS] Get portfolio group commands

Gets all the commands that modified a single portfolio group.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://localhost/api
configuration.host = "http://localhost/api"

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.PortfolioGroupsApi(api_client)
    scope = 'scope_example' # str | The scope of the portfolio group to retrieve the commands for.
code = 'code_example' # str | The code of the portfolio group to retrieve the commands for. Together with the scope this uniquely identifies the portfolio group.
from_as_at = '2013-10-20T19:20:30+01:00' # datetime | The lower bound asAt datetime (inclusive) from which to retrieve commands. There is no lower bound if this is not specified. (optional)
to_as_at = '2013-10-20T19:20:30+01:00' # datetime | The upper bound asAt datetime (inclusive) from which to retrieve commands. There is no upper bound if this is not specified. (optional)
filter = 'filter_example' # str | Expression to filter the result set.                For example, to filter on the User ID, use \"userId.id eq 'string'\"              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)

    try:
        # [EARLY ACCESS] Get portfolio group commands
        api_response = api_instance.get_portfolio_group_commands(scope, code, from_as_at=from_as_at, to_as_at=to_as_at, filter=filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PortfolioGroupsApi->get_portfolio_group_commands: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio group to retrieve the commands for. | 
 **code** | **str**| The code of the portfolio group to retrieve the commands for. Together with the scope this uniquely identifies the portfolio group. | 
 **from_as_at** | **datetime**| The lower bound asAt datetime (inclusive) from which to retrieve commands. There is no lower bound if this is not specified. | [optional] 
 **to_as_at** | **datetime**| The upper bound asAt datetime (inclusive) from which to retrieve commands. There is no upper bound if this is not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set.                For example, to filter on the User ID, use \&quot;userId.id eq &#39;string&#39;\&quot;              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 

### Return type

[**ResourceListOfProcessedCommand**](ResourceListOfProcessedCommand.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The commands that modified the specified portfolio group |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_portfolio_group_expansion**
> ExpandedGroup get_portfolio_group_expansion(scope, code, effective_at=effective_at, as_at=as_at, property_filter=property_filter)

[EARLY ACCESS] Get portfolio group expansion

List all the portfolios in a group, including all portfolios within sub groups in the group. Each portfolio will be decorated with all of its properties unless a property filter is specified.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://localhost/api
configuration.host = "http://localhost/api"

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.PortfolioGroupsApi(api_client)
    scope = 'scope_example' # str | The scope of the portfolio group to expand.
code = 'code_example' # str | The code of the portfolio group to expand. Together with the scope this uniquely identifies the portfolio              group to expand.
effective_at = '2013-10-20T19:20:30+01:00' # datetime | The effective datetime at which to expand the portfolio group. Defaults to the current LUSID system datetime if not specified. (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to expand the portfolio group. Defaults to return the latest version of each portfolio in the group if not specified. (optional)
property_filter = ['property_filter_example'] # list[str] | The restricted list of property keys from the \"Portfolio\" domain which will be decorated onto each portfolio. These take the format {domain}/{scope}/{code} e.g. \"Portfolio/Manager/Id\". (optional)

    try:
        # [EARLY ACCESS] Get portfolio group expansion
        api_response = api_instance.get_portfolio_group_expansion(scope, code, effective_at=effective_at, as_at=as_at, property_filter=property_filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PortfolioGroupsApi->get_portfolio_group_expansion: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio group to expand. | 
 **code** | **str**| The code of the portfolio group to expand. Together with the scope this uniquely identifies the portfolio              group to expand. | 
 **effective_at** | **datetime**| The effective datetime at which to expand the portfolio group. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to expand the portfolio group. Defaults to return the latest version of each portfolio in the group if not specified. | [optional] 
 **property_filter** | [**list[str]**](str.md)| The restricted list of property keys from the \&quot;Portfolio\&quot; domain which will be decorated onto each portfolio. These take the format {domain}/{scope}/{code} e.g. \&quot;Portfolio/Manager/Id\&quot;. | [optional] 

### Return type

[**ExpandedGroup**](ExpandedGroup.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The expanded portfolio group |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_portfolio_group_metadata**
> dict(str, list[AccessMetadataValue]) get_portfolio_group_metadata(scope, code, effective_at=effective_at, as_at=as_at)

[EXPERIMENTAL] Get Access Metadata rules for Portfolio Group

Pass the scope and Portfolio Group code parameters to retrieve the associated Access Metadata

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://localhost/api
configuration.host = "http://localhost/api"

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.PortfolioGroupsApi(api_client)
    scope = 'scope_example' # str | The scope of the Portfolio Group
code = 'code_example' # str | The Portfolio Group code
effective_at = 'effective_at_example' # str | The effectiveAt datetime at which to retrieve the Access Metadata (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Access Metadata (optional)

    try:
        # [EXPERIMENTAL] Get Access Metadata rules for Portfolio Group
        api_response = api_instance.get_portfolio_group_metadata(scope, code, effective_at=effective_at, as_at=as_at)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PortfolioGroupsApi->get_portfolio_group_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Portfolio Group | 
 **code** | **str**| The Portfolio Group code | 
 **effective_at** | **str**| The effectiveAt datetime at which to retrieve the Access Metadata | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Access Metadata | [optional] 

### Return type

**dict(str, list[AccessMetadataValue])**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The access metadata for the portfolio group or any failure. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_portfolio_groups**
> ResourceListOfPortfolioGroup list_portfolio_groups(scope, effective_at=effective_at, as_at=as_at, filter=filter)

[EARLY ACCESS] List portfolio groups

List all the portfolio groups in a single scope.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://localhost/api
configuration.host = "http://localhost/api"

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.PortfolioGroupsApi(api_client)
    scope = 'scope_example' # str | The scope to list the portfolio groups in.
effective_at = '2013-10-20T19:20:30+01:00' # datetime | The effective datetime at which to list the portfolio groups. Defaults to the current LUSID system datetime if not specified. (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the portfolio groups. Defaults to return the latest version of each portfolio group if not specified. (optional)
filter = 'filter_example' # str | Expression to filter the result set.              For example, to filter on the Display Name, use \"displayName eq 'string'\"              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)

    try:
        # [EARLY ACCESS] List portfolio groups
        api_response = api_instance.list_portfolio_groups(scope, effective_at=effective_at, as_at=as_at, filter=filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PortfolioGroupsApi->list_portfolio_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope to list the portfolio groups in. | 
 **effective_at** | **datetime**| The effective datetime at which to list the portfolio groups. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the portfolio groups. Defaults to return the latest version of each portfolio group if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set.              For example, to filter on the Display Name, use \&quot;displayName eq &#39;string&#39;\&quot;              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 

### Return type

[**ResourceListOfPortfolioGroup**](ResourceListOfPortfolioGroup.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The portfolio groups in the specified scope |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_portfolio_group**
> PortfolioGroup update_portfolio_group(scope, code, effective_at, request=request)

[EARLY ACCESS] Update portfolio group

Update the definition of a single portfolio group. Not all elements within a portfolio group definition are modifiable  due to the potential implications for data already stored against the portfolio group.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://localhost/api
configuration.host = "http://localhost/api"

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.PortfolioGroupsApi(api_client)
    scope = 'scope_example' # str | The scope of the portfolio group to update the definition for.
code = 'code_example' # str | The code of the portfolio group to update the definition for. Together with the scope this uniquely identifies the portfolio group.
effective_at = '2013-10-20T19:20:30+01:00' # datetime | The effective datetime at which to update the definition.
request = lusid.UpdatePortfolioGroupRequest() # UpdatePortfolioGroupRequest | The updated portfolio group definition. (optional)

    try:
        # [EARLY ACCESS] Update portfolio group
        api_response = api_instance.update_portfolio_group(scope, code, effective_at, request=request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PortfolioGroupsApi->update_portfolio_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio group to update the definition for. | 
 **code** | **str**| The code of the portfolio group to update the definition for. Together with the scope this uniquely identifies the portfolio group. | 
 **effective_at** | **datetime**| The effective datetime at which to update the definition. | 
 **request** | [**UpdatePortfolioGroupRequest**](UpdatePortfolioGroupRequest.md)| The updated portfolio group definition. | [optional] 

### Return type

[**PortfolioGroup**](PortfolioGroup.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The updated definition of the portfolio group |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_group_properties**
> PortfolioGroupProperties upsert_group_properties(scope, code, group_properties=group_properties)

[EARLY ACCESS] Upsert group properties

Update or insert one or more properties onto a single group. A property will be updated if it  already exists and inserted if it does not. All properties must be of the domain 'PortfolioGroup'.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://localhost/api
configuration.host = "http://localhost/api"

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.PortfolioGroupsApi(api_client)
    scope = 'scope_example' # str | The scope of the group to update or insert the properties onto.
code = 'code_example' # str | The code of the group to update or insert the properties onto. Together with the scope this uniquely identifies the group.
group_properties = {'key': lusid.ModelProperty()} # dict(str, ModelProperty) | The properties to be updated or inserted onto the group. Each property in              the request must be keyed by its unique property key. This has the format {domain}/{scope}/{code} e.g. \"PortfolioGroup/Manager/Id\". (optional)

    try:
        # [EARLY ACCESS] Upsert group properties
        api_response = api_instance.upsert_group_properties(scope, code, group_properties=group_properties)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PortfolioGroupsApi->upsert_group_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the group to update or insert the properties onto. | 
 **code** | **str**| The code of the group to update or insert the properties onto. Together with the scope this uniquely identifies the group. | 
 **group_properties** | [**dict(str, ModelProperty)**](ModelProperty.md)| The properties to be updated or inserted onto the group. Each property in              the request must be keyed by its unique property key. This has the format {domain}/{scope}/{code} e.g. \&quot;PortfolioGroup/Manager/Id\&quot;. | [optional] 

### Return type

[**PortfolioGroupProperties**](PortfolioGroupProperties.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated or inserted properties |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_portfolio_group_access_metadata**
> ResourceListOfAccessMetadataValueOf upsert_portfolio_group_access_metadata(scope, code, key, request, effective_at=effective_at)

[EXPERIMENTAL] Upsert a Portfolio Group Access Metadata entry associated with a specific key. This creates or updates the data in LUSID.

Update or insert one Portfolio Group Access Metadata Entry in a single scope. An item will be updated if it already exists  and inserted if it does not.                The response will return the successfully updated or inserted Portfolio Group Access Metadata rule or failure message if unsuccessful.                It is important to always check to verify success (or failure).                Multiple rules for a key can exist with different effective at dates, when resources are accessed the rule that is active for the current time will be fetched.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://localhost/api
configuration.host = "http://localhost/api"

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.PortfolioGroupsApi(api_client)
    scope = 'scope_example' # str | The scope of the Portfolio Group
code = 'code_example' # str | The Portfolio Group code
key = 'key_example' # str | Key of the access metadata entry to upsert
request = lusid.UpsertPortfolioGroupAccessMetadataRequest() # UpsertPortfolioGroupAccessMetadataRequest | The Portfolio Group Access Metadata rule to upsert
effective_at = 'effective_at_example' # str | The date this rule will be effective from (optional)

    try:
        # [EXPERIMENTAL] Upsert a Portfolio Group Access Metadata entry associated with a specific key. This creates or updates the data in LUSID.
        api_response = api_instance.upsert_portfolio_group_access_metadata(scope, code, key, request, effective_at=effective_at)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PortfolioGroupsApi->upsert_portfolio_group_access_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Portfolio Group | 
 **code** | **str**| The Portfolio Group code | 
 **key** | **str**| Key of the access metadata entry to upsert | 
 **request** | [**UpsertPortfolioGroupAccessMetadataRequest**](UpsertPortfolioGroupAccessMetadataRequest.md)| The Portfolio Group Access Metadata rule to upsert | 
 **effective_at** | **str**| The date this rule will be effective from | [optional] 

### Return type

[**ResourceListOfAccessMetadataValueOf**](ResourceListOfAccessMetadataValueOf.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully updated or inserted item or any failure. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

