# lusid.InvestmentAccountsApi

All URIs are relative to *https://fbn-prd.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_investment_account**](InvestmentAccountsApi.md#get_investment_account) | **GET** /api/investmentaccounts/{identifierType}/{identifierValue} | [EXPERIMENTAL] GetInvestmentAccount: Get Investment Account
[**list_all_investment_accounts**](InvestmentAccountsApi.md#list_all_investment_accounts) | **GET** /api/investmentaccounts | [EXPERIMENTAL] ListAllInvestmentAccounts: List Investment Accounts
[**upsert_investment_accounts**](InvestmentAccountsApi.md#upsert_investment_accounts) | **POST** /api/investmentaccounts/$batchUpsert | [EXPERIMENTAL] UpsertInvestmentAccounts: Upsert Investment Accounts


# **get_investment_account**
> InvestmentAccount get_investment_account(identifier_type, identifier_value, scope, identifier_scope, property_keys=property_keys, effective_at=effective_at, as_at=as_at, relationship_definition_ids=relationship_definition_ids)

[EXPERIMENTAL] GetInvestmentAccount: Get Investment Account

Retrieve the definition of an investment account.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    InvestmentAccountsApi
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
    api_instance = api_client_factory.build(InvestmentAccountsApi)
    identifier_type = 'identifier_type_example' # str | Code of the investment account identifier type.
    identifier_value = 'identifier_value_example' # str | Code of the investment account under specified identifier type's scope and code.
    scope = 'scope_example' # str | The scope of the investment account entity.
    identifier_scope = 'identifier_scope_example' # str | Scope of the investment account identifier type.
    property_keys = ['property_keys_example'] # List[str] | A list of property keys or identifier types (as property keys) from the \"InvestmentAccount\" domain             to include for found investment account, or from any domain that supports relationships to decorate onto related entities.             These take the format {domain}/{scope}/{code} e.g. \"InvestmentAccount/ContactDetails/Address\". (optional)
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve the investment account. Defaults to the current LUSID system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the investment account. Defaults to return the latest version of the investment account if not specified. (optional)
    relationship_definition_ids = ['relationship_definition_ids_example'] # List[str] | A list of relationship definitions that are used to decorate related entities             onto the investment account in the response. These must take the form {relationshipDefinitionScope}/{relationshipDefinitionCode}. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_investment_account(identifier_type, identifier_value, scope, identifier_scope, property_keys=property_keys, effective_at=effective_at, as_at=as_at, relationship_definition_ids=relationship_definition_ids, opts=opts)

        # [EXPERIMENTAL] GetInvestmentAccount: Get Investment Account
        api_response = api_instance.get_investment_account(identifier_type, identifier_value, scope, identifier_scope, property_keys=property_keys, effective_at=effective_at, as_at=as_at, relationship_definition_ids=relationship_definition_ids)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling InvestmentAccountsApi->get_investment_account: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier_type** | **str**| Code of the investment account identifier type. | 
 **identifier_value** | **str**| Code of the investment account under specified identifier type&#39;s scope and code. | 
 **scope** | **str**| The scope of the investment account entity. | 
 **identifier_scope** | **str**| Scope of the investment account identifier type. | 
 **property_keys** | [**List[str]**](str.md)| A list of property keys or identifier types (as property keys) from the \&quot;InvestmentAccount\&quot; domain             to include for found investment account, or from any domain that supports relationships to decorate onto related entities.             These take the format {domain}/{scope}/{code} e.g. \&quot;InvestmentAccount/ContactDetails/Address\&quot;. | [optional] 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the investment account. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the investment account. Defaults to return the latest version of the investment account if not specified. | [optional] 
 **relationship_definition_ids** | [**List[str]**](str.md)| A list of relationship definitions that are used to decorate related entities             onto the investment account in the response. These must take the form {relationshipDefinitionScope}/{relationshipDefinitionCode}. | [optional] 

### Return type

[**InvestmentAccount**](InvestmentAccount.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested investment account |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_all_investment_accounts**
> ResourceListOfInvestmentAccount list_all_investment_accounts(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys, relationship_definition_ids=relationship_definition_ids)

[EXPERIMENTAL] ListAllInvestmentAccounts: List Investment Accounts

List all investment accounts which the user is entitled to see.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    InvestmentAccountsApi
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
    api_instance = api_client_factory.build(InvestmentAccountsApi)
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to list the investment accounts. Defaults to the current LUSID             system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the investment accounts. Defaults to return the latest version             of each investment accounts if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing investment accounts from a previous call to list investment accounts. This value is returned from the previous call. If a pagination token is provided the filter, effectiveAt, sortBy and asAt fields must not have changed since the original request. (optional)
    limit = 56 # int | When paginating, limit the number of returned results to this many. Defaults to 5000 if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the result set.              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)
    sort_by = ['sort_by_example'] # List[str] | A list of field names or properties to sort by, each suffixed by \" ASC\" or \" DESC\". (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys or identifier types (as property keys) from the \"InvestmentAccount\" domain             to include for each investment account, or from any domain that supports relationships to decorate onto related entities.             These take the format {domain}/{scope}/{code} e.g. \"InvestmentAccount/ContactDetails/Address\". (optional)
    relationship_definition_ids = ['relationship_definition_ids_example'] # List[str] | A list of relationship definitions that are used to decorate related entities             onto each investment account in the response. These must take the form {relationshipDefinitionScope}/{relationshipDefinitionCode}. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_all_investment_accounts(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys, relationship_definition_ids=relationship_definition_ids, opts=opts)

        # [EXPERIMENTAL] ListAllInvestmentAccounts: List Investment Accounts
        api_response = api_instance.list_all_investment_accounts(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys, relationship_definition_ids=relationship_definition_ids)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling InvestmentAccountsApi->list_all_investment_accounts: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **effective_at** | **str**| The effective datetime or cut label at which to list the investment accounts. Defaults to the current LUSID             system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the investment accounts. Defaults to return the latest version             of each investment accounts if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing investment accounts from a previous call to list investment accounts. This value is returned from the previous call. If a pagination token is provided the filter, effectiveAt, sortBy and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 5000 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set.              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys or identifier types (as property keys) from the \&quot;InvestmentAccount\&quot; domain             to include for each investment account, or from any domain that supports relationships to decorate onto related entities.             These take the format {domain}/{scope}/{code} e.g. \&quot;InvestmentAccount/ContactDetails/Address\&quot;. | [optional] 
 **relationship_definition_ids** | [**List[str]**](str.md)| A list of relationship definitions that are used to decorate related entities             onto each investment account in the response. These must take the form {relationshipDefinitionScope}/{relationshipDefinitionCode}. | [optional] 

### Return type

[**ResourceListOfInvestmentAccount**](ResourceListOfInvestmentAccount.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All existing Investment Accounts |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **upsert_investment_accounts**
> UpsertInvestmentAccountsResponse upsert_investment_accounts(success_mode, request_body)

[EXPERIMENTAL] UpsertInvestmentAccounts: Upsert Investment Accounts

Creates or updates a collection of Investment Accounts

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    InvestmentAccountsApi
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
    api_instance = api_client_factory.build(InvestmentAccountsApi)
    success_mode = 'success_mode_example' # str | Whether the batch request should fail Atomically or in a Partial fashion - Allowed Values: Atomic, Partial
    request_body = {"firstExampleRequest":{"scope":"InvestmentAccount1Scope","identifiers":{"InvestmentAccount/ExternalIdentifier/ExternalIAId":{"key":"InvestmentAccount/ExternalIdentifier/ExternalIAId","value":{"labelValue":"IA_12345678"}},"InvestmentAccount/InternalIdentifier/InternalIAId":{"key":"InvestmentAccount/InternalIdentifier/InternalIAId","value":{"labelValue":"Internal_XHSP2038"}}},"displayName":"InvestmentAccount1DisplayName","description":"InvestmentAccount1Description","accountType":"Personal","accountHolders":[{"key":"AccountHolder1","identifiers":{"InvestorRecord/ExternalIdentifier/ExternalIRId":{"key":"InvestorRecord/ExternalIdentifier/ExternalIRId","value":{"labelValue":"IR_12345678"}},"InvestorRecord/InternalIdentifier/InternalIRId":{"key":"InvestorRecord/InternalIdentifier/InternalIRId","value":{"labelValue":"Internal_XHSP2038"}}}}],"investmentPortfolios":[],"properties":{"InvestmentAccount/Details/Name":{"key":"InvestmentAccount/Details/Name","value":{"labelValue":"John Doe"}},"InvestmentAccount/Details/Country":{"key":"InvestmentAccount/Details/Country","value":{"labelValue":"United Kingdom"},"effectiveFrom":"2016-01-01T00:00:00.0000000+00:00"}}},"secondExampleRequest":{"scope":"InvestmentAccount2Scope","identifiers":{"InvestmentAccount/ExternalIdentifier/ExternalIAId":{"key":"InvestmentAccount/ExternalIdentifier/ExternalIAId","value":{"labelValue":"IR_22345678"}},"InvestmentAccount/InternalIdentifier/InternalIAId":{"key":"InvestmentAccount/InternalIdentifier/InternalIAId","value":{"labelValue":"Internal_XHSP2039"}}},"displayName":"InvestmentAccount2DisplayName","description":"InvestmentAccount2Description","accountType":"JointMixed","accountHolders":[{"key":"AccountHolder1","identifiers":{"InvestorRecord/ExternalIdentifier/ExternalIRId":{"key":"InvestorRecord/ExternalIdentifier/ExternalIRId","value":{"labelValue":"IR_12345678"}},"InvestorRecord/InternalIdentifier/InternalIRId":{"key":"InvestorRecord/InternalIdentifier/InternalIRId","value":{"labelValue":"Internal_XHSP2038"}}}}],"investmentPortfolios":[],"properties":{"InvestmentAccount/Details/Name":{"key":"InvestmentAccount/Details/Name","value":{"labelValue":"Jane Doe"}},"InvestmentAccount/Details/Country":{"key":"InvestmentAccount/Details/Country","value":{"labelValue":"Germany"},"effectiveFrom":"2016-01-01T00:00:00.0000000+00:00"}}}} # Dict[str, UpsertInvestmentAccountRequest] | A collection of requests to create or update Investment Accounts.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.upsert_investment_accounts(success_mode, request_body, opts=opts)

        # [EXPERIMENTAL] UpsertInvestmentAccounts: Upsert Investment Accounts
        api_response = api_instance.upsert_investment_accounts(success_mode, request_body)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling InvestmentAccountsApi->upsert_investment_accounts: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **success_mode** | **str**| Whether the batch request should fail Atomically or in a Partial fashion - Allowed Values: Atomic, Partial | 
 **request_body** | [**Dict[str, UpsertInvestmentAccountRequest]**](UpsertInvestmentAccountRequest.md)| A collection of requests to create or update Investment Accounts. | 

### Return type

[**UpsertInvestmentAccountsResponse**](UpsertInvestmentAccountsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The successfully created or updated Investment Accounts along with any failures |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

