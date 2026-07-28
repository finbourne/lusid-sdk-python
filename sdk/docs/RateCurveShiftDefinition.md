# RateCurveShiftDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ccy** | **str** |  | 
**amount** | **float** |  | 
**start_tenor** | **str** |  | [optional] 
**end_tenor** | **str** |  | [optional] 
**shift_type** | **str** | Available values: Parallel, Steepen, Flatten, Twist. | 
**scenario_shift_type** | **str** | Available values: RateCurveShiftDefinition, FxShiftDefinition, EquityShiftDefinition, VolSurfaceShiftDefinition. | 
## Example

```python
from lusid.models.rate_curve_shift_definition import RateCurveShiftDefinition
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

ccy: StrictStr = "example_ccy"
amount: Union[StrictFloat, StrictInt]
start_tenor: Optional[StrictStr] = "example_start_tenor"
end_tenor: Optional[StrictStr] = "example_end_tenor"
shift_type: StrictStr = "example_shift_type"
scenario_shift_type: StrictStr = "example_scenario_shift_type"
rate_curve_shift_definition_instance = RateCurveShiftDefinition(ccy=ccy, amount=amount, start_tenor=start_tenor, end_tenor=end_tenor, shift_type=shift_type, scenario_shift_type=scenario_shift_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

