# FacilityPayableLine

A principal line on the facility payable in a Fund's journal.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** | The line&#39;s activity date. | 
**principal** | **float** | The principal the line puts on the payable: positive for a draw, negative for a repayment. | 
**currency** | **str** | The currency of the line. | 
**general_ledger_account_code** | **str** | The general ledger account the Fund&#39;s posting rules mapped the line to. Absent when no rule mapped it. | [optional] 
**transaction_id** | **str** | The transaction that booked the line. | 
**facility_id** | **str** | The Facility the transaction names. Absent when it names none. | [optional] 
## Example

```python
from lusid.models.facility_payable_line import FacilityPayableLine
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

var_date: datetime = # Replace with your value
principal: Union[StrictFloat, StrictInt] = # Replace with your value
currency: StrictStr = "example_currency"
general_ledger_account_code: Optional[StrictStr] = "example_general_ledger_account_code"
transaction_id: StrictStr = "example_transaction_id"
facility_id: Optional[StrictStr] = "example_facility_id"
facility_payable_line_instance = FacilityPayableLine(var_date=var_date, principal=principal, currency=currency, general_ledger_account_code=general_ledger_account_code, transaction_id=transaction_id, facility_id=facility_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

