# PikBondInterestEvent

Definition of a PIK Bond Interest Event  This is an event that describes the paid-in-kind portion of a coupon period on a  Payment-in-Kind ComplexBond that is settled by delivering units of another instrument, rather  than in cash or by capitalising the amount into the bond's current face. The interest amount is  converted to units of the deliverable at the delivery price and added to the deliverable's  holding as a new tax lot; the paying bond's own units and current face are unchanged.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ex_date** | **datetime** | The ex date (entitlement date) of the interest | [optional] 
**payment_date** | **datetime** | The date on which the securities are delivered | [optional] 
**currency** | **str** | The currency in which the interest amount is expressed | 
**coupon_per_unit** | **float** | The interest amount, in cash terms, per unit of the held bond&#39;s current face | [optional] 
**new_instrument** | [**NewInstrument**](NewInstrument.md) |  | 
**delivery_price** | **float** | The clean price the deliverable is delivered at, as a percentage of its nominal per unit  following bond market convention: 100 is par and 98.5 is a one-and-a-half point discount.  This is not a cash amount per unit. Null is par. It governs how many units the interest  amount buys, not how much face each of those units carries. | [optional] 
**delivered_contract_size** | **float** | The deliverable&#39;s nominal per unit - its contract size. Null is 1. | [optional] 
**delivered_current_face_per_unit** | **float** | The current face each delivered unit carries. Null falls back to DeliveredContractSize;  supply it for a seasoned note whose face has already amortised away from its contract size.  When both are absent the delivered lot carries no current face, which is how a deliverable  that is not current-face-based, such as an equity, is expressed. | [optional] 
**delivered_accrued_per_unit** | **float** | Interest accrued on the deliverable per delivered unit, settled alongside the clean price  when a seasoned note is delivered mid-period. Null is a fresh issue with nothing accrued. | [optional] 
**fractional_units_rounding_convention** | **str** | The convention used to round the units entitlement. Defaults to Floor.                Supported string (enumeration) values are: [Floor, Ceiling, RoundHalfUp, RoundHalfDown, RoundToDecimalPlaces, BankerRounding]. Available values: Floor, Ceiling, RoundHalfUp, RoundHalfDown, RoundToDecimalPlaces, BuyUp, BankerRounding. | [optional] 
**fractional_units_decimal_places** | **int** | The number of decimal places to round to when FractionalUnitsRoundingConvention is RoundToDecimalPlaces. | [optional] 
**fractional_units_cash_price** | **float** | The cash price paid in lieu of the units that could not be delivered. Supplying it, together  with FractionalUnitsCashCurrency, is what settles the undelivered fraction in cash; leave  both absent and the fraction is simply not paid. | [optional] 
**fractional_units_cash_currency** | **str** | The currency of the cash paid in lieu of the undelivered fraction. | [optional] 
**instrument_event_type** | **str** | The Type of Event. Available values: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent, ConsentEvent, DrawingEvent, CapitalGainsDistributionEvent, ExchangeOfferEvent, DutchAuctionEvent, WorthlessEvent, PutRedemptionEvent, LoanFacilityDelayedCompensationPaymentEvent, InterestPaymentEvent, PriorityIssueEvent, ClassActionEvent, BankruptcyEvent, LiquidationPaymentEvent, PartialDefeasanceEvent, SecurityWriteOffEvent, WarrantsExerciseEvent, PariPassuEvent, ChangeEvent, PikBondCouponEvent, PikBondCashCouponEvent, PikBondInterestCapitalisationEvent, PikBondPrincipalEvent, DelistingEvent, PikBondInterestEvent, CommodityForwardCashSettlementEvent, PaymentInKindEvent, CommodityForwardPhysicalSettlementEvent, CancelSwapEvent, BondOptionTerminationEvent. | 
## Example

```python
from lusid.models.pik_bond_interest_event import PikBondInterestEvent
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

ex_date: Optional[datetime] = # Replace with your value
payment_date: Optional[datetime] = # Replace with your value
currency: StrictStr = "example_currency"
coupon_per_unit: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
new_instrument: NewInstrument = # Replace with your value
delivery_price: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
delivered_contract_size: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
delivered_current_face_per_unit: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
delivered_accrued_per_unit: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
fractional_units_rounding_convention: Optional[StrictStr] = "example_fractional_units_rounding_convention"
fractional_units_decimal_places: Optional[StrictInt] = # Replace with your value
fractional_units_decimal_places: Optional[StrictInt] = None
fractional_units_cash_price: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
fractional_units_cash_currency: Optional[StrictStr] = "example_fractional_units_cash_currency"
instrument_event_type: StrictStr = "example_instrument_event_type"
pik_bond_interest_event_instance = PikBondInterestEvent(ex_date=ex_date, payment_date=payment_date, currency=currency, coupon_per_unit=coupon_per_unit, new_instrument=new_instrument, delivery_price=delivery_price, delivered_contract_size=delivered_contract_size, delivered_current_face_per_unit=delivered_current_face_per_unit, delivered_accrued_per_unit=delivered_accrued_per_unit, fractional_units_rounding_convention=fractional_units_rounding_convention, fractional_units_decimal_places=fractional_units_decimal_places, fractional_units_cash_price=fractional_units_cash_price, fractional_units_cash_currency=fractional_units_cash_currency, instrument_event_type=instrument_event_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

