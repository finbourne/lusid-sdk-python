# FundStructureEdgeTarget

The member a link points at, and for a dedicated share class link the share class on that member.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node** | **str** | The node code of the member the link points at. | 
**share_class_short_code** | **str** | The short code of the share class on the target member that the source invests into. Required for a DedicatedShareClass link and not allowed on any other. | [optional] 
## Example

```python
from lusid.models.fund_structure_edge_target import FundStructureEdgeTarget
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

node: StrictStr = "example_node"
share_class_short_code: Optional[StrictStr] = "example_share_class_short_code"
fund_structure_edge_target_instance = FundStructureEdgeTarget(node=node, share_class_short_code=share_class_short_code)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

