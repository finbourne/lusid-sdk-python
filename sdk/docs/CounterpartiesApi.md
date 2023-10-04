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

Delete the specified Counterparty Agreement from a single scope.  The response will return either detail of the deleted item, or an explanation (failure) as to why this did not succeed.                It is important to always check for any unsuccessful response.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-prd.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.CounterpartiesApi(api_client)
    scope = 'scope_example' # str | The scope of the Counterparty Agreement to delete.
code = 'code_example' # str | The Counterparty Agreement to delete.

    try:
        # [EARLY ACCESS] DeleteCounterpartyAgreement: Delete the Counterparty Agreement of given scope and code
        api_response = api_instance.delete_counterparty_agreement(scope, code)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CounterpartiesApi->delete_counterparty_agreement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Counterparty Agreement to delete. | 
 **code** | **str**| The Counterparty Agreement to delete. | 

### Return type

[**AnnulSingleStructuredDataResponse**](AnnulSingleStructuredDataResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The AsAt of deletion or failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_credit_support_annex**
> AnnulSingleStructuredDataResponse delete_credit_support_annex(scope, code)

[EARLY ACCESS] DeleteCreditSupportAnnex: Delete the Credit Support Annex of given scope and code

Delete the specified Credit Support Annex from a single scope.  The response will return either detail of the deleted item, or an explanation (failure) as to why this did not succeed.                It is important to always check for any unsuccessful response.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-prd.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.CounterpartiesApi(api_client)
    scope = 'scope_example' # str | The scope of the Credit Support Annex to delete.
code = 'code_example' # str | The Credit Support Annex to delete.

    try:
        # [EARLY ACCESS] DeleteCreditSupportAnnex: Delete the Credit Support Annex of given scope and code
        api_response = api_instance.delete_credit_support_annex(scope, code)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CounterpartiesApi->delete_credit_support_annex: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Credit Support Annex to delete. | 
 **code** | **str**| The Credit Support Annex to delete. | 

### Return type

[**AnnulSingleStructuredDataResponse**](AnnulSingleStructuredDataResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The AsAt of deletion or failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_counterparty_agreement**
> GetCounterpartyAgreementResponse get_counterparty_agreement(scope, code, as_at=as_at)

[EARLY ACCESS] GetCounterpartyAgreement: Get Counterparty Agreement

Get a Counterparty Agreement from a single scope.  The response will return either the Counterparty Agreement that has been stored, or a failure explaining why the request was unsuccessful.  It is important to always check for any unsuccessful requests (failures).

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-prd.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.CounterpartiesApi(api_client)
    scope = 'scope_example' # str | The scope of the Counterparty Agreement to retrieve.
code = 'code_example' # str | The name of the Counterparty Agreement to retrieve the data for.
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Counterparty Agreement. Defaults to return the latest version if not specified. (optional)

    try:
        # [EARLY ACCESS] GetCounterpartyAgreement: Get Counterparty Agreement
        api_response = api_instance.get_counterparty_agreement(scope, code, as_at=as_at)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CounterpartiesApi->get_counterparty_agreement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Counterparty Agreement to retrieve. | 
 **code** | **str**| The name of the Counterparty Agreement to retrieve the data for. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Counterparty Agreement. Defaults to return the latest version if not specified. | [optional] 

### Return type

[**GetCounterpartyAgreementResponse**](GetCounterpartyAgreementResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully retrieved Counterparty Agreement or any failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_credit_support_annex**
> GetCreditSupportAnnexResponse get_credit_support_annex(scope, code, as_at=as_at)

[EARLY ACCESS] GetCreditSupportAnnex: Get Credit Support Annex

Get a Credit Support Annex from a single scope.  The response will return either the Credit Support Annex that has been stored, or a failure explaining why the request was unsuccessful.  It is important to always check for any unsuccessful requests (failures).

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-prd.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.CounterpartiesApi(api_client)
    scope = 'scope_example' # str | The scope of the Credit Support Annex to retrieve.
code = 'code_example' # str | The name of the Credit Support Annex to retrieve the data for.
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Credit Support Annex . Defaults to return the latest version if not specified. (optional)

    try:
        # [EARLY ACCESS] GetCreditSupportAnnex: Get Credit Support Annex
        api_response = api_instance.get_credit_support_annex(scope, code, as_at=as_at)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CounterpartiesApi->get_credit_support_annex: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Credit Support Annex to retrieve. | 
 **code** | **str**| The name of the Credit Support Annex to retrieve the data for. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Credit Support Annex . Defaults to return the latest version if not specified. | [optional] 

### Return type

[**GetCreditSupportAnnexResponse**](GetCreditSupportAnnexResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully retrieved credit support annexes or any failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_counterparty_agreements**
> ResourceListOfGetCounterpartyAgreementResponse list_counterparty_agreements(as_at=as_at)

[EARLY ACCESS] ListCounterpartyAgreements: List the set of Counterparty Agreements

List the set of Counterparty Agreements at the specified AsAt date/time

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-prd.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.CounterpartiesApi(api_client)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the Counterparty Agreements. Defaults to latest if not specified. (optional)

    try:
        # [EARLY ACCESS] ListCounterpartyAgreements: List the set of Counterparty Agreements
        api_response = api_instance.list_counterparty_agreements(as_at=as_at)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CounterpartiesApi->list_counterparty_agreements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list the Counterparty Agreements. Defaults to latest if not specified. | [optional] 

### Return type

[**ResourceListOfGetCounterpartyAgreementResponse**](ResourceListOfGetCounterpartyAgreementResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Counterparty Agreements |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_credit_support_annexes**
> ResourceListOfGetCreditSupportAnnexResponse list_credit_support_annexes(as_at=as_at)

[EARLY ACCESS] ListCreditSupportAnnexes: List the set of Credit Support Annexes

List the set of Credit Support Annexes at the specified AsAt date/time

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-prd.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.CounterpartiesApi(api_client)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the Credit Support Annexes. Defaults to latest if not specified. (optional)

    try:
        # [EARLY ACCESS] ListCreditSupportAnnexes: List the set of Credit Support Annexes
        api_response = api_instance.list_credit_support_annexes(as_at=as_at)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CounterpartiesApi->list_credit_support_annexes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list the Credit Support Annexes. Defaults to latest if not specified. | [optional] 

### Return type

[**ResourceListOfGetCreditSupportAnnexResponse**](ResourceListOfGetCreditSupportAnnexResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Credit Support Annexes |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_counterparty_agreement**
> UpsertSingleStructuredDataResponse upsert_counterparty_agreement(upsert_counterparty_agreement_request)

[EARLY ACCESS] UpsertCounterpartyAgreement: Upsert Counterparty Agreement

Update or insert Counterparty Agreement in a single scope. An item will be updated if it already exists and inserted if it does not.                The response will return the successfully updated or inserted Counterparty Agreement or failure message if unsuccessful                It is important to always check to verify success (or failure).

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-prd.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.CounterpartiesApi(api_client)
    upsert_counterparty_agreement_request = {"counterpartyAgreement":{"displayName":"display-name","agreementType":"type","counterpartySignatory":{"name":"counterparty-signatory-name","legalEntityIdentifier":{"idTypeScope":"legal-identifier-idTypeScope","idTypeCode":"legal-identifier-idTypeCode","code":"legal-identifier-code"}},"datedAsOf":"2020-01-01T01:00:00.0000000+00:00","creditSupportAnnexId":{"scope":"credit-support-annex-scope","code":"credit-support-annex-code"},"id":{"scope":"some-scope","code":"some-code"}}} # UpsertCounterpartyAgreementRequest | The Counterparty Agreement to update or insert

    try:
        # [EARLY ACCESS] UpsertCounterpartyAgreement: Upsert Counterparty Agreement
        api_response = api_instance.upsert_counterparty_agreement(upsert_counterparty_agreement_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CounterpartiesApi->upsert_counterparty_agreement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_counterparty_agreement_request** | [**UpsertCounterpartyAgreementRequest**](UpsertCounterpartyAgreementRequest.md)| The Counterparty Agreement to update or insert | 

### Return type

[**UpsertSingleStructuredDataResponse**](UpsertSingleStructuredDataResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully updated or inserted Counterparty Agreement or any failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_credit_support_annex**
> UpsertSingleStructuredDataResponse upsert_credit_support_annex(upsert_credit_support_annex_request)

[EARLY ACCESS] UpsertCreditSupportAnnex: Upsert Credit Support Annex

Update or insert Credit Support Annex in a single scope. An item will be updated if it already exists and inserted if it does not.                The response will return the successfully updated or inserted Credit Support Annex or failure message if unsuccessful                It is important to always check to verify success (or failure).

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-prd.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.CounterpartiesApi(api_client)
    upsert_credit_support_annex_request = {"creditSupportAnnex":{"referenceCurrency":"GBP","collateralCurrencies":["GBP"],"isdaAgreementVersion":"ISDA2002","marginCallFrequency":"1W","valuationAgent":"Institution","thresholdAmount":0,"roundingDecimalPlaces":2,"initialMarginAmount":100000,"minimumTransferAmount":10000,"id":{"scope":"some-scope","code":"some-code"}}} # UpsertCreditSupportAnnexRequest | The Credit Support Annex to update or insert

    try:
        # [EARLY ACCESS] UpsertCreditSupportAnnex: Upsert Credit Support Annex
        api_response = api_instance.upsert_credit_support_annex(upsert_credit_support_annex_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CounterpartiesApi->upsert_credit_support_annex: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_credit_support_annex_request** | [**UpsertCreditSupportAnnexRequest**](UpsertCreditSupportAnnexRequest.md)| The Credit Support Annex to update or insert | 

### Return type

[**UpsertSingleStructuredDataResponse**](UpsertSingleStructuredDataResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully updated or inserted item or any failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

