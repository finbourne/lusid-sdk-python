# BondOption

LUSID representation of an OTC bilateral option (call or put) on a single mastered cash bond  (Bond, ComplexBond or InflationLinkedBond). Quote-driven valuation with an upfront premium;  European exercise only, cash-settled in the current scope (physical settlement is future work).
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | The start date of the instrument. This is normally synonymous with the trade-date. | 
**dom_ccy** | **str** | The domestic currency of the instrument. | 
**strike** | **float** | The strike as a clean price, percent of par (real/unindexed for a linker). | 
**contract_size** | **float** | The face amount per contract (e.g. 1,000,000). Together with the per-100 clean-price strike this  turns the strike and payoff into money: strikePerUnit &#x3D; strike / 100 * contractSize. | 
**delivery_type** | **str** | How does the option settle. Only Cash is supported for a BondOption.                Supported string (enumeration) values are: [Cash, Physical]. | 
**exercise_dates** | **List[datetime]** | The exercise dates; exactly one entry, equal to the expiry date (European only in scope). | 
**exercise_type** | **str** | Type of optionality that is present. Only European is supported for a BondOption.                Supported string (enumeration) values are: [European, Bermudan, American]. | [optional] 
**expiry_date** | **datetime** | This is the date when the option expires, i.e. the LAST exercise date of the option.  The property is internal, we may change it in the future (think about Bermuda options). | 
**option_type** | **str** | Type of optionality for the option.                Supported string (enumeration) values are: [Call, Put]. | 
**premium** | [**Premium**](Premium.md) |  | [optional] 
**time_zone_conventions** | [**TimeZoneConventions**](TimeZoneConventions.md) |  | [optional] 
**trading_conventions** | [**TradingConventions**](TradingConventions.md) |  | [optional] 
**underlying** | [**LusidInstrument**](LusidInstrument.md) |  | 
**instrument_type** | **str** | Available values: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo, ToBeAnnounced, VolatilitySwap, ToBeAnnouncedOption, CommodityForward, BondOption. | 
## Example

```python
from lusid.models.bond_option import BondOption
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

start_date: datetime = # Replace with your value
dom_ccy: StrictStr = "example_dom_ccy"
strike: Union[StrictFloat, StrictInt] = # Replace with your value
contract_size: Union[StrictFloat, StrictInt] = # Replace with your value
delivery_type: StrictStr = "example_delivery_type"
exercise_dates: List[datetime] = # Replace with your value
exercise_type: Optional[StrictStr] = "example_exercise_type"
expiry_date: datetime = # Replace with your value
option_type: StrictStr = "example_option_type"
premium: Optional[Premium] = None
time_zone_conventions: Optional[TimeZoneConventions] = # Replace with your value
trading_conventions: Optional[TradingConventions] = # Replace with your value
underlying: LusidInstrument
instrument_type: StrictStr = "example_instrument_type"
bond_option_instance = BondOption(start_date=start_date, dom_ccy=dom_ccy, strike=strike, contract_size=contract_size, delivery_type=delivery_type, exercise_dates=exercise_dates, exercise_type=exercise_type, expiry_date=expiry_date, option_type=option_type, premium=premium, time_zone_conventions=time_zone_conventions, trading_conventions=trading_conventions, underlying=underlying, instrument_type=instrument_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

