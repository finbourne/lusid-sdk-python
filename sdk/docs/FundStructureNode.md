# FundStructureNode

A node in a Fund Structure, representing a Fund and its role within the structure.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_code** | **str** | A unique identifier for this node within the Fund Structure. | 
**fund_scope** | **str** | The scope of the Fund referenced by this node. | 
**fund_code** | **str** | The code of the Fund referenced by this node. | 
**role** | **str** | The role of this node within the structure. Must be one of the acceptable values of the structure&#39;s role data type. | 
**allocation_basis** | [**FundStructureAllocationBasis**](FundStructureAllocationBasis.md) |  | [optional] 
**pnl_flow_mode** | **str** | How this member&#39;s profit and loss reaches the member that holds it. Set on the held member, not on the holder: it has no effect on a member no edge holds. EquityPickup (the default) leaves the holder revaluing its position in this member; BucketFlowThrough passes the holder one line per economic bucket, tagged with its origin; TransactionFlowThrough passes the holder every line, tagged with its origin and path. Available values: EquityPickup, BucketFlowThrough, TransactionFlowThrough. | [optional] 
**allocation_map_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**drift_materiality** | [**FundStructureDriftMateriality**](FundStructureDriftMateriality.md) |  | [optional] 
## Example

```python
from lusid.models.fund_structure_node import FundStructureNode
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

node_code: StrictStr = "example_node_code"
fund_scope: StrictStr = "example_fund_scope"
fund_code: StrictStr = "example_fund_code"
role: StrictStr = "example_role"
allocation_basis: Optional[FundStructureAllocationBasis] = # Replace with your value
pnl_flow_mode: Optional[StrictStr] = "example_pnl_flow_mode"
allocation_map_id: Optional[ResourceId] = # Replace with your value
drift_materiality: Optional[FundStructureDriftMateriality] = # Replace with your value
fund_structure_node_instance = FundStructureNode(node_code=node_code, fund_scope=fund_scope, fund_code=fund_code, role=role, allocation_basis=allocation_basis, pnl_flow_mode=pnl_flow_mode, allocation_map_id=allocation_map_id, drift_materiality=drift_materiality)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

