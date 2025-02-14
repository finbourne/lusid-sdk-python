# MbsPrincipalWriteOffEvent

Definition of an MBS Principal Write Off Event  This is an event that describes the occurence of a cashflow due to a mortgage-backed security principal write off.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ex_date** | **datetime** | The ex date (entitlement date) of the principal payment, usually several weeks prior to the payment date | 
**payment_date** | **datetime** | The payment date of the principal that is written off | 
**currency** | **str** | The currency in which the principal write off is notated | 
**principal_per_unit** | **float** | The principal amount to be written off for each unit of the instrument held on the ex date | [optional] 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent | 

## Example

```python
from lusid.models.mbs_principal_write_off_event import MbsPrincipalWriteOffEvent

# TODO update the JSON string below
json = "{}"
# create an instance of MbsPrincipalWriteOffEvent from a JSON string
mbs_principal_write_off_event_instance = MbsPrincipalWriteOffEvent.from_json(json)
# print the JSON string representation of the object
print MbsPrincipalWriteOffEvent.to_json()

# convert the object into a dict
mbs_principal_write_off_event_dict = mbs_principal_write_off_event_instance.to_dict()
# create an instance of MbsPrincipalWriteOffEvent from a dict
mbs_principal_write_off_event_form_dict = mbs_principal_write_off_event.from_dict(mbs_principal_write_off_event_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


