# ValuationPointResourceListOfTrialBalance

ResourceList with extra header fields used by the various ValuationPoint endpoints for returning additional context related to the list of results.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_valuation_point** | [**DiaryEntry**](DiaryEntry.md) |  | [optional] 
**version** | [**Version**](Version.md) |  | 
**values** | [**List[TrialBalance]**](TrialBalance.md) |  | 
**href** | **str** |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.valuation_point_resource_list_of_trial_balance import ValuationPointResourceListOfTrialBalance

# TODO update the JSON string below
json = "{}"
# create an instance of ValuationPointResourceListOfTrialBalance from a JSON string
valuation_point_resource_list_of_trial_balance_instance = ValuationPointResourceListOfTrialBalance.from_json(json)
# print the JSON string representation of the object
print ValuationPointResourceListOfTrialBalance.to_json()

# convert the object into a dict
valuation_point_resource_list_of_trial_balance_dict = valuation_point_resource_list_of_trial_balance_instance.to_dict()
# create an instance of ValuationPointResourceListOfTrialBalance from a dict
valuation_point_resource_list_of_trial_balance_form_dict = valuation_point_resource_list_of_trial_balance.from_dict(valuation_point_resource_list_of_trial_balance_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


