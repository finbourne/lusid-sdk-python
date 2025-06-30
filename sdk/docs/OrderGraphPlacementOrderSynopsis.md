# OrderGraphPlacementOrderSynopsis

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details** | [**List[OrderGraphPlacementOrderDetail]**](OrderGraphPlacementOrderDetail.md) | Identifiers for each order in the block. | 
## Example

```python
from lusid.models.order_graph_placement_order_synopsis import OrderGraphPlacementOrderSynopsis
from typing import Any, Dict, List
from pydantic.v1 import BaseModel, Field, conlist

details: conlist(OrderGraphPlacementOrderDetail) = # Replace with your value
order_graph_placement_order_synopsis_instance = OrderGraphPlacementOrderSynopsis(details=details)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

