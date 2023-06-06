# BasketAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**basket_name** | [**BasketIdentifier**](BasketIdentifier.md) |  | 
**basket_type** | **str** | What contents does the basket have. The validation will check that the instrument types contained match those expected.    Supported string (enumeration) values are: [Bonds, Credits, Equities, EquitySwap]. | 
**weighted_instruments** | [**WeightedInstruments**](WeightedInstruments.md) |  | 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan | 

## Example

```python
from lusid.models.basket_all_of import BasketAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of BasketAllOf from a JSON string
basket_all_of_instance = BasketAllOf.from_json(json)
# print the JSON string representation of the object
print BasketAllOf.to_json()

# convert the object into a dict
basket_all_of_dict = basket_all_of_instance.to_dict()
# create an instance of BasketAllOf from a dict
basket_all_of_form_dict = basket_all_of.from_dict(basket_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


