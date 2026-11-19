# CoreMatchingSetTolerance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_names** | **List[str]** | The core rules in the set, at least 2 and each once. The set pairs two items if at least one rule has a value on both sides and the values agree, and no rule has two values that differ. A rule with no value on one or both sides is ignored. No other core tolerance can name a rule of the set. | 
**tolerance_type** | **str** | Polymorphic discriminator. Supported types: CoreStringCross, CoreAttributeOptionality, CoreDateTolerance, Numeric, CoreMatchingSet. Available values: CoreStringCross, CoreAttributeOptionality, CoreDateTolerance, Numeric, CoreMatchingSet. | 
## Example

```python
from lusid.models.core_matching_set_tolerance import CoreMatchingSetTolerance
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

rule_names: List[StrictStr] = # Replace with your value
tolerance_type: StrictStr = "example_tolerance_type"
core_matching_set_tolerance_instance = CoreMatchingSetTolerance(rule_names=rule_names, tolerance_type=tolerance_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

