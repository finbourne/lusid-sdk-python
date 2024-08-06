# CreditSupportAnnex

Entity to capture the calculable and queryable methods and practices of determining and transferring collateral  to a counterparty as part of margining of transactions. These typically come from a particular ISDA agreement  that is in place between the two counterparties.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference_currency** | **str** | The base, or reference, currency against which MtM value and exposure should be calculated  and in which the CSA parameters are defined if the currency is not otherwise explicitly stated. | 
**collateral_currencies** | **List[str]** | The set of currencies within which it is acceptable to post cash collateral. | 
**isda_agreement_version** | **str** | The transactions will take place with reference to a particular ISDA master agreement. This  will likely be either the ISDA 1992 or ISDA 2002 agremeents or ISDA close-out 2009. | 
**margin_call_frequency** | **str** | The tenor, e.g. daily (1D) or biweekly (2W), at which frequency a margin call will be made, calculations  made and money transferred to readjust. The calculation might also require a specific time for valuation and notification. | 
**valuation_agent** | **str** | Are the calculations performed by the institutions&#39;s counterparty or the institution trading with them. | 
**threshold_amount** | **float** | At what level of exposure does collateral need to be posted. Will typically be zero for banks.  Should be stated in reference currency | 
**rounding_decimal_places** | **int** | Where a calculation needs to be rounded to a specific number of decimal places,  this states the number that that requires. | 
**initial_margin_amount** | **float** | The initial margin that is required. In the reference currency | 
**minimum_transfer_amount** | **float** | The minimum amount, in the reference currency, that must be transferred when required. | 
**id** | [**ResourceId**](ResourceId.md) |  | 

## Example

```python
from lusid.models.credit_support_annex import CreditSupportAnnex

# TODO update the JSON string below
json = "{}"
# create an instance of CreditSupportAnnex from a JSON string
credit_support_annex_instance = CreditSupportAnnex.from_json(json)
# print the JSON string representation of the object
print CreditSupportAnnex.to_json()

# convert the object into a dict
credit_support_annex_dict = credit_support_annex_instance.to_dict()
# create an instance of CreditSupportAnnex from a dict
credit_support_annex_form_dict = credit_support_annex.from_dict(credit_support_annex_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


