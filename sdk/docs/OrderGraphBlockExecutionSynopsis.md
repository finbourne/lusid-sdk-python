# OrderGraphBlockExecutionSynopsis

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **float** | Total number of units executed. | 
**details** | [**List[OrderGraphBlockExecutionDetail]**](OrderGraphBlockExecutionDetail.md) | Identifiers for each execution in this block. | 
## Example

```python
from lusid.models.order_graph_block_execution_synopsis import OrderGraphBlockExecutionSynopsis
from typing import Any, Dict, List, Union
from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt, conlist

quantity: Union[StrictFloat, StrictInt] = # Replace with your value
details: conlist(OrderGraphBlockExecutionDetail) = # Replace with your value
order_graph_block_execution_synopsis_instance = OrderGraphBlockExecutionSynopsis(quantity=quantity, details=details)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

