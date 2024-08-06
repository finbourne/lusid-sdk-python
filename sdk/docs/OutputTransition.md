# OutputTransition

A 'transition' within a corporate action, representing an output transition.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_identifiers** | **Dict[str, str]** | Unique instrument identifiers | 
**units_factor** | **float** | The factor to scale units by | 
**cost_factor** | **float** | The factor to scale cost by | 
**lusid_instrument_id** | **str** | LUSID&#39;s internal unique instrument identifier, resolved from the instrument identifiers | [optional] [readonly] 
**instrument_scope** | **str** | The scope in which the instrument lies. | [optional] [readonly] 
**rounding** | [**RoundingConfiguration**](RoundingConfiguration.md) |  | [optional] 

## Example

```python
from lusid.models.output_transition import OutputTransition

# TODO update the JSON string below
json = "{}"
# create an instance of OutputTransition from a JSON string
output_transition_instance = OutputTransition.from_json(json)
# print the JSON string representation of the object
print OutputTransition.to_json()

# convert the object into a dict
output_transition_dict = output_transition_instance.to_dict()
# create an instance of OutputTransition from a dict
output_transition_form_dict = output_transition.from_dict(output_transition_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


