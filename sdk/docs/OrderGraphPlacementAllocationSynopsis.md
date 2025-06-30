# OrderGraphPlacementAllocationSynopsis

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **float** | Total number of units allocated. | 
**details** | [**List[OrderGraphPlacementAllocationDetail]**](OrderGraphPlacementAllocationDetail.md) | Identifiers for each allocation in this placement. | 
## Example

```python
from lusid.models.order_graph_placement_allocation_synopsis import OrderGraphPlacementAllocationSynopsis
from typing import Any, Dict, List, Union
from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt, conlist

quantity: Union[StrictFloat, StrictInt] = # Replace with your value
details: conlist(OrderGraphPlacementAllocationDetail) = # Replace with your value
order_graph_placement_allocation_synopsis_instance = OrderGraphPlacementAllocationSynopsis(quantity=quantity, details=details)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

