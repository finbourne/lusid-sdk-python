# AddressKeyFilter

Class specifying a filtering operation
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left** | **str** | Address for the value in the row | [optional] 
**operator** | **str** | What sort of comparison is the filter performing. Can be either \&quot;eq\&quot; for equals or \&quot;neq\&quot; for not equals. | [optional] 
**right** | [**ResultValue**](ResultValue.md) |  | [optional] 
## Example

```python
from lusid.models.address_key_filter import AddressKeyFilter
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

left: Optional[StrictStr] = "example_left"
operator: Optional[StrictStr] = "example_operator"
right: Optional[ResultValue] = None
address_key_filter_instance = AddressKeyFilter(left=left, operator=operator, right=right)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

