# CorporateActionTransitionRequest

A 'transition' within a corporate action, representing a set of output movements paired to a single input position

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_transition** | [**CorporateActionTransitionComponentRequest**](CorporateActionTransitionComponentRequest.md) |  | [optional] 
**output_transitions** | [**List[CorporateActionTransitionComponentRequest]**](CorporateActionTransitionComponentRequest.md) |  | [optional] 

## Example

```python
from lusid.models.corporate_action_transition_request import CorporateActionTransitionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CorporateActionTransitionRequest from a JSON string
corporate_action_transition_request_instance = CorporateActionTransitionRequest.from_json(json)
# print the JSON string representation of the object
print CorporateActionTransitionRequest.to_json()

# convert the object into a dict
corporate_action_transition_request_dict = corporate_action_transition_request_instance.to_dict()
# create an instance of CorporateActionTransitionRequest from a dict
corporate_action_transition_request_form_dict = corporate_action_transition_request.from_dict(corporate_action_transition_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


