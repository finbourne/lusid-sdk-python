# IndexModelOptions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**portfolio_scaling** | **str** | The available values are: Sum, AbsoluteSum, Unity | 
**model_options_type** | **str** | The available values are: Invalid, OpaqueModelOptions, EmptyModelOptions, IndexModelOptions, FxForwardModelOptions, FundingLegModelOptions, EquityModelOptions | 

## Example

```python
from lusid.models.index_model_options import IndexModelOptions

# TODO update the JSON string below
json = "{}"
# create an instance of IndexModelOptions from a JSON string
index_model_options_instance = IndexModelOptions.from_json(json)
# print the JSON string representation of the object
print IndexModelOptions.to_json()

# convert the object into a dict
index_model_options_dict = index_model_options_instance.to_dict()
# create an instance of IndexModelOptions from a dict
index_model_options_form_dict = index_model_options.from_dict(index_model_options_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


