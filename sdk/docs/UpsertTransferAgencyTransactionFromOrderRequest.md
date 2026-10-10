# UpsertTransferAgencyTransactionFromOrderRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | [**ResourceId**](ResourceId.md) |  | 
**price_date** | **datetime** |  | 
## Example

```python
from lusid.models.upsert_transfer_agency_transaction_from_order_request import UpsertTransferAgencyTransactionFromOrderRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

order_id: ResourceId = # Replace with your value
price_date: datetime = # Replace with your value
upsert_transfer_agency_transaction_from_order_request_instance = UpsertTransferAgencyTransactionFromOrderRequest(order_id=order_id, price_date=price_date)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

