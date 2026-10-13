# AllocationPostingPlan

Everything booking an Allocation Event writes, in write order: the investors' lines, the roll-ups above them and  the fund side. Returned by a dry run, so a caller sees exactly what a booking would post before it does.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lp_side** | [**List[AllocationPostingLpLine]**](AllocationPostingLpLine.md) | The instrument events written on each investor&#39;s commitment line, one per component. | [optional] 
**roll_ups** | [**List[AllocationPostingRollUp]**](AllocationPostingRollUp.md) | The roll-ups written on each vehicle&#39;s line on the register above it, summing the lines beneath. | [optional] 
**fund_side** | [**List[AllocationPostingFundLine]**](AllocationPostingFundLine.md) | The transactions written on the fund&#39;s own books. | [optional] 
**counts** | [**AllocationPostingCounts**](AllocationPostingCounts.md) |  | [optional] 
**warnings** | [**List[AllocationEventBookingWarning]**](AllocationEventBookingWarning.md) | The validation rules the booking would be allowed to proceed through under the map&#39;s policy. | [optional] 
## Example

```python
from lusid.models.allocation_posting_plan import AllocationPostingPlan
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

lp_side: Optional[List[AllocationPostingLpLine]] = # Replace with your value
roll_ups: Optional[List[AllocationPostingRollUp]] = # Replace with your value
fund_side: Optional[List[AllocationPostingFundLine]] = # Replace with your value
counts: Optional[AllocationPostingCounts] = None
warnings: Optional[List[AllocationEventBookingWarning]] = # Replace with your value
allocation_posting_plan_instance = AllocationPostingPlan(lp_side=lp_side, roll_ups=roll_ups, fund_side=fund_side, counts=counts, warnings=warnings)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

