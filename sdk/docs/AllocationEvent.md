# AllocationEvent

One economic event shared across the participants of an Allocation Map: raised as a draft, computed into  per-investor shares, and finally booked.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**id** | [**ResourceId**](ResourceId.md) |  | 
**description** | **str** | A description of the Allocation Event. | [optional] 
**allocation_map_id** | [**ResourceId**](ResourceId.md) |  | 
**event_type** | **str** | The type of the event: CapitalCall, Distribution, FeeExpense, ValuationMove, Equalisation, RecallExpiry, Transfer, Default, Commitment or DealFunding. Selects the basis rule from the map. A recall is a CapitalCall with a Recall component. A Commitment event is not shared from a basis: its basis values are the signed commitment amounts per commitment line, and they must sum to the amount. Available values: CapitalCall, Distribution, FeeExpense, ValuationMove, Commitment, Equalisation, RecallExpiry, Transfer, Default, DealFunding. | 
**amount** | **float** | The total amount to be shared across the participants. | 
**currency** | **str** | The ISO 4217 code of the currency of the amount. The amount may not be finer than the currency&#39;s minor unit: two decimal places for most currencies, none for JPY, three for KWD and BHD. A code with no defined minor unit, such as XAU or XAG, is taken to have two decimal places. | 
**event_date** | **datetime** | The date of the event: the point at which the map, its participants and their basis values are read. | 
**status** | **str** | The lifecycle status of the event: Draft until its shares are computed, Computed once they are, Booking while its postings are being written, Booked once they all are, and Reversed once a booked event has been backed out. Available values: Draft, Computed, Booked, Booking, Reversed. | 
**basis_source** | **str** | Where the basis values came from when the shares were last computed. | [optional] 
**allocations** | [**List[AllocationMapAllocation]**](AllocationMapAllocation.md) | The per-investor shares of the amount, as last computed. | 
**booking_reference** | **str** | The reference under which the shares were posted. Set only once the event is booked. | [optional] 
**booked_at** | **datetime** | The datetime at which the event was booked. | [optional] 
**reallocation_reason** | **str** | The reason given when the event was last recomputed, if it has been. | [optional] 
**components** | [**List[AllocationEventComponent]**](AllocationEventComponent.md) | The parts the amount splits into, each shared on its own basis and booked to its own slot. The component amounts must sum to the event amount. Absent means the whole amount is one component: Investment for a CapitalCall, ROC for a Distribution. | [optional] 
**residuals** | [**List[AllocationEventRoundingResidual]**](AllocationEventRoundingResidual.md) | The minor units left over when each component&#39;s shares were rounded to the currency, and which investor records took them. | [optional] 
**basis_diagnostics** | [**AllocationEventBasisDiagnostics**](AllocationEventBasisDiagnostics.md) |  | [optional] 
**written_ids** | **List[str]** | The identifiers of the postings the booking has written so far, in write order. Complete once the event is Booked. | [optional] 
**booking_errors** | [**List[AllocationEventBookingError]**](AllocationEventBookingError.md) | The postings the booking could not write. Non-empty leaves the event in Booking; book again under the same reference to resume, or unbook to cancel what was written. | [optional] 
**warnings** | [**List[AllocationEventBookingWarning]**](AllocationEventBookingWarning.md) | The validation rules the booking was allowed to proceed through under the map&#39;s policy, for instance an OverCall on a map that warns rather than refuses. Kept for the life of the event. | [optional] 
**transfers** | [**List[AllocationEventTransfer]**](AllocationEventTransfer.md) | For a Transfer event, the legs to book: each moves a fraction of one capital interest line to another. Required for a Transfer event and not allowed on any other type. The fractions out of one line must sum to at most one; the amount of a Transfer event is zero. | [optional] 
**equalisation** | [**AllocationEventEqualisation**](AllocationEventEqualisation.md) |  | [optional] 
**use_of_proceeds** | [**List[AllocationEventUseOfProceeds]**](AllocationEventUseOfProceeds.md) | For a CapitalCall, what the call pays for: rows of purpose, deal and amount that sum to the call amount. An Investment row names a deal the vehicle has funded and is shared under that deal&#39;s participation, with each investor&#39;s share recorded as paid in for that deal; when the deal was funded from a facility the row repays the draw. Not allowed with components or on any other event type. | [optional] 
**deal_funding** | [**AllocationEventDealFunding**](AllocationEventDealFunding.md) |  | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**parent_allocation_event_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**replaces** | [**ResourceId**](ResourceId.md) |  | [optional] 
**reversal** | [**AllocationEventReversal**](AllocationEventReversal.md) |  | [optional] 
**notice_date** | **datetime** | The date the notice went to investors. | [optional] 
**due_date** | **datetime** | The date the investors&#39; cash is due. | [optional] 
**settlement_date** | **datetime** | The date the postings settle. Defaults to the event date. | [optional] 
**receipts** | [**List[AllocationEventReceipt]**](AllocationEventReceipt.md) | The cash received against the event, in the order it was recorded. | [optional] 
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
components: Optional[List[AllocationEventComponent]] = # Replace with your value
residuals: Optional[List[AllocationEventRoundingResidual]] = # Replace with your value
basis_diagnostics: Optional[AllocationEventBasisDiagnostics] = # Replace with your value
written_ids: Optional[List[StrictStr]] = # Replace with your value
booking_errors: Optional[List[AllocationEventBookingError]] = # Replace with your value
warnings: Optional[List[AllocationEventBookingWarning]] = # Replace with your value
transfers: Optional[List[AllocationEventTransfer]] = # Replace with your value
equalisation: Optional[AllocationEventEqualisation] = None
use_of_proceeds: Optional[List[AllocationEventUseOfProceeds]] = # Replace with your value
deal_funding: Optional[AllocationEventDealFunding] = # Replace with your value
version: Optional[Version] = None
parent_allocation_event_id: Optional[ResourceId] = # Replace with your value
replaces: Optional[ResourceId] = None
reversal: Optional[AllocationEventReversal] = None
notice_date: Optional[datetime] = # Replace with your value
due_date: Optional[datetime] = # Replace with your value
settlement_date: Optional[datetime] = # Replace with your value
receipts: Optional[List[AllocationEventReceipt]] = # Replace with your value
links: Optional[List[Link]] = None
allocation_event_instance = AllocationEvent(href=href, id=id, description=description, allocation_map_id=allocation_map_id, event_type=event_type, amount=amount, currency=currency, event_date=event_date, status=status, basis_source=basis_source, allocations=allocations, booking_reference=booking_reference, booked_at=booked_at, reallocation_reason=reallocation_reason, components=components, residuals=residuals, basis_diagnostics=basis_diagnostics, written_ids=written_ids, booking_errors=booking_errors, warnings=warnings, transfers=transfers, equalisation=equalisation, use_of_proceeds=use_of_proceeds, deal_funding=deal_funding, version=version, parent_allocation_event_id=parent_allocation_event_id, replaces=replaces, reversal=reversal, notice_date=notice_date, due_date=due_date, settlement_date=settlement_date, receipts=receipts, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

