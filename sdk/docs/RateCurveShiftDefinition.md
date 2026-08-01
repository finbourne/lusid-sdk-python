# RateCurveShiftDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ccy** | **str** |  | 
**amount** | **float** | The size of the shift, in the units given by Scale: basis points by default (50 means +50bps),  or a percentage of each rate when Scale is Percentage (1 means rates scaled by 1.01). | 
**start_tenor** | **str** |  | [optional] 
**end_tenor** | **str** |  | [optional] 
**shift_type** | **str** | Available values: Parallel, Steepen, Flatten, Twist. | 
**scale** | **str** | Available values: Bps, Percentage. | [optional] 
**scenario_shift_type** | **str** | Available values: RateCurveShiftDefinition, FxShiftDefinition, EquityShiftDefinition, VolSurfaceShiftDefinition, MdkrGroupShiftDefinition. | 
## Example

```python
from lusid.models.rate_curve_shift_definition import RateCurveShiftDefinition
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

ccy: StrictStr = "example_ccy"
amount: Union[StrictFloat, StrictInt] = # Replace with your value
start_tenor: Optional[StrictStr] = "example_start_tenor"
end_tenor: Optional[StrictStr] = "example_end_tenor"
shift_type: StrictStr = "example_shift_type"
scale: Optional[StrictStr] = "example_scale"
scenario_shift_type: StrictStr = "example_scenario_shift_type"
rate_curve_shift_definition_instance = RateCurveShiftDefinition(ccy=ccy, amount=amount, start_tenor=start_tenor, end_tenor=end_tenor, shift_type=shift_type, scale=scale, scenario_shift_type=scenario_shift_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

