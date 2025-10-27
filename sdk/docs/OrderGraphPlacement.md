# OrderGraphPlacement

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**placement** | [**Placement**](Placement.md) |  | 
**block_id** | [**ResourceId**](ResourceId.md) |  | 
**ordered** | [**OrderGraphPlacementOrderSynopsis**](OrderGraphPlacementOrderSynopsis.md) |  | 
**placed** | [**OrderGraphPlacementPlacementSynopsis**](OrderGraphPlacementPlacementSynopsis.md) |  | 
**executed** | [**OrderGraphPlacementExecutionSynopsis**](OrderGraphPlacementExecutionSynopsis.md) |  | 
**allocated** | [**OrderGraphPlacementAllocationSynopsis**](OrderGraphPlacementAllocationSynopsis.md) |  | 
**derived_state** | **str** | A simple description of the overall state of a placement. | 
**calculated_average_price** | **float** | Average price realised on executions for a given placement | [optional] 
## Example

```python
from lusid.models.order_graph_placement import OrderGraphPlacement
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

placement: Placement
block_id: ResourceId = # Replace with your value
ordered: OrderGraphPlacementOrderSynopsis
placed: OrderGraphPlacementPlacementSynopsis
executed: OrderGraphPlacementExecutionSynopsis
allocated: OrderGraphPlacementAllocationSynopsis
derived_state: StrictStr = "example_derived_state"
calculated_average_price: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
order_graph_placement_instance = OrderGraphPlacement(placement=placement, block_id=block_id, ordered=ordered, placed=placed, executed=executed, allocated=allocated, derived_state=derived_state, calculated_average_price=calculated_average_price)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

