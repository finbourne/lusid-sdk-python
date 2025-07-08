# OrderInstruction

Record of an order instruction
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**created_date** | **datetime** | The active date of this order instruction. | 
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | Client-defined properties associated with this execution. | [optional] 
**portfolio_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**instrument_identifiers** | **Dict[str, str]** | The instrument ordered. | 
**quantity** | **float** | The quantity of given instrument ordered. | [optional] 
**weight** | **float** | The proportion of the total portfolio value ordered for the given instrument ordered. | [optional] 
**price** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**instrument_scope** | **str** | The scope in which the instrument lies | [optional] 
**lusid_instrument_id** | **str** | The LUSID instrument id for the instrument ordered. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.order_instruction import OrderInstruction
from typing import Any, Dict, List, Optional, Union
from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt, StrictStr, conlist
from datetime import datetime
id: ResourceId = # Replace with your value
created_date: datetime = # Replace with your value
properties: Optional[Dict[str, PerpetualProperty]] = # Replace with your value
portfolio_id: Optional[ResourceId] = # Replace with your value
instrument_identifiers: Dict[str, StrictStr] = # Replace with your value
quantity: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
weight: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
price: Optional[CurrencyAndAmount] = None
instrument_scope: Optional[StrictStr] = "example_instrument_scope"
lusid_instrument_id: Optional[StrictStr] = "example_lusid_instrument_id"
version: Optional[Version] = None
links: Optional[conlist(Link)] = None
order_instruction_instance = OrderInstruction(id=id, created_date=created_date, properties=properties, portfolio_id=portfolio_id, instrument_identifiers=instrument_identifiers, quantity=quantity, weight=weight, price=price, instrument_scope=instrument_scope, lusid_instrument_id=lusid_instrument_id, version=version, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

