# CancelTransferAgencyTransactionRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**portfolio_id** | [**ResourceId**](ResourceId.md) |  | 
**transaction_id** | **str** |  | 
## Example

```python
from lusid.models.cancel_transfer_agency_transaction_request import CancelTransferAgencyTransactionRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

portfolio_id: ResourceId = # Replace with your value
transaction_id: StrictStr = "example_transaction_id"
cancel_transfer_agency_transaction_request_instance = CancelTransferAgencyTransactionRequest(portfolio_id=portfolio_id, transaction_id=transaction_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

