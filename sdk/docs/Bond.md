# Bond

LUSID representation of a Vanilla Fixed Rate Bond.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | The Start date of the bond, this is normally when accrual of the first coupon begins. | 
**maturity_date** | **datetime** | The Maturity date of the bond, this is when the last coupon accrual period ends.  Note that while most bonds have their last payment on this date there are some cases where the final payment is the next working day. | 
**dom_ccy** | **str** | The domestic currency of the instrument. This should be the same as the Currency set on the FlowConventions. | 
**flow_conventions** | [**FlowConventions**](FlowConventions.md) |  | 
**principal** | **float** | The face-value or principal for the bond at outset.  This might be reduced through its lifetime in the event of amortisation or similar. | 
**coupon_rate** | **float** | Simple coupon rate. | 
**identifiers** | **Dict[str, str]** | External market codes and identifiers for the bond, e.g. ISIN. | [optional] 
**ex_dividend_days** | **int** | Optional. Number of calendar days in the ex-dividend period.  If the settlement date falls in the ex-dividend period then the coupon paid is zero and the accrued interest is negative.  If set, this must be a non-negative number.  If not set, or set to 0, then there is no ex-dividend period.                NOTE: This field is deprecated.  If you wish to set the ExDividendDays on a bond, please use the ExDividendConfiguration. | [optional] 
**initial_coupon_date** | **datetime** | Optional and to be DEPRECATED. If set, this is the date at which the bond begins to accrue interest. Instead, this information should be entered in the field StartDate. | [optional] 
**first_coupon_pay_date** | **datetime** | The date that the first coupon of the bond is paid. This is required for bonds that have a long first coupon or short first coupon. The first coupon pay date is used  as an anchor to compare with the start date and determine if this is a long/short coupon period. | [optional] 
**calculation_type** | **str** | The calculation type applied to the bond coupon amount. This is required for bonds that have a particular type of computing the period coupon, such as simple compounding,  irregular coupons etc.  The default CalculationType is &#x60;Standard&#x60;, which returns a coupon amount equal to Principal * Coupon Rate / Coupon Frequency. Coupon Frequency is 12M / Payment Frequency.  Payment Frequency can be 1M, 3M, 6M, 12M etc. So Coupon Frequency can be 12, 4, 2, 1 respectively.    Supported string (enumeration) values are: [Standard, DayCountCoupon, NoCalculationFloater, BrazilFixedCoupon, StandardWithCappedAccruedInterest]. | [optional] 
**rounding_conventions** | [**List[RoundingConvention]**](RoundingConvention.md) | Rounding conventions for analytics, if any. | [optional] 
**ex_dividend_configuration** | [**ExDividendConfiguration**](ExDividendConfiguration.md) |  | [optional] 
**original_issue_price** | **float** | The price the bond was issued at. This is to be entered as a percentage of par, for example a value of 98.5 would represent 98.5%. | [optional] 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash | 

## Example

```python
from lusid.models.bond import Bond

# TODO update the JSON string below
json = "{}"
# create an instance of Bond from a JSON string
bond_instance = Bond.from_json(json)
# print the JSON string representation of the object
print Bond.to_json()

# convert the object into a dict
bond_dict = bond_instance.to_dict()
# create an instance of Bond from a dict
bond_form_dict = bond.from_dict(bond_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


