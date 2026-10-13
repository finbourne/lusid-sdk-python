# FeeStepDown

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trigger** | **str** | Available values: EndOfInvestmentPeriod, Date, Closing. | 
**step_down_date** | **datetime** |  | [optional] 
**closing_id** | **str** |  | [optional] 
**rate** | **float** |  | [optional] 
**basis** | **str** | Available values: CommittedCapital, InvestedCapital, NetInvestedCapital, Nav. | [optional] 
## Example

```python
from lusid.models.fee_step_down import FeeStepDown
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

trigger: StrictStr = "example_trigger"
step_down_date: Optional[datetime] = # Replace with your value
closing_id: Optional[StrictStr] = "example_closing_id"
rate: Optional[Union[StrictFloat, StrictInt]] = None
basis: Optional[StrictStr] = "example_basis"
fee_step_down_instance = FeeStepDown(trigger=trigger, step_down_date=step_down_date, closing_id=closing_id, rate=rate, basis=basis)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

