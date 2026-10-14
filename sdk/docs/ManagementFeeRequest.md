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
management_fee_request_instance = ManagementFeeRequest(period_start=period_start, period_end=period_end, basis=basis, offsets=offsets, book=book)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

