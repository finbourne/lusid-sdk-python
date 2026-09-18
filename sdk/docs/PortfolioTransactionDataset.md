# PortfolioTransactionDataset

Contains the run-time parameters that are appropriate for check definitions  with datasetSchema.type = \"PortfolioContents\" and datasetSchema.entityType = \"Transaction\"
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_at** | **datetime** | The asAt date to fetch the data. Nullable. Defaults to latest. | [optional] 
**from_effective_date** | **datetime** | The earliest transaction date to check, inclusive. Nullable. Unbounded if not provided. | [optional] 
**to_effective_date** | **datetime** | The latest transaction date to check, inclusive. Nullable — the window is unbounded above if not  provided. This value also resolves as the run&#39;s effectiveAt, so portfolios are resolved and transactions  decorated as of it; when not provided, that defaults to latest. Must be on or after fromEffectiveDate  when both are provided. | [optional] 
**portfolio_scope** | **str** | The scope of the portfolios whose transactions to check. Nullable. Every scope is checked if not provided. | [optional] 
**portfolio_selector_attribute** | **str** | An attribute (field name or propertyKey) to use to narrow down the portfolios whose transactions are  checked. Cannot be provided without portfolioSelectorValue, and vice versa. | [optional] 
**portfolio_selector_value** | **str** | The value of the above attribute used to narrow down the portfolios. Cannot be provided without  portfolioSelectorAttribute, and vice versa. | [optional] 
**transaction_selector_attribute** | **str** | An attribute (field name or propertyKey) to use to narrow down the transactions checked within those  portfolios. Cannot be provided without transactionSelectorValue, and vice versa. | [optional] 
**transaction_selector_value** | **str** | The value of the above attribute used to narrow down the transactions. Cannot be provided without  transactionSelectorAttribute, and vice versa. | [optional] 
## Example

```python
from lusid.models.portfolio_transaction_dataset import PortfolioTransactionDataset
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

as_at: Optional[datetime] = # Replace with your value
from_effective_date: Optional[datetime] = # Replace with your value
to_effective_date: Optional[datetime] = # Replace with your value
portfolio_scope: Optional[StrictStr] = "example_portfolio_scope"
portfolio_selector_attribute: Optional[StrictStr] = "example_portfolio_selector_attribute"
portfolio_selector_value: Optional[StrictStr] = "example_portfolio_selector_value"
transaction_selector_attribute: Optional[StrictStr] = "example_transaction_selector_attribute"
transaction_selector_value: Optional[StrictStr] = "example_transaction_selector_value"
portfolio_transaction_dataset_instance = PortfolioTransactionDataset(as_at=as_at, from_effective_date=from_effective_date, to_effective_date=to_effective_date, portfolio_scope=portfolio_scope, portfolio_selector_attribute=portfolio_selector_attribute, portfolio_selector_value=portfolio_selector_value, transaction_selector_attribute=transaction_selector_attribute, transaction_selector_value=transaction_selector_value)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

