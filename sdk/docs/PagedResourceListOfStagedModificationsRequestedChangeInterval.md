# PagedResourceListOfStagedModificationsRequestedChangeInterval

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**values** | [**List[StagedModificationsRequestedChangeInterval]**](StagedModificationsRequestedChangeInterval.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.paged_resource_list_of_staged_modifications_requested_change_interval import PagedResourceListOfStagedModificationsRequestedChangeInterval
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist

next_page: Optional[StrictStr] = "example_next_page"
previous_page: Optional[StrictStr] = "example_previous_page"
values: conlist(StagedModificationsRequestedChangeInterval) = # Replace with your value
href: Optional[StrictStr] = "example_href"
links: Optional[conlist(Link)] = None
paged_resource_list_of_staged_modifications_requested_change_interval_instance = PagedResourceListOfStagedModificationsRequestedChangeInterval(next_page=next_page, previous_page=previous_page, values=values, href=href, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

