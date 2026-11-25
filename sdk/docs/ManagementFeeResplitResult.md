# ManagementFeeResplitResult

What a re-split of a partnership fund's prepaid management fee periods found and wrote.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fund_id** | [**ResourceId**](ResourceId.md) |  | 
**periods** | [**List[ManagementFeePrepaidSplit]**](ManagementFeePrepaidSplit.md) | Every partner line&#39;s prepaid period the re-split read, in date order. | 
**written_transaction_ids** | **List[str]** | The fee transactions the re-split wrote in the fund&#39;s own books, new or replaced. Empty on a dry run, and when no split changed. | 
**cancelled_transaction_ids** | **List[str]** | The fee transactions the re-split cancelled in the fund&#39;s own books. Empty on a dry run, and when no split changed. | 
**warnings** | **List[str]** | What the re-split noticed but did not refuse, each starting with its code: on a dry run each out of date split (FeePrepaidSplitStale), and a payment to the manager in a currency other than the fee&#39;s (FeePaymentCurrencyIgnored). Absent when there is nothing to warn of. | [optional] 
## Example

```python
from lusid.models.management_fee_resplit_result import ManagementFeeResplitResult
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

fund_id: ResourceId = # Replace with your value
periods: List[ManagementFeePrepaidSplit] = # Replace with your value
written_transaction_ids: List[StrictStr] = # Replace with your value
cancelled_transaction_ids: List[StrictStr] = # Replace with your value
warnings: Optional[List[StrictStr]] = # Replace with your value
management_fee_resplit_result_instance = ManagementFeeResplitResult(fund_id=fund_id, periods=periods, written_transaction_ids=written_transaction_ids, cancelled_transaction_ids=cancelled_transaction_ids, warnings=warnings)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

