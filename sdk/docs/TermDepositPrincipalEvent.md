# TermDepositPrincipalEvent

Definition of a Term Deposit Interest Event.  This is an event that describes the occurence of principal on a term deposit ().

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | Currency of the principal payment. | 
**payment_date** | **datetime** | Payment date of the principal payment. | 
**principal_per_unit** | **float** | The principal payment made per unit of the held . | [optional] 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent | 

## Example

```python
from lusid.models.term_deposit_principal_event import TermDepositPrincipalEvent

# TODO update the JSON string below
json = "{}"
# create an instance of TermDepositPrincipalEvent from a JSON string
term_deposit_principal_event_instance = TermDepositPrincipalEvent.from_json(json)
# print the JSON string representation of the object
print TermDepositPrincipalEvent.to_json()

# convert the object into a dict
term_deposit_principal_event_dict = term_deposit_principal_event_instance.to_dict()
# create an instance of TermDepositPrincipalEvent from a dict
term_deposit_principal_event_form_dict = term_deposit_principal_event.from_dict(term_deposit_principal_event_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


