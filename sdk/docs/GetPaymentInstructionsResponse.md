# GetPaymentInstructionsResponse

The response from getting Payment Instructions by payment record id. Each requested payment record id  appears in exactly one of Values or Failed.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**Dict[str, PaymentInstruction]**](PaymentInstruction.md) | The Payment Instructions that were found, keyed by the payment record id used to retrieve them. Only Payment Instructions that were found will be contained in this collection. | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | The payment record ids that did not resolve to a Payment Instruction, along with the nature of the failure. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.get_payment_instructions_response import GetPaymentInstructionsResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

values: Optional[Dict[str, PaymentInstruction]] = # Replace with your value
failed: Optional[Dict[str, ErrorDetail]] = # Replace with your value
links: Optional[List[Link]] = None
get_payment_instructions_response_instance = GetPaymentInstructionsResponse(values=values, failed=failed, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

