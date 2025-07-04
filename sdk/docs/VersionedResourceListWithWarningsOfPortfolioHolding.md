# VersionedResourceListWithWarningsOfPortfolioHolding

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | [**Version**](Version.md) |  | 
**values** | [**List[PortfolioHolding]**](PortfolioHolding.md) | The resources to list. | 
**href** | **str** | The URI of the resource list. | [optional] 
**next_page** | **str** | The next page of results. | [optional] 
**previous_page** | **str** | The previous page of results. | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.versioned_resource_list_with_warnings_of_portfolio_holding import VersionedResourceListWithWarningsOfPortfolioHolding
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist

version: Version = # Replace with your value
values: conlist(PortfolioHolding) = # Replace with your value
href: Optional[StrictStr] = "example_href"
next_page: Optional[StrictStr] = "example_next_page"
previous_page: Optional[StrictStr] = "example_previous_page"
warnings: Optional[conlist(Warning)] = None
links: Optional[conlist(Link)] = None
versioned_resource_list_with_warnings_of_portfolio_holding_instance = VersionedResourceListWithWarningsOfPortfolioHolding(version=version, values=values, href=href, next_page=next_page, previous_page=previous_page, warnings=warnings, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

