# DrawingEvent

Mandatory partial bond redemption (DRAW) where the issuer lottery-selects specific bonds for early redemption.  The affected face amount (AFFB) is the lottery-selected portion of a holding that is redeemed. Because the  lottery selects per holder, AFFB genuinely differs between portfolios holding the same instrument, so it is  supplied per portfolio via an instrument event instruction rather than on the event itself. The event-level  AffectedAmount remains available as an optional fallback applied uniformly to every holding.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_date** | **datetime** | Date the cash actually flows for the drawn portion of the holding. | [optional] 
**effective_date** | **datetime** | Lottery Date (&#x3D; Record Date). Holdings are snapshotted at the close of this date to determine the affected balance. | [optional] 
**affected_amount** | **float** | Affected face amount (AFFB) — the lottery-selected portion of the holding that is redeemed, applied uniformly  to every portfolio holding the instrument. Optional: because the lottery selects per holder, AFFB is normally  supplied per portfolio via an instrument event instruction instead. When supplied it must be strictly positive.  A portfolio with neither an instruction nor an event-level value is treated as unaffected (UNAF). | [optional] 
**price_per_unit** | **float** | Redemption price per unit (OFFR / 100). Clean price convention.  Optional: AFFB is typically known before the issuer publishes OFFR, so a null price is permitted on upsert. | [optional] 
**currency** | **str** | Settlement currency for the redemption. | 
**instrument_event_type** | **str** | The Type of Event. Available values: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent, ConsentEvent, DrawingEvent, CapitalGainsDistributionEvent, ExchangeOfferEvent, DutchAuctionEvent, WorthlessEvent, PutRedemptionEvent, LoanFacilityDelayedCompensationPaymentEvent, InterestPaymentEvent, PriorityIssueEvent, ClassActionEvent, BankruptcyEvent, LiquidationPaymentEvent, PartialDefeasanceEvent, SecurityWriteOffEvent, WarrantsExerciseEvent, PariPassuEvent, ChangeEvent, PikBondCouponEvent, PikBondCashCouponEvent, PikBondInterestCapitalisationEvent, PikBondPrincipalEvent, DelistingEvent, PikBondInterestEvent, CommodityForwardCashSettlementEvent, PaymentInKindEvent, CommodityForwardPhysicalSettlementEvent, CancelSwapEvent, BondOptionTerminationEvent, TerminationEvent, CommodityCalendarSwapCashFlowEvent, DepositSweepEvent, BondForwardCashSettlementEvent, BondForwardTerminationEvent, AmendCommitmentEvent, CapitalCallEvent, FundDistributionEvent, NavReportEvent. | 
## Example

```python
from lusid.models.drawing_event import DrawingEvent
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

payment_date: Optional[datetime] = # Replace with your value
effective_date: Optional[datetime] = # Replace with your value
affected_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
price_per_unit: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
currency: StrictStr = "example_currency"
instrument_event_type: StrictStr = "example_instrument_event_type"
drawing_event_instance = DrawingEvent(payment_date=payment_date, effective_date=effective_date, affected_amount=affected_amount, price_per_unit=price_per_unit, currency=currency, instrument_event_type=instrument_event_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

