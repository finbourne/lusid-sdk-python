# BatchCreateClosedPeriodsRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**closed_periods** | [**List[CreateClosedPeriodRequest]**](CreateClosedPeriodRequest.md) | The ordered set of Closed Periods to create. Each Closed Period&#39;s EffectiveStart is derived from the previous Closed Period&#39;s EffectiveEnd (or the current chain tail for the first item), so EffectiveEnd must be strictly increasing across the batch. | 
## Example

```python
from lusid.models.batch_create_closed_periods_request import BatchCreateClosedPeriodsRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

closed_periods: List[CreateClosedPeriodRequest] = # Replace with your value
batch_create_closed_periods_request_instance = BatchCreateClosedPeriodsRequest(closed_periods=closed_periods)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

