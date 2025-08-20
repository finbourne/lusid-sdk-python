# InflationSwap

LUSID representation of an Inflation Swap. The implementation supports the following swap types: * Zero Coupon inflation swap, with a single payment at maturity. * LPI Swap (capped and floored) * Year on Year inflation swap              This instrument has multiple legs, to see how legs are used in LUSID see [knowledge base article KA-02252](https://support.lusid.com/knowledgebase/article/KA-02252).              | Leg Index | Leg Identifier | Description | | --------- | -------------- | ----------- | | 1 | InflationLeg | Cash flows with a rate relating to an underlying inflation index. | | 2 | FixedLeg | Cash flows with a fixed rate. | | 3 | AdditionalPayments | Cash flows relating to any additional payments (optional). |
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | The start date of the instrument. This is normally synonymous with the trade-date. | 
**maturity_date** | **datetime** | The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount. For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as Constant Maturity Swaps (CMS) often have sensitivities to rates that may well be observed or set prior to the maturity date, but refer to a termination date beyond it. | 
**inflation_leg** | [**InflationLeg**](InflationLeg.md) |  | 
**fixed_leg** | [**FixedLeg**](FixedLeg.md) |  | 
**additional_payments** | [**List[AdditionalPayment]**](AdditionalPayment.md) | Optional additional payments at a given date e.g. to level off an uneven inflation swap. The dates must be distinct and either all payments are Pay or all payments are Receive. | [optional] 
**time_zone_conventions** | [**TimeZoneConventions**](TimeZoneConventions.md) |  | [optional] 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo | 
## Example

```python
from lusid.models.inflation_swap import InflationSwap
from typing import Any, Dict, List, Optional
from pydantic.v1 import Field, StrictStr, conlist, validator
from datetime import datetime
start_date: datetime = # Replace with your value
maturity_date: datetime = # Replace with your value
inflation_leg: InflationLeg = # Replace with your value
fixed_leg: FixedLeg = # Replace with your value
additional_payments: Optional[conlist(AdditionalPayment)] = # Replace with your value
time_zone_conventions: Optional[TimeZoneConventions] = # Replace with your value
instrument_type: StrictStr = "example_instrument_type"
inflation_swap_instance = InflationSwap(start_date=start_date, maturity_date=maturity_date, inflation_leg=inflation_leg, fixed_leg=fixed_leg, additional_payments=additional_payments, time_zone_conventions=time_zone_conventions, instrument_type=instrument_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

