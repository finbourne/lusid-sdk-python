# SimpleInstrument

LUSID representation of a Simple Instrument, used as a basic definition of a generic instrument.  No analytics can be obtained for this.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maturity_date** | **datetime** | The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates that may well be observed or set prior to the maturity date, but refer to a termination date beyond it. | [optional] 
**dom_ccy** | **str** | The domestic currency. | 
**asset_class** | **str** | The available values are: InterestRates, FX, Inflation, Equities, Credit, Commodities, Money, Unknown | 
**fgn_ccys** | **List[str]** | The set of foreign currencies, if any (optional). | [optional] 
**simple_instrument_type** | **str** | The Instrument type of the simple instrument. | 
**time_zone_conventions** | [**TimeZoneConventions**](TimeZoneConventions.md) |  | [optional] 
**trading_conventions** | [**TradingConventions**](TradingConventions.md) |  | [optional] 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit | 
## Example

```python
from lusid.models.simple_instrument import SimpleInstrument
from typing import Any, Dict, List, Optional
from pydantic.v1 import Field, StrictStr, conlist, constr, validator
from datetime import datetime
maturity_date: Optional[datetime] = # Replace with your value
dom_ccy: StrictStr = "example_dom_ccy"
asset_class: StrictStr = "example_asset_class"
fgn_ccys: Optional[conlist(StrictStr)] = # Replace with your value
simple_instrument_type: StrictStr = "example_simple_instrument_type"
time_zone_conventions: Optional[TimeZoneConventions] = # Replace with your value
trading_conventions: Optional[TradingConventions] = # Replace with your value
instrument_type: StrictStr = "example_instrument_type"
simple_instrument_instance = SimpleInstrument(maturity_date=maturity_date, dom_ccy=dom_ccy, asset_class=asset_class, fgn_ccys=fgn_ccys, simple_instrument_type=simple_instrument_type, time_zone_conventions=time_zone_conventions, trading_conventions=trading_conventions, instrument_type=instrument_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

