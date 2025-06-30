# CreateRelationRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_entity_id** | **Dict[str, str]** | The identifier of the source entity. | 
**target_entity_id** | **Dict[str, str]** | The identifier of the target entity. | 
## Example

```python
from lusid.models.create_relation_request import CreateRelationRequest
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, StrictStr

source_entity_id: Dict[str, StrictStr] = # Replace with your value
target_entity_id: Dict[str, StrictStr] = # Replace with your value
create_relation_request_instance = CreateRelationRequest(source_entity_id=source_entity_id, target_entity_id=target_entity_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

