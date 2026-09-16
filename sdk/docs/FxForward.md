# FxForward

LUSID representation of an FX Forward.  Including FX Spot and Non-Deliverable Forwards.                This instrument has multiple legs, to see how legs are used in LUSID see [How does LUSID handle instrument legs?](https://support.lusid.com/docs/how-does-lusid-handle-instrument-legs).                | Leg Index | Leg Identifier | Description |  | --------- | -------------- | ----------- |  | 1 | DomesticLeg | Cash flows in the domestic currency of the forward. |  | 2 | ForeignLeg | Cash flows in the foreign currency of the forward (not present for non-deliverable forwards). |
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | The start date of the instrument. This is normally synonymous with the trade-date. | 
**maturity_date** | **datetime** | The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates that may well be observed or set prior to the maturity date, but refer to a termination date beyond it. | 
**dom_amount** | **float** | The amount that is to be paid in the domestic currency on the maturity date.  Required unless isPooled is set. On a pooled FX forward the domestic amount is the contract size and  not a traded amount: leave it absent and it is populated as one, so that holding units are amounts of  the domestic currency. | [optional] 
**dom_ccy** | **str** | The domestic currency of the instrument. | 
**fgn_amount** | **float** | The amount that is to be paid in the foreign currency on the maturity date.  Required unless isPooled is set. On a pooled FX forward it must be absent or zero, because the whole  foreign consideration is carried by the transactions booked against the pool. | [optional] 
**fgn_ccy** | **str** | The foreign (other) currency of the instrument. In the NDF case, only payments are made in the domestic currency.  For the outright forward, currencies are exchanged. | 
**ref_spot_rate** | **float** | The reference Fx Spot rate for currency pair Foreign-Domestic that was seen on the trade start date (time). | [optional] 
**is_ndf** | **bool** | Is the contract an Fx-Forward of \&quot;Non-Deliverable\&quot; type, meaning a single payment in the domestic currency based on the change in fx-rate vs  a reference rate is used.  Defaults to false if not set. | [optional] 
**fixing_date** | **datetime** | The fixing date. | [optional] 
**settlement_ccy** | **str** | The settlement currency.  If provided, present value will be calculated in settlement currency, otherwise the domestic currency. Applies only to non-deliverable FX Forwards. | [optional] 
**booked_as_spot** | **bool** | Boolean flag for FX Forward transactions booked with Spot settlement. This will default to False if not provided.  For information purposes only, this does not impact LUSID valuation, analytics, cashflows or events, but may be used by third party vendors. | [optional] 
**time_zone_conventions** | [**TimeZoneConventions**](TimeZoneConventions.md) |  | [optional] 
**is_pooled** | **bool** | Declares the contract to be a pool, carrying no traded amounts of its own. A pool is defined once for a  currency pair and maturity date and traded repeatedly at different rates, so the traded amounts are carried  by the transactions booked against it rather than by the instrument. The domestic amount of a pool is  therefore the contract size and not a traded amount, and is pinned to one so that holding units are amounts  of the domestic currency; the foreign amount and the reference spot rate must be absent, because the whole  foreign consideration is carried by the transaction.                Orientation is part of a pool&#39;s identity: the domestic currency is the unit currency and the foreign  currency the consideration currency, so a USD/JPY pool and a JPY/USD pool are distinct instruments, and  transactions must be booked in the pool&#39;s own direction (transaction currency equal to the domestic  currency, settlement currency equal to the foreign currency). This will default to False if not provided. | [optional] 
**instrument_type** | **str** | Available values: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo, ToBeAnnounced, VolatilitySwap, ToBeAnnouncedOption, CommodityForward, BondOption, CdsOption, CommodityCalendarSwap, BondForward, PreferredShare, CapitalInterest. | 
## Example

```python
from lusid.models.fx_forward import FxForward
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

start_date: datetime = # Replace with your value
maturity_date: datetime = # Replace with your value
dom_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
dom_ccy: StrictStr = "example_dom_ccy"
fgn_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
fgn_ccy: StrictStr = "example_fgn_ccy"
ref_spot_rate: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
is_ndf: Optional[StrictBool] = # Replace with your value
is_ndf:Optional[StrictBool] = None
fixing_date: Optional[datetime] = # Replace with your value
settlement_ccy: Optional[StrictStr] = "example_settlement_ccy"
booked_as_spot: Optional[StrictBool] = # Replace with your value
booked_as_spot:Optional[StrictBool] = None
time_zone_conventions: Optional[TimeZoneConventions] = # Replace with your value
is_pooled: Optional[StrictBool] = # Replace with your value
is_pooled:Optional[StrictBool] = None
instrument_type: StrictStr = "example_instrument_type"
fx_forward_instance = FxForward(start_date=start_date, maturity_date=maturity_date, dom_amount=dom_amount, dom_ccy=dom_ccy, fgn_amount=fgn_amount, fgn_ccy=fgn_ccy, ref_spot_rate=ref_spot_rate, is_ndf=is_ndf, fixing_date=fixing_date, settlement_ccy=settlement_ccy, booked_as_spot=booked_as_spot, time_zone_conventions=time_zone_conventions, is_pooled=is_pooled, instrument_type=instrument_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

