# OrderGraphBlockAllocationSynopsis

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **float** | Total number of units allocated. | 
**details** | [**List[OrderGraphBlockAllocationDetail]**](OrderGraphBlockAllocationDetail.md) | Identifiers for each allocation in this block. | 
## Example

```python
from lusid.models.order_graph_block_allocation_synopsis import OrderGraphBlockAllocationSynopsis
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

quantity: Union[StrictFloat, StrictInt] = # Replace with your value
details: List[OrderGraphBlockAllocationDetail] = # Replace with your value
order_graph_block_allocation_synopsis_instance = OrderGraphBlockAllocationSynopsis(quantity=quantity, details=details)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

