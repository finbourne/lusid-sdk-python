# AllocationEventEqualisationMark

A valuation move already allocated to the existing partners that the close re-trues to the admitted partners.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**origin_member_short_code** | **str** | The member of the structure the mark belongs to. | 
**amount** | **float** | The valuation move already allocated, in the event currency. Negative for a fall in value or an expense. | 
## Example

```python
from lusid.models.allocation_event_equalisation_mark import AllocationEventEqualisationMark
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

origin_member_short_code: StrictStr = "example_origin_member_short_code"
amount: Union[StrictFloat, StrictInt] = # Replace with your value
allocation_event_equalisation_mark_instance = AllocationEventEqualisationMark(origin_member_short_code=origin_member_short_code, amount=amount)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

