# DeleteTransferAgencyOrderResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**cancelled_transaction_ids** | **List[str]** |  | [optional] 
## Example

```python
from lusid.models.delete_transfer_agency_order_result import DeleteTransferAgencyOrderResult
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

order_id: Optional[ResourceId] = # Replace with your value
cancelled_transaction_ids: Optional[List[StrictStr]] = # Replace with your value
delete_transfer_agency_order_result_instance = DeleteTransferAgencyOrderResult(order_id=order_id, cancelled_transaction_ids=cancelled_transaction_ids)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

