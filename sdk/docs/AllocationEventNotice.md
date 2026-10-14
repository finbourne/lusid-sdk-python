# AllocationEventNotice

A capital call or distribution notice for one partner on an allocation event: the lines allocated to the  partner, the net amount due, the partner's unfunded commitment rolled through the event, cumulative balances  for the partner and the general partner, and a DRAFT watermark while the event is not yet booked.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fund** | [**ResourceId**](ResourceId.md) |  | 
**event** | [**AllocationEventNoticeEvent**](AllocationEventNoticeEvent.md) |  | 
**partner** | [**AllocationEventNoticePartner**](AllocationEventNoticePartner.md) |  | 
**currency** | **str** | The currency the notice amounts are expressed in. | 
**lines** | [**List[AllocationEventNoticeLine]**](AllocationEventNoticeLine.md) | The notice lines, one per component of the partner&#39;s allocation. | 
**net_amount_due** | **float** | The net amount due, positive when the partner pays the fund and negative when the fund pays the partner. | 
**unfunded_reconciliation** | [**AllocationEventNoticeUnfundedReconciliation**](AllocationEventNoticeUnfundedReconciliation.md) |  | 
**cumulative** | [**AllocationEventNoticeCumulative**](AllocationEventNoticeCumulative.md) |  | 
**gp_column** | [**AllocationEventNoticeCumulative**](AllocationEventNoticeCumulative.md) |  | [optional] 
**wire** | [**AllocationEventNoticeWire**](AllocationEventNoticeWire.md) |  | [optional] 
**payment_hold** | [**AllocationPaymentHold**](AllocationPaymentHold.md) |  | [optional] 
**watermark** | **str** | DRAFT until the allocation event is booked, otherwise null. | [optional] 
## Example

```python
from lusid.models.allocation_event_notice import AllocationEventNotice
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

fund: ResourceId
event: AllocationEventNoticeEvent
partner: AllocationEventNoticePartner
currency: StrictStr = "example_currency"
lines: List[AllocationEventNoticeLine] = # Replace with your value
net_amount_due: Union[StrictFloat, StrictInt] = # Replace with your value
unfunded_reconciliation: AllocationEventNoticeUnfundedReconciliation = # Replace with your value
cumulative: AllocationEventNoticeCumulative
gp_column: Optional[AllocationEventNoticeCumulative] = # Replace with your value
wire: Optional[AllocationEventNoticeWire] = None
payment_hold: Optional[AllocationPaymentHold] = # Replace with your value
watermark: Optional[StrictStr] = "example_watermark"
allocation_event_notice_instance = AllocationEventNotice(fund=fund, event=event, partner=partner, currency=currency, lines=lines, net_amount_due=net_amount_due, unfunded_reconciliation=unfunded_reconciliation, cumulative=cumulative, gp_column=gp_column, wire=wire, payment_hold=payment_hold, watermark=watermark)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

