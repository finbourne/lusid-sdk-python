# CorporateActionTransitionComponent

A single transition component, when grouped with other components a corporate action transition is formed.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_scope** | **str** | The scope in which the instrument lies. | 
**instrument_identifiers** | **Dict[str, str]** | Unique instrument identifiers | 
**instrument_uid** | **str** | LUSID&#39;s internal unique instrument identifier, resolved from the instrument identifiers | 
**units_factor** | **float** | The factor to scale units by | 
**cost_factor** | **float** | The factor to scale cost by | 

## Example

```python
from lusid.models.corporate_action_transition_component import CorporateActionTransitionComponent

# TODO update the JSON string below
json = "{}"
# create an instance of CorporateActionTransitionComponent from a JSON string
corporate_action_transition_component_instance = CorporateActionTransitionComponent.from_json(json)
# print the JSON string representation of the object
print CorporateActionTransitionComponent.to_json()

# convert the object into a dict
corporate_action_transition_component_dict = corporate_action_transition_component_instance.to_dict()
# create an instance of CorporateActionTransitionComponent from a dict
corporate_action_transition_component_form_dict = corporate_action_transition_component.from_dict(corporate_action_transition_component_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


