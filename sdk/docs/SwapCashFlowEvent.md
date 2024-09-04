# SwapCashFlowEvent

Definition of a swap cash flow event.  This event describes the cashflow generated from either an interest rate swap or inflation swap instrument.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ex_date** | **datetime** | The ex-dividend date of the cashflow. | 
**payment_date** | **datetime** | The payment date of the cashflow. | 
**currency** | **str** | The currency in which the cashflow is paid. | 
**cash_flow_per_unit** | **float** | The cashflow amount received for each unit of the instrument held on the ex date. | [optional] 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent | 

## Example

```python
from lusid.models.swap_cash_flow_event import SwapCashFlowEvent

# TODO update the JSON string below
json = "{}"
# create an instance of SwapCashFlowEvent from a JSON string
swap_cash_flow_event_instance = SwapCashFlowEvent.from_json(json)
# print the JSON string representation of the object
print SwapCashFlowEvent.to_json()

# convert the object into a dict
swap_cash_flow_event_dict = swap_cash_flow_event_instance.to_dict()
# create an instance of SwapCashFlowEvent from a dict
swap_cash_flow_event_form_dict = swap_cash_flow_event.from_dict(swap_cash_flow_event_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


