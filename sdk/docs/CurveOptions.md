# CurveOptions

Options for configuring how ComplexMarketData representing a 'curve' is interpreted.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day_count_convention** | **str** | Day count convention of the curve. Defaults to \&quot;Act360\&quot;. | [optional] 
**front_extrapolation_type** | **str** | What type of extrapolation is used to build the curve Imagine that the curve is facing the observer(you), then the \&quot;front\&quot; direction is the closest point on the curve onward.  example: 0D tenor to past Defaults to \&quot;Flat\&quot;. Supported string (enumeration) values are: [None, Flat, Linear]. | [optional] 
**back_extrapolation_type** | **str** | What type of extrapolation is used to build the curve.  Imagine that the curve is facing the observer(you), then the \&quot;back\&quot; direction is the furthest point on the curve onward. example: 30Y tenor to infinity  Defaults to \&quot;Flat\&quot;. Supported string (enumeration) values are: [None, Flat, Linear]. | [optional] 
**market_data_options_type** | **str** | The available values are: CurveOptions | 
## Example

```python
from lusid.models.curve_options import CurveOptions
from typing import Any, Dict, Optional
from pydantic.v1 import Field, StrictStr, constr, validator

day_count_convention: Optional[StrictStr] = "example_day_count_convention"
front_extrapolation_type: Optional[StrictStr] = "example_front_extrapolation_type"
back_extrapolation_type: Optional[StrictStr] = "example_back_extrapolation_type"
market_data_options_type: StrictStr = "example_market_data_options_type"
curve_options_instance = CurveOptions(day_count_convention=day_count_convention, front_extrapolation_type=front_extrapolation_type, back_extrapolation_type=back_extrapolation_type, market_data_options_type=market_data_options_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

