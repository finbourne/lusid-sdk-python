# TransactionQueryParameters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **str** | The lower bound effective datetime or cut label (inclusive) from which to build the transactions. | 
**end_date** | **str** | The upper bound effective datetime or cut label (inclusive) from which to retrieve transactions. | 
**query_mode** | **str** | The date to compare against the upper and lower bounds for the effective datetime or cut label. Defaults to &#39;TradeDate&#39; if not specified. The available values are: TradeDate, SettleDate | [optional] 
**show_cancelled_transactions** | **bool** | Option to specify whether or not to include cancelled transactions in the output. Defaults to False if not specified. | [optional] 
**timeline_scope** | **str** | Scope of the Timeline for the Portfolio. The Timeline to be used while building transactions | [optional] 
**timeline_code** | **str** | Code of the Timeline for the Portfolio. The Timeline to be used while building transactions | [optional] 
**include_economics** | **bool** | By default is false. When set to true the Economics data would be populated in the response. | [optional] 
## Example

```python
from lusid.models.transaction_query_parameters import TransactionQueryParameters
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictBool, StrictStr, constr, validator

start_date: StrictStr = "example_start_date"
end_date: StrictStr = "example_end_date"
query_mode: Optional[StrictStr] = "example_query_mode"
show_cancelled_transactions: Optional[StrictBool] = # Replace with your value
show_cancelled_transactions:Optional[StrictBool] = None
timeline_scope: Optional[StrictStr] = "example_timeline_scope"
timeline_code: Optional[StrictStr] = "example_timeline_code"
include_economics: Optional[StrictBool] = # Replace with your value
include_economics:Optional[StrictBool] = None
transaction_query_parameters_instance = TransactionQueryParameters(start_date=start_date, end_date=end_date, query_mode=query_mode, show_cancelled_transactions=show_cancelled_transactions, timeline_scope=timeline_scope, timeline_code=timeline_code, include_economics=include_economics)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

