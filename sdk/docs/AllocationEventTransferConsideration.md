# AllocationEventTransferConsideration

The consideration paid for a transferred capital interest.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | The consideration amount. | 
**currency** | **str** | The ISO 4217 code of the currency of the consideration. | 
**record_only** | **bool** | Whether the consideration is recorded for reference only, with no cash movement booked. Defaults to false. | [optional] 
## Example

```python
from lusid.models.allocation_event_transfer_consideration import AllocationEventTransferConsideration
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

amount: Union[StrictFloat, StrictInt] = # Replace with your value
currency: StrictStr = "example_currency"
record_only: Optional[StrictBool] = # Replace with your value
record_only:Optional[StrictBool] = None
allocation_event_transfer_consideration_instance = AllocationEventTransferConsideration(amount=amount, currency=currency, record_only=record_only)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

