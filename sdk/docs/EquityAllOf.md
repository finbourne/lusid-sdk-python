# EquityAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifiers** | [**EquityAllOfIdentifiers**](EquityAllOfIdentifiers.md) |  | [optional] 
**dom_ccy** | **str** | The domestic currency of the instrument. | 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan | 

## Example

```python
from lusid.models.equity_all_of import EquityAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of EquityAllOf from a JSON string
equity_all_of_instance = EquityAllOf.from_json(json)
# print the JSON string representation of the object
print EquityAllOf.to_json()

# convert the object into a dict
equity_all_of_dict = equity_all_of_instance.to_dict()
# create an instance of EquityAllOf from a dict
equity_all_of_form_dict = equity_all_of.from_dict(equity_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


