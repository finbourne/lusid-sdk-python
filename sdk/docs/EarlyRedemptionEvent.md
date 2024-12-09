# EarlyRedemptionEvent

Early redemption as a consequence of a bond being called or putted.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_date** | **datetime** | Date of redemption.  For internally generated European callables, this is set to the exercise date.  For internally generated American callables, this is set to the start of the exercise period. | [optional] 
**currency** | **str** | Currency of the redemption. | 
**early_redemption_elections** | [**List[EarlyRedemptionElection]**](EarlyRedemptionElection.md) | EarlyRedemptionElection for the redemption.  Used to trigger the redemption. | 
**redemption_percentage** | **float** | Percentage of the original issue that is redeemed, where 0.5 implies 50%.  Defaults to 1 if not set.  Must be between 0 and 1. | [optional] 
**price_per_unit** | **float** | The price, or strike, that each unit is redeemed at. | [optional] 
**accrued_interest_per_unit** | **float** | Unpaid accrued interest also repaid as part of the redemption, per unit.  Optional field.  If left empty, will be resolved internally by calculating the accrued owed on the EffectiveDate.  This process may require additional market data. | [optional] 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent | 

## Example

```python
from lusid.models.early_redemption_event import EarlyRedemptionEvent

# TODO update the JSON string below
json = "{}"
# create an instance of EarlyRedemptionEvent from a JSON string
early_redemption_event_instance = EarlyRedemptionEvent.from_json(json)
# print the JSON string representation of the object
print EarlyRedemptionEvent.to_json()

# convert the object into a dict
early_redemption_event_dict = early_redemption_event_instance.to_dict()
# create an instance of EarlyRedemptionEvent from a dict
early_redemption_event_form_dict = early_redemption_event.from_dict(early_redemption_event_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


