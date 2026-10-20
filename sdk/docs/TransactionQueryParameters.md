# TransactionQueryParameters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **str** | The lower bound effective datetime or cut label (inclusive) from which to build the transactions. | 
**end_date** | **str** | The upper bound effective datetime or cut label (inclusive) from which to retrieve transactions. | 
**query_mode** | **str** | The date to compare against the upper and lower bounds for the effective datetime or cut label. Default value: TradeDate. Available values: TradeDate, SettleDate. | [optional] 
**show_cancelled_transactions** | **bool** | Option to specify whether or not to include cancelled transactions in the output. Defaults to False if not specified. | [optional] 
**timeline_scope** | **str** | Scope of the Timeline for the Portfolio. The Timeline to be used while building transactions | [optional] 
**timeline_code** | **str** | Code of the Timeline for the Portfolio. The Timeline to be used while building transactions. This can optionally include a colon, followed by the Closed Period Id to use at the head of the timeline, for a timeline with unconfirmed periods. | [optional] 
**include_economics** | **bool** | By default is false. When set to true the Economics data would be populated in the response. | [optional] 
**include_settlement_status** | **bool** | By default is false. When set to true the Settlement Status data would be populated in the response. | [optional] 
**settlement_status_date** | **str** | Optional date used to specify end of an extended window for settlement information. When provided, transactions will be returned between start and end date, but settlement information between start date and this date will be included. When provided, the value must be greater than or equal to end date. | [optional] 
**return_excluded_transactions** | **bool** | Option to specify whether or not to include transactions that are marked as excluded by the portfolio&#39;s transaction exclusion filter. Excluded transactions do not affect holdings. Defaults to false if not specified. | [optional] 
**allocation_expansion** | **str** | How an input transaction that was split into allocation slices (strategy tag allocations or a prorated allocation method) is presented. &#39;Expanded&#39; (the default) returns one output transaction per slice. &#39;Combined&#39; returns one output transaction per input transaction with units, consideration and realised gain/loss summed over the slices, with every realised gain/loss record of each slice, including zero-realised ones, listed with its own transaction type and sub-holding key properties. For a prorated type with no units side the combined units are the total position the slices were prorated over, not the input&#39;s units. Transaction filters apply per slice, so a filter on a slice-level property combines only the matching slices. Sequence numbers are assigned after combining. Holdings and tax lots are identical in both modes. Available values: Expanded, Combined. | [optional] 
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
return_excluded_transactions: Optional[StrictBool] = # Replace with your value
return_excluded_transactions:Optional[StrictBool] = None
allocation_expansion: Optional[StrictStr] = "example_allocation_expansion"
transaction_query_parameters_instance = TransactionQueryParameters(start_date=start_date, end_date=end_date, query_mode=query_mode, show_cancelled_transactions=show_cancelled_transactions, timeline_scope=timeline_scope, timeline_code=timeline_code, include_economics=include_economics, include_settlement_status=include_settlement_status, settlement_status_date=settlement_status_date, return_excluded_transactions=return_excluded_transactions, allocation_expansion=allocation_expansion)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

