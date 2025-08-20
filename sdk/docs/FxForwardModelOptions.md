# FxForwardModelOptions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**forward_rate_observable_type** | **str** | The available values are: ForwardPoints, ForwardRate, RatesCurve, FxForwardCurve, Invalid | 
**discounting_method** | **str** | The available values are: Standard, ConstantTimeValueOfMoney, Invalid | 
**convert_to_report_ccy** | **bool** | Convert all FX flows to the report currency By setting this all FX forwards will be priced using Forward Curves that have Report Currency as the base. | 
**model_options_type** | **str** | The available values are: Invalid, OpaqueModelOptions, EmptyModelOptions, IndexModelOptions, FxForwardModelOptions, FundingLegModelOptions, EquityModelOptions, CdsModelOptions | 
## Example

```python
from lusid.models.fx_forward_model_options import FxForwardModelOptions
from typing import Any, Dict
from pydantic.v1 import Field, StrictBool, StrictStr, validator

forward_rate_observable_type: StrictStr = "example_forward_rate_observable_type"
discounting_method: StrictStr = "example_discounting_method"
convert_to_report_ccy: StrictBool = # Replace with your value
convert_to_report_ccy:StrictBool = True
model_options_type: StrictStr = "example_model_options_type"
fx_forward_model_options_instance = FxForwardModelOptions(forward_rate_observable_type=forward_rate_observable_type, discounting_method=discounting_method, convert_to_report_ccy=convert_to_report_ccy, model_options_type=model_options_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

