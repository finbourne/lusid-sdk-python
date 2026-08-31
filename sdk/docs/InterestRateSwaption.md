# InterestRateSwaption

LUSID representation of an Interest Rate Swaption.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | The start date of the instrument. This is normally synonymous with the trade-date. | 
**pay_or_receive_fixed** | **str** | Pay or Receive the fixed leg of the underlying swap.    Supported string (enumeration) values are: [Pay, Receive]. | 
**premium** | [**Premium**](Premium.md) |  | [optional] 
**delivery_method** | **str** | How does the option settle    Supported string (enumeration) values are: [Cash, Physical]. | 
**swap** | [**InterestRateSwap**](InterestRateSwap.md) |  | [optional] 
**time_zone_conventions** | [**TimeZoneConventions**](TimeZoneConventions.md) |  | [optional] 
**underlying** | [**LusidInstrument**](LusidInstrument.md) |  | [optional] 
**delivery_days** | **int** | Number of business days between exercise date and settlement of the option payoff or underlying.                Defaults to 0. | [optional] 
**business_day_convention** | **str** | Business day convention for option exercise date to settlement date calculation.  Default value: F. Available values: NoAdjustment, None, Previous, P, Following, F, ModifiedPrevious, MP, ModifiedFollowing, MF, HalfMonthModifiedFollowing, Nearest, Invalid. | [optional] 
**settlement_calendars** | **List[str]** | Holiday calendars for option exercise date to settlement date calculation. | [optional] 
**dom_ccy** | **str** | The currency the option settles in.                Optional, and in almost all cases it should be left to default. If not specified, the currency of  the underlying swap is used, which for a cross-currency swap is the currency of its first leg.                A specified currency is taken as given and is not validated against the underlying swap, since  settling in another currency is rare but legitimate. Note that valuation of such a swaption is not  supported, as converting from the currency the swap is valued in needs an fx rate the instrument  does not define. | [optional] 
**exercise_date** | **datetime** | The date the option expires, and for European exercise the date it is exercised. For American  exercise it is the end of the window the option may be exercised in, so it should be set on the  instrument for the option to be exercisable up to the intended date.                If not specified, the start date of the underlying swap is used. | [optional] 
**exercise_type** | **str** | Type of optionality that is present; European, American.                Supported string (enumeration) values are: [European, American].  Defaults to \&quot;European\&quot; if not set.                A European option is exercised on its exercise date, so its exercise event is generated with  that date already set. An American option may be exercised at any point up to that date, so the  date it is actually exercised on is supplied on the exercise event; set exerciseDate on the  instrument to open the window the event may fall in.                The swap delivered on exercise keeps the start date it was defined with, so exercising early  or late leaves it aged or forward-starting relative to the exercise. Keeping that swap  correct for the intended exercise is the responsibility of whoever defines it. In particular,  for an American physically settled swaption on a cross-currency underlying, neither the swap&#39;s  start date nor its fx notionals are determined at trade time, so amending the delivered swap  position after exercise is an operational step the client must carry out. | [optional] 
**strike** | **float** | The rate the option strikes against.                May only be specified when the underlying swap has no single fixed leg, as otherwise that leg&#39;s  fixed rate is the strike. It must be specified when the underlying swap has two fixed legs, as  there is then no single rate to strike against. | [optional] 
**trading_conventions** | [**TradingConventions**](TradingConventions.md) |  | [optional] 
**instrument_type** | **str** | Available values: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo, ToBeAnnounced, VolatilitySwap, ToBeAnnouncedOption, CommodityForward, BondOption, CdsOption, CommodityCalendarSwap, BondForward. | 
## Example

```python
from lusid.models.interest_rate_swaption import InterestRateSwaption
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

start_date: datetime = # Replace with your value
pay_or_receive_fixed: StrictStr = "example_pay_or_receive_fixed"
premium: Optional[Premium] = None
delivery_method: StrictStr = "example_delivery_method"
swap: Optional[InterestRateSwap] = None
time_zone_conventions: Optional[TimeZoneConventions] = # Replace with your value
underlying: Optional[LusidInstrument] = None
delivery_days: Optional[StrictInt] = # Replace with your value
delivery_days: Optional[StrictInt] = None
business_day_convention: Optional[StrictStr] = "example_business_day_convention"
settlement_calendars: Optional[List[StrictStr]] = # Replace with your value
dom_ccy: Optional[StrictStr] = "example_dom_ccy"
exercise_date: Optional[datetime] = # Replace with your value
exercise_type: Optional[StrictStr] = "example_exercise_type"
strike: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
trading_conventions: Optional[TradingConventions] = # Replace with your value
instrument_type: StrictStr = "example_instrument_type"
interest_rate_swaption_instance = InterestRateSwaption(start_date=start_date, pay_or_receive_fixed=pay_or_receive_fixed, premium=premium, delivery_method=delivery_method, swap=swap, time_zone_conventions=time_zone_conventions, underlying=underlying, delivery_days=delivery_days, business_day_convention=business_day_convention, settlement_calendars=settlement_calendars, dom_ccy=dom_ccy, exercise_date=exercise_date, exercise_type=exercise_type, strike=strike, trading_conventions=trading_conventions, instrument_type=instrument_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

