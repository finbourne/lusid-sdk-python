# InflationCurveShiftDefinition

A shift of an inflation curve, targeted by inflation index name. The shift applies to the  zero-coupon inflation swap quotes the curve was solved from and the curve re-solves with  the same seasonal factors and resolved fixings, so seasonality and the historic index path  survive the shift. Shift shapes, tenor windows, scales and the Tent pivot behave exactly  as they do on a rate curve shift.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **str** | The inflation index name the curve is keyed by, e.g. UKRPI or EUHICPXT. | 
**amount** | **float** | The size of the shift, in the units given by Scale: basis points on the zero-coupon  rates by default (50 means +50bps), or a percentage of each rate when Scale is  Percentage (1 means rates scaled by 1.01). | [optional] 
**start_tenor** | **str** |  | [optional] 
**end_tenor** | **str** |  | [optional] 
**shift_type** | **str** | Available values: Parallel, Steepen, Flatten, Twist, Tent. | 
**scale** | **str** | Available values: Bps, Percentage. | [optional] 
**pivot_tenor** | **str** | The tenor the Tent shift peaks at. The shift applies with the full Amount at this tenor,  falling linearly to zero at StartTenor and EndTenor - the key-rate triangle shape. Only  valid with ShiftType Tent; omitted, a Tent peaks at the midpoint of the window. Declared  last on purpose: generated SDKs emit their positional constructor in property-declaration  order, and this property must not shift the parameters of the ones before it. | [optional] 
**window_bounds** | **str** | Available values: Inclusive, StartExclusive, EndExclusive, Exclusive. | [optional] 
**minimum_amount_bps** | **float** | The smallest magnitude, in basis points, of the shift finally applied at each curve point,  evaluated per point AFTER the shape weight, in the direction the shift acts there. Exactly  the rate curve shift&#39;s MinimumAmountBps - see that field for the full semantics; the two  curve shifts keep one vocabulary. Omitted, no floor applies - today&#39;s behaviour.  Declared after PivotTenor on purpose, for the constructor-ordering reason given there. | [optional] 
**apply_when_value** | **str** | Available values: Any, Positive, Negative. | [optional] 
**scenario_shift_type** | **str** | Available values: RateCurveShiftDefinition, FxShiftDefinition, PriceShiftDefinition, VolSurfaceShiftDefinition, MdkrGroupShiftDefinition, InflationCurveShiftDefinition, CreditSpreadShiftDefinition, ModelOptionShiftDefinition. | 
## Example

```python
from lusid.models.inflation_curve_shift_definition import InflationCurveShiftDefinition
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

index: StrictStr = "example_index"
amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
start_tenor: Optional[StrictStr] = "example_start_tenor"
end_tenor: Optional[StrictStr] = "example_end_tenor"
shift_type: StrictStr = "example_shift_type"
scale: Optional[StrictStr] = "example_scale"
pivot_tenor: Optional[StrictStr] = "example_pivot_tenor"
window_bounds: Optional[StrictStr] = "example_window_bounds"
minimum_amount_bps: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
apply_when_value: Optional[StrictStr] = "example_apply_when_value"
scenario_shift_type: StrictStr = "example_scenario_shift_type"
inflation_curve_shift_definition_instance = InflationCurveShiftDefinition(index=index, amount=amount, start_tenor=start_tenor, end_tenor=end_tenor, shift_type=shift_type, scale=scale, pivot_tenor=pivot_tenor, window_bounds=window_bounds, minimum_amount_bps=minimum_amount_bps, apply_when_value=apply_when_value, scenario_shift_type=scenario_shift_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

