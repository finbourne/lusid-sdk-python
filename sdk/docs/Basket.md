# Basket

LUSID representation of a basket of instruments.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**basket_name** | [**BasketIdentifier**](BasketIdentifier.md) |  | 
**basket_type** | **str** | What contents does the basket have. The validation will check that the instrument types contained match those expected.  Supported string (enumeration) values are: [Bonds, Credits, Equities, EquitySwap]. | 
**weighted_instruments** | [**WeightedInstruments**](WeightedInstruments.md) |  | 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo | 
## Example

```python
from lusid.models.basket import Basket
from typing import Any, Dict
from pydantic.v1 import Field, StrictStr, constr, validator

basket_name: BasketIdentifier = # Replace with your value
basket_type: StrictStr = "example_basket_type"
weighted_instruments: WeightedInstruments = # Replace with your value
instrument_type: StrictStr = "example_instrument_type"
basket_instance = Basket(basket_name=basket_name, basket_type=basket_type, weighted_instruments=weighted_instruments, instrument_type=instrument_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

