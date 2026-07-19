# FundStructure

Definition of the structure of a fund
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**id** | [**ResourceId**](ResourceId.md) |  | 
**name** | **str** | The display name of the Fund Structure. | 
**description** | **str** | An optional description for the Fund Structure. | [optional] 
**funds** | [**List[Fund]**](Fund.md) | An optional list of existing funds to be incorporated as part of the structure. | [optional] 
**allocation_groups** | [**List[AllocationGroup]**](AllocationGroup.md) | An optional list of Allocation Groups that can apply across a Fund Structure. Only classes and feeder funds linked to the master fund specified are allowed. | [optional] 
**nodes** | [**List[FundStructureNode]**](FundStructureNode.md) | The list of nodes that make up the Fund Structure, each referencing a Fund and defining its role. | 
**edges** | [**List[FundStructureEdge]**](FundStructureEdge.md) | The list of edges that define the relationships between feeder and master nodes in the structure. | 
**version** | [**Version**](Version.md) |  | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | A set of properties to decorate onto the Fund Structure. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.fund_structure import FundStructure
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

href: Optional[StrictStr] = "example_href"
id: ResourceId
name: StrictStr = "example_name"
description: Optional[StrictStr] = "example_description"
funds: Optional[List[Fund]] = # Replace with your value
allocation_groups: Optional[List[AllocationGroup]] = # Replace with your value
nodes: List[FundStructureNode] = # Replace with your value
edges: List[FundStructureEdge] = # Replace with your value
version: Optional[Version] = None
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
links: Optional[List[Link]] = None
fund_structure_instance = FundStructure(href=href, id=id, name=name, description=description, funds=funds, allocation_groups=allocation_groups, nodes=nodes, edges=edges, version=version, properties=properties, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

