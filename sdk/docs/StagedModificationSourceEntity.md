# StagedModificationSourceEntity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_type** | **str** | The type of the source entity. | [optional] 
**scope** | **str** | The scope of the source entity. | [optional] 
**entity_unique_id** | **str** | The unique Id of the source entity. | [optional] 
**display_name** | **str** | The display name of the source entity. | [optional] 
## Example

```python
from lusid.models.staged_modification_source_entity import StagedModificationSourceEntity
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

entity_type: Optional[StrictStr] = "example_entity_type"
scope: Optional[StrictStr] = "example_scope"
entity_unique_id: Optional[StrictStr] = "example_entity_unique_id"
display_name: Optional[StrictStr] = "example_display_name"
staged_modification_source_entity_instance = StagedModificationSourceEntity(entity_type=entity_type, scope=scope, entity_unique_id=entity_unique_id, display_name=display_name)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

