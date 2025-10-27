# FundValuationRequest

Specification object for the parameters of a valuation
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_at** | **datetime** | The asAt date to use. | [optional] 
**metrics** | [**List[AggregateSpec]**](AggregateSpec.md) | The set of specifications to calculate or retrieve during the valuation and present in the results. For example:  AggregateSpec(&#39;Valuation/PV&#39;,&#39;Sum&#39;) for returning the PV (present value) of holdings  AggregateSpec(&#39;Holding/default/Units&#39;,&#39;Sum&#39;) for returning the units of holidays  AggregateSpec(&#39;Instrument/default/LusidInstrumentId&#39;,&#39;Value&#39;) for returning the Lusid Instrument identifier | 
**group_by** | **List[str]** | The set of items by which to perform grouping. This primarily matters when one or more of the metric operators is a mapping  that reduces set size, e.g. sum or proportion. The group-by statement determines the set of keys by which to break the results out. | [optional] 
**filters** | [**List[PropertyFilter]**](PropertyFilter.md) | A set of filters to use to reduce the data found in a request. Equivalent to the &#39;where ...&#39; part of a Sql select statement.  For example, filter a set of values within a given range or matching a particular value. | [optional] 
**sort** | [**List[OrderBySpec]**](OrderBySpec.md) | A (possibly empty/null) set of specifications for how to order the results. | [optional] 
**equip_with_subtotals** | **bool** | Flag directing the Valuation call to populate the results with subtotals of aggregates. | [optional] 
**return_result_as_expanded_types** | **bool** | Financially meaningful results can be presented as either simple flat types or more complex expanded types.  For example, the present value (PV) of a holding could be represented either as a simple decimal (with currency implied)  or as a decimal-currency pair. This flag allows either representation to be returned. In the PV example,  the returned value would be the decimal-currency pair if this flag is true, or the decimal only if this flag is false. | [optional] 
**include_order_flow** | [**OrderFlowConfiguration**](OrderFlowConfiguration.md) |  | [optional] 
**fund_valuation_schedule** | [**FundValuationSchedule**](FundValuationSchedule.md) |  | 
**market_data_overrides** | [**MarketDataOverrides**](MarketDataOverrides.md) |  | [optional] 
**corporate_action_source_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
## Example

```python
from lusid.models.fund_valuation_request import FundValuationRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

as_at: Optional[datetime] = # Replace with your value
metrics: List[AggregateSpec] = # Replace with your value
group_by: Optional[List[StrictStr]] = # Replace with your value
filters: Optional[List[PropertyFilter]] = # Replace with your value
sort: Optional[List[OrderBySpec]] = # Replace with your value
equip_with_subtotals: Optional[StrictBool] = # Replace with your value
equip_with_subtotals:Optional[StrictBool] = None
return_result_as_expanded_types: Optional[StrictBool] = # Replace with your value
return_result_as_expanded_types:Optional[StrictBool] = None
include_order_flow: Optional[OrderFlowConfiguration] = # Replace with your value
fund_valuation_schedule: FundValuationSchedule = # Replace with your value
market_data_overrides: Optional[MarketDataOverrides] = # Replace with your value
corporate_action_source_id: Optional[ResourceId] = # Replace with your value
fund_valuation_request_instance = FundValuationRequest(as_at=as_at, metrics=metrics, group_by=group_by, filters=filters, sort=sort, equip_with_subtotals=equip_with_subtotals, return_result_as_expanded_types=return_result_as_expanded_types, include_order_flow=include_order_flow, fund_valuation_schedule=fund_valuation_schedule, market_data_overrides=market_data_overrides, corporate_action_source_id=corporate_action_source_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

