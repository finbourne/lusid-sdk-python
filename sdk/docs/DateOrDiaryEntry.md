# DateOrDiaryEntry

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** | A date. If specified, DiaryEntry must not be specified. | [optional] 
**diary_entry** | **str** | The code of a diary entry. If specified, Date must not be specified. | [optional] 
## Example

```python
from lusid.models.date_or_diary_entry import DateOrDiaryEntry
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, constr, validator

var_date: Optional[StrictStr] = "example_var_date"
diary_entry: Optional[StrictStr] = "example_diary_entry"
date_or_diary_entry_instance = DateOrDiaryEntry(var_date=var_date, diary_entry=diary_entry)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

