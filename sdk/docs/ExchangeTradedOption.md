# ExchangeTradedOption

LUSID representation of an Exchange Traded Option.  Including, but not limited to, Equity Options, Bond Options, Index Options, Future Options, and Interest Rate Options.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | The start date of the instrument. This is normally synonymous with the trade-date. | 
**contract_details** | [**ExchangeTradedOptionContractDetails**](ExchangeTradedOptionContractDetails.md) |  | 
**contracts** | **float** | The number of contracts held. | 
**ref_spot_price** | **float** | The reference spot price for the option at which the contract was entered into. | 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit | 

## Example

```python
from lusid.models.exchange_traded_option import ExchangeTradedOption

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangeTradedOption from a JSON string
exchange_traded_option_instance = ExchangeTradedOption.from_json(json)
# print the JSON string representation of the object
print ExchangeTradedOption.to_json()

# convert the object into a dict
exchange_traded_option_dict = exchange_traded_option_instance.to_dict()
# create an instance of ExchangeTradedOption from a dict
exchange_traded_option_form_dict = exchange_traded_option.from_dict(exchange_traded_option_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


