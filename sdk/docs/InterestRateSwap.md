# InterestRateSwap

LUSID representation of an Interest Rate Swap, including:      * Vanilla (single currency fixed-float non-amortising)    * CrossCurrency (>1 currency is used by the swap legs)    * Basis (single currency, floating-floating legs of different tenors)    * Amortising (the swap has 1+ leg with amortised notional)                This instrument has multiple legs, to see how legs are used in LUSID see [knowledge base article KA-02252](https://support.lusid.com/knowledgebase/article/KA-02252).                | Leg Index | Leg Identifier | Description |  | --------- | -------------- | ----------- |  | 1 | Pay/Receive | Cash flows representing the pay/receive leg. |  | 2 | Receive/Pay | Cash flows representing the receive/pay leg. |  | 3 | AdditionalPayments | Cash flows relating to any additional payments (optional). |
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | The start date of the instrument. This is normally synonymous with the trade-date. | 
**maturity_date** | **datetime** | The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates that may well be observed or set prior to the maturity date, but refer to a termination date beyond it. | 
**is_non_deliverable** | **bool** | Is the contract an IRS of \&quot;Non-Deliverable\&quot; type, meaning a single payment in the settlement currency based on the difference between  the fixed and floating rates. | [optional] 
**legs** | [**List[InstrumentLeg]**](InstrumentLeg.md) | The set of instrument legs that define the swap instrument, these should be FloatingLeg or FixedLeg. | 
**settlement_ccy** | **str** | Settlement currency if IRS is non-deliverable. | [optional] 
**additional_payments** | [**List[AdditionalPayment]**](AdditionalPayment.md) | Optional additional payments at a given date e.g. to level off an uneven fixed-floating swap.  The dates must be distinct and either all payments are Pay or all payments are Receive. | [optional] 
**time_zone_conventions** | [**TimeZoneConventions**](TimeZoneConventions.md) |  | [optional] 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit | 
## Example

```python
from lusid.models.interest_rate_swap import InterestRateSwap
from typing import Any, Dict, List, Optional
from pydantic.v1 import Field, StrictBool, StrictStr, conlist, validator
from datetime import datetime
start_date: datetime = # Replace with your value
maturity_date: datetime = # Replace with your value
is_non_deliverable: Optional[StrictBool] = # Replace with your value
is_non_deliverable:Optional[StrictBool] = None
legs: conlist(InstrumentLeg) = # Replace with your value
settlement_ccy: Optional[StrictStr] = "example_settlement_ccy"
additional_payments: Optional[conlist(AdditionalPayment)] = # Replace with your value
time_zone_conventions: Optional[TimeZoneConventions] = # Replace with your value
instrument_type: StrictStr = "example_instrument_type"
interest_rate_swap_instance = InterestRateSwap(start_date=start_date, maturity_date=maturity_date, is_non_deliverable=is_non_deliverable, legs=legs, settlement_ccy=settlement_ccy, additional_payments=additional_payments, time_zone_conventions=time_zone_conventions, instrument_type=instrument_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

