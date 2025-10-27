# BlockedOrderRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | Client-defined properties associated with this order. | [optional] 
**quantity** | **float** | The quantity of the given instrument ordered. | 
**order_book_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**portfolio_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**id** | [**ResourceId**](ResourceId.md) |  | 
**state** | **str** | The order&#39;s state (examples: New, PartiallyFilled, ...) | [optional] 
**var_date** | **datetime** | The date on which the order was made | [optional] 
**price** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**order_instruction** | [**ResourceId**](ResourceId.md) |  | [optional] 
**package** | [**ResourceId**](ResourceId.md) |  | [optional] 
**side** | **str** | The client&#39;s representation of the order&#39;s side (buy, sell, short, etc) | [optional] 
## Example

```python
from lusid.models.blocked_order_request import BlockedOrderRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

properties: Optional[Dict[str, PerpetualProperty]] = # Replace with your value
quantity: Union[StrictFloat, StrictInt] = # Replace with your value
order_book_id: Optional[ResourceId] = # Replace with your value
portfolio_id: Optional[ResourceId] = # Replace with your value
id: ResourceId
state: Optional[StrictStr] = "example_state"
var_date: Optional[datetime] = # Replace with your value
price: Optional[CurrencyAndAmount] = None
order_instruction: Optional[ResourceId] = # Replace with your value
package: Optional[ResourceId] = None
side: Optional[StrictStr] = "example_side"
blocked_order_request_instance = BlockedOrderRequest(properties=properties, quantity=quantity, order_book_id=order_book_id, portfolio_id=portfolio_id, id=id, state=state, var_date=var_date, price=price, order_instruction=order_instruction, package=package, side=side)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

