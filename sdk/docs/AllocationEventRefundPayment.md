# AllocationEventRefundPayment

One payment of a refund owed to an investor record on a booked capital call, as recorded.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**investor_record_id** | **str** | The investor record the refund is paid to. | [optional] 
**amount** | **float** | The amount paid, in the event currency. Must be positive, no finer than the currency&#39;s minor unit, and no more than the refund still payable to the investor record on the event. | [optional] 
**paid_date** | **datetime** | The date the cash was paid out. Not before the receipt that created the refund payable. | [optional] 
**reference** | **str** | The caller&#39;s reference for the payment, for instance a payment instruction id. Posting the same reference again returns the event unchanged and writes nothing. | [optional] 
**posting_id** | **str** | The identifier of the fund-side posting the payment was written under. | [optional] 
## Example

```python
from lusid.models.allocation_event_refund_payment import AllocationEventRefundPayment
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

investor_record_id: Optional[StrictStr] = "example_investor_record_id"
amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
paid_date: Optional[datetime] = # Replace with your value
reference: Optional[StrictStr] = "example_reference"
posting_id: Optional[StrictStr] = "example_posting_id"
allocation_event_refund_payment_instance = AllocationEventRefundPayment(investor_record_id=investor_record_id, amount=amount, paid_date=paid_date, reference=reference, posting_id=posting_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

