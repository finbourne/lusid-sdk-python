# IncreaseInValueEvent

Increase in Value Event (INCR) — an increase in the face value of a single security, with the number of  securities in circulation unchanged. No cash is paid. The data on the event chooses its shape: with no new  instrument and no units ratio only the par value changes and nothing is booked; with a new instrument at  1 for 1 the holding moves to the new ISIN like for like; with a new instrument and a units ratio above  1 for 1 the holding is split onto the new ISIN.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_date** | **datetime** | The date the new par value applies. Required when only the par value changes; optional otherwise. | [optional] 
**announcement_date** | **datetime** | The date the increase in value was announced. | [optional] 
**previous_par_value** | **float** | The par value per share before the event. Recorded only: it books nothing and writes no property. | [optional] 
**new_par_value** | **float** | The par value per share after the event. Recorded only: it books nothing and writes no property. | [optional] 
**par_value_currency** | **str** | The currency of both par values. | [optional] 
**record_date** | **datetime** | The entitlement date where the holding moves to a new instrument at 1 for 1, when it is required.  Optional where the units ratio is above 1 for 1. Must be null when only the par value changes. | [optional] 
**ex_date** | **datetime** | The entitlement date where the units ratio is above 1 for 1, when it is required. Must be null otherwise. | [optional] 
**payment_date** | **datetime** | The date the holder receives the units. Required with a units ratio; must be null when only the par  value changes. | [optional] 
**new_instrument** | [**NewInstrument**](NewInstrument.md) |  | [optional] 
**units_ratio** | [**UnitsRatio**](UnitsRatio.md) |  | [optional] 
**par_value_property_key** | **str** | The key of the instrument property that holds the par value, for example Instrument/Ops/ParValue. It is  left out of the copy of the old instrument&#39;s properties, so the new instrument keeps its own value.  Required where the holding moves to a new instrument at 1 for 1; must be null otherwise. | [optional] 
**carry_relationships** | **str** | Whether, and in which direction, the old instrument&#39;s relationships are carried onto the new instrument  at 1 for 1: None, Outward or Both. When not supplied, the outward relationships are carried. Must be  null in every other shape. Available values: None, Outward, Both. | [optional] 
**instrument_event_type** | **str** | The Type of Event. Available values: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent, ConsentEvent, DrawingEvent, CapitalGainsDistributionEvent, ExchangeOfferEvent, DutchAuctionEvent, WorthlessEvent, PutRedemptionEvent, LoanFacilityDelayedCompensationPaymentEvent, InterestPaymentEvent, PriorityIssueEvent, ClassActionEvent, BankruptcyEvent, LiquidationPaymentEvent, PartialDefeasanceEvent, SecurityWriteOffEvent, WarrantsExerciseEvent, PariPassuEvent, ChangeEvent, PikBondCouponEvent, PikBondCashCouponEvent, PikBondInterestCapitalisationEvent, PikBondPrincipalEvent, DelistingEvent, PikBondInterestEvent, CommodityForwardCashSettlementEvent, PaymentInKindEvent, CommodityForwardPhysicalSettlementEvent, CancelSwapEvent, BondOptionTerminationEvent, TerminationEvent, CommodityCalendarSwapCashFlowEvent, DepositSweepEvent, BondForwardCashSettlementEvent, BondForwardTerminationEvent, AmendCommitmentEvent, CapitalCallEvent, FundDistributionEvent, NavReportEvent, DividendSuspensionEvent, LoanInterestCapitalisationEvent, TotalReturnSwapCashFlowEvent, GlobalLoanFacilityReinitialisationEvent, InvestorLoanFacilityReinitialisationEvent, CapitalCallReceiptEvent, RecallableCapitalExpiryEvent, CapitalInterestTransferEvent, FacilityDrawEvent, FacilityRepaymentEvent, FacilityInterestEvent, FacilityCommitmentFeeEvent, InstalmentCallEvent, DepositInterestCapitalisationEvent, PartialRedemptionWithoutReductionOfNominalValueEvent, StripBondCashflowEvent, CapitalisationEvent, SharesPremiumDividendEvent, CashDistributionFromNonEligibleSecuritiesSalesEvent, InflationIndexationEvent, InterestPaymentWithPrincipalEvent, IncreaseInValueEvent. | 
## Example

```python
from lusid.models.increase_in_value_event import IncreaseInValueEvent
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

effective_date: Optional[datetime] = # Replace with your value
announcement_date: Optional[datetime] = # Replace with your value
previous_par_value: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
new_par_value: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
par_value_currency: Optional[StrictStr] = "example_par_value_currency"
record_date: Optional[datetime] = # Replace with your value
ex_date: Optional[datetime] = # Replace with your value
payment_date: Optional[datetime] = # Replace with your value
new_instrument: Optional[NewInstrument] = # Replace with your value
units_ratio: Optional[UnitsRatio] = # Replace with your value
par_value_property_key: Optional[StrictStr] = "example_par_value_property_key"
carry_relationships: Optional[StrictStr] = "example_carry_relationships"
instrument_event_type: StrictStr = "example_instrument_event_type"
increase_in_value_event_instance = IncreaseInValueEvent(effective_date=effective_date, announcement_date=announcement_date, previous_par_value=previous_par_value, new_par_value=new_par_value, par_value_currency=par_value_currency, record_date=record_date, ex_date=ex_date, payment_date=payment_date, new_instrument=new_instrument, units_ratio=units_ratio, par_value_property_key=par_value_property_key, carry_relationships=carry_relationships, instrument_event_type=instrument_event_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

