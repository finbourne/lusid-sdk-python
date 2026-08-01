# EquityShiftDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument** | **str** |  | 
**amount** | **float** |  | 
**shift_type** | **str** | Available values: Absolute, Relative, Percentage. | 
**scenario_shift_type** | **str** | Available values: RateCurveShiftDefinition, FxShiftDefinition, EquityShiftDefinition, VolSurfaceShiftDefinition, MdkrGroupShiftDefinition. | 
## Example

```python
from lusid.models.equity_shift_definition import EquityShiftDefinition
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

instrument: StrictStr = "example_instrument"
amount: Union[StrictFloat, StrictInt]
shift_type: StrictStr = "example_shift_type"
scenario_shift_type: StrictStr = "example_scenario_shift_type"
equity_shift_definition_instance = EquityShiftDefinition(instrument=instrument, amount=amount, shift_type=shift_type, scenario_shift_type=scenario_shift_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

