# Link

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**relation** | **str** |  | 
**href** | **str** |  | 
**description** | **str** |  | [optional] 
**method** | **str** |  | 
## Example

```python
from lusid.models.link import Link
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr

relation: StrictStr = "example_relation"
href: StrictStr = "example_href"
description: Optional[StrictStr] = "example_description"
method: StrictStr = "example_method"
link_instance = Link(relation=relation, href=href, description=description, method=method)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

