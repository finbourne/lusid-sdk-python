# ExchangeOfferEvent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_date** | **datetime** |  | [optional] 
**settlement_date** | **datetime** |  | [optional] 
**event_source** | **str** |  | 
**new_instrument** | [**NewInstrument**](NewInstrument.md) |  | [optional] 
**cash_offer_elections** | [**List[CashOfferElection]**](CashOfferElection.md) |  | [optional] 
**security_offer_elections** | [**List[SecurityOfferElection]**](SecurityOfferElection.md) |  | [optional] 
**mixed_lot_constituents_elections** | [**List[MixedLotConstituentsElection]**](MixedLotConstituentsElection.md) |  | [optional] 
**lapse_elections** | [**List[LapseElection]**](LapseElection.md) |  | [optional] 
**min_piece_size** | **float** |  | [optional] 
**min_increment** | **float** |  | [optional] 
**fractional_units_cash_price** | **float** |  | [optional] 
**fractional_units_cash_currency** | **str** |  | [optional] 
**instruction_reference** | **str** |  | [optional] 
**instrument_event_type** | **str** | The Type of Event. Available values: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent, ConsentEvent, DrawingEvent, CapitalGainsDistributionEvent, ExchangeOfferEvent, DutchAuctionEvent, WorthlessEvent, PutRedemptionEvent, LoanFacilityDelayedCompensationPaymentEvent, InterestPaymentEvent, PriorityIssueEvent. | 
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
min_piece_size: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
min_increment: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
fractional_units_cash_price: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
fractional_units_cash_currency: Optional[StrictStr] = "example_fractional_units_cash_currency"
instruction_reference: Optional[StrictStr] = "example_instruction_reference"
instrument_event_type: StrictStr = "example_instrument_event_type"
exchange_offer_event_instance = ExchangeOfferEvent(effective_date=effective_date, settlement_date=settlement_date, event_source=event_source, new_instrument=new_instrument, cash_offer_elections=cash_offer_elections, security_offer_elections=security_offer_elections, mixed_lot_constituents_elections=mixed_lot_constituents_elections, lapse_elections=lapse_elections, min_piece_size=min_piece_size, min_increment=min_increment, fractional_units_cash_price=fractional_units_cash_price, fractional_units_cash_currency=fractional_units_cash_currency, instruction_reference=instruction_reference, instrument_event_type=instrument_event_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

