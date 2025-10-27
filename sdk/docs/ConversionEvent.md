# ConversionEvent

Conversion Event (CONV) - Conversion of securities (generally convertible bonds or preferred shares) into  another form of securities (usually common shares) at a pre-stated price/ratio.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**record_date** | **datetime** | Required.  Date at which positions are struck at the end of the day to  note which parties will receive the relevant amount of  entitlement, due to be distributed on the PaymentDate. | [optional] 
**payment_date** | **datetime** | Required. Date on which the movement is due to take place (cash and/or securities). | [optional] 
**new_instrument** | [**NewInstrument**](NewInstrument.md) |  | 
**response_deadline_date** | **datetime** | Date/time that the account servicer has set as the deadline to respond,  with instructions, to an outstanding event. Not required. | [optional] 
**market_deadline_date** | **datetime** | Date/time which the issuer or issuer&#39;s agent has set as the deadline to respond,  with an instruction, to an outstanding offer or privilege. Not required. | [optional] 
**period_of_action** | [**EventDateRange**](EventDateRange.md) |  | [optional] 
**fractional_units_cash_price** | **float** | The cash price paid in lieu of fractionalUnits. Not required.  If provided, must have FractionalUnitsCashCurrency too. | [optional] 
**fractional_units_cash_currency** | **str** | Optional. Used in calculating cash-in-lieu of fractional shares. Not required.  If provided, must have FractionalUnitsCashPrice too. | [optional] 
**security_offer_elections** | [**List[SecurityOfferElection]**](SecurityOfferElection.md) | List of possible security offers for this conversion event. There must be at most one election of this type.    If the ParticipationType is Mandatory:     This list must have exactly one election that is chosen and default.  CashAndSecurityOfferElections and CashOfferElections &lt;b&gt; must be null or empty&lt;/b&gt;.     If the ParticipationType is Voluntary:     This list can be empty,  so long as CashAndSecurityOfferElections or CashOfferElections  has at least one election. None of these elections have to be chosen or default. | [optional] 
**cash_and_security_offer_elections** | [**List[CashAndSecurityOfferElection]**](CashAndSecurityOfferElection.md) | List of possible cash and security offers for this conversion event. There must be at most one election of this type.    If the ParticipationType is Mandatory:    This list &lt;b&gt; must be null or empty&lt;/b&gt;.    If the ParticipationType is Voluntary:    This list can be empty,  so long as SecurityOfferElections or CashOfferElections  has at least one election. None of these elections have to be chosen or default. | [optional] 
**cash_offer_elections** | [**List[CashOfferElection]**](CashOfferElection.md) | List of possible cash offers for this conversion event. There must be at most one election of this type.    If the ParticipationType is Mandatory:    This list &lt;b&gt; must be null or empty&lt;/b&gt;.    If the ParticipationType is Voluntary:    This list can be empty,  so long as SecurityOfferElections or CashAndSecurityOfferElections  has at least one election. None of these elections have to be chosen or default. | [optional] 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent | 
## Example

```python
from lusid.models.conversion_event import ConversionEvent
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

record_date: Optional[datetime] = # Replace with your value
payment_date: Optional[datetime] = # Replace with your value
new_instrument: NewInstrument = # Replace with your value
response_deadline_date: Optional[datetime] = # Replace with your value
market_deadline_date: Optional[datetime] = # Replace with your value
period_of_action: Optional[EventDateRange] = # Replace with your value
fractional_units_cash_price: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
fractional_units_cash_currency: Optional[StrictStr] = "example_fractional_units_cash_currency"
security_offer_elections: Optional[List[SecurityOfferElection]] = # Replace with your value
cash_and_security_offer_elections: Optional[List[CashAndSecurityOfferElection]] = # Replace with your value
cash_offer_elections: Optional[List[CashOfferElection]] = # Replace with your value
instrument_event_type: StrictStr = "example_instrument_event_type"
conversion_event_instance = ConversionEvent(record_date=record_date, payment_date=payment_date, new_instrument=new_instrument, response_deadline_date=response_deadline_date, market_deadline_date=market_deadline_date, period_of_action=period_of_action, fractional_units_cash_price=fractional_units_cash_price, fractional_units_cash_currency=fractional_units_cash_currency, security_offer_elections=security_offer_elections, cash_and_security_offer_elections=cash_and_security_offer_elections, cash_offer_elections=cash_offer_elections, instrument_event_type=instrument_event_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

