# LockPeriodDiaryEntryRequest

A definition for the period you wish to lock
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**diary_entry_code** | **str** | Unique code assigned to a period. When left blank last closed period will be located. | [optional] 
**closing_options** | **List[str]** | The options which will be executed once a period is closed or locked. | [optional] 
## Example

```python
from lusid.models.lock_period_diary_entry_request import LockPeriodDiaryEntryRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

diary_entry_code: Optional[StrictStr] = "example_diary_entry_code"
closing_options: Optional[List[StrictStr]] = # Replace with your value
lock_period_diary_entry_request_instance = LockPeriodDiaryEntryRequest(diary_entry_code=diary_entry_code, closing_options=closing_options)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

