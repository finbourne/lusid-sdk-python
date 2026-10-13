# FundPartnerUnfundedReconciliationLine

One booked allocation to the partner on the unfunded commitment statement.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocation_event_id** | [**ResourceId**](ResourceId.md) |  | 
**event_date** | **datetime** | The event date of the allocation. | 
**event_type** | **str** | The kind of allocation event: CapitalCall, Distribution, FeeExpense, ValuationMove, Equalisation, RecallExpiry, Transfer, Default or Commitment. | 
**component** | **str** | The component of the event the amount belongs to, for example Investment, MgmtFee or ROC. | [optional] 
**ilpa_transaction_type** | **str** | The ILPA transaction type the line is reported under, from the map&#39;s override or the default for the event type and component. | 
**inside_fund** | **bool** | Whether the flow is inside the fund&#39;s commitment. False for flows outside it, such as equalisation interest or late payment interest, which do not move unfunded. | 
**amount** | **float** | The amount allocated to the partner, in the statement currency. | 
**unfunded_impact** | **float** | The effect of the line on unfunded commitment: negative for a call inside the commitment or an expired recallable, positive for a recallable distribution, and the signed amount for a commitment change or transfer. Zero for a flow that does not move unfunded. | 
**recallable_until** | **datetime** | For a recallable distribution, the last date it may be recalled. Absent when there is no deadline or the line is not recallable. | [optional] 
## Example

```python
from lusid.models.fund_partner_unfunded_reconciliation_line import FundPartnerUnfundedReconciliationLine
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

allocation_event_id: ResourceId = # Replace with your value
event_date: datetime = # Replace with your value
event_type: StrictStr = "example_event_type"
component: Optional[StrictStr] = "example_component"
ilpa_transaction_type: StrictStr = "example_ilpa_transaction_type"
inside_fund: StrictBool = # Replace with your value
inside_fund:StrictBool = True
amount: Union[StrictFloat, StrictInt] = # Replace with your value
unfunded_impact: Union[StrictFloat, StrictInt] = # Replace with your value
recallable_until: Optional[datetime] = # Replace with your value
fund_partner_unfunded_reconciliation_line_instance = FundPartnerUnfundedReconciliationLine(allocation_event_id=allocation_event_id, event_date=event_date, event_type=event_type, component=component, ilpa_transaction_type=ilpa_transaction_type, inside_fund=inside_fund, amount=amount, unfunded_impact=unfunded_impact, recallable_until=recallable_until)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

