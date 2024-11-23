# SwapPrincipalEvent

Definition of a Swap Principal Event.  This is an event that describes the occurence of a cashflow due to the principal payment.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ex_date** | **datetime** | The entitlement date of the principal payment. | 
**payment_date** | **datetime** | The payment date of the principal. | 
**currency** | **str** | The currency in which the principal is paid. | 
**principal_per_unit** | **float** | The principal amount received for each unit of the instrument held on the ex date. | [optional] 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent | 

## Example

```python
from lusid.models.swap_principal_event import SwapPrincipalEvent

# TODO update the JSON string below
json = "{}"
# create an instance of SwapPrincipalEvent from a JSON string
swap_principal_event_instance = SwapPrincipalEvent.from_json(json)
# print the JSON string representation of the object
print SwapPrincipalEvent.to_json()

# convert the object into a dict
swap_principal_event_dict = swap_principal_event_instance.to_dict()
# create an instance of SwapPrincipalEvent from a dict
swap_principal_event_form_dict = swap_principal_event.from_dict(swap_principal_event_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


