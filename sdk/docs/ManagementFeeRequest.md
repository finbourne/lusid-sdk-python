# ManagementFeeRequest

The request to calculate a period's management fee for the partners of a partnership fund.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period_start** | **datetime** | The start of the fee period, exclusive. | 
**period_end** | **datetime** | The end of the fee period, inclusive. | 
**basis** | **str** | The capital base the fee is charged on. Available values: Auto, CommittedCapital, InvestedCapital. Auto charges on committed capital until the investment period ends and on invested capital after. | [optional] 
**offsets** | [**List[ManagementFeeOffset]**](ManagementFeeOffset.md) | Fee income received by the manager that offsets the management fee. | [optional] 
**book** | **bool** | When true, the net fee per partner is booked. | [optional] 
**prepaid** | **bool** | When true with book, the period&#39;s fee is booked in advance: the fund prepays each partner&#39;s gross fee per component against the fee payable at the period&#39;s start, and the partnership ledger is not charged. Offsets are not prepaid. Fee runs accruing inside the period then charge the fee against the prepayment, up to its balance and at the prepayment&#39;s rate, and any excess against the payable; an offset arising inside the period reduces the payable, and any part of it above the payable is booked as a receivable from the manager. Defaults to false. | [optional] 
## Example

```python
from lusid.models.management_fee_request import ManagementFeeRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

period_start: datetime = # Replace with your value
period_end: datetime = # Replace with your value
basis: Optional[StrictStr] = "example_basis"
offsets: Optional[List[ManagementFeeOffset]] = # Replace with your value
book: Optional[StrictBool] = # Replace with your value
book:Optional[StrictBool] = None
prepaid: Optional[StrictBool] = # Replace with your value
prepaid:Optional[StrictBool] = None
management_fee_request_instance = ManagementFeeRequest(period_start=period_start, period_end=period_end, basis=basis, offsets=offsets, book=book, prepaid=prepaid)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

