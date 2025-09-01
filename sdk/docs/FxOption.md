# FxOption

LUSID representation of an FX Option.  Including Vanilla, American, European, and Digital (Binary) options.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | The start date of the instrument. This is normally synonymous with the trade-date. | 
**dom_ccy** | **str** | The domestic currency of the instrument. | 
**dom_amount** | **float** | The Amount of DomCcy that will be exchanged if the option is exercised.  This amount should be a positive number, with the Call/Put flag used to indicate direction.  The corresponding amount of FgnCcy that will be exchanged is this amount times the strike.  Note there is no rounding performed on this computed value.  This is an optional field, if not set the option ContractSize will default to 1. | [optional] 
**fgn_ccy** | **str** | The foreign currency of the FX. | 
**fgn_amount** | **float** | For a vanilla FxOption contract, FgnAmount cannot be set.  In case of a digital FxOption (IsPayoffDigital&#x3D;&#x3D;true)  a payoff (if the option is in the money) can be either  in domestic or in foreign currency - for the latter  FgnAmount must be set.  Note: It is invalid to have FgnAmount and DomAmount  at the same time. | [optional] 
**strike** | **float** | The strike of the option. | [optional] 
**barriers** | [**List[Barrier]**](Barrier.md) | For a barrier option the list should not be empty. Up to two barriers are supported.  An option cannot be at the same time barrier- and touch-option.  One (or both) of the lists must be empty. | [optional] 
**exercise_type** | **str** | Type of optionality that is present; European, American.    Supported string (enumeration) values are: [European, American].  Defaults to \&quot;European\&quot; if not set. | [optional] 
**is_call_not_put** | **bool** | True if the option is a call, false if the option is a put. | 
**is_delivery_not_cash** | **bool** | True if the option delivers the FX underlying, False if the option is settled in cash. | 
**is_payoff_digital** | **bool** | By default IsPayoffDigital is false. If IsPayoffDigital&#x3D;true,  the option is &#39;digital&#39;, and the option payoff is 0 or 1 unit of currency,  instead of a vanilla CallPayoff&#x3D;max(spot-strike,0) or PutPayoff&#x3D;max(strike-spot,0). | [optional] 
**option_maturity_date** | **datetime** | The maturity date of the option. | 
**option_settlement_date** | **datetime** | The settlement date of the option. | 
**payout_style** | **str** | PayoutStyle for touch options.                For options without touch optionality, payoutStyle should not be set.  For options with touch optionality (where the touches data has been set), payoutStyle must be defined and cannot be None.    Supported string (enumeration) values are: [Deferred, Immediate].  Defaults to \&quot;None\&quot; if not set. | [optional] 
**premium** | [**Premium**](Premium.md) |  | [optional] 
**touches** | [**List[Touch]**](Touch.md) | For a touch option the list should not be empty. Up to two touches are supported.  An option cannot be at the same time barrier- and touch-option.  One (or both) of the lists must be empty. | [optional] 
**time_zone_conventions** | [**TimeZoneConventions**](TimeZoneConventions.md) |  | [optional] 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo | 
## Example

```python
from lusid.models.fx_option import FxOption
from typing import Any, Dict, List, Optional, Union
from pydantic.v1 import Field, StrictBool, StrictFloat, StrictInt, StrictStr, conlist, validator
from datetime import datetime
start_date: datetime = # Replace with your value
dom_ccy: StrictStr = "example_dom_ccy"
dom_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
fgn_ccy: StrictStr = "example_fgn_ccy"
fgn_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
strike: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
barriers: Optional[conlist(Barrier)] = # Replace with your value
exercise_type: Optional[StrictStr] = "example_exercise_type"
is_call_not_put: StrictBool = # Replace with your value
is_call_not_put:StrictBool = True
is_delivery_not_cash: StrictBool = # Replace with your value
is_delivery_not_cash:StrictBool = True
is_payoff_digital: Optional[StrictBool] = # Replace with your value
is_payoff_digital:Optional[StrictBool] = None
option_maturity_date: datetime = # Replace with your value
option_settlement_date: datetime = # Replace with your value
payout_style: Optional[StrictStr] = "example_payout_style"
premium: Optional[Premium] = None
touches: Optional[conlist(Touch)] = # Replace with your value
time_zone_conventions: Optional[TimeZoneConventions] = # Replace with your value
instrument_type: StrictStr = "example_instrument_type"
fx_option_instance = FxOption(start_date=start_date, dom_ccy=dom_ccy, dom_amount=dom_amount, fgn_ccy=fgn_ccy, fgn_amount=fgn_amount, strike=strike, barriers=barriers, exercise_type=exercise_type, is_call_not_put=is_call_not_put, is_delivery_not_cash=is_delivery_not_cash, is_payoff_digital=is_payoff_digital, option_maturity_date=option_maturity_date, option_settlement_date=option_settlement_date, payout_style=payout_style, premium=premium, touches=touches, time_zone_conventions=time_zone_conventions, instrument_type=instrument_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

