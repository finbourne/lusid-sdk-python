# lusid.InvestmentAccountsApi

All URIs are relative to *https://fbn-prd.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_investment_account**](InvestmentAccountsApi.md#delete_investment_account) | **DELETE** /api/investmentaccounts/{identifierType}/{identifierValue} | [EXPERIMENTAL] DeleteInvestmentAccount: Delete Investment Account
[**delete_investment_account_access_metadata**](InvestmentAccountsApi.md#delete_investment_account_access_metadata) | **DELETE** /api/investmentaccounts/{identifierType}/{identifierValue}/metadata/{metadataKey} | [EXPERIMENTAL] DeleteInvestmentAccountAccessMetadata: Delete an Investment Account Access Metadata entry.
[**get_all_investment_account_access_metadata**](InvestmentAccountsApi.md#get_all_investment_account_access_metadata) | **GET** /api/investmentaccounts/{identifierType}/{identifierValue}/metadata | [EXPERIMENTAL] GetAllInvestmentAccountAccessMetadata: Get Access Metadata rules for an Investment Account.
[**get_investment_account**](InvestmentAccountsApi.md#get_investment_account) | **GET** /api/investmentaccounts/{identifierType}/{identifierValue} | [EXPERIMENTAL] GetInvestmentAccount: Get Investment Account
[**get_investment_account_relationships**](InvestmentAccountsApi.md#get_investment_account_relationships) | **GET** /api/investmentaccounts/{identifierType}/{identifierValue}/relationships | [EARLY ACCESS] GetInvestmentAccountRelationships: Get Investment Account relationships
[**list_all_investment_accounts**](InvestmentAccountsApi.md#list_all_investment_accounts) | **GET** /api/investmentaccounts | [EXPERIMENTAL] ListAllInvestmentAccounts: List Investment Accounts
[**patch_investment_account_access_metadata**](InvestmentAccountsApi.md#patch_investment_account_access_metadata) | **PATCH** /api/investmentaccounts/{identifierType}/{identifierValue}/metadata | [EXPERIMENTAL] PatchInvestmentAccountAccessMetadata: Patch Access Metadata rules for an Investment Account.
[**upsert_investment_accounts**](InvestmentAccountsApi.md#upsert_investment_accounts) | **POST** /api/investmentaccounts/$batchUpsert | [EXPERIMENTAL] UpsertInvestmentAccounts: Upsert Investment Accounts


# **delete_investment_account**
> DeletedEntityResponse delete_investment_account(identifier_type, identifier_value, scope, identifier_scope)

[EXPERIMENTAL] DeleteInvestmentAccount: Delete Investment Account

Delete an investment account. Deletion will be valid from the investment account's creation datetime.  This means that the investment account will no longer exist at any effective datetime from the asAt datetime of deletion.

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

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_investment_account(identifier_type, identifier_value, scope, identifier_scope, opts=opts)

        # [EXPERIMENTAL] DeleteInvestmentAccount: Delete Investment Account
        api_response = api_instance.delete_investment_account(identifier_type, identifier_value, scope, identifier_scope)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling InvestmentAccountsApi->delete_investment_account: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier_type** | **str**| Code of the investment account identifier type. | 
 **identifier_value** | **str**| Code of the investment account under specified identifier type&#39;s scope and code. | 
 **scope** | **str**| The scope of the investment account entity. | 
 **identifier_scope** | **str**| Scope of the investment account identifier type. | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response from deleting investment account. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_investment_account_access_metadata**
> DeletedEntityResponse delete_investment_account_access_metadata(identifier_type, identifier_value, metadata_key, scope, identifier_scope, effective_at=effective_at, effective_until=effective_until)

[EXPERIMENTAL] DeleteInvestmentAccountAccessMetadata: Delete an Investment Account Access Metadata entry.

Deletes the Investment Account Access Metadata entry that exactly matches the provided identifier parts.                It is important to always check to verify success (or failure).

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
    metadata_key = 'metadata_key_example' # str | Key of the metadata entry to delete
    scope = 'scope_example' # str | The scope of the investment account entity.
    identifier_scope = 'identifier_scope_example' # str | Scope of the investment account identifier type.
    effective_at = 'effective_at_example' # str | The effective date to delete at, if this is not supplied, it will delete all data found (optional)
    effective_until = '2013-10-20T19:20:30+01:00' # datetime | The effective date until which the delete is valid. If not supplied this will be valid indefinitely, or until the next 'effectiveAt' date of the Access Metadata (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_investment_account_access_metadata(identifier_type, identifier_value, metadata_key, scope, identifier_scope, effective_at=effective_at, effective_until=effective_until, opts=opts)

        # [EXPERIMENTAL] DeleteInvestmentAccountAccessMetadata: Delete an Investment Account Access Metadata entry.
        api_response = api_instance.delete_investment_account_access_metadata(identifier_type, identifier_value, metadata_key, scope, identifier_scope, effective_at=effective_at, effective_until=effective_until)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling InvestmentAccountsApi->delete_investment_account_access_metadata: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier_type** | **str**| Code of the investment account identifier type. | 
 **identifier_value** | **str**| Code of the investment account under specified identifier type&#39;s scope and code. | 
 **metadata_key** | **str**| Key of the metadata entry to delete | 
 **scope** | **str**| The scope of the investment account entity. | 
 **identifier_scope** | **str**| Scope of the investment account identifier type. | 
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
**200** | The Access Metadata with the given metadataKey has been deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_all_investment_account_access_metadata**
> Dict[str, List[AccessMetadataValue]] get_all_investment_account_access_metadata(identifier_type, identifier_value, scope, identifier_scope, effective_at=effective_at, as_at=as_at)

[EXPERIMENTAL] GetAllInvestmentAccountAccessMetadata: Get Access Metadata rules for an Investment Account.

Pass the Scope and Code of the Investment Account identifier along with the identifier value parameter to retrieve the associated Access Metadata.

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
    effective_at = 'effective_at_example' # str | The effectiveAt datetime at which to retrieve the Access Metadata (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Access Metadata (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_all_investment_account_access_metadata(identifier_type, identifier_value, scope, identifier_scope, effective_at=effective_at, as_at=as_at, opts=opts)

        # [EXPERIMENTAL] GetAllInvestmentAccountAccessMetadata: Get Access Metadata rules for an Investment Account.
        api_response = api_instance.get_all_investment_account_access_metadata(identifier_type, identifier_value, scope, identifier_scope, effective_at=effective_at, as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling InvestmentAccountsApi->get_all_investment_account_access_metadata: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier_type** | **str**| Code of the investment account identifier type. | 
 **identifier_value** | **str**| Code of the investment account under specified identifier type&#39;s scope and code. | 
 **scope** | **str**| The scope of the investment account entity. | 
 **identifier_scope** | **str**| Scope of the investment account identifier type. | 
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
**200** | The access metadata for the Investment Account or any failure. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

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
    property_keys = ['property_keys_example'] # List[str] | A list of property keys or identifier types (as property keys) from the \"InvestmentAccount\" domain              to include for found investment account, or from any domain that supports relationships to decorate onto related entities.              These take the format {domain}/{scope}/{code} e.g. \"InvestmentAccount/ContactDetails/Address\". (optional)
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve the investment account. Defaults to the current LUSID system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the investment account. Defaults to return the latest version of the investment account if not specified. (optional)
    relationship_definition_ids = ['relationship_definition_ids_example'] # List[str] | A list of relationship definitions that are used to decorate related entities              onto the investment account in the response. These must take the form {relationshipDefinitionScope}/{relationshipDefinitionCode}. (optional)

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
 **property_keys** | [**List[str]**](str.md)| A list of property keys or identifier types (as property keys) from the \&quot;InvestmentAccount\&quot; domain              to include for found investment account, or from any domain that supports relationships to decorate onto related entities.              These take the format {domain}/{scope}/{code} e.g. \&quot;InvestmentAccount/ContactDetails/Address\&quot;. | [optional] 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the investment account. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the investment account. Defaults to return the latest version of the investment account if not specified. | [optional] 
 **relationship_definition_ids** | [**List[str]**](str.md)| A list of relationship definitions that are used to decorate related entities              onto the investment account in the response. These must take the form {relationshipDefinitionScope}/{relationshipDefinitionCode}. | [optional] 

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

# **get_investment_account_relationships**
> ResourceListOfRelationship get_investment_account_relationships(identifier_type, identifier_value, scope, identifier_scope, effective_at=effective_at, as_at=as_at, filter=filter, identifier_types=identifier_types)

[EARLY ACCESS] GetInvestmentAccountRelationships: Get Investment Account relationships

Get relationships for a particular Investment Account.

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
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to get relationships. Defaults to the current LUSID system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve relationships. Defaults to return the latest LUSID AsAt time if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter relationships. Users should provide null or empty string for this field until further notice. (optional)
    identifier_types = ['identifier_types_example'] # List[str] | Identifier types (as property keys) used for referencing Persons or Legal Entities.              These can be specified from the 'Person' or 'LegalEntity' domains and have the format {domain}/{scope}/{code}, for example              'Person/CompanyDetails/Role'. An Empty array may be used to return all related Entities. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_investment_account_relationships(identifier_type, identifier_value, scope, identifier_scope, effective_at=effective_at, as_at=as_at, filter=filter, identifier_types=identifier_types, opts=opts)

        # [EARLY ACCESS] GetInvestmentAccountRelationships: Get Investment Account relationships
        api_response = api_instance.get_investment_account_relationships(identifier_type, identifier_value, scope, identifier_scope, effective_at=effective_at, as_at=as_at, filter=filter, identifier_types=identifier_types)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling InvestmentAccountsApi->get_investment_account_relationships: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier_type** | **str**| Code of the investment account identifier type. | 
 **identifier_value** | **str**| Code of the investment account under specified identifier type&#39;s scope and code. | 
 **scope** | **str**| The scope of the investment account entity. | 
 **identifier_scope** | **str**| Scope of the investment account identifier type. | 
 **effective_at** | **str**| The effective datetime or cut label at which to get relationships. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve relationships. Defaults to return the latest LUSID AsAt time if not specified. | [optional] 
 **filter** | **str**| Expression to filter relationships. Users should provide null or empty string for this field until further notice. | [optional] 
 **identifier_types** | [**List[str]**](str.md)| Identifier types (as property keys) used for referencing Persons or Legal Entities.              These can be specified from the &#39;Person&#39; or &#39;LegalEntity&#39; domains and have the format {domain}/{scope}/{code}, for example              &#39;Person/CompanyDetails/Role&#39;. An Empty array may be used to return all related Entities. | [optional] 

### Return type

[**ResourceListOfRelationship**](ResourceListOfRelationship.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The relationships for the specified investment account. |  -  |
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
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to list the investment accounts. Defaults to the current LUSID              system datetime if not specified. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the investment accounts. Defaults to return the latest version              of each investment accounts if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing investment accounts from a previous call to list investment accounts. This  value is returned from the previous call. If a pagination token is provided the filter, effectiveAt, sortBy  and asAt fields must not have changed since the original request. (optional)
    limit = 56 # int | When paginating, limit the number of returned results to this many. Defaults to 5000 if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the result set.               Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)
    sort_by = ['sort_by_example'] # List[str] | A list of field names or properties to sort by, each suffixed by \" ASC\" or \" DESC\". (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys or identifier types (as property keys) from the \"InvestmentAccount\" domain              to include for each investment account, or from any domain that supports relationships to decorate onto related entities.              These take the format {domain}/{scope}/{code} e.g. \"InvestmentAccount/ContactDetails/Address\". (optional)
    relationship_definition_ids = ['relationship_definition_ids_example'] # List[str] | A list of relationship definitions that are used to decorate related entities              onto each investment account in the response. These must take the form {relationshipDefinitionScope}/{relationshipDefinitionCode}. (optional)

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
 **effective_at** | **str**| The effective datetime or cut label at which to list the investment accounts. Defaults to the current LUSID              system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the investment accounts. Defaults to return the latest version              of each investment accounts if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing investment accounts from a previous call to list investment accounts. This  value is returned from the previous call. If a pagination token is provided the filter, effectiveAt, sortBy  and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 5000 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set.               Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys or identifier types (as property keys) from the \&quot;InvestmentAccount\&quot; domain              to include for each investment account, or from any domain that supports relationships to decorate onto related entities.              These take the format {domain}/{scope}/{code} e.g. \&quot;InvestmentAccount/ContactDetails/Address\&quot;. | [optional] 
 **relationship_definition_ids** | [**List[str]**](str.md)| A list of relationship definitions that are used to decorate related entities              onto each investment account in the response. These must take the form {relationshipDefinitionScope}/{relationshipDefinitionCode}. | [optional] 

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

# **patch_investment_account_access_metadata**
> Dict[str, List[AccessMetadataValue]] patch_investment_account_access_metadata(identifier_type, identifier_value, scope, identifier_scope, access_metadata_operation, effective_at=effective_at, effective_until=effective_until)

[EXPERIMENTAL] PatchInvestmentAccountAccessMetadata: Patch Access Metadata rules for an Investment Account.

Patch Investment Account Access Metadata Rules in a single scope.  The behaviour is defined by the JSON Patch specification.                Currently only 'add' is a supported operation on the patch document                Currently only valid metadata keys are supported paths on the patch document                The response will return any affected Investment Account Access Metadata rules or a failure message if unsuccessful.                It is important to always check to verify success (or failure).                Multiple rules for a metadataKey can exist with different effective at dates, when resources are accessed the rule that is active for the current time will be fetched.

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
    access_metadata_operation = [{"value":[{"value":"SilverLicence","provider":"TestDataProvider"}],"path":"/exampleMetadataKey","op":"add"}] # List[AccessMetadataOperation] | The Json Patch document
    effective_at = 'effective_at_example' # str | The effectiveAt datetime at which to upsert the Access Metadata (optional)
    effective_until = '2013-10-20T19:20:30+01:00' # datetime | The effective datetime until which the Access Metadata is valid. If not supplied this will be valid indefinitely, or until the next 'effectiveAt' datetime of the Access Metadata (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.patch_investment_account_access_metadata(identifier_type, identifier_value, scope, identifier_scope, access_metadata_operation, effective_at=effective_at, effective_until=effective_until, opts=opts)

        # [EXPERIMENTAL] PatchInvestmentAccountAccessMetadata: Patch Access Metadata rules for an Investment Account.
        api_response = api_instance.patch_investment_account_access_metadata(identifier_type, identifier_value, scope, identifier_scope, access_metadata_operation, effective_at=effective_at, effective_until=effective_until)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling InvestmentAccountsApi->patch_investment_account_access_metadata: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier_type** | **str**| Code of the investment account identifier type. | 
 **identifier_value** | **str**| Code of the investment account under specified identifier type&#39;s scope and code. | 
 **scope** | **str**| The scope of the investment account entity. | 
 **identifier_scope** | **str**| Scope of the investment account identifier type. | 
 **access_metadata_operation** | [**List[AccessMetadataOperation]**](AccessMetadataOperation.md)| The Json Patch document | 
 **effective_at** | **str**| The effectiveAt datetime at which to upsert the Access Metadata | [optional] 
 **effective_until** | **datetime**| The effective datetime until which the Access Metadata is valid. If not supplied this will be valid indefinitely, or until the next &#39;effectiveAt&#39; datetime of the Access Metadata | [optional] 

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
    request_body = {"firstExampleRequest":{"scope":"InvestmentAccount1Scope","identifiers":{"InvestmentAccount/ExternalIdentifier/ExternalIAId":{"key":"InvestmentAccount/ExternalIdentifier/ExternalIAId","value":{"labelValue":"IA_12345678"}},"InvestmentAccount/InternalIdentifier/InternalIAId":{"key":"InvestmentAccount/InternalIdentifier/InternalIAId","value":{"labelValue":"Internal_XHSP2038"}}},"displayName":"InvestmentAccount1DisplayName","description":"InvestmentAccount1Description","accountType":"Personal","accountHolders":[{"key":"AccountHolder1"}],"investmentPortfolios":[],"properties":{"InvestmentAccount/Details/Name":{"key":"InvestmentAccount/Details/Name","value":{"labelValue":"John Doe"}},"InvestmentAccount/Details/Country":{"key":"InvestmentAccount/Details/Country","value":{"labelValue":"United Kingdom"},"effectiveFrom":"2016-01-01T00:00:00.0000000+00:00"}}},"secondExampleRequest":{"scope":"InvestmentAccount2Scope","identifiers":{"InvestmentAccount/ExternalIdentifier/ExternalIAId":{"key":"InvestmentAccount/ExternalIdentifier/ExternalIAId","value":{"labelValue":"IR_22345678"}},"InvestmentAccount/InternalIdentifier/InternalIAId":{"key":"InvestmentAccount/InternalIdentifier/InternalIAId","value":{"labelValue":"Internal_XHSP2039"}}},"displayName":"InvestmentAccount2DisplayName","description":"InvestmentAccount2Description","accountType":"JointMixed","accountHolders":[{"key":"AccountHolder1"}],"investmentPortfolios":[],"properties":{"InvestmentAccount/Details/Name":{"key":"InvestmentAccount/Details/Name","value":{"labelValue":"Jane Doe"}},"InvestmentAccount/Details/Country":{"key":"InvestmentAccount/Details/Country","value":{"labelValue":"Germany"},"effectiveFrom":"2016-01-01T00:00:00.0000000+00:00"}}}} # Dict[str, UpsertInvestmentAccountRequest] | A collection of requests to create or update Investment Accounts.

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

