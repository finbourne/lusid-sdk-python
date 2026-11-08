# CollateralAllocation

Which of our assets to move for a margin call and why: every holding considered, with its rank or the constraint  that excluded it, and the lines chosen cheapest first, each carrying what a transaction moving it needs. Amounts  are in the agreement's base currency.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | **str** | The run the call belongs to. | 
**call_id** | **str** | The business key of the call within the run: agreement scope and code, item, margin type and direction joined with &#39;/&#39;. | 
**direction** | **str** | Whether the collateral is delivered to the counterparty or recalled from it. One of Deliver or Recall. | 
**inventory_source** | **str** | Where the holdings were read from: RunStore for the proposal the run made, Live for a ranking against the holdings as they stand now. | 
**as_at** | **datetime** | The asAt the holdings and terms were read at. | 
**agreement_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**item** | **str** | The margin item of the call. | [optional] 
**counterparty** | [**CounterpartyIdentifier**](CounterpartyIdentifier.md) |  | [optional] 
**business_date** | **datetime** | The business date of the call, which a transaction for a line trades on. | [optional] 
**deadline** | **datetime** | When the movement must have settled under the agreement&#39;s cut label. Null when the agreement sets none. | [optional] 
**margin_account** | **str** | The code of the custodian account the item names for collateral we post, which a delivery moves assets into and a recall moves them out of. Null when the item names none. | [optional] 
**base_currency** | **str** | The agreement&#39;s base currency, which every amount is in. | 
**required_amount** | **float** | The collateral value to deliver, or for a recall the excess to take back. | 
**covered_amount** | **float** | The collateral value of the lines chosen: below the requirement when the inventory ran out, above it when a lot could not be split. | 
**carry_per_day** | **float** | What the chosen lines cost the fund a day to leave locked up, in the base currency. | 
**all_cash_carry_per_day** | **float** | What covering the whole call in base-currency cash would cost a day. Null when the cash rate is unavailable or for a recall. | [optional] 
**candidates** | [**List[CollateralAllocationCandidate]**](CollateralAllocationCandidate.md) | Every holding considered, ranked ones first by rank, then the excluded with the constraint that excluded them. | 
**allocation** | [**List[CollateralAllocationLine]**](CollateralAllocationLine.md) | The assets chosen, cheapest first, each with what a transaction moving it needs. | 
## Example

```python
from lusid.models.collateral_allocation import CollateralAllocation
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

run_id: StrictStr = "example_run_id"
call_id: StrictStr = "example_call_id"
direction: StrictStr = "example_direction"
inventory_source: StrictStr = "example_inventory_source"
as_at: datetime = # Replace with your value
agreement_id: Optional[ResourceId] = # Replace with your value
item: Optional[StrictStr] = "example_item"
counterparty: Optional[CounterpartyIdentifier] = None
business_date: Optional[datetime] = # Replace with your value
deadline: Optional[datetime] = # Replace with your value
margin_account: Optional[StrictStr] = "example_margin_account"
base_currency: StrictStr = "example_base_currency"
required_amount: Union[StrictFloat, StrictInt] = # Replace with your value
covered_amount: Union[StrictFloat, StrictInt] = # Replace with your value
carry_per_day: Union[StrictFloat, StrictInt] = # Replace with your value
all_cash_carry_per_day: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
candidates: List[CollateralAllocationCandidate] = # Replace with your value
allocation: List[CollateralAllocationLine] = # Replace with your value
collateral_allocation_instance = CollateralAllocation(run_id=run_id, call_id=call_id, direction=direction, inventory_source=inventory_source, as_at=as_at, agreement_id=agreement_id, item=item, counterparty=counterparty, business_date=business_date, deadline=deadline, margin_account=margin_account, base_currency=base_currency, required_amount=required_amount, covered_amount=covered_amount, carry_per_day=carry_per_day, all_cash_carry_per_day=all_cash_carry_per_day, candidates=candidates, allocation=allocation)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

