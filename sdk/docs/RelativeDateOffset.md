# RelativeDateOffset

Defines a date offset which is relative to some anchor date.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**days** | **int** | The number of days to add to the anchor date. | 
**business_day_convention** | **str** | The adjustment type to apply to dates that fall upon a non-business day, e.g. modified following or following.  Supported string (enumeration) values are: [NoAdjustment, Previous, P, Following, F, ModifiedPrevious, MP, ModifiedFollowing, MF, HalfMonthModifiedFollowing, Nearest]. | 
**day_type** | **str** | Indicates if consideration is given to whether a day is a good business day or not when calculating the offset date.  Supported string (enumeration) values are: [Business, Calendar]. | [optional] 
## Example

```python
from lusid.models.relative_date_offset import RelativeDateOffset
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictInt, StrictStr, constr

days: StrictInt = # Replace with your value
days: StrictInt = 42
business_day_convention: StrictStr = "example_business_day_convention"
day_type: Optional[StrictStr] = "example_day_type"
relative_date_offset_instance = RelativeDateOffset(days=days, business_day_convention=business_day_convention, day_type=day_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

