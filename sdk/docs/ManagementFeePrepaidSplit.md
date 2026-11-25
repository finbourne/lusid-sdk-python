# ManagementFeePrepaidSplit

One partner line's prepaid management fee period, as a re-split found it.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prepaid_run_id** | **str** | The fee run that prepaid the period. | 
**investor_record_id** | **str** | The investor record the fee belongs to. | 
**commitment_line_id** | **str** | The partner&#39;s register line. | 
**period_start** | **datetime** | The start of the prepaid period, exclusive. | 
**period_end** | **datetime** | The end of the prepaid period, inclusive. | 
**was_stale** | **bool** | Whether the split the fund&#39;s books held between the fee payable and the receivable from the manager was out of date: deriving it again from the prepayment, the accruals and the payments to the manager changed it. | 
**is_current** | **bool** | Whether the split the fund&#39;s books now hold is the one derived from the period&#39;s prepayment, accruals and payments to the manager. False only on a dry run over an out of date split. | 
**payment_transaction_ids** | **List[str]** | The payments to the manager in the period booked or amended since its split was last derived. A cancelled payment cannot be named. | 
## Example

```python
from lusid.models.management_fee_prepaid_split import ManagementFeePrepaidSplit
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

prepaid_run_id: StrictStr = "example_prepaid_run_id"
investor_record_id: StrictStr = "example_investor_record_id"
commitment_line_id: StrictStr = "example_commitment_line_id"
period_start: datetime = # Replace with your value
period_end: datetime = # Replace with your value
was_stale: StrictBool = # Replace with your value
was_stale:StrictBool = True
is_current: StrictBool = # Replace with your value
is_current:StrictBool = True
payment_transaction_ids: List[StrictStr] = # Replace with your value
management_fee_prepaid_split_instance = ManagementFeePrepaidSplit(prepaid_run_id=prepaid_run_id, investor_record_id=investor_record_id, commitment_line_id=commitment_line_id, period_start=period_start, period_end=period_end, was_stale=was_stale, is_current=is_current, payment_transaction_ids=payment_transaction_ids)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

