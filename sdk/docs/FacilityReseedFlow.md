# FacilityReseedFlow

A draw or repayment booked on a Facility, as a re-seed reads it.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | **str** | The event that booked the draw or repayment. | 
**var_date** | **datetime** | The date the draw or repayment takes effect. | 
**amount** | **float** | The amount drawn or repaid. | 
**currency** | **str** | The currency the amount was booked in. | 
**is_draw** | **bool** | Whether the flow draws the Facility rather than repaying it. | 
**allocation_map_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**structure_member_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**reason** | **str** | Why the flow cannot be attributed to the Fund: its allocation map&#39;s structureMemberId is not the map&#39;s member fund. Present for an unattributable flow. | [optional] 
## Example

```python
from lusid.models.facility_reseed_flow import FacilityReseedFlow
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

event: StrictStr = "example_event"
var_date: datetime = # Replace with your value
amount: Union[StrictFloat, StrictInt] = # Replace with your value
currency: StrictStr = "example_currency"
is_draw: StrictBool = # Replace with your value
is_draw:StrictBool = True
allocation_map_id: Optional[ResourceId] = # Replace with your value
structure_member_id: Optional[ResourceId] = # Replace with your value
reason: Optional[StrictStr] = "example_reason"
facility_reseed_flow_instance = FacilityReseedFlow(event=event, var_date=var_date, amount=amount, currency=currency, is_draw=is_draw, allocation_map_id=allocation_map_id, structure_member_id=structure_member_id, reason=reason)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

