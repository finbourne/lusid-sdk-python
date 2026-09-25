# ExchangeOfferEvent

Exchange Offer Event (EXOF).
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_date** | **datetime** |  | [optional] 
**settlement_date** | **datetime** |  | [optional] 
**event_source** | **str** |  | 
**new_instrument** | [**NewInstrument**](NewInstrument.md) |  | [optional] 
**cash_offer_elections** | [**List[CashOfferElection]**](CashOfferElection.md) | List of possible CashOfferElections for this exchange offer event (CASH).    - The event requires at least one election of any type.    - If ParticipationType is Mandatory, CashOfferElection is not permitted.    - If ParticipationType is MandatoryWithChoices or Voluntary, at most one CashOfferElection may be supplied.    - Exactly one election on the event must be the default, and at most one may be chosen. | [optional] 
**security_offer_elections** | [**List[SecurityOfferElection]**](SecurityOfferElection.md) | List of possible SecurityOfferElections for this exchange offer event (SECU).    - The event requires at least one election of any type.    - Any number of SecurityOfferElections may be supplied.    - A NewInstrument is required on the event when this list is non-empty.    - Exactly one election on the event must be the default, and at most one may be chosen.    - If ParticipationType is Mandatory, the event must carry exactly one election in total; if MandatoryWithChoices, at least two. | [optional] 
**mixed_lot_constituents_elections** | [**List[MixedLotConstituentsElection]**](MixedLotConstituentsElection.md) | List of possible MixedLotConstituentsElections for this exchange offer event.    - The event requires at least one election of any type.    - Any number of MixedLotConstituentsElections may be supplied, up to a limit of 100 entries.    - Exactly one election on the event must be the default, and at most one may be chosen.    - If ParticipationType is Mandatory, the event must carry exactly one election in total; if MandatoryWithChoices, at least two. | [optional] 
**lapse_elections** | [**List[LapseElection]**](LapseElection.md) | List of possible LapseElections for this exchange offer event (NOAC).    - The event requires at least one election of any type.    - If ParticipationType is Mandatory, LapseElection is not permitted.    - If ParticipationType is MandatoryWithChoices, any number of LapseElections may be supplied, but none of them may be the default.    - If ParticipationType is Voluntary, at most one LapseElection may be supplied. | [optional] 
**cash_and_security_offer_elections** | [**List[CashAndSecurityOfferElection]**](CashAndSecurityOfferElection.md) | List of possible CashAndSecurityOfferElections for this exchange offer event (CASE).    - The event requires at least one election of any type.    - Any number of CashAndSecurityOfferElections may be supplied.    - Exactly one election on the event must be the default, and at most one may be chosen.    - If ParticipationType is Mandatory, the event must carry exactly one election in total; if MandatoryWithChoices, at least two. | [optional] 
**consent_and_exchange_elections** | [**List[ConsentAndExchangeElection]**](ConsentAndExchangeElection.md) | List of possible ConsentAndExchangeElections for this exchange offer event (CEXC).    - The event requires at least one election of any type.    - Any number of ConsentAndExchangeElections may be supplied.    - Exactly one election on the event must be the default, and at most one may be chosen.    - If ParticipationType is Mandatory, the event must carry exactly one election in total; if MandatoryWithChoices, at least two. | [optional] 
**abstain_elections** | [**List[AbstainElection]**](AbstainElection.md) | List of possible AbstainElections for this exchange offer event (ABST).    - The event requires at least one election of any type.    - Any number of AbstainElections may be supplied.    - Exactly one election on the event must be the default, and at most one may be chosen.    - If ParticipationType is Mandatory, the event must carry exactly one election in total; if MandatoryWithChoices, at least two. | [optional] 
**unknown_proceeds_elections** | [**List[UnknownProceedsElection]**](UnknownProceedsElection.md) | List of possible UnknownProceedsElections for this exchange offer event (UNKNOWN).    - The event requires at least one election of any type.    - Any number of UnknownProceedsElections may be supplied.    - Exactly one election on the event must be the default, and at most one may be chosen.    - If ParticipationType is Mandatory, the event must carry exactly one election in total; if MandatoryWithChoices, at least two. | [optional] 
**min_piece_size** | **float** |  | [optional] 
**min_increment** | **float** |  | [optional] 
**fractional_units_cash_price** | **float** |  | [optional] 
**fractional_units_cash_currency** | **str** |  | [optional] 
**fractional_units_rounding_convention** | **str** | The convention used to round the fractional units entitlement. Defaults to Floor. Available values: Floor, Ceiling, RoundHalfUp, RoundHalfDown, RoundToDecimalPlaces, BuyUp, BankerRounding. | [optional] 
**fractional_units_decimal_places** | **int** | The number of decimal places to round to when FractionalUnitsRoundingConvention is RoundToDecimalPlaces. | [optional] 
**instruction_reference** | **str** |  | [optional] 
**instrument_event_type** | **str** | The Type of Event. Available values: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent, ConsentEvent, DrawingEvent, CapitalGainsDistributionEvent, ExchangeOfferEvent, DutchAuctionEvent, WorthlessEvent, PutRedemptionEvent, LoanFacilityDelayedCompensationPaymentEvent, InterestPaymentEvent, PriorityIssueEvent, ClassActionEvent, BankruptcyEvent, LiquidationPaymentEvent, PartialDefeasanceEvent, SecurityWriteOffEvent, WarrantsExerciseEvent, PariPassuEvent, ChangeEvent, PikBondCouponEvent, PikBondCashCouponEvent, PikBondInterestCapitalisationEvent, PikBondPrincipalEvent, DelistingEvent, PikBondInterestEvent, CommodityForwardCashSettlementEvent, PaymentInKindEvent, CommodityForwardPhysicalSettlementEvent, CancelSwapEvent, BondOptionTerminationEvent, TerminationEvent, CommodityCalendarSwapCashFlowEvent, DepositSweepEvent, BondForwardCashSettlementEvent, BondForwardTerminationEvent, AmendCommitmentEvent, CapitalCallEvent, FundDistributionEvent, NavReportEvent, DividendSuspensionEvent, LoanInterestCapitalisationEvent, TotalReturnSwapCashFlowEvent. | 
## Example

