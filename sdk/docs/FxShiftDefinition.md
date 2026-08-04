# FxShiftDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_pair** | **str** |  | 
**amount** | **float** |  | 
**shift_type** | **str** | Available values: Absolute, Relative, Percentage. | 
**scenario_shift_type** | **str** | Available values: RateCurveShiftDefinition, FxShiftDefinition, PriceShiftDefinition, VolSurfaceShiftDefinition, MdkrGroupShiftDefinition. | 
## Example

```python
from lusid.models.fx_shift_definition import FxShiftDefinition
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

currency_pair: StrictStr = "example_currency_pair"
amount: Union[StrictFloat, StrictInt]
shift_type: StrictStr = "example_shift_type"
scenario_shift_type: StrictStr = "example_scenario_shift_type"
fx_shift_definition_instance = FxShiftDefinition(currency_pair=currency_pair, amount=amount, shift_type=shift_type, scenario_shift_type=scenario_shift_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

