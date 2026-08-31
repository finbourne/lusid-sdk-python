# ToBeAnnouncedOption

LUSID representation of an OTC option on a ToBeAnnounced (TBA) forward contract.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | The start date of the instrument. This is normally synonymous with the trade-date. | 
**expiry_date** | **datetime** | The date on which the option expires, i.e. the last exercise date of the option. | 
**dom_ccy** | **str** | The domestic currency of the instrument. | 
**option_type** | **str** | Type of optionality for the option.                Supported string (enumeration) values are: [Call, Put]. | 
**strike** | **float** | The strike of the option. | 
**delivery_type** | **str** | Is the option cash settled or physical delivery of the underlying TBA.                Supported string (enumeration) values are: [Cash, Physical]. | 
**underlying** | [**MasteredInstrument**](MasteredInstrument.md) |  | 
**exercise_type** | **str** | Type of optionality that is present; European only in this scope.                Supported string (enumeration) values are: [European]. | 
**premium** | [**Premium**](Premium.md) |  | 
**delivery_days** | **int** | Number of business days between exercise date and settlement of the option payoff or underlying.  Defaults to 0 if not set. | [optional] 
**business_day_convention** | **str** | Business day convention for option exercise date to settlement date calculation.  Default value: F. Available values: NoAdjustment, None, Previous, P, Following, F, ModifiedPrevious, MP, ModifiedFollowing, MF, HalfMonthModifiedFollowing, Nearest, Invalid. | [optional] 
**settlement_calendars** | **List[str]** | Holiday calendar for option exercise date to settlement date calculation. | [optional] 
**time_zone_conventions** | [**TimeZoneConventions**](TimeZoneConventions.md) |  | [optional] 
**trading_conventions** | [**TradingConventions**](TradingConventions.md) |  | [optional] 
**instrument_type** | **str** | Available values: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo, ToBeAnnounced, VolatilitySwap, ToBeAnnouncedOption, CommodityForward, BondOption, CdsOption, CommodityCalendarSwap, BondForward. | 
## Example

```python
from lusid.models.to_be_announced_option import ToBeAnnouncedOption
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

start_date: datetime = # Replace with your value
expiry_date: datetime = # Replace with your value
dom_ccy: StrictStr = "example_dom_ccy"
option_type: StrictStr = "example_option_type"
strike: Union[StrictFloat, StrictInt] = # Replace with your value
delivery_type: StrictStr = "example_delivery_type"
underlying: MasteredInstrument
exercise_type: StrictStr = "example_exercise_type"
premium: Premium
delivery_days: Optional[StrictInt] = # Replace with your value
delivery_days: Optional[StrictInt] = None
business_day_convention: Optional[StrictStr] = "example_business_day_convention"
settlement_calendars: Optional[List[StrictStr]] = # Replace with your value
time_zone_conventions: Optional[TimeZoneConventions] = # Replace with your value
trading_conventions: Optional[TradingConventions] = # Replace with your value
instrument_type: StrictStr = "example_instrument_type"
to_be_announced_option_instance = ToBeAnnouncedOption(start_date=start_date, expiry_date=expiry_date, dom_ccy=dom_ccy, option_type=option_type, strike=strike, delivery_type=delivery_type, underlying=underlying, exercise_type=exercise_type, premium=premium, delivery_days=delivery_days, business_day_convention=business_day_convention, settlement_calendars=settlement_calendars, time_zone_conventions=time_zone_conventions, trading_conventions=trading_conventions, instrument_type=instrument_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

