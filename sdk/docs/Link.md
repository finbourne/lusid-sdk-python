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
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

relation: StrictStr = "example_relation"
href: StrictStr = "example_href"
description: Optional[StrictStr] = "example_description"
method: StrictStr = "example_method"
link_instance = Link(relation=relation, href=href, description=description, method=method)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

