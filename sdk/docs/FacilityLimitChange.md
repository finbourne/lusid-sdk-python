# FacilityLimitChange

A change to a Facility's committed limit: the limit in force from a date until the next change.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_from** | **datetime** |  | 
**limit** | **float** |  | 
## Example

```python
from lusid.models.facility_limit_change import FacilityLimitChange
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

effective_from: datetime = # Replace with your value
limit: Union[StrictFloat, StrictInt]
facility_limit_change_instance = FacilityLimitChange(effective_from=effective_from, limit=limit)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

