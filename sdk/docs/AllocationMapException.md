# AllocationMapException

A departure from the default participation of an Allocation Map for one investor record.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**investor_record_id** | **str** | The investor record the exception applies to. | 
**treatment** | **str** | What the exception does. Excluded removes the investor record from every allocation; FixedPercentage gives it participationPercent of each event off the top, before the remainder is shared pro rata between the other participants. Available values: Excluded, FixedPercentage. | 
**participation_percent** | **float** | For a FixedPercentage exception, the fixed share as a fraction in the range (0, 1]. Not allowed on an Excluded exception. The fixed shares of all exceptions may not sum to more than 1. | [optional] 
**reason** | **str** | Why the exception exists, for example a side letter or regulatory restriction. Required. | 
**effective_from** | **datetime** | The datetime from which the exception is in force. Defaults to always if not specified. | [optional] 
## Example

```python
from lusid.models.allocation_map_exception import AllocationMapException
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

investor_record_id: StrictStr = "example_investor_record_id"
treatment: StrictStr = "example_treatment"
participation_percent: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
reason: StrictStr = "example_reason"
effective_from: Optional[datetime] = # Replace with your value
allocation_map_exception_instance = AllocationMapException(investor_record_id=investor_record_id, treatment=treatment, participation_percent=participation_percent, reason=reason, effective_from=effective_from)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

