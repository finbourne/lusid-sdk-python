# TransactionQueryParameters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **str** | The lower bound effective datetime or cut label (inclusive) from which to build the transactions. | 
**end_date** | **str** | The upper bound effective datetime or cut label (inclusive) from which to retrieve transactions. | 
**query_mode** | **str** | The date to compare against the upper and lower bounds for the effective datetime or cut label. Defaults to &#39;TradeDate&#39; if not specified. The available values are: TradeDate, SettleDate | [optional] 
**show_cancelled_transactions** | **bool** | Option to specify whether or not to include cancelled transactions in the output. Defaults to False if not specified. | [optional] 
**timeline_scope** | **str** | Scope of the Timeline for the Portfolio. The Timeline to be used while building transactions | [optional] 
**timeline_code** | **str** | Code of the Timeline for the Portfolio. The Timeline to be used while building transactions. This can optionally include a colon, followed by the Closed Period Id to use at the head of the timeline, for a timeline with unconfirmed periods. | [optional] 
**include_economics** | **bool** | By default is false. When set to true the Economics data would be populated in the response. | [optional] 
**include_settlement_status** | **bool** | By default is false. When set to true the Settlement Status data would be populated in the response. | [optional] 
**settlement_status_date** | **str** | Optional date used to specify end of an extended window for settlement information. When provided, transactions will be returned between start and end date, but settlement information between start date and this date will be included. When provided, the value must be greater than or equal to end date. | [optional] 
## Example

```python
from lusid.models.transaction_query_parameters import TransactionQueryParameters
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

start_date: StrictStr = "example_start_date"
end_date: StrictStr = "example_end_date"
query_mode: Optional[StrictStr] = "example_query_mode"
show_cancelled_transactions: Optional[StrictBool] = # Replace with your value
show_cancelled_transactions:Optional[StrictBool] = None
timeline_scope: Optional[StrictStr] = "example_timeline_scope"
timeline_code: Optional[StrictStr] = "example_timeline_code"
include_economics: Optional[StrictBool] = # Replace with your value
include_economics:Optional[StrictBool] = None
include_settlement_status: Optional[StrictBool] = # Replace with your value
include_settlement_status:Optional[StrictBool] = None
settlement_status_date: Optional[StrictStr] = "example_settlement_status_date"
transaction_query_parameters_instance = TransactionQueryParameters(start_date=start_date, end_date=end_date, query_mode=query_mode, show_cancelled_transactions=show_cancelled_transactions, timeline_scope=timeline_scope, timeline_code=timeline_code, include_economics=include_economics, include_settlement_status=include_settlement_status, settlement_status_date=settlement_status_date)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

