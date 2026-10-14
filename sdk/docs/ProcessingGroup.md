# ProcessingGroup

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**id** | [**ResourceId**](ResourceId.md) |  | 
**display_name** | **str** | The name of the Processing Group. | [optional] 
**description** | **str** | A description for the Processing Group. | [optional] 
**schedule** | [**ProcessingGroupSchedule**](ProcessingGroupSchedule.md) |  | [optional] 
**reference_list_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**workflow_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**resolved_reference_list** | [**ReferenceList**](ReferenceList.md) |  | [optional] 
**list_exception_filter** | **str** | A filter selecting reference list items to exclude whenever this Processing Group resolves its reference list. Optional. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.processing_group import ProcessingGroup
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

href: Optional[StrictStr] = "example_href"
id: ResourceId
display_name: Optional[StrictStr] = "example_display_name"
description: Optional[StrictStr] = "example_description"
schedule: Optional[ProcessingGroupSchedule] = None
reference_list_id: Optional[ResourceId] = # Replace with your value
workflow_id: Optional[ResourceId] = # Replace with your value
resolved_reference_list: Optional[ReferenceList] = # Replace with your value
list_exception_filter: Optional[StrictStr] = "example_list_exception_filter"
version: Optional[Version] = None
links: Optional[List[Link]] = None
processing_group_instance = ProcessingGroup(href=href, id=id, display_name=display_name, description=description, schedule=schedule, reference_list_id=reference_list_id, workflow_id=workflow_id, resolved_reference_list=resolved_reference_list, list_exception_filter=list_exception_filter, version=version, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

