# AllocationEvent

One economic event shared across the participants of an Allocation Map: raised as a draft, computed into  per-investor shares, and finally booked.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**id** | [**ResourceId**](ResourceId.md) |  | 
**description** | **str** | A description of the Allocation Event. | [optional] 
**allocation_map_id** | [**ResourceId**](ResourceId.md) |  | 
**event_type** | **str** | The type of the event: CapitalCall, Distribution, FeeExpense or ValuationMove. Selects the basis rule from the map. Available values: CapitalCall, Distribution, FeeExpense, ValuationMove. | 
**amount** | **float** | The total amount to be shared across the participants. | 
**currency** | **str** | The ISO 4217 code of the currency of the amount. The amount may not be finer than the currency&#39;s minor unit: two decimal places for most currencies, none for JPY, three for KWD and BHD. A code with no defined minor unit, such as XAU or XAG, is taken to have two decimal places. | 
**event_date** | **datetime** | The date of the event: the point at which the map, its participants and their basis values are read. | 
**status** | **str** | The lifecycle status of the event: Draft until its shares are computed, Computed once they are, and Booked once posted. Available values: Draft, Computed, Booked. | 
**basis_source** | **str** | Where the basis values came from when the shares were last computed. | [optional] 
**allocations** | [**List[AllocationMapAllocation]**](AllocationMapAllocation.md) | The per-investor shares of the amount, as last computed. | 
**booking_reference** | **str** | The reference under which the shares were posted. Set only once the event is booked. | [optional] 
**booked_at** | **datetime** | The datetime at which the event was booked. | [optional] 
**reallocation_reason** | **str** | The reason given when the event was last recomputed, if it has been. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.allocation_event import AllocationEvent
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

href: Optional[StrictStr] = "example_href"
id: ResourceId
description: Optional[StrictStr] = "example_description"
allocation_map_id: ResourceId = # Replace with your value
event_type: StrictStr = "example_event_type"
amount: Union[StrictFloat, StrictInt] = # Replace with your value
currency: StrictStr = "example_currency"
event_date: datetime = # Replace with your value
status: StrictStr = "example_status"
basis_source: Optional[StrictStr] = "example_basis_source"
allocations: List[AllocationMapAllocation] = # Replace with your value
booking_reference: Optional[StrictStr] = "example_booking_reference"
booked_at: Optional[datetime] = # Replace with your value
reallocation_reason: Optional[StrictStr] = "example_reallocation_reason"
version: Optional[Version] = None
links: Optional[List[Link]] = None
allocation_event_instance = AllocationEvent(href=href, id=id, description=description, allocation_map_id=allocation_map_id, event_type=event_type, amount=amount, currency=currency, event_date=event_date, status=status, basis_source=basis_source, allocations=allocations, booking_reference=booking_reference, booked_at=booked_at, reallocation_reason=reallocation_reason, version=version, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

