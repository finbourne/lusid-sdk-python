# CashFlowValue

Result class for a cash flow value
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_date** | **datetime** | The payment date of the cash flow | 
**diagnostics** | [**ResultValueDictionary**](ResultValueDictionary.md) |  | [optional] 
**cash_flow_lineage** | [**CashFlowLineage**](CashFlowLineage.md) |  | [optional] 
**payment_amount** | **float** | The amount paid or received | 
**payment_ccy** | **str** | The currency of the transaction | 
**result_value_type** | **str** | The available values are: ResultValue, ResultValueDictionary, ResultValue0D, ResultValueDecimal, ResultValueInt, ResultValueString, ResultValueBool, ResultValueCurrency, CashFlowValue, CashFlowValueSet, ResultValueLifeCycleEventValue, ResultValueDateTimeOffset | 
## Example

```python
from lusid.models.cash_flow_value import CashFlowValue
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

payment_date: datetime = # Replace with your value
diagnostics: Optional[ResultValueDictionary] = None
cash_flow_lineage: Optional[CashFlowLineage] = # Replace with your value
payment_amount: Union[StrictFloat, StrictInt] = # Replace with your value
payment_ccy: StrictStr = "example_payment_ccy"
result_value_type: StrictStr = "example_result_value_type"
cash_flow_value_instance = CashFlowValue(payment_date=payment_date, diagnostics=diagnostics, cash_flow_lineage=cash_flow_lineage, payment_amount=payment_amount, payment_ccy=payment_ccy, result_value_type=result_value_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

