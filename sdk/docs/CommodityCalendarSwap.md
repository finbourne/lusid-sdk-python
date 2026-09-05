# CommodityCalendarSwap

LUSID representation of an OTC bilateral commodity calendar swap.  The swap is a strip of periodic commodity forwards struck at a single strike, cash-settled at each  period end against a calendar-average commodity price, with the position amortising as each period  settles. Its present value is Quantity x Price, where the price is supplied externally pre-netted  (the calendar average minus strike) via the quote store. LUSID calculates no analytics for this  instrument, and it can only be priced by lookup pricing. The periodic settlement schedule is  currently stored and validated only; only the maturity lifecycle event is generated.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dom_ccy** | **str** | The domestic currency of the instrument. | 
**strike** | **float** | Agreed price per unit at trade inception. Reference only - not used in the market value  calculation, which consumes the pre-netted price from the quote store. | [optional] 
**commodity_calendar_schedule** | [**CommodityCalendarSchedule**](CommodityCalendarSchedule.md) |  | 
**delivery_type** | **str** | Whether the swap settles in cash or through physical delivery of the underlying.  Only cash settlement is supported.                Supported string (enumeration) values are: [Cash, Physical]. Available values: Cash, Physical. | 
**quantity_per_period** | **float** | The notional commodity quantity referenced by each settlement period. The initial holding is  this quantity multiplied by the number of periods, stepping down by this quantity as each  period settles. | 
**underlying** | [**LusidInstrument**](LusidInstrument.md) |  | [optional] 
**instrument_type** | **str** | Available values: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo, ToBeAnnounced, VolatilitySwap, ToBeAnnouncedOption, CommodityForward, BondOption, CdsOption, CommodityCalendarSwap, BondForward, PreferredShare, CapitalInterest. | 
## Example

```python
from lusid.models.commodity_calendar_swap import CommodityCalendarSwap
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

dom_ccy: StrictStr = "example_dom_ccy"
strike: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
commodity_calendar_schedule: CommodityCalendarSchedule = # Replace with your value
delivery_type: StrictStr = "example_delivery_type"
quantity_per_period: Union[StrictFloat, StrictInt] = # Replace with your value
underlying: Optional[LusidInstrument] = None
instrument_type: StrictStr = "example_instrument_type"
commodity_calendar_swap_instance = CommodityCalendarSwap(dom_ccy=dom_ccy, strike=strike, commodity_calendar_schedule=commodity_calendar_schedule, delivery_type=delivery_type, quantity_per_period=quantity_per_period, underlying=underlying, instrument_type=instrument_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

