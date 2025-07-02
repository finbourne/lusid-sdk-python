# ComplexBond

LUSID representation of a Complex Bond.  Including Floating, Fixed-to-float, Sinkable, Callable, Puttable, and Mortgage Backed Securities.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifiers** | **Dict[str, str]** | External market codes and identifiers for the bond, e.g. ISIN. | [optional] 
**calculation_type** | **str** | The calculation type applied to the bond coupon amount. This is required for bonds that have a particular type of computing the period coupon, such as simple compounding,  irregular coupons etc.  The default CalculationType is &#x60;Standard&#x60;, which returns a coupon amount equal to Principal * Coupon Rate / Coupon Frequency. Coupon Frequency is 12M / Payment Frequency.  Payment Frequency can be 1M, 3M, 6M, 12M etc. So Coupon Frequency can be 12, 4, 2, 1 respectively.    Supported string (enumeration) values are: [Standard, DayCountCoupon, NoCalculationFloater, BrazilFixedCoupon, StandardWithCappedAccruedInterest]. | [optional] 
**schedules** | [**List[Schedule]**](Schedule.md) | schedules. | [optional] 
**original_issue_price** | **float** | The price the complex bond was issued at. This is to be entered as a percentage of par, for example a value of 98.5 would represent 98.5%. | [optional] 
**rounding_conventions** | [**List[RoundingConvention]**](RoundingConvention.md) | Rounding conventions for analytics, if any. | [optional] 
**asset_backed** | **bool** | If this flag is set to true, then the outstanding notional and principal repayments will be calculated based  on pool factors in the quote store. Usually AssetBacked bonds also require a RollConvention setting of   within the FlowConventions any given rates schedule (to ensure payment dates always happen on the same day  of the month) and US Agency MBSs with Pay Delay features also require their rates schedules to include an  ExDividendConfiguration to drive the lag between interest accrual and payment. | [optional] 
**asset_pool_identifier** | **str** | Identifier used to retrieve pool factor information about this bond from the quote store. This is typically  the bond&#39;s ISIN, but can also be ClientInternal. Please ensure you align the MarketDataKeyRule with the  correct Quote (Quote.ClientInternal.* or Quote.Isin.*) | [optional] 
**trading_conventions** | [**TradingConventions**](TradingConventions.md) |  | [optional] 
**time_zone_conventions** | [**TimeZoneConventions**](TimeZoneConventions.md) |  | [optional] 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit | 
## Example

```python
from lusid.models.complex_bond import ComplexBond
from typing import Any, Dict, List, Optional, Union
from pydantic.v1 import Field, StrictBool, StrictFloat, StrictInt, StrictStr, conlist, constr, validator

identifiers: Optional[Dict[str, StrictStr]] = # Replace with your value
calculation_type: Optional[StrictStr] = "example_calculation_type"
schedules: Optional[conlist(Schedule)] = # Replace with your value
original_issue_price: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
rounding_conventions: Optional[conlist(RoundingConvention)] = # Replace with your value
asset_backed: Optional[StrictBool] = # Replace with your value
asset_backed:Optional[StrictBool] = None
asset_pool_identifier: Optional[StrictStr] = "example_asset_pool_identifier"
trading_conventions: Optional[TradingConventions] = # Replace with your value
time_zone_conventions: Optional[TimeZoneConventions] = # Replace with your value
instrument_type: StrictStr = "example_instrument_type"
complex_bond_instance = ComplexBond(identifiers=identifiers, calculation_type=calculation_type, schedules=schedules, original_issue_price=original_issue_price, rounding_conventions=rounding_conventions, asset_backed=asset_backed, asset_pool_identifier=asset_pool_identifier, trading_conventions=trading_conventions, time_zone_conventions=time_zone_conventions, instrument_type=instrument_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

