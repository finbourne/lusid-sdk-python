# AllocationEventReceiptRequest

The request used to record cash received from an investor against a booked capital call.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**investor_record_id** | **str** | The investor record the cash came from. | 
**amount** | **float** | The cash the partner sent, as sent and before any bank charge: in the payment currency if one is given and otherwise in the event currency. | 
**receipt_date** | **datetime** | The date the cash was received. | 
**payment_currency** | **str** | The ISO 4217 code of the currency the cash arrived in, when it differs from the event currency. | [optional] 
**payment_fx_rate** | **float** | The rate the payment was converted at, as units of event currency per unit of payment currency. Required with a payment currency. | [optional] 
**notice_fx_rate** | **float** | The rate the call was noticed at in the payment currency, in the same terms as the payment FX rate. With one, only the rate&#39;s effect on the payment is an FX difference; without one a payment converting to less than the call is simply short. Only with a payment currency. | [optional] 
**bank_charge** | **float** | Any bank charge deducted from the cash before it arrived, in the event currency. | [optional] 
**bank_charge_bearer** | **str** | Who bears the bank charge: Partner leaves it outstanding on the investor, Fund books it as a fund expense. Defaults to the map&#39;s policy. | [optional] 
## Example

```python
from lusid.models.allocation_event_receipt_request import AllocationEventReceiptRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

investor_record_id: StrictStr = "example_investor_record_id"
amount: Union[StrictFloat, StrictInt] = # Replace with your value
receipt_date: datetime = # Replace with your value
payment_currency: Optional[StrictStr] = "example_payment_currency"
payment_fx_rate: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
notice_fx_rate: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
bank_charge: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
bank_charge_bearer: Optional[StrictStr] = "example_bank_charge_bearer"
allocation_event_receipt_request_instance = AllocationEventReceiptRequest(investor_record_id=investor_record_id, amount=amount, receipt_date=receipt_date, payment_currency=payment_currency, payment_fx_rate=payment_fx_rate, notice_fx_rate=notice_fx_rate, bank_charge=bank_charge, bank_charge_bearer=bank_charge_bearer)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

