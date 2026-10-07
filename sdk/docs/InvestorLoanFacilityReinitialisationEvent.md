# InvestorLoanFacilityReinitialisationEvent

Sets one investor's loan-facility position at tax lot granularity - contract balances, accrued interest and  cost - on lots a trade has already opened, where those are not simply the pro-rata share the trade derived  from the facility's global state. Every figure is an absolute target, not a delta.                Tax lot ids are only unique within a portfolio, and the event lives on a corporate action source that  several portfolios can share, so it names the portfolio it corrects.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract_allocations** | [**List[LoanFacilityTaxLotAllocation]**](LoanFacilityTaxLotAllocation.md) | Investor-level state per contract per tax lot - the balance, and the accrued interest on it where  that is stated rather than derived. Each entry names its own contract, so a tax lot holding a balance  on two contracts appears twice. May be omitted for a fully undrawn lot named in TaxLotStates. | [optional] 
**var_date** | **datetime** | Effective date of the reinitialisation. The tax lots it names must already have been opened, and  settled, by a trade dated no later than this. | [optional] 
**portfolio_scope** | **str** | Scope of the portfolio whose lots the event corrects. | 
**portfolio_code** | **str** | Code of the portfolio whose lots the event corrects. | 
**tax_lot_states** | [**List[LoanFacilityTaxLotState]**](LoanFacilityTaxLotState.md) | Facility-level state per tax lot - cost, and the facility&#39;s own accrual on its undrawn amount. Keyed  on the tax lot alone, so a lot holding balances on several contracts has one entry here and one  ContractAllocation per contract. | [optional] 
**instrument_event_type** | **str** | The Type of Event. Available values: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent, ConsentEvent, DrawingEvent, CapitalGainsDistributionEvent, ExchangeOfferEvent, DutchAuctionEvent, WorthlessEvent, PutRedemptionEvent, LoanFacilityDelayedCompensationPaymentEvent, InterestPaymentEvent, PriorityIssueEvent, ClassActionEvent, BankruptcyEvent, LiquidationPaymentEvent, PartialDefeasanceEvent, SecurityWriteOffEvent, WarrantsExerciseEvent, PariPassuEvent, ChangeEvent, PikBondCouponEvent, PikBondCashCouponEvent, PikBondInterestCapitalisationEvent, PikBondPrincipalEvent, DelistingEvent, PikBondInterestEvent, CommodityForwardCashSettlementEvent, PaymentInKindEvent, CommodityForwardPhysicalSettlementEvent, CancelSwapEvent, BondOptionTerminationEvent, TerminationEvent, CommodityCalendarSwapCashFlowEvent, DepositSweepEvent, BondForwardCashSettlementEvent, BondForwardTerminationEvent, AmendCommitmentEvent, CapitalCallEvent, FundDistributionEvent, NavReportEvent, DividendSuspensionEvent, LoanInterestCapitalisationEvent, TotalReturnSwapCashFlowEvent, GlobalLoanFacilityReinitialisationEvent, InvestorLoanFacilityReinitialisationEvent. | 
## Example

```python
from lusid.models.investor_loan_facility_reinitialisation_event import InvestorLoanFacilityReinitialisationEvent
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

contract_allocations: Optional[List[LoanFacilityTaxLotAllocation]] = # Replace with your value
var_date: Optional[datetime] = # Replace with your value
portfolio_scope: StrictStr = "example_portfolio_scope"
portfolio_code: StrictStr = "example_portfolio_code"
tax_lot_states: Optional[List[LoanFacilityTaxLotState]] = # Replace with your value
instrument_event_type: StrictStr = "example_instrument_event_type"
investor_loan_facility_reinitialisation_event_instance = InvestorLoanFacilityReinitialisationEvent(contract_allocations=contract_allocations, var_date=var_date, portfolio_scope=portfolio_scope, portfolio_code=portfolio_code, tax_lot_states=tax_lot_states, instrument_event_type=instrument_event_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

