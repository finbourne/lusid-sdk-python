# Cash

LUSID representation of Cash which is the sum of one or more cashflows from the past.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dom_ccy** | **str** | The domestic currency of the instrument. | 
**amount** | **float** | Cash amount. | 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit | 
## Example

```python
from lusid.models.cash import Cash
from typing import Any, Dict, Union
from pydantic.v1 import Field, StrictFloat, StrictInt, StrictStr, validator

dom_ccy: StrictStr = "example_dom_ccy"
amount: Union[StrictFloat, StrictInt] = # Replace with your value
instrument_type: StrictStr = "example_instrument_type"
cash_instance = Cash(dom_ccy=dom_ccy, amount=amount, instrument_type=instrument_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

