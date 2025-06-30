# PlacementUpdateRequest

A request to create or update a Placement.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**quantity** | **float** | The quantity of given instrument ordered. | [optional] 
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | Client-defined properties associated with this placement. | [optional] 
**counterparty** | **str** | Optionally specifies the market entity this placement is placed with. | [optional] 
**execution_system** | **str** | Optionally specifies the execution system in use. | [optional] 
**entry_type** | **str** | Optionally specifies the entry type of this placement. | [optional] 
## Example

```python
from lusid.models.placement_update_request import PlacementUpdateRequest
from typing import Any, Dict, Optional, Union
from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt, StrictStr, constr

id: ResourceId = # Replace with your value
quantity: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
properties: Optional[Dict[str, PerpetualProperty]] = # Replace with your value
counterparty: Optional[StrictStr] = "example_counterparty"
execution_system: Optional[StrictStr] = "example_execution_system"
entry_type: Optional[StrictStr] = "example_entry_type"
placement_update_request_instance = PlacementUpdateRequest(id=id, quantity=quantity, properties=properties, counterparty=counterparty, execution_system=execution_system, entry_type=entry_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

