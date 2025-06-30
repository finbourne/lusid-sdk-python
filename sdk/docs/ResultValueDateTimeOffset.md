# ResultValueDateTimeOffset

A simple result for a date time value
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **datetime** | The value itself | [optional] 
**dimension** | **int** | The dimension of the result. Can be null if there is no sensible way of defining the dimension. This field should not be  populate by the user on upsertion. | [optional] 
**result_value_type** | **str** | The available values are: ResultValue, ResultValueDictionary, ResultValue0D, ResultValueDecimal, ResultValueInt, ResultValueString, ResultValueBool, ResultValueCurrency, CashFlowValue, CashFlowValueSet, ResultValueLifeCycleEventValue, ResultValueDateTimeOffset | 
## Example

```python
from lusid.models.result_value_date_time_offset import ResultValueDateTimeOffset
from typing import Any, Dict, Optional
from pydantic.v1 import Field, StrictInt, StrictStr, validator
from datetime import datetime
value: Optional[datetime] = # Replace with your value
dimension: Optional[StrictInt] = # Replace with your value
dimension: Optional[StrictInt] = None
result_value_type: StrictStr = "example_result_value_type"
result_value_date_time_offset_instance = ResultValueDateTimeOffset(value=value, dimension=dimension, result_value_type=result_value_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

