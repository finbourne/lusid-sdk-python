# CorporateActionTransition

A 'transition' within a corporate action, representing a set of output movements paired to a single input position

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_transition** | [**CorporateActionTransitionComponent**](CorporateActionTransitionComponent.md) |  | [optional] 
**output_transitions** | [**List[CorporateActionTransitionComponent]**](CorporateActionTransitionComponent.md) | What will be generated relative to the input transition | [optional] 

## Example

```python
from lusid.models.corporate_action_transition import CorporateActionTransition

# TODO update the JSON string below
json = "{}"
# create an instance of CorporateActionTransition from a JSON string
corporate_action_transition_instance = CorporateActionTransition.from_json(json)
# print the JSON string representation of the object
print CorporateActionTransition.to_json()

# convert the object into a dict
corporate_action_transition_dict = corporate_action_transition_instance.to_dict()
# create an instance of CorporateActionTransition from a dict
corporate_action_transition_form_dict = corporate_action_transition.from_dict(corporate_action_transition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


