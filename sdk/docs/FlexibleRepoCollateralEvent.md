# FlexibleRepoCollateralEvent

Definition of FlexibleRepoCollateralEvent which represents a single collateral transfer as part of a repo contract  modelled as a FlexibleRepo, either as part of the purchase leg or repurchase leg, or any early closure.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settlement_date** | **datetime** | Date at which the transfer of units settles. This is a required field. | [optional] 
**entitlement_date** | **datetime** | Date at which the recipient of the collateral is entitled to the units being transferred. This is a required field. | [optional] 
**amount** | **float** | The total amount of collateral being transferred as part of the repo contract.  Signed to indicate direction of transfer. This is a required field. | 
**collateral_instrument** | [**NewInstrument**](NewInstrument.md) |  | 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent | 
## Example

```python
from lusid.models.flexible_repo_collateral_event import FlexibleRepoCollateralEvent
from typing import Any, Dict, Optional, Union
from pydantic.v1 import Field, StrictFloat, StrictInt, StrictStr, validator
from datetime import datetime
settlement_date: Optional[datetime] = # Replace with your value
entitlement_date: Optional[datetime] = # Replace with your value
amount: Union[StrictFloat, StrictInt] = # Replace with your value
collateral_instrument: NewInstrument = # Replace with your value
instrument_event_type: StrictStr = "example_instrument_event_type"
flexible_repo_collateral_event_instance = FlexibleRepoCollateralEvent(settlement_date=settlement_date, entitlement_date=entitlement_date, amount=amount, collateral_instrument=collateral_instrument, instrument_event_type=instrument_event_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

