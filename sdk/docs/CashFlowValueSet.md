# CashFlowValueSet

Result value for a collection of cash flow values
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cashflows** | [**List[CashFlowValue]**](CashFlowValue.md) | The set of cash flows in the result | [optional] 
**result_value_type** | **str** | The available values are: ResultValue, ResultValueDictionary, ResultValue0D, ResultValueDecimal, ResultValueInt, ResultValueString, ResultValueBool, ResultValueCurrency, CashFlowValue, CashFlowValueSet, ResultValueLifeCycleEventValue, ResultValueDateTimeOffset | 
## Example

```python
from lusid.models.cash_flow_value_set import CashFlowValueSet
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

cashflows: Optional[List[CashFlowValue]] = # Replace with your value
result_value_type: StrictStr = "example_result_value_type"
cash_flow_value_set_instance = CashFlowValueSet(cashflows=cashflows, result_value_type=result_value_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

