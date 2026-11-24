# FundGroupReportResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fund_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**nav_type_code** | **str** | The code of the NAV type the row, or result, was produced for. | [optional] 
**status** | **str** | Whether the fund was reported. Available values: Succeeded, Failed. | [optional] 
**valuation_points** | [**List[FundGroupReportValuationPoint]**](FundGroupReportValuationPoint.md) | The valuation points reported for the fund and NAV type, oldest first. Empty when it failed. | [optional] 
**error** | [**ErrorDetail**](ErrorDetail.md) |  | [optional] 
## Example

```python
from lusid.models.fund_group_report_result import FundGroupReportResult
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

fund_id: Optional[ResourceId] = # Replace with your value
nav_type_code: Optional[StrictStr] = "example_nav_type_code"
status: Optional[StrictStr] = "example_status"
valuation_points: Optional[List[FundGroupReportValuationPoint]] = # Replace with your value
error: Optional[ErrorDetail] = None
fund_group_report_result_instance = FundGroupReportResult(fund_id=fund_id, nav_type_code=nav_type_code, status=status, valuation_points=valuation_points, error=error)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

