# ReferenceInstrumentAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_id** | **str** | The Identifier code | 
**instrument_id_type** | **str** | the type of the instrument id e.g. LusidInstrument Id | 
**scope** | **str** | (optional) Scope for the instrument | 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan | 

## Example

```python
from lusid.models.reference_instrument_all_of import ReferenceInstrumentAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of ReferenceInstrumentAllOf from a JSON string
reference_instrument_all_of_instance = ReferenceInstrumentAllOf.from_json(json)
# print the JSON string representation of the object
print ReferenceInstrumentAllOf.to_json()

# convert the object into a dict
reference_instrument_all_of_dict = reference_instrument_all_of_instance.to_dict()
# create an instance of ReferenceInstrumentAllOf from a dict
reference_instrument_all_of_form_dict = reference_instrument_all_of.from_dict(reference_instrument_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


