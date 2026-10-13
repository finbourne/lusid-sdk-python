# AllocationEventRequest

The request used to raise or replace an Allocation Event. The event is computed against its map straight away.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The code of the Allocation Event. Together with the scope this uniquely identifies the event. | 
**allocation_map_id** | [**ResourceId**](ResourceId.md) |  | 
**event_type** | **str** | The type of the event: CapitalCall, Distribution, FeeExpense, ValuationMove, Equalisation, RecallExpiry, Transfer, Default, Commitment or DealFunding. Selects the basis rule from the map. A recall is a CapitalCall with a Recall component. A Commitment event is not shared from a basis: its basis values are the signed commitment amounts per commitment line, and they must sum to the amount. Available values: CapitalCall, Distribution, FeeExpense, ValuationMove, Commitment, Equalisation, RecallExpiry, Transfer, Default, DealFunding. | 
**amount** | **float** | The total amount to be shared across the participants. | 
**currency** | **str** | The ISO 4217 code of the currency of the amount. The amount may not be finer than the currency&#39;s minor unit: two decimal places for most currencies, none for JPY, three for KWD and BHD. A code with no defined minor unit, such as XAU or XAG, is taken to have two decimal places. | 
**event_date** | **datetime** | The date of the event: the point at which the map, its participants and their basis values are read. | 
**description** | **str** | A description of the Allocation Event. | [optional] 
**basis_values** | [**List[AllocationMapBasisValue]**](AllocationMapBasisValue.md) | Optional basis values per investor record, used when the map&#39;s basis is not resolvable from stored data. | [optional] 
**components** | [**List[AllocationEventComponent]**](AllocationEventComponent.md) | The parts the amount splits into, each shared on its own basis and booked to its own slot. The component amounts must sum to the event amount. Absent means the whole amount is one component: Investment for a CapitalCall, ROC for a Distribution. | [optional] 
**transfers** | [**List[AllocationEventTransfer]**](AllocationEventTransfer.md) | For a Transfer event, the legs to book: each moves a fraction of one capital interest line to another. Required for a Transfer event and not allowed on any other type. The fractions out of one line must sum to at most one; the amount of a Transfer event is zero. | [optional] 
**equalisation** | [**AllocationEventEqualisation**](AllocationEventEqualisation.md) |  | [optional] 
**use_of_proceeds** | [**List[AllocationEventUseOfProceeds]**](AllocationEventUseOfProceeds.md) | For a CapitalCall, what the call pays for: rows of purpose, deal and amount that sum to the call amount. An Investment row names a deal the vehicle has funded and is shared under that deal&#39;s participation, with each investor&#39;s share recorded as paid in for that deal; when the deal was funded from a facility the row repays the draw. Not allowed with components or on any other event type. | [optional] 
**deal_funding** | [**AllocationEventDealFunding**](AllocationEventDealFunding.md) |  | [optional] 
**effective_at** | **datetime** | The effective datetime at which the event is created or replaced. Defaults to the earliest effective time on create and the current LUSID system datetime on replace. | [optional] 
**replaces** | [**ResourceId**](ResourceId.md) |  | [optional] 
**notice_date** | **datetime** | The date the notice went to investors. | [optional] 
**due_date** | **datetime** | The date the investors&#39; cash is due. | [optional] 
**settlement_date** | **datetime** | The date the postings settle. Defaults to the event date. | [optional] 
## Example

```python
from lusid.models.allocation_event_request import AllocationEventRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

code: StrictStr = "example_code"
allocation_map_id: ResourceId = # Replace with your value
event_type: StrictStr = "example_event_type"
amount: Union[StrictFloat, StrictInt] = # Replace with your value
currency: StrictStr = "example_currency"
event_date: datetime = # Replace with your value
description: Optional[StrictStr] = "example_description"
basis_values: Optional[List[AllocationMapBasisValue]] = # Replace with your value
components: Optional[List[AllocationEventComponent]] = # Replace with your value
transfers: Optional[List[AllocationEventTransfer]] = # Replace with your value
equalisation: Optional[AllocationEventEqualisation] = None
use_of_proceeds: Optional[List[AllocationEventUseOfProceeds]] = # Replace with your value
deal_funding: Optional[AllocationEventDealFunding] = # Replace with your value
effective_at: Optional[datetime] = # Replace with your value
replaces: Optional[ResourceId] = None
notice_date: Optional[datetime] = # Replace with your value
due_date: Optional[datetime] = # Replace with your value
settlement_date: Optional[datetime] = # Replace with your value
allocation_event_request_instance = AllocationEventRequest(code=code, allocation_map_id=allocation_map_id, event_type=event_type, amount=amount, currency=currency, event_date=event_date, description=description, basis_values=basis_values, components=components, transfers=transfers, equalisation=equalisation, use_of_proceeds=use_of_proceeds, deal_funding=deal_funding, effective_at=effective_at, replaces=replaces, notice_date=notice_date, due_date=due_date, settlement_date=settlement_date)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

