# CreateRelationshipRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_entity_id** | **Dict[str, str]** | The identifier of the source entity. | 
**target_entity_id** | **Dict[str, str]** | The identifier of the target entity. | 
**effective_from** | **str** | The effective date of the relationship to be created | [optional] 
**effective_until** | **str** | The effective datetime until which the relationship is valid. If not supplied this will be valid indefinitely. | [optional] 
## Example

```python
from lusid.models.create_relationship_request import CreateRelationshipRequest
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, constr, validator

source_entity_id: Dict[str, StrictStr] = # Replace with your value
target_entity_id: Dict[str, StrictStr] = # Replace with your value
effective_from: Optional[StrictStr] = "example_effective_from"
effective_until: Optional[StrictStr] = "example_effective_until"
create_relationship_request_instance = CreateRelationshipRequest(source_entity_id=source_entity_id, target_entity_id=target_entity_id, effective_from=effective_from, effective_until=effective_until)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

