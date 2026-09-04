# CreditSpreadShiftDefinition

A shift of a credit spread curve, targeted by the ticker of the reference entity and,  optionally, the currency the curve is quoted in. The shift applies to the par spread quotes  the curve carries, so a basis-point amount means basis points of spread - the units a spread  shock is quoted in. Shift shapes, tenor windows, scales and the Tent pivot behave exactly as  they do on a rate curve shift.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ticker** | **str** | The ticker of the reference entity whose spread curve is shifted. | 
**ccy** | **str** | The currency the curve is quoted in; disambiguates a ticker quoted in more than one  currency. Omitted, the shift matches the ticker in every currency. | [optional] 
**amount** | **float** | The size of the shift, in the units given by Scale: basis points of spread by default  (50 means +50bps), or a percentage of each spread when Scale is Percentage (1 means  spreads scaled by 1.01). | [optional] 
**start_tenor** | **str** |  | [optional] 
**end_tenor** | **str** |  | [optional] 
**shift_type** | **str** | Available values: Parallel, Steepen, Flatten, Twist, Tent. | 
**scale** | **str** | Available values: Bps, Percentage. | [optional] 
**pivot_tenor** | **str** | The tenor the Tent shift peaks at. The shift applies with the full Amount at this tenor,  falling linearly to zero at StartTenor and EndTenor - the key-rate triangle shape. Only  valid with ShiftType Tent; omitted, a Tent peaks at the midpoint of the window. Declared  last on purpose: generated SDKs emit their positional constructor in property-declaration  order, and this property must not shift the parameters of the ones before it. | [optional] 
**minimum_amount_bps** | **float** | The smallest magnitude, in basis points, of the shift finally applied at each curve point,  evaluated per point AFTER the shape weight, in the direction the shift acts there. Exactly  the rate curve shift&#39;s MinimumAmountBps - see that field for the full semantics; the  curve shifts keep one vocabulary. Omitted, no floor applies - today&#39;s behaviour.  Declared after PivotTenor on purpose, for the constructor-ordering reason given there. | [optional] 
**apply_when_value** | **str** | Available values: Any, Positive, Negative. | [optional] 
**scenario_shift_type** | **str** | Available values: RateCurveShiftDefinition, FxShiftDefinition, PriceShiftDefinition, VolSurfaceShiftDefinition, MdkrGroupShiftDefinition, InflationCurveShiftDefinition, CreditSpreadShiftDefinition, ModelOptionShiftDefinition. | 
## Example

```python
from lusid.models.credit_spread_shift_definition import CreditSpreadShiftDefinition
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

ticker: StrictStr = "example_ticker"
ccy: Optional[StrictStr] = "example_ccy"
amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
start_tenor: Optional[StrictStr] = "example_start_tenor"
end_tenor: Optional[StrictStr] = "example_end_tenor"
shift_type: StrictStr = "example_shift_type"
scale: Optional[StrictStr] = "example_scale"
pivot_tenor: Optional[StrictStr] = "example_pivot_tenor"
minimum_amount_bps: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
apply_when_value: Optional[StrictStr] = "example_apply_when_value"
scenario_shift_type: StrictStr = "example_scenario_shift_type"
credit_spread_shift_definition_instance = CreditSpreadShiftDefinition(ticker=ticker, ccy=ccy, amount=amount, start_tenor=start_tenor, end_tenor=end_tenor, shift_type=shift_type, scale=scale, pivot_tenor=pivot_tenor, minimum_amount_bps=minimum_amount_bps, apply_when_value=apply_when_value, scenario_shift_type=scenario_shift_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

