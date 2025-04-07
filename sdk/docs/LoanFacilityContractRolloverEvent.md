# LoanFacilityContractRolloverEvent

Event for rolling over one or more FlexibleLoan contracts into one or more different FlexibleLoan contracts against the same facility.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** | Effective date of the event. | [optional] 
**rollover_constituents** | [**List[RolloverConstituent]**](RolloverConstituent.md) | Source and target contracts of the rollover. That is, a set of contracts and their respective changes to balance  Expect at least one contract to as the source of the rollover and at least one target contract. | 
**with_interest** | **bool** | If set to true, then active contracts whose balance is reduced by the rollover will have their accrued interest  repaid pro rata to the balance reduction. | 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent | 

## Example

```python
from lusid.models.loan_facility_contract_rollover_event import LoanFacilityContractRolloverEvent

# TODO update the JSON string below
json = "{}"
# create an instance of LoanFacilityContractRolloverEvent from a JSON string
loan_facility_contract_rollover_event_instance = LoanFacilityContractRolloverEvent.from_json(json)
# print the JSON string representation of the object
print LoanFacilityContractRolloverEvent.to_json()

# convert the object into a dict
loan_facility_contract_rollover_event_dict = loan_facility_contract_rollover_event_instance.to_dict()
# create an instance of LoanFacilityContractRolloverEvent from a dict
loan_facility_contract_rollover_event_form_dict = loan_facility_contract_rollover_event.from_dict(loan_facility_contract_rollover_event_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


