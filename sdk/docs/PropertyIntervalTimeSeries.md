# PropertyIntervalTimeSeries

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The property key that this time series belongs to. | 
**values** | [**List[PropertyInterval]**](PropertyInterval.md) | The complete time series (history) of intervals for the property key. | 
## Example

```python
from lusid.models.property_interval_time_series import PropertyIntervalTimeSeries
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

key: StrictStr = "example_key"
values: List[PropertyInterval] = # Replace with your value
property_interval_time_series_instance = PropertyIntervalTimeSeries(key=key, values=values)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

