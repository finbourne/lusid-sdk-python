# PriceShiftDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument** | **str** |  | 
**amount** | **float** |  | 
**shift_type** | **str** | Available values: Absolute, Relative, Percentage. | 
**quote_type** | **str** | Available values: Price, Spread, Rate, LogNormalVol, NormalVol, ParSpread, IsdaSpread, Upfront, Index, Ratio, Delta, PoolFactor, InflationAssumption, DirtyPrice, PrincipalWriteOff, InterestDeferred, InterestShortfall, ConstituentWeightFactor. | [optional] 
**scenario_shift_type** | **str** | Available values: RateCurveShiftDefinition, FxShiftDefinition, PriceShiftDefinition, VolSurfaceShiftDefinition, MdkrGroupShiftDefinition. | 
## Example

```python
from lusid.models.price_shift_definition import PriceShiftDefinition
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

instrument: StrictStr = "example_instrument"
amount: Union[StrictFloat, StrictInt]
shift_type: StrictStr = "example_shift_type"
quote_type: Optional[StrictStr] = "example_quote_type"
scenario_shift_type: StrictStr = "example_scenario_shift_type"
price_shift_definition_instance = PriceShiftDefinition(instrument=instrument, amount=amount, shift_type=shift_type, quote_type=quote_type, scenario_shift_type=scenario_shift_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

