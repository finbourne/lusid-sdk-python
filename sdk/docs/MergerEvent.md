# MergerEvent

Merger Event (MRGR).
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**announcement_date** | **datetime** | The date the merger is announced. | [optional] 
**cash_and_security_offer_elections** | [**List[CashAndSecurityOfferElection]**](CashAndSecurityOfferElection.md) | List of possible CashAndSecurityOfferElections for this merger event | [optional] 
**cash_offer_elections** | [**List[CashOfferElection]**](CashOfferElection.md) | List of possible CashOfferElections for this merger event | [optional] 
**mixed_lot_constituents_elections** | [**List[MixedLotConstituentsElection]**](MixedLotConstituentsElection.md) | List of possible mixed lot offers for this merger event, if any. Each election replaces the parent position  with one or more distinct new securities and/or cash legs of its own, taking the place of the single  event-level NewInstrument that the other security-bearing elections resolve to.    A merger may carry more than one of these, describing mutually exclusive multi-destination options. | [optional] 
**ex_date** | **datetime** | The first date on which the holder of record of the original shares has entitled ownership of the new shares. | [optional] 
**fractional_units_cash_currency** | **str** | Optional. Used in calculating cash-in-lieu of fractional shares. | [optional] 
**fractional_units_cash_price** | **float** | Optional. Used in calculating cash-in-lieu of fractional shares. | [optional] 
**fractional_units_rounding_convention** | **str** | The convention used to round the fractional units entitlement. Defaults to Floor. Available values: Floor, Ceiling, RoundHalfUp, RoundHalfDown, RoundToDecimalPlaces, BuyUp, BankerRounding. | [optional] 
**fractional_units_decimal_places** | **int** | The number of decimal places to round to when FractionalUnitsRoundingConvention is RoundToDecimalPlaces. | [optional] 
**new_instrument** | [**NewInstrument**](NewInstrument.md) |  | [optional] 
**payment_date** | **datetime** | Date on which the merger takes place. | [optional] 
**record_date** | **datetime** | Optional. Date you have to be the holder of record of the original shares in order to receive the new shares. | [optional] 
**security_offer_elections** | [**List[SecurityOfferElection]**](SecurityOfferElection.md) | List of possible SecurityOfferElections for this merger event | [optional] 
**instrument_event_type** | **str** | The Type of Event. Available values: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent, ConsentEvent, DrawingEvent, CapitalGainsDistributionEvent, ExchangeOfferEvent, DutchAuctionEvent, WorthlessEvent, PutRedemptionEvent, LoanFacilityDelayedCompensationPaymentEvent, InterestPaymentEvent, PriorityIssueEvent, ClassActionEvent, BankruptcyEvent, LiquidationPaymentEvent, PartialDefeasanceEvent, SecurityWriteOffEvent, WarrantsExerciseEvent, PariPassuEvent, ChangeEvent, PikBondCouponEvent, PikBondCashCouponEvent, PikBondInterestCapitalisationEvent, PikBondPrincipalEvent, DelistingEvent, PikBondInterestEvent, CommodityForwardCashSettlementEvent, PaymentInKindEvent, CommodityForwardPhysicalSettlementEvent, CancelSwapEvent, BondOptionTerminationEvent, TerminationEvent, CommodityCalendarSwapCashFlowEvent, DepositSweepEvent. | 
## Example

```python
from lusid.models.merger_event import MergerEvent
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

announcement_date: Optional[datetime] = # Replace with your value
cash_and_security_offer_elections: Optional[List[CashAndSecurityOfferElection]] = # Replace with your value
cash_offer_elections: Optional[List[CashOfferElection]] = # Replace with your value
mixed_lot_constituents_elections: Optional[List[MixedLotConstituentsElection]] = # Replace with your value
ex_date: Optional[datetime] = # Replace with your value
fractional_units_cash_currency: Optional[StrictStr] = "example_fractional_units_cash_currency"
fractional_units_cash_price: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
fractional_units_rounding_convention: Optional[StrictStr] = "example_fractional_units_rounding_convention"
fractional_units_decimal_places: Optional[StrictInt] = # Replace with your value
fractional_units_decimal_places: Optional[StrictInt] = None
new_instrument: Optional[NewInstrument] = # Replace with your value
payment_date: Optional[datetime] = # Replace with your value
record_date: Optional[datetime] = # Replace with your value
security_offer_elections: Optional[List[SecurityOfferElection]] = # Replace with your value
instrument_event_type: StrictStr = "example_instrument_event_type"
merger_event_instance = MergerEvent(announcement_date=announcement_date, cash_and_security_offer_elections=cash_and_security_offer_elections, cash_offer_elections=cash_offer_elections, mixed_lot_constituents_elections=mixed_lot_constituents_elections, ex_date=ex_date, fractional_units_cash_currency=fractional_units_cash_currency, fractional_units_cash_price=fractional_units_cash_price, fractional_units_rounding_convention=fractional_units_rounding_convention, fractional_units_decimal_places=fractional_units_decimal_places, new_instrument=new_instrument, payment_date=payment_date, record_date=record_date, security_offer_elections=security_offer_elections, instrument_event_type=instrument_event_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

