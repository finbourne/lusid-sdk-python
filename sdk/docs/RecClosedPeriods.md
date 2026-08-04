# RecClosedPeriods

References to the closed periods created on the left and right timelines when a Closed Period  instance is locked.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left** | [**RecClosedPeriodReference**](RecClosedPeriodReference.md) |  | 
**right** | [**RecClosedPeriodReference**](RecClosedPeriodReference.md) |  | 
## Example

```python
from lusid.models.rec_closed_periods import RecClosedPeriods
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

left: RecClosedPeriodReference
right: RecClosedPeriodReference
rec_closed_periods_instance = RecClosedPeriods(left=left, right=right)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

