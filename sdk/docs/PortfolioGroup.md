# PortfolioGroup

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**id** | [**ResourceId**](ResourceId.md) |  | 
**display_name** | **str** | The name of the portfolio group. | 
**description** | **str** | The long form description of the portfolio group. | [optional] 
**created** | **datetime** | The effective datetime at which the portfolio group was created. No portfolios or sub groups can be added to the group before this date. | [optional] 
**portfolios** | [**List[ResourceId]**](ResourceId.md) | The collection of resource identifiers for the portfolios contained in the portfolio group. | [optional] 
**sub_groups** | [**List[ResourceId]**](ResourceId.md) | The collection of resource identifiers for the portfolio groups contained in the portfolio group as sub groups. | [optional] 
**relationships** | [**List[Relationship]**](Relationship.md) | A set of relationships associated to the portfolio group. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.portfolio_group import PortfolioGroup
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, constr
from datetime import datetime
href: Optional[StrictStr] = "example_href"
id: ResourceId = # Replace with your value
display_name: StrictStr = "example_display_name"
description: Optional[StrictStr] = "example_description"
created: Optional[datetime] = # Replace with your value
portfolios: Optional[conlist(ResourceId)] = # Replace with your value
sub_groups: Optional[conlist(ResourceId)] = # Replace with your value
relationships: Optional[conlist(Relationship)] = # Replace with your value
version: Optional[Version] = None
links: Optional[conlist(Link)] = None
portfolio_group_instance = PortfolioGroup(href=href, id=id, display_name=display_name, description=description, created=created, portfolios=portfolios, sub_groups=sub_groups, relationships=relationships, version=version, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

