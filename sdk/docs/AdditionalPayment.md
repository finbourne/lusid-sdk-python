# AdditionalPayment

Record describing additional payment entity.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | The payment amount. | 
**currency** | **str** | The payment currency. | 
**pay_date** | **datetime** | Date when the payment is made. | 
**pay_receive** | **str** | Is it pay or receive.  Supported string (enumeration) values are: [Pay, Receive]. | 
## Example

```python
from lusid.models.additional_payment import AdditionalPayment
from typing import Any, Dict, Union
from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt, StrictStr, constr
from datetime import datetime
amount: Union[StrictFloat, StrictInt] = # Replace with your value
currency: StrictStr = "example_currency"
pay_date: datetime = # Replace with your value
pay_receive: StrictStr = "example_pay_receive"
additional_payment_instance = AdditionalPayment(amount=amount, currency=currency, pay_date=pay_date, pay_receive=pay_receive)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

