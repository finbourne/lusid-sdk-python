# CallOnIntermediateSecuritiesEvent

CallOnIntermediateSecuritiesEvent event (EXRI), representing an exercise on intermediate securities resulting from an intermediate securities distribution.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiry_date** | **datetime** | The date on which the issue ends. | 
**payment_date** | **datetime** | The payment date of the event. | 
**new_instrument** | [**NewInstrument**](NewInstrument.md) |  | 
**units_ratio** | [**UnitsRatio**](UnitsRatio.md) |  | 
**price** | **float** | The price at which new units are purchased. | 
**exercise_currency** | **str** | The currency of the exercise. | 
**option_exercise_elections** | [**List[OptionExerciseElection]**](OptionExerciseElection.md) | Option exercise election for this event. | [optional] 
**lapse_elections** | [**List[LapseElection]**](LapseElection.md) | Lapse election for this event. | [optional] 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent | 

## Example

```python
from lusid.models.call_on_intermediate_securities_event import CallOnIntermediateSecuritiesEvent

# TODO update the JSON string below
json = "{}"
# create an instance of CallOnIntermediateSecuritiesEvent from a JSON string
call_on_intermediate_securities_event_instance = CallOnIntermediateSecuritiesEvent.from_json(json)
# print the JSON string representation of the object
print CallOnIntermediateSecuritiesEvent.to_json()

# convert the object into a dict
call_on_intermediate_securities_event_dict = call_on_intermediate_securities_event_instance.to_dict()
# create an instance of CallOnIntermediateSecuritiesEvent from a dict
call_on_intermediate_securities_event_form_dict = call_on_intermediate_securities_event.from_dict(call_on_intermediate_securities_event_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


