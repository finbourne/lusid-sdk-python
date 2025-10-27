# ExpandedGroup

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**id** | [**ResourceId**](ResourceId.md) |  | 
**display_name** | **str** | The name of the portfolio group. | 
**description** | **str** | The long form description of the portfolio group. | [optional] 
**values** | [**List[CompletePortfolio]**](CompletePortfolio.md) | The collection of resource identifiers for the portfolios contained in the portfolio group. | [optional] 
**sub_groups** | [**List[ExpandedGroup]**](ExpandedGroup.md) | The collection of resource identifiers for the portfolio groups contained in the portfolio group as sub groups. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.expanded_group import ExpandedGroup
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

href: Optional[StrictStr] = "example_href"
id: ResourceId
display_name: StrictStr = "example_display_name"
description: Optional[StrictStr] = "example_description"
values: Optional[List[CompletePortfolio]] = # Replace with your value
sub_groups: Optional[List[ExpandedGroup]] = # Replace with your value
version: Optional[Version] = None
links: Optional[List[Link]] = None
expanded_group_instance = ExpandedGroup(href=href, id=id, display_name=display_name, description=description, values=values, sub_groups=sub_groups, version=version, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

