# InterestRateSwaption

LUSID representation of an Interest Rate Swaption.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | The start date of the instrument. This is normally synonymous with the trade-date. | 
**pay_or_receive_fixed** | **str** | Pay or Receive the fixed leg of the underlying swap.  Supported string (enumeration) values are: [Pay, Receive]. | 
**premium** | [**Premium**](Premium.md) |  | [optional] 
**delivery_method** | **str** | How does the option settle  Supported string (enumeration) values are: [Cash, Physical]. | 
**swap** | [**InterestRateSwap**](InterestRateSwap.md) |  | 
**time_zone_conventions** | [**TimeZoneConventions**](TimeZoneConventions.md) |  | [optional] 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo | 
## Example

```python
from lusid.models.interest_rate_swaption import InterestRateSwaption
from typing import Any, Dict, Optional
from pydantic.v1 import Field, StrictStr, constr, validator
from datetime import datetime
start_date: datetime = # Replace with your value
pay_or_receive_fixed: StrictStr = "example_pay_or_receive_fixed"
premium: Optional[Premium] = None
delivery_method: StrictStr = "example_delivery_method"
swap: InterestRateSwap = # Replace with your value
time_zone_conventions: Optional[TimeZoneConventions] = # Replace with your value
instrument_type: StrictStr = "example_instrument_type"
interest_rate_swaption_instance = InterestRateSwaption(start_date=start_date, pay_or_receive_fixed=pay_or_receive_fixed, premium=premium, delivery_method=delivery_method, swap=swap, time_zone_conventions=time_zone_conventions, instrument_type=instrument_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

