# TrialBalanceQueryParameters


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | [**DateOrDiaryEntry**](DateOrDiaryEntry.md) |  | [optional] 
**end** | [**DateOrDiaryEntry**](DateOrDiaryEntry.md) |  | [optional] 
**date_mode** | **str** | The mode of calculation of the trial balance. The available values are: ActivityDate, AccountingDate. | [optional] 
**general_ledger_profile_code** | **str** | The optional code of a general ledger profile used to decorate trial balance with levels. | [optional] 
**property_keys** | **List[str]** | A list of property keys from the &#39;Instrument&#39;, &#39;Transaction&#39;, &#39;Portfolio&#39;, &#39;Account&#39;, &#39;LegalEntity&#39; or &#39;CustodianAccount&#39; domain to decorate onto the trial balance. | [optional] 
**exclude_cleardown_module** | **bool** | By deafult this flag is set to false, if this is set to true, no cleardown module will be applied to the trial balance. | [optional] 

## Example

```python
from lusid.models.trial_balance_query_parameters import TrialBalanceQueryParameters

# TODO update the JSON string below
json = "{}"
# create an instance of TrialBalanceQueryParameters from a JSON string
trial_balance_query_parameters_instance = TrialBalanceQueryParameters.from_json(json)
# print the JSON string representation of the object
print TrialBalanceQueryParameters.to_json()

# convert the object into a dict
trial_balance_query_parameters_dict = trial_balance_query_parameters_instance.to_dict()
# create an instance of TrialBalanceQueryParameters from a dict
trial_balance_query_parameters_form_dict = trial_balance_query_parameters.from_dict(trial_balance_query_parameters_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


