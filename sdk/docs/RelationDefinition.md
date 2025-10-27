# RelationDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | [**Version**](Version.md) |  | [optional] 
**relation_definition_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**source_entity_domain** | **str** | The entity domain of the source entity object. | [optional] 
**target_entity_domain** | **str** | The entity domain of the target entity object. | [optional] 
**display_name** | **str** | The display name of the relation. | [optional] 
**outward_description** | **str** | The description to relate source entity object and target entity object | [optional] 
**inward_description** | **str** | The description to relate target entity object and source entity object | [optional] 
**life_time** | **str** | Describes how the relations can change over time, allowed values are \&quot;Perpetual\&quot; and \&quot;TimeVariant\&quot; | [optional] 
**constraint_style** | **str** | Describes the uniqueness and cardinality for relations with a specific source entity object and relations under this definition. Allowed values are \&quot;Property\&quot; and \&quot;Collection\&quot;, defaults to \&quot;Collection\&quot; if not specified. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.relation_definition import RelationDefinition
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

version: Optional[Version] = None
relation_definition_id: Optional[ResourceId] = # Replace with your value
source_entity_domain: Optional[StrictStr] = "example_source_entity_domain"
target_entity_domain: Optional[StrictStr] = "example_target_entity_domain"
display_name: Optional[StrictStr] = "example_display_name"
outward_description: Optional[StrictStr] = "example_outward_description"
inward_description: Optional[StrictStr] = "example_inward_description"
life_time: Optional[StrictStr] = "example_life_time"
constraint_style: Optional[StrictStr] = "example_constraint_style"
links: Optional[List[Link]] = None
relation_definition_instance = RelationDefinition(version=version, relation_definition_id=relation_definition_id, source_entity_domain=source_entity_domain, target_entity_domain=target_entity_domain, display_name=display_name, outward_description=outward_description, inward_description=inward_description, life_time=life_time, constraint_style=constraint_style, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

