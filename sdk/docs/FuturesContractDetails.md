# FuturesContractDetails

Most, if not all, information about contracts is standardized. See, e.g. https://www.cmegroup.com/ for  common codes and similar data. This appears to be in common use by well known market information providers, e.g. Bloomberg and Refinitiv.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dom_ccy** | **str** | Currency in which the contract is paid. | 
**fgn_ccy** | **str** | Currency of the underlying, for use with FX Futures | [optional] 
**asset_class** | **str** | The asset class of the underlying. Optional and will default to Unknown if not set.    Supported string (enumeration) values are: [InterestRates, FX, Inflation, Equities, Credit, Commodities, Money]. | [optional] 
**contract_code** | **str** | The contract code used by the exchange, e.g. “CL” for Crude Oil, “ES” for E-mini SP 500, “FGBL” for Bund Futures, etc. | 
**contract_month** | **str** | Which month does the contract trade for.    Supported string (enumeration) values are: [F, G, H, J, K, M, N, Q, U, V, X, Z]. | [optional] 
**contract_size** | **float** | Size of a single contract. | 
**convention** | **str** | If appropriate, the day count convention method used in pricing (rates futures).  For more information on day counts, see [knowledge base article KA-01798](https://support.lusid.com/knowledgebase/article/KA-01798)                Supported string (enumeration) values are: [Actual360, Act360, MoneyMarket, Actual365, Act365, Thirty360, ThirtyU360, Bond, ThirtyE360, EuroBond, ActualActual, ActAct, ActActIsda, ActActIsma, ActActIcma, OneOne, Act364, Act365F, Act365L, Act365_25, Act252, Bus252, NL360, NL365, ActActAFB, Act365Cad, ThirtyActIsda, Thirty365Isda, ThirtyEActIsda, ThirtyE360Isda, ThirtyE365Isda, ThirtyU360EOM]. | [optional] 
**country** | **str** | Country (code) for the exchange. | [optional] 
**description** | **str** | Description of contract. | [optional] 
**exchange_code** | **str** | Exchange code for contract. This can be any string to uniquely identify the exchange (e.g. Exchange Name, MIC, BBG code). | 
**exchange_name** | **str** | Exchange name (for when code is not automatically recognised). | [optional] 
**ticker_step** | **float** | Minimal step size change in ticker. | [optional] 
**unit_value** | **float** | The value in the currency of a 1 unit change in the contract price. | [optional] 
**calendars** | **List[str]** | Holiday calendars that apply to yield-to-price conversions (i.e. for BRL futures). | [optional] 
**delivery_type** | **str** | Delivery type to be used on settling the contract.  Optional: Defaults to DeliveryType.Physical if not provided.    Supported string (enumeration) values are: [Cash, Physical]. | [optional] 

## Example

```python
from lusid.models.futures_contract_details import FuturesContractDetails

# TODO update the JSON string below
json = "{}"
# create an instance of FuturesContractDetails from a JSON string
futures_contract_details_instance = FuturesContractDetails.from_json(json)
# print the JSON string representation of the object
print FuturesContractDetails.to_json()

# convert the object into a dict
futures_contract_details_dict = futures_contract_details_instance.to_dict()
# create an instance of FuturesContractDetails from a dict
futures_contract_details_form_dict = futures_contract_details.from_dict(futures_contract_details_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


