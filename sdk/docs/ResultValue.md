# ResultValue

Base class for representing result values in LUSID.  This base class should not be directly instantiated; each supported ResultValueType has a corresponding inherited class.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result_value_type** | **str** | The available values are: ResultValue, ResultValueDictionary, ResultValue0D, ResultValueDecimal, ResultValueInt, ResultValueString, ResultValueBool, ResultValueCurrency, CashFlowValue, CashFlowValueSet, ResultValueLifeCycleEventValue, ResultValueDateTimeOffset | 
## Example

```python
from lusid.models.result_value import ResultValue
from typing import Any, Dict, Union
from pydantic.v1 import BaseModel, Field, StrictStr, validator

result_value_type: StrictStr = "example_result_value_type"
result_value_instance = ResultValue(result_value_type=result_value_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

