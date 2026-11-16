# InflationSwap

LUSID representation of an Inflation Swap.  The implementation supports the following swap types:  * Zero Coupon inflation swap, with a single payment at maturity.  * LPI Swap (capped and floored)  * Year on Year inflation swap                This instrument has multiple legs, to see how legs are used in LUSID see [How does LUSID handle instrument legs?](https://support.lusid.com/docs/how-does-lusid-handle-instrument-legs).                | Leg Index | Leg Identifier | Description |  | --------- | -------------- | ----------- |  | 1 | InflationLeg | Cash flows with a rate relating to an underlying inflation index. |  | 2 | FixedLeg | Cash flows with a fixed rate. |  | 3 | AdditionalPayments | Cash flows relating to any additional payments (optional). |                With `legs`, the legs are in the order given and identified as InflationLeg, FixedLeg or FloatingLeg, so a  linker asset swap, a year-on-year or LPI swap against a floating leg, an income swap or a cross-currency  proceeds asset swap books as one instrument. The `inflationLeg` and `fixedLeg` fields remain for the original  shape and cannot be combined with `legs`.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | The start date of the instrument. This is normally synonymous with the trade-date. | 
**maturity_date** | **datetime** | The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates that may well be observed or set prior to the maturity date, but refer to a termination date beyond it. | 
**inflation_leg** | [**InflationLeg**](InflationLeg.md) |  | [optional] 
**fixed_leg** | [**FixedLeg**](FixedLeg.md) |  | [optional] 
**additional_payments** | [**List[AdditionalPayment]**](AdditionalPayment.md) | Optional additional payments at a given date e.g. to level off an uneven inflation swap.  The dates must be distinct and either all payments are Pay or all payments are Receive. | [optional] 
**time_zone_conventions** | [**TimeZoneConventions**](TimeZoneConventions.md) |  | [optional] 
**legs** | [**List[LusidInstrument]**](LusidInstrument.md) | The legs of the swap: exactly two, exactly one of them an InflationLeg and the other a FixedLeg or a  FloatingLeg, one paid and one received, each starting on or after the swap and maturing on or before it.  The legs may be in different currencies; the first leg&#39;s currency is the swap&#39;s domestic currency.  Not set together with InflationLeg and FixedLeg. In this shape capRate and floorRate are accepted only on  a YearOnYear inflation leg. | [optional] 
**instrument_type** | **str** | Available values: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo, ToBeAnnounced, VolatilitySwap, ToBeAnnouncedOption, CommodityForward, BondOption, CdsOption, CommodityCalendarSwap, BondForward, PreferredShare, CapitalInterest, WholeLoanFacility, StripBond. | 
## Example

```python
from lusid.models.inflation_swap import InflationSwap
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

start_date: datetime = # Replace with your value
maturity_date: datetime = # Replace with your value
inflation_leg: Optional[InflationLeg] = # Replace with your value
fixed_leg: Optional[FixedLeg] = # Replace with your value
additional_payments: Optional[List[AdditionalPayment]] = # Replace with your value
time_zone_conventions: Optional[TimeZoneConventions] = # Replace with your value
legs: Optional[List[LusidInstrument]] = # Replace with your value
instrument_type: StrictStr = "example_instrument_type"
inflation_swap_instance = InflationSwap(start_date=start_date, maturity_date=maturity_date, inflation_leg=inflation_leg, fixed_leg=fixed_leg, additional_payments=additional_payments, time_zone_conventions=time_zone_conventions, legs=legs, instrument_type=instrument_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

