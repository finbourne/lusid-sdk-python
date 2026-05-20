# TransferAgencyOrdersResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**successes** | [**Dict[str, TransferAgencyOrderResult]**](TransferAgencyOrderResult.md) | A dictionary of successfully processed orders, keyed by the request key. | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | A dictionary of failed order processing attempts, keyed by the request key, containing error details. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.transfer_agency_orders_response import TransferAgencyOrdersResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

successes: Optional[Dict[str, TransferAgencyOrderResult]] = # Replace with your value
failed: Optional[Dict[str, ErrorDetail]] = # Replace with your value
links: Optional[List[Link]] = None
transfer_agency_orders_response_instance = TransferAgencyOrdersResponse(successes=successes, failed=failed, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

