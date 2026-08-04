# RecClosedPeriodReference

A reference to a closed period created on a timeline when the instance was locked.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timeline_id** | [**ResourceId**](ResourceId.md) |  | 
**closed_period_id** | **str** | The identifier of the closed period. | 
## Example

```python
from lusid.models.rec_closed_period_reference import RecClosedPeriodReference
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

timeline_id: ResourceId = # Replace with your value
closed_period_id: StrictStr = "example_closed_period_id"
rec_closed_period_reference_instance = RecClosedPeriodReference(timeline_id=timeline_id, closed_period_id=closed_period_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

