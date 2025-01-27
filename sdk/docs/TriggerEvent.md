# TriggerEvent

Definition of a trigger event.  This is an event that occurs on transformation of an option instrument being  triggered by a barrier/touch price level being hit by the underlying asset.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | **float** | The underlying price level that triggers the event | 
**trigger_type** | **str** | The type of the trigger; valid options are Knock-In, Knock-Out, Touch or No-Touch | 
**trigger_direction** | **str** | The direction of the trigger; valid options are Up and Down | 
**trigger_date** | **datetime** | The date the trigger happens at. | 
**maturity_date** | **datetime** | The date the trigger takes effect. | 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent | 

## Example

```python
from lusid.models.trigger_event import TriggerEvent

# TODO update the JSON string below
json = "{}"
# create an instance of TriggerEvent from a JSON string
trigger_event_instance = TriggerEvent.from_json(json)
# print the JSON string representation of the object
print TriggerEvent.to_json()

# convert the object into a dict
trigger_event_dict = trigger_event_instance.to_dict()
# create an instance of TriggerEvent from a dict
trigger_event_form_dict = trigger_event.from_dict(trigger_event_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


