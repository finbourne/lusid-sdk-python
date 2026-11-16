# InflationLeg

LUSID representation of an Inflation Leg.  This leg instrument is part of the InflationSwap instrument, but can also be used as a standalone instrument.  The implementation supports the following inflation leg types:  * Zero Coupon inflation leg (CPI Leg), with a single payment at maturity.  * Year on Year inflation leg  * LPI Swap Leg (capped and floored YoY)
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | The start date of the instrument. This is normally synonymous with the trade-date. | 
**maturity_date** | **datetime** | The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates that may well be observed or set prior to the maturity date, but refer to a termination date beyond it. | 
**flow_conventions** | [**FlowConventions**](FlowConventions.md) |  | 
**base_cpi** | **float** | Optional BaseCPI, if specified it will be used in place of BaseCPI(StartDate).  This should not be required for standard inflation swaps. | [optional] 
**calculation_type** | **str** | The calculation type.  ZeroCoupon is used for CPILegs where there is a single payment at maturity of  Notional * (CPI(T) / CPI(T0) - 1)  where CPI(T0) is the BaseCPI of this leg  YearOnYear is used for YoY and LPI swap legs where there is a series of annual payments  Notional * dayCount * (CPI(t) / CPI(t-1) - 1)  If a cap and floor is added to this it becomes an LPI swap leg.  Compounded is used for inflation swap legs where there is a series of annual payments  Notional * dayCount * (CPI(t) / CPI(T0) - 1)  i.e. the BaseCPI is used every year. These swaps are not as common as CPI or    IndexedCoupon is used for the coupon stream of an inflation-linked bond, where each period pays  Notional * FixedRate * dayCount * IndexRatio(t)  and IndexRatio(t) is CPI(t) / BaseCPI rounded to IndexPrecision, as on InflationLinkedBond.                Supported string (enumeration) values are: [ZeroCoupon, YearOnYear, Compounded, IndexedCoupon]. | 
**cap_rate** | **float** | Optional cap on a YearOnYear leg: each period&#39;s 12-month inflation rate is clamped to at most this rate before  the accrual fraction is applied, at any payment frequency, so an LPI leg caps each year at 5%. In the legs  form of an InflationSwap it is rejected on a ZeroCoupon, Compounded or IndexedCoupon leg, where it would clamp  the total change since the start. In the deprecated inflationLeg form a ZeroCoupon or Compounded cap keeps  clamping that total change, as today. | [optional] 
**floor_rate** | **float** | Optional floor on a YearOnYear leg: each period&#39;s 12-month inflation rate is clamped to at least this rate  before the accrual fraction is applied, at any payment frequency, so a 0% floor stops deflation being paid.  In the legs form of an InflationSwap it is rejected on a ZeroCoupon, Compounded or IndexedCoupon leg, where it  would clamp the total change since the start. In the deprecated inflationLeg form a ZeroCoupon or Compounded  floor keeps clamping that total change, as today. | [optional] 
**inflation_index_conventions** | [**InflationIndexConventions**](InflationIndexConventions.md) |  | 
**notional** | **float** | The notional | 
**pay_receive** | **str** | PayReceive flag for the inflation leg.  This field is optional and defaults to Pay.    Supported string (enumeration) values are: [Pay, Receive]. | [optional] 
**time_zone_conventions** | [**TimeZoneConventions**](TimeZoneConventions.md) |  | [optional] 
**fixed_rate** | **float** | The real coupon rate of an IndexedCoupon leg: each period pays Notional * FixedRate * dayCount * IndexRatio.  Required when CalculationType is IndexedCoupon and not allowed otherwise. | [optional] 
**base_cpi_date** | **datetime** | Optional date the base CPI is observed on, with the same meaning as on InflationLinkedBond: the un-lagged  date (for a bond asset swap, the bond&#39;s dated date) whose reference CPI is the base. Defaults to the StartDate.  Ignored when BaseCPI is given. | [optional] 
**index_precision** | **int** | Number of decimal places the IndexedCoupon index ratio is rounded to, as on InflationLinkedBond. Defaults to 5. | [optional] 
**principal_protection** | **bool** | Whether an indexed final notional exchange is floored at par, paying max(IndexRatio, 1) times the amount, as on  InflationLinkedBond. Coupons are never floored. Defaults to true. | [optional] 
**notional_exchange_type** | **str** | Which notional exchanges the leg makes. The start exchange pays the un-indexed amount against the leg; the  maturity exchange pays the amount times the index ratio with the leg, floored at par under PrincipalProtection.                Supported string (enumeration) values are: [None, Initial, Final, Both].  Defaults to \&quot;None\&quot; if not set. | [optional] 
**initial_exchange_amount** | **float** | The amount exchanged at the start of the leg, when NotionalExchangeType is Initial or Both. Defaults to the  notional. Never indexed. Must be non-negative. | [optional] 
**final_exchange_amount** | **float** | The real amount exchanged at maturity, when NotionalExchangeType is Final or Both. Defaults to the notional.  Paid times the index ratio, floored at par under PrincipalProtection. Must be non-negative. | [optional] 
**instrument_type** | **str** | Available values: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo, ToBeAnnounced, VolatilitySwap, ToBeAnnouncedOption, CommodityForward, BondOption, CdsOption, CommodityCalendarSwap, BondForward, PreferredShare, CapitalInterest, WholeLoanFacility, StripBond. | 
## Example

```python
from lusid.models.inflation_leg import InflationLeg
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
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
fixed_rate: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
base_cpi_date: Optional[datetime] = # Replace with your value
index_precision: Optional[StrictInt] = # Replace with your value
index_precision: Optional[StrictInt] = None
principal_protection: Optional[StrictBool] = # Replace with your value
principal_protection:Optional[StrictBool] = None
notional_exchange_type: Optional[StrictStr] = "example_notional_exchange_type"
initial_exchange_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
final_exchange_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
instrument_type: StrictStr = "example_instrument_type"
inflation_leg_instance = InflationLeg(start_date=start_date, maturity_date=maturity_date, flow_conventions=flow_conventions, base_cpi=base_cpi, calculation_type=calculation_type, cap_rate=cap_rate, floor_rate=floor_rate, inflation_index_conventions=inflation_index_conventions, notional=notional, pay_receive=pay_receive, time_zone_conventions=time_zone_conventions, fixed_rate=fixed_rate, base_cpi_date=base_cpi_date, index_precision=index_precision, principal_protection=principal_protection, notional_exchange_type=notional_exchange_type, initial_exchange_amount=initial_exchange_amount, final_exchange_amount=final_exchange_amount, instrument_type=instrument_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

