# ResultValueDictionary

Result value for a collection of key-value pairs. Used for diagnostics associated to a cash flow, etc.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**elements** | [**Dict[str, ResultValue]**](ResultValue.md) | The dictionary elements | [optional] 
**result_value_type** | **str** | The available values are: ResultValue, ResultValueDictionary, ResultValue0D, ResultValueDecimal, ResultValueInt, ResultValueString, ResultValueBool, ResultValueCurrency, CashFlowValue, CashFlowValueSet, ResultValueLifeCycleEventValue, ResultValueDateTimeOffset | 
## Example

```python
from lusid.models.result_value_dictionary import ResultValueDictionary
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

elements: Optional[Dict[str, ResultValue]] = # Replace with your value
result_value_type: StrictStr = "example_result_value_type"
result_value_dictionary_instance = ResultValueDictionary(elements=elements, result_value_type=result_value_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

