# ReferenceInstrument

LUSID representation of a reference to another instrument that has already been loaded (e.g. a lookthrough to a portfolio).

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_id** | **str** | The Identifier code | 
**instrument_id_type** | **str** | The type of the instrument id e.g. LusidInstrument Id | 
**scope** | **str** | Scope for the instrument (optional) | 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass | 

## Example

```python
from lusid.models.reference_instrument import ReferenceInstrument

# TODO update the JSON string below
json = "{}"
# create an instance of ReferenceInstrument from a JSON string
reference_instrument_instance = ReferenceInstrument.from_json(json)
# print the JSON string representation of the object
print ReferenceInstrument.to_json()

# convert the object into a dict
reference_instrument_dict = reference_instrument_instance.to_dict()
# create an instance of ReferenceInstrument from a dict
reference_instrument_form_dict = reference_instrument.from_dict(reference_instrument_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


