# FxForwardModelOptionsAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**forward_rate_observable_type** | **str** | The available values are: ForwardPoints, ForwardRate, RatesCurve, FxForwardCurve, Invalid | 
**discounting_method** | **str** | The available values are: Standard, ConstantTimeValueOfMoney, Invalid | 
**convert_to_report_ccy** | **bool** | Convert all FX flows to the report currency  By setting this all FX forwards will be priced using Forward Curves that have Report Currency as the base. | 
**model_options_type** | **str** | The available values are: Invalid, OpaqueModelOptions, EmptyModelOptions, IndexModelOptions, FxForwardModelOptions, FundingLegModelOptions, EquityModelOptions | 

## Example

```python
from lusid.models.fx_forward_model_options_all_of import FxForwardModelOptionsAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of FxForwardModelOptionsAllOf from a JSON string
fx_forward_model_options_all_of_instance = FxForwardModelOptionsAllOf.from_json(json)
# print the JSON string representation of the object
print FxForwardModelOptionsAllOf.to_json()

# convert the object into a dict
fx_forward_model_options_all_of_dict = fx_forward_model_options_all_of_instance.to_dict()
# create an instance of FxForwardModelOptionsAllOf from a dict
fx_forward_model_options_all_of_form_dict = fx_forward_model_options_all_of.from_dict(fx_forward_model_options_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


