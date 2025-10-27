# CustomEntityId

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier_scope** | **str** | The scope the identifier resides in (the scope of the identifier property definition). | 
**identifier_type** | **str** | What the identifier represents (the code of the identifier property definition). | 
**identifier_value** | **str** | The value of the identifier for this entity. | 
**effective_from** | **datetime** | The effective datetime from which the identifier is valid. | [optional] 
**effective_until** | **datetime** | The effective datetime until which the identifier is valid. If not supplied this will be valid indefinitely, or until the next &#39;effectiveFrom&#39; datetime of the identifier. | [optional] 
## Example

```python
from lusid.models.custom_entity_id import CustomEntityId
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

identifier_scope: StrictStr = "example_identifier_scope"
identifier_type: StrictStr = "example_identifier_type"
identifier_value: StrictStr = "example_identifier_value"
effective_from: Optional[datetime] = # Replace with your value
effective_until: Optional[datetime] = # Replace with your value
custom_entity_id_instance = CustomEntityId(identifier_scope=identifier_scope, identifier_type=identifier_type, identifier_value=identifier_value, effective_from=effective_from, effective_until=effective_until)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

