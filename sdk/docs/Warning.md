# Warning

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | **str** |  | 
**message** | **str** |  | 
## Example

```python
from lusid.models.warning import Warning
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, StrictStr

entity_id: StrictStr = "example_entity_id"
message: StrictStr = "example_message"
warning_instance = Warning(entity_id=entity_id, message=message)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

