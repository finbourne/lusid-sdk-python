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
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit | 

## Example

```python
from lusid.models.equity import Equity

# TODO update the JSON string below
json = "{}"
# create an instance of Equity from a JSON string
equity_instance = Equity.from_json(json)
# print the JSON string representation of the object
print Equity.to_json()

# convert the object into a dict
equity_dict = equity_instance.to_dict()
# create an instance of Equity from a dict
equity_form_dict = equity.from_dict(equity_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


