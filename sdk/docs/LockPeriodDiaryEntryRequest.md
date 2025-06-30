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
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, constr, validator

diary_entry_code: Optional[StrictStr] = "example_diary_entry_code"
closing_options: Optional[conlist(StrictStr)] = # Replace with your value
lock_period_diary_entry_request_instance = LockPeriodDiaryEntryRequest(diary_entry_code=diary_entry_code, closing_options=closing_options)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

