# PaymentInstructionsResponse

The response from upserting a set of Payment Instructions. Each request key from the  incoming map appears in exactly one of Successes or Failed.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**successes** | [**Dict[str, PaymentInstruction]**](PaymentInstruction.md) | The Payment Instructions that were created or updated successfully, keyed by the ephemeral request key supplied by the caller. | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | Details of the requests that failed, keyed by the ephemeral request key supplied by the caller. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.payment_instructions_response import PaymentInstructionsResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

successes: Optional[Dict[str, PaymentInstruction]] = # Replace with your value
failed: Optional[Dict[str, ErrorDetail]] = # Replace with your value
links: Optional[List[Link]] = None
payment_instructions_response_instance = PaymentInstructionsResponse(successes=successes, failed=failed, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

