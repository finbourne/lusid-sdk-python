# EquityModelOptions

Model options for equity related pricing.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**equity_forward_projection_type** | **str** | Determines how forward equity prices should be projected.                Supported string (enumeration) values are: [FlatForwardCurveFromSpot, EquityCurveByPrices, ForwardProjectedFromRatesCurve]. | 
**model_options_type** | **str** | The available values are: Invalid, OpaqueModelOptions, EmptyModelOptions, IndexModelOptions, FxForwardModelOptions, FundingLegModelOptions, EquityModelOptions, LookUpPricingModelOptions | 

## Example

```python
from lusid.models.equity_model_options import EquityModelOptions

# TODO update the JSON string below
json = "{}"
# create an instance of EquityModelOptions from a JSON string
equity_model_options_instance = EquityModelOptions.from_json(json)
# print the JSON string representation of the object
print EquityModelOptions.to_json()

# convert the object into a dict
equity_model_options_dict = equity_model_options_instance.to_dict()
# create an instance of EquityModelOptions from a dict
equity_model_options_form_dict = equity_model_options.from_dict(equity_model_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


