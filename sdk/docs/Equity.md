# Equity

LUSID representation of an Equity.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifiers** | [**EquityAllOfIdentifiers**](EquityAllOfIdentifiers.md) |  | [optional] 
**dom_ccy** | **str** | The domestic currency of the instrument. | 
**lot_size** | **int** | Deprecated: Use TradingConventions field instead  Equity LotSize, the minimum number of shares that can be bought at once.  Optional, if set must be non-negative, if not set defaults to 1.    Note this property does not impact valuation. From a LUSID analytics perspective, it is purely informational. | [optional] 
**time_zone_conventions** | [**TimeZoneConventions**](TimeZoneConventions.md) |  | [optional] 
**trading_conventions** | [**TradingConventions**](TradingConventions.md) |  | [optional] 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo | 
## Example

```python
from lusid.models.equity import Equity
from typing import Any, Dict, Optional
from pydantic.v1 import Field, StrictInt, StrictStr, validator

identifiers: Optional[EquityAllOfIdentifiers] = None
dom_ccy: StrictStr = "example_dom_ccy"
lot_size: Optional[StrictInt] = # Replace with your value
lot_size: Optional[StrictInt] = None
time_zone_conventions: Optional[TimeZoneConventions] = # Replace with your value
trading_conventions: Optional[TradingConventions] = # Replace with your value
instrument_type: StrictStr = "example_instrument_type"
equity_instance = Equity(identifiers=identifiers, dom_ccy=dom_ccy, lot_size=lot_size, time_zone_conventions=time_zone_conventions, trading_conventions=trading_conventions, instrument_type=instrument_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

