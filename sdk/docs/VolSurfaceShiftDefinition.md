# VolSurfaceShiftDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument** | **str** | The market-data descriptor of the surfaces to shift, not an instrument identifier such as a LUID.  For an equity vol surface this is the underlier code the surface was mastered against (e.g. &#39;TSLA&#39;  for market asset &#39;TSLA/USD/LN&#39;); for an interest rate vol surface it is the currency (e.g. &#39;USD&#39;);  for an FX vol surface it is the currency pair (e.g. &#39;GBP/USD&#39;). The wildcard &#39;EquityVol.*&#39; widens  the shift to every equity vol surface in the valuation; interest rate and FX vol surfaces cannot  be widened, since neither a currency nor a currency pair names a set of instruments. | 
**amount** | **float** |  | [optional] 
**strike** | **float** |  | [optional] 
**expiry** | **str** | The expiry of the surface points the shift applies to, resolved against the valuation  date. A whole number of units, in any case: BD (business day), D, W, M, Q or Qtr, SA  (semi-annual), Y or A - for example \&quot;1BD\&quot;, \&quot;3m\&quot;, \&quot;6M\&quot;, \&quot;1Qtr\&quot;, \&quot;5y\&quot;. Omitted, every  expiry on the surface is shifted. | [optional] 
**shift_type** | **str** | Available values: Absolute, Relative. | 
**scenario_shift_type** | **str** | Available values: RateCurveShiftDefinition, FxShiftDefinition, PriceShiftDefinition, VolSurfaceShiftDefinition, MdkrGroupShiftDefinition, InflationCurveShiftDefinition, CreditSpreadShiftDefinition, ModelOptionShiftDefinition. | 
## Example

```python
from lusid.models.vol_surface_shift_definition import VolSurfaceShiftDefinition
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

instrument: StrictStr = "example_instrument"
amount: Optional[Union[StrictFloat, StrictInt]] = None
strike: Optional[Union[StrictFloat, StrictInt]] = None
expiry: Optional[StrictStr] = "example_expiry"
shift_type: StrictStr = "example_shift_type"
scenario_shift_type: StrictStr = "example_scenario_shift_type"
vol_surface_shift_definition_instance = VolSurfaceShiftDefinition(instrument=instrument, amount=amount, strike=strike, expiry=expiry, shift_type=shift_type, scenario_shift_type=scenario_shift_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

