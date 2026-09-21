# CoreStringCrossTolerance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference_value** | **str** | The value for the reference side. | 
**cross_value** | **str** | The value for the side other than the reference one. | 
**reference_side** | **str** | Reference side (source of truth). One of: Left, Right. Available values: Left, Right, Either. | [optional] 
**tolerance_type** | **str** | Polymorphic discriminator. Supported types: CoreStringCross, CoreAttributeOptionality, CoreDateTolerance, Numeric. Available values: CoreStringCross, CoreAttributeOptionality, CoreDateTolerance, Numeric. | 
**rule_name** | **str** | The reference name of the rule that this tolerance relaxes. | 
## Example

```python
from lusid.models.core_string_cross_tolerance import CoreStringCrossTolerance
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

reference_value: StrictStr = "example_reference_value"
cross_value: StrictStr = "example_cross_value"
reference_side: Optional[StrictStr] = "example_reference_side"
tolerance_type: StrictStr = "example_tolerance_type"
rule_name: StrictStr = "example_rule_name"
core_string_cross_tolerance_instance = CoreStringCrossTolerance(reference_value=reference_value, cross_value=cross_value, reference_side=reference_side, tolerance_type=tolerance_type, rule_name=rule_name)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

