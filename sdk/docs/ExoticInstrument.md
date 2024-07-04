# ExoticInstrument

LUSID representation of a generic OTC Exotic Instrument that is not fully defined within other LUSID models.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_format** | [**InstrumentDefinitionFormat**](InstrumentDefinitionFormat.md) |  | 
**content** | **str** | The original document received into the system. This format could potentially be anything though is most likely to be either Json or Xml. In the case where no other  interface is supported it is possible to fall back onto this.  For example, a trade from an external client system. This may be recognized internally by Lusid or simply passed through to another vendor system. | 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash | 

## Example

```python
from lusid.models.exotic_instrument import ExoticInstrument

# TODO update the JSON string below
json = "{}"
# create an instance of ExoticInstrument from a JSON string
exotic_instrument_instance = ExoticInstrument.from_json(json)
# print the JSON string representation of the object
print ExoticInstrument.to_json()

# convert the object into a dict
exotic_instrument_dict = exotic_instrument_instance.to_dict()
# create an instance of ExoticInstrument from a dict
exotic_instrument_form_dict = exotic_instrument.from_dict(exotic_instrument_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


