# TransitionRecInstanceRequest

The request to apply a lifecycle transition (re-run, lock or unlock) to a rec instance.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | The transition to apply. Available values: ReRun, Lock, Unlock. | 
## Example

```python
from lusid.models.transition_rec_instance_request import TransitionRecInstanceRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

action: StrictStr = "example_action"
transition_rec_instance_request_instance = TransitionRecInstanceRequest(action=action)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

