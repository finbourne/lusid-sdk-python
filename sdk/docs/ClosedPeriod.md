# ClosedPeriod

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**closed_period_id** | **str** | The unique Id of the Closed Period. The ClosedPeriodId, together with the Timeline Scope and Code, uniquely identifies a Closed Period | [optional] 
**display_name** | **str** | The name of the Closed Period. | [optional] 
**description** | **str** | A description for the Closed Period. | [optional] 
**effective_start** | **datetime** | The effective start of the Closed Period | [optional] 
**effective_end** | **datetime** | The effective end of the Closed Period | [optional] 
**as_at_closed** | **datetime** | The asAt closed datetime for the Closed Period | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | The Closed Periods properties. These will be from the &#39;ClosedPeriod&#39; domain. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**post_close_activities** | [**List[PostCloseActivity]**](PostCloseActivity.md) | All the post close activities for the closed period. | [optional] 
**holdings_as_at_closed_override** | **datetime** | The optional AsAtClosed Override to use for building holdings in the Closed Period.If not specified, the AsAtClosed on the Closed Period will be used. | [optional] 
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested asAt datetime. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.closed_period import ClosedPeriod
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist
from datetime import datetime
closed_period_id: Optional[StrictStr] = "example_closed_period_id"
display_name: Optional[StrictStr] = "example_display_name"
description: Optional[StrictStr] = "example_description"
effective_start: Optional[datetime] = # Replace with your value
effective_end: Optional[datetime] = # Replace with your value
as_at_closed: Optional[datetime] = # Replace with your value
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
version: Optional[Version] = None
post_close_activities: Optional[conlist(PostCloseActivity)] = # Replace with your value
holdings_as_at_closed_override: Optional[datetime] = # Replace with your value
href: Optional[StrictStr] = "example_href"
links: Optional[conlist(Link)] = None
closed_period_instance = ClosedPeriod(closed_period_id=closed_period_id, display_name=display_name, description=description, effective_start=effective_start, effective_end=effective_end, as_at_closed=as_at_closed, properties=properties, version=version, post_close_activities=post_close_activities, holdings_as_at_closed_override=holdings_as_at_closed_override, href=href, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

