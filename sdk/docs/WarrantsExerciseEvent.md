# WarrantsExerciseEvent

Warrants Exercise (EXWA) — the holder's election to exercise an outstanding warrant, paying the  strike and receiving the underlying security, or to let it lapse at zero proceeds. Elective  (Voluntary / MandatoryWithChoices) on EquityOption (EquityOptionType = Warrant) and SimpleInstrument.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_date** | **datetime** | The DvP settlement date on which the strike is paid and the underlying is delivered.  Must be on or after PeriodOfActionEnd. | [optional] 
**period_of_action_start** | **datetime** | Start of the exercise window. | [optional] 
**period_of_action_end** | **datetime** | End of the exercise window. | [optional] 
**response_deadline_date** | **datetime** | Holder response deadline. Required when participation is MandatoryWithChoices. | [optional] 
**market_deadline_date** | **datetime** | Market deadline. Required when participation is MandatoryWithChoices. | [optional] 
**early_response_deadline** | **datetime** | Early response deadline. Optional; populated by some vendor wires. | [optional] 
**strike_per_unit** | **float** | Cash payable per warrant on exercise. Null-allowed on upsert if the warrant instrument resolves  a non-null EquityOption.Strike (instrument-level fallback applied later). If supplied, must be  strictly positive and accompanied by a StrikeCurrency. | [optional] 
**strike_currency** | **str** | Currency of the strike (ISO 4217 3-letter code). Required if StrikePerUnit is non-null. | [optional] 
**units_ratio** | [**UnitsRatio**](UnitsRatio.md) |  | [optional] 
**new_instrument** | [**NewInstrument**](NewInstrument.md) |  | [optional] 
**fraction_disposition** | **str** | Handling of fractional underlying units. Defaults to round-down (RDDN) in the holdings engine when null.                Supported string (enumeration) values are: [RDDN, CINL]. Available values: RDDN, CINL. | [optional] 
**option_exercise_elections** | [**List[OptionExerciseElection]**](OptionExerciseElection.md) | Option exercise elections for this event. At least one entry. | [optional] 
**lapse_elections** | [**List[LapseElection]**](LapseElection.md) | Lapse elections for this event. Required when participation is MandatoryWithChoices or when the  issuer publishes a no-action default. | [optional] 
**instrument_event_type** | **str** | The Type of Event. Available values: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent, ConsentEvent, DrawingEvent, CapitalGainsDistributionEvent, ExchangeOfferEvent, DutchAuctionEvent, WorthlessEvent, PutRedemptionEvent, LoanFacilityDelayedCompensationPaymentEvent, InterestPaymentEvent, PriorityIssueEvent, ClassActionEvent, BankruptcyEvent, LiquidationPaymentEvent, PartialDefeasanceEvent, SecurityWriteOffEvent, WarrantsExerciseEvent, PariPassuEvent, ChangeEvent, PikBondCouponEvent, PikBondCashCouponEvent, PikBondInterestCapitalisationEvent, PikBondPrincipalEvent, DelistingEvent, PikBondInterestEvent, CommodityForwardCashSettlementEvent, PaymentInKindEvent, CommodityForwardPhysicalSettlementEvent, CancelSwapEvent, BondOptionTerminationEvent, TerminationEvent, CommodityCalendarSwapCashFlowEvent, DepositSweepEvent, BondForwardCashSettlementEvent, BondForwardTerminationEvent, AmendCommitmentEvent, CapitalCallEvent, FundDistributionEvent, NavReportEvent. | 
## Example

```python
from lusid.models.warrants_exercise_event import WarrantsExerciseEvent
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

payment_date: Optional[datetime] = # Replace with your value
period_of_action_start: Optional[datetime] = # Replace with your value
period_of_action_end: Optional[datetime] = # Replace with your value
response_deadline_date: Optional[datetime] = # Replace with your value
market_deadline_date: Optional[datetime] = # Replace with your value
early_response_deadline: Optional[datetime] = # Replace with your value
strike_per_unit: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
strike_currency: Optional[StrictStr] = "example_strike_currency"
units_ratio: Optional[UnitsRatio] = # Replace with your value
new_instrument: Optional[NewInstrument] = # Replace with your value
fraction_disposition: Optional[StrictStr] = "example_fraction_disposition"
option_exercise_elections: Optional[List[OptionExerciseElection]] = # Replace with your value
lapse_elections: Optional[List[LapseElection]] = # Replace with your value
instrument_event_type: StrictStr = "example_instrument_event_type"
warrants_exercise_event_instance = WarrantsExerciseEvent(payment_date=payment_date, period_of_action_start=period_of_action_start, period_of_action_end=period_of_action_end, response_deadline_date=response_deadline_date, market_deadline_date=market_deadline_date, early_response_deadline=early_response_deadline, strike_per_unit=strike_per_unit, strike_currency=strike_currency, units_ratio=units_ratio, new_instrument=new_instrument, fraction_disposition=fraction_disposition, option_exercise_elections=option_exercise_elections, lapse_elections=lapse_elections, instrument_event_type=instrument_event_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

