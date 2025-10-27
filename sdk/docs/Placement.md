# Placement

A street order for a quantity of a single instrument placed with a single market entity.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**parent_placement_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**block_ids** | [**List[ResourceId]**](ResourceId.md) | The IDs of the Blocks associated with this placement. | 
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | Client-defined properties associated with this placement. | [optional] 
**instrument_identifiers** | **Dict[str, Optional[str]]** | The instrument ordered. | 
**lusid_instrument_id** | **str** | The LUSID instrument id for the instrument placement. | 
**quantity** | **float** | The quantity of given instrument ordered. | 
**state** | **str** | The state of this placement (typically a FIX state; Open, Filled, etc). | 
**side** | **str** | The side (Buy, Sell, ...) of this placement. | 
**time_in_force** | **str** | The time in force applicable to this placement (GTC, FOK, Day, etc) | 
**type** | **str** | The type of this placement (Market, Limit, etc). | 
**created_date** | **datetime** | The active date of this placement. | 
**limit_price** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**stop_price** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**counterparty** | **str** | Optionally specifies the market entity this placement is placed with. | [optional] 
**execution_system** | **str** | Optionally specifies the execution system in use. | [optional] 
**entry_type** | **str** | Optionally specifies the entry type of this placement. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**data_model_membership** | [**DataModelMembership**](DataModelMembership.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.placement import Placement
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: ResourceId
parent_placement_id: Optional[ResourceId] = # Replace with your value
block_ids: List[ResourceId] = # Replace with your value
properties: Optional[Dict[str, PerpetualProperty]] = # Replace with your value
instrument_identifiers: Dict[str, Optional[StrictStr]] = # Replace with your value
lusid_instrument_id: StrictStr = "example_lusid_instrument_id"
quantity: Union[StrictFloat, StrictInt] = # Replace with your value
state: StrictStr = "example_state"
side: StrictStr = "example_side"
time_in_force: StrictStr = "example_time_in_force"
type: StrictStr = "example_type"
created_date: datetime = # Replace with your value
limit_price: Optional[CurrencyAndAmount] = # Replace with your value
stop_price: Optional[CurrencyAndAmount] = # Replace with your value
counterparty: Optional[StrictStr] = "example_counterparty"
execution_system: Optional[StrictStr] = "example_execution_system"
entry_type: Optional[StrictStr] = "example_entry_type"
version: Optional[Version] = None
data_model_membership: Optional[DataModelMembership] = # Replace with your value
links: Optional[List[Link]] = None
placement_instance = Placement(id=id, parent_placement_id=parent_placement_id, block_ids=block_ids, properties=properties, instrument_identifiers=instrument_identifiers, lusid_instrument_id=lusid_instrument_id, quantity=quantity, state=state, side=side, time_in_force=time_in_force, type=type, created_date=created_date, limit_price=limit_price, stop_price=stop_price, counterparty=counterparty, execution_system=execution_system, entry_type=entry_type, version=version, data_model_membership=data_model_membership, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

