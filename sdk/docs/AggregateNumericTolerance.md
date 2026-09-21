# AggregateNumericTolerance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference_side** | **str** | Reference side (source of truth). One of: Left, Right. Available values: Left, Right. | 
**absolute_threshold** | **float** | Numeric tolerance absolute value (allowable diff compared to the reference side value). | [optional] 
**relative_threshold** | **float** | Numeric tolerance value as a relative % of the reference value. | [optional] 
**threshold_priority** | **str** | Whether to apply the GreaterOf or LesserOf the absoluteThreshold vs relativeThreshold. One of: GreaterOf, LesserOf. Available values: GreaterOf, LesserOf. | 
**offset** | **str** | How the threshold should be applied to the reference side value. One of: Above, Below, Either. Defaults to Either. Available values: Above, Below, Either. | [optional] 
**tolerance_type** | **str** | Polymorphic discriminator. Supported types: CoreStringCross, CoreAttributeOptionality, CoreDateTolerance, Numeric. Available values: CoreStringCross, CoreAttributeOptionality, CoreDateTolerance, Numeric. | 
**rule_name** | **str** | The reference name of the rule that this tolerance relaxes. | 
## Example

```python
from lusid.models.aggregate_numeric_tolerance import AggregateNumericTolerance
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

reference_side: StrictStr = "example_reference_side"
absolute_threshold: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
relative_threshold: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
threshold_priority: StrictStr = "example_threshold_priority"
offset: Optional[StrictStr] = "example_offset"
tolerance_type: StrictStr = "example_tolerance_type"
rule_name: StrictStr = "example_rule_name"
aggregate_numeric_tolerance_instance = AggregateNumericTolerance(reference_side=reference_side, absolute_threshold=absolute_threshold, relative_threshold=relative_threshold, threshold_priority=threshold_priority, offset=offset, tolerance_type=tolerance_type, rule_name=rule_name)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

