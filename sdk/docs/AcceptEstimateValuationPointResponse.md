# AcceptEstimateValuationPointResponse

The Valuation Point Data Response for AcceptEstimate called on the Fund and specified date.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**candidate_valuation_point** | [**ValuationPointDataResponse**](ValuationPointDataResponse.md) |  | 
**latest_valuation_point** | [**ValuationPointDataResponse**](ValuationPointDataResponse.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.accept_estimate_valuation_point_response import AcceptEstimateValuationPointResponse
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist

href: Optional[StrictStr] = "example_href"
candidate_valuation_point: ValuationPointDataResponse = # Replace with your value
latest_valuation_point: Optional[ValuationPointDataResponse] = # Replace with your value
links: Optional[conlist(Link)] = None
accept_estimate_valuation_point_response_instance = AcceptEstimateValuationPointResponse(href=href, candidate_valuation_point=candidate_valuation_point, latest_valuation_point=latest_valuation_point, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

