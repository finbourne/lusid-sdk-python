# OrderRequest

A request to create or update an Order.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | Client-defined properties associated with this order. | [optional] 
**instrument_identifiers** | **Dict[str, str]** | The instrument ordered. | 
**quantity** | **float** | The quantity of the given instrument ordered. | [optional] 
**side** | **str** | The client&#39;s representation of the order&#39;s side (buy, sell, short, etc) | 
**order_book_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**portfolio_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**id** | [**ResourceId**](ResourceId.md) |  | 
**state** | **str** | The order&#39;s state (examples: New, PartiallyFilled, ...) | [optional] 
**type** | **str** | The order&#39;s type (examples: Limit, Market, ...) | [optional] 
**time_in_force** | **str** | The order&#39;s time in force (examples: Day, GoodTilCancel, ...) | [optional] 
**var_date** | **datetime** | The date on which the order was made | [optional] 
**price** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**limit_price** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**stop_price** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**order_instruction** | [**ResourceId**](ResourceId.md) |  | [optional] 
**package** | [**ResourceId**](ResourceId.md) |  | [optional] 
**weight** | **float** | The proportion of the total portfolio value ordered for the given instrument ordered. | [optional] 
**amount** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
## Example

```python
from lusid.models.order_request import OrderRequest
from typing import Any, Dict, Optional, Union
from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt, StrictStr, constr
from datetime import datetime
properties: Optional[Dict[str, PerpetualProperty]] = # Replace with your value
instrument_identifiers: Dict[str, StrictStr] = # Replace with your value
quantity: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
side: StrictStr = "example_side"
order_book_id: Optional[ResourceId] = # Replace with your value
portfolio_id: Optional[ResourceId] = # Replace with your value
id: ResourceId = # Replace with your value
state: Optional[StrictStr] = "example_state"
type: Optional[StrictStr] = "example_type"
time_in_force: Optional[StrictStr] = "example_time_in_force"
var_date: Optional[datetime] = # Replace with your value
price: Optional[CurrencyAndAmount] = None
limit_price: Optional[CurrencyAndAmount] = # Replace with your value
stop_price: Optional[CurrencyAndAmount] = # Replace with your value
order_instruction: Optional[ResourceId] = # Replace with your value
package: Optional[ResourceId] = None
weight: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
amount: Optional[CurrencyAndAmount] = None
order_request_instance = OrderRequest(properties=properties, instrument_identifiers=instrument_identifiers, quantity=quantity, side=side, order_book_id=order_book_id, portfolio_id=portfolio_id, id=id, state=state, type=type, time_in_force=time_in_force, var_date=var_date, price=price, limit_price=limit_price, stop_price=stop_price, order_instruction=order_instruction, package=package, weight=weight, amount=amount)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

