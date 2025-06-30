# MappedString

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left_value** | **str** |  | [optional] 
**right_value** | **str** |  | [optional] 
**mapping_direction** | **str** |  | [optional] 
**is_case_sensitive** | **bool** |  | [optional] 
## Example

```python
from lusid.models.mapped_string import MappedString
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictBool, StrictStr

left_value: Optional[StrictStr] = "example_left_value"
right_value: Optional[StrictStr] = "example_right_value"
mapping_direction: Optional[StrictStr] = "example_mapping_direction"
is_case_sensitive: Optional[StrictBool] = # Replace with your value
is_case_sensitive:Optional[StrictBool] = None
mapped_string_instance = MappedString(left_value=left_value, right_value=right_value, mapping_direction=mapping_direction, is_case_sensitive=is_case_sensitive)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

