# BondForwardTerminationEvent

Termination of a BondForward because its underlying bond  was redeemed early: the deliverable ceases to exist, so the forward terminates against the proceeds  the underlying was actually redeemed for.  The event is posted against the forward's own LusidInstrumentId by the feed or orchestration layer.  The corporate-action dependency graph is self-keyed by LUID and a MasteredInstrument reference links  price, not events, so the underlying's own EarlyRedemptionEvent does not propagate here and neither  the redemption price nor either accrued figure can be derived on the forward.  Unlike cash settlement, both accrued figures appear and neither cancels: the redemption accrues to the  redemption date and the forward's obligation accrued to its own settlement date, so the two differ.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agreed_clean_price** | **float** | The agreed price, percent of par, carried from the definition; rejected where it differs from the  instrument&#39;s own value. | 
**contract_size** | **float** | Face amount per unit, carried from the definition; rejected where it differs from the instrument&#39;s  own value. | 
**redemption_accrued** | **float** | Accrued paid on the underlying&#39;s redemption, percent of par, at full precision. Required, not  resolved: the forward cannot read the underlying&#39;s accrual. Nullable so that absence is detectable,  zero staying a legitimate supplied value (a bond trading flat); null is rejected. | [optional] 
**redemption_price** | **float** | The price the underlying was redeemed at, percent of par. Must be supplied: it comes from the  underlying&#39;s own redemption. Nullable so that absence is detectable; null is rejected, and zero is  legal (a write-off or liquidation may recover nothing). | [optional] 
**settlement_accrued** | **float** | Accrued the buyer would have paid at the forward&#39;s own maturity date - the invoice date it escaped,  not this event&#39;s settlement date. Nullable so that absence is detectable; null is rejected. | [optional] 
**settlement_amount_per_unit** | **float** | The net termination amount per unit. A supplied value wins; null is computed as  ((redemptionPrice + redemptionAccrued) - (agreedCleanPrice + settlementAccrued)) / 100 x contractSize,  which is undiscounted - where the confirmation nets on a discounted basis, supply the agreed figure.  Negative is valid and means the holder pays; it must not be floored. | [optional] 
**settlement_currency** | **str** | Currency the net amount settles in. | 
**settlement_date** | **datetime** | The date the net termination amount settles. | [optional] 
**termination_date** | **datetime** | The date the termination takes effect, being the effective date of the underlying&#39;s redemption.  Required, not defaulted: the forward cannot read the underlying&#39;s redemption. | [optional] 
**instrument_event_type** | **str** | The Type of Event. Available values: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent, ConsentEvent, DrawingEvent, CapitalGainsDistributionEvent, ExchangeOfferEvent, DutchAuctionEvent, WorthlessEvent, PutRedemptionEvent, LoanFacilityDelayedCompensationPaymentEvent, InterestPaymentEvent, PriorityIssueEvent, ClassActionEvent, BankruptcyEvent, LiquidationPaymentEvent, PartialDefeasanceEvent, SecurityWriteOffEvent, WarrantsExerciseEvent, PariPassuEvent, ChangeEvent, PikBondCouponEvent, PikBondCashCouponEvent, PikBondInterestCapitalisationEvent, PikBondPrincipalEvent, DelistingEvent, PikBondInterestEvent, CommodityForwardCashSettlementEvent, PaymentInKindEvent, CommodityForwardPhysicalSettlementEvent, CancelSwapEvent, BondOptionTerminationEvent, TerminationEvent, CommodityCalendarSwapCashFlowEvent, DepositSweepEvent, BondForwardCashSettlementEvent, BondForwardTerminationEvent, AmendCommitmentEvent, CapitalCallEvent, FundDistributionEvent, NavReportEvent. | 
## Example

```python
from lusid.models.bond_forward_termination_event import BondForwardTerminationEvent
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

agreed_clean_price: Union[StrictFloat, StrictInt] = # Replace with your value
contract_size: Union[StrictFloat, StrictInt] = # Replace with your value
redemption_accrued: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
redemption_price: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
settlement_accrued: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
settlement_amount_per_unit: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
settlement_currency: StrictStr = "example_settlement_currency"
settlement_date: Optional[datetime] = # Replace with your value
termination_date: Optional[datetime] = # Replace with your value
instrument_event_type: StrictStr = "example_instrument_event_type"
bond_forward_termination_event_instance = BondForwardTerminationEvent(agreed_clean_price=agreed_clean_price, contract_size=contract_size, redemption_accrued=redemption_accrued, redemption_price=redemption_price, settlement_accrued=settlement_accrued, settlement_amount_per_unit=settlement_amount_per_unit, settlement_currency=settlement_currency, settlement_date=settlement_date, termination_date=termination_date, instrument_event_type=instrument_event_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

