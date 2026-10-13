# AllocationEventReceipt

One receipt of cash against a booked capital call, as recorded.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**investor_record_id** | **str** | The investor record the cash came from. | [optional] 
**amount** | **float** | The cash received, in the event currency after any FX conversion. | [optional] 
**receipt_date** | **datetime** | The date the cash was received. | [optional] 
**applied** | **float** | How much of the receipt was applied to what the investor owed. | [optional] 
**refund** | **float** | How much of the receipt exceeded what the investor owed and became a refund payable. | [optional] 
**payment_currency** | **str** | The ISO 4217 code of the currency the cash arrived in, when it differs from the event currency. | [optional] 
**payment_fx_rate** | **float** | The rate the payment was converted at, as units of event currency per unit of payment currency. Required with a payment currency. | [optional] 
**fx_difference** | **float** | The part of the difference between the payment converted at the notice rate and at the payment rate that the fund did not absorb; positive when the rate moved against the fund. Zero without a notice rate. | [optional] 
**bank_charge** | **float** | Any bank charge deducted from the cash before it arrived, in the event currency. | [optional] 
**bank_charge_bearer** | **str** | Who bears the bank charge: Partner leaves it outstanding on the investor, Fund books it as a fund expense. Defaults to the map&#39;s policy. | [optional] 
**shortfall_written_off** | **float** | Any small shortfall within the map&#39;s tolerance that was written off rather than left outstanding. | [optional] 
**posting_id** | **str** | The identifier of the receipt posting on the investor&#39;s line. | [optional] 
## Example

```python
from lusid.models.allocation_event_receipt import AllocationEventReceipt
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

investor_record_id: Optional[StrictStr] = "example_investor_record_id"
amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
receipt_date: Optional[datetime] = # Replace with your value
applied: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
refund: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
payment_currency: Optional[StrictStr] = "example_payment_currency"
payment_fx_rate: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
fx_difference: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
bank_charge: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
bank_charge_bearer: Optional[StrictStr] = "example_bank_charge_bearer"
shortfall_written_off: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
posting_id: Optional[StrictStr] = "example_posting_id"
allocation_event_receipt_instance = AllocationEventReceipt(investor_record_id=investor_record_id, amount=amount, receipt_date=receipt_date, applied=applied, refund=refund, payment_currency=payment_currency, payment_fx_rate=payment_fx_rate, fx_difference=fx_difference, bank_charge=bank_charge, bank_charge_bearer=bank_charge_bearer, shortfall_written_off=shortfall_written_off, posting_id=posting_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

