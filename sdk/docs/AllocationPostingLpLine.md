# AllocationPostingLpLine

One instrument event a booking writes on an investor's commitment line.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The deterministic identifier of the posting: the booking reference, investor record, commitment line, component and side. | [optional] 
**instrument** | **str** | The commitment-line instrument the event is written on. | [optional] 
**portfolio** | [**ResourceId**](ResourceId.md) |  | [optional] 
**event** | **str** | The instrument event type written, for instance CapitalCallEvent. | [optional] 
**amount** | **float** | The amount posted, in the event currency. | [optional] 
**component** | **str** | The component of the event the posting carries. | [optional] 
**investor_record_id** | **str** | The investor record the posting is for. | [optional] 
**origin_member_short_code** | **str** | The member of the structure the component originates from, when it is not the map&#39;s own member. | [optional] 
## Example

```python
from lusid.models.allocation_posting_lp_line import AllocationPostingLpLine
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: Optional[StrictStr] = "example_id"
instrument: Optional[StrictStr] = "example_instrument"
portfolio: Optional[ResourceId] = None
event: Optional[StrictStr] = "example_event"
amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
component: Optional[StrictStr] = "example_component"
investor_record_id: Optional[StrictStr] = "example_investor_record_id"
origin_member_short_code: Optional[StrictStr] = "example_origin_member_short_code"
allocation_posting_lp_line_instance = AllocationPostingLpLine(id=id, instrument=instrument, portfolio=portfolio, event=event, amount=amount, component=component, investor_record_id=investor_record_id, origin_member_short_code=origin_member_short_code)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

