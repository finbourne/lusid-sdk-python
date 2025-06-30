# UpsertReferencePortfolioConstituentsResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.upsert_reference_portfolio_constituents_response import UpsertReferencePortfolioConstituentsResponse
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, StrictStr, conlist

href: Optional[StrictStr] = "example_href"
version: Optional[Version] = None
links: Optional[conlist(Link)] = None
upsert_reference_portfolio_constituents_response_instance = UpsertReferencePortfolioConstituentsResponse(href=href, version=version, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

