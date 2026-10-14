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
management_fee_result_instance = ManagementFeeResult(fund_id=fund_id, period_start=period_start, period_end=period_end, basis=basis, lines=lines, totals=totals, booked_transaction_ids=booked_transaction_ids)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

