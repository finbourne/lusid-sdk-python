# EmptyModelOptions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_options_type** | **str** | The available values are: Invalid, OpaqueModelOptions, EmptyModelOptions, IndexModelOptions, FxForwardModelOptions, FundingLegModelOptions, EquityModelOptions | 

## Example

```python
from lusid.models.empty_model_options import EmptyModelOptions

# TODO update the JSON string below
json = "{}"
# create an instance of EmptyModelOptions from a JSON string
empty_model_options_instance = EmptyModelOptions.from_json(json)
# print the JSON string representation of the object
print EmptyModelOptions.to_json()

# convert the object into a dict
empty_model_options_dict = empty_model_options_instance.to_dict()
# create an instance of EmptyModelOptions from a dict
empty_model_options_form_dict = empty_model_options.from_dict(empty_model_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


