# ShareClassRoundingConvention

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**precision** | **int** | The precision of the rounding: the number of decimal places, or of significant figures when PrecisionType is SignificantFigures. At most 28, and at least 1 for SignificantFigures. Defaults to 0. | [optional] 
**rounding_type** | **str** | The type of rounding, applied at the last decimal place or significant figure. Defaults to None, which leaves the value unrounded. Available values: None, Down, Up, Nearest. | [optional] 
**precision_type** | **str** | What Precision counts: DecimalPlaces (the default) or SignificantFigures. A SignificantFigures convention is not copied onto an instrument created for the share class. Available values: DecimalPlaces, SignificantFigures. | [optional] 
## Example

```python
from lusid.models.share_class_rounding_convention import ShareClassRoundingConvention
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

precision: Optional[StrictInt] = # Replace with your value
precision: Optional[StrictInt] = None
rounding_type: Optional[StrictStr] = "example_rounding_type"
precision_type: Optional[StrictStr] = "example_precision_type"
share_class_rounding_convention_instance = ShareClassRoundingConvention(precision=precision, rounding_type=rounding_type, precision_type=precision_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

