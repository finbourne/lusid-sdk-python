# ProtectionPayoutCashFlowEvent

Protection payout cashflow for credit default instruments (CDS or CDX).

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ex_date** | **datetime** | The ex-dividend date of the cashflow. | 
**payment_date** | **datetime** | The payment date of the cashflow. | 
**currency** | **str** | The currency in which the cashflow is paid. | 
**cash_flow_per_unit** | **float** | The cashflow amount received for each unit of the instrument held on the ex date. | [optional] 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent | 

## Example

```python
from lusid.models.protection_payout_cash_flow_event import ProtectionPayoutCashFlowEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ProtectionPayoutCashFlowEvent from a JSON string
protection_payout_cash_flow_event_instance = ProtectionPayoutCashFlowEvent.from_json(json)
# print the JSON string representation of the object
print ProtectionPayoutCashFlowEvent.to_json()

# convert the object into a dict
protection_payout_cash_flow_event_dict = protection_payout_cash_flow_event_instance.to_dict()
# create an instance of ProtectionPayoutCashFlowEvent from a dict
protection_payout_cash_flow_event_form_dict = protection_payout_cash_flow_event.from_dict(protection_payout_cash_flow_event_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


