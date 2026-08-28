# CreateTransferResponse

The transfer that was created, and the transaction legs it booked.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transfer_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**transfer_type** | **str** |  | [optional] 
**portfolio_id_out** | [**ResourceId**](ResourceId.md) |  | [optional] 
**portfolio_id_in** | [**ResourceId**](ResourceId.md) |  | [optional] 
**transaction_id_out** | **str** |  | [optional] 
**transaction_id_in** | **str** |  | [optional] 
## Example

```python
from lusid.models.create_transfer_response import CreateTransferResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

transfer_id: Optional[ResourceId] = # Replace with your value
transfer_type: Optional[StrictStr] = "example_transfer_type"
portfolio_id_out: Optional[ResourceId] = # Replace with your value
portfolio_id_in: Optional[ResourceId] = # Replace with your value
transaction_id_out: Optional[StrictStr] = "example_transaction_id_out"
transaction_id_in: Optional[StrictStr] = "example_transaction_id_in"
create_transfer_response_instance = CreateTransferResponse(transfer_id=transfer_id, transfer_type=transfer_type, portfolio_id_out=portfolio_id_out, portfolio_id_in=portfolio_id_in, transaction_id_out=transaction_id_out, transaction_id_in=transaction_id_in)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

