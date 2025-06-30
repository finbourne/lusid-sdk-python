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
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, constr

left: Optional[StrictStr] = "example_left"
operator: Optional[StrictStr] = "example_operator"
right: Optional[ResultValue] = None
address_key_filter_instance = AddressKeyFilter(left=left, operator=operator, right=right)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

