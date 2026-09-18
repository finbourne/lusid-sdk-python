# PortfolioTransactionResult

Represents transaction details for a data quality check result.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_type** | **str** | The type of the entity. Always \&quot;Transaction\&quot;. | [optional] 
**transaction_view** | **str** | Whether this is an input or an output transaction | [optional] 
**as_at** | **datetime** | The as-at timestamp for the transaction | [optional] 
**transaction_date** | **datetime** | The transaction date | [optional] 
**transaction_id** | **str** | The transaction&#39;s identifier within its portfolio | [optional] 
**entity_unique_id** | **str** | The transaction&#39;s unique identifier across portfolios | [optional] 
**source_portfolio_scope** | **str** | The scope of the portfolio this transaction came from | [optional] 
**source_portfolio_code** | **str** | The code of the portfolio this transaction came from | [optional] 
**source_portfolio_entity_unique_id** | **str** | The unique identifier of the portfolio this transaction came from | [optional] 
**source_portfolio_display_name** | **str** | The display name of the portfolio this transaction came from | [optional] 
**lusid_instrument_id** | **str** | The LUSID instrument identifier of the instrument transacted | [optional] 
**instrument_display_name** | **str** | The name of the instrument transacted | [optional] 
**transaction_type** | **str** | The transaction type, e.g. Buy, Sell | [optional] 
## Example

```python
from lusid.models.portfolio_transaction_result import PortfolioTransactionResult
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

entity_type: Optional[StrictStr] = "example_entity_type"
transaction_view: Optional[StrictStr] = "example_transaction_view"
as_at: Optional[datetime] = # Replace with your value
transaction_date: Optional[datetime] = # Replace with your value
transaction_id: Optional[StrictStr] = "example_transaction_id"
entity_unique_id: Optional[StrictStr] = "example_entity_unique_id"
source_portfolio_scope: Optional[StrictStr] = "example_source_portfolio_scope"
source_portfolio_code: Optional[StrictStr] = "example_source_portfolio_code"
source_portfolio_entity_unique_id: Optional[StrictStr] = "example_source_portfolio_entity_unique_id"
source_portfolio_display_name: Optional[StrictStr] = "example_source_portfolio_display_name"
lusid_instrument_id: Optional[StrictStr] = "example_lusid_instrument_id"
instrument_display_name: Optional[StrictStr] = "example_instrument_display_name"
transaction_type: Optional[StrictStr] = "example_transaction_type"
portfolio_transaction_result_instance = PortfolioTransactionResult(entity_type=entity_type, transaction_view=transaction_view, as_at=as_at, transaction_date=transaction_date, transaction_id=transaction_id, entity_unique_id=entity_unique_id, source_portfolio_scope=source_portfolio_scope, source_portfolio_code=source_portfolio_code, source_portfolio_entity_unique_id=source_portfolio_entity_unique_id, source_portfolio_display_name=source_portfolio_display_name, lusid_instrument_id=lusid_instrument_id, instrument_display_name=instrument_display_name, transaction_type=transaction_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

