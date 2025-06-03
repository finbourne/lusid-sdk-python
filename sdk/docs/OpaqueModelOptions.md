# OpaqueModelOptions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **Dict[str, object]** |  | 
**model_options_type** | **str** | The available values are: Invalid, OpaqueModelOptions, EmptyModelOptions, IndexModelOptions, FxForwardModelOptions, FundingLegModelOptions, EquityModelOptions, CdsModelOptions | 

## Example

```python
from lusid.models.opaque_model_options import OpaqueModelOptions

# TODO update the JSON string below
json = "{}"
# create an instance of OpaqueModelOptions from a JSON string
opaque_model_options_instance = OpaqueModelOptions.from_json(json)
# print the JSON string representation of the object
print OpaqueModelOptions.to_json()

# convert the object into a dict
opaque_model_options_dict = opaque_model_options_instance.to_dict()
# create an instance of OpaqueModelOptions from a dict
opaque_model_options_form_dict = opaque_model_options.from_dict(opaque_model_options_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


