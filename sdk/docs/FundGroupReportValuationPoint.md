# FundGroupReportValuationPoint

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**diary_entry_code** | **str** | The code of the valuation point the row was produced for. | [optional] 
**status** | **str** | The status of the valuation point the row was produced for, such as Final or Estimate. | [optional] 
**effective_end** | **datetime** | The effective end date of the valuation point the row was produced for. | [optional] 
## Example

```python
from lusid.models.fund_group_report_valuation_point import FundGroupReportValuationPoint
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

diary_entry_code: Optional[StrictStr] = "example_diary_entry_code"
status: Optional[StrictStr] = "example_status"
effective_end: Optional[datetime] = # Replace with your value
fund_group_report_valuation_point_instance = FundGroupReportValuationPoint(diary_entry_code=diary_entry_code, status=status, effective_end=effective_end)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

