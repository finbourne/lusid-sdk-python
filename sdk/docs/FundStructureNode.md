# FundStructureNode

A node in a Fund Structure, representing a Fund and its role within the structure.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_code** | **str** | A unique identifier for this node within the Fund Structure. | 
**fund_scope** | **str** | The scope of the Fund referenced by this node. | 
**fund_code** | **str** | The code of the Fund referenced by this node. | 
**role** | **str** | The role of this node within the structure. Available values: Master, Feeder. | 
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
fund_structure_node_instance = FundStructureNode(node_code=node_code, fund_scope=fund_scope, fund_code=fund_code, role=role)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

