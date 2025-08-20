# GetReferencePortfolioConstituentsResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_from** | **datetime** |  | 
**weight_type** | **str** | The available values are: Static, Floating, Periodical | 
**period_type** | **str** | The available values are: Daily, Weekly, Monthly, Quarterly, Annually | [optional] 
**period_count** | **int** |  | [optional] 
**constituents** | [**List[ReferencePortfolioConstituent]**](ReferencePortfolioConstituent.md) | Set of constituents (instrument/weight pairings) | 
**href** | **str** | The Uri that returns the same result as the original request, but may include resolved as at time(s). | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.get_reference_portfolio_constituents_response import GetReferencePortfolioConstituentsResponse
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictInt, StrictStr, conlist, validator
from datetime import datetime
effective_from: datetime = # Replace with your value
weight_type: StrictStr = "example_weight_type"
period_type: Optional[StrictStr] = "example_period_type"
period_count: Optional[StrictInt] = # Replace with your value
period_count: Optional[StrictInt] = None
constituents: conlist(ReferencePortfolioConstituent) = # Replace with your value
href: Optional[StrictStr] = "example_href"
links: Optional[conlist(Link)] = None
get_reference_portfolio_constituents_response_instance = GetReferencePortfolioConstituentsResponse(effective_from=effective_from, weight_type=weight_type, period_type=period_type, period_count=period_count, constituents=constituents, href=href, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

