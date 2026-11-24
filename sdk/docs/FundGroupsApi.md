# lusid.FundGroupsApi

All URIs are relative to *https://fbn-prd.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_fund_group_trial_balance**](FundGroupsApi.md#get_fund_group_trial_balance) | **POST** /api/fundgroups/{scope}/{code}/trialbalance/$query | [EARLY ACCESS] GetFundGroupTrialBalance: Get the Trial Balance for a group of Funds.


# **get_fund_group_trial_balance**
> FundGroupTrialBalanceResponse get_fund_group_trial_balance(scope, code, fund_group_trial_balance_request, as_at=as_at, filter=filter, limit=limit, page=page, property_keys=property_keys)

[EARLY ACCESS] GetFundGroupTrialBalance: Get the Trial Balance for a group of Funds.

Runs the Trial Balance once for every Fund in a fund group, where the group is a reference list of type  FundIdList or FilteredFundIdList identified by the scope and code. LUSID chooses the Valuation Point for  each Fund and NAV type from the run type, and each returned row carries the Fund, NAV type and Valuation Point  it came from. A Fund that could not be reported, because no Valuation Point matches the run type or the NAV type  is missing, is listed in fundResults alongside the rows. A Fund in a FundIdList that the caller is not entitled  to read is listed there too; a FilteredFundIdList only ever contains the Funds the caller can read.                Rows are ordered by Fund scope, then Fund code, then NAV type code, then as GetValuationPointTrialBalance orders  them, so the order is stable across pages.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    FundGroupsApi
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
    api_instance = api_client_factory.build(FundGroupsApi)
    scope = 'scope_example' # str | The scope of the reference list that defines the fund group.
    code = 'code_example' # str | The code of the reference list that defines the fund group. Together with the scope this uniquely identifies the reference list.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # fund_group_trial_balance_request = FundGroupTrialBalanceRequest.from_json("")
    # fund_group_trial_balance_request = FundGroupTrialBalanceRequest.from_dict({})
    fund_group_trial_balance_request = FundGroupTrialBalanceRequest()
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Trial Balances and resolve the fund group.               Defaults to returning the latest version if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the rows by, using the same fields as GetValuationPointTrialBalance.               For more information about filtering results, see https://support.lusid.com/docs/filtering-information-retrieved-from-lusid. (optional)
    limit = 56 # int | When paginating, limit the number of returned rows to this number.               Defaults to 100 if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing rows.               This token is returned from the previous call.               If a pagination token is provided, the filter, request body and asAt fields               must not have changed since the original request. (optional)
    property_keys = ['property_keys_example'] # List[str] | A list of property keys from the 'Instrument', 'Transaction', 'Portfolio', 'Account', 'LegalEntity' or 'CustodianAccount'               domain to decorate onto each row's TrialBalance. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_fund_group_trial_balance(scope, code, fund_group_trial_balance_request, as_at=as_at, filter=filter, limit=limit, page=page, property_keys=property_keys, opts=opts)

        # [EARLY ACCESS] GetFundGroupTrialBalance: Get the Trial Balance for a group of Funds.
        api_response = api_instance.get_fund_group_trial_balance(scope, code, fund_group_trial_balance_request, as_at=as_at, filter=filter, limit=limit, page=page, property_keys=property_keys)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling FundGroupsApi->get_fund_group_trial_balance: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the reference list that defines the fund group. | 
 **code** | **str**| The code of the reference list that defines the fund group. Together with the scope this uniquely identifies the reference list. | 
 **fund_group_trial_balance_request** | [**FundGroupTrialBalanceRequest**](FundGroupTrialBalanceRequest.md)| The run type, dates, NAV type and Trial Balance options. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Trial Balances and resolve the fund group.               Defaults to returning the latest version if not specified. | [optional] 
 **filter** | **str**| Expression to filter the rows by, using the same fields as GetValuationPointTrialBalance.               For more information about filtering results, see https://support.lusid.com/docs/filtering-information-retrieved-from-lusid. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned rows to this number.               Defaults to 100 if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing rows.               This token is returned from the previous call.               If a pagination token is provided, the filter, request body and asAt fields               must not have changed since the original request. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;Instrument&#39;, &#39;Transaction&#39;, &#39;Portfolio&#39;, &#39;Account&#39;, &#39;LegalEntity&#39; or &#39;CustodianAccount&#39;               domain to decorate onto each row&#39;s TrialBalance. | [optional] 

### Return type

[**FundGroupTrialBalanceResponse**](FundGroupTrialBalanceResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Trial Balance rows of the Funds in the group, with the outcome for each Fund and NAV type. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

