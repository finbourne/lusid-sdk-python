# CashPerpetualAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | The start date of the instrument. This is normally synonymous with the trade-date. | 
**dom_ccy** | **str** | The domestic currency of the instrument. | 
**principal** | **float** | The face-value or principal for the cash at outset. | 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan | 

## Example

```python
from lusid.models.cash_perpetual_all_of import CashPerpetualAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of CashPerpetualAllOf from a JSON string
cash_perpetual_all_of_instance = CashPerpetualAllOf.from_json(json)
# print the JSON string representation of the object
print CashPerpetualAllOf.to_json()

# convert the object into a dict
cash_perpetual_all_of_dict = cash_perpetual_all_of_instance.to_dict()
# create an instance of CashPerpetualAllOf from a dict
cash_perpetual_all_of_form_dict = cash_perpetual_all_of.from_dict(cash_perpetual_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


