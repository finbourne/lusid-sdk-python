# CompleteRelationship

Representation of a relationship containing details of source and target entities, and both outward and inward descriptions.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**relationship_definition_id** | [**ResourceId**](ResourceId.md) |  | 
**source_entity** | [**RelatedEntity**](RelatedEntity.md) |  | 
**target_entity** | [**RelatedEntity**](RelatedEntity.md) |  | 
**outward_description** | **str** | Description of the relationship based on relationship definition&#39;s outward description. | 
**inward_description** | **str** | Description of the relationship based on relationship definition&#39;s inward description. | 
**effective_from** | **datetime** | The effective datetime from which the relationship is valid. | [optional] 
**effective_until** | **datetime** | The effective datetime to which the relationship is valid until. | [optional] 
## Example

```python
from lusid.models.complete_relationship import CompleteRelationship
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

href: Optional[StrictStr] = "example_href"
version: Optional[Version] = None
relationship_definition_id: ResourceId = # Replace with your value
source_entity: RelatedEntity = # Replace with your value
target_entity: RelatedEntity = # Replace with your value
outward_description: StrictStr = "example_outward_description"
inward_description: StrictStr = "example_inward_description"
effective_from: Optional[datetime] = # Replace with your value
effective_until: Optional[datetime] = # Replace with your value
complete_relationship_instance = CompleteRelationship(href=href, version=version, relationship_definition_id=relationship_definition_id, source_entity=source_entity, target_entity=target_entity, outward_description=outward_description, inward_description=inward_description, effective_from=effective_from, effective_until=effective_until)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

