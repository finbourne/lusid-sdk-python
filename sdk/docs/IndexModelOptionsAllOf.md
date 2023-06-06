# IndexModelOptionsAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**portfolio_scaling** | **str** | The available values are: Sum, AbsoluteSum, Unity | 
**model_options_type** | **str** | The available values are: Invalid, OpaqueModelOptions, EmptyModelOptions, IndexModelOptions, FxForwardModelOptions, FundingLegModelOptions, EquityModelOptions | 

## Example

```python
from lusid.models.index_model_options_all_of import IndexModelOptionsAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of IndexModelOptionsAllOf from a JSON string
index_model_options_all_of_instance = IndexModelOptionsAllOf.from_json(json)
# print the JSON string representation of the object
print IndexModelOptionsAllOf.to_json()

# convert the object into a dict
index_model_options_all_of_dict = index_model_options_all_of_instance.to_dict()
# create an instance of IndexModelOptionsAllOf from a dict
index_model_options_all_of_form_dict = index_model_options_all_of.from_dict(index_model_options_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


