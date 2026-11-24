# ReturnMetric

The rate of return over each period of the grid, or over a window looking back from each period when  one is given.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**window** | [**ReturnsMetricWindow**](ReturnsMetricWindow.md) |  | [optional] 
**type** | **str** | Available values: Return, IndicativeAmount. | 
**alias** | **str** |  | [optional] 
## Example

```python
from lusid.models.return_metric import ReturnMetric
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

window: Optional[ReturnsMetricWindow] = None
type: StrictStr = "example_type"
alias: Optional[StrictStr] = "example_alias"
return_metric_instance = ReturnMetric(window=window, type=type, alias=alias)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

