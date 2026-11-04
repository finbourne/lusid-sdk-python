# PreviewBlocksRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**orders** | [**List[OrderRequest]**](OrderRequest.md) | The orders to group into blocks. Properties in the Block domain are taken as the block&#39;s properties and form part of the grouping key. | 
**grouping_mode** | **str** | How orders are grouped. None: one block per order. SameSide: orders sharing instrument, side, type, time in force, price (for Limit and Stop), basis, date and block properties share a block. CrossSide: as SameSide but ignoring side, so opposing orders may net into one block, provided each portfolio&#39;s net for the instrument has the same sign as the block&#39;s first portfolio. Available values: None, SameSide, CrossSide. | [optional] 
**block_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
## Example

```python
from lusid.models.preview_blocks_request import PreviewBlocksRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

orders: List[OrderRequest] = # Replace with your value
grouping_mode: Optional[StrictStr] = "example_grouping_mode"
block_id: Optional[ResourceId] = # Replace with your value
preview_blocks_request_instance = PreviewBlocksRequest(orders=orders, grouping_mode=grouping_mode, block_id=block_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

