# AggregateToleranceBase

Abstract base for tolerances that apply to aggregate matching rules. Distinguishes aggregate  tolerances from core tolerances at the type level (both share a common tolerance base).
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tolerance_type** | **str** | Polymorphic discriminator. Supported types: CoreStringCross, CoreAttributeOptionality, CoreDateTolerance, Numeric. Available values: CoreStringCross, CoreAttributeOptionality, CoreDateTolerance, Numeric. | 
**rule_name** | **str** | The reference name of the rule that this tolerance relaxes. | 
## Example

```python
from lusid.models.aggregate_tolerance_base import AggregateToleranceBase
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

tolerance_type: StrictStr = "example_tolerance_type"
rule_name: StrictStr = "example_rule_name"
aggregate_tolerance_base_instance = AggregateToleranceBase(tolerance_type=tolerance_type, rule_name=rule_name)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

