# PreferredShare

LUSID representation of a preferred (preference) share: an equity-classified security that pays an  intrinsic, schedule-driven dividend of DividendRate x ParValue. The schedule is perpetual unless a  MaturityDate is supplied, in which case the share redeems at par on that date.  It carries Bond's shape rather than Equity's - StartDate, MaturityDate and FlowConventions are real,  settable properties - but its dividend is a flat amount per period rather than a day-count-weighted  coupon, and its schedule can be open ended.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | The start date of the instrument. This is the first dividend accrual start date. | 
**maturity_date** | **datetime** | The redemption date of a dated series. Omit it for a perpetual, which is the default: there is  no sentinel date for the client to supply, and a distant date such as one in the year 9999 is  taken literally and schedules a par redemption on it. | [optional] 
**flow_conventions** | [**FlowConventions**](FlowConventions.md) |  | 
**identifiers** | [**PreferredShareAllOfIdentifiers**](PreferredShareAllOfIdentifiers.md) |  | [optional] 
**dom_ccy** | **str** | The domestic currency of the instrument. It is the currency of the dividends and of ParValue. | 
**call_schedule** | [**OptionalitySchedule**](OptionalitySchedule.md) |  | [optional] 
**cfi_code** | **str** | The ISO 10962 CFI code, if the client stores one. Free text, not validated against the standard. | [optional] 
**conversion_schedule** | [**BondConversionSchedule**](BondConversionSchedule.md) |  | [optional] 
**dividend_rate** | **float** | The fixed annualised dividend rate applied to ParValue, so 0.06 is 6%. A scalar for the life of  the share: there is no rate reset, so a fixed-to-floating preferred carries the rate for the  current period and is re-upserted at each reset. | 
**first_dividend_date** | **datetime** | Anchors a short or long first dividend period. Omitted means no stub. | [optional] 
**is_cumulative** | **bool** | Whether a missed dividend accumulates as arrears rather than being forfeited. The client must  state it; there is no default. | 
**lot_size** | **int** | The minimum number of shares that can be traded at once. Microstructure only: it has no effect  on valuation or on cash flows. Defaults to 1. | [optional] 
**par_value** | **float** | The liquidation preference per share. It is the base for the dividend, for the call strike and  for the redemption amount. It is not a price multiplier. | 
**instrument_type** | **str** | Available values: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo, ToBeAnnounced, VolatilitySwap, ToBeAnnouncedOption, CommodityForward, BondOption, CdsOption, CommodityCalendarSwap, BondForward, PreferredShare, CapitalInterest. | 
## Example

```python
from lusid.models.preferred_share import PreferredShare
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

start_date: datetime = # Replace with your value
maturity_date: Optional[datetime] = # Replace with your value
flow_conventions: FlowConventions = # Replace with your value
identifiers: Optional[PreferredShareAllOfIdentifiers] = None
dom_ccy: StrictStr = "example_dom_ccy"
call_schedule: Optional[OptionalitySchedule] = # Replace with your value
cfi_code: Optional[StrictStr] = "example_cfi_code"
conversion_schedule: Optional[BondConversionSchedule] = # Replace with your value
dividend_rate: Union[StrictFloat, StrictInt] = # Replace with your value
first_dividend_date: Optional[datetime] = # Replace with your value
is_cumulative: StrictBool = # Replace with your value
is_cumulative:StrictBool = True
lot_size: Optional[StrictInt] = # Replace with your value
lot_size: Optional[StrictInt] = None
par_value: Union[StrictFloat, StrictInt] = # Replace with your value
instrument_type: StrictStr = "example_instrument_type"
preferred_share_instance = PreferredShare(start_date=start_date, maturity_date=maturity_date, flow_conventions=flow_conventions, identifiers=identifiers, dom_ccy=dom_ccy, call_schedule=call_schedule, cfi_code=cfi_code, conversion_schedule=conversion_schedule, dividend_rate=dividend_rate, first_dividend_date=first_dividend_date, is_cumulative=is_cumulative, lot_size=lot_size, par_value=par_value, instrument_type=instrument_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

