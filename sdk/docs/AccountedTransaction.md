# AccountedTransaction

The Valuation Point Data Response for the Fund and specified date.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounting_date** | **datetime** | The transaction&#39;s accounting date. | [optional] 
**journal_entry_action** | **str** | The journal entry line action associated with this transaction. | [optional] 
**transaction** | [**OutputTransaction**](OutputTransaction.md) |  | [optional] 
**portfolio_id** | [**PortfolioId**](PortfolioId.md) |  | [optional] 
## Example

```python
from lusid.models.accounted_transaction import AccountedTransaction
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr
from datetime import datetime
accounting_date: Optional[datetime] = # Replace with your value
journal_entry_action: Optional[StrictStr] = "example_journal_entry_action"
transaction: Optional[OutputTransaction] = None
portfolio_id: Optional[PortfolioId] = # Replace with your value
accounted_transaction_instance = AccountedTransaction(accounting_date=accounting_date, journal_entry_action=journal_entry_action, transaction=transaction, portfolio_id=portfolio_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

