# InterestPaymentEvent

Interest Payment event (INTR). A cash distribution of interest from a debt issuer to its noteholders,  carrying a per-unit absolute interest rate on each CashElection. Supports Mandatory  (single declared election) and MandatoryWithChoices (one election per offered currency) participation.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**record_date** | **datetime** | The record-date cut-off determining entitlement. Required. Map from the vendor RecordDate (NOT the  ExDate sentinel). | [optional] 
**payment_date** | **datetime** | The date the interest is paid to noteholders. Required. Also the effective date of the event. | [optional] 
**response_deadline** | **datetime** | The holder-instruction deadline. Required for MandatoryWithChoices; must be null for Mandatory. | [optional] 
**market_deadline** | **datetime** | The market-organisation deadline. Required for MandatoryWithChoices; must be null for Mandatory. | [optional] 
**announcement_date** | **datetime** | The date the event was announced by the issuer. Optional. | [optional] 
**cash_elections** | [**List[CashElection]**](CashElection.md) | The cash elections for this event. For Mandatory participation a single declared election is supplied  with IsDeclared, IsDefault and IsChosen all true; for MandatoryWithChoices one entry per offered  currency is supplied, with exactly one declared, one default and one chosen. Every election carries a  per-unit absolute (signed) DividendRate and an ExchangeRate of 1. | 
**instrument_event_type** | **str** | The Type of Event. Available values: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent, ConsentEvent, DrawingEvent, CapitalGainsDistributionEvent, ExchangeOfferEvent, DutchAuctionEvent, WorthlessEvent, PutRedemptionEvent, LoanFacilityDelayedCompensationPaymentEvent, InterestPaymentEvent. | 
## Example

```python
from lusid.models.interest_payment_event import InterestPaymentEvent
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

record_date: Optional[datetime] = # Replace with your value
payment_date: Optional[datetime] = # Replace with your value
response_deadline: Optional[datetime] = # Replace with your value
market_deadline: Optional[datetime] = # Replace with your value
announcement_date: Optional[datetime] = # Replace with your value
cash_elections: List[CashElection] = # Replace with your value
instrument_event_type: StrictStr = "example_instrument_event_type"
interest_payment_event_instance = InterestPaymentEvent(record_date=record_date, payment_date=payment_date, response_deadline=response_deadline, market_deadline=market_deadline, announcement_date=announcement_date, cash_elections=cash_elections, instrument_event_type=instrument_event_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

