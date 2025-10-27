# CustomEntityDefinition

Representation of Custom Entity Definition on LUSID API
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**entity_type_name** | **str** | The name provided when the custom entity type was created. This has been prefixed with “~” and returned as “entityType”, which is the identifier for the custom entity type. | 
**display_name** | **str** | A display label for the custom entity type. | 
**description** | **str** | A description for the custom entity type. | [optional] 
**entity_type** | **str** | The identifier for the custom entity type, derived from the “entityTypeName” provided on creation. | 
**field_schema** | [**List[CustomEntityFieldDefinition]**](CustomEntityFieldDefinition.md) | The description of the fields on the custom entity type. | 
**version** | [**Version**](Version.md) |  | 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.custom_entity_definition import CustomEntityDefinition
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

href: Optional[StrictStr] = "example_href"
entity_type_name: StrictStr = "example_entity_type_name"
display_name: StrictStr = "example_display_name"
description: Optional[StrictStr] = "example_description"
entity_type: StrictStr = "example_entity_type"
field_schema: List[CustomEntityFieldDefinition] = # Replace with your value
version: Version
links: Optional[List[Link]] = None
custom_entity_definition_instance = CustomEntityDefinition(href=href, entity_type_name=entity_type_name, display_name=display_name, description=description, entity_type=entity_type, field_schema=field_schema, version=version, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

