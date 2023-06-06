# ModelOptions

Base class for representing model options in LUSID, which provide config for instrument analytics.  This base class should not be directly instantiated; each supported ModelOptionsType has a corresponding inherited class.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_options_type** | **str** | The available values are: Invalid, OpaqueModelOptions, EmptyModelOptions, IndexModelOptions, FxForwardModelOptions, FundingLegModelOptions, EquityModelOptions | 

## Example

```python
from lusid.models.model_options import ModelOptions

# TODO update the JSON string below
json = "{}"
# create an instance of ModelOptions from a JSON string
model_options_instance = ModelOptions.from_json(json)
# print the JSON string representation of the object
print ModelOptions.to_json()

# convert the object into a dict
model_options_dict = model_options_instance.to_dict()
# create an instance of ModelOptions from a dict
model_options_form_dict = model_options.from_dict(model_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


