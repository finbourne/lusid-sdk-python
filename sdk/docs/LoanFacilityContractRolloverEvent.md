# LoanFacilityContractRolloverEvent

Event for rolling over one or more FlexibleLoan contracts into one or more different FlexibleLoan contracts against the same facility.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** | Effective date of the event. | [optional] 
**rollover_constituents** | [**List[RolloverConstituent]**](RolloverConstituent.md) | Source and target contracts of the rollover. That is, a set of contracts and their respective changes to balance  Expect at least one contract to as the source of the rollover and at least one target contract. | 
**with_interest** | **bool** | If set to true, then active contracts whose balance is reduced by the rollover will have their accrued interest  repaid pro rata to the balance reduction. | 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent | 
## Example

```python
from lusid.models.loan_facility_contract_rollover_event import LoanFacilityContractRolloverEvent
from typing import Any, Dict, List, Optional
from pydantic.v1 import Field, StrictBool, StrictStr, conlist, validator
from datetime import datetime
var_date: Optional[datetime] = # Replace with your value
rollover_constituents: conlist(RolloverConstituent) = # Replace with your value
with_interest: StrictBool = # Replace with your value
with_interest:StrictBool = True
instrument_event_type: StrictStr = "example_instrument_event_type"
loan_facility_contract_rollover_event_instance = LoanFacilityContractRolloverEvent(var_date=var_date, rollover_constituents=rollover_constituents, with_interest=with_interest, instrument_event_type=instrument_event_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

