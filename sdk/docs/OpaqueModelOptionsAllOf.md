# OpaqueModelOptionsAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **Dict[str, object]** |  | 
**model_options_type** | **str** | The available values are: Invalid, OpaqueModelOptions, EmptyModelOptions, IndexModelOptions, FxForwardModelOptions, FundingLegModelOptions, EquityModelOptions | 

## Example

```python
from lusid.models.opaque_model_options_all_of import OpaqueModelOptionsAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of OpaqueModelOptionsAllOf from a JSON string
opaque_model_options_all_of_instance = OpaqueModelOptionsAllOf.from_json(json)
# print the JSON string representation of the object
print OpaqueModelOptionsAllOf.to_json()

# convert the object into a dict
opaque_model_options_all_of_dict = opaque_model_options_all_of_instance.to_dict()
# create an instance of OpaqueModelOptionsAllOf from a dict
opaque_model_options_all_of_form_dict = opaque_model_options_all_of.from_dict(opaque_model_options_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


