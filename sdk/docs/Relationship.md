# Relationship

Representation of a Relationship between a requested entity with the stated entity as RelatedEntityId
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | [**Version**](Version.md) |  | [optional] 
**relationship_definition_id** | [**ResourceId**](ResourceId.md) |  | 
**related_entity** | [**RelatedEntity**](RelatedEntity.md) |  | 
**traversal_direction** | **str** | Direction of relationship between the requested entity and related entity. This can be &#39;In&#39; or &#39;Out&#39;. Read more about relationships traversal direction in LUSID Knowledge Base here https://support.lusid.com/knowledgebase/article/KA-01679. | 
**traversal_description** | **str** | Description of the relationship based on relationship&#39;s traversal direction. If &#39;TraversalDirection&#39; is &#39;Out&#39;, this description would be &#39;OutwardDescription&#39; from the associated relationship definition. If &#39;TraversalDirection&#39; is &#39;In&#39;, this description would be &#39;InwardDescription&#39; from the associated relationship definition. | 
**effective_from** | **datetime** | The effective datetime from which the relationship is valid. | [optional] 
**effective_until** | **datetime** | The effective datetime until which the relationship is valid. If no future deletions are present or an effective until has not been set for the relationship, this will be indefinite and represented by the maximum date. | [optional] 
## Example

```python
from lusid.models.relationship import Relationship
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, constr
from datetime import datetime
version: Optional[Version] = None
relationship_definition_id: ResourceId = # Replace with your value
related_entity: RelatedEntity = # Replace with your value
traversal_direction: StrictStr = "example_traversal_direction"
traversal_description: StrictStr = "example_traversal_description"
effective_from: Optional[datetime] = # Replace with your value
effective_until: Optional[datetime] = # Replace with your value
relationship_instance = Relationship(version=version, relationship_definition_id=relationship_definition_id, related_entity=related_entity, traversal_direction=traversal_direction, traversal_description=traversal_description, effective_from=effective_from, effective_until=effective_until)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

