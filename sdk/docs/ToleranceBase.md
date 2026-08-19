# ToleranceBase

Base class for the tolerances that relax how strictly a matching rule compares its two sides. Polymorphic  by ToleranceType; each supported type has a corresponding inherited class.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tolerance_type** | **str** | Polymorphic discriminator. Supported types: CoreStringCross, CoreAttributeOptionality, CoreDateTolerance, Numeric. Available values: CoreStringCross, CoreAttributeOptionality, CoreDateTolerance, Numeric. | 
**rule_name** | **str** | The reference name of the rule that this tolerance relaxes. | 
## Example

```python
from lusid.models.tolerance_base import ToleranceBase
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

tolerance_type: StrictStr = "example_tolerance_type"
rule_name: StrictStr = "example_rule_name"
tolerance_base_instance = ToleranceBase(tolerance_type=tolerance_type, rule_name=rule_name)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

