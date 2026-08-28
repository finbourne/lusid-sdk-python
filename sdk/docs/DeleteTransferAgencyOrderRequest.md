# DeleteTransferAgencyOrderRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | [**ResourceId**](ResourceId.md) |  | 
## Example

```python
from lusid.models.delete_transfer_agency_order_request import DeleteTransferAgencyOrderRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

order_id: ResourceId = # Replace with your value
delete_transfer_agency_order_request_instance = DeleteTransferAgencyOrderRequest(order_id=order_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

