# ReturnsMetricWindow

The window a metric looks back over from each period of the grid, such as the last three months or the  time since inception, and how the metric is reported over it.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lookback** | **str** |  | 
**allow_partial** | **bool** |  | [optional] 
**annualised** | **bool** |  | [optional] 
## Example

```python
from lusid.models.returns_metric_window import ReturnsMetricWindow
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

lookback: StrictStr = "example_lookback"
allow_partial: Optional[StrictBool] = # Replace with your value
allow_partial:Optional[StrictBool] = None
annualised: Optional[StrictBool] = None
annualised:Optional[StrictBool] = None
returns_metric_window_instance = ReturnsMetricWindow(lookback=lookback, allow_partial=allow_partial, annualised=annualised)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

