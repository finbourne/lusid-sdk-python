# BlockAndOrdersRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_id** | [**ResourceId**](ResourceId.md) |  | 
**orders** | [**List[BlockedOrderRequest]**](BlockedOrderRequest.md) | An order which belongs to a block. Fields common to both entities (such as instrument) should be derived from the block. | 
**block_properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | Client-defined properties associated with this block. | [optional] 
**instrument_identifiers** | **Dict[str, Optional[str]]** | The instrument ordered. | 
**side** | **str** | The client&#39;s representation of the block&#39;s side (buy, sell, short, etc). BlockedOrders in the request which do not specify a side will have their side populated with this value. | [optional] 
**type** | **str** | The block order&#39;s type (examples: Limit, Market, ...) | [optional] 
**time_in_force** | **str** | The block orders&#39; time in force (examples: Day, GoodTilCancel, ...) | [optional] 
**var_date** | **datetime** | The date on which the block was made | [optional] 
**limit_price** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**stop_price** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
## Example

```python
from lusid.models.block_and_orders_request import BlockAndOrdersRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

block_id: ResourceId = # Replace with your value
orders: List[BlockedOrderRequest] = # Replace with your value
block_properties: Optional[Dict[str, PerpetualProperty]] = # Replace with your value
instrument_identifiers: Dict[str, Optional[StrictStr]] = # Replace with your value
side: Optional[StrictStr] = "example_side"
type: Optional[StrictStr] = "example_type"
time_in_force: Optional[StrictStr] = "example_time_in_force"
var_date: Optional[datetime] = # Replace with your value
limit_price: Optional[CurrencyAndAmount] = # Replace with your value
stop_price: Optional[CurrencyAndAmount] = # Replace with your value
block_and_orders_request_instance = BlockAndOrdersRequest(block_id=block_id, orders=orders, block_properties=block_properties, instrument_identifiers=instrument_identifiers, side=side, type=type, time_in_force=time_in_force, var_date=var_date, limit_price=limit_price, stop_price=stop_price)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

