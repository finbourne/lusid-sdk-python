# OrderGraphPlacementOrderSynopsis

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details** | [**List[OrderGraphPlacementOrderDetail]**](OrderGraphPlacementOrderDetail.md) | Identifiers for each order in the block. | 
## Example

```python
from lusid.models.order_graph_placement_order_synopsis import OrderGraphPlacementOrderSynopsis
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

details: List[OrderGraphPlacementOrderDetail] = # Replace with your value
order_graph_placement_order_synopsis_instance = OrderGraphPlacementOrderSynopsis(details=details)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

