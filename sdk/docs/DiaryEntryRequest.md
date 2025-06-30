# DiaryEntryRequest

The request to add a diary entry
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**diary_entry_code** | **str** | The code of the diary entry. | 
**name** | **str** | The name of the diary entry. | [optional] 
**status** | **str** | The status of a Diary Entry of Type &#39;Other&#39;. Defaults to &#39;Undefined&#39; and supports &#39;Undefined&#39;, &#39;Estimate&#39;, &#39;Candidate&#39;, and &#39;Final&#39;. | [optional] 
**effective_at** | **datetime** | The effective time of the diary entry. | 
**query_as_at** | **datetime** | The query time of the diary entry. Defaults to latest. | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | A set of properties for the diary entry. | [optional] 
## Example

```python
from lusid.models.diary_entry_request import DiaryEntryRequest
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, constr, validator
from datetime import datetime
diary_entry_code: StrictStr = "example_diary_entry_code"
name: Optional[StrictStr] = "example_name"
status: Optional[StrictStr] = "example_status"
effective_at: datetime = # Replace with your value
query_as_at: Optional[datetime] = # Replace with your value
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
diary_entry_request_instance = DiaryEntryRequest(diary_entry_code=diary_entry_code, name=name, status=status, effective_at=effective_at, query_as_at=query_as_at, properties=properties)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

