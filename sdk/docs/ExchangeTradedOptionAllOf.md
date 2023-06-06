# ExchangeTradedOptionAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | The start date of the instrument. This is normally synonymous with the trade-date. | 
**contract_details** | [**ExchangeTradedOptionContractDetails**](ExchangeTradedOptionContractDetails.md) |  | 
**contracts** | **float** | The number of contracts held. | 
**ref_spot_price** | **float** | The reference spot price for the option at which the contract was entered into. | 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan | 

## Example

```python
from lusid.models.exchange_traded_option_all_of import ExchangeTradedOptionAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangeTradedOptionAllOf from a JSON string
exchange_traded_option_all_of_instance = ExchangeTradedOptionAllOf.from_json(json)
# print the JSON string representation of the object
print ExchangeTradedOptionAllOf.to_json()

# convert the object into a dict
exchange_traded_option_all_of_dict = exchange_traded_option_all_of_instance.to_dict()
# create an instance of ExchangeTradedOptionAllOf from a dict
exchange_traded_option_all_of_form_dict = exchange_traded_option_all_of.from_dict(exchange_traded_option_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


