# AllocationReceivable

One investor's position on a booked capital call.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**investor_record_id** | **str** | The investor record. | [optional] 
**called** | **float** | What the investor record was called for. | [optional] 
**received** | **float** | What has been received and applied so far. | [optional] 
**outstanding** | **float** | What is still owed. Never negative: an overpayment becomes a refund payable instead. | [optional] 
**days_past_due** | **int** | How many days past the due date the outstanding amount is, or zero when not yet due or nothing is owed. | [optional] 
**bucket** | **str** | The ageing bucket: Current, 1-30, 31-60, 61-90 or 90+. | [optional] 
## Example

```python
from lusid.models.allocation_receivable import AllocationReceivable
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

investor_record_id: Optional[StrictStr] = "example_investor_record_id"
called: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
received: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
outstanding: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
days_past_due: Optional[StrictInt] = # Replace with your value
days_past_due: Optional[StrictInt] = None
bucket: Optional[StrictStr] = "example_bucket"
allocation_receivable_instance = AllocationReceivable(investor_record_id=investor_record_id, called=called, received=received, outstanding=outstanding, days_past_due=days_past_due, bucket=bucket)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

