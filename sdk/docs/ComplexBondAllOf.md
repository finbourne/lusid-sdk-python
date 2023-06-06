# ComplexBondAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifiers** | **Dict[str, str]** | external market codes and identifiers for the bond, e.g. ISIN. | [optional] 
**calculation_type** | **str** | The calculation type applied to the bond coupon amount. This is required for bonds that have a particular type of computing the period coupon, such as simple compounding,  irregular coupons etc.  The default CalculationType is &#x60;Standard&#x60;, which returns a coupon amount equal to Principal * Coupon Rate / Coupon Frequency. Coupon Frequency is 12M / Payment Frequency.  Payment Frequency can be 1M, 3M, 6M, 12M etc. So Coupon Frequency can be 12, 4, 2, 1 respectively.    Supported string (enumeration) values are: [Standard, DayCountCoupon, NoCalculationFloater, BrazilFixedCoupon]. | [optional] 
**schedules** | [**List[Schedule]**](Schedule.md) | schedules. | [optional] 
**rounding_conventions** | [**List[RoundingConvention]**](RoundingConvention.md) | Rounding conventions for analytics, if any. | [optional] 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan | 

## Example

```python
from lusid.models.complex_bond_all_of import ComplexBondAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of ComplexBondAllOf from a JSON string
complex_bond_all_of_instance = ComplexBondAllOf.from_json(json)
# print the JSON string representation of the object
print ComplexBondAllOf.to_json()

# convert the object into a dict
complex_bond_all_of_dict = complex_bond_all_of_instance.to_dict()
# create an instance of ComplexBondAllOf from a dict
complex_bond_all_of_form_dict = complex_bond_all_of.from_dict(complex_bond_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


