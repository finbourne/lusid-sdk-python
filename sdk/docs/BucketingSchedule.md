# BucketingSchedule

A schedule for dates
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenor** | **str** | Rolling tenor | [optional] 
**roll_direction** | **str** | Optional direction in which the bucketing dates are rolled out from the schedule tenor.  Supported string (enumeration) values are: [ForwardFromStart, BackwardFromEnd].  If absent (and StubType is also absent), the pre-existing date generation behaviour is used. Available values: ForwardFromStart, BackwardFromEnd. | [optional] 
**stub_type** | **str** | Optional treatment of the irregular (stub) period when the window length is not an exact multiple of the tenor.  Supported string (enumeration) values are: [ShortStub, LongStub].  If absent (and RollDirection is also absent), the pre-existing date generation behaviour is used. Available values: ShortStub, LongStub. | [optional] 
## Example

```python
from lusid.models.bucketing_schedule import BucketingSchedule
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

tenor: Optional[StrictStr] = "example_tenor"
roll_direction: Optional[StrictStr] = "example_roll_direction"
stub_type: Optional[StrictStr] = "example_stub_type"
bucketing_schedule_instance = BucketingSchedule(tenor=tenor, roll_direction=roll_direction, stub_type=stub_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

