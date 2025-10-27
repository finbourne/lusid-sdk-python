# OrderGraphBlockPlacementSynopsis

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **float** | Total number of units placed. | 
**quantity_by_state** | **Dict[str, float]** | Total number of units placed. | [optional] 
**details** | [**List[OrderGraphBlockPlacementDetail]**](OrderGraphBlockPlacementDetail.md) | Identifiers for each placement in this block. | 
## Example

```python
from lusid.models.order_graph_block_placement_synopsis import OrderGraphBlockPlacementSynopsis
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

quantity: Union[StrictFloat, StrictInt] = # Replace with your value
quantity_by_state: Optional[Dict[str, Union[StrictFloat, StrictInt]]] = # Replace with your value
details: List[OrderGraphBlockPlacementDetail] = # Replace with your value
order_graph_block_placement_synopsis_instance = OrderGraphBlockPlacementSynopsis(quantity=quantity, quantity_by_state=quantity_by_state, details=details)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

