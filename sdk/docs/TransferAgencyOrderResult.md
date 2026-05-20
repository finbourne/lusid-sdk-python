# TransferAgencyOrderResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**transaction_id** | **str** |  | [optional] 
## Example

```python
from lusid.models.transfer_agency_order_result import TransferAgencyOrderResult
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

order_id: Optional[ResourceId] = # Replace with your value
transaction_id: Optional[StrictStr] = "example_transaction_id"
transfer_agency_order_result_instance = TransferAgencyOrderResult(order_id=order_id, transaction_id=transaction_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

