# ClosePeriodDiaryEntryRequest

A definition for the period you wish to close
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**diary_entry_code** | **str** | Unique code assigned to a period. When left blank a code will be created by the system in the format &#39;yyyyMMDD&#39;. | [optional] 
**name** | **str** | Identifiable Name assigned to the period. Where left blank, the system will generate a name in the format &#39;yyyyMMDD&#39;. | [optional] 
**effective_at** | **datetime** | The effective time of the diary entry. | [optional] 
**query_as_at** | **datetime** | The query time of the diary entry. Defaults to latest. | [optional] 
**status** | **str** | The status of a Diary Entry of Type &#39;PeriodBoundary&#39;. Defaults to &#39;Estimate&#39; when closing a period, and supports &#39;Estimate&#39; and &#39;Final&#39; for closing periods and &#39;Final&#39; for locking periods. | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | A set of properties for the diary entry. | [optional] 
**closing_options** | **List[str]** | The options which will be executed once a period is closed or locked. | [optional] 
## Example

```python
from lusid.models.close_period_diary_entry_request import ClosePeriodDiaryEntryRequest
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, constr, validator
from datetime import datetime
diary_entry_code: Optional[StrictStr] = "example_diary_entry_code"
name: Optional[StrictStr] = "example_name"
effective_at: Optional[datetime] = # Replace with your value
query_as_at: Optional[datetime] = # Replace with your value
status: Optional[StrictStr] = "example_status"
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
closing_options: Optional[conlist(StrictStr)] = # Replace with your value
close_period_diary_entry_request_instance = ClosePeriodDiaryEntryRequest(diary_entry_code=diary_entry_code, name=name, effective_at=effective_at, query_as_at=query_as_at, status=status, properties=properties, closing_options=closing_options)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

