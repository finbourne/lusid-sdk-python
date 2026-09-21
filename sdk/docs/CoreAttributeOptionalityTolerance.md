# CoreAttributeOptionalityTolerance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**optional_side** | **str** | Which side is allowed to have no value while still attempting to match. One of: Left, Right, Either. Defaults to Either. Available values: Left, Right, Either. | [optional] 
**tolerance_type** | **str** | Polymorphic discriminator. Supported types: CoreStringCross, CoreAttributeOptionality, CoreDateTolerance, Numeric. Available values: CoreStringCross, CoreAttributeOptionality, CoreDateTolerance, Numeric. | 
**rule_name** | **str** | The reference name of the rule that this tolerance relaxes. | 
## Example

```python
from lusid.models.core_attribute_optionality_tolerance import CoreAttributeOptionalityTolerance
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

optional_side: Optional[StrictStr] = "example_optional_side"
tolerance_type: StrictStr = "example_tolerance_type"
rule_name: StrictStr = "example_rule_name"
core_attribute_optionality_tolerance_instance = CoreAttributeOptionalityTolerance(optional_side=optional_side, tolerance_type=tolerance_type, rule_name=rule_name)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

