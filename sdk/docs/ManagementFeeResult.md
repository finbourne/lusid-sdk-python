# ManagementFeeResult

The outcome of a management fee calculation.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fund_id** | [**ResourceId**](ResourceId.md) |  | 
**period_start** | **datetime** | The start of the fee period, exclusive. | 
**period_end** | **datetime** | The end of the fee period, inclusive. | 
**basis** | **str** | The capital base the fee is charged on. Available values: Auto, CommittedCapital, InvestedCapital. Auto charges on committed capital until the investment period ends and on invested capital after. | 
**lines** | [**List[ManagementFeeLine]**](ManagementFeeLine.md) | The fee per partner. | 
**totals** | [**ManagementFeeTotals**](ManagementFeeTotals.md) |  | 
**booked_transaction_ids** | **List[str]** | The identifiers of the transactions booked, if any. | 
**fund_transaction_ids** | **List[str]** | The identifiers of the fee transactions the run holds in the fund&#39;s own books, one per partner and fee component, when the run was booked. | [optional] 
**warnings** | **List[str]** | What booking the run noticed but did not refuse, each starting with its code, for example a payment to the manager on the fee payable in a currency other than the fee&#39;s, which settles none of the payable an offset is set against (FeePaymentCurrencyIgnored), or a prepaid period in the year to the run&#39;s period end whose split between the fee payable and the receivable from the manager is out of date, because a payment to the manager was booked, amended or cancelled since it was derived (FeePrepaidSplitStale): its balances are provisional until the period is re-split. Absent when there is nothing to warn of. | [optional] 
## Example

```python
from lusid.models.management_fee_result import ManagementFeeResult
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

fund_id: ResourceId = # Replace with your value
period_start: datetime = # Replace with your value
period_end: datetime = # Replace with your value
basis: StrictStr = "example_basis"
lines: List[ManagementFeeLine] = # Replace with your value
totals: ManagementFeeTotals
booked_transaction_ids: List[StrictStr] = # Replace with your value
fund_transaction_ids: Optional[List[StrictStr]] = # Replace with your value
warnings: Optional[List[StrictStr]] = # Replace with your value
management_fee_result_instance = ManagementFeeResult(fund_id=fund_id, period_start=period_start, period_end=period_end, basis=basis, lines=lines, totals=totals, booked_transaction_ids=booked_transaction_ids, fund_transaction_ids=fund_transaction_ids, warnings=warnings)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

