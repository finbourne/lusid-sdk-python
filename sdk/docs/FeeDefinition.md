# FeeDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee_code** | **str** |  | 
**basis** | **str** | Available values: CommittedCapital, InvestedCapital, NetInvestedCapital, Nav. | 
**rate** | **float** |  | [optional] 
**tiers** | [**List[FeeSizeTier]**](FeeSizeTier.md) |  | [optional] 
**day_count_convention** | **str** |  | [optional] 
**step_down** | [**FeeStepDown**](FeeStepDown.md) |  | [optional] 
**offset_percentage** | **float** |  | [optional] 
**waiver_percentage** | **float** |  | [optional] 
## Example

```python
from lusid.models.fee_definition import FeeDefinition
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

fee_code: StrictStr = "example_fee_code"
basis: StrictStr = "example_basis"
rate: Optional[Union[StrictFloat, StrictInt]] = None
tiers: Optional[List[FeeSizeTier]] = None
day_count_convention: Optional[StrictStr] = "example_day_count_convention"
step_down: Optional[FeeStepDown] = # Replace with your value
offset_percentage: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
waiver_percentage: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
fee_definition_instance = FeeDefinition(fee_code=fee_code, basis=basis, rate=rate, tiers=tiers, day_count_convention=day_count_convention, step_down=step_down, offset_percentage=offset_percentage, waiver_percentage=waiver_percentage)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

