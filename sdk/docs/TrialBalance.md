# TrialBalance

A TrialBalance entity.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**general_ledger_account_code** | **str** | The Account code that the trial balance results have been grouped against | 
**description** | **str** | The description of the record | [optional] 
**levels** | **List[str]** | The levels that have been derived from the specified General Ledger Profile | 
**account_type** | **str** | The account type attributed to the record | 
**opening** | **float** | The opening balance at the start of the period | 
**closing** | **float** | The closing balance at the end of the period | 
**debit** | **float** | All debits that occured in the period | 
**credit** | **float** | All credits that occured in the period | 
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
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


