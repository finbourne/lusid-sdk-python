# lusid.CounterpartiesApi

All URIs are relative to *https://fbn-prd.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_counterparty_agreement**](CounterpartiesApi.md#delete_counterparty_agreement) | **DELETE** /api/counterparties/counterpartyagreements/{scope}/{code} | [EARLY ACCESS] DeleteCounterpartyAgreement: Delete the Counterparty Agreement of given scope and code
[**delete_credit_support_annex**](CounterpartiesApi.md#delete_credit_support_annex) | **DELETE** /api/counterparties/creditsupportannexes/{scope}/{code} | [EARLY ACCESS] DeleteCreditSupportAnnex: Delete the Credit Support Annex of given scope and code
[**get_counterparty_agreement**](CounterpartiesApi.md#get_counterparty_agreement) | **GET** /api/counterparties/counterpartyagreements/{scope}/{code} | [EARLY ACCESS] GetCounterpartyAgreement: Get Counterparty Agreement
[**get_credit_support_annex**](CounterpartiesApi.md#get_credit_support_annex) | **GET** /api/counterparties/creditsupportannexes/{scope}/{code} | [EARLY ACCESS] GetCreditSupportAnnex: Get Credit Support Annex
[**list_counterparty_agreements**](CounterpartiesApi.md#list_counterparty_agreements) | **GET** /api/counterparties/counterpartyagreements | [EARLY ACCESS] ListCounterpartyAgreements: List the set of Counterparty Agreements
[**list_credit_support_annexes**](CounterpartiesApi.md#list_credit_support_annexes) | **GET** /api/counterparties/creditsupportannexes | [EARLY ACCESS] ListCreditSupportAnnexes: List the set of Credit Support Annexes
[**upsert_counterparty_agreement**](CounterpartiesApi.md#upsert_counterparty_agreement) | **POST** /api/counterparties/counterpartyagreements | [EARLY ACCESS] UpsertCounterpartyAgreement: Upsert Counterparty Agreement
[**upsert_credit_support_annex**](CounterpartiesApi.md#upsert_credit_support_annex) | **POST** /api/counterparties/creditsupportannexes | [EARLY ACCESS] UpsertCreditSupportAnnex: Upsert Credit Support Annex


# **delete_counterparty_agreement**
> AnnulSingleStructuredDataResponse delete_counterparty_agreement(scope, code)

[EARLY ACCESS] DeleteCounterpartyAgreement: Delete the Counterparty Agreement of given scope and code

Delete the specified Counterparty Agreement from a single scope. The response will return either detail of the deleted item, or an explanation (failure) as to why this did not succeed.              It is important to always check for any unsuccessful response.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    CounterpartiesApi
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
    api_instance = api_client_factory.build(CounterpartiesApi)
    scope = 'scope_example' # str | The scope of the Counterparty Agreement to delete.
    code = 'code_example' # str | The Counterparty Agreement to delete.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_counterparty_agreement(scope, code, opts=opts)

        # [EARLY ACCESS] DeleteCounterpartyAgreement: Delete the Counterparty Agreement of given scope and code
        api_response = api_instance.delete_counterparty_agreement(scope, code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling CounterpartiesApi->delete_counterparty_agreement: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Counterparty Agreement to delete. | 
 **code** | **str**| The Counterparty Agreement to delete. | 

### Return type

[**AnnulSingleStructuredDataResponse**](AnnulSingleStructuredDataResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The AsAt of deletion or failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_credit_support_annex**
> AnnulSingleStructuredDataResponse delete_credit_support_annex(scope, code)

[EARLY ACCESS] DeleteCreditSupportAnnex: Delete the Credit Support Annex of given scope and code

Delete the specified Credit Support Annex from a single scope. The response will return either detail of the deleted item, or an explanation (failure) as to why this did not succeed.              It is important to always check for any unsuccessful response.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    CounterpartiesApi
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
    api_instance = api_client_factory.build(CounterpartiesApi)
    scope = 'scope_example' # str | The scope of the Credit Support Annex to delete.
    code = 'code_example' # str | The Credit Support Annex to delete.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_credit_support_annex(scope, code, opts=opts)

        # [EARLY ACCESS] DeleteCreditSupportAnnex: Delete the Credit Support Annex of given scope and code
        api_response = api_instance.delete_credit_support_annex(scope, code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling CounterpartiesApi->delete_credit_support_annex: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Credit Support Annex to delete. | 
 **code** | **str**| The Credit Support Annex to delete. | 

### Return type

[**AnnulSingleStructuredDataResponse**](AnnulSingleStructuredDataResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The AsAt of deletion or failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_counterparty_agreement**
> GetCounterpartyAgreementResponse get_counterparty_agreement(scope, code, as_at=as_at)

[EARLY ACCESS] GetCounterpartyAgreement: Get Counterparty Agreement

Get a Counterparty Agreement from a single scope. The response will return either the Counterparty Agreement that has been stored, or a failure explaining why the request was unsuccessful. It is important to always check for any unsuccessful requests (failures).

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    CounterpartiesApi
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
    api_instance = api_client_factory.build(CounterpartiesApi)
    scope = 'scope_example' # str | The scope of the Counterparty Agreement to retrieve.
    code = 'code_example' # str | The name of the Counterparty Agreement to retrieve the data for.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Counterparty Agreement. Defaults to return the latest version if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_counterparty_agreement(scope, code, as_at=as_at, opts=opts)

        # [EARLY ACCESS] GetCounterpartyAgreement: Get Counterparty Agreement
        api_response = api_instance.get_counterparty_agreement(scope, code, as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling CounterpartiesApi->get_counterparty_agreement: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Counterparty Agreement to retrieve. | 
 **code** | **str**| The name of the Counterparty Agreement to retrieve the data for. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Counterparty Agreement. Defaults to return the latest version if not specified. | [optional] 

### Return type

[**GetCounterpartyAgreementResponse**](GetCounterpartyAgreementResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully retrieved Counterparty Agreement or any failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_credit_support_annex**
> GetCreditSupportAnnexResponse get_credit_support_annex(scope, code, as_at=as_at)

[EARLY ACCESS] GetCreditSupportAnnex: Get Credit Support Annex

Get a Credit Support Annex from a single scope. The response will return either the Credit Support Annex that has been stored, or a failure explaining why the request was unsuccessful. It is important to always check for any unsuccessful requests (failures).

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    CounterpartiesApi
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
    api_instance = api_client_factory.build(CounterpartiesApi)
    scope = 'scope_example' # str | The scope of the Credit Support Annex to retrieve.
    code = 'code_example' # str | The name of the Credit Support Annex to retrieve the data for.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Credit Support Annex . Defaults to return the latest version if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_credit_support_annex(scope, code, as_at=as_at, opts=opts)

        # [EARLY ACCESS] GetCreditSupportAnnex: Get Credit Support Annex
        api_response = api_instance.get_credit_support_annex(scope, code, as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling CounterpartiesApi->get_credit_support_annex: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Credit Support Annex to retrieve. | 
 **code** | **str**| The name of the Credit Support Annex to retrieve the data for. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Credit Support Annex . Defaults to return the latest version if not specified. | [optional] 

### Return type

[**GetCreditSupportAnnexResponse**](GetCreditSupportAnnexResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully retrieved credit support annexes or any failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_counterparty_agreements**
> ResourceListOfGetCounterpartyAgreementResponse list_counterparty_agreements(as_at=as_at)

[EARLY ACCESS] ListCounterpartyAgreements: List the set of Counterparty Agreements

List the set of Counterparty Agreements at the specified AsAt date/time

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    CounterpartiesApi
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
    api_instance = api_client_factory.build(CounterpartiesApi)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the Counterparty Agreements. Defaults to latest if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_counterparty_agreements(as_at=as_at, opts=opts)

        # [EARLY ACCESS] ListCounterpartyAgreements: List the set of Counterparty Agreements
        api_response = api_instance.list_counterparty_agreements(as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling CounterpartiesApi->list_counterparty_agreements: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list the Counterparty Agreements. Defaults to latest if not specified. | [optional] 

### Return type

[**ResourceListOfGetCounterpartyAgreementResponse**](ResourceListOfGetCounterpartyAgreementResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Counterparty Agreements |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_credit_support_annexes**
> ResourceListOfGetCreditSupportAnnexResponse list_credit_support_annexes(as_at=as_at)

[EARLY ACCESS] ListCreditSupportAnnexes: List the set of Credit Support Annexes

List the set of Credit Support Annexes at the specified AsAt date/time

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    CounterpartiesApi
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
    api_instance = api_client_factory.build(CounterpartiesApi)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the Credit Support Annexes. Defaults to latest if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_credit_support_annexes(as_at=as_at, opts=opts)

        # [EARLY ACCESS] ListCreditSupportAnnexes: List the set of Credit Support Annexes
        api_response = api_instance.list_credit_support_annexes(as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling CounterpartiesApi->list_credit_support_annexes: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list the Credit Support Annexes. Defaults to latest if not specified. | [optional] 

### Return type

[**ResourceListOfGetCreditSupportAnnexResponse**](ResourceListOfGetCreditSupportAnnexResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Credit Support Annexes |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **upsert_counterparty_agreement**
> UpsertSingleStructuredDataResponse upsert_counterparty_agreement(upsert_counterparty_agreement_request)

[EARLY ACCESS] UpsertCounterpartyAgreement: Upsert Counterparty Agreement

Update or insert Counterparty Agreement in a single scope. An item will be updated if it already exists and inserted if it does not.              The response will return the successfully updated or inserted Counterparty Agreement or failure message if unsuccessful              It is important to always check to verify success (or failure).

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    CounterpartiesApi
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
    api_instance = api_client_factory.build(CounterpartiesApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # upsert_counterparty_agreement_request = UpsertCounterpartyAgreementRequest.from_json("")
    # upsert_counterparty_agreement_request = UpsertCounterpartyAgreementRequest.from_dict({})
    upsert_counterparty_agreement_request = UpsertCounterpartyAgreementRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.upsert_counterparty_agreement(upsert_counterparty_agreement_request, opts=opts)

        # [EARLY ACCESS] UpsertCounterpartyAgreement: Upsert Counterparty Agreement
        api_response = api_instance.upsert_counterparty_agreement(upsert_counterparty_agreement_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling CounterpartiesApi->upsert_counterparty_agreement: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_counterparty_agreement_request** | [**UpsertCounterpartyAgreementRequest**](UpsertCounterpartyAgreementRequest.md)| The Counterparty Agreement to update or insert | 

### Return type

[**UpsertSingleStructuredDataResponse**](UpsertSingleStructuredDataResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully updated or inserted Counterparty Agreement or any failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **upsert_credit_support_annex**
> UpsertSingleStructuredDataResponse upsert_credit_support_annex(upsert_credit_support_annex_request)

[EARLY ACCESS] UpsertCreditSupportAnnex: Upsert Credit Support Annex

Update or insert Credit Support Annex in a single scope. An item will be updated if it already exists and inserted if it does not.              The response will return the successfully updated or inserted Credit Support Annex or failure message if unsuccessful              It is important to always check to verify success (or failure).

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    CounterpartiesApi
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
    api_instance = api_client_factory.build(CounterpartiesApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # upsert_credit_support_annex_request = UpsertCreditSupportAnnexRequest.from_json("")
    # upsert_credit_support_annex_request = UpsertCreditSupportAnnexRequest.from_dict({})
    upsert_credit_support_annex_request = UpsertCreditSupportAnnexRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.upsert_credit_support_annex(upsert_credit_support_annex_request, opts=opts)

        # [EARLY ACCESS] UpsertCreditSupportAnnex: Upsert Credit Support Annex
        api_response = api_instance.upsert_credit_support_annex(upsert_credit_support_annex_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling CounterpartiesApi->upsert_credit_support_annex: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_credit_support_annex_request** | [**UpsertCreditSupportAnnexRequest**](UpsertCreditSupportAnnexRequest.md)| The Credit Support Annex to update or insert | 

### Return type

[**UpsertSingleStructuredDataResponse**](UpsertSingleStructuredDataResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully updated or inserted item or any failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

