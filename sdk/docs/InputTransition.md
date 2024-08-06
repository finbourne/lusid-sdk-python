# InputTransition

The input 'transition' within a corporate action, representing the singular input position

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**units_factor** | **float** | The factor to scale units by | 
**cost_factor** | **float** | The factor to scale cost by | 

## Example

```python
from lusid.models.input_transition import InputTransition

# TODO update the JSON string below
json = "{}"
# create an instance of InputTransition from a JSON string
input_transition_instance = InputTransition.from_json(json)
# print the JSON string representation of the object
print InputTransition.to_json()

# convert the object into a dict
input_transition_dict = input_transition_instance.to_dict()
# create an instance of InputTransition from a dict
input_transition_form_dict = input_transition.from_dict(input_transition_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


