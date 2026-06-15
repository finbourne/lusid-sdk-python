# SettlementActivityQuery

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_at** | **datetime** | The asAt time at which to query settlement activity. Defaults to latest. | [optional] 
**portfolio_entity_ids** | [**List[PortfolioEntityId]**](PortfolioEntityId.md) | The portfolios and / or portfolio groups to query. At least one entry is required. | [optional] 
**start_activity_date** | **str** | Lower bound (inclusive) of the activity date range. If not set, no lower bound is applied. | [optional] 
**end_activity_date** | **str** | Upper bound (inclusive) of the activity date range. Defaults to the current date and time. Treated as effectiveAt. | [optional] 
**filter** | **str** | A LUSID standard filter expression. Supports traversal into transaction and settlementInstruction. | [optional] 
**settlement_instruction_property_keys** | **List[str]** | Settlement instruction property keys to populate on the response. Behaviour matches BuildSettlementInstructions. | [optional] 
**transaction_property_keys** | **List[str]** | Transaction property keys to populate on the response. Behaviour matches BuildSettlementInstructions. | [optional] 
**limit** | **int** | Page size limit; standard pagination control. Defaults to 5000. | [optional] 
**page** | **str** | Pagination cursor returned by a previous response. | [optional] 
## Example

```python
from lusid.models.settlement_activity_query import SettlementActivityQuery
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

as_at: Optional[datetime] = # Replace with your value
portfolio_entity_ids: Optional[List[PortfolioEntityId]] = # Replace with your value
start_activity_date: Optional[StrictStr] = "example_start_activity_date"
end_activity_date: Optional[StrictStr] = "example_end_activity_date"
filter: Optional[StrictStr] = "example_filter"
settlement_instruction_property_keys: Optional[List[StrictStr]] = # Replace with your value
transaction_property_keys: Optional[List[StrictStr]] = # Replace with your value
limit: Optional[StrictInt] = # Replace with your value
limit: Optional[StrictInt] = None
page: Optional[StrictStr] = "example_page"
settlement_activity_query_instance = SettlementActivityQuery(as_at=as_at, portfolio_entity_ids=portfolio_entity_ids, start_activity_date=start_activity_date, end_activity_date=end_activity_date, filter=filter, settlement_instruction_property_keys=settlement_instruction_property_keys, transaction_property_keys=transaction_property_keys, limit=limit, page=page)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

