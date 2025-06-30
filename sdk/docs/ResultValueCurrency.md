# ResultValueCurrency

A simple result for a currency value
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The value itself | [optional] 
**result_value_type** | **str** | The available values are: ResultValue, ResultValueDictionary, ResultValue0D, ResultValueDecimal, ResultValueInt, ResultValueString, ResultValueBool, ResultValueCurrency, CashFlowValue, CashFlowValueSet, ResultValueLifeCycleEventValue, ResultValueDateTimeOffset | 
## Example

```python
from lusid.models.result_value_currency import ResultValueCurrency
from typing import Any, Dict, Optional
from pydantic.v1 import Field, StrictStr, validator

value: Optional[StrictStr] = "example_value"
result_value_type: StrictStr = "example_result_value_type"
result_value_currency_instance = ResultValueCurrency(value=value, result_value_type=result_value_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

