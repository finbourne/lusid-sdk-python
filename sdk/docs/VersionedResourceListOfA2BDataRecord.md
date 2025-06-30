# VersionedResourceListOfA2BDataRecord

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | [**Version**](Version.md) |  | 
**values** | [**List[A2BDataRecord]**](A2BDataRecord.md) |  | 
**href** | **str** |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.versioned_resource_list_of_a2_b_data_record import VersionedResourceListOfA2BDataRecord
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist

version: Version = # Replace with your value
values: conlist(A2BDataRecord) = # Replace with your value
href: Optional[StrictStr] = "example_href"
next_page: Optional[StrictStr] = "example_next_page"
previous_page: Optional[StrictStr] = "example_previous_page"
links: Optional[conlist(Link)] = None
versioned_resource_list_of_a2_b_data_record_instance = VersionedResourceListOfA2BDataRecord(version=version, values=values, href=href, next_page=next_page, previous_page=previous_page, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

