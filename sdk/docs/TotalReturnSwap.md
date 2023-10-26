# TotalReturnSwap

A swap in which one party makes payments based on leg rates (fixed or floating) while the other party makes payments based on the return of an underlying instrument.  The underlying instrument can be provided as an inline economic definition or as a reference instrument pointing to an already upserted instrument.  A reference instrument in this case would consist of instrument scope, instrument id and instrument id type (ISIN, LUID etc.)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | The start date of the instrument. This is normally synonymous with the trade-date. | 
**maturity_date** | **datetime** | The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates that may well be observed or set prior to the maturity date, but refer to a termination date beyond it. | 
**payment_leg** | [**InstrumentLeg**](InstrumentLeg.md) |  | 
**underlying_leg** | [**UnderlyingLeg**](UnderlyingLeg.md) |  | 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg | 

## Example

```python
from lusid.models.total_return_swap import TotalReturnSwap

# TODO update the JSON string below
json = "{}"
# create an instance of TotalReturnSwap from a JSON string
total_return_swap_instance = TotalReturnSwap.from_json(json)
# print the JSON string representation of the object
print TotalReturnSwap.to_json()

# convert the object into a dict
total_return_swap_dict = total_return_swap_instance.to_dict()
# create an instance of TotalReturnSwap from a dict
total_return_swap_form_dict = total_return_swap.from_dict(total_return_swap_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


