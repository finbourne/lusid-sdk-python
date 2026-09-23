# PikBondInterestCapitalisationEvent

Definition of a PIK Bond Interest Capitalisation Event  This is an event that describes the capitalised (paid-in-kind) portion of a coupon period on a  Payment-in-Kind ComplexBond, whereby the coupon amount is added to the bond's current face.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ex_date** | **datetime** | The ex date (entitlement date) of the coupon | [optional] 
**payment_date** | **datetime** | The payment date of the coupon | [optional] 
**currency** | **str** | The currency in which the coupon is denominated | 
**coupon_per_unit** | **float** | The capitalised coupon amount per unit of the held bond&#39;s current face. Never rounded. | [optional] 
**face_rounding_convention** | **str** | How the face credited to a holding is rounded once CouponPerUnit has been scaled by the holding&#39;s  current face. Defaults to null, which leaves it unrounded. Carried from the bond&#39;s PikSchedule; the  per-unit coupon itself is never rounded. BuyUp is one of the available values but is rejected for  this event: a capitalisation has no cash leg to fund the next whole unit from. Available values: Floor, Ceiling, RoundHalfUp, RoundHalfDown, RoundToDecimalPlaces, BuyUp, BankerRounding. | [optional] 
**face_rounding_decimal_places** | **int** | The number of decimal places the credited face is rounded to. Required when  FaceRoundingConvention is RoundToDecimalPlaces and not permitted otherwise. | [optional] 
**instrument_event_type** | **str** | The Type of Event. Available values: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent, ConsentEvent, DrawingEvent, CapitalGainsDistributionEvent, ExchangeOfferEvent, DutchAuctionEvent, WorthlessEvent, PutRedemptionEvent, LoanFacilityDelayedCompensationPaymentEvent, InterestPaymentEvent, PriorityIssueEvent, ClassActionEvent, BankruptcyEvent, LiquidationPaymentEvent, PartialDefeasanceEvent, SecurityWriteOffEvent, WarrantsExerciseEvent, PariPassuEvent, ChangeEvent, PikBondCouponEvent, PikBondCashCouponEvent, PikBondInterestCapitalisationEvent, PikBondPrincipalEvent, DelistingEvent, PikBondInterestEvent, CommodityForwardCashSettlementEvent, PaymentInKindEvent, CommodityForwardPhysicalSettlementEvent, CancelSwapEvent, BondOptionTerminationEvent, TerminationEvent, CommodityCalendarSwapCashFlowEvent, DepositSweepEvent, BondForwardCashSettlementEvent, BondForwardTerminationEvent, AmendCommitmentEvent, CapitalCallEvent, FundDistributionEvent, NavReportEvent, DividendSuspensionEvent, LoanInterestCapitalisationEvent, TotalReturnSwapCashFlowEvent. | 
## Example

```python
from lusid.models.pik_bond_interest_capitalisation_event import PikBondInterestCapitalisationEvent
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

ex_date: Optional[datetime] = # Replace with your value
payment_date: Optional[datetime] = # Replace with your value
currency: StrictStr = "example_currency"
coupon_per_unit: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
face_rounding_convention: Optional[StrictStr] = "example_face_rounding_convention"
face_rounding_decimal_places: Optional[StrictInt] = # Replace with your value
face_rounding_decimal_places: Optional[StrictInt] = None
instrument_event_type: StrictStr = "example_instrument_event_type"
pik_bond_interest_capitalisation_event_instance = PikBondInterestCapitalisationEvent(ex_date=ex_date, payment_date=payment_date, currency=currency, coupon_per_unit=coupon_per_unit, face_rounding_convention=face_rounding_convention, face_rounding_decimal_places=face_rounding_decimal_places, instrument_event_type=instrument_event_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

