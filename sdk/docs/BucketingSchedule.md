# BucketingSchedule

A schedule for dates
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenor** | **str** | Rolling tenor | [optional] 
## Example

```python
from lusid.models.bucketing_schedule import BucketingSchedule
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

tenor: Optional[StrictStr] = "example_tenor"
bucketing_schedule_instance = BucketingSchedule(tenor=tenor)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

