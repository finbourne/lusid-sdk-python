# DeleteRelationshipRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_entity_id** | **Dict[str, Optional[str]]** | The identifier of the source entity of the relationship to be deleted. | 
**target_entity_id** | **Dict[str, Optional[str]]** | The identifier of the target entity of the relationship to be deleted. | 
**effective_from** | **str** | The effective date of the relationship to be deleted | [optional] 
**effective_until** | **str** | The effective datetime until which the relationship will be deleted. If not supplied the deletion will be permanent. | [optional] 
## Example

```python
from lusid.models.delete_relationship_request import DeleteRelationshipRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

source_entity_id: Dict[str, Optional[StrictStr]] = # Replace with your value
target_entity_id: Dict[str, Optional[StrictStr]] = # Replace with your value
effective_from: Optional[StrictStr] = "example_effective_from"
effective_until: Optional[StrictStr] = "example_effective_until"
delete_relationship_request_instance = DeleteRelationshipRequest(source_entity_id=source_entity_id, target_entity_id=target_entity_id, effective_from=effective_from, effective_until=effective_until)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

