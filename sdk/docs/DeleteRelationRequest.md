# DeleteRelationRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_entity_id** | **Dict[str, Optional[str]]** | The identifier of the source entity of the relation to be deleted. | 
**target_entity_id** | **Dict[str, Optional[str]]** | The identifier of the target entity of the relation to be deleted. | 
## Example

```python
from lusid.models.delete_relation_request import DeleteRelationRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

source_entity_id: Dict[str, Optional[StrictStr]] = # Replace with your value
target_entity_id: Dict[str, Optional[StrictStr]] = # Replace with your value
delete_relation_request_instance = DeleteRelationRequest(source_entity_id=source_entity_id, target_entity_id=target_entity_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

