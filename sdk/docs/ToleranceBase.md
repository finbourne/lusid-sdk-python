# ToleranceBase

Base class for the tolerances that relax how strictly a matching rule compares its two sides. Polymorphic  by ToleranceType; each supported type has a corresponding inherited class.
## Example

```python
from lusid.models.tolerance_base import ToleranceBase
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

# Example with ToleranceBase 

aggregate_numeric_tolerance_instance = lusid.models.aggregate_numeric_tolerance.AggregateNumericTolerance(
                        reference_side = '', 
                        absolute_threshold = 1.337, 
                        relative_threshold = 1.337, 
                        threshold_priority = '', 
                        offset = '', 
                        tolerance_type = '', 
                        rule_name = '', )

tolerance_base_instance = ToleranceBase(aggregate_numeric_tolerance_instance)

```
See all compatible oneOf types with ToleranceBase


 * [CoreAttributeOptionalityTolerance](./CoreAttributeOptionalityTolerance.md)

 * [CoreDateTolerance](./CoreDateTolerance.md)

 * [CoreStringCrossTolerance](./CoreStringCrossTolerance.md)

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

