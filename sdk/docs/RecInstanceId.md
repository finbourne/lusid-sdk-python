# RecInstanceId

Identifies a rec instance, and how it was created.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance_id_type** | **str** | How the instance was created. Available values: WorkflowServiceTaskId, Manual. | 
**instance_id_value** | **str** | The instance identifier value (a GUID). | 
## Example

```python
from lusid.models.rec_instance_id import RecInstanceId
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

instance_id_type: StrictStr = "example_instance_id_type"
instance_id_value: StrictStr = "example_instance_id_value"
rec_instance_id_instance = RecInstanceId(instance_id_type=instance_id_type, instance_id_value=instance_id_value)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

