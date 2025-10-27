# ModelSchema

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | **str** |  | [optional] 
**href** | **str** |  | [optional] 
**values** | [**Dict[str, FieldSchema]**](FieldSchema.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.model_schema import ModelSchema
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

entity: Optional[StrictStr] = "example_entity"
href: Optional[StrictStr] = "example_href"
values: Optional[Dict[str, FieldSchema]] = None
links: Optional[List[Link]] = None
model_schema_instance = ModelSchema(entity=entity, href=href, values=values, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

