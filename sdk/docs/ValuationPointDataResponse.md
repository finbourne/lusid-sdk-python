# ValuationPointDataResponse

The Valuation Point Data Response for the Fund and specified date.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**type** | **str** | The Type of the associated Diary Entry (&#39;PeriodBoundary&#39;,&#39;ValuationPoint&#39;,&#39;Other&#39; or &#39;Adhoc&#39; when a diary entry wasn&#39;t used). | 
**status** | **str** | The status of a Diary Entry of Type &#39;ValuationPoint&#39;. Defaults to &#39;Estimate&#39; when upserting a diary entry, moves to &#39;Candidate&#39; or &#39;Final&#39; when a ValuationPoint is accepted, and &#39;Final&#39; when it is finalised. The status of a Diary Entry becomes &#39;Unofficial&#39; when a diary entry wasn&#39;t used. | 
**fund_details** | [**FundDetails**](FundDetails.md) |  | 
**fund_valuation_point_data** | [**FundValuationPointData**](FundValuationPointData.md) |  | 
**share_class_data** | [**List[ShareClassData]**](ShareClassData.md) | The data for all share classes in fund. Share classes are identified by their short codes. | 
**valuation_point_code** | **str** | The code of the valuation point. | [optional] 
**previous_valuation_point_code** | **str** | The code of the previous valuation point. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.valuation_point_data_response import ValuationPointDataResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

href: Optional[StrictStr] = "example_href"
type: StrictStr = "example_type"
status: StrictStr = "example_status"
fund_details: FundDetails = # Replace with your value
fund_valuation_point_data: FundValuationPointData = # Replace with your value
share_class_data: List[ShareClassData] = # Replace with your value
valuation_point_code: Optional[StrictStr] = "example_valuation_point_code"
previous_valuation_point_code: Optional[StrictStr] = "example_previous_valuation_point_code"
links: Optional[List[Link]] = None
valuation_point_data_response_instance = ValuationPointDataResponse(href=href, type=type, status=status, fund_details=fund_details, fund_valuation_point_data=fund_valuation_point_data, share_class_data=share_class_data, valuation_point_code=valuation_point_code, previous_valuation_point_code=previous_valuation_point_code, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

