# OrderGraphPlacementExecutionSynopsis

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **float** | Total number of units executed. | 
**details** | [**List[OrderGraphPlacementExecutionDetail]**](OrderGraphPlacementExecutionDetail.md) | Identifiers info for each execution against this placement. | 
## Example

```python
from lusid.models.order_graph_placement_execution_synopsis import OrderGraphPlacementExecutionSynopsis
from typing import Any, Dict, List, Union
from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt, conlist

quantity: Union[StrictFloat, StrictInt] = # Replace with your value
details: conlist(OrderGraphPlacementExecutionDetail) = # Replace with your value
order_graph_placement_execution_synopsis_instance = OrderGraphPlacementExecutionSynopsis(quantity=quantity, details=details)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

