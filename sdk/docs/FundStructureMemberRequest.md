# FundStructureMemberRequest

A member to add to a Fund Structure: the node, and the links that join it to members already in the structure.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node** | [**FundStructureNode**](FundStructureNode.md) |  | 
**edges** | [**List[FundStructureEdge]**](FundStructureEdge.md) | The links joining the new node to members already in the structure. May be empty for a member that is linked later. | [optional] 
## Example

```python
from lusid.models.fund_structure_member_request import FundStructureMemberRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

node: FundStructureNode
edges: Optional[List[FundStructureEdge]] = # Replace with your value
fund_structure_member_request_instance = FundStructureMemberRequest(node=node, edges=edges)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

