# lusid.TaxClassificationsApi

All URIs are relative to *https://fbn-prd.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_tax_classification**](TaxClassificationsApi.md#get_tax_classification) | **GET** /api/tax/classifications/{scope}/{luid} | [EARLY ACCESS] GetTaxClassification: Get a tax classification.
[**get_tax_qualifying_investments_history**](TaxClassificationsApi.md#get_tax_qualifying_investments_history) | **GET** /api/tax/classifications/{scope}/{luid}/qualifyinginvestments | [EARLY ACCESS] GetTaxQualifyingInvestmentsHistory: Get the qualifying investments history of an instrument.
[**list_tax_classification_exceptions**](TaxClassificationsApi.md#list_tax_classification_exceptions) | **GET** /api/tax/classifications/exceptions | [EARLY ACCESS] ListTaxClassificationExceptions: List tax classification exceptions.
[**list_tax_classifications**](TaxClassificationsApi.md#list_tax_classifications) | **GET** /api/tax/classifications | [EARLY ACCESS] ListTaxClassifications: List tax classifications.
[**remove_tax_treatment_override**](TaxClassificationsApi.md#remove_tax_treatment_override) | **DELETE** /api/tax/classifications/{scope}/{luid}/override | [EARLY ACCESS] RemoveTaxTreatmentOverride: Remove a tax treatment override.
[**upsert_tax_treatment_override**](TaxClassificationsApi.md#upsert_tax_treatment_override) | **POST** /api/tax/classifications/{scope}/{luid}/override | [EARLY ACCESS] UpsertTaxTreatmentOverride: Upsert a tax treatment override.


# **get_tax_classification**
> TaxClassificationDetail get_tax_classification(scope, luid, effective_at=effective_at, as_at=as_at)

[EARLY ACCESS] GetTaxClassification: Get a tax classification.

Gets one instrument's tax classification together with the ordered decision trace that produced it and the  bitemporal history of every input and override field behind it.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TaxClassificationsApi
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
    api_instance = api_client_factory.build(TaxClassificationsApi)
    scope = 'scope_example' # str | The scope of the instrument.
    luid = 'luid_example' # str | The LUSID instrument identifier of the instrument.
    effective_at = 'effective_at_example' # str | Optional. The effective datetime or cut label at which to classify. Defaults to the current time. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The as-at datetime at which to read the classification inputs. Defaults to the latest. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_tax_classification(scope, luid, effective_at=effective_at, as_at=as_at, opts=opts)

        # [EARLY ACCESS] GetTaxClassification: Get a tax classification.
        api_response = api_instance.get_tax_classification(scope, luid, effective_at=effective_at, as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TaxClassificationsApi->get_tax_classification: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the instrument. | 
 **luid** | **str**| The LUSID instrument identifier of the instrument. | 
 **effective_at** | **str**| Optional. The effective datetime or cut label at which to classify. Defaults to the current time. | [optional] 
 **as_at** | **datetime**| Optional. The as-at datetime at which to read the classification inputs. Defaults to the latest. | [optional] 

### Return type

[**TaxClassificationDetail**](TaxClassificationDetail.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The tax classification of the instrument with its decision trace and field history. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_tax_qualifying_investments_history**
> QualifyingInvestmentsHistory get_tax_qualifying_investments_history(scope, luid, from_date=from_date, to_date=to_date, as_at=as_at)

[EARLY ACCESS] GetTaxQualifyingInvestmentsHistory: Get the qualifying investments history of an instrument.

Returns the daily qualifying investments (60 percent non-equity) test observations of a collective investment  scheme over the requested window, together with every crossing: a pair of consecutive observations on which  the test result flipped.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TaxClassificationsApi
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
    api_instance = api_client_factory.build(TaxClassificationsApi)
    scope = 'scope_example' # str | The scope of the instrument.
    luid = 'luid_example' # str | The LUSID instrument identifier of the scheme.
    from_date = '2013-10-20T19:20:30+01:00' # datetime | Optional. The first date of the window, inclusive. Defaults to one year before the toDate. The window may span at most ten years. (optional)
    to_date = '2013-10-20T19:20:30+01:00' # datetime | Optional. The last date of the window, inclusive. Defaults to the asAt date. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The as-at datetime at which to read the observations. Defaults to the latest. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_tax_qualifying_investments_history(scope, luid, from_date=from_date, to_date=to_date, as_at=as_at, opts=opts)

        # [EARLY ACCESS] GetTaxQualifyingInvestmentsHistory: Get the qualifying investments history of an instrument.
        api_response = api_instance.get_tax_qualifying_investments_history(scope, luid, from_date=from_date, to_date=to_date, as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TaxClassificationsApi->get_tax_qualifying_investments_history: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the instrument. | 
 **luid** | **str**| The LUSID instrument identifier of the scheme. | 
 **from_date** | **datetime**| Optional. The first date of the window, inclusive. Defaults to one year before the toDate. The window may span at most ten years. | [optional] 
 **to_date** | **datetime**| Optional. The last date of the window, inclusive. Defaults to the asAt date. | [optional] 
 **as_at** | **datetime**| Optional. The as-at datetime at which to read the observations. Defaults to the latest. | [optional] 

### Return type

[**QualifyingInvestmentsHistory**](QualifyingInvestmentsHistory.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The qualifying investments observations and crossings of the instrument. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_tax_classification_exceptions**
> ResourceListOfTaxClassificationExceptionRecord list_tax_classification_exceptions(scope, effective_at=effective_at, as_at=as_at)

[EARLY ACCESS] ListTaxClassificationExceptions: List tax classification exceptions.

Lists every instrument in the scope that could not be classified at the given time, with the kind of  exception (missing inputs, conflicting set-up, conflicting override, qualifying investments crossing) and a  message naming the fields involved.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TaxClassificationsApi
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
    api_instance = api_client_factory.build(TaxClassificationsApi)
    scope = 'scope_example' # str | The scope of the instruments.
    effective_at = 'effective_at_example' # str | Optional. The effective datetime or cut label at which to classify. Defaults to the current time. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The as-at datetime at which to read the classification inputs. Defaults to the latest. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_tax_classification_exceptions(scope, effective_at=effective_at, as_at=as_at, opts=opts)

        # [EARLY ACCESS] ListTaxClassificationExceptions: List tax classification exceptions.
        api_response = api_instance.list_tax_classification_exceptions(scope, effective_at=effective_at, as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TaxClassificationsApi->list_tax_classification_exceptions: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the instruments. | 
 **effective_at** | **str**| Optional. The effective datetime or cut label at which to classify. Defaults to the current time. | [optional] 
 **as_at** | **datetime**| Optional. The as-at datetime at which to read the classification inputs. Defaults to the latest. | [optional] 

### Return type

[**ResourceListOfTaxClassificationExceptionRecord**](ResourceListOfTaxClassificationExceptionRecord.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The instruments that could not be classified and the reason for each. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_tax_classifications**
> ResourceListOfTaxClassification list_tax_classifications(scope, treatment=treatment, status=status, effective_at=effective_at, as_at=as_at)

[EARLY ACCESS] ListTaxClassifications: List tax classifications.

Lists the tax classification of every instrument in the scope at the given effective and as-at time. Each  entry carries the treatment leaf the instrument resolved to, the treatment it implies, whether it was  system-derived or overridden, and the rule that fired. Narrow the list with the treatment and status filters.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TaxClassificationsApi
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
    api_instance = api_client_factory.build(TaxClassificationsApi)
    scope = 'scope_example' # str | The scope of the instruments to classify.
    treatment = 'treatment_example' # str | Optional. Only return instruments with this treatment. Available values: ChargeableGains, LoanRelationship, Excluded, Unclassified. (optional)
    status = 'status_example' # str | Optional. Only return instruments with this classification status. Available values: Classified, Overridden, Rejected, Unclassified. (optional)
    effective_at = 'effective_at_example' # str | Optional. The effective datetime or cut label at which to classify. Defaults to the current time. (optional)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The as-at datetime at which to read the classification inputs. Defaults to the latest. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_tax_classifications(scope, treatment=treatment, status=status, effective_at=effective_at, as_at=as_at, opts=opts)

        # [EARLY ACCESS] ListTaxClassifications: List tax classifications.
        api_response = api_instance.list_tax_classifications(scope, treatment=treatment, status=status, effective_at=effective_at, as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TaxClassificationsApi->list_tax_classifications: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the instruments to classify. | 
 **treatment** | **str**| Optional. Only return instruments with this treatment. Available values: ChargeableGains, LoanRelationship, Excluded, Unclassified. | [optional] 
 **status** | **str**| Optional. Only return instruments with this classification status. Available values: Classified, Overridden, Rejected, Unclassified. | [optional] 
 **effective_at** | **str**| Optional. The effective datetime or cut label at which to classify. Defaults to the current time. | [optional] 
 **as_at** | **datetime**| Optional. The as-at datetime at which to read the classification inputs. Defaults to the latest. | [optional] 

### Return type

[**ResourceListOfTaxClassification**](ResourceListOfTaxClassification.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The tax classifications of the instruments in the scope. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **remove_tax_treatment_override**
> DeletedEntityResponse remove_tax_treatment_override(scope, luid, effective_at=effective_at)

[EARLY ACCESS] RemoveTaxTreatmentOverride: Remove a tax treatment override.

Removes the user override from the given effective date onward, returning the instrument to its  system-derived treatment leaf from that date.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TaxClassificationsApi
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
    api_instance = api_client_factory.build(TaxClassificationsApi)
    scope = 'scope_example' # str | The scope of the instrument.
    luid = 'luid_example' # str | The LUSID instrument identifier of the instrument.
    effective_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The effective datetime from which the override no longer applies. Defaults to the current time. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.remove_tax_treatment_override(scope, luid, effective_at=effective_at, opts=opts)

        # [EARLY ACCESS] RemoveTaxTreatmentOverride: Remove a tax treatment override.
        api_response = api_instance.remove_tax_treatment_override(scope, luid, effective_at=effective_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TaxClassificationsApi->remove_tax_treatment_override: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the instrument. | 
 **luid** | **str**| The LUSID instrument identifier of the instrument. | 
 **effective_at** | **datetime**| Optional. The effective datetime from which the override no longer applies. Defaults to the current time. | [optional] 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime from which the override was removed. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **upsert_tax_treatment_override**
> TaxClassification upsert_tax_treatment_override(scope, luid, upsert_tax_treatment_override_request)

[EARLY ACCESS] UpsertTaxTreatmentOverride: Upsert a tax treatment override.

Replaces the system-derived treatment leaf of the instrument with the given one from the request's effective  date onward. The response is the classification as it now stands at that effective date.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    TaxClassificationsApi
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
    api_instance = api_client_factory.build(TaxClassificationsApi)
    scope = 'scope_example' # str | The scope of the instrument.
    luid = 'luid_example' # str | The LUSID instrument identifier of the instrument.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # upsert_tax_treatment_override_request = UpsertTaxTreatmentOverrideRequest.from_json("")
    # upsert_tax_treatment_override_request = UpsertTaxTreatmentOverrideRequest.from_dict({})
    upsert_tax_treatment_override_request = UpsertTaxTreatmentOverrideRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.upsert_tax_treatment_override(scope, luid, upsert_tax_treatment_override_request, opts=opts)

        # [EARLY ACCESS] UpsertTaxTreatmentOverride: Upsert a tax treatment override.
        api_response = api_instance.upsert_tax_treatment_override(scope, luid, upsert_tax_treatment_override_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TaxClassificationsApi->upsert_tax_treatment_override: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the instrument. | 
 **luid** | **str**| The LUSID instrument identifier of the instrument. | 
 **upsert_tax_treatment_override_request** | [**UpsertTaxTreatmentOverrideRequest**](UpsertTaxTreatmentOverrideRequest.md)| The treatment leaf to apply and the effective date it applies from. | 

### Return type

[**TaxClassification**](TaxClassification.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The classification of the instrument after the override was applied. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

