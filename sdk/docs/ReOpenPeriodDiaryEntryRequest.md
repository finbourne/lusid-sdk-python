# ReOpenPeriodDiaryEntryRequest

A definition for the period you wish to re open
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**diary_entry_code** | **str** | Unique code assigned to a period. When left blank last period will be used. | [optional] 
## Example

```python
from lusid.models.re_open_period_diary_entry_request import ReOpenPeriodDiaryEntryRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

diary_entry_code: Optional[StrictStr] = "example_diary_entry_code"
re_open_period_diary_entry_request_instance = ReOpenPeriodDiaryEntryRequest(diary_entry_code=diary_entry_code)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

