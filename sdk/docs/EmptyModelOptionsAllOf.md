# EmptyModelOptionsAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_options_type** | **str** | The available values are: Invalid, OpaqueModelOptions, EmptyModelOptions, IndexModelOptions, FxForwardModelOptions, FundingLegModelOptions, EquityModelOptions | 

## Example

```python
from lusid.models.empty_model_options_all_of import EmptyModelOptionsAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of EmptyModelOptionsAllOf from a JSON string
empty_model_options_all_of_instance = EmptyModelOptionsAllOf.from_json(json)
# print the JSON string representation of the object
print EmptyModelOptionsAllOf.to_json()

# convert the object into a dict
empty_model_options_all_of_dict = empty_model_options_all_of_instance.to_dict()
# create an instance of EmptyModelOptionsAllOf from a dict
empty_model_options_all_of_form_dict = empty_model_options_all_of.from_dict(empty_model_options_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


