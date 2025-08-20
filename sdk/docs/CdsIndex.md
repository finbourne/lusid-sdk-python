# CdsIndex

LUSID representation of a Credit Default Swap Index (CDX).              This instrument has multiple legs, to see how legs are used in LUSID see [knowledge base article KA-02252](https://support.lusid.com/knowledgebase/article/KA-02252).              | Leg Index | Leg Identifier | Description | | --------- | -------------- | ----------- | | 1 | ProtectionLeg | Payments made by the protection seller in the case of default across all CDS instruments in the index. | | 2 | PremiumLeg | The premium payments made by the protection buyer across all CDS instruments in the index. | | 3 | AdditionalPayments | Cash flows relating to any additional payments (optional). |
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | The start date of the instrument. This is normally synonymous with the trade-date. | 
**maturity_date** | **datetime** | The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount. For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as Constant Maturity Swaps (CMS) often have sensitivities to rates that may well be observed or set prior to the maturity date, but refer to a termination date beyond it. | 
**flow_conventions** | [**CdsFlowConventions**](CdsFlowConventions.md) |  | [optional] 
**coupon_rate** | **float** | The coupon rate paid on each payment date of the premium leg as a fraction of 100 percent, e.g. \&quot;0.05\&quot; meaning 500 basis points or 5%. For a standard corporate CDS (North American) this must be either 100bps or 500bps. | 
**identifiers** | **Dict[str, str]** | External market codes and identifiers for the cds index, e.g. a RED code, BBG ID or ICE code. | 
**basket** | [**Basket**](Basket.md) |  | [optional] 
**convention_name** | [**FlowConventionName**](FlowConventionName.md) |  | [optional] 
**notional** | **float** | The notional quantity that applies to both the premium and protection legs. | 
**additional_payments** | [**List[AdditionalPayment]**](AdditionalPayment.md) | Optional additional payments at a given date e.g. to level off an uneven swap. The dates must be distinct and either all payments are Pay or all payments are Receive. | [optional] 
**time_zone_conventions** | [**TimeZoneConventions**](TimeZoneConventions.md) |  | [optional] 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo | 
## Example

```python
from lusid.models.cds_index import CdsIndex
from typing import Any, Dict, List, Optional, Union
from pydantic.v1 import Field, StrictFloat, StrictInt, StrictStr, conlist, validator
from datetime import datetime
start_date: datetime = # Replace with your value
maturity_date: datetime = # Replace with your value
flow_conventions: Optional[CdsFlowConventions] = # Replace with your value
coupon_rate: Union[StrictFloat, StrictInt] = # Replace with your value
identifiers: Dict[str, StrictStr] = # Replace with your value
basket: Optional[Basket] = None
convention_name: Optional[FlowConventionName] = # Replace with your value
notional: Union[StrictFloat, StrictInt] = # Replace with your value
additional_payments: Optional[conlist(AdditionalPayment)] = # Replace with your value
time_zone_conventions: Optional[TimeZoneConventions] = # Replace with your value
instrument_type: StrictStr = "example_instrument_type"
cds_index_instance = CdsIndex(start_date=start_date, maturity_date=maturity_date, flow_conventions=flow_conventions, coupon_rate=coupon_rate, identifiers=identifiers, basket=basket, convention_name=convention_name, notional=notional, additional_payments=additional_payments, time_zone_conventions=time_zone_conventions, instrument_type=instrument_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

