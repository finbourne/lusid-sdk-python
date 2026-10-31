# CapitalisationEvent

Capitalisation (CAPI, AMI-SeCo SCoRE section 4.10): an increase in the current principal of a debt instrument  without an increase in its nominal value, normally from incorporating due but unpaid interest into the  principal. A notified CAPI on a ComplexBond, recording the factor before (previousFactor) and after  (nextFactor) the event. Mandatory and purely informational: it generates no cash flow, movements or  transactions. The capitalisation itself is booked by the bond's PikSchedule.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_date** | **datetime** | The date the next factor applies (:98A::EFFD). Required. | [optional] 
**payment_date** | **datetime** | The payment date (:98A::PAYD). Optional and informational; it may fall before effectiveDate. | [optional] 
**record_date** | **datetime** | The record date (:98A::RDTE). Optional and informational; when supplied it must not fall after  effectiveDate. | [optional] 
**previous_factor** | **float** | The factor, current principal per unit of nominal, in force before the event (:92A::PRFC). Optional, but  supplied together with nextFactor or not at all; greater than 0 when supplied. An event without the  factors is stored as economically incomplete. | [optional] 
**next_factor** | **float** | The factor, current principal per unit of nominal, in force from effectiveDate (:92A::NWFC). Optional, but  supplied together with previousFactor or not at all; not less than previousFactor when supplied. | [optional] 
**interest_rate** | **float** | The annual interest rate capitalised, as a fraction, so 6 per cent is 0.06 (:92A::INTP). Optional and  informational; not negative when supplied. | [optional] 
**currency** | **str** | The currency of the capitalised principal (:11A::DENO). Optional and informational. | [optional] 
**instrument_event_type** | **str** | The Type of Event. Available values: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent, ConsentEvent, DrawingEvent, CapitalGainsDistributionEvent, ExchangeOfferEvent, DutchAuctionEvent, WorthlessEvent, PutRedemptionEvent, LoanFacilityDelayedCompensationPaymentEvent, InterestPaymentEvent, PriorityIssueEvent, ClassActionEvent, BankruptcyEvent, LiquidationPaymentEvent, PartialDefeasanceEvent, SecurityWriteOffEvent, WarrantsExerciseEvent, PariPassuEvent, ChangeEvent, PikBondCouponEvent, PikBondCashCouponEvent, PikBondInterestCapitalisationEvent, PikBondPrincipalEvent, DelistingEvent, PikBondInterestEvent, CommodityForwardCashSettlementEvent, PaymentInKindEvent, CommodityForwardPhysicalSettlementEvent, CancelSwapEvent, BondOptionTerminationEvent, TerminationEvent, CommodityCalendarSwapCashFlowEvent, DepositSweepEvent, BondForwardCashSettlementEvent, BondForwardTerminationEvent, AmendCommitmentEvent, CapitalCallEvent, FundDistributionEvent, NavReportEvent, DividendSuspensionEvent, LoanInterestCapitalisationEvent, TotalReturnSwapCashFlowEvent, GlobalLoanFacilityReinitialisationEvent, InvestorLoanFacilityReinitialisationEvent, CapitalCallReceiptEvent, RecallableCapitalExpiryEvent, CapitalInterestTransferEvent, FacilityDrawEvent, FacilityRepaymentEvent, FacilityInterestEvent, FacilityCommitmentFeeEvent, InstalmentCallEvent, DepositInterestCapitalisationEvent, PartialRedemptionWithoutReductionOfNominalValueEvent, StripBondCashflowEvent, CapitalisationEvent. | 
## Example

```python
from lusid.models.capitalisation_event import CapitalisationEvent
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

effective_date: Optional[datetime] = # Replace with your value
payment_date: Optional[datetime] = # Replace with your value
record_date: Optional[datetime] = # Replace with your value
previous_factor: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
next_factor: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
interest_rate: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
currency: Optional[StrictStr] = "example_currency"
instrument_event_type: StrictStr = "example_instrument_event_type"
capitalisation_event_instance = CapitalisationEvent(effective_date=effective_date, payment_date=payment_date, record_date=record_date, previous_factor=previous_factor, next_factor=next_factor, interest_rate=interest_rate, currency=currency, instrument_event_type=instrument_event_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

