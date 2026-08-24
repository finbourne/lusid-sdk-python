# PortfolioHoldingResult

Represents holding details for a data quality check result, where LusidEntityResult represents a scope-and-code  or identifier-addressed entity. A holding has no scope and code of its own, so it is identified by the portfolio  it came from plus what distinguishes it within that portfolio.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_type** | **str** | The type of the entity. Always \&quot;Holding\&quot;. | [optional] 
**as_at** | **datetime** | The as-at timestamp for the holding | [optional] 
**effective_at** | **datetime** | The effective-at timestamp for the holding | [optional] 
**source_portfolio_scope** | **str** | The scope of the portfolio this holding came from | [optional] 
**source_portfolio_code** | **str** | The code of the portfolio this holding came from | [optional] 
**source_portfolio_entity_unique_id** | **str** | The unique identifier of the portfolio this holding came from | [optional] 
**source_portfolio_display_name** | **str** | The display name of the portfolio this holding came from | [optional] 
**holding_id** | **str** | The holding&#39;s identifier within its portfolio | [optional] 
**taxlot_id** | **str** | The tax lot identifier, where the holding was expanded to tax lots. Null otherwise. | [optional] 
**sub_entity_id** | **str** | Identifies the holding to the derived property explain API: the holding id on its own, or the holding id  and tax lot id colon-separated where a tax lot is present. | [optional] 
**lusid_instrument_id** | **str** | The LUSID instrument identifier of the instrument held | [optional] 
**instrument_display_name** | **str** | The name of the instrument held | [optional] 
**holding_type_name** | **str** | The kind of holding, e.g. Position, Balance | [optional] 
**currency** | **str** | The currency of the holding | [optional] 
## Example

```python
from lusid.models.portfolio_holding_result import PortfolioHoldingResult
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

entity_type: Optional[StrictStr] = "example_entity_type"
as_at: Optional[datetime] = # Replace with your value
effective_at: Optional[datetime] = # Replace with your value
source_portfolio_scope: Optional[StrictStr] = "example_source_portfolio_scope"
source_portfolio_code: Optional[StrictStr] = "example_source_portfolio_code"
source_portfolio_entity_unique_id: Optional[StrictStr] = "example_source_portfolio_entity_unique_id"
source_portfolio_display_name: Optional[StrictStr] = "example_source_portfolio_display_name"
holding_id: Optional[StrictStr] = "example_holding_id"
taxlot_id: Optional[StrictStr] = "example_taxlot_id"
sub_entity_id: Optional[StrictStr] = "example_sub_entity_id"
lusid_instrument_id: Optional[StrictStr] = "example_lusid_instrument_id"
instrument_display_name: Optional[StrictStr] = "example_instrument_display_name"
holding_type_name: Optional[StrictStr] = "example_holding_type_name"
currency: Optional[StrictStr] = "example_currency"
portfolio_holding_result_instance = PortfolioHoldingResult(entity_type=entity_type, as_at=as_at, effective_at=effective_at, source_portfolio_scope=source_portfolio_scope, source_portfolio_code=source_portfolio_code, source_portfolio_entity_unique_id=source_portfolio_entity_unique_id, source_portfolio_display_name=source_portfolio_display_name, holding_id=holding_id, taxlot_id=taxlot_id, sub_entity_id=sub_entity_id, lusid_instrument_id=lusid_instrument_id, instrument_display_name=instrument_display_name, holding_type_name=holding_type_name, currency=currency)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

