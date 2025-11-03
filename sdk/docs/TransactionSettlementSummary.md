# TransactionSettlementSummary

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**overall_status** | [**CategorySettlementStatus**](CategorySettlementStatus.md) |  | 
**stock_status** | [**CategorySettlementStatus**](CategorySettlementStatus.md) |  | 
**cash_status** | [**CategorySettlementStatus**](CategorySettlementStatus.md) |  | 
**deferred_cash_receipt_status** | [**CategorySettlementStatus**](CategorySettlementStatus.md) |  | 
## Example

```python
from lusid.models.transaction_settlement_summary import TransactionSettlementSummary
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

overall_status: CategorySettlementStatus = # Replace with your value
stock_status: CategorySettlementStatus = # Replace with your value
cash_status: CategorySettlementStatus = # Replace with your value
deferred_cash_receipt_status: CategorySettlementStatus = # Replace with your value
transaction_settlement_summary_instance = TransactionSettlementSummary(overall_status=overall_status, stock_status=stock_status, cash_status=cash_status, deferred_cash_receipt_status=deferred_cash_receipt_status)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

