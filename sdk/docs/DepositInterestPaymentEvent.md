# DepositInterestPaymentEvent

Event to signify the repayment of interest accrued against a deposit holding.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_date** | **datetime** | Date that the interest is due to be paid. | 
**ex_date** | **datetime** | Date that the accrued interest is calculated up until. | 
**currency** | **str** | Currency of the repayment. | 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent | 

## Example

```python
from lusid.models.deposit_interest_payment_event import DepositInterestPaymentEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DepositInterestPaymentEvent from a JSON string
deposit_interest_payment_event_instance = DepositInterestPaymentEvent.from_json(json)
# print the JSON string representation of the object
print DepositInterestPaymentEvent.to_json()

# convert the object into a dict
deposit_interest_payment_event_dict = deposit_interest_payment_event_instance.to_dict()
# create an instance of DepositInterestPaymentEvent from a dict
deposit_interest_payment_event_form_dict = deposit_interest_payment_event.from_dict(deposit_interest_payment_event_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


