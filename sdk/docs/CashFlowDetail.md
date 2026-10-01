# CashFlowDetail

An individual cashflow inside a cashflow bucket, annotated with the source that produced it  in the cash flow waterfall (SRS > Transaction > Instrument).
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_date** | **datetime** | The date on which the cashflow is paid. | 
**amount** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**source_type** | **str** | The source that produced the cashflow in the cash flow waterfall. One of &#39;Instrument&#39; (produced by the valuation engine), &#39;Transaction&#39; (produced from a booked transaction or movement) or &#39;SRS&#39; (sourced from the structured results store). | 
**instrument_id** | **str** | The LUSID instrument identifier of the instrument that produced the cashflow. | 
**instrument_display_name** | **str** | The display name of the instrument that produced the cashflow. Not present when the instrument cannot be resolved (e.g. deleted, no permission). | [optional] 
**transaction_id** | **str** | The identifier of the transaction from which the cashflow originates, where known. | [optional] 
**portfolio_id** | [**ResourceId**](ResourceId.md) |  | 
**flow_type** | **str** | The type of the cashflow, e.g. Coupon, Principal or Premium. | [optional] 
**movement_name** | **str** | The name of the movement that produced the cashflow (e.g. Coupon, Side1), falling back to the flow type when the movement is unnamed. Not present when the cashflow could not be valued. | [optional] 
**pay_receive** | **str** | Indicates whether the cashflow is paid or received. | [optional] 
**gross_amount** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**haircut_fraction** | **float** | The fraction of the gross amount removed by the haircut, in the range [0, 1]. Zero for outflows and for cashflows no rule matched. Only populated when haircut rules were supplied on the request. | [optional] 
**net_amount** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**haircut_rule_applied** | **str** | The identifier of the haircut rule that was applied to the cashflow, or not present when no rule matched or no haircut rules were supplied on the request. | [optional] 
**error** | **str** | Present when the cashflow could not be valued, for example because of missing market data: the valuation error, matching the CashflowError diagnostic reported by the QueryCashFlows endpoint. In that case the amount is null rather than zero. Error may also be set when only the report-currency FX lookup failed (see ReportCurrencyAmount), in which case the base Amount remains populated and only ReportCurrencyAmount and TradeToReportCurrencyRate are null. | [optional] 
**report_currency_amount** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**trade_to_report_currency_rate** | **float** | The FX rate used to convert the cashflow amount from its own payment currency (see Amount) into the request&#39;s report currency, resolved at the cashflow&#39;s transaction (trade) date, not its payment date. Only present when ReportCurrency was supplied on the request; not present when it was omitted, or when the rate could not be resolved (see Error). | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.cash_flow_detail import CashFlowDetail
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

payment_date: datetime = # Replace with your value
amount: Optional[CurrencyAndAmount] = None
source_type: StrictStr = "example_source_type"
instrument_id: StrictStr = "example_instrument_id"
instrument_display_name: Optional[StrictStr] = "example_instrument_display_name"
transaction_id: Optional[StrictStr] = "example_transaction_id"
portfolio_id: ResourceId = # Replace with your value
flow_type: Optional[StrictStr] = "example_flow_type"
movement_name: Optional[StrictStr] = "example_movement_name"
pay_receive: Optional[StrictStr] = "example_pay_receive"
gross_amount: Optional[CurrencyAndAmount] = # Replace with your value
haircut_fraction: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
net_amount: Optional[CurrencyAndAmount] = # Replace with your value
haircut_rule_applied: Optional[StrictStr] = "example_haircut_rule_applied"
error: Optional[StrictStr] = "example_error"
report_currency_amount: Optional[CurrencyAndAmount] = # Replace with your value
trade_to_report_currency_rate: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
links: Optional[List[Link]] = None
cash_flow_detail_instance = CashFlowDetail(payment_date=payment_date, amount=amount, source_type=source_type, instrument_id=instrument_id, instrument_display_name=instrument_display_name, transaction_id=transaction_id, portfolio_id=portfolio_id, flow_type=flow_type, movement_name=movement_name, pay_receive=pay_receive, gross_amount=gross_amount, haircut_fraction=haircut_fraction, net_amount=net_amount, haircut_rule_applied=haircut_rule_applied, error=error, report_currency_amount=report_currency_amount, trade_to_report_currency_rate=trade_to_report_currency_rate, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

