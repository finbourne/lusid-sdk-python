# Block

A block of orders for the same instrument, intended to record for example a trader's aggregation  of outstanding orders at a given time.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**order_ids** | [**List[ResourceId]**](ResourceId.md) | The related order ids. | 
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | Client-defined properties associated with this block. | [optional] 
**instrument_identifiers** | **Dict[str, Optional[str]]** | The instrument ordered. | 
**lusid_instrument_id** | **str** | The LUSID instrument id for the instrument ordered. | 
**quantity** | **float** | The total quantity of given instrument ordered. | 
**side** | **str** | The client&#39;s representation of the block&#39;s side (buy, sell, short, etc) | 
**type** | **str** | The block order&#39;s type (examples: Limit, Market, ...) | 
**time_in_force** | **str** | The block orders&#39; time in force (examples: Day, GoodTilCancel, ...) | 
**created_date** | **datetime** | The date on which the block was made | 
**limit_price** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**stop_price** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**is_swept** | **bool** | Swept blocks are considered no longer of active interest, and no longer take part in various order management processes | 
**version** | [**Version**](Version.md) |  | [optional] 
**data_model_membership** | [**DataModelMembership**](DataModelMembership.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.block import Block
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: ResourceId
order_ids: List[ResourceId] = # Replace with your value
properties: Optional[Dict[str, PerpetualProperty]] = # Replace with your value
instrument_identifiers: Dict[str, Optional[StrictStr]] = # Replace with your value
lusid_instrument_id: StrictStr = "example_lusid_instrument_id"
quantity: Union[StrictFloat, StrictInt] = # Replace with your value
side: StrictStr = "example_side"
type: StrictStr = "example_type"
time_in_force: StrictStr = "example_time_in_force"
created_date: datetime = # Replace with your value
limit_price: Optional[CurrencyAndAmount] = # Replace with your value
stop_price: Optional[CurrencyAndAmount] = # Replace with your value
is_swept: StrictBool = # Replace with your value
is_swept:StrictBool = True
version: Optional[Version] = None
data_model_membership: Optional[DataModelMembership] = # Replace with your value
links: Optional[List[Link]] = None
block_instance = Block(id=id, order_ids=order_ids, properties=properties, instrument_identifiers=instrument_identifiers, lusid_instrument_id=lusid_instrument_id, quantity=quantity, side=side, type=type, time_in_force=time_in_force, created_date=created_date, limit_price=limit_price, stop_price=stop_price, is_swept=is_swept, version=version, data_model_membership=data_model_membership, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

