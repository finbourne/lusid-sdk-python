# FutureExpiryEvent

Definition of a Future Expiry Event.  This is an event that describes the expiry of a Future instrument.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiry_date** | **datetime** | Expiry date of the Future instrument. | 
**settlement_currency** | **str** | Settlement currency of the Future instrument. | 
**notional_amount_per_unit** | **float** | The notional amount of each unit in the Future instrument. | [optional] 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent | 

## Example

```python
from lusid.models.future_expiry_event import FutureExpiryEvent

# TODO update the JSON string below
json = "{}"
# create an instance of FutureExpiryEvent from a JSON string
future_expiry_event_instance = FutureExpiryEvent.from_json(json)
# print the JSON string representation of the object
print FutureExpiryEvent.to_json()

# convert the object into a dict
future_expiry_event_dict = future_expiry_event_instance.to_dict()
# create an instance of FutureExpiryEvent from a dict
future_expiry_event_form_dict = future_expiry_event.from_dict(future_expiry_event_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


