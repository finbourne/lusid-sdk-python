# PaymentRecordReference

Identifies a Payment Record attached to a specific transaction within a portfolio.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**portfolio_id** | [**ResourceId**](ResourceId.md) |  | 
**transaction_id** | **str** | The ID of the cash transaction within the portfolio to which the Payment Record is attached. | 
**payment_record_id** | **str** | The unique identifier of the Payment Record attached to the above transaction. | 
## Example

```python
from lusid.models.payment_record_reference import PaymentRecordReference
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

portfolio_id: ResourceId = # Replace with your value
transaction_id: StrictStr = "example_transaction_id"
payment_record_id: StrictStr = "example_payment_record_id"
payment_record_reference_instance = PaymentRecordReference(portfolio_id=portfolio_id, transaction_id=transaction_id, payment_record_id=payment_record_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

