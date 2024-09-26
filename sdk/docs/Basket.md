# Basket

LUSID representation of a basket of instruments.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**basket_name** | [**BasketIdentifier**](BasketIdentifier.md) |  | 
**basket_type** | **str** | What contents does the basket have. The validation will check that the instrument types contained match those expected.    Supported string (enumeration) values are: [Bonds, Credits, Equities, EquitySwap]. | 
**weighted_instruments** | [**WeightedInstruments**](WeightedInstruments.md) |  | 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument | 

## Example

```python
from lusid.models.basket import Basket

# TODO update the JSON string below
json = "{}"
# create an instance of Basket from a JSON string
basket_instance = Basket.from_json(json)
# print the JSON string representation of the object
print Basket.to_json()

# convert the object into a dict
basket_dict = basket_instance.to_dict()
# create an instance of Basket from a dict
basket_form_dict = basket.from_dict(basket_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


