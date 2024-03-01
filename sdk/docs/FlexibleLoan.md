# FlexibleLoan

LUSID flexible loan instrument. Represents the basic building block of a more complex loan structure that  can handle deferred interest payments.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | The start date of the instrument. This is normally synonymous with the trade-date. | 
**maturity_date** | **datetime** | The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates that may well be observed or set prior to the maturity date, but refer to a termination date beyond it. | 
**dom_ccy** | **str** | The domestic currency of the instrument. | 
**schedules** | [**List[Schedule]**](Schedule.md) | Repayment schedules for the loan. | 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan | 

## Example

```python
from lusid.models.flexible_loan import FlexibleLoan

# TODO update the JSON string below
json = "{}"
# create an instance of FlexibleLoan from a JSON string
flexible_loan_instance = FlexibleLoan.from_json(json)
# print the JSON string representation of the object
print FlexibleLoan.to_json()

# convert the object into a dict
flexible_loan_dict = flexible_loan_instance.to_dict()
# create an instance of FlexibleLoan from a dict
flexible_loan_form_dict = flexible_loan.from_dict(flexible_loan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


