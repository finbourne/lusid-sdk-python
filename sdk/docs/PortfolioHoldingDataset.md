# PortfolioHoldingDataset

Contains the run-time parameters that are appropriate for check definitions  with datasetSchema.type = \"PortfolioContents\"
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_at** | **datetime** | The asAt date to fetch the data. Nullable. Defaults to latest. | [optional] 
**effective_at** | **datetime** | The effectiveAt date to fetch the data. Nullable. Defaults to latest. | [optional] 
**portfolio_scope** | **str** | The scope of the portfolios whose holdings to check. Nullable. Every scope is checked if not provided. | [optional] 
**portfolio_selector_attribute** | **str** | An attribute (field name or propertyKey) to use to narrow down the portfolios whose holdings are checked. | [optional] 
**portfolio_selector_value** | **str** | The value of the above attribute used to narrow down the portfolios. | [optional] 
**holding_selector_attribute** | **str** | An attribute (field name, propertyKey or sub-holding key) to use to narrow down the holdings checked  within those portfolios. | [optional] 
**holding_selector_value** | **str** | The value of the above attribute used to narrow down the holdings. | [optional] 
**by_taxlots** | **bool** | Whether to expand holdings to their underlying tax lots. Defaults to false. | [optional] 
## Example

```python
from lusid.models.portfolio_holding_dataset import PortfolioHoldingDataset
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

as_at: Optional[datetime] = # Replace with your value
effective_at: Optional[datetime] = # Replace with your value
portfolio_scope: Optional[StrictStr] = "example_portfolio_scope"
portfolio_selector_attribute: Optional[StrictStr] = "example_portfolio_selector_attribute"
portfolio_selector_value: Optional[StrictStr] = "example_portfolio_selector_value"
holding_selector_attribute: Optional[StrictStr] = "example_holding_selector_attribute"
holding_selector_value: Optional[StrictStr] = "example_holding_selector_value"
by_taxlots: Optional[StrictBool] = # Replace with your value
by_taxlots:Optional[StrictBool] = None
portfolio_holding_dataset_instance = PortfolioHoldingDataset(as_at=as_at, effective_at=effective_at, portfolio_scope=portfolio_scope, portfolio_selector_attribute=portfolio_selector_attribute, portfolio_selector_value=portfolio_selector_value, holding_selector_attribute=holding_selector_attribute, holding_selector_value=holding_selector_value, by_taxlots=by_taxlots)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

