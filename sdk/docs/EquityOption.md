# EquityOption

LUSID representation of a plain vanilla OTC Equity Option.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | The start date of the instrument. This is normally synonymous with the trade-date. | 
**option_maturity_date** | **datetime** | The maturity date of the option. | 
**option_settlement_date** | **datetime** | The settlement date of the option. | [optional] 
**delivery_type** | **str** | Is the option cash settled or physical delivery of option    Supported string (enumeration) values are: [Cash, Physical]. | 
**option_type** | **str** | Type of optionality for the option    Supported string (enumeration) values are: [Call, Put]. | 
**strike** | **float** | The strike of the option. | 
**dom_ccy** | **str** | The domestic currency of the instrument. | 
**underlying_identifier** | **str** | The market identifier type of the underlying code, e.g RIC.    Supported string (enumeration) values are: [LusidInstrumentId, Isin, Sedol, Cusip, ClientInternal, Figi, RIC, QuotePermId, REDCode, BBGId, ICECode].  Optional field, should be used in combination with the Code field.  Not compatible with the Underlying field. | [optional] 
**code** | **str** | The identifying code for the equity underlying, e.g. &#39;IBM.N&#39;.  Optional field, should be used in combination with the UnderlyingIdentifier field.  Not compatible with the Underlying field. | [optional] 
**equity_option_type** | **str** | Equity option types. E.g. Vanilla (default), RightsIssue, Warrant.    Supported string (enumeration) values are: [Vanilla, RightsIssue, Warrant]. | [optional] 
**number_of_shares** | **float** | The amount of shares to exchange if the option is exercised. | [optional] 
**premium** | [**Premium**](Premium.md) |  | [optional] 
**exercise_type** | **str** | Type of optionality that is present; European, American.    Supported string (enumeration) values are: [European, American]. | [optional] 
**underlying** | [**LusidInstrument**](LusidInstrument.md) |  | [optional] 
**delivery_days** | **int** | Number of business days between exercise date and settlement of the option payoff or underlying. | [optional] 
**business_day_convention** | **str** | Business day convention for option exercise date to settlement date calculation.  Supported string (enumeration) values are: [NoAdjustment, Previous, P, Following, F, ModifiedPrevious, MP, ModifiedFollowing, MF, HalfMonthModifiedFollowing, Nearest]. | [optional] 
**settlement_calendars** | **List[str]** | Holiday calendars for option exercise date to settlement date calculation. | [optional] 
**time_zone_conventions** | [**TimeZoneConventions**](TimeZoneConventions.md) |  | [optional] 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit | 
## Example

```python
from lusid.models.equity_option import EquityOption
from typing import Any, Dict, List, Optional, Union
from pydantic.v1 import Field, StrictFloat, StrictInt, StrictStr, conlist, constr, validator
from datetime import datetime
start_date: datetime = # Replace with your value
option_maturity_date: datetime = # Replace with your value
option_settlement_date: Optional[datetime] = # Replace with your value
delivery_type: StrictStr = "example_delivery_type"
option_type: StrictStr = "example_option_type"
strike: Union[StrictFloat, StrictInt] = # Replace with your value
dom_ccy: StrictStr = "example_dom_ccy"
underlying_identifier: Optional[StrictStr] = "example_underlying_identifier"
code: Optional[StrictStr] = "example_code"
equity_option_type: Optional[StrictStr] = "example_equity_option_type"
number_of_shares: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
premium: Optional[Premium] = None
exercise_type: Optional[StrictStr] = "example_exercise_type"
underlying: Optional[LusidInstrument] = None
delivery_days: Optional[StrictInt] = # Replace with your value
delivery_days: Optional[StrictInt] = None
business_day_convention: Optional[StrictStr] = "example_business_day_convention"
settlement_calendars: Optional[conlist(StrictStr)] = # Replace with your value
time_zone_conventions: Optional[TimeZoneConventions] = # Replace with your value
instrument_type: StrictStr = "example_instrument_type"
equity_option_instance = EquityOption(start_date=start_date, option_maturity_date=option_maturity_date, option_settlement_date=option_settlement_date, delivery_type=delivery_type, option_type=option_type, strike=strike, dom_ccy=dom_ccy, underlying_identifier=underlying_identifier, code=code, equity_option_type=equity_option_type, number_of_shares=number_of_shares, premium=premium, exercise_type=exercise_type, underlying=underlying, delivery_days=delivery_days, business_day_convention=business_day_convention, settlement_calendars=settlement_calendars, time_zone_conventions=time_zone_conventions, instrument_type=instrument_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

