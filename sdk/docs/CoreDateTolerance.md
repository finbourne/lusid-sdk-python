# CoreDateTolerance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference_side** | **str** | Reference side (source of truth). One of: Left, Right. Available values: Left, Right. | 
**interval** | **str** | The allowed tolerance for date time core rule values, defined as an ISO Period. | 
**offset** | **str** | How the interval should be applied to the reference side value. One of: Earlier, Later, Either. Defaults to Either. Available values: Earlier, Later, Either. | [optional] 
**tolerance_type** | **str** | Polymorphic discriminator. Supported types: CoreStringCross, CoreAttributeOptionality, CoreDateTolerance, Numeric. Available values: CoreStringCross, CoreAttributeOptionality, CoreDateTolerance, Numeric. | 
**rule_name** | **str** | The reference name of the rule that this tolerance relaxes. | 
## Example

```python
from lusid.models.core_date_tolerance import CoreDateTolerance
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

reference_side: StrictStr = "example_reference_side"
interval: StrictStr = "example_interval"
offset: Optional[StrictStr] = "example_offset"
tolerance_type: StrictStr = "example_tolerance_type"
rule_name: StrictStr = "example_rule_name"
core_date_tolerance_instance = CoreDateTolerance(reference_side=reference_side, interval=interval, offset=offset, tolerance_type=tolerance_type, rule_name=rule_name)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

