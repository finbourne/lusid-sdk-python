# FundStructureRequest

The request used to create a Fund Structure.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The code of the Fund Structure. | 
**name** | **str** | The display name of the Fund Structure. | 
**description** | **str** | An optional description for the Fund Structure. | [optional] 
**existing_funds** | [**List[ResourceId]**](ResourceId.md) | An optional list of existing funds to be incorporated as part of the structure. | [optional] 
**new_funds** | [**List[FundDefinitionRequest]**](FundDefinitionRequest.md) | An optional list of Fund definitions to be created inline as part of the structure. | [optional] 
**allocation_groups** | [**List[AllocationGroup]**](AllocationGroup.md) | An optional list of Allocation Groups that can apply across a Fund Structure. Only classes and feeder funds linked to the master fund specified are allowed. | [optional] 
**nodes** | [**List[FundStructureNode]**](FundStructureNode.md) | The list of nodes that make up the Fund Structure, each referencing a Fund and defining its role. | 
**edges** | [**List[FundStructureEdge]**](FundStructureEdge.md) | The list of edges that define the relationships between feeder and master nodes in the structure. | 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | A set of properties to decorate onto the Fund Structure. | [optional] 
## Example

```python
from lusid.models.fund_structure_request import FundStructureRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

code: StrictStr = "example_code"
name: StrictStr = "example_name"
description: Optional[StrictStr] = "example_description"
existing_funds: Optional[List[ResourceId]] = # Replace with your value
new_funds: Optional[List[FundDefinitionRequest]] = # Replace with your value
allocation_groups: Optional[List[AllocationGroup]] = # Replace with your value
nodes: List[FundStructureNode] = # Replace with your value
edges: List[FundStructureEdge] = # Replace with your value
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
fund_structure_request_instance = FundStructureRequest(code=code, name=name, description=description, existing_funds=existing_funds, new_funds=new_funds, allocation_groups=allocation_groups, nodes=nodes, edges=edges, properties=properties)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

