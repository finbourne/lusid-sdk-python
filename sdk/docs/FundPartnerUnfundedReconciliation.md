# FundPartnerUnfundedReconciliation

The unfunded commitment statement of one partner over a period: the register's opening unfunded, the booked  activity that moves it, the closing unfunded that implies, and the register's own closing unfunded it is checked against.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**investor_record_id** | **str** | The investor record the statement is for. | 
**fund_id** | [**ResourceId**](ResourceId.md) |  | 
**currency** | **str** | The currency of every amount on the statement, being the commitment currency of the register line. | 
**period_from** | **datetime** | The effective datetime the statement opens at. | 
**period_to** | **datetime** | The effective datetime the statement closes at. | 
**opening_unfunded** | **float** | The unfunded commitment at the opening datetime, from the register. | 
**contributions_inside_commitment** | **float** | Capital called inside the commitment over the period, which reduces unfunded. Contributions outside the commitment, such as equalisation interest, are listed but do not count here. | 
**recallable_distributions** | **float** | Distributions over the period returned as recallable, which restore unfunded. | 
**expired_recallable** | **float** | Recallable distributions whose recall deadline passed in the period without being recalled, which reduce unfunded. | 
**commitment_changes** | **float** | Changes to the commitment over the period, which move unfunded one for one. | 
**transfers** | **float** | Commitment transferred in or out over the period, which moves unfunded one for one. | 
**closing_unfunded** | **float** | Opening unfunded less contributions inside the commitment, plus recallable distributions, less expired recallable, plus or minus commitment changes and transfers. | 
**register_unfunded** | **float** | The unfunded commitment at the closing datetime, from the register. | 
**difference** | **float** | Closing unfunded less the register&#39;s unfunded at the closing datetime. Zero when the statement ties. | 
**ties** | **bool** | Whether the closing unfunded equals the register&#39;s unfunded at the closing datetime. | 
**lines** | [**List[FundPartnerUnfundedReconciliationLine]**](FundPartnerUnfundedReconciliationLine.md) | Every booked allocation to the partner over the period, in event date order, with the ILPA transaction type each is reported under and its effect on unfunded. | 
## Example

```python
from lusid.models.fund_partner_unfunded_reconciliation import FundPartnerUnfundedReconciliation
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

investor_record_id: StrictStr = "example_investor_record_id"
fund_id: ResourceId = # Replace with your value
currency: StrictStr = "example_currency"
period_from: datetime = # Replace with your value
period_to: datetime = # Replace with your value
opening_unfunded: Union[StrictFloat, StrictInt] = # Replace with your value
contributions_inside_commitment: Union[StrictFloat, StrictInt] = # Replace with your value
recallable_distributions: Union[StrictFloat, StrictInt] = # Replace with your value
expired_recallable: Union[StrictFloat, StrictInt] = # Replace with your value
commitment_changes: Union[StrictFloat, StrictInt] = # Replace with your value
transfers: Union[StrictFloat, StrictInt] = # Replace with your value
closing_unfunded: Union[StrictFloat, StrictInt] = # Replace with your value
register_unfunded: Union[StrictFloat, StrictInt] = # Replace with your value
difference: Union[StrictFloat, StrictInt] = # Replace with your value
ties: StrictBool = # Replace with your value
ties:StrictBool = True
lines: List[FundPartnerUnfundedReconciliationLine] = # Replace with your value
fund_partner_unfunded_reconciliation_instance = FundPartnerUnfundedReconciliation(investor_record_id=investor_record_id, fund_id=fund_id, currency=currency, period_from=period_from, period_to=period_to, opening_unfunded=opening_unfunded, contributions_inside_commitment=contributions_inside_commitment, recallable_distributions=recallable_distributions, expired_recallable=expired_recallable, commitment_changes=commitment_changes, transfers=transfers, closing_unfunded=closing_unfunded, register_unfunded=register_unfunded, difference=difference, ties=ties, lines=lines)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

