# GetReferencePortfolioConstituentsResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_from** | **datetime** |  | 
**weight_type** | **str** | The available values are: Static, Floating, Periodical | 
**period_type** | **str** | The available values are: Daily, Weekly, Monthly, Quarterly, Annually | [optional] 
**period_count** | **int** |  | [optional] 
**constituents** | [**List[ReferencePortfolioConstituent]**](ReferencePortfolioConstituent.md) | Set of constituents (instrument/weight pairings) | 
**href** | **str** | The Uri that returns the same result as the original request,  but may include resolved as at time(s). | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.get_reference_portfolio_constituents_response import GetReferencePortfolioConstituentsResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

effective_from: datetime = # Replace with your value
weight_type: StrictStr = "example_weight_type"
period_type: Optional[StrictStr] = "example_period_type"
period_count: Optional[StrictInt] = # Replace with your value
period_count: Optional[StrictInt] = None
constituents: List[ReferencePortfolioConstituent] = # Replace with your value
href: Optional[StrictStr] = "example_href"
links: Optional[List[Link]] = None
get_reference_portfolio_constituents_response_instance = GetReferencePortfolioConstituentsResponse(effective_from=effective_from, weight_type=weight_type, period_type=period_type, period_count=period_count, constituents=constituents, href=href, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

