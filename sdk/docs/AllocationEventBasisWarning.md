# AllocationEventBasisWarning

One thing the basis source had to work around when it read the register for an Allocation Event.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The warning, for example MissingFeeRate or RoundingPartnerNotParticipant. | [optional] 
**investor_record_id** | **str** | The investor record the warning concerns, or absent when it concerns the event as a whole. | [optional] 
## Example

```python
from lusid.models.allocation_event_basis_warning import AllocationEventBasisWarning
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

code: Optional[StrictStr] = "example_code"
investor_record_id: Optional[StrictStr] = "example_investor_record_id"
allocation_event_basis_warning_instance = AllocationEventBasisWarning(code=code, investor_record_id=investor_record_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

