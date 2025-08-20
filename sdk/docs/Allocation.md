# Allocation

An Allocation of a certain quantity of a specific instrument against an originating Order.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**allocated_order_id** | [**ResourceId**](ResourceId.md) |  | 
**portfolio_id** | [**ResourceId**](ResourceId.md) |  | 
**quantity** | **float** | The quantity of given instrument allocated. | 
**instrument_identifiers** | **Dict[str, str]** | The instrument allocated. | 
**version** | [**Version**](Version.md) |  | [optional] 
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | Client-defined properties associated with this allocation. | [optional] 
**instrument_scope** | **str** | The scope in which the instrument lies | [optional] 
**lusid_instrument_id** | **str** | The LUSID instrument id for the instrument allocated. | 
**placement_ids** | [**List[ResourceId]**](ResourceId.md) | A placement - also known as an order placed in the market - associated with this allocation. | [optional] 
**state** | **str** | The state of this allocation. | [optional] 
**side** | **str** | The side of this allocation (examples: Buy, Sell, ...). | [optional] 
**type** | **str** | The type of order associated with this allocation (examples: Limit, Market, ...). | [optional] 
**settlement_date** | **datetime** | The settlement date for this allocation. | [optional] 
**var_date** | **datetime** | The date of this allocation. | [optional] 
**price** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**settlement_currency** | **str** | The settlement currency of this allocation. | [optional] 
**settlement_currency_fx_rate** | **float** | The settlement currency to allocation currency FX rate. | [optional] 
**counterparty** | **str** | The counterparty for this allocation. | [optional] 
**execution_ids** | [**List[ResourceId]**](ResourceId.md) | The executions associated with this allocation | [optional] 
**data_model_membership** | [**DataModelMembership**](DataModelMembership.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.allocation import Allocation
from typing import Any, Dict, List, Optional, Union
from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt, StrictStr, conlist, constr
from datetime import datetime
id: ResourceId = # Replace with your value
allocated_order_id: ResourceId = # Replace with your value
portfolio_id: ResourceId = # Replace with your value
quantity: Union[StrictFloat, StrictInt] = # Replace with your value
instrument_identifiers: Dict[str, StrictStr] = # Replace with your value
version: Optional[Version] = None
properties: Optional[Dict[str, PerpetualProperty]] = # Replace with your value
instrument_scope: Optional[StrictStr] = "example_instrument_scope"
lusid_instrument_id: StrictStr = "example_lusid_instrument_id"
placement_ids: Optional[conlist(ResourceId)] = # Replace with your value
state: Optional[StrictStr] = "example_state"
side: Optional[StrictStr] = "example_side"
type: Optional[StrictStr] = "example_type"
settlement_date: Optional[datetime] = # Replace with your value
var_date: Optional[datetime] = # Replace with your value
price: Optional[CurrencyAndAmount] = None
settlement_currency: Optional[StrictStr] = "example_settlement_currency"
settlement_currency_fx_rate: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
counterparty: Optional[StrictStr] = "example_counterparty"
execution_ids: Optional[conlist(ResourceId)] = # Replace with your value
data_model_membership: Optional[DataModelMembership] = # Replace with your value
links: Optional[conlist(Link)] = None
allocation_instance = Allocation(id=id, allocated_order_id=allocated_order_id, portfolio_id=portfolio_id, quantity=quantity, instrument_identifiers=instrument_identifiers, version=version, properties=properties, instrument_scope=instrument_scope, lusid_instrument_id=lusid_instrument_id, placement_ids=placement_ids, state=state, side=side, type=type, settlement_date=settlement_date, var_date=var_date, price=price, settlement_currency=settlement_currency, settlement_currency_fx_rate=settlement_currency_fx_rate, counterparty=counterparty, execution_ids=execution_ids, data_model_membership=data_model_membership, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

