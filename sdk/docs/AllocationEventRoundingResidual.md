# AllocationEventRoundingResidual

The cents left over when one component of an Allocation Event was rounded to the currency's minor unit, and where they went.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component** | **str** | The component the residual belongs to. | [optional] 
**cents** | **int** | The number of minor units left over after each share was truncated to the currency. | [optional] 
**amount** | **float** | The same, in the event currency. | [optional] 
**method** | **str** | How the leftover was placed: LargestRemainder spreads it one minor unit at a time over the largest remainders; RoundingPartner gives all of it to the map&#39;s rounding partner line. Available values: LargestRemainder, RoundingPartner. | [optional] 
**taken_by** | **List[str]** | The investor records that each took a minor unit, in the order they took it. | [optional] 
## Example

```python
from lusid.models.allocation_event_rounding_residual import AllocationEventRoundingResidual
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

component: Optional[StrictStr] = "example_component"
cents: Optional[StrictInt] = # Replace with your value
cents: Optional[StrictInt] = None
amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
method: Optional[StrictStr] = "example_method"
taken_by: Optional[List[StrictStr]] = # Replace with your value
allocation_event_rounding_residual_instance = AllocationEventRoundingResidual(component=component, cents=cents, amount=amount, method=method, taken_by=taken_by)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

