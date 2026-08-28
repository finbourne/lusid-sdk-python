# UnconfirmClosedPeriodRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delete_subsequent_periods** | **bool** | Whether to delete every Closed Period that comes after the requested Closed Period on the Timeline. When false (the default) only the latest confirmed Closed Period may be unconfirmed. | [optional] 
## Example

```python
from lusid.models.unconfirm_closed_period_request import UnconfirmClosedPeriodRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

delete_subsequent_periods: Optional[StrictBool] = # Replace with your value
delete_subsequent_periods:Optional[StrictBool] = None
unconfirm_closed_period_request_instance = UnconfirmClosedPeriodRequest(delete_subsequent_periods=delete_subsequent_periods)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

