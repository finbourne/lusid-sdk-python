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
**allocation_groups** | [**List[AllocationGroup]**](AllocationGroup.md) | An optional list of Allocation Groups that can apply across a Fund Structure. A group may span the share classes of a member and the members that invest into it through dedicated share class links. | [optional] 
**nodes** | [**List[FundStructureNode]**](FundStructureNode.md) | The list of nodes that make up the Fund Structure, each referencing a Fund and defining its role. May be empty on create, with members added later through the members endpoint. | 
**edges** | [**List[FundStructureEdge]**](FundStructureEdge.md) | The list of edges that define how the members of the structure are linked: a member investing into a dedicated share class of another, or holding an equity, GP, LP or carry interest in another through an instrument. | 
**role_data_type_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**nav_type_codes** | **List[str]** | The NAV types every member of the structure produces, by code. Declaring them once here gives the structure a shared Timeline. At least one is required, and every member fund must define a NAV type with each of these codes. | [optional] 
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
role_data_type_id: Optional[ResourceId] = # Replace with your value
nav_type_codes: Optional[List[StrictStr]] = # Replace with your value
version: Optional[Version] = None
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
links: Optional[List[Link]] = None
fund_structure_instance = FundStructure(href=href, id=id, name=name, description=description, funds=funds, allocation_groups=allocation_groups, nodes=nodes, edges=edges, role_data_type_id=role_data_type_id, nav_type_codes=nav_type_codes, version=version, properties=properties, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

