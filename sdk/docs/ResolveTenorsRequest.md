# ResolveTenorsRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** |  | 
**calendars** | [**List[ResourceId]**](ResourceId.md) |  | 
**spot_days** | **int** |  | 
**tenors** | **List[str]** |  | 
**business_day_convention** | **str** | Available values: NoAdjustment, None, Previous, P, Following, F, ModifiedPrevious, MP, ModifiedFollowing, MF, HalfMonthModifiedFollowing, Nearest, Invalid. | [optional] 
**eom_rule** | **str** |  | [optional] 
**as_at** | **datetime** |  | [optional] 
## Example

```python
from lusid.models.resolve_tenors_request import ResolveTenorsRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

start_date: datetime = # Replace with your value
calendars: List[ResourceId]
spot_days: StrictInt = # Replace with your value
spot_days: StrictInt = 42
tenors: List[StrictStr]
business_day_convention: Optional[StrictStr] = "example_business_day_convention"
eom_rule: Optional[StrictStr] = "example_eom_rule"
as_at: Optional[datetime] = # Replace with your value
resolve_tenors_request_instance = ResolveTenorsRequest(start_date=start_date, calendars=calendars, spot_days=spot_days, tenors=tenors, business_day_convention=business_day_convention, eom_rule=eom_rule, as_at=as_at)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

