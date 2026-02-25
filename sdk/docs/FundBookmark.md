# FundBookmark

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The unique Code of the Calendar Entry. The Calendar Entry, together with the Fund Scope and Code, uniquely identifies a Fund Calendar Entry. | 
**display_name** | **str** | The name of the Fund Calendar entry. | 
**description** | **str** | A description for the Fund Calendar entry. | [optional] 
**nav_type_code** | **str** | The navTypeCode of the Fund Calendar Entry. This is the code of the NAV type that this Calendar Entry is associated with. | 
**timeline_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**previous_entry** | [**PreviousFundCalendarEntry**](PreviousFundCalendarEntry.md) |  | [optional] 
**effective_at** | **datetime** | The effective at of the Calendar Entry. | [optional] 
**as_at** | **datetime** | The asAt datetime for the Calendar Entry. | 
**entry_type** | **str** | The type of the Fund Calendar Entry. The available values are: ValuationPointFundCalendarEntry, BookmarkFundCalendarEntry | 
**status** | **str** | The status of the Fund Calendar Entry. Can be &#39;Estimate&#39;, &#39;Unofficial&#39; or &#39;Final&#39;. | [optional] 
**apply_clear_down** | **bool** | Set to true if that closed period should have the clear down applied. | [optional] 
**holdings_as_at_override** | **datetime** | The optional AsAt Override to use for building holdings in the Valuation Point. Defaults to Latest. | [optional] 
**valuations_as_at_override** | **datetime** | The optional AsAt Override to use for performing valuations in the Valuation Point. Defaults to Latest. | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | The properties for the Calendar Entry. These will be from the &#39;ClosedPeriod&#39; domain. | [optional] 
**version** | [**Version**](Version.md) |  | 
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested asAt datetime. | [optional] 
**leader_nav_type_code** | **str** | The code of the Nav Type that this Nav Type will follow when set. | [optional] 
**fund_calendar_entries_type** | **str** | The type of the Calendar Entry. The available values are: FinalisedValuationPoint, FundEstimateValuationPoint, FundBookmark | 
## Example

```python
from lusid.models.fund_bookmark import FundBookmark
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

code: StrictStr = "example_code"
display_name: StrictStr = "example_display_name"
description: Optional[StrictStr] = "example_description"
nav_type_code: StrictStr = "example_nav_type_code"
timeline_id: Optional[ResourceId] = # Replace with your value
previous_entry: Optional[PreviousFundCalendarEntry] = # Replace with your value
effective_at: Optional[datetime] = # Replace with your value
as_at: datetime = # Replace with your value
entry_type: StrictStr = "example_entry_type"
status: Optional[StrictStr] = "example_status"
apply_clear_down: Optional[StrictBool] = # Replace with your value
apply_clear_down:Optional[StrictBool] = None
holdings_as_at_override: Optional[datetime] = # Replace with your value
valuations_as_at_override: Optional[datetime] = # Replace with your value
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
version: Version
href: Optional[StrictStr] = "example_href"
leader_nav_type_code: Optional[StrictStr] = "example_leader_nav_type_code"
fund_calendar_entries_type: StrictStr = "example_fund_calendar_entries_type"
fund_bookmark_instance = FundBookmark(code=code, display_name=display_name, description=description, nav_type_code=nav_type_code, timeline_id=timeline_id, previous_entry=previous_entry, effective_at=effective_at, as_at=as_at, entry_type=entry_type, status=status, apply_clear_down=apply_clear_down, holdings_as_at_override=holdings_as_at_override, valuations_as_at_override=valuations_as_at_override, properties=properties, version=version, href=href, leader_nav_type_code=leader_nav_type_code, fund_calendar_entries_type=fund_calendar_entries_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

