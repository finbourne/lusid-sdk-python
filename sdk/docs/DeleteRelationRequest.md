# DeleteRelationRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_entity_id** | **Dict[str, str]** | The identifier of the source entity of the relation to be deleted. | 
**target_entity_id** | **Dict[str, str]** | The identifier of the target entity of the relation to be deleted. | 
## Example

```python
from lusid.models.delete_relation_request import DeleteRelationRequest
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, StrictStr

source_entity_id: Dict[str, StrictStr] = # Replace with your value
target_entity_id: Dict[str, StrictStr] = # Replace with your value
delete_relation_request_instance = DeleteRelationRequest(source_entity_id=source_entity_id, target_entity_id=target_entity_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

