# ReferenceListRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**name** | **str** | The name of the reference list. | 
**description** | **str** | The description of the reference list. | [optional] 
**tags** | **List[str]** | The tags associated with the reference list. | [optional] 
**reference_list** | [**ReferenceList**](ReferenceList.md) |  | 
## Example

```python
from lusid.models.reference_list_request import ReferenceListRequest
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, constr

id: ResourceId = # Replace with your value
name: StrictStr = "example_name"
description: Optional[StrictStr] = "example_description"
tags: Optional[conlist(StrictStr)] = # Replace with your value
reference_list: ReferenceList = # Replace with your value
reference_list_request_instance = ReferenceListRequest(id=id, name=name, description=description, tags=tags, reference_list=reference_list)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

