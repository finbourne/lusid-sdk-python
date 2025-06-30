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
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictBool, StrictInt, conlist, constr

index: StrictInt = # Replace with your value
index: StrictInt = 42
name: StrictStr = "example_name"
display_name: StrictStr = "example_display_name"
description: StrictStr = "example_description"
required: StrictBool = # Replace with your value
required:StrictBool = True
links: Optional[conlist(Link)] = None
identifier_part_schema_instance = IdentifierPartSchema(index=index, name=name, display_name=display_name, description=description, required=required, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

