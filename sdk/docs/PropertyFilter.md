# PropertyFilter

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left** | **str** | The key that uniquely identifies a queryable address in Lusid. | [optional] 
**operator** | **str** | The available values are: Equals, NotEquals, GreaterThan, GreaterThanOrEqualTo, LessThan, LessThanOrEqualTo, In | [optional] 
**right** | **object** |  | [optional] 
**right_operand_type** | **str** | The available values are: Absolute, Property | [optional] 
## Example

```python
from lusid.models.property_filter import PropertyFilter
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

left: Optional[StrictStr] = "example_left"
operator: Optional[StrictStr] = "example_operator"
right: Optional[Any] = None
right_operand_type: Optional[StrictStr] = "example_right_operand_type"
property_filter_instance = PropertyFilter(left=left, operator=operator, right=right, right_operand_type=right_operand_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

