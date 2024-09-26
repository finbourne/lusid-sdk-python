# lusid.TransactionFeesApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_transaction_fee_rule**](TransactionFeesApi.md#delete_transaction_fee_rule) | **DELETE** /api/transactions/fees/rules/{code} | [EXPERIMENTAL] DeleteTransactionFeeRule: Deletes a fee rule.
[**get_applicable_transaction_fees**](TransactionFeesApi.md#get_applicable_transaction_fees) | **POST** /api/transactions/fees/$GetApplicableFees | [EXPERIMENTAL] GetApplicableTransactionFees: Get the Fees and Commissions that may be applicable to a transaction.
[**get_transaction_fee_rule**](TransactionFeesApi.md#get_transaction_fee_rule) | **GET** /api/transactions/fees/rules/{code} | [EXPERIMENTAL] GetTransactionFeeRule: Retrieve the definition of single fee rule.
[**list_transaction_fee_rules**](TransactionFeesApi.md#list_transaction_fee_rules) | **GET** /api/transactions/fees/rules | [EXPERIMENTAL] ListTransactionFeeRules: List fee rules, with optional filtering.
[**upsert_transaction_fee_rules**](TransactionFeesApi.md#upsert_transaction_fee_rules) | **POST** /api/transactions/fees/rules | [EXPERIMENTAL] UpsertTransactionFeeRules: Upsert fee rules.


# **delete_transaction_fee_rule**
> DeletedEntityResponse delete_transaction_fee_rule(code)

[EXPERIMENTAL] DeleteTransactionFeeRule: Deletes a fee rule.

<br>              Deletes the rule for all effective time.                <br>              The rule will remain viewable at previous as at times, but it will no longer be considered by              GetApplicableFees.                <br>              This cannot be undone.              

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    TransactionFeesApi
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

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(TransactionFeesApi)
        code = 'code_example' # str | The fee rule code.

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.delete_transaction_fee_rule(code, opts=opts)

            # [EXPERIMENTAL] DeleteTransactionFeeRule: Deletes a fee rule.
            api_response = await api_instance.delete_transaction_fee_rule(code)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling TransactionFeesApi->delete_transaction_fee_rule: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The fee rule code. | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_applicable_transaction_fees**
> ResourceListOfFeeRule get_applicable_transaction_fees(effective_at=effective_at, as_at=as_at, instrument_identifier_type=instrument_identifier_type, instrument_identifier=instrument_identifier, portfolio_scope=portfolio_scope, portfolio_code=portfolio_code, request_body=request_body)

[EXPERIMENTAL] GetApplicableTransactionFees: Get the Fees and Commissions that may be applicable to a transaction.

Additionally, matching can be based on the instrument's properties, its portfolio properties, and any additional property keys present in the data file.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    TransactionFeesApi
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

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(TransactionFeesApi)
        effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to match rule definitions. Defaults to the current LUSID  system datetime if not specified. (optional)
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to match rule definitions. Defaults to returning the latest version if not  specified. (optional)
        instrument_identifier_type = 'instrument_identifier_type_example' # str | Optional. The unique identifier type to use, eg 'Figi' or 'LusidInstrumentId'. (optional)
        instrument_identifier = 'instrument_identifier_example' # str | Optional. The Instrument Identifier to get properties for. (optional)
        portfolio_scope = 'portfolio_scope_example' # str | Optional. The scope of the portfolio to fetch properties from. (optional)
        portfolio_code = 'portfolio_code_example' # str | Optional. The code of the portfolio to fetch properties from. (optional)
        request_body = {"SettlementCurrency":"GBP","Country":"UK","Instrument/default/HeadOffice":"London"} # Dict[str, str] | Any other property keys or fields, including the top-level fields of the              fee rule (e.g. \"ExecutionBroker\" and \"SettlementCurrency\" ) and those defined in AdditionalKeys, along with              their corresponding values that should be matched for fees. Eg. \"Instrument/default/Name=exampleValue\" or              \"AdditionalKey2=Value2\". (optional)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.get_applicable_transaction_fees(effective_at=effective_at, as_at=as_at, instrument_identifier_type=instrument_identifier_type, instrument_identifier=instrument_identifier, portfolio_scope=portfolio_scope, portfolio_code=portfolio_code, request_body=request_body, opts=opts)

            # [EXPERIMENTAL] GetApplicableTransactionFees: Get the Fees and Commissions that may be applicable to a transaction.
            api_response = await api_instance.get_applicable_transaction_fees(effective_at=effective_at, as_at=as_at, instrument_identifier_type=instrument_identifier_type, instrument_identifier=instrument_identifier, portfolio_scope=portfolio_scope, portfolio_code=portfolio_code, request_body=request_body)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling TransactionFeesApi->get_applicable_transaction_fees: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **effective_at** | **str**| The effective datetime or cut label at which to match rule definitions. Defaults to the current LUSID  system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to match rule definitions. Defaults to returning the latest version if not  specified. | [optional] 
 **instrument_identifier_type** | **str**| Optional. The unique identifier type to use, eg &#39;Figi&#39; or &#39;LusidInstrumentId&#39;. | [optional] 
 **instrument_identifier** | **str**| Optional. The Instrument Identifier to get properties for. | [optional] 
 **portfolio_scope** | **str**| Optional. The scope of the portfolio to fetch properties from. | [optional] 
 **portfolio_code** | **str**| Optional. The code of the portfolio to fetch properties from. | [optional] 
 **request_body** | [**Dict[str, str]**](str.md)| Any other property keys or fields, including the top-level fields of the              fee rule (e.g. \&quot;ExecutionBroker\&quot; and \&quot;SettlementCurrency\&quot; ) and those defined in AdditionalKeys, along with              their corresponding values that should be matched for fees. Eg. \&quot;Instrument/default/Name&#x3D;exampleValue\&quot; or              \&quot;AdditionalKey2&#x3D;Value2\&quot;. | [optional] 

### Return type

[**ResourceListOfFeeRule**](ResourceListOfFeeRule.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of applicable fee rules. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_transaction_fee_rule**
> FeeRule get_transaction_fee_rule(code, effective_at=effective_at, as_at=as_at)

[EXPERIMENTAL] GetTransactionFeeRule: Retrieve the definition of single fee rule.

Retrieves the fee rule definition at the given effective and as at times.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    TransactionFeesApi
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

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(TransactionFeesApi)
        code = 'code_example' # str | The fee rule code.
        effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve the rule definition. Defaults to the current LUSID  system datetime if not specified. (optional)
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the rule definition. Defaults to returning the latest version if not  specified. (optional)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.get_transaction_fee_rule(code, effective_at=effective_at, as_at=as_at, opts=opts)

            # [EXPERIMENTAL] GetTransactionFeeRule: Retrieve the definition of single fee rule.
            api_response = await api_instance.get_transaction_fee_rule(code, effective_at=effective_at, as_at=as_at)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling TransactionFeesApi->get_transaction_fee_rule: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The fee rule code. | 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the rule definition. Defaults to the current LUSID  system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the rule definition. Defaults to returning the latest version if not  specified. | [optional] 

### Return type

[**FeeRule**](FeeRule.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details of one fee rule. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_transaction_fee_rules**
> ResourceListOfFeeRule list_transaction_fee_rules(effective_at=effective_at, as_at=as_at, limit=limit, filter=filter, page=page)

[EXPERIMENTAL] ListTransactionFeeRules: List fee rules, with optional filtering.

For more information about filtering results,  see https://support.lusid.com/knowledgebase/article/KA-01914.

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    TransactionFeesApi
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

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(TransactionFeesApi)
        effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve the rule definitions. Defaults to the current LUSID  system datetime if not specified. (optional)
        as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the rule definitions. Defaults to returning the latest version if not  specified. (optional)
        limit = 56 # int | When paginating, limit the results to this number. Defaults to 100 if not specified. (optional)
        filter = 'filter_example' # str | Expression to filter the results. (optional)
        page = 'page_example' # str | The pagination token to use to continue listing entities; this value is returned from the previous call. If  a pagination token is provided, the filter, effectiveAt and asAt fields must not have changed since the  original request. (optional)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.list_transaction_fee_rules(effective_at=effective_at, as_at=as_at, limit=limit, filter=filter, page=page, opts=opts)

            # [EXPERIMENTAL] ListTransactionFeeRules: List fee rules, with optional filtering.
            api_response = await api_instance.list_transaction_fee_rules(effective_at=effective_at, as_at=as_at, limit=limit, filter=filter, page=page)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling TransactionFeesApi->list_transaction_fee_rules: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the rule definitions. Defaults to the current LUSID  system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the rule definitions. Defaults to returning the latest version if not  specified. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results. | [optional] 
 **page** | **str**| The pagination token to use to continue listing entities; this value is returned from the previous call. If  a pagination token is provided, the filter, effectiveAt and asAt fields must not have changed since the  original request. | [optional] 

### Return type

[**ResourceListOfFeeRule**](ResourceListOfFeeRule.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A filtered list of fee rules available. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **upsert_transaction_fee_rules**
> FeeRuleUpsertResponse upsert_transaction_fee_rules(request_body, effective_at=effective_at)

[EXPERIMENTAL] UpsertTransactionFeeRules: Upsert fee rules.

<br>              To upsert a new rule, the code field must be left empty, a code will then be assigned and returned as part              of the response. To update an existing rule, include the fee code. It is possible to both create and update              fee rules in the same request.                <br>              The upsert is transactional - either all create/update operations will succeed or none of them will.              

### Example

```python
import asyncio
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    ApiClientFactory,
    TransactionFeesApi
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

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(TransactionFeesApi)
        request_body = {"Update":{"code":"FeeRule_1","transactionPropertyKey":"Transaction/default/fee","transactionType":"*","country":"UK","counterparty":"*","transactionCurrency":"*","settlementCurrency":"*","executionBroker":"*","custodian":"*","exchange":"My Exchange","fee":{"calculationMethod":"BasisPoints","multiplier":"Value","calculationAmount":10},"additionalKeys":{"Instrument/default/HeadOffice":"London"},"description":"Basic fee rule to be updated."},"Create":{"transactionPropertyKey":"Transaction/default/fee","transactionType":"*","country":"UK","counterparty":"*","transactionCurrency":"*","settlementCurrency":"*","executionBroker":"*","custodian":"*","exchange":"My Exchange","fee":{"calculationMethod":"BasisPoints","multiplier":"Value","calculationAmount":10},"minFee":{"calculationMethod":"Flat","multiplier":"Value","calculationAmount":5},"maxFee":{"calculationMethod":"Flat","multiplier":"Value","calculationAmount":25},"additionalKeys":{"Instrument/default/HeadOffice":"London"},"description":"Basic fee rule with minimum/maximum to be created"}} # Dict[str, FeeRuleUpsertRequest] | A dictionary of upsert request identifiers to rule upsert requests. The request              identifiers are valid for the request only and can be used to link the upserted fee rule to the code of a              created fee rule.
        effective_at = 'effective_at_example' # str | The effective datetime or cut label at which the rule will take effect. Defaults to the current LUSID  system datetime if not specified. In the case of an update, the changes will take place from this effective  time until the next effective time that the rule as been upserted at. For example, consider a rule that  already exists, and has previously had an update applied so that the definition will change on the first day  of the coming month. An upsert effective from the current day will only change the definition until the  first day of the coming month. An additional upsert at the same time (first day of the month) is required  if the newly-updated definition is to supersede the future definition. (optional)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.upsert_transaction_fee_rules(request_body, effective_at=effective_at, opts=opts)

            # [EXPERIMENTAL] UpsertTransactionFeeRules: Upsert fee rules.
            api_response = await api_instance.upsert_transaction_fee_rules(request_body, effective_at=effective_at)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling TransactionFeesApi->upsert_transaction_fee_rules: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, FeeRuleUpsertRequest]**](FeeRuleUpsertRequest.md)| A dictionary of upsert request identifiers to rule upsert requests. The request              identifiers are valid for the request only and can be used to link the upserted fee rule to the code of a              created fee rule. | 
 **effective_at** | **str**| The effective datetime or cut label at which the rule will take effect. Defaults to the current LUSID  system datetime if not specified. In the case of an update, the changes will take place from this effective  time until the next effective time that the rule as been upserted at. For example, consider a rule that  already exists, and has previously had an update applied so that the definition will change on the first day  of the coming month. An upsert effective from the current day will only change the definition until the  first day of the coming month. An additional upsert at the same time (first day of the month) is required  if the newly-updated definition is to supersede the future definition. | [optional] 

### Return type

[**FeeRuleUpsertResponse**](FeeRuleUpsertResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Upsert fee rules. New fee rules must have an empty code field. Where a code is given, this rule must already exist and will be updated. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

