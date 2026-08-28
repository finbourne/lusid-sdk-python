# DeleteTransferAgencyOrdersResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**successes** | [**Dict[str, DeleteTransferAgencyOrderResult]**](DeleteTransferAgencyOrderResult.md) | A dictionary of successfully deleted orders, keyed by the request key. | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | A dictionary of failed order deletion attempts, keyed by the request key, containing error details. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.delete_transfer_agency_orders_response import DeleteTransferAgencyOrdersResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

successes: Optional[Dict[str, DeleteTransferAgencyOrderResult]] = # Replace with your value
failed: Optional[Dict[str, ErrorDetail]] = # Replace with your value
links: Optional[List[Link]] = None
delete_transfer_agency_orders_response_instance = DeleteTransferAgencyOrdersResponse(successes=successes, failed=failed, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

