# OrderGraphPlacementPlacementSynopsis

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details** | [**List[OrderGraphPlacementChildPlacementDetail]**](OrderGraphPlacementChildPlacementDetail.md) | Identifiers for each child placement for this placement. | 
**quantity** | **float** | Total number of units placed. | 
## Example

```python
from lusid.models.order_graph_placement_placement_synopsis import OrderGraphPlacementPlacementSynopsis
from typing import Any, Dict, List, Union
from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt, conlist

details: conlist(OrderGraphPlacementChildPlacementDetail) = # Replace with your value
quantity: Union[StrictFloat, StrictInt] = # Replace with your value
order_graph_placement_placement_synopsis_instance = OrderGraphPlacementPlacementSynopsis(details=details, quantity=quantity)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

