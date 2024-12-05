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
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit | 

## Example

```python
from lusid.models.complex_bond import ComplexBond

# TODO update the JSON string below
json = "{}"
# create an instance of ComplexBond from a JSON string
complex_bond_instance = ComplexBond.from_json(json)
# print the JSON string representation of the object
print ComplexBond.to_json()

# convert the object into a dict
complex_bond_dict = complex_bond_instance.to_dict()
# create an instance of ComplexBond from a dict
complex_bond_form_dict = complex_bond.from_dict(complex_bond_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


