# BondForward

LUSID representation of an OTC bilateral forward contract to buy or sell a specified, already-mastered  debt security (Bond or ComplexBond) at an agreed clean price on a settlement date beyond the market's  standard settlement cycle. No cash moves at trade date, there is no premium, and both parties are  unconditionally obliged. Quote-driven valuation; cash settlement only in the current scope (physical  delivery is future work). Direction is the sign of the holding's units and size is the holding's units,  neither is on the definition, so a partial unwind or novation is an ordinary change in units.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | The start date of the instrument. This is normally synonymous with the trade-date. | 
**maturity_date** | **datetime** | The contractual settlement date, on which cash settlement takes place. Named MaturityDate because  IDefinition requires it and every other forward uses it. Supplied as an agreed business day on the  settlement currency&#39;s own calendar; LUSID does not adjust it. | 
**dom_ccy** | **str** | The domestic currency of the instrument. | 
**agreed_clean_price** | **float** | The agreed price, percent of par. Named agreedCleanPrice rather than strike because the contract  carries no optionality, and a percent-of-par price would read as an option strike under that name. | 
**contract_size** | **float** | Face amount of the underlying per unit. Together with the per-100 price this converts price into  money: pricePerUnit &#x3D; agreedCleanPrice / 100 * contractSize. Set 1 to make one unit equal one  currency unit of face. | 
**delivery_type** | **str** | How the forward settles. Only Cash is accepted in the current scope: physical delivery of a bond by  a wrapper instrument has no shipped mechanism for opening the delivered position with purchased  accrued. The field is required rather than defaulted so that a physically-settling contract is  refused explicitly rather than silently cash-settled.                Supported string (enumeration) values are: [Cash, Physical]. Available values: Cash, Physical. | 
**price_basis** | **str** | Whether the agreed price is quoted clean or dirty. Only Clean is accepted: a dirty forward price is  an invoice price for value at settlement, and nothing downstream carries the clean-and-accrued split,  so a Dirty value is rejected at upsert with the conversion instruction. The field is required so that  a dirty price supplied as clean is declared rather than silently mispriced.                Supported string (enumeration) values are: [Clean, Dirty]. Available values: Clean, Dirty. | 
**time_zone_conventions** | [**TimeZoneConventions**](TimeZoneConventions.md) |  | [optional] 
**trading_conventions** | [**TradingConventions**](TradingConventions.md) |  | [optional] 
**underlying** | [**LusidInstrument**](LusidInstrument.md) |  | 
**instrument_type** | **str** | Available values: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo, ToBeAnnounced, VolatilitySwap, ToBeAnnouncedOption, CommodityForward, BondOption, CdsOption, CommodityCalendarSwap, BondForward. | 
## Example

```python
from lusid.models.bond_forward import BondForward
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

start_date: datetime = # Replace with your value
maturity_date: datetime = # Replace with your value
dom_ccy: StrictStr = "example_dom_ccy"
agreed_clean_price: Union[StrictFloat, StrictInt] = # Replace with your value
contract_size: Union[StrictFloat, StrictInt] = # Replace with your value
delivery_type: StrictStr = "example_delivery_type"
price_basis: StrictStr = "example_price_basis"
time_zone_conventions: Optional[TimeZoneConventions] = # Replace with your value
trading_conventions: Optional[TradingConventions] = # Replace with your value
underlying: LusidInstrument
instrument_type: StrictStr = "example_instrument_type"
bond_forward_instance = BondForward(start_date=start_date, maturity_date=maturity_date, dom_ccy=dom_ccy, agreed_clean_price=agreed_clean_price, contract_size=contract_size, delivery_type=delivery_type, price_basis=price_basis, time_zone_conventions=time_zone_conventions, trading_conventions=trading_conventions, underlying=underlying, instrument_type=instrument_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

