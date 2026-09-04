# RateCurveShiftDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ccy** | **str** |  | 
**amount** | **float** | The size of the shift, in the units given by Scale: basis points by default (50 means +50bps),  or a percentage of each rate when Scale is Percentage (1 means rates scaled by 1.01). | [optional] 
**start_tenor** | **str** |  | [optional] 
**end_tenor** | **str** |  | [optional] 
**shift_type** | **str** | Available values: Parallel, Steepen, Flatten, Twist, Tent. | 
**scale** | **str** | Available values: Bps, Percentage. | [optional] 
**apply_to** | **str** | A LUSID filter expression over the instrument entity scoping which instruments this shift is  for, e.g. \&quot;properties[Instrument/default/CountryOfIssue] eq &#39;Italy&#39;\&quot;. The shifted market data  is used by the whole valuation run, but when the scenario is requested as a result column the  column is only populated for matching instruments. Only usable when the scenario is applied as  a per-metric column. Note that with a scope set, the base and scenario columns cover different  instrument populations: an aggregate (e.g. Sum) of the scenario column totals only the matching  instruments, so it is not directly comparable to the same aggregate of the base column. | [optional] 
**pivot_tenor** | **str** | The tenor the Tent shift peaks at. The shift applies with the full Amount at this tenor,  falling linearly to zero at StartTenor and EndTenor - the key-rate triangle shape, whose  asymmetry matters because key-rate buckets are rarely evenly spaced. Only valid with  ShiftType Tent; omitted, a Tent peaks at the midpoint of the window. Declared last on  purpose: generated SDKs emit their positional constructor in property-declaration order,  and this property must not shift the parameters of the ones before it.  Over a window containing a single curve point, that point takes the full Amount regardless  of where the pivot lands: a one-point window has no slope to express, and every shift  shape degenerates the same way there. | [optional] 
**window_bounds** | **str** | Available values: Inclusive, StartExclusive, EndExclusive, Exclusive. | [optional] 
**curve_name** | **str** | The funding identifier of the one curve in the currency this shift targets, letting a  scenario shock a named curve (say, an issuer discounting curve) without also moving the  risk-free curve mastered in the same currency. Omitted - as on every scenario stored  before this field existed - the shift matches every rate curve in the currency, exactly  as before. Declared last on purpose: generated SDKs emit their positional constructor in  property-declaration order, and this property must not shift the parameters of the ones  before it. | [optional] 
**minimum_amount_bps** | **float** | The smallest magnitude, in basis points, of the shift finally applied at each curve point.  Evaluated per point AFTER the shape weight, in the direction the shift acts there (the sign  of Amount times the shape weight): the applied move becomes at least the minimum in that  direction, even where a Percentage shift on a negative rate would have pointed the other  way - the Solvency II up-shock&#39;s \&quot;at least one percentage point at any maturity\&quot; is  MinimumAmountBps &#x3D; 100 on the relative shift the regulation states. A point whose shape  weight is exactly zero stays unshifted: the floor strengthens a shock where the shape  applies one, it does not extend the shock to points the shape excludes (a Tent&#39;s window  ends remain unmoved). Deliberately in basis points rather than in Scale units, because the  floor and the shift are in different units by construction: the regulation states a  relative shock with an absolute floor. Omitted, no floor applies - today&#39;s behaviour.  Declared after PivotTenor on purpose, for the constructor-ordering reason given there. | [optional] 
**apply_when_value** | **str** | Available values: Any, Positive, Negative. | [optional] 
**scenario_shift_type** | **str** | Available values: RateCurveShiftDefinition, FxShiftDefinition, PriceShiftDefinition, VolSurfaceShiftDefinition, MdkrGroupShiftDefinition, InflationCurveShiftDefinition, CreditSpreadShiftDefinition, ModelOptionShiftDefinition. | 
## Example

```python
from lusid.models.rate_curve_shift_definition import RateCurveShiftDefinition
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

ccy: StrictStr = "example_ccy"
amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
start_tenor: Optional[StrictStr] = "example_start_tenor"
end_tenor: Optional[StrictStr] = "example_end_tenor"
shift_type: StrictStr = "example_shift_type"
scale: Optional[StrictStr] = "example_scale"
apply_to: Optional[StrictStr] = "example_apply_to"
pivot_tenor: Optional[StrictStr] = "example_pivot_tenor"
window_bounds: Optional[StrictStr] = "example_window_bounds"
curve_name: Optional[StrictStr] = "example_curve_name"
minimum_amount_bps: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
apply_when_value: Optional[StrictStr] = "example_apply_when_value"
scenario_shift_type: StrictStr = "example_scenario_shift_type"
rate_curve_shift_definition_instance = RateCurveShiftDefinition(ccy=ccy, amount=amount, start_tenor=start_tenor, end_tenor=end_tenor, shift_type=shift_type, scale=scale, apply_to=apply_to, pivot_tenor=pivot_tenor, window_bounds=window_bounds, curve_name=curve_name, minimum_amount_bps=minimum_amount_bps, apply_when_value=apply_when_value, scenario_shift_type=scenario_shift_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

