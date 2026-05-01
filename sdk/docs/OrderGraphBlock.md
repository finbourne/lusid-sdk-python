# OrderGraphBlock

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block** | [**Block**](Block.md) |  | 
**ordered** | [**OrderGraphBlockOrderSynopsis**](OrderGraphBlockOrderSynopsis.md) |  | 
**placed** | [**OrderGraphBlockPlacementSynopsis**](OrderGraphBlockPlacementSynopsis.md) |  | 
**executed** | [**OrderGraphBlockExecutionSynopsis**](OrderGraphBlockExecutionSynopsis.md) |  | 
**allocated** | [**OrderGraphBlockAllocationSynopsis**](OrderGraphBlockAllocationSynopsis.md) |  | 
**booked** | [**OrderGraphBlockTransactionSynopsis**](OrderGraphBlockTransactionSynopsis.md) |  | 
**derived_state** | **str** | A simple description of the overall state of a block. | 
**derived_compliance_state** | **str** | The overall compliance state of a block, derived from the block&#39;s orders. Available values: Pending, Failed, Passed, ManuallyApproved, PartiallyOverridden, Warning. | 
**derived_approval_state** | **str** | The overall approval state of a block, derived from approval of the block&#39;s orders. Available values: Pending, Rejected, Approved. | 
## Example

```python
from lusid.models.order_graph_block import OrderGraphBlock
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

block: Block
ordered: OrderGraphBlockOrderSynopsis
placed: OrderGraphBlockPlacementSynopsis
executed: OrderGraphBlockExecutionSynopsis
allocated: OrderGraphBlockAllocationSynopsis
booked: OrderGraphBlockTransactionSynopsis
derived_state: StrictStr = "example_derived_state"
derived_compliance_state: StrictStr = "example_derived_compliance_state"
derived_approval_state: StrictStr = "example_derived_approval_state"
order_graph_block_instance = OrderGraphBlock(block=block, ordered=ordered, placed=placed, executed=executed, allocated=allocated, booked=booked, derived_state=derived_state, derived_compliance_state=derived_compliance_state, derived_approval_state=derived_approval_state)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

