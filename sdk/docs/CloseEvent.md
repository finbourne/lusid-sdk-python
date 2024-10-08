# CloseEvent

The termination of an instrument.  In some cases termination can happen over a range of dates e.g. american option exercise.  In most cases the startDate == endDate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | The first date on which the instrument could close | [optional] 
**end_date** | **datetime** | The last date on which the instrument could close | [optional] 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent | 

## Example

```python
from lusid.models.close_event import CloseEvent

# TODO update the JSON string below
json = "{}"
# create an instance of CloseEvent from a JSON string
close_event_instance = CloseEvent.from_json(json)
# print the JSON string representation of the object
print CloseEvent.to_json()

# convert the object into a dict
close_event_dict = close_event_instance.to_dict()
# create an instance of CloseEvent from a dict
close_event_form_dict = close_event.from_dict(close_event_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


