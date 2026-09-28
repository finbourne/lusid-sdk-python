# FundStructureRequest

The request used to create a Fund Structure.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The code of the Fund Structure. | 
**name** | **str** | The display name of the Fund Structure. | 
**description** | **str** | An optional description for the Fund Structure. | [optional] 
**existing_funds** | [**List[ResourceId]**](ResourceId.md) | An optional list of existing funds to be incorporated as part of the structure. | [optional] 
**allocation_groups** | [**List[AllocationGroup]**](AllocationGroup.md) | An optional list of Allocation Groups that can apply across a Fund Structure. A group may span the share classes of a member and the members that invest into it through dedicated share class links. | [optional] 
**nodes** | [**List[FundStructureNode]**](FundStructureNode.md) | The list of nodes that make up the Fund Structure, each referencing a Fund and defining its role. May be empty on create, with members added later through the members endpoint. | [optional] 
**edges** | [**List[FundStructureEdge]**](FundStructureEdge.md) | The list of edges that define how the members of the structure are linked: a member investing into a dedicated share class of another, or holding an equity, GP, LP or carry interest in another through an instrument. | [optional] 
**effective_at** | **datetime** | The effective datetime from which the Fund Structure applies. Defaults to the beginning of time if not specified, so that the structure is visible at every effective datetime. | [optional] 
**role_data_type_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**nav_type_codes** | **List[str]** | The NAV types every member of the structure produces, by code. Declaring them once here gives the structure a shared Timeline. At least one is required, and every member fund must define a NAV type with each of these codes. | 
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
allocation_groups: Optional[List[AllocationGroup]] = # Replace with your value
nodes: Optional[List[FundStructureNode]] = # Replace with your value
edges: Optional[List[FundStructureEdge]] = # Replace with your value
effective_at: Optional[datetime] = # Replace with your value
role_data_type_id: Optional[ResourceId] = # Replace with your value
nav_type_codes: List[StrictStr] = # Replace with your value
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
fund_structure_request_instance = FundStructureRequest(code=code, name=name, description=description, existing_funds=existing_funds, allocation_groups=allocation_groups, nodes=nodes, edges=edges, effective_at=effective_at, role_data_type_id=role_data_type_id, nav_type_codes=nav_type_codes, properties=properties)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

