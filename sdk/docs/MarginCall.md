# MarginCall

A margin call a run produced under a collateral agreement: our figure, the counterparty's demand once recorded  and how they compare, and where the call is in its lifecycle.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The URI of this margin call. | [optional] 
**id** | **str** | The identifier of the call: the run id and the call&#39;s business key joined with &#39;/&#39;. | 
**run_id** | **str** | The run that produced the call. Filterable. | 
**agreement_id** | [**ResourceId**](ResourceId.md) |  | 
**counterparty** | [**CounterpartyIdentifier**](CounterpartyIdentifier.md) |  | [optional] 
**item** | **str** | The margin item of the agreement the call is for. Filterable. | 
**margin_type** | **str** | The type of margin called. Currently VariationMargin. Filterable. | 
**method** | **str** | The calculation method of the margin item. | [optional] 
**settlement** | **str** | Whether the item is settled or collateralised. | [optional] 
**direction** | **str** | Who posts: WePost, TheyPost or None when the exposure is flat. Filterable. | 
**currency** | **str** | The currency of the call, the agreement&#39;s base currency. Filterable. | 
**required** | **float** | The margin required under the agreement, signed as the call. | 
**held** | **float** | The collateral already held against the item, signed as the call. | 
**call** | **float** | Our figure for the amount to move: required less held. Filterable. | 
**match_tolerance** | **float** | The agreement&#39;s match tolerance captured on the call. | [optional] 
**counterparty_demand** | **float** | The counterparty&#39;s figure for the call, once recorded. | [optional] 
**difference** | **float** | The counterparty&#39;s demand less our call, once recorded. | [optional] 
**match_status** | **str** | How the counterparty&#39;s demand compares to our call. One of Unmatched, Matched, WithinTolerance, Break or NotRequired. Filterable. | 
**demand_received_at** | **datetime** | When the counterparty&#39;s demand was received. | [optional] 
**statement_reference** | **str** | A reference to the counterparty&#39;s statement, such as a Drive path. | [optional] 
**demand_note** | **str** | A note recorded with the counterparty&#39;s demand. | [optional] 
**agreed_amount** | **float** | The amount agreed to move, once the call is accepted or disputed. | [optional] 
**disputed_amount** | **float** | The part of the larger of our call and the counterparty&#39;s demand left in dispute. | [optional] 
**dispute_reason** | **str** | Why the call is disputed. | [optional] 
**dispute_owner** | **str** | Who owns the dispute. | [optional] 
**state** | **str** | Where the call is in its lifecycle. One of Calculated, Accepted or Disputed. Filterable. | 
**deadline** | **datetime** | The time the call must be agreed by. Empty until agreements carry a notification time. | [optional] 
**supersedes** | [**MarginCallReference**](MarginCallReference.md) |  | [optional] 
**carried_from** | [**MarginCallReference**](MarginCallReference.md) |  | [optional] 
**carried_disputed_amount** | **float** | The amount left in dispute on the carried call. Informational; not added to this call. | [optional] 
## Example

```python
from lusid.models.margin_call import MarginCall
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

href: Optional[StrictStr] = "example_href"
id: StrictStr = "example_id"
run_id: StrictStr = "example_run_id"
agreement_id: ResourceId = # Replace with your value
counterparty: Optional[CounterpartyIdentifier] = None
item: StrictStr = "example_item"
margin_type: StrictStr = "example_margin_type"
method: Optional[StrictStr] = "example_method"
settlement: Optional[StrictStr] = "example_settlement"
direction: StrictStr = "example_direction"
currency: StrictStr = "example_currency"
required: Union[StrictFloat, StrictInt] = # Replace with your value
held: Union[StrictFloat, StrictInt] = # Replace with your value
call: Union[StrictFloat, StrictInt] = # Replace with your value
match_tolerance: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
counterparty_demand: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
difference: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
match_status: StrictStr = "example_match_status"
demand_received_at: Optional[datetime] = # Replace with your value
statement_reference: Optional[StrictStr] = "example_statement_reference"
demand_note: Optional[StrictStr] = "example_demand_note"
agreed_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
disputed_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
dispute_reason: Optional[StrictStr] = "example_dispute_reason"
dispute_owner: Optional[StrictStr] = "example_dispute_owner"
state: StrictStr = "example_state"
deadline: Optional[datetime] = # Replace with your value
supersedes: Optional[MarginCallReference] = None
carried_from: Optional[MarginCallReference] = # Replace with your value
carried_disputed_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
margin_call_instance = MarginCall(href=href, id=id, run_id=run_id, agreement_id=agreement_id, counterparty=counterparty, item=item, margin_type=margin_type, method=method, settlement=settlement, direction=direction, currency=currency, required=required, held=held, call=call, match_tolerance=match_tolerance, counterparty_demand=counterparty_demand, difference=difference, match_status=match_status, demand_received_at=demand_received_at, statement_reference=statement_reference, demand_note=demand_note, agreed_amount=agreed_amount, disputed_amount=disputed_amount, dispute_reason=dispute_reason, dispute_owner=dispute_owner, state=state, deadline=deadline, supersedes=supersedes, carried_from=carried_from, carried_disputed_amount=carried_disputed_amount)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

