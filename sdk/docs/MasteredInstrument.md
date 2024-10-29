# MasteredInstrument

LUSID representation of a reference to another instrument that has already been upserted (Mastered)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifiers** | **Dict[str, str]** | Dictionary of identifiers of the mastered instrument | 
**mastered_dom_ccy** | **str** | DomCcy of the Instrument that Mastered Instrument points to - read only field | [optional] [readonly] 
**mastered_instrument_type** | **str** | Type of the Instrument that Mastered Instrument points to - read only field | [optional] [readonly] 
**mastered_lusid_instrument_id** | **str** | Luid of the Instrument that Mastered Instrument points to - read only field | [optional] [readonly] 
**mastered_name** | **str** | Name of the Instrument that Mastered Instrument points to - read only field | [optional] [readonly] 
**mastered_scope** | **str** | Scope of the Instrument that Mastered Instrument points to - read only field | [optional] [readonly] 
**mastered_asset_class** | **str** | Asset class of the underlying mastered instrument - read only field    Supported string (enumeration) values are: [InterestRates, FX, Inflation, Equities, Credit, Commodities, Money]. | [optional] [readonly] 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility | 

## Example

```python
from lusid.models.mastered_instrument import MasteredInstrument

# TODO update the JSON string below
json = "{}"
# create an instance of MasteredInstrument from a JSON string
mastered_instrument_instance = MasteredInstrument.from_json(json)
# print the JSON string representation of the object
print MasteredInstrument.to_json()

# convert the object into a dict
mastered_instrument_dict = mastered_instrument_instance.to_dict()
# create an instance of MasteredInstrument from a dict
mastered_instrument_form_dict = mastered_instrument.from_dict(mastered_instrument_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


