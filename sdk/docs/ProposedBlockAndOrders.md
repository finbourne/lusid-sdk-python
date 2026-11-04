# ProposedBlockAndOrders

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**BlockAndOrdersRequest**](BlockAndOrdersRequest.md) |  | [optional] 
**net_quantity** | **float** | The block&#39;s quantity, netted by direction, where any order is quantity-based. | [optional] 
**net_amount** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
## Example

```python
from lusid.models.proposed_block_and_orders import ProposedBlockAndOrders
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

request: Optional[BlockAndOrdersRequest] = None
net_quantity: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
net_amount: Optional[CurrencyAndAmount] = # Replace with your value
proposed_block_and_orders_instance = ProposedBlockAndOrders(request=request, net_quantity=net_quantity, net_amount=net_amount)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

