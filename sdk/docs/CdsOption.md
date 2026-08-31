# CdsOption

LUSID representation of an option on a single-name Credit Default Swap or a CDX/iTraxx index,  discriminated by the MasteredInstrumentType field of the referenced MasteredInstrument, which is derived  from the resolved type of the underlying. Referenced via a MasteredInstrument.  Quote-driven by default: it has no coupon or projected interim cashflow, its only cash movement being  the spot premium.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | The start date of the instrument. This is normally synonymous with the trade-date. | 
**dom_ccy** | **str** | The domestic currency of the instrument. | 
**strike** | **float** | The strike of the option. | 
**business_day_convention** | **str** | Business day convention for the maturity-to-settlement date calculation.  Default value: F.                Supported string (enumeration) values are: [NoAdjustment, Previous, P, Following, F, ModifiedPrevious, MP, ModifiedFollowing, MF, HalfMonthModifiedFollowing, Nearest]. Default value: F. Available values: NoAdjustment, None, Previous, P, Following, F, ModifiedPrevious, MP, ModifiedFollowing, MF, HalfMonthModifiedFollowing, Nearest, Invalid. | [optional] [default to 'F']
**delivery_days** | **int** | Number of business days between the option maturity date and settlement, used to compute  OptionSettlementDate when not explicitly overridden. Defaults to 2 if not set. | [optional] [default to 2]
**delivery_type** | **str** | Is the option cash settled or physical delivery of the underlying.                Supported string (enumeration) values are: [Cash, Physical]. Available values: Cash, Physical. | 
**exercise_type** | **str** | Type of optionality that is present; European only in this scope.  Default value: European.                Supported string (enumeration) values are: [European, Bermudan, American]. Default value: European. Available values: None, European, Bermudan, American. | [optional] [default to 'European']
**notional** | **float** | Fixed per-unit reference multiplier. Aggregate exposure &#x3D; Holding/Units x Notional; not a mutable total. | 
**option_maturity_date** | **datetime** | The last exercise date of the option. | 
**option_settlement_date** | **datetime** | Explicit override of the option&#39;s settlement date. If not supplied, it is computed as a  business-day-adjusted delivery of DeliveryDays after OptionMaturityDate. | [optional] 
**option_type** | **str** | The direction of the credit option: Payer or Receiver.                Supported string (enumeration) values are: [Payer, Receiver]. Available values: Payer, Receiver. | 
**premium** | [**Premium**](Premium.md) |  | [optional] 
**settlement_calendars** | **List[str]** | Holiday calendars for the maturity-to-settlement date calculation. | [optional] 
**underlying** | [**MasteredInstrument**](MasteredInstrument.md) |  | [optional] 
**underlying_version** | **datetime** | The AsAt timestamp of the underlying&#39;s definition at the time this option was written, pinning  lookups of the underlying&#39;s composition and terms independently of subsequent index rolls or re-upserts. | 
**instrument_type** | **str** | Available values: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo, ToBeAnnounced, VolatilitySwap, ToBeAnnouncedOption, CommodityForward, BondOption, CdsOption, CommodityCalendarSwap, BondForward. | 
## Example

```python
from lusid.models.cds_option import CdsOption
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

start_date: datetime = # Replace with your value
dom_ccy: StrictStr = "example_dom_ccy"
strike: Union[StrictFloat, StrictInt] = # Replace with your value
business_day_convention: Optional[StrictStr] = "example_business_day_convention"
delivery_days: Optional[StrictInt] = # Replace with your value
delivery_days: Optional[StrictInt] = None
delivery_type: StrictStr = "example_delivery_type"
exercise_type: Optional[StrictStr] = "example_exercise_type"
notional: Union[StrictFloat, StrictInt] = # Replace with your value
option_maturity_date: datetime = # Replace with your value
option_settlement_date: Optional[datetime] = # Replace with your value
option_type: StrictStr = "example_option_type"
premium: Optional[Premium] = None
settlement_calendars: Optional[List[StrictStr]] = # Replace with your value
underlying: Optional[MasteredInstrument] = None
underlying_version: datetime = # Replace with your value
instrument_type: StrictStr = "example_instrument_type"
cds_option_instance = CdsOption(start_date=start_date, dom_ccy=dom_ccy, strike=strike, business_day_convention=business_day_convention, delivery_days=delivery_days, delivery_type=delivery_type, exercise_type=exercise_type, notional=notional, option_maturity_date=option_maturity_date, option_settlement_date=option_settlement_date, option_type=option_type, premium=premium, settlement_calendars=settlement_calendars, underlying=underlying, underlying_version=underlying_version, instrument_type=instrument_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

