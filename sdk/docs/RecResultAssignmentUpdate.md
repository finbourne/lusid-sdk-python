# RecResultAssignmentUpdate

An assignment update (assigned user or role) within a batch review item. Omitting the object leaves  the existing value untouched; a null value nullifies it.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The value to set, or null to nullify. | [optional] 
## Example

```python
from lusid.models.rec_result_assignment_update import RecResultAssignmentUpdate
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

value: Optional[StrictStr] = "example_value"
rec_result_assignment_update_instance = RecResultAssignmentUpdate(value=value)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

