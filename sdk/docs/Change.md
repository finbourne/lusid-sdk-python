# Change

The time an entity was modified (amendment and/or historical correction).
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**entity_id** | [**ResourceId**](ResourceId.md) |  | 
**corrected** | **bool** |  | 
**correction_effective_at** | **datetime** |  | [optional] 
**correction_as_at** | **datetime** |  | [optional] 
**amended** | **bool** |  | 
**amendment_effective_at** | **datetime** |  | [optional] 
**amendment_as_at** | **datetime** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.change import Change
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictBool, StrictStr, conlist
from datetime import datetime
href: Optional[StrictStr] = "example_href"
entity_id: ResourceId = # Replace with your value
corrected: StrictBool = # Replace with your value
corrected:StrictBool = True
correction_effective_at: Optional[datetime] = # Replace with your value
correction_as_at: Optional[datetime] = # Replace with your value
amended: StrictBool = # Replace with your value
amended:StrictBool = True
amendment_effective_at: Optional[datetime] = # Replace with your value
amendment_as_at: Optional[datetime] = # Replace with your value
links: Optional[conlist(Link)] = None
change_instance = Change(href=href, entity_id=entity_id, corrected=corrected, correction_effective_at=correction_effective_at, correction_as_at=correction_as_at, amended=amended, amendment_effective_at=amendment_effective_at, amendment_as_at=amendment_as_at, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

