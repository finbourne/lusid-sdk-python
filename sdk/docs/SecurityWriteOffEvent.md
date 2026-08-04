# SecurityWriteOffEvent

Security write-off (WOFF) — removes a security holding from the portfolio at zero proceeds following an  issuer-, lender-, or regulator-declared write-off. The full eligible holding is debited on the PaymentDate;  no cash is received and no new security is credited. Supports Mandatory and Voluntary participation; on the  Voluntary path the holder submits a SubscribeElection to recognise (apply) the write-off.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**record_date** | **datetime** | Positions are struck at close of business on this date to determine eligible holdings. | [optional] 
**payment_date** | **datetime** | The date the security debit is processed in LUSID; no cash payment is associated. Must be &gt;&#x3D; RecordDate. | [optional] 
**announcement_date** | **datetime** | The date the issuer, agent or regulator announces the write-off. Optional — null when no separate  announcement date is provided. When populated, must be &lt;&#x3D; RecordDate. | [optional] 
**subscribe_elections** | [**List[SubscribeElection]**](SubscribeElection.md) | List of possible subscribe elections for this event. Populated on the Voluntary path only, where the  holder elects to recognise (apply) the write-off. Ignored on the Mandatory path. | [optional] 
**instrument_event_type** | **str** | The Type of Event. Available values: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent, ConsentEvent, DrawingEvent, CapitalGainsDistributionEvent, ExchangeOfferEvent, DutchAuctionEvent, WorthlessEvent, PutRedemptionEvent, LoanFacilityDelayedCompensationPaymentEvent, InterestPaymentEvent, PriorityIssueEvent, ClassActionEvent, BankruptcyEvent, LiquidationPaymentEvent, PartialDefeasanceEvent, SecurityWriteOffEvent, WarrantsExerciseEvent, PariPassuEvent, ChangeEvent, PikBondCouponEvent, PikBondCashCouponEvent, PikBondInterestCapitalisationEvent, PikBondPrincipalEvent, DelistingEvent. | 
## Example

```python
from lusid.models.security_write_off_event import SecurityWriteOffEvent
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

record_date: Optional[datetime] = # Replace with your value
payment_date: Optional[datetime] = # Replace with your value
announcement_date: Optional[datetime] = # Replace with your value
subscribe_elections: Optional[List[SubscribeElection]] = # Replace with your value
instrument_event_type: StrictStr = "example_instrument_event_type"
security_write_off_event_instance = SecurityWriteOffEvent(record_date=record_date, payment_date=payment_date, announcement_date=announcement_date, subscribe_elections=subscribe_elections, instrument_event_type=instrument_event_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

