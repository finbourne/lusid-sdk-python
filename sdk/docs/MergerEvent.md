# MergerEvent

Merger Event (MRGR).
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**announcement_date** | **datetime** | The date the merger is announced. | [optional] 
**cash_and_security_offer_elections** | [**List[CashAndSecurityOfferElection]**](CashAndSecurityOfferElection.md) | List of possible CashAndSecurityOfferElections for this merger event | [optional] 
**cash_offer_elections** | [**List[CashOfferElection]**](CashOfferElection.md) | List of possible CashOfferElections for this merger event | [optional] 
**ex_date** | **datetime** | The first date on which the holder of record of the original shares has entitled ownership of the new shares. | [optional] 
**fractional_units_cash_currency** | **str** | Optional. Used in calculating cash-in-lieu of fractional shares. | [optional] 
**fractional_units_cash_price** | **float** | Optional. Used in calculating cash-in-lieu of fractional shares. | [optional] 
**new_instrument** | [**NewInstrument**](NewInstrument.md) |  | 
**payment_date** | **datetime** | Date on which the merger takes place. | [optional] 
**record_date** | **datetime** | Optional. Date you have to be the holder of record of the original shares in order to receive the new shares. | [optional] 
**security_offer_elections** | [**List[SecurityOfferElection]**](SecurityOfferElection.md) | List of possible SecurityOfferElections for this merger event | [optional] 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent | 
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
ex_date: Optional[datetime] = # Replace with your value
fractional_units_cash_currency: Optional[StrictStr] = "example_fractional_units_cash_currency"
fractional_units_cash_price: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
new_instrument: NewInstrument = # Replace with your value
payment_date: Optional[datetime] = # Replace with your value
record_date: Optional[datetime] = # Replace with your value
security_offer_elections: Optional[List[SecurityOfferElection]] = # Replace with your value
instrument_event_type: StrictStr = "example_instrument_event_type"
merger_event_instance = MergerEvent(announcement_date=announcement_date, cash_and_security_offer_elections=cash_and_security_offer_elections, cash_offer_elections=cash_offer_elections, ex_date=ex_date, fractional_units_cash_currency=fractional_units_cash_currency, fractional_units_cash_price=fractional_units_cash_price, new_instrument=new_instrument, payment_date=payment_date, record_date=record_date, security_offer_elections=security_offer_elections, instrument_event_type=instrument_event_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

