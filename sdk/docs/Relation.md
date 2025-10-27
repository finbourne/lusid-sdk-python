# Relation

Representation of a Relation between a requested entity with the stated entity as RelationedEntityId
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | [**Version**](Version.md) |  | [optional] 
**relation_definition_id** | [**ResourceId**](ResourceId.md) |  | 
**related_entity_id** | **Dict[str, Optional[str]]** |  | 
**traversal_direction** | **str** |  | 
**traversal_description** | **str** |  | 
**effective_from** | **datetime** |  | [optional] 
## Example

```python
from lusid.models.relation import Relation
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

version: Optional[Version] = None
relation_definition_id: ResourceId = # Replace with your value
related_entity_id: Dict[str, Optional[StrictStr]] = # Replace with your value
traversal_direction: StrictStr = "example_traversal_direction"
traversal_description: StrictStr = "example_traversal_description"
effective_from: Optional[datetime] = # Replace with your value
relation_instance = Relation(version=version, relation_definition_id=relation_definition_id, related_entity_id=related_entity_id, traversal_direction=traversal_direction, traversal_description=traversal_description, effective_from=effective_from)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

