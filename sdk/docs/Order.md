# Order

An Order for a certain quantity of a specific instrument
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | Client-defined properties associated with this order. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**instrument_identifiers** | **Dict[str, Optional[str]]** | The instrument ordered. | 
**quantity** | **float** | The quantity of the given instrument ordered. | [optional] 
**side** | **str** | The client&#39;s representation of the order&#39;s side (buy, sell, short, etc) | 
**order_book_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**portfolio_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**id** | [**ResourceId**](ResourceId.md) |  | 
**instrument_scope** | **str** | The scope in which the instrument lies | [optional] 
**lusid_instrument_id** | **str** | The LUSID instrument id for the instrument ordered. | 
**state** | **str** | The order&#39;s state (examples: New, PartiallyFilled, ...) | [optional] 
**type** | **str** | The order&#39;s type (examples: Limit, Market, ...) | [optional] 
**time_in_force** | **str** | The order&#39;s time in force (examples: Day, GoodTilCancel, ...) | [optional] 
**var_date** | **datetime** | The date on which the order was made | [optional] 
**price** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**limit_price** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**stop_price** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**order_instruction_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**package_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**weight** | **float** | The proportion of the total portfolio value ordered for the given instrument ordered. | [optional] 
**amount** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**data_model_membership** | [**DataModelMembership**](DataModelMembership.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.order import Order
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

properties: Optional[Dict[str, PerpetualProperty]] = # Replace with your value
version: Optional[Version] = None
instrument_identifiers: Dict[str, Optional[StrictStr]] = # Replace with your value
quantity: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
side: StrictStr = "example_side"
order_book_id: Optional[ResourceId] = # Replace with your value
portfolio_id: Optional[ResourceId] = # Replace with your value
id: ResourceId
instrument_scope: Optional[StrictStr] = "example_instrument_scope"
lusid_instrument_id: StrictStr = "example_lusid_instrument_id"
state: Optional[StrictStr] = "example_state"
type: Optional[StrictStr] = "example_type"
time_in_force: Optional[StrictStr] = "example_time_in_force"
var_date: Optional[datetime] = # Replace with your value
price: Optional[CurrencyAndAmount] = None
limit_price: Optional[CurrencyAndAmount] = # Replace with your value
stop_price: Optional[CurrencyAndAmount] = # Replace with your value
order_instruction_id: Optional[ResourceId] = # Replace with your value
package_id: Optional[ResourceId] = # Replace with your value
weight: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
amount: Optional[CurrencyAndAmount] = None
data_model_membership: Optional[DataModelMembership] = # Replace with your value
links: Optional[List[Link]] = None
order_instance = Order(properties=properties, version=version, instrument_identifiers=instrument_identifiers, quantity=quantity, side=side, order_book_id=order_book_id, portfolio_id=portfolio_id, id=id, instrument_scope=instrument_scope, lusid_instrument_id=lusid_instrument_id, state=state, type=type, time_in_force=time_in_force, var_date=var_date, price=price, limit_price=limit_price, stop_price=stop_price, order_instruction_id=order_instruction_id, package_id=package_id, weight=weight, amount=amount, data_model_membership=data_model_membership, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

