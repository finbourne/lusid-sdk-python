# GetTransferRequest

The transfer to read. Every part of its identity is required: a transfer is identified by its scope, its code  and the two portfolios its in and out transaction are booked into.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transfer_id** | [**ResourceId**](ResourceId.md) |  | 
**portfolio_id_out** | [**ResourceId**](ResourceId.md) |  | 
**portfolio_id_in** | [**ResourceId**](ResourceId.md) |  | 
**property_keys** | **List[str]** |  | [optional] 
## Example

```python
from lusid.models.get_transfer_request import GetTransferRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

transfer_id: ResourceId = # Replace with your value
portfolio_id_out: ResourceId = # Replace with your value
portfolio_id_in: ResourceId = # Replace with your value
property_keys: Optional[List[StrictStr]] = # Replace with your value
get_transfer_request_instance = GetTransferRequest(transfer_id=transfer_id, portfolio_id_out=portfolio_id_out, portfolio_id_in=portfolio_id_in, property_keys=property_keys)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

