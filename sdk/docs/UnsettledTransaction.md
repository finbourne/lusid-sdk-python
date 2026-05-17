# UnsettledTransaction

A transaction that remains unsettled as at the valuation point, with per-bucket settlement status.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction** | [**OutputTransaction**](OutputTransaction.md) |  | [optional] 
**portfolio_id** | [**PortfolioId**](PortfolioId.md) |  | [optional] 
**overall_settlement_status** | **str** | The overall settlement status of the transaction (Unsettled, PartSettled, Settled, None). | [optional] 
**overall_is_overdue** | **bool** | Whether the transaction is overdue for settlement. | [optional] 
**cash_settlement_status** | **str** | The settlement status of the cash component. | [optional] 
**cash_is_overdue** | **bool** | Whether the cash component is overdue for settlement. | [optional] 
**stock_settlement_status** | **str** | The settlement status of the stock component. | [optional] 
**stock_is_overdue** | **bool** | Whether the stock component is overdue for settlement. | [optional] 
**deferred_cash_settlement_status** | **str** | The settlement status of the deferred cash component. | [optional] 
**deferred_cash_is_overdue** | **bool** | Whether the deferred cash component is overdue for settlement. | [optional] 
## Example

```python
from lusid.models.unsettled_transaction import UnsettledTransaction
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

transaction: Optional[OutputTransaction] = None
portfolio_id: Optional[PortfolioId] = # Replace with your value
overall_settlement_status: Optional[StrictStr] = "example_overall_settlement_status"
overall_is_overdue: Optional[StrictBool] = # Replace with your value
overall_is_overdue:Optional[StrictBool] = None
cash_settlement_status: Optional[StrictStr] = "example_cash_settlement_status"
cash_is_overdue: Optional[StrictBool] = # Replace with your value
cash_is_overdue:Optional[StrictBool] = None
stock_settlement_status: Optional[StrictStr] = "example_stock_settlement_status"
stock_is_overdue: Optional[StrictBool] = # Replace with your value
stock_is_overdue:Optional[StrictBool] = None
deferred_cash_settlement_status: Optional[StrictStr] = "example_deferred_cash_settlement_status"
deferred_cash_is_overdue: Optional[StrictBool] = # Replace with your value
deferred_cash_is_overdue:Optional[StrictBool] = None
unsettled_transaction_instance = UnsettledTransaction(transaction=transaction, portfolio_id=portfolio_id, overall_settlement_status=overall_settlement_status, overall_is_overdue=overall_is_overdue, cash_settlement_status=cash_settlement_status, cash_is_overdue=cash_is_overdue, stock_settlement_status=stock_settlement_status, stock_is_overdue=stock_is_overdue, deferred_cash_settlement_status=deferred_cash_settlement_status, deferred_cash_is_overdue=deferred_cash_is_overdue)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

