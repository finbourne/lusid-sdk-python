# TermDeposit

LUSID representation of a Term Deposit.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | The start date of the instrument. This is normally synonymous with the trade-date. | 
**maturity_date** | **datetime** | The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates that may well be observed or set prior to the maturity date, but refer to a termination date beyond it. | 
**contract_size** | **float** | With an OTC we have the problem of multiple ways of booking a quantity.              e.g.              If buying a swap do you have a holding of size 1 of 100,000,000 notional swap or a holding of 100,000,000 size of 1 notional swap, or any combination that multiplies to 10^8.              When you get for a price for a &#39;unit swap&#39; what do you mean? The definition must be consistent across all quotes. This includes bonds which have a face value and              fx-forwards which often trade in standard contract sizes. When we look up a price, and there are no units, we are assuming it is a price for a contract size of 1.              The logical effect of this is that              instrument clean price &#x3D; contract size * quoted unit price              holding clean price    &#x3D; holding quantity * instrument clean price &#x3D; holding quantity * contract size * quoted unit price              In calculating accrued interest the same should hold.              NB: The real problem is that people store \&quot;prices\&quot; without complete units. Everything should really be \&quot;x ccy for n units\&quot;. Where the n is implicit the above has to hold. | 
**flow_convention** | [**FlowConventions**](FlowConventions.md) |  | 
**rate** | **float** | The fixed rate for the term deposit. Specified as a decimal, e.g 0.03 is meant to be 3% interest | 
**dom_ccy** | **str** | DomCcy of the TermDeposit. If provided, must match the currency of FlowConvention. | [optional] 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan | 

## Example

```python
from lusid.models.term_deposit import TermDeposit

# TODO update the JSON string below
json = "{}"
# create an instance of TermDeposit from a JSON string
term_deposit_instance = TermDeposit.from_json(json)
# print the JSON string representation of the object
print TermDeposit.to_json()

# convert the object into a dict
term_deposit_dict = term_deposit_instance.to_dict()
# create an instance of TermDeposit from a dict
term_deposit_form_dict = term_deposit.from_dict(term_deposit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


