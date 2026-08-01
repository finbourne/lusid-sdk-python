# VolSurfaceShiftDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument** | **str** |  | 
**amount** | **float** |  | 
**strike** | **float** |  | [optional] 
**expiry** | **str** |  | [optional] 
**shift_type** | **str** | Available values: Absolute, Relative. | 
**scenario_shift_type** | **str** | Available values: RateCurveShiftDefinition, FxShiftDefinition, EquityShiftDefinition, VolSurfaceShiftDefinition, MdkrGroupShiftDefinition. | 
## Example

```python
from lusid.models.vol_surface_shift_definition import VolSurfaceShiftDefinition
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

instrument: StrictStr = "example_instrument"
amount: Union[StrictFloat, StrictInt]
strike: Optional[Union[StrictFloat, StrictInt]] = None
expiry: Optional[StrictStr] = "example_expiry"
shift_type: StrictStr = "example_shift_type"
scenario_shift_type: StrictStr = "example_scenario_shift_type"
vol_surface_shift_definition_instance = VolSurfaceShiftDefinition(instrument=instrument, amount=amount, strike=strike, expiry=expiry, shift_type=shift_type, scenario_shift_type=scenario_shift_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

