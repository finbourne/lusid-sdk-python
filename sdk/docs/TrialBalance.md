# TrialBalance

A TrialBalance entity.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**general_ledger_account_code** | **str** | The Account code that the trial balance results have been grouped against. | 
**description** | **str** | The description of the record. | [optional] 
**levels** | **List[str]** | The levels that have been derived from the specified General Ledger Profile. | 
**account_type** | **str** | The account type attributed to the record. | 
**local_currency** | **str** | The local currency for the amounts specified. Defaults to base currency if multiple different currencies present in the grouped line. | 
**opening** | [**MultiCurrencyAmounts**](MultiCurrencyAmounts.md) |  | 
**closing** | [**MultiCurrencyAmounts**](MultiCurrencyAmounts.md) |  | 
**debit** | [**MultiCurrencyAmounts**](MultiCurrencyAmounts.md) |  | 
**credit** | [**MultiCurrencyAmounts**](MultiCurrencyAmounts.md) |  | 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | Properties found on the mapped &#39;Account&#39;, as specified in request. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.trial_balance import TrialBalance

# TODO update the JSON string below
json = "{}"
# create an instance of TrialBalance from a JSON string
trial_balance_instance = TrialBalance.from_json(json)
# print the JSON string representation of the object
print TrialBalance.to_json()

# convert the object into a dict
trial_balance_dict = trial_balance_instance.to_dict()
# create an instance of TrialBalance from a dict
trial_balance_form_dict = trial_balance.from_dict(trial_balance_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


