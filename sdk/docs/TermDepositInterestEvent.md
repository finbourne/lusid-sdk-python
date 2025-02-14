# TermDepositInterestEvent

Definition of a Term Deposit Interest Event.  This is an event that describes the occurence of interest on a term deposit ().

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | Currency of the interest payment. | 
**interest_per_unit** | **float** | The interest payment made per unit of the held . | [optional] 
**payment_date** | **datetime** | Payment date of the interest payment. | 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent | 

## Example

```python
from lusid.models.term_deposit_interest_event import TermDepositInterestEvent

# TODO update the JSON string below
json = "{}"
# create an instance of TermDepositInterestEvent from a JSON string
term_deposit_interest_event_instance = TermDepositInterestEvent.from_json(json)
# print the JSON string representation of the object
print TermDepositInterestEvent.to_json()

# convert the object into a dict
term_deposit_interest_event_dict = term_deposit_interest_event_instance.to_dict()
# create an instance of TermDepositInterestEvent from a dict
term_deposit_interest_event_form_dict = term_deposit_interest_event.from_dict(term_deposit_interest_event_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


