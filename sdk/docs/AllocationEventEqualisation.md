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
**treatment** | **str** | How the existing partners&#39; excess is returned: ReturnOfExcess restores it to their uncalled commitment; RecallableDistribution distributes it as recallable capital; CreditAgainstFutureCalls restores it to their uncalled commitment and keeps the cash in the fund as a credit their next calls draw down; RetainedByFund hands nothing back and instead calls the admitted partners up to the existing partners&#39; level on the commitments before the close. Defaults to ReturnOfExcess. Available values: ReturnOfExcess, RecallableDistribution, CreditAgainstFutureCalls, RetainedByFund. | [optional] 
**pnl** | **str** | Whether profit and loss already allocated is re-trued between partners with no cash so each holds its post-close share (ReTrue), or the equalisation is kept to capital (CapitalOnly). Defaults to CapitalOnly when omitted on a request. An equalisation stored before this default was introduced keeps the treatment it was stored with, which is ReTrue. Available values: ReTrue, CapitalOnly. | [optional] 
**fee_catch_ups** | [**List[AllocationEventEqualisationFeeCatchUp]**](AllocationEventEqualisationFeeCatchUp.md) | The management fees each admitted partner owes from the first fee date to the close, including any stub period, as explicit amounts. Paid to the manager and allocated to that partner only. | [optional] 
**marks** | [**List[AllocationEventEqualisationMark]**](AllocationEventEqualisationMark.md) | The valuation moves already allocated to the existing partners, by the member of the structure they belong to, to re-true to the admitted partners. Ignored when the profit and loss treatment is CapitalOnly. | [optional] 
**prior_distribution_ids** | [**List[ResourceId]**](ResourceId.md) | The booked distributions on the same allocation map, dated before the close, whose return of capital is re-spread net of the prior calls. When omitted, every booked distribution on the map dated before the close counts. | [optional] 
**interest_treatment** | **str** | How the equalisation interest reaches the existing partners: Cash pays it to them; CapitalCredit credits it to their capital accounts with no cash; None charges and pays no equalisation interest. Defaults to Cash. Available values: Cash, CapitalCredit, None. | [optional] 
**excluded_components** | **List[str]** | The call components left out of the re-spread: ManagementFee, OtherFee, Expense, OrganisationCost or Recall. Defaults to ManagementFee. A component no prior call carries, other than ManagementFee, is refused. Available values: ManagementFee, OtherFee, Expense, OrganisationCost, Recall. | [optional] 
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
prior_distribution_ids: Optional[List[ResourceId]] = # Replace with your value
interest_treatment: Optional[StrictStr] = "example_interest_treatment"
excluded_components: Optional[List[StrictStr]] = # Replace with your value
allocation_event_equalisation_instance = AllocationEventEqualisation(prior_call_ids=prior_call_ids, new_investor_record_ids=new_investor_record_ids, interest_rate=interest_rate, day_count_convention=day_count_convention, interest_on_fees=interest_on_fees, treatment=treatment, pnl=pnl, fee_catch_ups=fee_catch_ups, marks=marks, prior_distribution_ids=prior_distribution_ids, interest_treatment=interest_treatment, excluded_components=excluded_components)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

