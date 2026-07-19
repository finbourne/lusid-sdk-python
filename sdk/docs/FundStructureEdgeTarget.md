# FundStructureEdgeTarget

The target of a Fund Structure edge, identifying the master node and share class the feeder invests into.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node** | **str** | The node code of the master node that is the target of this relationship. | 
**share_class_short_code** | **str** | The short code of the share class on the master fund that the feeder invests into. | 
## Example

```python
from lusid.models.fund_structure_edge_target import FundStructureEdgeTarget
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

node: StrictStr = "example_node"
share_class_short_code: StrictStr = "example_share_class_short_code"
fund_structure_edge_target_instance = FundStructureEdgeTarget(node=node, share_class_short_code=share_class_short_code)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

