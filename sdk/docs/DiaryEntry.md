# DiaryEntry

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**abor_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**diary_entry_code** | **str** | The code of the diary entry. | [optional] 
**type** | **str** | The type of the diary entry. | 
**name** | **str** | The name of the diary entry. | [optional] 
**status** | **str** | The status of the diary entry. Statuses are constrained and defaulted by &#39;Type&#39; specified.   Type &#39;Other&#39; defaults to &#39;Undefined&#39; and supports &#39;Undefined&#39;, &#39;Estimate&#39;, &#39;Candidate&#39;, and &#39;Final&#39;.  Type &#39;PeriodBoundary&#39; defaults to &#39;Estimate&#39; when closing a period, and supports &#39;Estimate&#39; and &#39;Final&#39; for closing periods and &#39;Final&#39; for locking periods.  Type &#39;ValuationPoint&#39; defaults to &#39;Estimate&#39; when upserting a diary entry, moves to &#39;Candidate&#39; or &#39;Final&#39; when a ValuationPoint is accepted, and &#39;Final&#39; when it is finalised. | 
**apply_clear_down** | **bool** | Defaults to false. Set to true if you want that the closed period to have the clear down applied. | [optional] 
**effective_at** | **datetime** | The effective time of the diary entry. | 
**query_as_at** | **datetime** | The query time of the diary entry. Defaults to latest. | [optional] 
**previous_entry_time** | **datetime** | The entry time of the previous diary entry. | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | A set of properties for the diary entry. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.diary_entry import DiaryEntry
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictBool, StrictStr, conlist, constr, validator
from datetime import datetime
href: Optional[StrictStr] = "example_href"
abor_id: Optional[ResourceId] = # Replace with your value
diary_entry_code: Optional[StrictStr] = "example_diary_entry_code"
type: StrictStr = "example_type"
name: Optional[StrictStr] = "example_name"
status: StrictStr = "example_status"
apply_clear_down: Optional[StrictBool] = # Replace with your value
apply_clear_down:Optional[StrictBool] = None
effective_at: datetime = # Replace with your value
query_as_at: Optional[datetime] = # Replace with your value
previous_entry_time: Optional[datetime] = # Replace with your value
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
version: Optional[Version] = None
links: Optional[conlist(Link)] = None
diary_entry_instance = DiaryEntry(href=href, abor_id=abor_id, diary_entry_code=diary_entry_code, type=type, name=name, status=status, apply_clear_down=apply_clear_down, effective_at=effective_at, query_as_at=query_as_at, previous_entry_time=previous_entry_time, properties=properties, version=version, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

