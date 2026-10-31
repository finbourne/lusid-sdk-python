# InstalmentCallEvent

Instalment Call Event (PPMT) — the issuer calls the next instalment due on a partly-paid equity line.  The holder pays the call price per unit and the holding moves from the partly-paid line to the  line carrying the higher paid-up amount. Under MandatoryWithChoices the holder may instead lapse,  in which case nothing moves and the partly-paid line survives.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_date** | **datetime** | The date on which the call cash and the replacement units settle. | [optional] 
**record_date** | **datetime** | The date on which entitlement is struck. Optional; when absent, entitlement strikes on the payment date. | [optional] 
**response_deadline_date** | **datetime** | The deadline by which the holder must instruct. Required when the participation type is  MandatoryWithChoices; must be null when it is Mandatory. | [optional] 
**market_deadline_date** | **datetime** | The deadline by which the custodian must forward instructions to the market. Required when the  participation type is MandatoryWithChoices; must be null when it is Mandatory. | [optional] 
**new_instrument** | [**NewInstrument**](NewInstrument.md) |  | 
**units_ratio** | [**UnitsRatio**](UnitsRatio.md) |  | 
**call_price_per_unit** | **float** | The amount of money payable per eligible unit on this instalment, in the call currency.  This is money per unit, not a percentage of the issue price: a 40 per cent call on a 2.50 issue  price is supplied as 1.00. | 
**call_currency** | **str** | The currency in which the call settles. Must match the currency of the new instrument. | 
**option_exercise_elections** | [**List[OptionExerciseElection]**](OptionExerciseElection.md) | The election to pay the call and receive the new instrument. Exactly one is required.  Under Mandatory participation it must be both default and chosen. | [optional] 
**lapse_elections** | [**List[LapseElection]**](LapseElection.md) | The election to decline the call, leaving the partly-paid line unchanged. Exactly one is required  under MandatoryWithChoices participation; none may be supplied under Mandatory participation. | [optional] 
**fractional_units_rounding_convention** | **str** | The convention used to round the fractional units entitlement. Defaults to Floor.  Supported values: Floor, Ceiling, RoundHalfUp, RoundHalfDown, BankerRounding. Available values: Floor, Ceiling, RoundHalfUp, RoundHalfDown, RoundToDecimalPlaces, BuyUp, BankerRounding. | [optional] 
**fractional_units_decimal_places** | **int** | The number of decimal places to round to. Not used by any of the supported rounding conventions. | [optional] 
**instrument_event_type** | **str** | The Type of Event. Available values: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent, ConsentEvent, DrawingEvent, CapitalGainsDistributionEvent, ExchangeOfferEvent, DutchAuctionEvent, WorthlessEvent, PutRedemptionEvent, LoanFacilityDelayedCompensationPaymentEvent, InterestPaymentEvent, PriorityIssueEvent, ClassActionEvent, BankruptcyEvent, LiquidationPaymentEvent, PartialDefeasanceEvent, SecurityWriteOffEvent, WarrantsExerciseEvent, PariPassuEvent, ChangeEvent, PikBondCouponEvent, PikBondCashCouponEvent, PikBondInterestCapitalisationEvent, PikBondPrincipalEvent, DelistingEvent, PikBondInterestEvent, CommodityForwardCashSettlementEvent, PaymentInKindEvent, CommodityForwardPhysicalSettlementEvent, CancelSwapEvent, BondOptionTerminationEvent, TerminationEvent, CommodityCalendarSwapCashFlowEvent, DepositSweepEvent, BondForwardCashSettlementEvent, BondForwardTerminationEvent, AmendCommitmentEvent, CapitalCallEvent, FundDistributionEvent, NavReportEvent, DividendSuspensionEvent, LoanInterestCapitalisationEvent, TotalReturnSwapCashFlowEvent, GlobalLoanFacilityReinitialisationEvent, InvestorLoanFacilityReinitialisationEvent, CapitalCallReceiptEvent, RecallableCapitalExpiryEvent, CapitalInterestTransferEvent, FacilityDrawEvent, FacilityRepaymentEvent, FacilityInterestEvent, FacilityCommitmentFeeEvent, InstalmentCallEvent, DepositInterestCapitalisationEvent, PartialRedemptionWithoutReductionOfNominalValueEvent, StripBondCashflowEvent, CapitalisationEvent. | 
## Example

```python
from lusid.models.instalment_call_event import InstalmentCallEvent
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

payment_date: Optional[datetime] = # Replace with your value
record_date: Optional[datetime] = # Replace with your value
response_deadline_date: Optional[datetime] = # Replace with your value
market_deadline_date: Optional[datetime] = # Replace with your value
new_instrument: NewInstrument = # Replace with your value
units_ratio: UnitsRatio = # Replace with your value
call_price_per_unit: Union[StrictFloat, StrictInt] = # Replace with your value
call_currency: StrictStr = "example_call_currency"
option_exercise_elections: Optional[List[OptionExerciseElection]] = # Replace with your value
lapse_elections: Optional[List[LapseElection]] = # Replace with your value
fractional_units_rounding_convention: Optional[StrictStr] = "example_fractional_units_rounding_convention"
fractional_units_decimal_places: Optional[StrictInt] = # Replace with your value
fractional_units_decimal_places: Optional[StrictInt] = None
instrument_event_type: StrictStr = "example_instrument_event_type"
instalment_call_event_instance = InstalmentCallEvent(payment_date=payment_date, record_date=record_date, response_deadline_date=response_deadline_date, market_deadline_date=market_deadline_date, new_instrument=new_instrument, units_ratio=units_ratio, call_price_per_unit=call_price_per_unit, call_currency=call_currency, option_exercise_elections=option_exercise_elections, lapse_elections=lapse_elections, fractional_units_rounding_convention=fractional_units_rounding_convention, fractional_units_decimal_places=fractional_units_decimal_places, instrument_event_type=instrument_event_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

