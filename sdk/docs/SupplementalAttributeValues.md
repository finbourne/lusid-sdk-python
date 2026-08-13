# SupplementalAttributeValues

A supplemental attribute value carried on a rec result for context. Does not contribute to matching.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_name** | **str** | The name of the supplemental attribute. | 
**left_value** | **str** | The left-side value. | [optional] 
**right_value** | **str** | The right-side value. | [optional] 
## Example

```python
from lusid.models.supplemental_attribute_values import SupplementalAttributeValues
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

attribute_name: StrictStr = "example_attribute_name"
left_value: Optional[StrictStr] = "example_left_value"
right_value: Optional[StrictStr] = "example_right_value"
supplemental_attribute_values_instance = SupplementalAttributeValues(attribute_name=attribute_name, left_value=left_value, right_value=right_value)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

