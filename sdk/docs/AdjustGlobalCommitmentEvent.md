# AdjustGlobalCommitmentEvent

Event to adjust the limit/balance of a LoanFacility.  Used to initially set up the facility, but also used to increase/reduce the associated limit and balance.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Amount that the limit and balance are changed by.  A positive number signifies an increase, and a negative number here signifies a decrease. | 
**var_date** | **datetime** | Date of the adjustment.  Signifies when the facility begins to accrue interest. | [optional] 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent | 

## Example

```python
from lusid.models.adjust_global_commitment_event import AdjustGlobalCommitmentEvent

# TODO update the JSON string below
json = "{}"
# create an instance of AdjustGlobalCommitmentEvent from a JSON string
adjust_global_commitment_event_instance = AdjustGlobalCommitmentEvent.from_json(json)
# print the JSON string representation of the object
print AdjustGlobalCommitmentEvent.to_json()

# convert the object into a dict
adjust_global_commitment_event_dict = adjust_global_commitment_event_instance.to_dict()
# create an instance of AdjustGlobalCommitmentEvent from a dict
adjust_global_commitment_event_form_dict = adjust_global_commitment_event.from_dict(adjust_global_commitment_event_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


