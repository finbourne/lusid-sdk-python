# CashFlowDetail

An individual cashflow inside a cashflow bucket, annotated with the source that produced it  in the cash flow waterfall (SRS > Transaction > Instrument).
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_date** | **datetime** | The date on which the cashflow is paid. | 
**amount** | **float** | The signed amount of the cashflow. A positive amount indicates money is received, a negative amount indicates money is paid. The amount is always the gross (pre-haircut) signed amount; when haircut rules are supplied the haircut and net amounts are reported separately. | [optional] 
**currency** | **str** | The payment currency of the cashflow. | 
**source_type** | **str** | The source that produced the cashflow in the cash flow waterfall. One of &#39;Instrument&#39; (produced by the valuation engine), &#39;Transaction&#39; (produced from a booked transaction or movement) or &#39;SRS&#39; (sourced from the structured results store). | 
**instrument_id** | **str** | The LUSID instrument identifier of the instrument that produced the cashflow. | 
**transaction_id** | **str** | The identifier of the transaction from which the cashflow originates, where known. | [optional] 
**portfolio_id** | [**ResourceId**](ResourceId.md) |  | 
**flow_type** | **str** | The type of the cashflow, e.g. Coupon, Principal or Premium. | [optional] 
**pay_receive** | **str** | Indicates whether the cashflow is paid or received. | [optional] 
**gross_amount** | **float** | The signed amount of the cashflow before any haircut was applied. Only populated when haircut rules were supplied on the request. | [optional] 
**haircut_fraction** | **float** | The fraction of the gross amount removed by the haircut, in the range [0, 1]. Zero for outflows and for cashflows no rule matched. Only populated when haircut rules were supplied on the request. | [optional] 
**net_amount** | **float** | The signed amount of the cashflow net of the haircut. Only populated when haircut rules were supplied on the request. | [optional] 
**haircut_rule_applied** | **str** | The identifier of the haircut rule that was applied to the cashflow, or not present when no rule matched or no haircut rules were supplied on the request. | [optional] 
**error** | **str** | Only present when the cashflow could not be valued, for example because of missing market data: the valuation error, matching the CashflowError diagnostic reported by the QueryCashFlows endpoint. When set, the amount is null rather than zero. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.cash_flow_detail import CashFlowDetail
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

payment_date: datetime = # Replace with your value
amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
currency: StrictStr = "example_currency"
source_type: StrictStr = "example_source_type"
instrument_id: StrictStr = "example_instrument_id"
transaction_id: Optional[StrictStr] = "example_transaction_id"
portfolio_id: ResourceId = # Replace with your value
flow_type: Optional[StrictStr] = "example_flow_type"
pay_receive: Optional[StrictStr] = "example_pay_receive"
gross_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
haircut_fraction: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
net_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
haircut_rule_applied: Optional[StrictStr] = "example_haircut_rule_applied"
error: Optional[StrictStr] = "example_error"
links: Optional[List[Link]] = None
cash_flow_detail_instance = CashFlowDetail(payment_date=payment_date, amount=amount, currency=currency, source_type=source_type, instrument_id=instrument_id, transaction_id=transaction_id, portfolio_id=portfolio_id, flow_type=flow_type, pay_receive=pay_receive, gross_amount=gross_amount, haircut_fraction=haircut_fraction, net_amount=net_amount, haircut_rule_applied=haircut_rule_applied, error=error, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

