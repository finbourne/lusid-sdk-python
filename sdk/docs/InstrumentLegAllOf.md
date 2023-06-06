# InstrumentLegAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan | 

## Example

```python
from lusid.models.instrument_leg_all_of import InstrumentLegAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of InstrumentLegAllOf from a JSON string
instrument_leg_all_of_instance = InstrumentLegAllOf.from_json(json)
# print the JSON string representation of the object
print InstrumentLegAllOf.to_json()

# convert the object into a dict
instrument_leg_all_of_dict = instrument_leg_all_of_instance.to_dict()
# create an instance of InstrumentLegAllOf from a dict
instrument_leg_all_of_form_dict = instrument_leg_all_of.from_dict(instrument_leg_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


