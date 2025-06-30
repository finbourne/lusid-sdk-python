# PortfolioSearchResult

A list of portfolios.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**type** | **str** | The type of the portfolio. The available values are: Transaction, Reference, DerivedTransaction, SimplePosition | 
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**description** | **str** | The long form description of the portfolio. | [optional] 
**display_name** | **str** | The name of the portfolio. | 
**is_derived** | **bool** | Whether or not this is a derived portfolio. | [optional] [readonly] 
**created** | **datetime** | The effective datetime at which the portfolio was created. No transactions or constituents can be added to the portfolio before this date. | 
**parent_portfolio_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**base_currency** | **str** | The base currency of the portfolio. | [optional] 
**properties** | [**List[ModelProperty]**](ModelProperty.md) | The requested portfolio properties. These will be from the &#39;Portfolio&#39; domain. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.portfolio_search_result import PortfolioSearchResult
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictBool, StrictStr, conlist, constr, validator
from datetime import datetime
id: ResourceId = # Replace with your value
type: StrictStr = "example_type"
href: Optional[StrictStr] = "example_href"
description: Optional[StrictStr] = "example_description"
display_name: StrictStr = "example_display_name"
is_derived: Optional[StrictBool] = # Replace with your value
is_derived:Optional[StrictBool] = None
created: datetime = # Replace with your value
parent_portfolio_id: Optional[ResourceId] = # Replace with your value
base_currency: Optional[StrictStr] = "example_base_currency"
properties: Optional[conlist(ModelProperty)] = # Replace with your value
links: Optional[conlist(Link)] = None
portfolio_search_result_instance = PortfolioSearchResult(id=id, type=type, href=href, description=description, display_name=display_name, is_derived=is_derived, created=created, parent_portfolio_id=parent_portfolio_id, base_currency=base_currency, properties=properties, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

