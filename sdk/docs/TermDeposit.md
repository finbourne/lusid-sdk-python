# TermDeposit

LUSID representation of a Term Deposit.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | The start date of the instrument. For term deposits this is the start date of the interest calculation period. | 
**maturity_date** | **datetime** | The maturity date of the instrument. For term deposits this is the last date of the interest calculation period. | 
**contract_size** | **float** | The principal amount of the term deposit. | 
**flow_convention** | [**FlowConventions**](FlowConventions.md) |  | 
**rate** | **float** | The fixed rate for the term deposit. Specified as a decimal, e.g 0.03 is meant to be 3% interest | 
**dom_ccy** | **str** | The domestic currency of the instrument. This should be the same as the Currency set on the FlowConventions.  You do not need to populate this field for Term Deposits in LUSID as all functionality is driven by the Currency set on the FlowConventions.  LUSID will not store values saved on this field. | [optional] 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit | 

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
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


