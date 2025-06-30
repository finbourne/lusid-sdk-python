# MetricValue

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** | The numerical value of the property. | [optional] 
**unit** | **str** |  | [optional] 
## Example

```python
from lusid.models.metric_value import MetricValue
from typing import Any, Dict, Optional, Union
from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt, StrictStr

value: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
unit: Optional[StrictStr] = "example_unit"
metric_value_instance = MetricValue(value=value, unit=unit)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

