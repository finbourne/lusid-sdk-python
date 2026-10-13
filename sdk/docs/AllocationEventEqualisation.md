# AllocationEventEqualisation

The terms of a subsequent close an Equalisation Allocation Event applies: the booked prior calls to equalise, the  partners admitted, and how interest, excess and profit and loss are treated.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prior_call_ids** | [**List[ResourceId]**](ResourceId.md) | The booked capital calls to equalise, and any earlier equalisation on the same map whose catch-up the admitted partners must also be brought level with. Each must be booked, on the same allocation map and in the same currency. | 
**new_investor_record_ids** | **List[str]** | The investor records admitted at this close. Each must be on the register with its commitment at the event date. | 
**interest_rate** | **float** | The simple annual rate of equalisation interest the admitted partners pay on each catch-up from the prior call&#39;s due date to the event date. Defaults to 0.08. | [optional] 
**day_count_convention** | **str** | The day count of the equalisation interest: ACT/365 or ACT/360. Defaults to ACT/365. | [optional] 
**interest_on_fees** | **bool** | Whether equalisation interest is also charged on the management fee catch-ups, from each fee&#39;s due date. Defaults to false. | [optional] 
**treatment** | **str** | How the existing partners&#39; excess is returned: ReturnOfExcess restores it to their uncalled commitment; RecallableDistribution distributes it as recallable capital. Defaults to ReturnOfExcess. Available values: ReturnOfExcess, RecallableDistribution. | [optional] 
**pnl** | **str** | Whether profit and loss already allocated is re-trued between partners with no cash so each holds its post-close share (ReTrue), or the equalisation is kept to capital (CapitalOnly). Defaults to ReTrue. Available values: ReTrue, CapitalOnly. | [optional] 
**fee_catch_ups** | [**List[AllocationEventEqualisationFeeCatchUp]**](AllocationEventEqualisationFeeCatchUp.md) | The management fees each admitted partner owes from the first fee date to the close, including any stub period, as explicit amounts. Paid to the manager and allocated to that partner only. | [optional] 
**marks** | [**List[AllocationEventEqualisationMark]**](AllocationEventEqualisationMark.md) | The valuation moves already allocated to the existing partners, by the member of the structure they belong to, to re-true to the admitted partners. Ignored when the profit and loss treatment is CapitalOnly. | [optional] 
## Example

```python
from lusid.models.allocation_event_equalisation import AllocationEventEqualisation
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

prior_call_ids: List[ResourceId] = # Replace with your value
new_investor_record_ids: List[StrictStr] = # Replace with your value
interest_rate: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
day_count_convention: Optional[StrictStr] = "example_day_count_convention"
interest_on_fees: Optional[StrictBool] = # Replace with your value
interest_on_fees:Optional[StrictBool] = None
treatment: Optional[StrictStr] = "example_treatment"
pnl: Optional[StrictStr] = "example_pnl"
fee_catch_ups: Optional[List[AllocationEventEqualisationFeeCatchUp]] = # Replace with your value
marks: Optional[List[AllocationEventEqualisationMark]] = # Replace with your value
allocation_event_equalisation_instance = AllocationEventEqualisation(prior_call_ids=prior_call_ids, new_investor_record_ids=new_investor_record_ids, interest_rate=interest_rate, day_count_convention=day_count_convention, interest_on_fees=interest_on_fees, treatment=treatment, pnl=pnl, fee_catch_ups=fee_catch_ups, marks=marks)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