```python
from lusid.models.exchange_offer_event import ExchangeOfferEvent
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

effective_date: Optional[datetime] = # Replace with your value
settlement_date: Optional[datetime] = # Replace with your value
event_source: StrictStr = "example_event_source"
new_instrument: Optional[NewInstrument] = # Replace with your value
cash_offer_elections: Optional[List[CashOfferElection]] = # Replace with your value
security_offer_elections: Optional[List[SecurityOfferElection]] = # Replace with your value
mixed_lot_constituents_elections: Optional[List[MixedLotConstituentsElection]] = # Replace with your value
lapse_elections: Optional[List[LapseElection]] = # Replace with your value
cash_and_security_offer_elections: Optional[List[CashAndSecurityOfferElection]] = # Replace with your value
consent_and_exchange_elections: Optional[List[ConsentAndExchangeElection]] = # Replace with your value
abstain_elections: Optional[List[AbstainElection]] = # Replace with your value
unknown_proceeds_elections: Optional[List[UnknownProceedsElection]] = # Replace with your value
min_piece_size: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
min_increment: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
fractional_units_cash_price: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
fractional_units_cash_currency: Optional[StrictStr] = "example_fractional_units_cash_currency"
fractional_units_rounding_convention: Optional[StrictStr] = "example_fractional_units_rounding_convention"
fractional_units_decimal_places: Optional[StrictInt] = # Replace with your value
fractional_units_decimal_places: Optional[StrictInt] = None
instruction_reference: Optional[StrictStr] = "example_instruction_reference"
instrument_event_type: StrictStr = "example_instrument_event_type"
exchange_offer_event_instance = ExchangeOfferEvent(effective_date=effective_date, settlement_date=settlement_date, event_source=event_source, new_instrument=new_instrument, cash_offer_elections=cash_offer_elections, security_offer_elections=security_offer_elections, mixed_lot_constituents_elections=mixed_lot_constituents_elections, lapse_elections=lapse_elections, cash_and_security_offer_elections=cash_and_security_offer_elections, consent_and_exchange_elections=consent_and_exchange_elections, abstain_elections=abstain_elections, unknown_proceeds_elections=unknown_proceeds_elections, min_piece_size=min_piece_size, min_increment=min_increment, fractional_units_cash_price=fractional_units_cash_price, fractional_units_cash_currency=fractional_units_cash_currency, fractional_units_rounding_convention=fractional_units_rounding_convention, fractional_units_decimal_places=fractional_units_decimal_places, instruction_reference=instruction_reference, instrument_event_type=instrument_event_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

