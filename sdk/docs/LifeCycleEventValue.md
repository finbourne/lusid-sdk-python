# LifeCycleEventValue

The instrument life cycle event result value type
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_date** | **datetime** | The effective date of the event | [optional] 
**event_values** | [**ResultValueDictionary**](ResultValueDictionary.md) |  | [optional] 
**event_lineage** | [**LifeCycleEventLineage**](LifeCycleEventLineage.md) |  | [optional] 
**result_value_type** | **str** | The available values are: ResultValue, ResultValueDictionary, ResultValue0D, ResultValueDecimal, ResultValueInt, ResultValueString, ResultValueBool, ResultValueCurrency, CashFlowValue, CashFlowValueSet, ResultValueLifeCycleEventValue, ResultValueDateTimeOffset | 
## Example

```python
from lusid.models.life_cycle_event_value import LifeCycleEventValue
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

effective_date: Optional[datetime] = # Replace with your value
event_values: Optional[ResultValueDictionary] = # Replace with your value
event_lineage: Optional[LifeCycleEventLineage] = # Replace with your value
result_value_type: StrictStr = "example_result_value_type"
life_cycle_event_value_instance = LifeCycleEventValue(effective_date=effective_date, event_values=event_values, event_lineage=event_lineage, result_value_type=result_value_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

