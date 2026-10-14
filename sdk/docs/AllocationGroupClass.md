# AllocationGroupClass

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**share_class_short_code** | **str** | A short code that uniquely identifies the share class within the Fund and is attached to the transaction. | 
**apportionment_factor** | **float** | Only used for fixed percentage method or be zero, must equal 1 or 0 across all classes in the fund. | [optional] 
**share_class_series_code** | **str** | The series of the share class the member refers to. Not yet supported: an allocation group is apportioned by share class, so a member that names a series is rejected. | [optional] 
## Example

```python
from lusid.models.allocation_group_class import AllocationGroupClass
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

share_class_short_code: StrictStr = "example_share_class_short_code"
apportionment_factor: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
share_class_series_code: Optional[StrictStr] = "example_share_class_series_code"
allocation_group_class_instance = AllocationGroupClass(share_class_short_code=share_class_short_code, apportionment_factor=apportionment_factor, share_class_series_code=share_class_series_code)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

