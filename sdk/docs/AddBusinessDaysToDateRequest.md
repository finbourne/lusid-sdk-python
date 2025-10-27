# AddBusinessDaysToDateRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_day_offset** | **int** |  | 
**holiday_codes** | **List[str]** |  | 
**start_date** | **datetime** |  | [optional] 
**as_at** | **datetime** |  | [optional] 
## Example

```python
from lusid.models.add_business_days_to_date_request import AddBusinessDaysToDateRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

business_day_offset: StrictInt = # Replace with your value
business_day_offset: StrictInt = 42
holiday_codes: List[StrictStr] = # Replace with your value
start_date: Optional[datetime] = # Replace with your value
as_at: Optional[datetime] = # Replace with your value
add_business_days_to_date_request_instance = AddBusinessDaysToDateRequest(business_day_offset=business_day_offset, holiday_codes=holiday_codes, start_date=start_date, as_at=as_at)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

