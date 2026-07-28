# PaymentInstruction

A Payment Instruction groups one or more Payment Records into a single block  for transmission to a downstream treasury management system via the Horizon integration.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**payment_record_ids** | [**List[PaymentRecordReference]**](PaymentRecordReference.md) | One or more Payment Records batched into this instruction block. All referenced Payment Records must share the same currency as the top-level currency field. | 
**currency** | **str** | ISO 4217 currency code. All referenced Payment Records must share this currency value. | 
**total_payment_amount** | **float** | Total payment amount across all referenced Payment Records. | 
**payment_date** | **datetime** | The value date on which settlement is due. ISO 8601 date. | 
**payor_payment_details_reference** | [**PaymentDetailsReferenceResponse**](PaymentDetailsReferenceResponse.md) |  | 
**payee_payment_details_reference** | [**PaymentDetailsReferenceResponse**](PaymentDetailsReferenceResponse.md) |  | 
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | Client-defined properties associated with this Payment Instruction. | [optional] 
**status** | [**PaymentInstructionStatus**](PaymentInstructionStatus.md) |  | 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.payment_instruction import PaymentInstruction
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: ResourceId
payment_record_ids: List[PaymentRecordReference] = # Replace with your value
currency: StrictStr = "example_currency"
total_payment_amount: Union[StrictFloat, StrictInt] = # Replace with your value
payment_date: datetime = # Replace with your value
payor_payment_details_reference: PaymentDetailsReferenceResponse = # Replace with your value
payee_payment_details_reference: PaymentDetailsReferenceResponse = # Replace with your value
properties: Optional[Dict[str, PerpetualProperty]] = # Replace with your value
status: PaymentInstructionStatus
version: Optional[Version] = None
links: Optional[List[Link]] = None
payment_instruction_instance = PaymentInstruction(id=id, payment_record_ids=payment_record_ids, currency=currency, total_payment_amount=total_payment_amount, payment_date=payment_date, payor_payment_details_reference=payor_payment_details_reference, payee_payment_details_reference=payee_payment_details_reference, properties=properties, status=status, version=version, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

