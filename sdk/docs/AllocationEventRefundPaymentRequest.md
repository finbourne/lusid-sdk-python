# AllocationEventRefundPaymentRequest

The request used to pay out a refund owed to an investor whose receipt against a booked capital call exceeded  what it owed.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**investor_record_id** | **str** | The investor record the refund is paid to. | 
**amount** | **float** | The amount paid, in the event currency. Must be positive, no finer than the currency&#39;s minor unit, and no more than the refund still payable to the investor record on the event. | 
**paid_date** | **datetime** | The date the cash was paid out. Not before the receipt that created the refund payable. | 
**reference** | **str** | The caller&#39;s reference for the payment, for instance a payment instruction id. Posting the same reference again returns the event unchanged and writes nothing. | 
## Example

```python
from lusid.models.allocation_event_refund_payment_request import AllocationEventRefundPaymentRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

investor_record_id: StrictStr = "example_investor_record_id"
amount: Union[StrictFloat, StrictInt] = # Replace with your value
paid_date: datetime = # Replace with your value
reference: StrictStr = "example_reference"
allocation_event_refund_payment_request_instance = AllocationEventRefundPaymentRequest(investor_record_id=investor_record_id, amount=amount, paid_date=paid_date, reference=reference)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

