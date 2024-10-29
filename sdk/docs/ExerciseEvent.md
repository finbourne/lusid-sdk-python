# ExerciseEvent

Definition of an exercise event.  This is an event that occurs on transformation of an instrument owing to exercise. e.g. an option of  some type into its underlying.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument** | [**LusidInstrument**](LusidInstrument.md) |  | 
**anchor_date** | **datetime** | The date the exercise window starts, or point it takes effect on. | 
**event_window_end** | **datetime** | The date the exercise window ends, or point it takes effect on. | [optional] [readonly] 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent | 

## Example

```python
from lusid.models.exercise_event import ExerciseEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ExerciseEvent from a JSON string
exercise_event_instance = ExerciseEvent.from_json(json)
# print the JSON string representation of the object
print ExerciseEvent.to_json()

# convert the object into a dict
exercise_event_dict = exercise_event_instance.to_dict()
# create an instance of ExerciseEvent from a dict
exercise_event_form_dict = exercise_event.from_dict(exercise_event_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


