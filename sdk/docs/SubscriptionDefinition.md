# SubscriptionDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** |  | 
**code** | **str** |  | 
**display_name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**portfolio_id** | [**ResourceId**](ResourceId.md) |  | 
**timeline_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**timeline_property** | **str** | A portfolio property key (Portfolio/scope/code) naming a perpetual portfolio property whose value  (scope/code) identifies the timeline for each portfolio. Mutually exclusive with timelineId.  The property must be defined, with a data type of value type ResourceId or String. | [optional] 
**portfolio_filter** | **str** | A filter, in the syntax of the list portfolios filter, that narrows a wildcard portfolioId to the portfolios  of the scope that match it. Only valid when portfolioId.code is \&quot;*\&quot;. It may use the portfolio&#39;s own fields and  its perpetual Portfolio properties; time-variant and derived properties and relationships are not supported.  A portfolio that starts or stops matching joins or leaves the subscription. | [optional] 
**address_keys** | **List[str]** | The set of addresses the subscriber wishes to receive. | [optional] 
**by_tax_lots** | **bool** |  | [optional] 
**subscription_type** | **str** | Required. The kind of data the subscription streams: before/after effects per  holding (holdings), the transactions themselves (transactions), or each changed holding&#39;s  complete current state (positions). Address keys and byTaxLots are not valid for a  transactions subscription. Available values: Holdings, Transactions, Positions. | 
**start_effective_at** | **datetime** |  | [optional] 
**end_effective_at** | **datetime** | Deprecated and no longer honoured: a fixed forward date stops being a forward view once  the live edge passes it. Use effectiveForwardDays instead. Still accepted and echoed back  so existing subscriptions keep round-tripping. | [optional] 
**effective_forward_days** | **int** | How far forward the subscription reports, as a number of calendar days past the live  edge — a rolling forward view that advances as time passes. | [optional] 
## Example

```python
from lusid.models.subscription_definition import SubscriptionDefinition
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

scope: StrictStr = "example_scope"
code: StrictStr = "example_code"
display_name: Optional[StrictStr] = "example_display_name"
description: Optional[StrictStr] = "example_description"
portfolio_id: ResourceId = # Replace with your value
timeline_id: Optional[ResourceId] = # Replace with your value
timeline_property: Optional[StrictStr] = "example_timeline_property"
portfolio_filter: Optional[StrictStr] = "example_portfolio_filter"
address_keys: Optional[List[StrictStr]] = # Replace with your value
by_tax_lots: Optional[StrictBool] = # Replace with your value
by_tax_lots:Optional[StrictBool] = None
subscription_type: StrictStr = "example_subscription_type"
start_effective_at: Optional[datetime] = # Replace with your value
end_effective_at: Optional[datetime] = # Replace with your value
effective_forward_days: Optional[StrictInt] = # Replace with your value
effective_forward_days: Optional[StrictInt] = None
subscription_definition_instance = SubscriptionDefinition(scope=scope, code=code, display_name=display_name, description=description, portfolio_id=portfolio_id, timeline_id=timeline_id, timeline_property=timeline_property, portfolio_filter=portfolio_filter, address_keys=address_keys, by_tax_lots=by_tax_lots, subscription_type=subscription_type, start_effective_at=start_effective_at, end_effective_at=end_effective_at, effective_forward_days=effective_forward_days)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

