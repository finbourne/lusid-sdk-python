# FundShareClass

LUSID representation of a FundShareClass.  A ShareClass represents a pool of shares, held by investors, within a fund. A ShareClass can represent a differing investment approach by either Fees, Income, Currency Risk and Investor type.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**short_code** | **str** | A short identifier, unique across a single fund, usually made up of the ShareClass components. Eg \&quot;A Accumulation Euro Hedged Class\&quot; could become \&quot;A Acc H EUR\&quot;. | 
**fund_share_class_type** | **str** | The type of distribution that the ShareClass will calculate. Can be either &#39;Income&#39; or &#39;Accumulation&#39; - Income classes will pay out and Accumulation classes will retain their ShareClass attributable income.    Supported string (enumeration) values are: [Income, Accumulation]. | 
**distribution_payment_type** | **str** | The tax treatment applied to any distributions calculated within the ShareClass. Can be either &#39;Net&#39; (Distribution Calculated net of tax) or &#39;Gross&#39; (Distribution calculated gross of tax).    Supported string (enumeration) values are: [Gross, Net]. | 
**hedging** | **str** | A flag to indicate the ShareClass is operating currency hedging as a means to limit currency risk as part of it&#39;s investment strategy.    Supported string (enumeration) values are: [Invalid, None, ApplyHedging]. | 
**dom_ccy** | **str** | The domestic currency of the instrument. | 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass | 

## Example

```python
from lusid.models.fund_share_class import FundShareClass

# TODO update the JSON string below
json = "{}"
# create an instance of FundShareClass from a JSON string
fund_share_class_instance = FundShareClass.from_json(json)
# print the JSON string representation of the object
print FundShareClass.to_json()

# convert the object into a dict
fund_share_class_dict = fund_share_class_instance.to_dict()
# create an instance of FundShareClass from a dict
fund_share_class_form_dict = fund_share_class.from_dict(fund_share_class_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


