# EquitySwap

LUSID representation of an Equity Swap.              This instrument has multiple legs, to see how legs are used in LUSID see [knowledge base article KA-02252](https://support.lusid.com/knowledgebase/article/KA-02252).              | Leg Index | Leg Identifier | Description | | --------- | -------------- | ----------- | | 1 | EquityLeg | Cash flows relating to the performance of the underlying equity. | | 2 | FundingLeg | The funding leg of the swap. | | 3 | EquityDividendLeg | Cash flows relating to dividend payments on the underlying equity (optional). | | 4 | AdditionalPayments | Cash flows relating to any additional payments (optional). |
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | The start date of the EquitySwap. | 
**maturity_date** | **datetime** | The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount. For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as Constant Maturity Swaps (CMS) often have sensitivities to rates that may well be observed or set prior to the maturity date, but refer to a termination date beyond it. | 
**code** | **str** | The code of the underlying. | 
**equity_flow_conventions** | [**FlowConventions**](FlowConventions.md) |  | 
**funding_leg** | [**InstrumentLeg**](InstrumentLeg.md) |  | 
**include_dividends** | **bool** | Dividend inclusion flag, if true dividends are included in the equity leg (total return). | 
**initial_price** | **float** | The initial equity price of the Equity Swap. | 
**notional_reset** | **bool** | Notional reset flag, if true the notional of the funding leg is reset at the start of every coupon to match the value of the equity leg (equity price at start of coupon times quantity). | 
**quantity** | **float** | The quantity or number of shares in the Equity Swap. | 
**underlying_identifier** | **str** | External market codes and identifiers for the EquitySwap, e.g. RIC.  Supported string (enumeration) values are: [LusidInstrumentId, Isin, Sedol, Cusip, ClientInternal, Figi, RIC, QuotePermId, REDCode, BBGId, ICECode]. | 
**equity_swap_dividend_payment_timing** | **str** | Determines how the payment of dividends is handled for the equity swap. Defaults to paying at the next Equity coupon date.              Supported string (enumeration) values are: [PayAtNextEquityCouponDate, PayAtMaturityOfSwap, PayAtNextFundingLegCouponDate, PayAtPaymentDateOfDividendEvent]. | [optional] 
**additional_payments** | [**List[AdditionalPayment]**](AdditionalPayment.md) | Optional additional payments at a given date e.g. to level off an uneven equity swap. The dates must be distinct and either all payments are Pay or all payments are Receive. | [optional] 
**time_zone_conventions** | [**TimeZoneConventions**](TimeZoneConventions.md) |  | [optional] 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo | 
## Example

```python
from lusid.models.equity_swap import EquitySwap
from typing import Any, Dict, List, Optional, Union
from pydantic.v1 import Field, StrictBool, StrictFloat, StrictInt, StrictStr, conlist, constr, validator
from datetime import datetime
start_date: datetime = # Replace with your value
maturity_date: datetime = # Replace with your value
code: StrictStr = "example_code"
equity_flow_conventions: FlowConventions = # Replace with your value
funding_leg: InstrumentLeg = # Replace with your value
include_dividends: StrictBool = # Replace with your value
include_dividends:StrictBool = True
initial_price: Union[StrictFloat, StrictInt] = # Replace with your value
notional_reset: StrictBool = # Replace with your value
notional_reset:StrictBool = True
quantity: Union[StrictFloat, StrictInt] = # Replace with your value
underlying_identifier: StrictStr = "example_underlying_identifier"
equity_swap_dividend_payment_timing: Optional[StrictStr] = "example_equity_swap_dividend_payment_timing"
additional_payments: Optional[conlist(AdditionalPayment)] = # Replace with your value
time_zone_conventions: Optional[TimeZoneConventions] = # Replace with your value
instrument_type: StrictStr = "example_instrument_type"
equity_swap_instance = EquitySwap(start_date=start_date, maturity_date=maturity_date, code=code, equity_flow_conventions=equity_flow_conventions, funding_leg=funding_leg, include_dividends=include_dividends, initial_price=initial_price, notional_reset=notional_reset, quantity=quantity, underlying_identifier=underlying_identifier, equity_swap_dividend_payment_timing=equity_swap_dividend_payment_timing, additional_payments=additional_payments, time_zone_conventions=time_zone_conventions, instrument_type=instrument_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

