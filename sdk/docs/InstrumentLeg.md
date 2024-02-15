# InstrumentLeg

Base class for representing instrument legs in LUSID.  An instrument leg describes a set of cashflows that are paid at a set of points in time according to some set of conventions.  This base class should not be directly instantiated; only its inheritors should be used.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass | 

## Example

```python
from lusid.models.instrument_leg import InstrumentLeg

# TODO update the JSON string below
json = "{}"
# create an instance of InstrumentLeg from a JSON string
instrument_leg_instance = InstrumentLeg.from_json(json)
# print the JSON string representation of the object
print InstrumentLeg.to_json()

# convert the object into a dict
instrument_leg_dict = instrument_leg_instance.to_dict()
# create an instance of InstrumentLeg from a dict
instrument_leg_form_dict = instrument_leg.from_dict(instrument_leg_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


