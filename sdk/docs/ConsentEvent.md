# ConsentEvent

A consent solicitation (CONS) or a bondholder meeting's fee (BMET): voluntary when holders respond to it, mandatory when it pays a fee to every eligible holder without an instruction.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consent_type** | **str** | The type of consent solicitation. Optional; omitting it records Unknown.                Supported string (enumeration) values are: [ChangeInTerms, DueAndPayable, Unknown]. Available values: ChangeInTerms, DueAndPayable, Unknown. | [optional] 
**record_date** | **datetime** | The entitlement determination date. | [optional] 
**response_deadline** | **datetime** | The last date to submit instructions. | [optional] 
**market_deadline** | **datetime** | The issuer-set outer deadline. Must be greater than or equal to ResponseDeadline. | [optional] 
**early_response_deadline** | **datetime** | Deadline for instructions that qualify for an early fee. Optional. When set, must be earlier than ResponseDeadline. Must be null on a Mandatory event. | [optional] 
**payment_date** | **datetime** | Date on which the fee is paid. Required when a CashOfferElection or a fee-bearing ConsentGrantedElection is offered; otherwise must be null. | [optional] 
**cash_offer_elections** | [**List[CashOfferElection]**](CashOfferElection.md) | Options that pay a cash fee to the holder who chooses them, whatever the vote: for example a fee for voting against, for a split vote or for an ineligible-holder confirmation. Keys are free-form and unique across all election lists. The price is quoted per 1,000 of face for bonds (the current notional at the record date: amortised face for a ComplexBond, inflation-adjusted face for an InflationLinkedBond) and per unit for equities and simple instruments. On a Mandatory event, exactly one, both default and chosen. | [optional] 
**lapse_elections** | [**List[LapseElection]**](LapseElection.md) | List of possible lapse elections for this event (NOAC). | [optional] 
**consent_granted_elections** | [**List[ConsentGrantedElection]**](ConsentGrantedElection.md) | List of possible consent-granted elections for this event (CONY), each optionally carrying a consent fee. | [optional] 
**consent_denied_elections** | [**List[ConsentDeniedElection]**](ConsentDeniedElection.md) | List of possible consent-denied elections for this event (CONN). | [optional] 
**abstain_elections** | [**List[AbstainElection]**](AbstainElection.md) | List of possible abstain elections for this event (ABST). | [optional] 
**instrument_event_type** | **str** | The Type of Event. Available values: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent, ConsentEvent, DrawingEvent, CapitalGainsDistributionEvent, ExchangeOfferEvent, DutchAuctionEvent, WorthlessEvent, PutRedemptionEvent, LoanFacilityDelayedCompensationPaymentEvent, InterestPaymentEvent, PriorityIssueEvent, ClassActionEvent, BankruptcyEvent, LiquidationPaymentEvent, PartialDefeasanceEvent, SecurityWriteOffEvent, WarrantsExerciseEvent, PariPassuEvent, ChangeEvent, PikBondCouponEvent, PikBondCashCouponEvent, PikBondInterestCapitalisationEvent, PikBondPrincipalEvent, DelistingEvent, PikBondInterestEvent, CommodityForwardCashSettlementEvent, PaymentInKindEvent, CommodityForwardPhysicalSettlementEvent, CancelSwapEvent, BondOptionTerminationEvent, TerminationEvent, CommodityCalendarSwapCashFlowEvent, DepositSweepEvent, BondForwardCashSettlementEvent, BondForwardTerminationEvent, AmendCommitmentEvent, CapitalCallEvent, FundDistributionEvent, NavReportEvent, DividendSuspensionEvent, LoanInterestCapitalisationEvent, TotalReturnSwapCashFlowEvent, GlobalLoanFacilityReinitialisationEvent, InvestorLoanFacilityReinitialisationEvent. | 
## Example

```python
from lusid.models.consent_event import ConsentEvent
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

consent_type: Optional[StrictStr] = "example_consent_type"
record_date: Optional[datetime] = # Replace with your value
response_deadline: Optional[datetime] = # Replace with your value
market_deadline: Optional[datetime] = # Replace with your value
early_response_deadline: Optional[datetime] = # Replace with your value
payment_date: Optional[datetime] = # Replace with your value
cash_offer_elections: Optional[List[CashOfferElection]] = # Replace with your value
lapse_elections: Optional[List[LapseElection]] = # Replace with your value
consent_granted_elections: Optional[List[ConsentGrantedElection]] = # Replace with your value
consent_denied_elections: Optional[List[ConsentDeniedElection]] = # Replace with your value
abstain_elections: Optional[List[AbstainElection]] = # Replace with your value
instrument_event_type: StrictStr = "example_instrument_event_type"
consent_event_instance = ConsentEvent(consent_type=consent_type, record_date=record_date, response_deadline=response_deadline, market_deadline=market_deadline, early_response_deadline=early_response_deadline, payment_date=payment_date, cash_offer_elections=cash_offer_elections, lapse_elections=lapse_elections, consent_granted_elections=consent_granted_elections, consent_denied_elections=consent_denied_elections, abstain_elections=abstain_elections, instrument_event_type=instrument_event_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

