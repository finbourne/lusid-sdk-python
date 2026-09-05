# CreditDefaultSwap

LUSID representation of a Credit Default Swap (CDS).                This instrument has multiple legs, to see how legs are used in LUSID see [knowledge base article KA-02252](https://support.lusid.com/knowledgebase/article/KA-02252).                | Leg Index | Leg Identifier | Description |  | --------- | -------------- | ----------- |  | 1 | ProtectionLeg | Cash flows occurring in the case of default. |  | 2 | PremiumLeg | The premium payments made by the protection buyer. |  | 3 | AdditionalPayments | Cash flows relating to any additional payments (optional). |
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ticker** | **str** | A ticker to uniquely specify the entity against which the CDS is written. Defaults to \&quot;DefaultCDSTicker\&quot;. | [optional] [default to 'DefaultCDSTicker']
**start_date** | **datetime** | The start date of the instrument. This is normally synonymous with the trade-date. | 
**maturity_date** | **datetime** | The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates that may well be observed or set prior to the maturity date, but refer to a termination date beyond it. | 
**flow_conventions** | [**CdsFlowConventions**](CdsFlowConventions.md) |  | [optional] 
**coupon_rate** | **float** | The coupon rate paid on each payment date of the premium leg as a fraction of 100 percent, e.g. \&quot;0.05\&quot; meaning 500 basis points or 5%.  For a standard corporate CDS (North American) this must be either 100bps or 500bps. | 
**convention_name** | [**FlowConventionName**](FlowConventionName.md) |  | [optional] 
**notional** | **float** | The notional protected by the Credit Default Swap | [optional] 
**is_non_standard** | **bool** | By default IsNonStandard is false, and the contract follows the IMM convention: the roll and payment  frequencies must be 3M or 6M, and the start and maturity dates are rolled onto IMM dates  (the 20th of March, June, September or December).  If IsNonStandard&#x3D;true, the premium schedule uses the stated start and maturity dates and any payment  frequency is accepted. The payment dates roll back from the maturity, so a term that is not a whole  number of payment periods has a short first period. | [optional] 
**protection_detail_specification** | [**CdsProtectionDetailSpecification**](CdsProtectionDetailSpecification.md) |  | [optional] 
**additional_payments** | [**List[AdditionalPayment]**](AdditionalPayment.md) | Optional additional payments at a given date e.g. to level off an uneven swap.  The dates must be distinct and either all payments are Pay or all payments are Receive. | [optional] 
**time_zone_conventions** | [**TimeZoneConventions**](TimeZoneConventions.md) |  | [optional] 
**instrument_type** | **str** | Available values: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo, ToBeAnnounced, VolatilitySwap, ToBeAnnouncedOption, CommodityForward, BondOption, CdsOption, CommodityCalendarSwap, BondForward, PreferredShare, CapitalInterest. | 
## Example

```python
from lusid.models.credit_default_swap import CreditDefaultSwap
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

ticker: Optional[StrictStr] = "example_ticker"
start_date: datetime = # Replace with your value
maturity_date: datetime = # Replace with your value
flow_conventions: Optional[CdsFlowConventions] = # Replace with your value
coupon_rate: Union[StrictFloat, StrictInt] = # Replace with your value
convention_name: Optional[FlowConventionName] = # Replace with your value
notional: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
is_non_standard: Optional[StrictBool] = # Replace with your value
is_non_standard:Optional[StrictBool] = None
protection_detail_specification: Optional[CdsProtectionDetailSpecification] = # Replace with your value
additional_payments: Optional[List[AdditionalPayment]] = # Replace with your value
time_zone_conventions: Optional[TimeZoneConventions] = # Replace with your value
instrument_type: StrictStr = "example_instrument_type"
credit_default_swap_instance = CreditDefaultSwap(ticker=ticker, start_date=start_date, maturity_date=maturity_date, flow_conventions=flow_conventions, coupon_rate=coupon_rate, convention_name=convention_name, notional=notional, is_non_standard=is_non_standard, protection_detail_specification=protection_detail_specification, additional_payments=additional_payments, time_zone_conventions=time_zone_conventions, instrument_type=instrument_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

