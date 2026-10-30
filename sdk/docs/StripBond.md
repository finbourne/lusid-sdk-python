# StripBond

A stripped bond: an entitlement to one side of a mastered parent bond's cash flows. An interest-only strip  receives the interest the parent pays, on a notional that runs down with the parent's principal; a  principal-only strip receives the parent's principal and none of its interest. The strip carries no schedule,  coupon or conventions of its own: it points at the parent through a MasteredInstrument and reads the parent's  cash flows, pool factor, dates and conventions from the parent's live definition, so a re-upsert of the parent  reaches every strip on it. One unit of a strip is one unit of the parent's original face.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_negative_yield** | **bool** | Whether a negative effective yield books negative income. Null means false: a negative effective yield is  then applied as zero, so the whole receipt returns capital. | [optional] 
**strip_type** | **str** | Which side of the parent&#39;s flows the strip receives: InterestOnly receives the parent&#39;s interest,  PrincipalOnly receives the parent&#39;s principal.                Supported string (enumeration) values are: [InterestOnly, PrincipalOnly]. Available values: InterestOnly, PrincipalOnly. | 
**trading_conventions** | [**TradingConventions**](TradingConventions.md) |  | [optional] 
**underlying** | [**LusidInstrument**](LusidInstrument.md) |  | 
**instrument_type** | **str** | Available values: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo, ToBeAnnounced, VolatilitySwap, ToBeAnnouncedOption, CommodityForward, BondOption, CdsOption, CommodityCalendarSwap, BondForward, PreferredShare, CapitalInterest, WholeLoanFacility, StripBond. | 
## Example

```python
from lusid.models.strip_bond import StripBond
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

allow_negative_yield: Optional[StrictBool] = # Replace with your value
allow_negative_yield:Optional[StrictBool] = None
strip_type: StrictStr = "example_strip_type"
trading_conventions: Optional[TradingConventions] = # Replace with your value
underlying: LusidInstrument
instrument_type: StrictStr = "example_instrument_type"
strip_bond_instance = StripBond(allow_negative_yield=allow_negative_yield, strip_type=strip_type, trading_conventions=trading_conventions, underlying=underlying, instrument_type=instrument_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

