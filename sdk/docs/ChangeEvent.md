# ChangeEvent

Change event (CHAN) — a reorganisation in which an instrument's certificates, name, or  terms are changed. Holders of record on the record date have their positions converted  automatically to the new instrument at a fixed 1:1 ratio on the payment date.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**record_date** | **datetime** | The record date — the eligibility cutoff. Holders of record on this date enter the  change. | [optional] 
**payment_date** | **datetime** | The payment date — the date the change fires and the paired StockMovement  transactions land. | [optional] 
**new_instrument** | [**NewInstrument**](NewInstrument.md) |  | 
**units_ratio** | [**UnitsRatio**](UnitsRatio.md) |  | 
**change_type** | **str** | The nature of the change — one of \&quot;Certificates\&quot;, \&quot;Name\&quot;, or \&quot;Terms\&quot;. Available values: Certificates, Name, Terms. | 
**term_target** | **str** | The target of a terms change — one of \&quot;InstrumentDefinitionField\&quot; or  \&quot;InstrumentProperty\&quot;. Only applicable when ChangeType is \&quot;Terms\&quot;. Available values: InstrumentDefinitionField, InstrumentProperty. | [optional] 
**term_target_identifier** | **str** | The identifier of the term target being changed. Must be paired with TermTarget. | [optional] 
**additional_information** | **str** | Free-text additional information describing the change. | [optional] 
**instrument_event_type** | **str** | The Type of Event. Available values: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent, ConsentEvent, DrawingEvent, CapitalGainsDistributionEvent, ExchangeOfferEvent, DutchAuctionEvent, WorthlessEvent, PutRedemptionEvent, LoanFacilityDelayedCompensationPaymentEvent, InterestPaymentEvent, PriorityIssueEvent, ClassActionEvent, BankruptcyEvent, LiquidationPaymentEvent, PartialDefeasanceEvent, SecurityWriteOffEvent, WarrantsExerciseEvent, PariPassuEvent, ChangeEvent, PikBondCouponEvent, PikBondCashCouponEvent, PikBondInterestCapitalisationEvent, PikBondPrincipalEvent, DelistingEvent, PikBondInterestEvent, CommodityForwardCashSettlementEvent, PaymentInKindEvent, CommodityForwardPhysicalSettlementEvent, CancelSwapEvent, BondOptionTerminationEvent. | 
## Example

```python
from lusid.models.change_event import ChangeEvent
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

record_date: Optional[datetime] = # Replace with your value
payment_date: Optional[datetime] = # Replace with your value
new_instrument: NewInstrument = # Replace with your value
units_ratio: UnitsRatio = # Replace with your value
change_type: StrictStr = "example_change_type"
term_target: Optional[StrictStr] = "example_term_target"
term_target_identifier: Optional[StrictStr] = "example_term_target_identifier"
additional_information: Optional[StrictStr] = "example_additional_information"
instrument_event_type: StrictStr = "example_instrument_event_type"
change_event_instance = ChangeEvent(record_date=record_date, payment_date=payment_date, new_instrument=new_instrument, units_ratio=units_ratio, change_type=change_type, term_target=term_target, term_target_identifier=term_target_identifier, additional_information=additional_information, instrument_event_type=instrument_event_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

