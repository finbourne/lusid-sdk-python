# RelationalDatasetDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**display_name** | **str** | A user-friendly display name for the relational dataset definition. | 
**description** | **str** | A detailed description of the relational dataset definition and its purpose. | [optional] 
**applicable_entity_types** | **List[str]** | The types of entities this relational dataset definition can be applied to (e.g. Instrument, Portfolio, etc.). | 
**field_schema** | [**List[RelationalDatasetFieldDefinition]**](RelationalDatasetFieldDefinition.md) | The schema defining the structure and data types of the relational dataset. | 
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.relational_dataset_definition import RelationalDatasetDefinition
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: ResourceId
display_name: StrictStr = "example_display_name"
description: Optional[StrictStr] = "example_description"
applicable_entity_types: List[StrictStr] = # Replace with your value
field_schema: List[RelationalDatasetFieldDefinition] = # Replace with your value
href: Optional[StrictStr] = "example_href"
version: Optional[Version] = None
links: Optional[List[Link]] = None
relational_dataset_definition_instance = RelationalDatasetDefinition(id=id, display_name=display_name, description=description, applicable_entity_types=applicable_entity_types, field_schema=field_schema, href=href, version=version, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

