# FundStructureEdge

A directed edge in a Fund Structure, defining a relationship from a feeder node to a master node share class.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **str** | The node code of the feeder node that is the source of this relationship. | 
**to** | [**FundStructureEdgeTarget**](FundStructureEdgeTarget.md) |  | 
## Example

```python
from lusid.models.fund_structure_edge import FundStructureEdge
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

var_from: StrictStr = "example_var_from"
to: FundStructureEdgeTarget
fund_structure_edge_instance = FundStructureEdge(var_from=var_from, to=to)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

