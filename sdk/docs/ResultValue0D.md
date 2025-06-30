# ResultValue0D

Result value representing a 0D result. These results can be equipped with a unit
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**units** | **str** | Unit of the result | [optional] 
**value** | **float** | The value of the result | [optional] 
**dimension** | **int** | The dimension of the result. Can be null if there is no sensible way of defining the dimension. This field should not be  populate by the user on upsertion. | [optional] 
**result_value_type** | **str** | The available values are: ResultValue, ResultValueDictionary, ResultValue0D, ResultValueDecimal, ResultValueInt, ResultValueString, ResultValueBool, ResultValueCurrency, CashFlowValue, CashFlowValueSet, ResultValueLifeCycleEventValue, ResultValueDateTimeOffset | 
## Example

```python
from lusid.models.result_value0_d import ResultValue0D
from typing import Any, Dict, Optional, Union
from pydantic.v1 import Field, StrictFloat, StrictInt, StrictStr, validator

units: Optional[StrictStr] = "example_units"
value: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
dimension: Optional[StrictInt] = # Replace with your value
dimension: Optional[StrictInt] = None
result_value_type: StrictStr = "example_result_value_type"
result_value0_d_instance = ResultValue0D(units=units, value=value, dimension=dimension, result_value_type=result_value_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

