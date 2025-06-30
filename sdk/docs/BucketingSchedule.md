# BucketingSchedule

A schedule for dates
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenor** | **str** | Rolling tenor | [optional] 
## Example

```python
from lusid.models.bucketing_schedule import BucketingSchedule
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr

tenor: Optional[StrictStr] = "example_tenor"
bucketing_schedule_instance = BucketingSchedule(tenor=tenor)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

