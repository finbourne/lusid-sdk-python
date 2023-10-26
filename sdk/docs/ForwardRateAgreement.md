# ForwardRateAgreement

LUSID representation of a Forward Rate Agreement.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | The settlement date of the FRA | 
**maturity_date** | **datetime** | The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates beyond their last payment date. | 
**dom_ccy** | **str** | The domestic currency of the instrument. | 
**fixing_date** | **datetime** | The date at which the rate to be paid, the reference rate, is confirmed/observed. | 
**fra_rate** | **float** | The rate at which the FRA is traded. | 
**notional** | **float** | The amount for which the FRA is traded. | 
**index_convention** | [**IndexConvention**](IndexConvention.md) |  | [optional] 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg | 

## Example

```python
from lusid.models.forward_rate_agreement import ForwardRateAgreement

# TODO update the JSON string below
json = "{}"
# create an instance of ForwardRateAgreement from a JSON string
forward_rate_agreement_instance = ForwardRateAgreement.from_json(json)
# print the JSON string representation of the object
print ForwardRateAgreement.to_json()

# convert the object into a dict
forward_rate_agreement_dict = forward_rate_agreement_instance.to_dict()
# create an instance of ForwardRateAgreement from a dict
forward_rate_agreement_form_dict = forward_rate_agreement.from_dict(forward_rate_agreement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


