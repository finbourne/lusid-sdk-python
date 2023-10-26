# CorporateAction

A corporate action

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**corporate_action_code** | **str** | The unique identifier of this corporate action | 
**description** | **str** | The description of the corporate action. | [optional] 
**announcement_date** | **datetime** | The announcement date of the corporate action | [optional] 
**ex_date** | **datetime** | The ex date of the corporate action | [optional] 
**record_date** | **datetime** | The record date of the corporate action | [optional] 
**payment_date** | **datetime** | The payment date of the corporate action | [optional] 
**transitions** | [**List[CorporateActionTransition]**](CorporateActionTransition.md) | The transitions that result from this corporate action | [optional] 

## Example

```python
from lusid.models.corporate_action import CorporateAction

# TODO update the JSON string below
json = "{}"
# create an instance of CorporateAction from a JSON string
corporate_action_instance = CorporateAction.from_json(json)
# print the JSON string representation of the object
print CorporateAction.to_json()

# convert the object into a dict
corporate_action_dict = corporate_action_instance.to_dict()
# create an instance of CorporateAction from a dict
corporate_action_form_dict = corporate_action.from_dict(corporate_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


