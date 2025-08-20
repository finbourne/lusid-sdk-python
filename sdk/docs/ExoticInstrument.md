# ExoticInstrument

LUSID representation of a generic OTC Exotic Instrument that is not fully defined within other LUSID models.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_format** | [**InstrumentDefinitionFormat**](InstrumentDefinitionFormat.md) |  | 
**content** | **str** | The original document received into the system. This format could potentially be anything though is most likely to be either Json or Xml. In the case where no other interface is supported it is possible to fall back onto this. For example, a trade from an external client system. This may be recognized internally by Lusid or simply passed through to another vendor system. | 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo | 
## Example

```python
from lusid.models.exotic_instrument import ExoticInstrument
from typing import Any, Dict
from pydantic.v1 import Field, StrictStr, constr, validator

instrument_format: InstrumentDefinitionFormat = # Replace with your value
content: StrictStr = "example_content"
instrument_type: StrictStr = "example_instrument_type"
exotic_instrument_instance = ExoticInstrument(instrument_format=instrument_format, content=content, instrument_type=instrument_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

