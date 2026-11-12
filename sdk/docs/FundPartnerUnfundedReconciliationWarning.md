# FundPartnerUnfundedReconciliationWarning

A soft warning on an unfunded commitment statement: the statement is still produced, with a caveat.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The warning. PeriodStartsBeforeAdmission: the period opens before the partner was admitted, so the opening balances are zero and the admission commitment is counted as a commitment change. | 
**admitted_on** | **datetime** | For PeriodStartsBeforeAdmission, the date the partner was admitted to the fund. | [optional] 
## Example

```python
from lusid.models.fund_partner_unfunded_reconciliation_warning import FundPartnerUnfundedReconciliationWarning
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

code: StrictStr = "example_code"
admitted_on: Optional[datetime] = # Replace with your value
fund_partner_unfunded_reconciliation_warning_instance = FundPartnerUnfundedReconciliationWarning(code=code, admitted_on=admitted_on)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

