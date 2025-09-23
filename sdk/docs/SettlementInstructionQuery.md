# SettlementInstructionQuery

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **str** |  | [optional] 
**end_date** | **str** |  | [optional] 
**limit** | **int** |  | [optional] 
**page** | **str** |  | [optional] 
**filter** | **str** |  | [optional] 
**settlement_instruction_property_keys** | **List[str]** |  | [optional] 
**transaction_property_keys** | **List[str]** |  | [optional] 
## Example

```python
from lusid.models.settlement_instruction_query import SettlementInstructionQuery
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictInt, StrictStr, conlist, constr, validator

start_date: Optional[StrictStr] = "example_start_date"
end_date: Optional[StrictStr] = "example_end_date"
limit: Optional[StrictInt] = None
limit: Optional[StrictInt] = None
page: Optional[StrictStr] = "example_page"
filter: Optional[StrictStr] = "example_filter"
settlement_instruction_property_keys: Optional[conlist(StrictStr)] = # Replace with your value
transaction_property_keys: Optional[conlist(StrictStr)] = # Replace with your value
settlement_instruction_query_instance = SettlementInstructionQuery(start_date=start_date, end_date=end_date, limit=limit, page=page, filter=filter, settlement_instruction_property_keys=settlement_instruction_property_keys, transaction_property_keys=transaction_property_keys)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

