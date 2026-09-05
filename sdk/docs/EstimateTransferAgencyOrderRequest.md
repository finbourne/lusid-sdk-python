# EstimateTransferAgencyOrderRequest

A request to estimate the values of one order. `OrderId` is required whether or not the order has been  saved, because it is the identity the estimate is returned against. Supply `Order` to estimate values  that differ from - or do not yet exist in - the saved order.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | [**ResourceId**](ResourceId.md) |  | 
**order** | [**TransferAgencyOrderToEstimate**](TransferAgencyOrderToEstimate.md) |  | [optional] 
## Example

```python
from lusid.models.estimate_transfer_agency_order_request import EstimateTransferAgencyOrderRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

order_id: ResourceId = # Replace with your value
order: Optional[TransferAgencyOrderToEstimate] = None
estimate_transfer_agency_order_request_instance = EstimateTransferAgencyOrderRequest(order_id=order_id, order=order)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

