# FundShareClass

LUSID representation of a FundShareClass.  A ShareClass represents a pool of shares, held by investors, within a fund.   A ShareClass can represent a differing investment approach by either Fees,   Income, Currency Risk and Investor type.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**short_code** | **str** | A short identifier, unique across a single fund, usually made up of the ShareClass components. Eg \&quot;A Accumulation Euro Hedged Class\&quot; could become \&quot;A Acc H EUR\&quot;. | 
**fund_share_class_type** | **str** | The type of distribution that the ShareClass will calculate. Can be either &#39;Income&#39; or &#39;Accumulation&#39; - Income classes will pay out and Accumulation classes will retain their ShareClass attributable income.    Supported string (enumeration) values are: [Income, Accumulation]. | 
**distribution_payment_type** | **str** | The tax treatment applied to any distributions calculated within the ShareClass. Can be either &#39;Net&#39; (Distribution Calculated net of tax) or &#39;Gross&#39; (Distribution calculated gross of tax).    Supported string (enumeration) values are: [Gross, Net]. | 
**hedging** | **str** | A flag to indicate the ShareClass is operating currency hedging as a means to limit currency risk as part of it&#39;s investment strategy.    Supported string (enumeration) values are: [Invalid, None, ApplyHedging]. | 
**dom_ccy** | **str** | The domestic currency of the instrument. | 
**rounding_conventions** | [**List[SimpleRoundingConvention]**](SimpleRoundingConvention.md) | Rounding Convention used for the FundShareClass quotes | [optional] 
**trading_conventions** | [**TradingConventions**](TradingConventions.md) |  | [optional] 
**time_zone_conventions** | [**TimeZoneConventions**](TimeZoneConventions.md) |  | [optional] 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo | 
## Example

```python
from lusid.models.fund_share_class import FundShareClass
from typing import Any, Dict, List, Optional
from pydantic.v1 import Field, StrictStr, conlist, constr, validator

short_code: StrictStr = "example_short_code"
fund_share_class_type: StrictStr = "example_fund_share_class_type"
distribution_payment_type: StrictStr = "example_distribution_payment_type"
hedging: StrictStr = "example_hedging"
dom_ccy: StrictStr = "example_dom_ccy"
rounding_conventions: Optional[conlist(SimpleRoundingConvention)] = # Replace with your value
trading_conventions: Optional[TradingConventions] = # Replace with your value
time_zone_conventions: Optional[TimeZoneConventions] = # Replace with your value
instrument_type: StrictStr = "example_instrument_type"
fund_share_class_instance = FundShareClass(short_code=short_code, fund_share_class_type=fund_share_class_type, distribution_payment_type=distribution_payment_type, hedging=hedging, dom_ccy=dom_ccy, rounding_conventions=rounding_conventions, trading_conventions=trading_conventions, time_zone_conventions=time_zone_conventions, instrument_type=instrument_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

