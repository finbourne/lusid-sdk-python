# LoanPeriod

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_date** | **datetime** |  | 
**notional** | **float** |  | 
**interest_amount** | **float** |  | 
## Example

```python
from lusid.models.loan_period import LoanPeriod
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

payment_date: datetime = # Replace with your value
notional: Union[StrictFloat, StrictInt]
interest_amount: Union[StrictFloat, StrictInt] = # Replace with your value
loan_period_instance = LoanPeriod(payment_date=payment_date, notional=notional, interest_amount=interest_amount)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

