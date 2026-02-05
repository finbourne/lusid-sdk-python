# OrderGraphBlockAllocationDetail

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**allocated_order_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**quantity** | **float** | The quantity of this allocation, with direction relative to the containing block. | 
## Example

```python
from lusid.models.order_graph_block_allocation_detail import OrderGraphBlockAllocationDetail
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: ResourceId
allocated_order_id: Optional[ResourceId] = # Replace with your value
quantity: Union[StrictFloat, StrictInt] = # Replace with your value
order_graph_block_allocation_detail_instance = OrderGraphBlockAllocationDetail(id=id, allocated_order_id=allocated_order_id, quantity=quantity)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

