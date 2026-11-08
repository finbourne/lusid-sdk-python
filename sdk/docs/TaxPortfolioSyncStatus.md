# TaxPortfolioSyncStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**portfolio_id** | [**ResourceId**](ResourceId.md) |  | 
**last_transaction_as_at** | **datetime** | The asAt the latest transaction was booked to the portfolio. Absent when the portfolio has no transactions. | [optional] 
**last_tax_as_at** | **datetime** | The asAt the tax engine last processed the Fund, taken from its latest valuation point. Absent when no valuation point has been run. | [optional] 
**in_sync** | **bool** | True when the tax position is no older than the latest booked transaction, or the portfolio has no transactions. | 
**asset_class** | **str** | The asset class of the portfolio&#39;s holdings where the holding data carries one. Optional. | [optional] 
**country_of_domicile** | **str** | The country of domicile of the portfolio&#39;s holdings where the holding data carries one. Optional. | [optional] 
## Example

```python
from lusid.models.tax_portfolio_sync_status import TaxPortfolioSyncStatus
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

portfolio_id: ResourceId = # Replace with your value
last_transaction_as_at: Optional[datetime] = # Replace with your value
last_tax_as_at: Optional[datetime] = # Replace with your value
in_sync: StrictBool = # Replace with your value
in_sync:StrictBool = True
asset_class: Optional[StrictStr] = "example_asset_class"
country_of_domicile: Optional[StrictStr] = "example_country_of_domicile"
tax_portfolio_sync_status_instance = TaxPortfolioSyncStatus(portfolio_id=portfolio_id, last_transaction_as_at=last_transaction_as_at, last_tax_as_at=last_tax_as_at, in_sync=in_sync, asset_class=asset_class, country_of_domicile=country_of_domicile)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

