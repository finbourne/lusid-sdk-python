# RelationshipDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | [**Version**](Version.md) |  | [optional] 
**relationship_definition_id** | [**ResourceId**](ResourceId.md) |  | 
**source_entity_type** | **str** | The entity type of the source entity object. | 
**target_entity_type** | **str** | The entity type of the target entity object. | 
**display_name** | **str** | The display name of the relationship. | 
**outward_description** | **str** | The description to relate source entity object and target entity object | 
**inward_description** | **str** | The description to relate target entity object and source entity object | 
**life_time** | **str** | Describes how the relationships can change over time. | 
**relationship_cardinality** | **str** | Describes the cardinality of the relationship between source entity and target entity. | 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.relationship_definition import RelationshipDefinition
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

version: Optional[Version] = None
relationship_definition_id: ResourceId = # Replace with your value
source_entity_type: StrictStr = "example_source_entity_type"
target_entity_type: StrictStr = "example_target_entity_type"
display_name: StrictStr = "example_display_name"
outward_description: StrictStr = "example_outward_description"
inward_description: StrictStr = "example_inward_description"
life_time: StrictStr = "example_life_time"
relationship_cardinality: StrictStr = "example_relationship_cardinality"
links: Optional[List[Link]] = None
relationship_definition_instance = RelationshipDefinition(version=version, relationship_definition_id=relationship_definition_id, source_entity_type=source_entity_type, target_entity_type=target_entity_type, display_name=display_name, outward_description=outward_description, inward_description=inward_description, life_time=life_time, relationship_cardinality=relationship_cardinality, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

