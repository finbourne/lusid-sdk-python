# UnitsRatio

The number of units you have after the event (output) for a given number of units you have prior to the event (input).
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input** | **float** | Input amount.  Denominator of the Ratio | 
**output** | **float** | Output amount. Numerator of the Ratio | 
**unit_scale_type** | **str** | Determines how units are scaled when processing the event.  Supported values: [NEWO, ADEX]. Available values: NEWO, ADEX. | [optional] 
## Example

```python
from lusid.models.units_ratio import UnitsRatio
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

input: Union[StrictFloat, StrictInt] = # Replace with your value
output: Union[StrictFloat, StrictInt] = # Replace with your value
unit_scale_type: Optional[StrictStr] = "example_unit_scale_type"
units_ratio_instance = UnitsRatio(input=input, output=output, unit_scale_type=unit_scale_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

