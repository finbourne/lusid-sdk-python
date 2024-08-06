# FxForwardModelOptions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**forward_rate_observable_type** | **str** | The available values are: ForwardPoints, ForwardRate, RatesCurve, FxForwardCurve, Invalid | 
**discounting_method** | **str** | The available values are: Standard, ConstantTimeValueOfMoney, Invalid | 
**convert_to_report_ccy** | **bool** | Convert all FX flows to the report currency  By setting this all FX forwards will be priced using Forward Curves that have Report Currency as the base. | 
**model_options_type** | **str** | The available values are: Invalid, OpaqueModelOptions, EmptyModelOptions, IndexModelOptions, FxForwardModelOptions, FundingLegModelOptions, EquityModelOptions | 

## Example

```python
from lusid.models.fx_forward_model_options import FxForwardModelOptions

# TODO update the JSON string below
json = "{}"
# create an instance of FxForwardModelOptions from a JSON string
fx_forward_model_options_instance = FxForwardModelOptions.from_json(json)
# print the JSON string representation of the object
print FxForwardModelOptions.to_json()

# convert the object into a dict
fx_forward_model_options_dict = fx_forward_model_options_instance.to_dict()
# create an instance of FxForwardModelOptions from a dict
fx_forward_model_options_form_dict = fx_forward_model_options.from_dict(fx_forward_model_options_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


