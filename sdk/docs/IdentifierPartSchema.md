# IdentifierPartSchema

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** |  | 
**name** | **str** |  | 
**display_name** | **str** |  | 
**description** | **str** |  | 
**required** | **bool** |  | 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.identifier_part_schema import IdentifierPartSchema
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

index: StrictInt
index: StrictInt = 42
name: StrictStr = "example_name"
display_name: StrictStr = "example_display_name"
description: StrictStr = "example_description"
required: StrictBool
required:StrictBool = True
links: Optional[List[Link]] = None
identifier_part_schema_instance = IdentifierPartSchema(index=index, name=name, display_name=display_name, description=description, required=required, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

