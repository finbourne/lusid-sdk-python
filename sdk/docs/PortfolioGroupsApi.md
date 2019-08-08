# lusid.PortfolioGroupsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_portfolio_to_group**](PortfolioGroupsApi.md#add_portfolio_to_group) | **POST** /api/portfoliogroups/{scope}/{code}/portfolios | [EARLY ACCESS] Add portfolio to group
[**add_sub_group_to_group**](PortfolioGroupsApi.md#add_sub_group_to_group) | **POST** /api/portfoliogroups/{scope}/{code}/subgroups | [EARLY ACCESS] Add group to group
[**create_portfolio_group**](PortfolioGroupsApi.md#create_portfolio_group) | **POST** /api/portfoliogroups/{scope} | [EARLY ACCESS] Create group
[**delete_portfolio_from_group**](PortfolioGroupsApi.md#delete_portfolio_from_group) | **DELETE** /api/portfoliogroups/{scope}/{code}/portfolios/{portfolioScope}/{portfolioCode} | [EARLY ACCESS] Remove portfolio from group
[**delete_portfolio_group**](PortfolioGroupsApi.md#delete_portfolio_group) | **DELETE** /api/portfoliogroups/{scope}/{code} | [EARLY ACCESS] Delete group
[**delete_sub_group_from_group**](PortfolioGroupsApi.md#delete_sub_group_from_group) | **DELETE** /api/portfoliogroups/{scope}/{code}/subgroups/{subgroupScope}/{subgroupCode} | [EARLY ACCESS] Remove group from group
[**get_portfolio_group**](PortfolioGroupsApi.md#get_portfolio_group) | **GET** /api/portfoliogroups/{scope}/{code} | [EARLY ACCESS] Get portfolio group
[**get_portfolio_group_commands**](PortfolioGroupsApi.md#get_portfolio_group_commands) | **GET** /api/portfoliogroups/{scope}/{code}/commands | [EARLY ACCESS] Get commands
[**get_portfolio_group_expansion**](PortfolioGroupsApi.md#get_portfolio_group_expansion) | **GET** /api/portfoliogroups/{scope}/{code}/expansion | [EARLY ACCESS] Get a full expansion of a portfolio group
[**list_portfolio_groups**](PortfolioGroupsApi.md#list_portfolio_groups) | **GET** /api/portfoliogroups/{scope} | [EARLY ACCESS] List groups in scope
[**update_portfolio_group**](PortfolioGroupsApi.md#update_portfolio_group) | **PUT** /api/portfoliogroups/{scope}/{code} | [EARLY ACCESS] Update group


# **add_portfolio_to_group**
> PortfolioGroup add_portfolio_to_group(scope, code, portfolio_id=portfolio_id)

[EARLY ACCESS] Add portfolio to group

Adds a portfolio to a previously defined portfolio group

### Example

```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lusid.PortfolioGroupsApi()
scope = 'scope_example' # str | The scope of the portfolio group to which a portfolio is being added
code = 'code_example' # str | The code of the portfolio group to which a portfolio is being added
portfolio_id = lusid.ResourceId() # ResourceId | The id of the portfolio (optional)

try:
    # [EARLY ACCESS] Add portfolio to group
    api_response = api_instance.add_portfolio_to_group(scope, code, portfolio_id=portfolio_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfolioGroupsApi->add_portfolio_to_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio group to which a portfolio is being added | 
 **code** | **str**| The code of the portfolio group to which a portfolio is being added | 
 **portfolio_id** | [**ResourceId**](ResourceId.md)| The id of the portfolio | [optional] 

### Return type

[**PortfolioGroup**](PortfolioGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_sub_group_to_group**
> PortfolioGroup add_sub_group_to_group(scope, code, portfolio_group_id=portfolio_group_id)

[EARLY ACCESS] Add group to group

Adds a portfolio group, as a sub-group, to an existing portfolio group

### Example

```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lusid.PortfolioGroupsApi()
scope = 'scope_example' # str | The scope of the portfolio group to which a sub-group is being added
code = 'code_example' # str | The code of the portfolio group to which a sub-group is being added
portfolio_group_id = lusid.ResourceId() # ResourceId | The id of the portfolio group being added as a sub-group (optional)

try:
    # [EARLY ACCESS] Add group to group
    api_response = api_instance.add_sub_group_to_group(scope, code, portfolio_group_id=portfolio_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfolioGroupsApi->add_sub_group_to_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio group to which a sub-group is being added | 
 **code** | **str**| The code of the portfolio group to which a sub-group is being added | 
 **portfolio_group_id** | [**ResourceId**](ResourceId.md)| The id of the portfolio group being added as a sub-group | [optional] 

### Return type

[**PortfolioGroup**](PortfolioGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_portfolio_group**
> PortfolioGroup create_portfolio_group(scope, request=request)

[EARLY ACCESS] Create group

Create a new portfolio group.

### Example

```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lusid.PortfolioGroupsApi()
scope = 'scope_example' # str | The scope into which the portfolio group will be created
request = lusid.CreatePortfolioGroupRequest() # CreatePortfolioGroupRequest | The definition of the new portfolio group (optional)

try:
    # [EARLY ACCESS] Create group
    api_response = api_instance.create_portfolio_group(scope, request=request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfolioGroupsApi->create_portfolio_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope into which the portfolio group will be created | 
 **request** | [**CreatePortfolioGroupRequest**](CreatePortfolioGroupRequest.md)| The definition of the new portfolio group | [optional] 

### Return type

[**PortfolioGroup**](PortfolioGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_portfolio_from_group**
> PortfolioGroup delete_portfolio_from_group(scope, code, portfolio_scope, portfolio_code)

[EARLY ACCESS] Remove portfolio from group

Removes a portfolio from a portfolio group

### Example

```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lusid.PortfolioGroupsApi()
scope = 'scope_example' # str | The scope of the portfolio group
code = 'code_example' # str | The code of the portfolio group
portfolio_scope = 'portfolio_scope_example' # str | The scope of the portfolio being removed
portfolio_code = 'portfolio_code_example' # str | The code of the portfolio being removed

try:
    # [EARLY ACCESS] Remove portfolio from group
    api_response = api_instance.delete_portfolio_from_group(scope, code, portfolio_scope, portfolio_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfolioGroupsApi->delete_portfolio_from_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio group | 
 **code** | **str**| The code of the portfolio group | 
 **portfolio_scope** | **str**| The scope of the portfolio being removed | 
 **portfolio_code** | **str**| The code of the portfolio being removed | 

### Return type

[**PortfolioGroup**](PortfolioGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_portfolio_group**
> DeletedEntityResponse delete_portfolio_group(scope, code)

[EARLY ACCESS] Delete group

Deletes the definition of the specified portfolio group

### Example

```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lusid.PortfolioGroupsApi()
scope = 'scope_example' # str | The scope of the portfolio group
code = 'code_example' # str | The code of the portfolio group

try:
    # [EARLY ACCESS] Delete group
    api_response = api_instance.delete_portfolio_group(scope, code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfolioGroupsApi->delete_portfolio_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio group | 
 **code** | **str**| The code of the portfolio group | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sub_group_from_group**
> PortfolioGroup delete_sub_group_from_group(scope, code, subgroup_scope, subgroup_code)

[EARLY ACCESS] Remove group from group

Remove a portfolio group (sub-group) from a parent portfolio group

### Example

```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lusid.PortfolioGroupsApi()
scope = 'scope_example' # str | The scope of the portfolio group
code = 'code_example' # str | The code of the portfolio group
subgroup_scope = 'subgroup_scope_example' # str | The scope of the sub-group being removed
subgroup_code = 'subgroup_code_example' # str | The code of the sub-group being removed

try:
    # [EARLY ACCESS] Remove group from group
    api_response = api_instance.delete_sub_group_from_group(scope, code, subgroup_scope, subgroup_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfolioGroupsApi->delete_sub_group_from_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio group | 
 **code** | **str**| The code of the portfolio group | 
 **subgroup_scope** | **str**| The scope of the sub-group being removed | 
 **subgroup_code** | **str**| The code of the sub-group being removed | 

### Return type

[**PortfolioGroup**](PortfolioGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_portfolio_group**
> PortfolioGroup get_portfolio_group(scope, code, as_at=as_at)

[EARLY ACCESS] Get portfolio group

Get the definition of the specified portfolio group

### Example

```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lusid.PortfolioGroupsApi()
scope = 'scope_example' # str | The scope of the portfolio group
code = 'code_example' # str | The code of the portfolio group
as_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The AsAt date of the data (optional)

try:
    # [EARLY ACCESS] Get portfolio group
    api_response = api_instance.get_portfolio_group(scope, code, as_at=as_at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfolioGroupsApi->get_portfolio_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio group | 
 **code** | **str**| The code of the portfolio group | 
 **as_at** | **datetime**| Optional. The AsAt date of the data | [optional] 

### Return type

[**PortfolioGroup**](PortfolioGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_portfolio_group_commands**
> ResourceListOfProcessedCommand get_portfolio_group_commands(scope, code, from_as_at=from_as_at, to_as_at=to_as_at, sort_by=sort_by, start=start, limit=limit, filter=filter)

[EARLY ACCESS] Get commands

Gets all commands that modified a specific portfolio group

### Example

```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lusid.PortfolioGroupsApi()
scope = 'scope_example' # str | The scope of the portfolio group
code = 'code_example' # str | The code of the portfolio group
from_as_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. Filters commands by those that were processed at or after this date and time (optional)
to_as_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. Filters commands by those that were processed at or before this date and time (optional)
sort_by = ['sort_by_example'] # list[str] | Optional. Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName (optional)
start = 56 # int | Optional. When paginating, skip this number of results (optional)
limit = 56 # int | Optional. When paginating, limit the number of returned results to this many. (optional)
filter = 'filter_example' # str | Optional. Expression to filter the result set (optional)

try:
    # [EARLY ACCESS] Get commands
    api_response = api_instance.get_portfolio_group_commands(scope, code, from_as_at=from_as_at, to_as_at=to_as_at, sort_by=sort_by, start=start, limit=limit, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfolioGroupsApi->get_portfolio_group_commands: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio group | 
 **code** | **str**| The code of the portfolio group | 
 **from_as_at** | **datetime**| Optional. Filters commands by those that were processed at or after this date and time | [optional] 
 **to_as_at** | **datetime**| Optional. Filters commands by those that were processed at or before this date and time | [optional] 
 **sort_by** | [**list[str]**](str.md)| Optional. Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName | [optional] 
 **start** | **int**| Optional. When paginating, skip this number of results | [optional] 
 **limit** | **int**| Optional. When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Optional. Expression to filter the result set | [optional] 

### Return type

[**ResourceListOfProcessedCommand**](ResourceListOfProcessedCommand.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_portfolio_group_expansion**
> ExpandedGroup get_portfolio_group_expansion(scope, code, effective_at=effective_at, as_at=as_at, property_filter=property_filter)

[EARLY ACCESS] Get a full expansion of a portfolio group

Lists all portfolios in a group, and all sub groups. Portfolios are decorated with their properties.

### Example

```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lusid.PortfolioGroupsApi()
scope = 'scope_example' # str | The scope of the portfolio
code = 'code_example' # str | The code of the portfolio
effective_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The effective date of the data (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The AsAt date of the data (optional)
property_filter = ['property_filter_example'] # list[str] | Optional. The restricted set of properties that should be returned (optional)

try:
    # [EARLY ACCESS] Get a full expansion of a portfolio group
    api_response = api_instance.get_portfolio_group_expansion(scope, code, effective_at=effective_at, as_at=as_at, property_filter=property_filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfolioGroupsApi->get_portfolio_group_expansion: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio | 
 **code** | **str**| The code of the portfolio | 
 **effective_at** | **datetime**| Optional. The effective date of the data | [optional] 
 **as_at** | **datetime**| Optional. The AsAt date of the data | [optional] 
 **property_filter** | [**list[str]**](str.md)| Optional. The restricted set of properties that should be returned | [optional] 

### Return type

[**ExpandedGroup**](ExpandedGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_portfolio_groups**
> ResourceListOfPortfolioGroup list_portfolio_groups(scope, as_at=as_at, sort_by=sort_by, start=start, limit=limit, filter=filter)

[EARLY ACCESS] List groups in scope

Lists all portfolio groups in a specified scope

### Example

```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lusid.PortfolioGroupsApi()
scope = 'scope_example' # str | The scope
as_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The AsAt date of the data (optional)
sort_by = ['sort_by_example'] # list[str] | Optional. Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName (optional)
start = 56 # int | Optional. When paginating, skip this number of results (optional)
limit = 56 # int | Optional. When paginating, limit the number of returned results to this many. (optional)
filter = 'filter_example' # str | Optional. Expression to filter the result set (optional)

try:
    # [EARLY ACCESS] List groups in scope
    api_response = api_instance.list_portfolio_groups(scope, as_at=as_at, sort_by=sort_by, start=start, limit=limit, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfolioGroupsApi->list_portfolio_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope | 
 **as_at** | **datetime**| Optional. The AsAt date of the data | [optional] 
 **sort_by** | [**list[str]**](str.md)| Optional. Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName | [optional] 
 **start** | **int**| Optional. When paginating, skip this number of results | [optional] 
 **limit** | **int**| Optional. When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Optional. Expression to filter the result set | [optional] 

### Return type

[**ResourceListOfPortfolioGroup**](ResourceListOfPortfolioGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_portfolio_group**
> PortfolioGroup update_portfolio_group(scope, code, request=request)

[EARLY ACCESS] Update group

Update the definition of the specified existing portfolio group.    Not all elements within a portfolio group definition are modifiable after creation.

### Example

```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lusid.PortfolioGroupsApi()
scope = 'scope_example' # str | The scope of the portfolio group
code = 'code_example' # str | The code of the portfolio group
request = lusid.UpdatePortfolioGroupRequest() # UpdatePortfolioGroupRequest | The updated definition of the portfolio group (optional)

try:
    # [EARLY ACCESS] Update group
    api_response = api_instance.update_portfolio_group(scope, code, request=request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfolioGroupsApi->update_portfolio_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio group | 
 **code** | **str**| The code of the portfolio group | 
 **request** | [**UpdatePortfolioGroupRequest**](UpdatePortfolioGroupRequest.md)| The updated definition of the portfolio group | [optional] 

### Return type

[**PortfolioGroup**](PortfolioGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

