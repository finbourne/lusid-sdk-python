# EquitySwap

LUSID representation of an Equity Swap.                This instrument has multiple legs, to see how legs are used in LUSID see https://support.lusid.com/knowledgebase/article/KA-02252.                | Leg Index | Leg Identifier | Description |  | --------- | -------------- | ----------- |  | 1 | EquityLeg | Cash flows relating to the performance of the underlying equity. |  | 2 | FundingLeg | The funding leg of the swap. |  | 3 | EquityDividendLeg | Cash flows relating to dividend payments on the underlying equity (optional). |

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | The start date of the EquitySwap. | 
**maturity_date** | **datetime** | The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates that may well be observed or set prior to the maturity date, but refer to a termination date beyond it. | 
**code** | **str** | The code of the underlying. | 
**equity_flow_conventions** | [**FlowConventions**](FlowConventions.md) |  | 
**funding_leg** | [**InstrumentLeg**](InstrumentLeg.md) |  | 
**include_dividends** | **bool** | Dividend inclusion flag, if true dividends are included in the equity leg (total return). | 
**initial_price** | **float** | The initial equity price of the Equity Swap. | 
**notional_reset** | **bool** | Notional reset flag, if true the notional of the funding leg is reset at the start of every  coupon to match the value of the equity leg (equity price at start of coupon times quantity). | 
**quantity** | **float** | The quantity or number of shares in the Equity Swap. | 
**underlying_identifier** | **str** | External market codes and identifiers for the EquitySwap, e.g. RIC.    Supported string (enumeration) values are: [LusidInstrumentId, Isin, Sedol, Cusip, ClientInternal, Figi, RIC, QuotePermId, REDCode, BBGId, ICECode]. | 
**equity_swap_dividend_payment_timing** | **str** | Determines how the payment of dividends is handled for the equity swap.  Defaults to paying at the next Equity coupon date.                Supported string (enumeration) values are: [PayAtNextEquityCouponDate, PayAtMaturityOfSwap, PayAtNextFundingLegCouponDate, PayAtPaymentDateOfDividendEvent]. | [optional] 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg | 

## Example

```python
from lusid.models.equity_swap import EquitySwap

# TODO update the JSON string below
json = "{}"
# create an instance of EquitySwap from a JSON string
equity_swap_instance = EquitySwap.from_json(json)
# print the JSON string representation of the object
print EquitySwap.to_json()

# convert the object into a dict
equity_swap_dict = equity_swap_instance.to_dict()
# create an instance of EquitySwap from a dict
equity_swap_form_dict = equity_swap.from_dict(equity_swap_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


