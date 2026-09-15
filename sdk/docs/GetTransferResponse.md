# GetTransferResponse

A transfer and both of the transactions it booked.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transfer_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**transfer_type** | **str** |  | [optional] 
**portfolio_id_out** | [**ResourceId**](ResourceId.md) |  | [optional] 
**portfolio_id_in** | [**ResourceId**](ResourceId.md) |  | [optional] 
**transaction_out** | [**Transaction**](Transaction.md) |  | [optional] 
**transaction_in** | [**Transaction**](Transaction.md) |  | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) |  | [optional] 
## Example

```python
from lusid.models.get_transfer_response import GetTransferResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

transfer_id: Optional[ResourceId] = # Replace with your value
transfer_type: Optional[StrictStr] = "example_transfer_type"
portfolio_id_out: Optional[ResourceId] = # Replace with your value
portfolio_id_in: Optional[ResourceId] = # Replace with your value
transaction_out: Optional[Transaction] = # Replace with your value
transaction_in: Optional[Transaction] = # Replace with your value
properties: Optional[Dict[str, ModelProperty]] = None
get_transfer_response_instance = GetTransferResponse(transfer_id=transfer_id, transfer_type=transfer_type, portfolio_id_out=portfolio_id_out, portfolio_id_in=portfolio_id_in, transaction_out=transaction_out, transaction_in=transaction_in, properties=properties)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

