# MetricValue

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** | The numerical value of the property. | [optional] 
**unit** | **str** |  | [optional] 
## Example

```python
from lusid.models.metric_value import MetricValue
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

value: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
unit: Optional[StrictStr] = "example_unit"
metric_value_instance = MetricValue(value=value, unit=unit)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

