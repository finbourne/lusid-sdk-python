# ReferenceListResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**name** | **str** | The name of the reference list. | 
**description** | **str** | The description of the reference list. | [optional] 
**tags** | **List[str]** | The tags associated with the reference list. | [optional] 
**reference_list** | [**ReferenceList**](ReferenceList.md) |  | 
**version** | [**Version**](Version.md) |  | 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.reference_list_response import ReferenceListResponse
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, constr

id: ResourceId = # Replace with your value
name: StrictStr = "example_name"
description: Optional[StrictStr] = "example_description"
tags: Optional[conlist(StrictStr)] = # Replace with your value
reference_list: ReferenceList = # Replace with your value
version: Version = # Replace with your value
links: Optional[conlist(Link)] = None
reference_list_response_instance = ReferenceListResponse(id=id, name=name, description=description, tags=tags, reference_list=reference_list, version=version, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

