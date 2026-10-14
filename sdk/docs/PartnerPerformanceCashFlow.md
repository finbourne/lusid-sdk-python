# PartnerPerformanceCashFlow

One dated cash flow the net IRR was solved from, signed from the partner's point of view.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** | The date of the cash flow. | 
**amount** | **float** | The amount of the cash flow, negative for contributions and positive for distributions and the residual value. | 
**kind** | **str** | The kind of cash flow: Contribution, Distribution or ResidualValue. | 
## Example

```python
from lusid.models.partner_performance_cash_flow import PartnerPerformanceCashFlow
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

var_date: datetime = # Replace with your value
amount: Union[StrictFloat, StrictInt] = # Replace with your value
kind: StrictStr = "example_kind"
partner_performance_cash_flow_instance = PartnerPerformanceCashFlow(var_date=var_date, amount=amount, kind=kind)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

