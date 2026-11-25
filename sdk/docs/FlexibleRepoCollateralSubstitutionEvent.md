# FlexibleRepoCollateralSubstitutionEvent

Event representing the substitution of collateral on a repurchase agreement booked as a FlexibleRepo.  One or more outgoing collateral instruments are returned by the Buyer and replaced by one or more incoming  collateral instruments provided by the Seller, without closing or modifying the repo itself.  The outgoing instruments are held on the repo until the settlement date and the incoming instruments from it,  in the units given on each CollateralIn entry. Optional flags allow deferral of the manufactured and cash  payments to repo maturity, and payment of the repo interest accrued to the entitlement date.  Specific to a FlexibleRepo instrument.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entitlement_date** | **datetime** | Required property.  The date on which the substitution takes effect. Must be on or before the settlement date.  This is a required field, unless otherwise supplied via \&quot;EventDateStamps\&quot; in  the instrument event upsert request. | [optional] 
**settlement_date** | **datetime** | Required property.  The date on which the collateral transfers settle: the outgoing instruments are held on the repo until this  date and the incoming instruments from it. Must be on or after the entitlement date and strictly before the  repo maturity date.  This is a required field, unless otherwise supplied via \&quot;EventDateStamps\&quot; in  the instrument event upsert request. | [optional] 
**collateral_out** | [**List[CollateralSubstitutionConstituent]**](CollateralSubstitutionConstituent.md) | The collateral instruments being removed from the repo. If omitted, every collateral instrument held on the  repo on the settlement date is substituted in full. If provided, must contain at least one entry, each of an  instrument held on the repo from before the settlement date. | [optional] 
**collateral_in** | [**List[CollateralSubstitutionConstituent]**](CollateralSubstitutionConstituent.md) | The collateral instruments being added to the repo. Must contain at least one entry. | 
**amount** | **float** | Not supported: must be omitted. Partial substitution of the outgoing collateral is not available; the amounts  are given on each CollateralOut and CollateralIn entry. | [optional] 
**amount_type** | **str** | Not supported: must be omitted. See Amount.  Supported string (enumeration) values are: [Percentage, Units]. Available values: Percentage, Units. | [optional] 
**adjust_collateral_units** | **bool** | Required property.  Must be false: the incoming collateral units are taken from the Amount on each CollateralIn entry.  Sizing the incoming units so that their market value matches the outgoing collateral (true) is not yet supported. | 
**defer_cash_payment** | **bool** | Only valid if AdjustCollateralUnits is false. If true, the residual cash payment is deferred to repo maturity.  Defaults to false. | [optional] 
**accrue_deferred_cash_payment** | **bool** | Only valid if DeferCashPayment is true. If true, the deferred cash payment accrues interest at the repo rate  until maturity. Defaults to false. | [optional] 
**pay_accrued_repo_interest_at_substitution** | **bool** | If true, the repo interest accrued from the repo start date to the entitlement date is paid on the settlement  date, and repo interest resets and resumes from the entitlement date to maturity. Defaults to false. | [optional] 
**instrument_event_type** | **str** | The Type of Event. Available values: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent, ConsentEvent, DrawingEvent, CapitalGainsDistributionEvent, ExchangeOfferEvent, DutchAuctionEvent, WorthlessEvent, PutRedemptionEvent, LoanFacilityDelayedCompensationPaymentEvent, InterestPaymentEvent, PriorityIssueEvent, ClassActionEvent, BankruptcyEvent, LiquidationPaymentEvent, PartialDefeasanceEvent, SecurityWriteOffEvent, WarrantsExerciseEvent, PariPassuEvent, ChangeEvent, PikBondCouponEvent, PikBondCashCouponEvent, PikBondInterestCapitalisationEvent, PikBondPrincipalEvent, DelistingEvent, PikBondInterestEvent, CommodityForwardCashSettlementEvent, PaymentInKindEvent, CommodityForwardPhysicalSettlementEvent, CancelSwapEvent, BondOptionTerminationEvent, TerminationEvent, CommodityCalendarSwapCashFlowEvent, DepositSweepEvent, BondForwardCashSettlementEvent, BondForwardTerminationEvent, AmendCommitmentEvent, CapitalCallEvent, FundDistributionEvent, NavReportEvent, DividendSuspensionEvent, LoanInterestCapitalisationEvent, TotalReturnSwapCashFlowEvent, GlobalLoanFacilityReinitialisationEvent, InvestorLoanFacilityReinitialisationEvent, CapitalCallReceiptEvent, RecallableCapitalExpiryEvent, CapitalInterestTransferEvent, FacilityDrawEvent, FacilityRepaymentEvent, FacilityInterestEvent, FacilityCommitmentFeeEvent, InstalmentCallEvent, DepositInterestCapitalisationEvent, PartialRedemptionWithoutReductionOfNominalValueEvent, StripBondCashflowEvent, CapitalisationEvent, SharesPremiumDividendEvent, CashDistributionFromNonEligibleSecuritiesSalesEvent, InflationIndexationEvent, InterestPaymentWithPrincipalEvent, IncreaseInValueEvent, FlexibleRepoCollateralSubstitutionEvent. | 
## Example

```python
from lusid.models.flexible_repo_collateral_substitution_event import FlexibleRepoCollateralSubstitutionEvent
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

entitlement_date: Optional[datetime] = # Replace with your value
settlement_date: Optional[datetime] = # Replace with your value
collateral_out: Optional[List[CollateralSubstitutionConstituent]] = # Replace with your value
collateral_in: List[CollateralSubstitutionConstituent] = # Replace with your value
amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
amount_type: Optional[StrictStr] = "example_amount_type"
adjust_collateral_units: StrictBool = # Replace with your value
adjust_collateral_units:StrictBool = True
defer_cash_payment: Optional[StrictBool] = # Replace with your value
defer_cash_payment:Optional[StrictBool] = None
accrue_deferred_cash_payment: Optional[StrictBool] = # Replace with your value
accrue_deferred_cash_payment:Optional[StrictBool] = None
pay_accrued_repo_interest_at_substitution: Optional[StrictBool] = # Replace with your value
pay_accrued_repo_interest_at_substitution:Optional[StrictBool] = None
instrument_event_type: StrictStr = "example_instrument_event_type"
flexible_repo_collateral_substitution_event_instance = FlexibleRepoCollateralSubstitutionEvent(entitlement_date=entitlement_date, settlement_date=settlement_date, collateral_out=collateral_out, collateral_in=collateral_in, amount=amount, amount_type=amount_type, adjust_collateral_units=adjust_collateral_units, defer_cash_payment=defer_cash_payment, accrue_deferred_cash_payment=accrue_deferred_cash_payment, pay_accrued_repo_interest_at_substitution=pay_accrued_repo_interest_at_substitution, instrument_event_type=instrument_event_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

