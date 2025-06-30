# CompleteRelation

Representation of a relation containing details of source and target entities, and both outward and inward descriptions.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**relation_definition_id** | [**ResourceId**](ResourceId.md) |  | 
**source_entity_id** | **Dict[str, str]** |  | 
**target_entity_id** | **Dict[str, str]** |  | 
**outward_description** | **str** |  | 
**inward_description** | **str** |  | 
**effective_from** | **datetime** |  | [optional] 
## Example

```python
from lusid.models.complete_relation import CompleteRelation
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, constr
from datetime import datetime
href: Optional[StrictStr] = "example_href"
version: Optional[Version] = None
relation_definition_id: ResourceId = # Replace with your value
source_entity_id: Dict[str, StrictStr] = # Replace with your value
target_entity_id: Dict[str, StrictStr] = # Replace with your value
outward_description: StrictStr = "example_outward_description"
inward_description: StrictStr = "example_inward_description"
effective_from: Optional[datetime] = # Replace with your value
complete_relation_instance = CompleteRelation(href=href, version=version, relation_definition_id=relation_definition_id, source_entity_id=source_entity_id, target_entity_id=target_entity_id, outward_description=outward_description, inward_description=inward_description, effective_from=effective_from)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

