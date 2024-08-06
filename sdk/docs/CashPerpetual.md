# CashPerpetual

LUSID representation of a Perpetual Cash Flow.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | The start date of the instrument. This is normally synonymous with the trade-date. | 
**dom_ccy** | **str** | The domestic currency of the instrument. | 
**principal** | **float** | The face-value or principal for the cash at outset. | 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash | 

## Example

```python
from lusid.models.cash_perpetual import CashPerpetual

# TODO update the JSON string below
json = "{}"
# create an instance of CashPerpetual from a JSON string
cash_perpetual_instance = CashPerpetual.from_json(json)
# print the JSON string representation of the object
print CashPerpetual.to_json()

# convert the object into a dict
cash_perpetual_dict = cash_perpetual_instance.to_dict()
# create an instance of CashPerpetual from a dict
cash_perpetual_form_dict = cash_perpetual.from_dict(cash_perpetual_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


