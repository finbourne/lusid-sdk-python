# PortfolioGroupSearchResult

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
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.portfolio_group_search_result import PortfolioGroupSearchResult
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

href: Optional[StrictStr] = "example_href"
id: ResourceId
display_name: StrictStr = "example_display_name"
description: Optional[StrictStr] = "example_description"
created: Optional[datetime] = # Replace with your value
portfolios: Optional[List[ResourceId]] = # Replace with your value
sub_groups: Optional[List[ResourceId]] = # Replace with your value
version: Optional[Version] = None
links: Optional[List[Link]] = None
portfolio_group_search_result_instance = PortfolioGroupSearchResult(href=href, id=id, display_name=display_name, description=description, created=created, portfolios=portfolios, sub_groups=sub_groups, version=version, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

