# ActionId

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** |  | 
**activity** | **str** |  | 
**entity** | **str** |  | 
## Example

```python
from lusid.models.action_id import ActionId
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

scope: StrictStr = "example_scope"
activity: StrictStr = "example_activity"
entity: StrictStr = "example_entity"
action_id_instance = ActionId(scope=scope, activity=activity, entity=entity)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

