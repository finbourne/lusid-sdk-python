# InflationLeg

LUSID representation of an Inflation Leg. This leg instrument is part of the InflationSwap instrument, but can also be used as a standalone instrument. The implementation supports the following inflation leg types: * Zero Coupon inflation leg (CPI Leg), with a single payment at maturity. * Year on Year inflation leg * LPI Swap Leg (capped and floored YoY)
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | The start date of the instrument. This is normally synonymous with the trade-date. | 
**maturity_date** | **datetime** | The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount. For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as Constant Maturity Swaps (CMS) often have sensitivities to rates that may well be observed or set prior to the maturity date, but refer to a termination date beyond it. | 
**flow_conventions** | [**FlowConventions**](FlowConventions.md) |  | 
**base_cpi** | **float** | Optional BaseCPI, if specified it will be used in place of BaseCPI(StartDate). This should not be required for standard inflation swaps. | [optional] 
**calculation_type** | **str** | The calculation type. ZeroCoupon is used for CPILegs where there is a single payment at maturity of Notional * (CPI(T) / CPI(T0) - 1) where CPI(T0) is the BaseCPI of this leg YearOnYear is used for YoY and LPI swap legs where there is a series of annual payments Notional * dayCount * (CPI(t) / CPI(t-1) - 1) If a cap and floor is added to this it becomes an LPI swap leg. Compounded is used for inflation swap legs where there is a series of annual payments Notional * dayCount * (CPI(t) / CPI(T0) - 1) i.e. the BaseCPI is used every year. These swaps are not as common as CPI or  Supported string (enumeration) values are: [ZeroCoupon, YearOnYear, Compounded]. | 
**cap_rate** | **float** | Optional cap, needed for LPI Legs or CPI Legs with Caps | [optional] 
**floor_rate** | **float** | Optional floor, needed for LPI Legs or CPI Legs with Floors. | [optional] 
**inflation_index_conventions** | [**InflationIndexConventions**](InflationIndexConventions.md) |  | 
**notional** | **float** | The notional | 
**pay_receive** | **str** | PayReceive flag for the inflation leg. This field is optional and defaults to Pay.  Supported string (enumeration) values are: [Pay, Receive]. | [optional] 
**time_zone_conventions** | [**TimeZoneConventions**](TimeZoneConventions.md) |  | [optional] 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo | 
## Example

```python
from lusid.models.inflation_leg import InflationLeg
from typing import Any, Dict, Optional, Union
from pydantic.v1 import Field, StrictFloat, StrictInt, StrictStr, constr, validator
from datetime import datetime
start_date: datetime = # Replace with your value
maturity_date: datetime = # Replace with your value
flow_conventions: FlowConventions = # Replace with your value
base_cpi: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
calculation_type: StrictStr = "example_calculation_type"
cap_rate: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
floor_rate: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
inflation_index_conventions: InflationIndexConventions = # Replace with your value
notional: Union[StrictFloat, StrictInt] = # Replace with your value
pay_receive: Optional[StrictStr] = "example_pay_receive"
time_zone_conventions: Optional[TimeZoneConventions] = # Replace with your value
instrument_type: StrictStr = "example_instrument_type"
inflation_leg_instance = InflationLeg(start_date=start_date, maturity_date=maturity_date, flow_conventions=flow_conventions, base_cpi=base_cpi, calculation_type=calculation_type, cap_rate=cap_rate, floor_rate=floor_rate, inflation_index_conventions=inflation_index_conventions, notional=notional, pay_receive=pay_receive, time_zone_conventions=time_zone_conventions, instrument_type=instrument_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

