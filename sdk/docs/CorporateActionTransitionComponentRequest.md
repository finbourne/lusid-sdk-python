# CorporateActionTransitionComponentRequest

A single transition component request, when grouped with other transition component requests a corporate action  transition request is formed.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_identifiers** | **Dict[str, str]** | Unique instrument identifiers | 
**units_factor** | **float** | The factor to scale units by | 
**cost_factor** | **float** | The factor to scale cost by | 

## Example

```python
from lusid.models.corporate_action_transition_component_request import CorporateActionTransitionComponentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CorporateActionTransitionComponentRequest from a JSON string
corporate_action_transition_component_request_instance = CorporateActionTransitionComponentRequest.from_json(json)
# print the JSON string representation of the object
print CorporateActionTransitionComponentRequest.to_json()

# convert the object into a dict
corporate_action_transition_component_request_dict = corporate_action_transition_component_request_instance.to_dict()
# create an instance of CorporateActionTransitionComponentRequest from a dict
corporate_action_transition_component_request_form_dict = corporate_action_transition_component_request.from_dict(corporate_action_transition_component_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


