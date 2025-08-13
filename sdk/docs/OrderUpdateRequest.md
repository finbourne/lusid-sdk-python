# OrderUpdateRequest

A request to create or update a Order.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**quantity** | **float** | The quantity of the given instrument ordered. | [optional] 
**portfolio_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | Client-defined properties associated with this order. | [optional] 
**price** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**limit_price** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**stop_price** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**var_date** | **datetime** | The date on which the order was made | [optional] 
**side** | **str** | The client&#39;s representation of the order&#39;s side (buy, sell, short, etc) | [optional] 
## Example

```python
from lusid.models.order_update_request import OrderUpdateRequest
from typing import Any, Dict, Optional, Union
from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt, constr
from datetime import datetime
id: ResourceId = # Replace with your value
quantity: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
portfolio_id: Optional[ResourceId] = # Replace with your value
properties: Optional[Dict[str, PerpetualProperty]] = # Replace with your value
price: Optional[CurrencyAndAmount] = None
limit_price: Optional[CurrencyAndAmount] = # Replace with your value
stop_price: Optional[CurrencyAndAmount] = # Replace with your value
var_date: Optional[datetime] = # Replace with your value
side: Optional[StrictStr] = "example_side"
order_update_request_instance = OrderUpdateRequest(id=id, quantity=quantity, portfolio_id=portfolio_id, properties=properties, price=price, limit_price=limit_price, stop_price=stop_price, var_date=var_date, side=side)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

