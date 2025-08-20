# lusid.PortfolioGroupsApi

All URIs are relative to *https://fbn-prd.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_portfolio_to_group**](PortfolioGroupsApi.md#add_portfolio_to_group) | **POST** /api/portfoliogroups/{scope}/{code}/portfolios | [EARLY ACCESS] AddPortfolioToGroup: Add portfolio to group
[**add_sub_group_to_group**](PortfolioGroupsApi.md#add_sub_group_to_group) | **POST** /api/portfoliogroups/{scope}/{code}/subgroups | [EARLY ACCESS] AddSubGroupToGroup: Add sub group to group
[**build_transactions_for_portfolio_group**](PortfolioGroupsApi.md#build_transactions_for_portfolio_group) | **POST** /api/portfoliogroups/{scope}/{code}/transactions/$build | BuildTransactionsForPortfolioGroup: Build transactions for transaction portfolios in a portfolio group
[**create_portfolio_group**](PortfolioGroupsApi.md#create_portfolio_group) | **POST** /api/portfoliogroups/{scope} | CreatePortfolioGroup: Create portfolio group
[**delete_group_properties**](PortfolioGroupsApi.md#delete_group_properties) | **POST** /api/portfoliogroups/{scope}/{code}/properties/$delete | [EARLY ACCESS] DeleteGroupProperties: Delete group properties
[**delete_key_from_portfolio_group_access_metadata**](PortfolioGroupsApi.md#delete_key_from_portfolio_group_access_metadata) | **DELETE** /api/portfoliogroups/{scope}/{code}/metadata/{metadataKey} | [EARLY ACCESS] DeleteKeyFromPortfolioGroupAccessMetadata: Delete a Portfolio Group Access Metadata entry
[**delete_portfolio_from_group**](PortfolioGroupsApi.md#delete_portfolio_from_group) | **DELETE** /api/portfoliogroups/{scope}/{code}/portfolios/{portfolioScope}/{portfolioCode} | [EARLY ACCESS] DeletePortfolioFromGroup: Delete portfolio from group
[**delete_portfolio_group**](PortfolioGroupsApi.md#delete_portfolio_group) | **DELETE** /api/portfoliogroups/{scope}/{code} | [EARLY ACCESS] DeletePortfolioGroup: Delete portfolio group
[**delete_sub_group_from_group**](PortfolioGroupsApi.md#delete_sub_group_from_group) | **DELETE** /api/portfoliogroups/{scope}/{code}/subgroups/{subgroupScope}/{subgroupCode} | [EARLY ACCESS] DeleteSubGroupFromGroup: Delete sub group from group
[**get_a2_b_data_for_portfolio_group**](PortfolioGroupsApi.md#get_a2_b_data_for_portfolio_group) | **GET** /api/portfoliogroups/{scope}/{code}/a2b | [EARLY ACCESS] GetA2BDataForPortfolioGroup: Get A2B data for a Portfolio Group
[**get_group_properties**](PortfolioGroupsApi.md#get_group_properties) | **GET** /api/portfoliogroups/{scope}/{code}/properties | [EARLY ACCESS] GetGroupProperties: Get group properties
[**get_holdings_for_portfolio_group**](PortfolioGroupsApi.md#get_holdings_for_portfolio_group) | **GET** /api/portfoliogroups/{scope}/{code}/holdings | GetHoldingsForPortfolioGroup: Get holdings for transaction portfolios in portfolio group
[**get_portfolio_group**](PortfolioGroupsApi.md#get_portfolio_group) | **GET** /api/portfoliogroups/{scope}/{code} | GetPortfolioGroup: Get portfolio group
[**get_portfolio_group_access_metadata_by_key**](PortfolioGroupsApi.md#get_portfolio_group_access_metadata_by_key) | **GET** /api/portfoliogroups/{scope}/{code}/metadata/{metadataKey} | [EARLY ACCESS] GetPortfolioGroupAccessMetadataByKey: Get an entry identified by a metadataKey in the Access Metadata of a Portfolio Group
[**get_portfolio_group_commands**](PortfolioGroupsApi.md#get_portfolio_group_commands) | **GET** /api/portfoliogroups/{scope}/{code}/commands | GetPortfolioGroupCommands: Get portfolio group commands
[**get_portfolio_group_expansion**](PortfolioGroupsApi.md#get_portfolio_group_expansion) | **GET** /api/portfoliogroups/{scope}/{code}/expansion | [EARLY ACCESS] GetPortfolioGroupExpansion: Get portfolio group expansion
[**get_portfolio_group_metadata**](PortfolioGroupsApi.md#get_portfolio_group_metadata) | **GET** /api/portfoliogroups/{scope}/{code}/metadata | [EARLY ACCESS] GetPortfolioGroupMetadata: Get Access Metadata rules for Portfolio Group
[**get_portfolio_group_property_time_series**](PortfolioGroupsApi.md#get_portfolio_group_property_time_series) | **GET** /api/portfoliogroups/{scope}/{code}/properties/time-series | [EARLY ACCESS] GetPortfolioGroupPropertyTimeSeries: Get the time series of a portfolio group property
[**get_portfolio_group_relations**](PortfolioGroupsApi.md#get_portfolio_group_relations) | **GET** /api/portfoliogroups/{scope}/{code}/relations | [EXPERIMENTAL] GetPortfolioGroupRelations: Get Relations for Portfolio Group
[**get_portfolio_group_relationships**](PortfolioGroupsApi.md#get_portfolio_group_relationships) | **GET** /api/portfoliogroups/{scope}/{code}/relationships | [EARLY ACCESS] GetPortfolioGroupRelationships: Get Relationships for Portfolio Group
[**get_transactions_for_portfolio_group**](PortfolioGroupsApi.md#get_transactions_for_portfolio_group) | **GET** /api/portfoliogroups/{scope}/{code}/transactions | GetTransactionsForPortfolioGroup: Get transactions for transaction portfolios in a portfolio group
[**list_portfolio_groups**](PortfolioGroupsApi.md#list_portfolio_groups) | **GET** /api/portfoliogroups/{scope} | ListPortfolioGroups: List portfolio groups
[**patch_portfolio_group_access_metadata**](PortfolioGroupsApi.md#patch_portfolio_group_access_metadata) | **PATCH** /api/portfoliogroups/{scope}/{code}/metadata | [EARLY ACCESS] PatchPortfolioGroupAccessMetadata: Patch Access Metadata rules for a Portfolio Group.
[**update_portfolio_group**](PortfolioGroupsApi.md#update_portfolio_group) | **PUT** /api/portfoliogroups/{scope}/{code} | [EARLY ACCESS] UpdatePortfolioGroup: Update portfolio group
[**upsert_group_properties**](PortfolioGroupsApi.md#upsert_group_properties) | **POST** /api/portfoliogroups/{scope}/{code}/properties/$upsert | [EARLY ACCESS] UpsertGroupProperties: Upsert group properties
[**upsert_portfolio_group_access_metadata**](PortfolioGroupsApi.md#upsert_portfolio_group_access_metadata) | **PUT** /api/portfoliogroups/{scope}/{code}/metadata/{metadataKey} | UpsertPortfolioGroupAccessMetadata: Upsert a Portfolio Group Access Metadata entry associated with a specific metadataKey. This creates or updates the data in LUSID.


# **add_portfolio_to_group**
> PortfolioGroup add_portfolio_to_group(scope, code, effective_at=effective_at, resource_id=resource_id)

[EARLY ACCESS] AddPortfolioToGroup: Add portfolio to group

Add a single portfolio to a portfolio group.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    PortfolioGroupsApi
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
    api_instance = api_client_factory.build(PortfolioGroupsApi)
    scope = 'scope_example' # str | The scope of the portfolio group to add a portfolio to.
    code = 'code_example' # str | The code of the portfolio group to add a portfolio to. Together with the scope this uniquely identifies the portfolio group.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label from which the portfolio will be added to the group. (optional)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # resource_id = ResourceId.from_json("")
    # resource_id = ResourceId.from_dict({})
    resource_id = ResourceId()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.add_portfolio_to_group(scope, code, effective_at=effective_at, resource_id=resource_id, opts=opts)

        # [EARLY ACCESS] AddPortfolioToGroup: Add portfolio to group
        api_response = api_instance.add_portfolio_to_group(scope, code, effective_at=effective_at, resource_id=resource_id)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling PortfolioGroupsApi->add_portfolio_to_group: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio group to add a portfolio to. | 
 **code** | **str**| The code of the portfolio group to add a portfolio to. Together with the scope this uniquely identifies the portfolio group. | 
 **effective_at** | **str**| The effective datetime or cut label from which the portfolio will be added to the group. | [optional] 
 **resource_id** | [**ResourceId**](ResourceId.md)| The resource identifier of the portfolio to add to the portfolio group. | [optional] 

### Return type

[**PortfolioGroup**](PortfolioGroup.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The portfolio group containing the newly added portfolio |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **add_sub_group_to_group**
> PortfolioGroup add_sub_group_to_group(scope, code, effective_at=effective_at, resource_id=resource_id)

[EARLY ACCESS] AddSubGroupToGroup: Add sub group to group

Add a portfolio group to a portfolio group as a sub group.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    PortfolioGroupsApi
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
    api_instance = api_client_factory.build(PortfolioGroupsApi)
    scope = 'scope_example' # str | The scope of the portfolio group to add a portfolio group to.
    code = 'code_example' # str | The code of the portfolio group to add a portfolio group to. Together with the scope this uniquely identifies the portfolio group.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label from which the sub group will be added to the group. (optional)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # resource_id = ResourceId.from_json("")
    # resource_id = ResourceId.from_dict({})
    resource_id = ResourceId()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.add_sub_group_to_group(scope, code, effective_at=effective_at, resource_id=resource_id, opts=opts)

        # [EARLY ACCESS] AddSubGroupToGroup: Add sub group to group
        api_response = api_instance.add_sub_group_to_group(scope, code, effective_at=effective_at, resource_id=resource_id)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling PortfolioGroupsApi->add_sub_group_to_group: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio group to add a portfolio group to. | 
 **code** | **str**| The code of the portfolio group to add a portfolio group to. Together with the scope this uniquely identifies the portfolio group. | 
 **effective_at** | **str**| The effective datetime or cut label from which the sub group will be added to the group. | [optional] 
 **resource_id** | [**ResourceId**](ResourceId.md)| The resource identifier of the portfolio group to add to the portfolio group as a sub group. | [optional] 

### Return type

[**PortfolioGroup**](PortfolioGroup.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The portfolio group containing the newly added portfolio group as a sub group |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **build_transactions_for_portfolio_group**
> VersionedResourceListOfOutputTransaction build_transactions_for_portfolio_group(scope, code, transaction_query_parameters, as_at=as_at, filter=filter, property_keys=property_keys, limit=limit, page=page)

BuildTransactionsForPortfolioGroup: Build transactions for transaction portfolios in a portfolio group

Build transactions for transaction portfolios in a portfolio group over a given interval of effective time.              When the specified portfolio in a portfolio group is a derived transaction portfolio, the returned set of transactions is the union set of all transactions of the parent (and any grandparents etc.) and the specified derived transaction portfolio itself.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    PortfolioGroupsApi
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
    api_instance = api_client_factory.build(PortfolioGroupsApi)
    scope = 'scope_example' # str | The scope of the portfolio group.
    code = 'code_example' # str | The code of the portfolio group. Together with the scope this uniquely identifies              the portfolio group.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # transaction_query_parameters = TransactionQueryParameters.from_json("")
    # transaction_query_parameters = TransactionQueryParameters.from_dict({})
    transaction_query_parameters = TransactionQueryParameters()
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to build the transactions. Defaults to return the latest              version of each transaction if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the result set.              For example, to filter on the Transaction Type, use \"type eq 'Buy'\"              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the \"Instrument\" or \"Transaction\" domain to decorate onto              the transactions. These take the format {domain}/{scope}/{code} e.g. \"Instrument/system/Name\" or              \"Transaction/strategy/quantsignal\". (optional)
    limit = 56 # int | When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing transactions from a previous call to BuildTransactions. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.build_transactions_for_portfolio_group(scope, code, transaction_query_parameters, as_at=as_at, filter=filter, property_keys=property_keys, limit=limit, page=page, opts=opts)

        # BuildTransactionsForPortfolioGroup: Build transactions for transaction portfolios in a portfolio group
        api_response = api_instance.build_transactions_for_portfolio_group(scope, code, transaction_query_parameters, as_at=as_at, filter=filter, property_keys=property_keys, limit=limit, page=page)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling PortfolioGroupsApi->build_transactions_for_portfolio_group: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio group. | 
 **code** | **str**| The code of the portfolio group. Together with the scope this uniquely identifies              the portfolio group. | 
 **transaction_query_parameters** | [**TransactionQueryParameters**](TransactionQueryParameters.md)| The query queryParameters which control how the output transactions are built. | 
 **as_at** | **datetime**| The asAt datetime at which to build the transactions. Defaults to return the latest              version of each transaction if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set.              For example, to filter on the Transaction Type, use \&quot;type eq &#39;Buy&#39;\&quot;              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the \&quot;Instrument\&quot; or \&quot;Transaction\&quot; domain to decorate onto              the transactions. These take the format {domain}/{scope}/{code} e.g. \&quot;Instrument/system/Name\&quot; or              \&quot;Transaction/strategy/quantsignal\&quot;. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing transactions from a previous call to BuildTransactions. | [optional] 

### Return type

[**VersionedResourceListOfOutputTransaction**](VersionedResourceListOfOutputTransaction.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested transactions from transaction portfolios in the specified portfolio group |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **create_portfolio_group**
> PortfolioGroup create_portfolio_group(scope, create_portfolio_group_request=create_portfolio_group_request)

CreatePortfolioGroup: Create portfolio group

Create a portfolio group in a specific scope.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    PortfolioGroupsApi
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
    api_instance = api_client_factory.build(PortfolioGroupsApi)
    scope = 'scope_example' # str | The scope that the portfolio group will be created in.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # create_portfolio_group_request = CreatePortfolioGroupRequest.from_json("")
    # create_portfolio_group_request = CreatePortfolioGroupRequest.from_dict({})
    create_portfolio_group_request = CreatePortfolioGroupRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.create_portfolio_group(scope, create_portfolio_group_request=create_portfolio_group_request, opts=opts)

        # CreatePortfolioGroup: Create portfolio group
        api_response = api_instance.create_portfolio_group(scope, create_portfolio_group_request=create_portfolio_group_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling PortfolioGroupsApi->create_portfolio_group: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that the portfolio group will be created in. | 
 **create_portfolio_group_request** | [**CreatePortfolioGroupRequest**](CreatePortfolioGroupRequest.md)| The definition and details of the portfolio group. | [optional] 

### Return type

[**PortfolioGroup**](PortfolioGroup.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created portfolio group |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_group_properties**
> DeletedEntityResponse delete_group_properties(scope, code, request_body, effective_at=effective_at)

[EARLY ACCESS] DeleteGroupProperties: Delete group properties

Delete one or more properties from a single portfolio group. If the properties are time variant then an effective date time from which the properties will be deleted must be specified. If the properties are perpetual then it is invalid to specify an effective date time for deletion.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    PortfolioGroupsApi
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
    api_instance = api_client_factory.build(PortfolioGroupsApi)
    scope = 'scope_example' # str | The scope of the group to delete properties from.
    code = 'code_example' # str | The code of the group to delete properties from. Together with the scope this uniquely identifies the group.
    request_body = ["PortfolioGroup/MyScope/MyPropertyName","PortfolioGroup/MyScope/MyPropertyName2"] # List[str] | The property keys of the properties to delete. These take the format             {domain}/{scope}/{code} e.g. \"PortfolioGroup/Manager/Id\". Each property must be from the \"PortfolioGroup\" domain.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to delete time-variant properties from.             The property must exist at the specified 'effectiveAt' datetime. If the 'effectiveAt' is not provided or is             before the time-variant property exists then a failure is returned. Do not specify this parameter if any of             the properties to delete are perpetual. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_group_properties(scope, code, request_body, effective_at=effective_at, opts=opts)

        # [EARLY ACCESS] DeleteGroupProperties: Delete group properties
        api_response = api_instance.delete_group_properties(scope, code, request_body, effective_at=effective_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling PortfolioGroupsApi->delete_group_properties: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the group to delete properties from. | 
 **code** | **str**| The code of the group to delete properties from. Together with the scope this uniquely identifies the group. | 
 **request_body** | [**List[str]**](str.md)| The property keys of the properties to delete. These take the format             {domain}/{scope}/{code} e.g. \&quot;PortfolioGroup/Manager/Id\&quot;. Each property must be from the \&quot;PortfolioGroup\&quot; domain. | 
 **effective_at** | **str**| The effective datetime or cut label at which to delete time-variant properties from.             The property must exist at the specified &#39;effectiveAt&#39; datetime. If the &#39;effectiveAt&#39; is not provided or is             before the time-variant property exists then a failure is returned. Do not specify this parameter if any of             the properties to delete are perpetual. | [optional] 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the properties were deleted from the specified group |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_key_from_portfolio_group_access_metadata**
> DeletedEntityResponse delete_key_from_portfolio_group_access_metadata(scope, code, metadata_key, effective_at=effective_at, effective_until=effective_until)

[EARLY ACCESS] DeleteKeyFromPortfolioGroupAccessMetadata: Delete a Portfolio Group Access Metadata entry

Deletes the Portfolio Group Access Metadata entry that exactly matches the provided identifier parts.  It is important to always check to verify success (or failure).

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    PortfolioGroupsApi
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
    api_instance = api_client_factory.build(PortfolioGroupsApi)
    scope = 'scope_example' # str | The scope of the Portfolio Group
    code = 'code_example' # str | The Portfolio Group code
    metadata_key = 'metadata_key_example' # str | Key of the Access Metadata entry to delete
    effective_at = 'effective_at_example' # str | The effective date to delete at, if this is not supplied, it will delete all data found (optional)
    effective_until = '2013-10-20T19:20:30+01:00' # datetime | The effective date until which the delete is valid. If not supplied this will be valid indefinitely, or until the next 'effectiveAt' date of the Access Metadata (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_key_from_portfolio_group_access_metadata(scope, code, metadata_key, effective_at=effective_at, effective_until=effective_until, opts=opts)

        # [EARLY ACCESS] DeleteKeyFromPortfolioGroupAccessMetadata: Delete a Portfolio Group Access Metadata entry
        api_response = api_instance.delete_key_from_portfolio_group_access_metadata(scope, code, metadata_key, effective_at=effective_at, effective_until=effective_until)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling PortfolioGroupsApi->delete_key_from_portfolio_group_access_metadata: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Portfolio Group | 
 **code** | **str**| The Portfolio Group code | 
 **metadata_key** | **str**| Key of the Access Metadata entry to delete | 
 **effective_at** | **str**| The effective date to delete at, if this is not supplied, it will delete all data found | [optional] 
 **effective_until** | **datetime**| The effective date until which the delete is valid. If not supplied this will be valid indefinitely, or until the next &#39;effectiveAt&#39; date of the Access Metadata | [optional] 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The has been deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_portfolio_from_group**
> PortfolioGroup delete_portfolio_from_group(scope, code, portfolio_scope, portfolio_code, effective_at=effective_at)

[EARLY ACCESS] DeletePortfolioFromGroup: Delete portfolio from group

Remove a single portfolio from a portfolio group.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    PortfolioGroupsApi
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
    api_instance = api_client_factory.build(PortfolioGroupsApi)
    scope = 'scope_example' # str | The scope of the portfolio group to remove the portfolio from.
    code = 'code_example' # str | The code of the portfolio group to remove the portfolio from. Together with the scope this uniquely identifies the portfolio group.
    portfolio_scope = 'portfolio_scope_example' # str | The scope of the portfolio being removed from the portfolio group.
    portfolio_code = 'portfolio_code_example' # str | The code of the portfolio being removed from the portfolio group. Together with the scope this uniquely identifies the portfolio to remove.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label from which the portfolio will be removed from the portfolio group. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_portfolio_from_group(scope, code, portfolio_scope, portfolio_code, effective_at=effective_at, opts=opts)

        # [EARLY ACCESS] DeletePortfolioFromGroup: Delete portfolio from group
        api_response = api_instance.delete_portfolio_from_group(scope, code, portfolio_scope, portfolio_code, effective_at=effective_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling PortfolioGroupsApi->delete_portfolio_from_group: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio group to remove the portfolio from. | 
 **code** | **str**| The code of the portfolio group to remove the portfolio from. Together with the scope this uniquely identifies the portfolio group. | 
 **portfolio_scope** | **str**| The scope of the portfolio being removed from the portfolio group. | 
 **portfolio_code** | **str**| The code of the portfolio being removed from the portfolio group. Together with the scope this uniquely identifies the portfolio to remove. | 
 **effective_at** | **str**| The effective datetime or cut label from which the portfolio will be removed from the portfolio group. | [optional] 

### Return type

[**PortfolioGroup**](PortfolioGroup.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The portfolio group with the portfolio removed from the group |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_portfolio_group**
> DeletedEntityResponse delete_portfolio_group(scope, code)

[EARLY ACCESS] DeletePortfolioGroup: Delete portfolio group

Delete a single portfolio group. A portfolio group can be deleted while it still contains portfolios or sub groups. In this case any portfolios or sub groups contained in this group will not be deleted, however they will no longer be grouped together by this portfolio group. The deletion will be valid from the portfolio group's creation datetime, ie. the portfolio group will no longer exist at any effective datetime from the asAt datetime of deletion.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    PortfolioGroupsApi
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
    api_instance = api_client_factory.build(PortfolioGroupsApi)
    scope = 'scope_example' # str | The scope of the portfolio group to delete.
    code = 'code_example' # str | The code of the portfolio group to delete. Together with the scope this uniquely identifies the portfolio group to delete.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_portfolio_group(scope, code, opts=opts)

        # [EARLY ACCESS] DeletePortfolioGroup: Delete portfolio group
        api_response = api_instance.delete_portfolio_group(scope, code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling PortfolioGroupsApi->delete_portfolio_group: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio group to delete. | 
 **code** | **str**| The code of the portfolio group to delete. Together with the scope this uniquely identifies the portfolio group to delete. | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the portfolio group was deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_sub_group_from_group**
> PortfolioGroup delete_sub_group_from_group(scope, code, subgroup_scope, subgroup_code, effective_at=effective_at)

[EARLY ACCESS] DeleteSubGroupFromGroup: Delete sub group from group

Remove a single portfolio group (sub group) from a portfolio group.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    PortfolioGroupsApi
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
    api_instance = api_client_factory.build(PortfolioGroupsApi)
    scope = 'scope_example' # str | The scope of the portfolio group to remove the sub group from.
    code = 'code_example' # str | The code of the portfolio group to remove the sub group from. Together with the scope this uniquely identifies the portfolio group.
    subgroup_scope = 'subgroup_scope_example' # str | The scope of the sub group to remove from the portfolio group.
    subgroup_code = 'subgroup_code_example' # str | The code of the sub group to remove from the portfolio group. Together with the scope this uniquely identifies the sub group.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label from which the sub group will be removed from the portfolio group. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_sub_group_from_group(scope, code, subgroup_scope, subgroup_code, effective_at=effective_at, opts=opts)

        # [EARLY ACCESS] DeleteSubGroupFromGroup: Delete sub group from group
        api_response = api_instance.delete_sub_group_from_group(scope, code, subgroup_scope, subgroup_code, effective_at=effective_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling PortfolioGroupsApi->delete_sub_group_from_group: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio group to remove the sub group from. | 
 **code** | **str**| The code of the portfolio group to remove the sub group from. Together with the scope this uniquely identifies the portfolio group. | 
 **subgroup_scope** | **str**| The scope of the sub group to remove from the portfolio group. | 
 **subgroup_code** | **str**| The code of the sub group to remove from the portfolio group. Together with the scope this uniquely identifies the sub group. | 
 **effective_at** | **str**| The effective datetime or cut label from which the sub group will be removed from the portfolio group. | [optional] 

### Return type

[**PortfolioGroup**](PortfolioGroup.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The portfolio group with the sub group removed from the group |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_a2_b_data_for_portfolio_group**
> VersionedResourceListOfA2BDataRecord get_a2_b_data_for_portfolio_group(scope, code, from_effective_at, to_effective_at, as_at=as_at, recipe_id_scope=recipe_id_scope, recipe_id_code=recipe_id_code, property_keys=property_keys, filter=filter)

[EARLY ACCESS] GetA2BDataForPortfolioGroup: Get A2B data for a Portfolio Group

Get an A2B report for all Transaction Portfolios within the given portfolio group.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    PortfolioGroupsApi
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
    api_instance = api_client_factory.build(PortfolioGroupsApi)
    scope = 'scope_example' # str | The scope of the group to retrieve the A2B report for.
    code = 'code_example' # str | The code of the group to retrieve the A2B report for. Together with the scope this             uniquely identifies the portfolio group.
    from_effective_at = 'from_effective_at_example' # str | The lower bound effective datetime or cut label (inclusive) from which to retrieve the data.             There is no lower bound if this is not specified.
    to_effective_at = 'to_effective_at_example' # str | The upper bound effective datetime or cut label (inclusive) from which to retrieve the data.             There is no upper bound if this is not specified.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the portfolio. Defaults to return the latest version             of each transaction if not specified. (optional)
    recipe_id_scope = 'recipe_id_scope_example' # str | The scope of the given recipeId (optional)
    recipe_id_code = 'recipe_id_code_example' # str | The code of the given recipeId (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the \"Instrument\" domain to decorate onto             the results. These take the format {domain}/{scope}/{code} e.g. \"Instrument/system/Name\". (optional)
    filter = 'filter_example' # str | Expression to filter the result set.             Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_a2_b_data_for_portfolio_group(scope, code, from_effective_at, to_effective_at, as_at=as_at, recipe_id_scope=recipe_id_scope, recipe_id_code=recipe_id_code, property_keys=property_keys, filter=filter, opts=opts)

        # [EARLY ACCESS] GetA2BDataForPortfolioGroup: Get A2B data for a Portfolio Group
        api_response = api_instance.get_a2_b_data_for_portfolio_group(scope, code, from_effective_at, to_effective_at, as_at=as_at, recipe_id_scope=recipe_id_scope, recipe_id_code=recipe_id_code, property_keys=property_keys, filter=filter)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling PortfolioGroupsApi->get_a2_b_data_for_portfolio_group: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the group to retrieve the A2B report for. | 
 **code** | **str**| The code of the group to retrieve the A2B report for. Together with the scope this             uniquely identifies the portfolio group. | 
 **from_effective_at** | **str**| The lower bound effective datetime or cut label (inclusive) from which to retrieve the data.             There is no lower bound if this is not specified. | 
 **to_effective_at** | **str**| The upper bound effective datetime or cut label (inclusive) from which to retrieve the data.             There is no upper bound if this is not specified. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the portfolio. Defaults to return the latest version             of each transaction if not specified. | [optional] 
 **recipe_id_scope** | **str**| The scope of the given recipeId | [optional] 
 **recipe_id_code** | **str**| The code of the given recipeId | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the \&quot;Instrument\&quot; domain to decorate onto             the results. These take the format {domain}/{scope}/{code} e.g. \&quot;Instrument/system/Name\&quot;. | [optional] 
 **filter** | **str**| Expression to filter the result set.             Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 

### Return type

[**VersionedResourceListOfA2BDataRecord**](VersionedResourceListOfA2BDataRecord.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested group A2B data |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_group_properties**
> PortfolioGroupProperties get_group_properties(scope, code, effective_at=effective_at, as_at=as_at)

[EARLY ACCESS] GetGroupProperties: Get group properties

List all the properties of a single portfolio group.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    PortfolioGroupsApi
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
    api_instance = api_client_factory.build(PortfolioGroupsApi)
    scope = 'scope_example' # str | The scope of the group to list the properties for.
    code = 'code_example' # str | The code of the group to list the properties for. Together with the scope this uniquely identifies the group.
    effective_at = 'effective_at_example' # str | The effective date time or cut label at which to list the group's properties. Defaults to the current LUSID system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt date time at which to list the group's properties. Defaults to return the latest version of each property if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_group_properties(scope, code, effective_at=effective_at, as_at=as_at, opts=opts)

        # [EARLY ACCESS] GetGroupProperties: Get group properties
        api_response = api_instance.get_group_properties(scope, code, effective_at=effective_at, as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling PortfolioGroupsApi->get_group_properties: %s\n" % e)

main()
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

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The properties of the specified group |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_holdings_for_portfolio_group**
> VersionedResourceListOfPortfolioHolding get_holdings_for_portfolio_group(scope, code, effective_at=effective_at, as_at=as_at, filter=filter, property_keys=property_keys, by_taxlots=by_taxlots, include_settlement_events_after_days=include_settlement_events_after_days)

GetHoldingsForPortfolioGroup: Get holdings for transaction portfolios in portfolio group

Get the holdings of transaction portfolios in specified portfolio group.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    PortfolioGroupsApi
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
    api_instance = api_client_factory.build(PortfolioGroupsApi)
    scope = 'scope_example' # str | The scope of the portfolio group.
    code = 'code_example' # str | The code of the portfolio group. Together with the scope this uniquely identifies             the portfolio group.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve the holdings of transaction             portfolios in the portfolio group. Defaults to the current LUSID system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the holdings of transaction portfolios in the portfolio group. Defaults             to return the latest version of the holdings if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the \"Instrument\", \"Holding\" or \"Portfolio\" domain to decorate onto             the holdings. These take the format {domain}/{scope}/{code} e.g. \"Instrument/system/Name\" or \"Holding/system/Cost\". (optional)
    by_taxlots = True # bool | Whether or not to expand the holdings to return the underlying tax-lots. Defaults to             False. (optional)
    include_settlement_events_after_days = 56 # int | Number of days ahead to bring back settlements from, in relation to the specified effectiveAt (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_holdings_for_portfolio_group(scope, code, effective_at=effective_at, as_at=as_at, filter=filter, property_keys=property_keys, by_taxlots=by_taxlots, include_settlement_events_after_days=include_settlement_events_after_days, opts=opts)

        # GetHoldingsForPortfolioGroup: Get holdings for transaction portfolios in portfolio group
        api_response = api_instance.get_holdings_for_portfolio_group(scope, code, effective_at=effective_at, as_at=as_at, filter=filter, property_keys=property_keys, by_taxlots=by_taxlots, include_settlement_events_after_days=include_settlement_events_after_days)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling PortfolioGroupsApi->get_holdings_for_portfolio_group: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio group. | 
 **code** | **str**| The code of the portfolio group. Together with the scope this uniquely identifies             the portfolio group. | 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the holdings of transaction             portfolios in the portfolio group. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the holdings of transaction portfolios in the portfolio group. Defaults             to return the latest version of the holdings if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the \&quot;Instrument\&quot;, \&quot;Holding\&quot; or \&quot;Portfolio\&quot; domain to decorate onto             the holdings. These take the format {domain}/{scope}/{code} e.g. \&quot;Instrument/system/Name\&quot; or \&quot;Holding/system/Cost\&quot;. | [optional] 
 **by_taxlots** | **bool**| Whether or not to expand the holdings to return the underlying tax-lots. Defaults to             False. | [optional] 
 **include_settlement_events_after_days** | **int**| Number of days ahead to bring back settlements from, in relation to the specified effectiveAt | [optional] 

### Return type

[**VersionedResourceListOfPortfolioHolding**](VersionedResourceListOfPortfolioHolding.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The holdings of transaction portfolios in a specific version of portfolio group |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_portfolio_group**
> PortfolioGroup get_portfolio_group(scope, code, effective_at=effective_at, as_at=as_at, related_entity_property_keys=related_entity_property_keys, relationship_definition_ids=relationship_definition_ids)

GetPortfolioGroup: Get portfolio group

Retrieve the definition of a single portfolio group.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    PortfolioGroupsApi
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
    api_instance = api_client_factory.build(PortfolioGroupsApi)
    scope = 'scope_example' # str | The scope of the portfolio group to retrieve the definition for.
    code = 'code_example' # str | The code of the portfolio group to retrieve the definition for. Together with the scope             this uniquely identifies the portfolio group.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve the portfolio group definition. Defaults to the current LUSID system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the portfolio group definition. Defaults to return             the latest version of the portfolio group definition if not specified. (optional)
    related_entity_property_keys = ['related_entity_property_keys_example'] # List[str] | A list of property keys from any domain that supports relationships             to decorate onto related entities. These must take the format {domain}/{scope}/{code}, for example 'Portfolio/Manager/Id'. (optional)
    relationship_definition_ids = ['relationship_definition_ids_example'] # List[str] | A list of relationship definitions that are used to decorate related entities             onto the portfolio group in the response. These must take the form {relationshipDefinitionScope}/{relationshipDefinitionCode}. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_portfolio_group(scope, code, effective_at=effective_at, as_at=as_at, related_entity_property_keys=related_entity_property_keys, relationship_definition_ids=relationship_definition_ids, opts=opts)

        # GetPortfolioGroup: Get portfolio group
        api_response = api_instance.get_portfolio_group(scope, code, effective_at=effective_at, as_at=as_at, related_entity_property_keys=related_entity_property_keys, relationship_definition_ids=relationship_definition_ids)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling PortfolioGroupsApi->get_portfolio_group: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio group to retrieve the definition for. | 
 **code** | **str**| The code of the portfolio group to retrieve the definition for. Together with the scope             this uniquely identifies the portfolio group. | 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the portfolio group definition. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the portfolio group definition. Defaults to return             the latest version of the portfolio group definition if not specified. | [optional] 
 **related_entity_property_keys** | [**List[str]**](str.md)| A list of property keys from any domain that supports relationships             to decorate onto related entities. These must take the format {domain}/{scope}/{code}, for example &#39;Portfolio/Manager/Id&#39;. | [optional] 
 **relationship_definition_ids** | [**List[str]**](str.md)| A list of relationship definitions that are used to decorate related entities             onto the portfolio group in the response. These must take the form {relationshipDefinitionScope}/{relationshipDefinitionCode}. | [optional] 

### Return type

[**PortfolioGroup**](PortfolioGroup.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested portfolio group definition |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_portfolio_group_access_metadata_by_key**
> List[AccessMetadataValue] get_portfolio_group_access_metadata_by_key(scope, code, metadata_key, effective_at=effective_at, as_at=as_at)

[EARLY ACCESS] GetPortfolioGroupAccessMetadataByKey: Get an entry identified by a metadataKey in the Access Metadata of a Portfolio Group

Get a specific Portfolio Group access metadata by specifying the corresponding identifier parts              No matching will be performed through this endpoint. To retrieve a rule, it is necessary to specify, exactly, the identifier of the rule

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    PortfolioGroupsApi
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
    api_instance = api_client_factory.build(PortfolioGroupsApi)
    scope = 'scope_example' # str | The scope of the Portfolio Group
    code = 'code_example' # str | The Portfolio Group code
    metadata_key = 'metadata_key_example' # str | Key of the metadata entry to retrieve
    effective_at = 'effective_at_example' # str | The effectiveAt datetime at which to retrieve the access metadata (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the access metadata (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_portfolio_group_access_metadata_by_key(scope, code, metadata_key, effective_at=effective_at, as_at=as_at, opts=opts)

        # [EARLY ACCESS] GetPortfolioGroupAccessMetadataByKey: Get an entry identified by a metadataKey in the Access Metadata of a Portfolio Group
        api_response = api_instance.get_portfolio_group_access_metadata_by_key(scope, code, metadata_key, effective_at=effective_at, as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling PortfolioGroupsApi->get_portfolio_group_access_metadata_by_key: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Portfolio Group | 
 **code** | **str**| The Portfolio Group code | 
 **metadata_key** | **str**| Key of the metadata entry to retrieve | 
 **effective_at** | **str**| The effectiveAt datetime at which to retrieve the access metadata | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the access metadata | [optional] 

### Return type

[**List[AccessMetadataValue]**](AccessMetadataValue.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully retrieved Portfolio group access metadata filtered by metadataKey or any failure. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_portfolio_group_commands**
> ResourceListOfProcessedCommand get_portfolio_group_commands(scope, code, from_as_at=from_as_at, to_as_at=to_as_at, filter=filter)

GetPortfolioGroupCommands: Get portfolio group commands

Gets all the commands that modified a single portfolio group.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    PortfolioGroupsApi
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
    api_instance = api_client_factory.build(PortfolioGroupsApi)
    scope = 'scope_example' # str | The scope of the portfolio group to retrieve the commands for.
    code = 'code_example' # str | The code of the portfolio group to retrieve the commands for. Together with the scope this uniquely identifies the portfolio group.
    from_as_at = '2013-10-20T19:20:30+01:00' # datetime | The lower bound asAt datetime (inclusive) from which to retrieve commands. There is no lower bound if this is not specified. (optional)
    to_as_at = '2013-10-20T19:20:30+01:00' # datetime | The upper bound asAt datetime (inclusive) from which to retrieve commands. There is no upper bound if this is not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the result set.              For example, to filter on the User ID, use \"userId.id eq 'string'\"             Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_portfolio_group_commands(scope, code, from_as_at=from_as_at, to_as_at=to_as_at, filter=filter, opts=opts)

        # GetPortfolioGroupCommands: Get portfolio group commands
        api_response = api_instance.get_portfolio_group_commands(scope, code, from_as_at=from_as_at, to_as_at=to_as_at, filter=filter)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling PortfolioGroupsApi->get_portfolio_group_commands: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio group to retrieve the commands for. | 
 **code** | **str**| The code of the portfolio group to retrieve the commands for. Together with the scope this uniquely identifies the portfolio group. | 
 **from_as_at** | **datetime**| The lower bound asAt datetime (inclusive) from which to retrieve commands. There is no lower bound if this is not specified. | [optional] 
 **to_as_at** | **datetime**| The upper bound asAt datetime (inclusive) from which to retrieve commands. There is no upper bound if this is not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set.              For example, to filter on the User ID, use \&quot;userId.id eq &#39;string&#39;\&quot;             Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 

### Return type

[**ResourceListOfProcessedCommand**](ResourceListOfProcessedCommand.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The commands that modified the specified portfolio group |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_portfolio_group_expansion**
> ExpandedGroup get_portfolio_group_expansion(scope, code, effective_at=effective_at, as_at=as_at, property_filter=property_filter)

[EARLY ACCESS] GetPortfolioGroupExpansion: Get portfolio group expansion

List all the portfolios in a group, including all portfolios within sub groups in the group. Each portfolio will be decorated with all of its properties unless a property filter is specified.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    PortfolioGroupsApi
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
    api_instance = api_client_factory.build(PortfolioGroupsApi)
    scope = 'scope_example' # str | The scope of the portfolio group to expand.
    code = 'code_example' # str | The code of the portfolio group to expand. Together with the scope this uniquely identifies the portfolio             group to expand.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to expand the portfolio group. Defaults to the current LUSID system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to expand the portfolio group. Defaults to return the latest version of each portfolio in the group if not specified. (optional)
    property_filter = ['property_filter_example'] # List[str] | The restricted list of property keys from the \"Portfolio\" domain which will be decorated onto each portfolio. These take the format {domain}/{scope}/{code} e.g. \"Portfolio/Manager/Id\". (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_portfolio_group_expansion(scope, code, effective_at=effective_at, as_at=as_at, property_filter=property_filter, opts=opts)

        # [EARLY ACCESS] GetPortfolioGroupExpansion: Get portfolio group expansion
        api_response = api_instance.get_portfolio_group_expansion(scope, code, effective_at=effective_at, as_at=as_at, property_filter=property_filter)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling PortfolioGroupsApi->get_portfolio_group_expansion: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio group to expand. | 
 **code** | **str**| The code of the portfolio group to expand. Together with the scope this uniquely identifies the portfolio             group to expand. | 
 **effective_at** | **str**| The effective datetime or cut label at which to expand the portfolio group. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to expand the portfolio group. Defaults to return the latest version of each portfolio in the group if not specified. | [optional] 
 **property_filter** | [**List[str]**](str.md)| The restricted list of property keys from the \&quot;Portfolio\&quot; domain which will be decorated onto each portfolio. These take the format {domain}/{scope}/{code} e.g. \&quot;Portfolio/Manager/Id\&quot;. | [optional] 

### Return type

[**ExpandedGroup**](ExpandedGroup.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The expanded portfolio group |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_portfolio_group_metadata**
> Dict[str, List[AccessMetadataValue]] get_portfolio_group_metadata(scope, code, effective_at=effective_at, as_at=as_at)

[EARLY ACCESS] GetPortfolioGroupMetadata: Get Access Metadata rules for Portfolio Group

Pass the scope and Portfolio Group code parameters to retrieve the associated Access Metadata

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    PortfolioGroupsApi
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
    api_instance = api_client_factory.build(PortfolioGroupsApi)
    scope = 'scope_example' # str | The scope of the Portfolio Group
    code = 'code_example' # str | The Portfolio Group code
    effective_at = 'effective_at_example' # str | The effectiveAt datetime at which to retrieve the Access Metadata (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Access Metadata (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_portfolio_group_metadata(scope, code, effective_at=effective_at, as_at=as_at, opts=opts)

        # [EARLY ACCESS] GetPortfolioGroupMetadata: Get Access Metadata rules for Portfolio Group
        api_response = api_instance.get_portfolio_group_metadata(scope, code, effective_at=effective_at, as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling PortfolioGroupsApi->get_portfolio_group_metadata: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Portfolio Group | 
 **code** | **str**| The Portfolio Group code | 
 **effective_at** | **str**| The effectiveAt datetime at which to retrieve the Access Metadata | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Access Metadata | [optional] 

### Return type

**Dict[str, List[AccessMetadataValue]]**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The access metadata for the portfolio group or any failure. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_portfolio_group_property_time_series**
> ResourceListOfPropertyInterval get_portfolio_group_property_time_series(scope, code, property_key, portfolio_group_effective_at=portfolio_group_effective_at, as_at=as_at, filter=filter, page=page, limit=limit)

[EARLY ACCESS] GetPortfolioGroupPropertyTimeSeries: Get the time series of a portfolio group property

List the complete time series of a portfolio group property.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    PortfolioGroupsApi
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
    api_instance = api_client_factory.build(PortfolioGroupsApi)
    scope = 'scope_example' # str | The scope of the group.
    code = 'code_example' # str | The code of the group. Together with the scope this uniquely identifies             the portfolio group.
    property_key = 'property_key_example' # str | The property key of the property that will have its history shown. These must be in the format {domain}/{scope}/{code} e.g. \"PortfolioGroup/Manager/Id\".             Each property must be from the \"PortfolioGroup\" domain.
    portfolio_group_effective_at = 'portfolio_group_effective_at_example' # str | The effective datetime used to resolve the portfolio group. Defaults to the current LUSID system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the portfolio group's property history. Defaults to return the current datetime if not supplied. (optional)
    filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing properties from a previous call to get property time series.             This value is returned from the previous call. If a pagination token is provided the filter, effectiveAt, and asAt fields             must not have changed since the original request. (optional)
    limit = 56 # int | When paginating, limit the number of returned results to this many. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_portfolio_group_property_time_series(scope, code, property_key, portfolio_group_effective_at=portfolio_group_effective_at, as_at=as_at, filter=filter, page=page, limit=limit, opts=opts)

        # [EARLY ACCESS] GetPortfolioGroupPropertyTimeSeries: Get the time series of a portfolio group property
        api_response = api_instance.get_portfolio_group_property_time_series(scope, code, property_key, portfolio_group_effective_at=portfolio_group_effective_at, as_at=as_at, filter=filter, page=page, limit=limit)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling PortfolioGroupsApi->get_portfolio_group_property_time_series: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the group. | 
 **code** | **str**| The code of the group. Together with the scope this uniquely identifies             the portfolio group. | 
 **property_key** | **str**| The property key of the property that will have its history shown. These must be in the format {domain}/{scope}/{code} e.g. \&quot;PortfolioGroup/Manager/Id\&quot;.             Each property must be from the \&quot;PortfolioGroup\&quot; domain. | 
 **portfolio_group_effective_at** | **str**| The effective datetime used to resolve the portfolio group. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the portfolio group&#39;s property history. Defaults to return the current datetime if not supplied. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **page** | **str**| The pagination token to use to continue listing properties from a previous call to get property time series.             This value is returned from the previous call. If a pagination token is provided the filter, effectiveAt, and asAt fields             must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] 

### Return type

[**ResourceListOfPropertyInterval**](ResourceListOfPropertyInterval.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The time series of the property |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_portfolio_group_relations**
> ResourceListOfRelation get_portfolio_group_relations(scope, code, effective_at=effective_at, as_at=as_at, filter=filter, identifier_types=identifier_types)

[EXPERIMENTAL] GetPortfolioGroupRelations: Get Relations for Portfolio Group

Get relations for the specified Portfolio Group

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    PortfolioGroupsApi
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
    api_instance = api_client_factory.build(PortfolioGroupsApi)
    scope = 'scope_example' # str | The scope of the portfolio group.
    code = 'code_example' # str | The code of the portfolio group. Together with the scope this uniquely identifies             the portfolio group.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve relations. Defaults to the current LUSID system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve relations. Defaults to return the latest LUSID AsAt time if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the relations. Users should provide null or empty string for this field until further notice. (optional)
    identifier_types = ['identifier_types_example'] # List[str] | Identifiers types (as property keys) used for referencing Persons or Legal Entities. These take the format             {domain}/{scope}/{code} e.g. \"Person/CompanyDetails/Role\". They must be from the \"Person\" or \"LegalEntity\" domain.             Only identifier types stated will be used to look up relevant entities in relations. If not applicable, provide an empty array. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_portfolio_group_relations(scope, code, effective_at=effective_at, as_at=as_at, filter=filter, identifier_types=identifier_types, opts=opts)

        # [EXPERIMENTAL] GetPortfolioGroupRelations: Get Relations for Portfolio Group
        api_response = api_instance.get_portfolio_group_relations(scope, code, effective_at=effective_at, as_at=as_at, filter=filter, identifier_types=identifier_types)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling PortfolioGroupsApi->get_portfolio_group_relations: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio group. | 
 **code** | **str**| The code of the portfolio group. Together with the scope this uniquely identifies             the portfolio group. | 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve relations. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve relations. Defaults to return the latest LUSID AsAt time if not specified. | [optional] 
 **filter** | **str**| Expression to filter the relations. Users should provide null or empty string for this field until further notice. | [optional] 
 **identifier_types** | [**List[str]**](str.md)| Identifiers types (as property keys) used for referencing Persons or Legal Entities. These take the format             {domain}/{scope}/{code} e.g. \&quot;Person/CompanyDetails/Role\&quot;. They must be from the \&quot;Person\&quot; or \&quot;LegalEntity\&quot; domain.             Only identifier types stated will be used to look up relevant entities in relations. If not applicable, provide an empty array. | [optional] 

### Return type

[**ResourceListOfRelation**](ResourceListOfRelation.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The relations for the specific portfolio group. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_portfolio_group_relationships**
> ResourceListOfRelationship get_portfolio_group_relationships(scope, code, effective_at=effective_at, as_at=as_at, filter=filter, identifier_types=identifier_types)

[EARLY ACCESS] GetPortfolioGroupRelationships: Get Relationships for Portfolio Group

Get relationships for the specified Portfolio Group

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    PortfolioGroupsApi
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
    api_instance = api_client_factory.build(PortfolioGroupsApi)
    scope = 'scope_example' # str | The scope of the portfolio group.
    code = 'code_example' # str | The code of the portfolio group. Together with the scope this uniquely identifies             the portfolio group.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve relationship. Defaults to the current LUSID system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve relationships. Defaults to return the latest LUSID AsAt time if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter relationships. Users should provide null or empty string for this field until further notice. (optional)
    identifier_types = ['identifier_types_example'] # List[str] | Identifier types (as property keys) used for referencing Persons or Legal Entities.             These can be specified from the 'Person' or 'LegalEntity' domains and have the format {domain}/{scope}/{code}, for example             'Person/CompanyDetails/Role'. An Empty array may be used to return all related Entities. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_portfolio_group_relationships(scope, code, effective_at=effective_at, as_at=as_at, filter=filter, identifier_types=identifier_types, opts=opts)

        # [EARLY ACCESS] GetPortfolioGroupRelationships: Get Relationships for Portfolio Group
        api_response = api_instance.get_portfolio_group_relationships(scope, code, effective_at=effective_at, as_at=as_at, filter=filter, identifier_types=identifier_types)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling PortfolioGroupsApi->get_portfolio_group_relationships: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio group. | 
 **code** | **str**| The code of the portfolio group. Together with the scope this uniquely identifies             the portfolio group. | 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve relationship. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve relationships. Defaults to return the latest LUSID AsAt time if not specified. | [optional] 
 **filter** | **str**| Expression to filter relationships. Users should provide null or empty string for this field until further notice. | [optional] 
 **identifier_types** | [**List[str]**](str.md)| Identifier types (as property keys) used for referencing Persons or Legal Entities.             These can be specified from the &#39;Person&#39; or &#39;LegalEntity&#39; domains and have the format {domain}/{scope}/{code}, for example             &#39;Person/CompanyDetails/Role&#39;. An Empty array may be used to return all related Entities. | [optional] 

### Return type

[**ResourceListOfRelationship**](ResourceListOfRelationship.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The relationships for the specific portfolio group. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_transactions_for_portfolio_group**
> VersionedResourceListOfTransaction get_transactions_for_portfolio_group(scope, code, from_transaction_date=from_transaction_date, to_transaction_date=to_transaction_date, as_at=as_at, filter=filter, property_keys=property_keys, limit=limit, page=page, show_cancelled_transactions=show_cancelled_transactions, sort_by=sort_by)

GetTransactionsForPortfolioGroup: Get transactions for transaction portfolios in a portfolio group

Get transactions for transaction portfolios in a portfolio group over a given interval of effective time.              When the specified portfolio in a portfolio group is a derived transaction portfolio, the returned set of transactions is the union set of all transactions of the parent (and any grandparents etc.) and the specified derived transaction portfolio itself.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    PortfolioGroupsApi
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
    api_instance = api_client_factory.build(PortfolioGroupsApi)
    scope = 'scope_example' # str | The scope of the portfolio group.
    code = 'code_example' # str | The code of the portfolio group. Together with the scope this uniquely identifies              the portfolio group.
    from_transaction_date = 'from_transaction_date_example' # str | The lower bound effective datetime or cut label (inclusive) from which to retrieve the transactions.              There is no lower bound if this is not specified. (optional)
    to_transaction_date = 'to_transaction_date_example' # str | The upper bound effective datetime or cut label (inclusive) from which to retrieve transactions.              There is no upper bound if this is not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the transactions. Defaults to return the latest version              of each transaction if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the result set.              For example, to filter on the Transaction Type, use \"type eq 'Buy'\"              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the \"Instrument\", \"Transaction\", \"LegalEntity\" or \"CustodianAccount\" domain to decorate onto              the transactions. These take the format {domain}/{scope}/{code} e.g. \"Instrument/system/Name\" or              \"Transaction/strategy/quantsignal\". (optional)
    limit = 56 # int | When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing transactions from a previous call to GetTransactions. (optional)
    show_cancelled_transactions = True # bool | Option to specify whether or not to include cancelled transactions,              including previous versions of transactions which have since been amended.              Defaults to False if not specified. (optional)
    sort_by = ['sort_by_example'] # List[str] | A list of field names or properties to sort by, each suffixed by \" ASC\" or \" DESC\". (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_transactions_for_portfolio_group(scope, code, from_transaction_date=from_transaction_date, to_transaction_date=to_transaction_date, as_at=as_at, filter=filter, property_keys=property_keys, limit=limit, page=page, show_cancelled_transactions=show_cancelled_transactions, sort_by=sort_by, opts=opts)

        # GetTransactionsForPortfolioGroup: Get transactions for transaction portfolios in a portfolio group
        api_response = api_instance.get_transactions_for_portfolio_group(scope, code, from_transaction_date=from_transaction_date, to_transaction_date=to_transaction_date, as_at=as_at, filter=filter, property_keys=property_keys, limit=limit, page=page, show_cancelled_transactions=show_cancelled_transactions, sort_by=sort_by)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling PortfolioGroupsApi->get_transactions_for_portfolio_group: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio group. | 
 **code** | **str**| The code of the portfolio group. Together with the scope this uniquely identifies              the portfolio group. | 
 **from_transaction_date** | **str**| The lower bound effective datetime or cut label (inclusive) from which to retrieve the transactions.              There is no lower bound if this is not specified. | [optional] 
 **to_transaction_date** | **str**| The upper bound effective datetime or cut label (inclusive) from which to retrieve transactions.              There is no upper bound if this is not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the transactions. Defaults to return the latest version              of each transaction if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set.              For example, to filter on the Transaction Type, use \&quot;type eq &#39;Buy&#39;\&quot;              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the \&quot;Instrument\&quot;, \&quot;Transaction\&quot;, \&quot;LegalEntity\&quot; or \&quot;CustodianAccount\&quot; domain to decorate onto              the transactions. These take the format {domain}/{scope}/{code} e.g. \&quot;Instrument/system/Name\&quot; or              \&quot;Transaction/strategy/quantsignal\&quot;. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing transactions from a previous call to GetTransactions. | [optional] 
 **show_cancelled_transactions** | **bool**| Option to specify whether or not to include cancelled transactions,              including previous versions of transactions which have since been amended.              Defaults to False if not specified. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 

### Return type

[**VersionedResourceListOfTransaction**](VersionedResourceListOfTransaction.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested transactions from transaction portfolios in the specified portfolio group |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_portfolio_groups**
> PagedResourceListOfPortfolioGroup list_portfolio_groups(scope, effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, related_entity_property_keys=related_entity_property_keys, relationship_definition_ids=relationship_definition_ids)

ListPortfolioGroups: List portfolio groups

List all the portfolio groups in a single scope.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    PortfolioGroupsApi
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
    api_instance = api_client_factory.build(PortfolioGroupsApi)
    scope = 'scope_example' # str | The scope to list the portfolio groups in.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to list the portfolio groups. Defaults to the current LUSID system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the portfolio groups. Defaults to return the latest version of each portfolio group if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing portfolio groups from a previous call to list portfolio groups. This value is returned from the previous call. If a pagination token is provided the filter, effectiveAt, sortBy and asAt fields must not have changed since the original request. (optional)
    limit = 56 # int | When paginating, limit the number of returned results to this many. Defaults to no limit if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the result set.             For example, to filter on the Display Name, use \"displayName eq 'string'\"             Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)
    sort_by = ['sort_by_example'] # List[str] | A list of field names to sort by, each suffixed by \" ASC\" or \" DESC\" (optional)
    related_entity_property_keys = ['related_entity_property_keys_example'] # List[str] | A list of property keys from any domain that supports relationships             to decorate onto related entities. These must take the format {domain}/{scope}/{code}, for example 'Portfolio/Manager/Id'. (optional)
    relationship_definition_ids = ['relationship_definition_ids_example'] # List[str] | A list of relationship definitions that are used to decorate related entities             onto the portfolio groups in the response. These must take the form {relationshipDefinitionScope}/{relationshipDefinitionCode}. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_portfolio_groups(scope, effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, related_entity_property_keys=related_entity_property_keys, relationship_definition_ids=relationship_definition_ids, opts=opts)

        # ListPortfolioGroups: List portfolio groups
        api_response = api_instance.list_portfolio_groups(scope, effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, related_entity_property_keys=related_entity_property_keys, relationship_definition_ids=relationship_definition_ids)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling PortfolioGroupsApi->list_portfolio_groups: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope to list the portfolio groups in. | 
 **effective_at** | **str**| The effective datetime or cut label at which to list the portfolio groups. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the portfolio groups. Defaults to return the latest version of each portfolio group if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing portfolio groups from a previous call to list portfolio groups. This value is returned from the previous call. If a pagination token is provided the filter, effectiveAt, sortBy and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to no limit if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set.             For example, to filter on the Display Name, use \&quot;displayName eq &#39;string&#39;\&quot;             Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot; | [optional] 
 **related_entity_property_keys** | [**List[str]**](str.md)| A list of property keys from any domain that supports relationships             to decorate onto related entities. These must take the format {domain}/{scope}/{code}, for example &#39;Portfolio/Manager/Id&#39;. | [optional] 
 **relationship_definition_ids** | [**List[str]**](str.md)| A list of relationship definitions that are used to decorate related entities             onto the portfolio groups in the response. These must take the form {relationshipDefinitionScope}/{relationshipDefinitionCode}. | [optional] 

### Return type

[**PagedResourceListOfPortfolioGroup**](PagedResourceListOfPortfolioGroup.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The portfolio groups in the specified scope |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **patch_portfolio_group_access_metadata**
> Dict[str, List[AccessMetadataValue]] patch_portfolio_group_access_metadata(scope, code, access_metadata_operation, effective_at=effective_at, effective_until=effective_until)

[EARLY ACCESS] PatchPortfolioGroupAccessMetadata: Patch Access Metadata rules for a Portfolio Group.

Patch Portfolio Group Access Metadata Rules in a single scope. The behaviour is defined by the JSON Patch specification.              Currently only 'add' is a supported operation on the patch document.  Currently only valid metadata keys are supported paths on the patch document.              The response will return any affected Portfolio Group Access Metadata rules or a failure message if unsuccessful.              It is important to always check to verify success (or failure).              Multiple rules for a metadataKey can exist with different effective at dates, when resources are accessed the rule that is active for the current time will be fetched.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    PortfolioGroupsApi
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
    api_instance = api_client_factory.build(PortfolioGroupsApi)
    scope = 'scope_example' # str | The scope of the Portfolio Group
    code = 'code_example' # str | The Portfolio Group code
    access_metadata_operation = [{"value":[{"value":"SilverLicence","provider":"TestDataProvider"}],"path":"/exampleMetadataKey","op":"add"}] # List[AccessMetadataOperation] | The Json patch document
    effective_at = 'effective_at_example' # str | The date this rule will be effective from (optional)
    effective_until = '2013-10-20T19:20:30+01:00' # datetime | The effective date until which the Access Metadata is valid. If not supplied this will be valid indefinitely, or until the next 'effectiveAt' date of the Access Metadata (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.patch_portfolio_group_access_metadata(scope, code, access_metadata_operation, effective_at=effective_at, effective_until=effective_until, opts=opts)

        # [EARLY ACCESS] PatchPortfolioGroupAccessMetadata: Patch Access Metadata rules for a Portfolio Group.
        api_response = api_instance.patch_portfolio_group_access_metadata(scope, code, access_metadata_operation, effective_at=effective_at, effective_until=effective_until)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling PortfolioGroupsApi->patch_portfolio_group_access_metadata: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Portfolio Group | 
 **code** | **str**| The Portfolio Group code | 
 **access_metadata_operation** | [**List[AccessMetadataOperation]**](AccessMetadataOperation.md)| The Json patch document | 
 **effective_at** | **str**| The date this rule will be effective from | [optional] 
 **effective_until** | **datetime**| The effective date until which the Access Metadata is valid. If not supplied this will be valid indefinitely, or until the next &#39;effectiveAt&#39; date of the Access Metadata | [optional] 

### Return type

**Dict[str, List[AccessMetadataValue]]**

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully patched items. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **update_portfolio_group**
> PortfolioGroup update_portfolio_group(scope, code, effective_at=effective_at, update_portfolio_group_request=update_portfolio_group_request)

[EARLY ACCESS] UpdatePortfolioGroup: Update portfolio group

Update the definition of a single portfolio group. Not all elements within a portfolio group definition are modifiable due to the potential implications for data already stored against the portfolio group.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    PortfolioGroupsApi
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
    api_instance = api_client_factory.build(PortfolioGroupsApi)
    scope = 'scope_example' # str | The scope of the portfolio group to update the definition for.
    code = 'code_example' # str | The code of the portfolio group to update the definition for. Together with the scope this uniquely identifies the portfolio group.
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to update the definition. (optional)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # update_portfolio_group_request = UpdatePortfolioGroupRequest.from_json("")
    # update_portfolio_group_request = UpdatePortfolioGroupRequest.from_dict({})
    update_portfolio_group_request = UpdatePortfolioGroupRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.update_portfolio_group(scope, code, effective_at=effective_at, update_portfolio_group_request=update_portfolio_group_request, opts=opts)

        # [EARLY ACCESS] UpdatePortfolioGroup: Update portfolio group
        api_response = api_instance.update_portfolio_group(scope, code, effective_at=effective_at, update_portfolio_group_request=update_portfolio_group_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling PortfolioGroupsApi->update_portfolio_group: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio group to update the definition for. | 
 **code** | **str**| The code of the portfolio group to update the definition for. Together with the scope this uniquely identifies the portfolio group. | 
 **effective_at** | **str**| The effective datetime or cut label at which to update the definition. | [optional] 
 **update_portfolio_group_request** | [**UpdatePortfolioGroupRequest**](UpdatePortfolioGroupRequest.md)| The updated portfolio group definition. | [optional] 

### Return type

[**PortfolioGroup**](PortfolioGroup.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated definition of the portfolio group |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **upsert_group_properties**
> PortfolioGroupProperties upsert_group_properties(scope, code, request_body=request_body)

[EARLY ACCESS] UpsertGroupProperties: Upsert group properties

Update or insert one or more properties onto a single group. A property will be updated if it already exists and inserted if it does not. All properties must be of the domain 'PortfolioGroup'.              Upserting a property that exists for a group, with a null value, will delete the instance of the property for that group.              Properties have an <i>effectiveFrom</i> datetime for which the property is valid, and an <i>effectiveUntil</i> datetime until which the property is valid. Not supplying an <i>effectiveUntil</i> datetime results in the property being valid indefinitely, or until the next <i>effectiveFrom</i> datetime of the property.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    PortfolioGroupsApi
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
    api_instance = api_client_factory.build(PortfolioGroupsApi)
    scope = 'scope_example' # str | The scope of the group to update or insert the properties onto.
    code = 'code_example' # str | The code of the group to update or insert the properties onto. Together with the scope this uniquely identifies the group.
    request_body = {"PortfolioGroup/MyScope/FundManagerName":{"key":"PortfolioGroup/MyScope/FundManagerName","value":{"labelValue":"Smith"},"effectiveFrom":"2018-03-05T00:00:00.0000000+00:00"},"PortfolioGroup/MyScope/SomeProperty":{"key":"PortfolioGroup/MyScope/SomeProperty","value":{"labelValue":"SomeValue"},"effectiveFrom":"2016-01-01T00:00:00.0000000+00:00"},"PortfolioGroup/MyScope/AnotherProperty":{"key":"PortfolioGroup/MyScope/AnotherProperty","value":{"labelValue":"AnotherValue"},"effectiveFrom":"2018-03-05T00:00:00.0000000+00:00","effectiveUntil":"2020-01-01T00:00:00.0000000+00:00"},"PortfolioGroup/MyScope/ReBalanceInterval":{"key":"PortfolioGroup/MyScope/ReBalanceInterval","value":{"metricValue":{"value":30,"unit":"Days"}}}} # Dict[str, ModelProperty] | The properties to be updated or inserted onto the group. Each property in              the request must be keyed by its unique property key. This has the format {domain}/{scope}/{code} e.g. \"PortfolioGroup/Manager/Id\". (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.upsert_group_properties(scope, code, request_body=request_body, opts=opts)

        # [EARLY ACCESS] UpsertGroupProperties: Upsert group properties
        api_response = api_instance.upsert_group_properties(scope, code, request_body=request_body)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling PortfolioGroupsApi->upsert_group_properties: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the group to update or insert the properties onto. | 
 **code** | **str**| The code of the group to update or insert the properties onto. Together with the scope this uniquely identifies the group. | 
 **request_body** | [**Dict[str, ModelProperty]**](ModelProperty.md)| The properties to be updated or inserted onto the group. Each property in              the request must be keyed by its unique property key. This has the format {domain}/{scope}/{code} e.g. \&quot;PortfolioGroup/Manager/Id\&quot;. | [optional] 

### Return type

[**PortfolioGroupProperties**](PortfolioGroupProperties.md)

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

# **upsert_portfolio_group_access_metadata**
> ResourceListOfAccessMetadataValueOf upsert_portfolio_group_access_metadata(scope, code, metadata_key, upsert_portfolio_group_access_metadata_request, effective_at=effective_at, effective_until=effective_until)

UpsertPortfolioGroupAccessMetadata: Upsert a Portfolio Group Access Metadata entry associated with a specific metadataKey. This creates or updates the data in LUSID.

Update or insert one Portfolio Group Access Metadata Entry in a single scope. An item will be updated if it already exists and inserted if it does not.              The response will return the successfully updated or inserted Portfolio Group Access Metadata rule or failure message if unsuccessful.              It is important to always check to verify success (or failure).              Multiple rules for a metadataKey can exist with different effective at dates, when resources are accessed the rule that is active for the current time will be fetched.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    PortfolioGroupsApi
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
    api_instance = api_client_factory.build(PortfolioGroupsApi)
    scope = 'scope_example' # str | The scope of the Portfolio Group
    code = 'code_example' # str | The Portfolio Group code
    metadata_key = 'metadata_key_example' # str | Key of the access metadata entry to upsert

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # upsert_portfolio_group_access_metadata_request = UpsertPortfolioGroupAccessMetadataRequest.from_json("")
    # upsert_portfolio_group_access_metadata_request = UpsertPortfolioGroupAccessMetadataRequest.from_dict({})
    upsert_portfolio_group_access_metadata_request = UpsertPortfolioGroupAccessMetadataRequest()
    effective_at = 'effective_at_example' # str | The date this rule will be effective from (optional)
    effective_until = '2013-10-20T19:20:30+01:00' # datetime | The effective date until which the Access Metadata is valid. If not supplied this will be valid indefinitely, or until the next 'effectiveAt' date of the Access Metadata (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.upsert_portfolio_group_access_metadata(scope, code, metadata_key, upsert_portfolio_group_access_metadata_request, effective_at=effective_at, effective_until=effective_until, opts=opts)

        # UpsertPortfolioGroupAccessMetadata: Upsert a Portfolio Group Access Metadata entry associated with a specific metadataKey. This creates or updates the data in LUSID.
        api_response = api_instance.upsert_portfolio_group_access_metadata(scope, code, metadata_key, upsert_portfolio_group_access_metadata_request, effective_at=effective_at, effective_until=effective_until)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling PortfolioGroupsApi->upsert_portfolio_group_access_metadata: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Portfolio Group | 
 **code** | **str**| The Portfolio Group code | 
 **metadata_key** | **str**| Key of the access metadata entry to upsert | 
 **upsert_portfolio_group_access_metadata_request** | [**UpsertPortfolioGroupAccessMetadataRequest**](UpsertPortfolioGroupAccessMetadataRequest.md)| The Portfolio Group Access Metadata rule to upsert | 
 **effective_at** | **str**| The date this rule will be effective from | [optional] 
 **effective_until** | **datetime**| The effective date until which the Access Metadata is valid. If not supplied this will be valid indefinitely, or until the next &#39;effectiveAt&#39; date of the Access Metadata | [optional] 

### Return type

[**ResourceListOfAccessMetadataValueOf**](ResourceListOfAccessMetadataValueOf.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully updated or inserted item or any failure. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

