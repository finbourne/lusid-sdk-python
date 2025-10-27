# CreateCustomEntityTypeRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_type_name** | **str** | A name for the custom entity type. This will be prefixed with “~” and returned as “entityType”, which is the identifier for the custom entity type. | 
**display_name** | **str** | A display label for the custom entity type. | 
**description** | **str** | A description for the custom entity type. | 
**field_schema** | [**List[CustomEntityFieldDefinition]**](CustomEntityFieldDefinition.md) | The description of the fields on the custom entity type. | 
## Example

```python
from lusid.models.create_custom_entity_type_request import CreateCustomEntityTypeRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

entity_type_name: StrictStr = "example_entity_type_name"
display_name: StrictStr = "example_display_name"
description: StrictStr = "example_description"
field_schema: List[CustomEntityFieldDefinition] = # Replace with your value
create_custom_entity_type_request_instance = CreateCustomEntityTypeRequest(entity_type_name=entity_type_name, display_name=display_name, description=description, field_schema=field_schema)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

