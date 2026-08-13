# VolatilitySwap

LUSID representation of an OTC variance or volatility swap. A single-leg, bullet instrument with no  schedule, no interim cashflows and no accrual. Its market value is supplied by lookup pricing as  Quantity x Notional x Price / PriceDenominator, where the unit price arrives via the quote store  already netted against the strike. The variance/volatility distinction is expressed purely through the  scalar (1 for volatility swaps, 100 for variance swaps) and instrument  properties; it is not a first-class field.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | The start date of the instrument. This is normally synonymous with the trade-date. | 
**maturity_date** | **datetime** | The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates that may well be observed or set prior to the maturity date, but refer to a termination date beyond it. | 
**dom_ccy** | **str** | The domestic currency of the instrument, in which the looked-up price and market value are  denominated. Quotes supplied in a minor unit of this currency (e.g. GBp) are re-denominated  to it by the lookup pricer. | 
**strike** | **float** | The variance or volatility strike agreed at trade date, stored for reference only.  Not used in valuation or close-out. | [optional] 
**notional** | **float** | The agreed notional for the swap. The sign conveys direction (a negative notional held long  produces a negative market value). | 
**price_denominator** | **int** | Scalar divisor applied in the market value calculation:  MktVal &#x3D; Quantity x Notional x Price / PriceDenominator.  1 for volatility swaps (VOLS) and 100 for variance swaps (VARS). Must be positive. | 
**time_zone_conventions** | [**TimeZoneConventions**](TimeZoneConventions.md) |  | [optional] 
**underlying** | **str** | Free-text reference label identifying the underlying index or asset (e.g. &#39;SPX&#39;, &#39;SX5E&#39;, &#39;KOSPI2&#39;).  Reference only; not used in valuation. | [optional] 
**instrument_type** | **str** | Available values: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo, ToBeAnnounced, VolatilitySwap, ToBeAnnouncedOption, CommodityForward, BondOption. | 
## Example

```python
from lusid.models.volatility_swap import VolatilitySwap
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

start_date: datetime = # Replace with your value
maturity_date: datetime = # Replace with your value
dom_ccy: StrictStr = "example_dom_ccy"
strike: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
notional: Union[StrictFloat, StrictInt] = # Replace with your value
price_denominator: StrictInt = # Replace with your value
price_denominator: StrictInt = 42
time_zone_conventions: Optional[TimeZoneConventions] = # Replace with your value
underlying: Optional[StrictStr] = "example_underlying"
instrument_type: StrictStr = "example_instrument_type"
volatility_swap_instance = VolatilitySwap(start_date=start_date, maturity_date=maturity_date, dom_ccy=dom_ccy, strike=strike, notional=notional, price_denominator=price_denominator, time_zone_conventions=time_zone_conventions, underlying=underlying, instrument_type=instrument_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

